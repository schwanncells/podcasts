#!/usr/bin/env python3
"""
Discover new podcast episodes and print candidates for processing.

Usage:
    python scripts/discover_candidates.py <days> [--refresh]

Args:
    days       Number of days to look back (e.g. 3 for "since Friday")
    --refresh  Refresh active feeds before querying (default: True)
    --no-refresh  Skip feed refresh (faster if feeds were refreshed recently)

Output (JSON to stdout):
    {
        "total": N,
        "by_podcast": {"Podcast Name": [episode, ...]},
        "episodes": [...]
    }

Each episode:
    {id, feed_id, feed_title, title, published_at, status, has_transcript, summary_exists}
"""

import sys
import json
import os
import re
import subprocess
import concurrent.futures
import html
import urllib.request
import urllib.error
import math
from datetime import datetime, timezone
from pathlib import Path

API_BASE = "http://127.0.0.1:8000"
WORKSPACE = Path("/home/kayshway/podcasts")
SUMMARIES_DIR = WORKSPACE / "data/podcasts/summaries"
TRANSCRIPTS_DIR = WORKSPACE / "data/podcasts/transcripts"
SUMMARIZED_IDS_FILE = WORKSPACE / "data/summarized_episodes.json"


def _load_summarized_ids() -> set[int]:
    """Load the set of already-summarized episode IDs from the tracking file."""
    try:
        if SUMMARIZED_IDS_FILE.exists():
            with open(SUMMARIZED_IDS_FILE) as f:
                data = json.load(f)
            return {int(x) for x in data.get("episode_ids", [])}
    except Exception as e:
        print(f"Warning: could not load summarized_episodes.json: {e}", file=sys.stderr)
    return set()


SUMMARIZED_IDS: set[int] = _load_summarized_ids()

def get_excluded_feed_ids() -> set[int]:
    """Fetch excluded feed IDs directly from the database."""
    try:
        import psycopg2
        from os import getenv
        
        # Use same connection method as cast2md
        database_url = getenv("DATABASE_URL", "postgresql://cast2md:dev@localhost:5432/cast2md")
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        cur.execute("SELECT id FROM feed WHERE excluded = true")
        ids = {row[0] for row in cur.fetchall()}
        cur.close()
        conn.close()
        return ids
    except Exception as e:
        print(f"Warning: Could not fetch excluded feeds from database: {e}", file=sys.stderr)
        return set()


def api_get(path: str) -> dict:
    req = urllib.request.Request(f"{API_BASE}{path}")
    resp = urllib.request.urlopen(req, timeout=30)
    return json.loads(resp.read())


def api_post(path: str) -> dict:
    req = urllib.request.Request(f"{API_BASE}{path}", method="POST")
    try:
        resp = urllib.request.urlopen(req, timeout=120)
        return json.loads(resp.read())
    except Exception:
        return {}


def get_active_feed_ids() -> list[int]:
    data = api_get("/api/episodes/recent?days=60&limit=500")
    return list({e["feed_id"] for e in data.get("episodes", [])})


def refresh_feed(feed_id: int) -> None:
    api_post(f"/api/feeds/{feed_id}/refresh")


def sanitize_title(title: str) -> str:
    """Replicate the title sanitization for filename matching."""
    title = html.unescape(title)
    title = title.replace(" ", "_")
    for ch in r'/\:*?"<>|':
        title = title.replace(ch, "")
    return title


def _build_transcript_path(ep: dict) -> Path:
    """Derive the expected transcript file path for an episode (mirrors acquire_transcripts.py logic)."""
    feed_title = ep["feed_title"]
    date = ep["published_at"][:10]
    title_slug = sanitize_title(ep["title"])
    filename = f"{date}_{title_slug}.md"

    spaced = TRANSCRIPTS_DIR / feed_title
    underscored = TRANSCRIPTS_DIR / feed_title.replace(" ", "_")

    if underscored.exists():
        return underscored / filename
    elif spaced.exists():
        return spaced / filename
    else:
        return underscored / filename


def verify_transcript_accessible(ep: dict) -> bool:
    """
    Verify that an episode's transcript is accessible from a FREE source.

    "Accessible" means we either already have it OR can acquire it for free:
      1. Disk file already exists (already acquired)
      2. Episode has a free transcript URL (Podcast 2.0 RSS or Pocket Casts) — can be acquired at no cost
      3. Transcript content already cached in the DB (already acquired)

    Returns True if ANY free source is available, False only if ALL checks fail
    (meaning AssemblyAI would be required — treat exceptions as failure).
    """
    ep_id = ep["id"]

    # Check 1: disk file already acquired
    try:
        path = _build_transcript_path(ep)
        if path.exists() and path.stat().st_size > 100:
            return True
    except Exception:
        pass

    # Check 2: free transcript URL available (Podcast 2.0 or Pocket Casts)
    # GET /api/episodes/{id} returns transcript_url (Podcast 2.0 RSS link) and
    # pocketcasts_transcript_url — either means we can acquire for free at no cost
    try:
        ep_detail = api_get(f"/api/episodes/{ep_id}")
        if ep_detail.get("transcript_url"):
            return True
        if ep_detail.get("pocketcasts_transcript_url"):
            return True
    except Exception:
        pass

    # Check 3: transcript content already cached in DB
    try:
        data = api_get(f"/api/episodes/{ep_id}/transcript/section?duration=99999")
        t = data.get("transcript", "")
        if t and t.strip():
            return True
    except Exception:
        pass

    return False


def _summary_file_exists(feed_title: str, published_at: str, title: str) -> bool:
    """Check if a summary file already exists on disk (filename-based fallback)."""
    date = published_at[:10]  # YYYY-MM-DD
    podcast_slug = feed_title.replace(" ", "_")
    title_slug = sanitize_title(title)
    summary_path = SUMMARIES_DIR / date / f"{podcast_slug}__{title_slug}.md"
    return summary_path.exists()


def is_summarized(ep: dict) -> bool:
    """Return True if this episode has already been summarized.

    Primary check: episode ID in the SUMMARIZED_IDS tracking set.
    Fallback: filename-based disk check (catches episodes recorded before ID tracking).
    """
    ep_id = ep.get("id")
    if ep_id is not None and int(ep_id) in SUMMARIZED_IDS:
        return True
    # Belt-and-suspenders: also check for the summary file on disk
    return _summary_file_exists(ep["feed_title"], ep["published_at"], ep["title"])


def transcript_status_emoji(has_transcript: bool) -> str:
    """Return emoji based on transcript availability."""
    return ":page_with_curl:" if has_transcript else ":speaker:"


def main():
    args = sys.argv[1:]

    since_last_run = "--since-last-run" in args
    do_refresh = "--no-refresh" not in args
    since_timestamp = None

    if since_last_run:
        # Compute days from last discovery state
        state_path = WORKSPACE / "data" / "discovery-state.json"
        if state_path.exists():
            try:
                state = json.loads(state_path.read_text())
                last_ts = state["last_discovery_at"]
                since_timestamp = last_ts
                last_dt = datetime.fromisoformat(last_ts.replace("Z", "+00:00"))
                delta = datetime.now(timezone.utc) - last_dt
                days = max(1, math.ceil(delta.total_seconds() / 86400))
                print(f"Since last run: {last_ts} ({days} days)", file=sys.stderr)
            except Exception as e:
                print(f"Warning: could not parse discovery-state.json: {e}. Falling back to 2 days.", file=sys.stderr)
                days = 2
        else:
            print("No discovery-state.json found. Falling back to 2 days (first run).", file=sys.stderr)
            days = 2
    else:
        positional = [a for a in args if not a.startswith("--")]
        if not positional:
            print("Usage: discover_candidates.py <days> [--no-refresh]", file=sys.stderr)
            print("       discover_candidates.py --since-last-run [--no-refresh]", file=sys.stderr)
            sys.exit(1)
        days = int(positional[0])

    # Refresh active feeds in parallel
    if do_refresh:
        feed_ids = get_active_feed_ids()
        print(f"Refreshing {len(feed_ids)} active feeds...", file=sys.stderr)
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
            list(ex.map(refresh_feed, feed_ids))
        print("Refresh done.", file=sys.stderr)

    # Query episodes
    data = api_get(f"/api/episodes/recent?days={days}&limit=200")
    episodes = data.get("episodes", [])

    # Filter and annotate
    excluded_ids = get_excluded_feed_ids()
    filtered = []
    for ep in episodes:
        if ep["feed_id"] in excluded_ids:
            continue
        ep["summary_exists"] = is_summarized(ep)
        filtered.append(ep)

    # Verify transcript accessibility for ALL unsummarized episodes
    # The API's has_transcript flag is unreliable — many episodes have free
    # transcripts available (via Pocket Casts, disk, or DB) that aren't pre-flagged.
    # Check every unsummarized episode so the discovery emoji is accurate.
    episodes_to_verify = [ep for ep in filtered if not ep["summary_exists"]]
    if episodes_to_verify:
        print(f"Verifying transcript accessibility for {len(episodes_to_verify)} unsummarized episode(s)...", file=sys.stderr)
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
            future_to_ep = {ex.submit(verify_transcript_accessible, ep): ep for ep in episodes_to_verify}
            for future in concurrent.futures.as_completed(future_to_ep):
                ep = future_to_ep[future]
                try:
                    accessible = future.result()
                except Exception:
                    accessible = False  # conservative: treat errors as no transcript
                was_flagged = ep.get("has_transcript", False)
                ep["has_transcript"] = accessible
                if not accessible and was_flagged:
                    print(f"⚠ ep {ep['id']}: API flagged transcript but not accessible — downgraded", file=sys.stderr)
                elif accessible and not was_flagged:
                    print(f"✓ ep {ep['id']}: free transcript found (not flagged by API)", file=sys.stderr)

    # Apply transcript emoji after verification
    for ep in filtered:
        ep["transcript_emoji"] = transcript_status_emoji(ep.get("has_transcript", False))

    # Sort: newest date first, then podcast name
    filtered.sort(key=lambda e: (e["published_at"][:10], e["feed_title"]), reverse=False)
    filtered.sort(key=lambda e: e["published_at"][:10], reverse=True)

    # Group by podcast
    from collections import defaultdict
    by_podcast = defaultdict(list)
    for ep in filtered:
        by_podcast[ep["feed_title"]].append(ep)

    result = {
        "total": len(filtered),
        "unsummarized": sum(1 for e in filtered if not e["summary_exists"]),
        "by_podcast": dict(by_podcast),
        "episodes": filtered,
    }

    if since_timestamp:
        result["since_timestamp"] = since_timestamp

    print(json.dumps(result))


if __name__ == "__main__":
    main()
