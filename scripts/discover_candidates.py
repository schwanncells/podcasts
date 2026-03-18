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
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

API_BASE = "http://127.0.0.1:8000"
WORKSPACE = Path("/home/kayshway/podcasts")
SUMMARIES_DIR = WORKSPACE / "data/podcasts/summaries"

EXCLUDED_PODCASTS = {
    "The Pomp Podcast",
    "StarTalk Radio",
    "Radio Rental",
    "NPR Music",
}


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
    import html
    title = html.unescape(title)
    title = title.replace(" ", "_")
    for ch in r'/\:*?"<>|':
        title = title.replace(ch, "")
    return title


def summary_exists(feed_title: str, published_at: str, title: str) -> bool:
    """Check if a summary file already exists on disk."""
    date = published_at[:10]  # YYYY-MM-DD
    podcast_slug = feed_title.replace(" ", "_")
    title_slug = sanitize_title(title)
    summary_path = SUMMARIES_DIR / date / f"{podcast_slug}__{title_slug}.md"
    return summary_path.exists()


def transcript_status_emoji(has_transcript: bool) -> str:
    """Return emoji based on transcript availability."""
    return ":page_with_curl:" if has_transcript else ":speaker:"


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: discover_candidates.py <days> [--no-refresh]", file=sys.stderr)
        sys.exit(1)

    days = int(args[0])
    do_refresh = "--no-refresh" not in args

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
    filtered = []
    for ep in episodes:
        if ep["feed_title"] in EXCLUDED_PODCASTS:
            continue
        ep["summary_exists"] = summary_exists(ep["feed_title"], ep["published_at"], ep["title"])
        ep["transcript_emoji"] = transcript_status_emoji(ep.get("has_transcript", False))
        filtered.append(ep)

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

    print(json.dumps(result))


if __name__ == "__main__":
    main()
