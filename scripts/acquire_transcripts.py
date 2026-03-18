#!/usr/bin/env python3
"""
Acquire transcripts for a list of episode IDs.

For each episode, tries in order:
  1. Disk (already exists)
  2. cast2md DB
  3. Free download (Pocket Casts / Podcast 2.0), polls 60s
  4. AssemblyAI (last resort, costs money)

Usage:
    python scripts/acquire_transcripts.py [--no-assemblyai] <episode_id> [episode_id ...]

Requires ASSEMBLYAI_API_KEY in environment (for step 4).

Output (JSON to stdout):
    {
        "<episode_id>": {
            "status": "disk|db|pocketcasts|assemblyai|failed",
            "path": "data/podcasts/transcripts/...",
            "chars": 12345
        },
        ...
    }
"""

import sys
import argparse
import json
import os
import re
import html
import time
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

API_BASE = "http://127.0.0.1:8000"
WORKSPACE = Path("/home/kayshway/podcasts")
TRANSCRIPTS_DIR = WORKSPACE / "data/podcasts/transcripts"
POLL_INTERVAL = 5
POLL_TIMEOUT = 60


def api_get(path: str) -> dict:
    req = urllib.request.Request(f"{API_BASE}{path}")
    resp = urllib.request.urlopen(req, timeout=30)
    return json.loads(resp.read())


def api_post(path: str) -> dict:
    req = urllib.request.Request(f"{API_BASE}{path}", method="POST")
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        return json.loads(resp.read())
    except Exception:
        return {}


def sanitize_title(title: str) -> str:
    title = html.unescape(title)
    title = title.replace(" ", "_")
    for ch in r'/\:*?"<>|':
        title = title.replace(ch, "")
    return title


def transcript_path(ep: dict) -> Path:
    """Find existing transcript dir or derive a new path."""
    feed_title = ep["feed_title"]
    date = ep["published_at"][:10]
    title_slug = sanitize_title(ep["title"])
    filename = f"{date}_{title_slug}.md"

    # Check existing dirs (underscored or spaced)
    spaced = TRANSCRIPTS_DIR / feed_title
    underscored = TRANSCRIPTS_DIR / feed_title.replace(" ", "_")

    if underscored.exists():
        return underscored / filename
    elif spaced.exists():
        return spaced / filename
    else:
        # Default to underscored for new dirs
        return underscored / filename


def get_db_transcript(ep_id: int) -> str | None:
    try:
        data = api_get(f"/api/episodes/{ep_id}/transcript/section?duration=99999")
        t = data.get("transcript", "")
        return t if t and t.strip() else None
    except Exception:
        return None


def save_transcript(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def get_feed_title(feed_id: int) -> str:
    try:
        data = api_get(f"/api/feeds/{feed_id}")
        return data.get("display_title") or data.get("title", str(feed_id))
    except Exception:
        return str(feed_id)


def acquire_one(ep_id: int) -> tuple[int, dict]:
    ep = api_get(f"/api/episodes/{ep_id}")
    # Enrich with feed_title if missing
    if "feed_title" not in ep:
        ep["feed_title"] = get_feed_title(ep["feed_id"])
    path = transcript_path(ep)

    # 1. Disk
    if path.exists() and path.stat().st_size > 0:
        return ep_id, {"status": "disk", "path": str(path.relative_to(WORKSPACE)), "chars": path.stat().st_size}

    # 2. DB
    text = get_db_transcript(ep_id)
    if text:
        save_transcript(path, text)
        return ep_id, {"status": "db", "path": str(path.relative_to(WORKSPACE)), "chars": len(text)}

    # 3. Free download — fire request, will poll below
    api_post(f"/api/queue/episodes/{ep_id}/transcript-download")
    return ep_id, {"status": "pending", "path": str(path.relative_to(WORKSPACE)), "ep": ep}


def poll_pending(pending: dict[int, dict], timeout: int = POLL_TIMEOUT) -> dict[int, dict]:
    """Poll pending episodes until transcripts arrive or timeout."""
    results = {}
    deadline = time.time() + timeout
    remaining = dict(pending)

    while remaining and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        for ep_id in list(remaining.keys()):
            info = remaining[ep_id]
            text = get_db_transcript(ep_id)
            if text:
                path = Path(WORKSPACE / info["path"])
                save_transcript(path, text)
                results[ep_id] = {"status": "pocketcasts", "path": info["path"], "chars": len(text)}
                del remaining[ep_id]

    return results, remaining  # remaining = still no transcript after timeout


def assemblyai_transcribe(ep_id: int, info: dict) -> tuple[int, dict]:
    """Fall back to AssemblyAI for an episode."""
    ep = info.get("ep", api_get(f"/api/episodes/{ep_id}"))
    audio_url = ep.get("audio_url", "")
    path_str = info["path"]
    output_path = WORKSPACE / path_str

    if not audio_url:
        return ep_id, {"status": "failed", "path": path_str, "error": "no audio_url"}

    env = os.environ.copy()
    result = subprocess.run(
        [str(WORKSPACE / ".venv/bin/python"), str(WORKSPACE / "scripts/transcribe_assemblyai.py"),
         audio_url, str(output_path)],
        capture_output=True, text=True, timeout=60 * 50, env=env,
        cwd=str(WORKSPACE),
    )

    if result.returncode == 0 and output_path.exists() and output_path.stat().st_size > 0:
        return ep_id, {"status": "assemblyai", "path": path_str, "chars": output_path.stat().st_size}
    else:
        return ep_id, {"status": "failed", "path": path_str, "error": result.stderr[-200:]}


def main():
    parser = argparse.ArgumentParser(description="Acquire transcripts for episodes")
    parser.add_argument("episode_ids", nargs="+", type=int, help="Episode IDs to process")
    parser.add_argument("--no-assemblyai", action="store_true",
                        help="Skip AssemblyAI fallback (only use free sources)")
    args = parser.parse_args()
    episode_ids = args.episode_ids

    results = {}
    pending = {}

    # Phase 1+2+3-fire: disk, DB, queue free download
    print(f"Checking {len(episode_ids)} episodes (disk + DB)...", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(acquire_one, eid): eid for eid in episode_ids}
        for future in as_completed(futures):
            ep_id, info = future.result()
            if info["status"] == "pending":
                pending[ep_id] = info
            else:
                results[ep_id] = info

    # Phase 3-poll: wait up to 60s for free transcripts
    if pending:
        print(f"Polling {len(pending)} free downloads (up to {POLL_TIMEOUT}s)...", file=sys.stderr)
        got, still_pending = poll_pending(pending)
        results.update(got)
    else:
        still_pending = {}

    # Phase 4: AssemblyAI for anything still missing (unless --no-assemblyai)
    if still_pending:
        if args.no_assemblyai:
            print(f"Skipping AssemblyAI for {len(still_pending)} episodes (--no-assemblyai)", file=sys.stderr)
            for ep_id, info in still_pending.items():
                results[ep_id] = {"status": "skipped", "path": info["path"], "reason": "no-assemblyai flag set"}
        else:
            print(f"AssemblyAI fallback for {len(still_pending)} episodes...", file=sys.stderr)
            with ThreadPoolExecutor(max_workers=4) as ex:
                futures = {ex.submit(assemblyai_transcribe, eid, info): eid
                           for eid, info in still_pending.items()}
                for future in as_completed(futures):
                    ep_id, info = future.result()
                    results[ep_id] = info

    print(json.dumps({str(k): v for k, v in results.items()}))


if __name__ == "__main__":
    main()
