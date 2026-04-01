#!/usr/bin/env python3
"""
One-time backfill: scan existing summary files and record their episode IDs.

Connects to PostgreSQL, scans data/podcasts/summaries/ recursively, and for
each summary file attempts to match it to an episode in the database by:
  1. Fuzzy-matching podcast name + episode title (normalized)
  2. Fallback: date (from parent dir) + podcast name match

Writes matched IDs to data/summarized_episodes.json and prints a report.

Usage:
    DATABASE_URL=... python scripts/backfill_summarized.py
"""

import sys
import json
import os
import html
import re
from pathlib import Path

import psycopg2

WORKSPACE = Path("/home/kayshway/podcasts")
SUMMARIES_DIR = WORKSPACE / "data/podcasts/summaries"
TRACKING_FILE = WORKSPACE / "data/summarized_episodes.json"


def normalize(text: str) -> str:
    """Normalize a string for fuzzy matching: decode HTML entities, strip special chars, lowercase."""
    text = html.unescape(text)
    text = text.lower()
    # Replace underscores and hyphens with spaces (filenames use underscores for spaces)
    text = text.replace("_", " ").replace("-", " ")
    # Strip special characters — keep alphanumeric and spaces
    text = re.sub(r"[^a-z0-9 ]", "", text)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_episode_ids() -> list[int]:
    if not TRACKING_FILE.exists():
        return []
    with open(TRACKING_FILE) as f:
        data = json.load(f)
    return [int(x) for x in data.get("episode_ids", [])]


def save_episode_ids(ids: list[int]) -> None:
    tmp_path = TRACKING_FILE.with_suffix(".json.tmp")
    with open(tmp_path, "w") as f:
        json.dump({"episode_ids": ids}, f)
        f.write("\n")
    os.replace(tmp_path, TRACKING_FILE)


def main():
    database_url = os.getenv("DATABASE_URL", "postgresql://cast2md:dev@localhost:5432/cast2md")

    # Connect to DB
    try:
        conn = psycopg2.connect(database_url)
    except Exception as e:
        print(f"Error: could not connect to database: {e}", file=sys.stderr)
        sys.exit(1)
    cur = conn.cursor()

    # Load all episodes from DB into memory for matching
    # Columns: id, feed_title (from joined feed), title, published_at
    cur.execute("""
        SELECT e.id, f.title AS feed_title, e.title, e.published_at::date::text
        FROM episode e
        JOIN feed f ON f.id = e.feed_id
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # Build lookup structures
    # By (norm_feed, norm_title) -> id
    by_title: dict[tuple[str, str], int] = {}
    # By (date, norm_feed) -> list of ids (may be multiple episodes same day/feed)
    by_date_feed: dict[tuple[str, str], list[int]] = {}

    for ep_id, feed_title, title, pub_date in rows:
        nf = normalize(feed_title or "")
        nt = normalize(title or "")
        key = (nf, nt)
        if key not in by_title:
            by_title[key] = ep_id  # keep first match

        date_key = (pub_date or "", nf)
        by_date_feed.setdefault(date_key, []).append(ep_id)

    # Scan summary files
    summary_files = list(SUMMARIES_DIR.rglob("*.md"))
    print(f"Found {len(summary_files)} summary file(s) in {SUMMARIES_DIR}", file=sys.stderr)

    matched_ids: set[int] = set()
    unmatched: list[str] = []

    for summary_path in summary_files:
        # Parent dir name is YYYY-MM-DD
        date = summary_path.parent.name  # e.g. "2025-03-10"
        stem = summary_path.stem  # e.g. "My_Podcast__Episode_Title"

        # Split on double underscore
        parts = stem.split("__", 1)
        if len(parts) != 2:
            unmatched.append(str(summary_path.relative_to(WORKSPACE)))
            continue

        podcast_slug, title_slug = parts
        norm_podcast = normalize(podcast_slug)
        norm_title = normalize(title_slug)

        # Strategy 1: title match
        ep_id = by_title.get((norm_podcast, norm_title))
        if ep_id:
            matched_ids.add(ep_id)
            continue

        # Strategy 2: date + feed match (if only one episode that day for that feed)
        candidates = by_date_feed.get((date, norm_podcast), [])
        if len(candidates) == 1:
            matched_ids.add(candidates[0])
            continue

        # Strategy 3: date + feed with partial title match among candidates
        if len(candidates) > 1:
            best = None
            best_score = 0
            for cid in candidates:
                # Find this candidate's title
                for ep_id2, feed_title2, title2, pub_date2 in rows:
                    if ep_id2 == cid:
                        nt2 = normalize(title2 or "")
                        # Simple overlap score: shared words
                        words_a = set(norm_title.split())
                        words_b = set(nt2.split())
                        score = len(words_a & words_b)
                        if score > best_score:
                            best_score = score
                            best = cid
                        break
            if best and best_score > 0:
                matched_ids.add(best)
                continue

        unmatched.append(str(summary_path.relative_to(WORKSPACE)))

    # Merge with existing IDs
    existing = set(load_episode_ids())
    combined = sorted(existing | matched_ids)
    save_episode_ids(combined)

    # Report
    new_count = len(matched_ids - existing)
    print(f"\n=== Backfill Report ===")
    print(f"Summary files found:  {len(summary_files)}")
    print(f"Matched:              {len(matched_ids)}")
    print(f"New IDs recorded:     {new_count}")
    print(f"Unmatched:            {len(unmatched)}")
    print(f"Total IDs in file:    {len(combined)}")
    if unmatched:
        print("\nUnmatched files:")
        for f in sorted(unmatched):
            print(f"  {f}")


if __name__ == "__main__":
    main()
