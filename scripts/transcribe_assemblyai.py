"""Transcribe an audio file or URL via AssemblyAI REST API.

Usage:
    python scripts/transcribe_assemblyai.py <audio_path_or_url> <output_path>

Requires ASSEMBLYAI_API_KEY in the environment.
Accepts a local file path OR a URL. If given a URL, downloads the audio first
with a browser user-agent (some podcast CDNs reject bare requests).
Uploads to AssemblyAI, requests transcription with universal-2, polls until
complete, and writes the plain-text transcript to output_path.
"""

import os
import sys
import tempfile
import time
from pathlib import Path
from urllib.parse import urlparse

import httpx

API_KEY = os.environ.get("ASSEMBLYAI_API_KEY", "")
if not API_KEY:
    print("ERROR: ASSEMBLYAI_API_KEY not set. Run: source .env", file=sys.stderr)
    sys.exit(1)
BASE = "https://api.assemblyai.com/v2"
HEADERS = {"authorization": API_KEY, "content-type": "application/json"}
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
MAX_RETRIES = 3
POLL_INTERVAL_SECONDS = 5
POLL_TIMEOUT_SECONDS = 60 * 45


def _is_url(s: str) -> bool:
    return s.startswith("http://") or s.startswith("https://")


def _download(url: str) -> Path:
    """Download a URL to a temp file, return the path."""
    print(f"Downloading audio from URL...", file=sys.stderr, flush=True)
    with httpx.stream("GET", url, headers={"User-Agent": USER_AGENT}, follow_redirects=True, timeout=300.0) as resp:
        resp.raise_for_status()
        suffix = Path(urlparse(url).path).suffix or ".mp3"
        tmp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
        for chunk in resp.iter_bytes(chunk_size=65536):
            tmp.write(chunk)
        tmp.close()
        size_mb = Path(tmp.name).stat().st_size / 1024 / 1024
        print(f"Downloaded {size_mb:.1f}MB -> {tmp.name}", file=sys.stderr, flush=True)
        return Path(tmp.name)


def _upload(audio_path: Path) -> str:
    """Upload an audio file to AssemblyAI, return the upload URL. Retries on failure."""
    size_mb = audio_path.stat().st_size / 1024 / 1024
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"Uploading {audio_path.name} ({size_mb:.1f}MB)...", file=sys.stderr, flush=True)
            with open(audio_path, "rb") as f:
                resp = httpx.post(
                    f"{BASE}/upload",
                    headers={"authorization": API_KEY},
                    content=f,
                    timeout=600.0,
                )
                resp.raise_for_status()
            return resp.json()["upload_url"]
        except (httpx.HTTPError, KeyError) as e:
            if attempt == MAX_RETRIES:
                raise
            wait = 5 * attempt
            print(f"Upload failed ({e}), retrying in {wait}s...", file=sys.stderr, flush=True)
            time.sleep(wait)


def _start_transcript(upload_url: str) -> str:
    """Create a transcript job and return transcript_id. Retries on transient failures."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = httpx.post(
                f"{BASE}/transcript",
                headers=HEADERS,
                json={
                    "audio_url": upload_url,
                    "language_code": "en",
                    "speech_models": ["universal-2"],
                },
                timeout=60.0,
            )
            resp.raise_for_status()
            return resp.json()["id"]
        except (httpx.HTTPError, KeyError) as e:
            if attempt == MAX_RETRIES:
                raise
            wait = 5 * attempt
            print(
                f"Transcript create failed ({e}), retrying in {wait}s...",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(wait)


def transcribe(source: str, output_path: Path) -> None:
    tmp_file = None
    try:
        if output_path.exists() and output_path.stat().st_size > 0:
            print(f"Cache hit: {output_path} already exists, skipping transcription.", file=sys.stderr)
            return

        if _is_url(source):
            audio_path = _download(source)
            tmp_file = audio_path
        else:
            audio_path = Path(source)
            if not audio_path.exists():
                print(f"ERROR: File not found: {audio_path}", file=sys.stderr)
                sys.exit(1)

        upload_url = _upload(audio_path)
        print("Uploaded.", file=sys.stderr, flush=True)

        transcript_id = _start_transcript(upload_url)
        print(f"Job {transcript_id} queued, polling...", file=sys.stderr, flush=True)

        started_at = time.time()
        while True:
            if time.time() - started_at > POLL_TIMEOUT_SECONDS:
                print(
                    f"ERROR: polling timed out after {POLL_TIMEOUT_SECONDS}s for job {transcript_id}",
                    file=sys.stderr,
                )
                sys.exit(1)

            resp = httpx.get(
                f"{BASE}/transcript/{transcript_id}",
                headers=HEADERS,
                timeout=60.0,
            )
            resp.raise_for_status()
            data = resp.json()
            status = data["status"]

            if status == "completed":
                break
            if status == "error":
                print(f"ERROR: {data.get('error')}", file=sys.stderr)
                sys.exit(1)

            print(f"  status: {status}...", file=sys.stderr, flush=True)
            time.sleep(POLL_INTERVAL_SECONDS)

        try:
            para_resp = httpx.get(
                f"{BASE}/transcript/{transcript_id}/paragraphs",
                headers=HEADERS,
                timeout=60.0,
            )
            para_resp.raise_for_status()
            paragraphs = para_resp.json().get("paragraphs", [])
            text = "\n\n".join(p["text"] for p in paragraphs)
        except Exception:
            text = data.get("text", "")

        if not text or not text.strip():
            print("ERROR: AssemblyAI returned empty transcript.", file=sys.stderr)
            sys.exit(1)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
        print(f"Done: {len(text)} chars -> {output_path}", file=sys.stderr)
    finally:
        if tmp_file and tmp_file.exists():
            tmp_file.unlink()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <audio_path_or_url> <output_path>", file=sys.stderr)
        sys.exit(1)
    transcribe(sys.argv[1], Path(sys.argv[2]))
