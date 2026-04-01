#!/usr/bin/env python3
"""
Record summarized episode IDs to the tracking file.

Usage:
    python scripts/record_summarized.py 123 456 789

Loads data/summarized_episodes.json, adds the given IDs (deduped, sorted),
and saves back atomically.
"""

import sys
import json
import os
from pathlib import Path

WORKSPACE = Path("/home/kayshway/podcasts")
TRACKING_FILE = WORKSPACE / "data/summarized_episodes.json"


def load_episode_ids() -> list[int]:
    """Load existing episode IDs from the tracking file."""
    if not TRACKING_FILE.exists():
        return []
    with open(TRACKING_FILE) as f:
        data = json.load(f)
    return [int(x) for x in data.get("episode_ids", [])]


def save_episode_ids(ids: list[int]) -> None:
    """Save episode IDs atomically (write to .tmp, then rename)."""
    tmp_path = TRACKING_FILE.with_suffix(".json.tmp")
    with open(tmp_path, "w") as f:
        json.dump({"episode_ids": ids}, f)
        f.write("\n")
    os.replace(tmp_path, TRACKING_FILE)


def main():
    if len(sys.argv) < 2:
        print("Usage: record_summarized.py <id1> [id2] ...", file=sys.stderr)
        sys.exit(1)

    try:
        new_ids = [int(arg) for arg in sys.argv[1:]]
    except ValueError as e:
        print(f"Error: all arguments must be integer episode IDs: {e}", file=sys.stderr)
        sys.exit(1)

    existing = load_episode_ids()
    combined = sorted(set(existing) | set(new_ids))

    added = set(new_ids) - set(existing)
    save_episode_ids(combined)

    print(
        f"Recorded {len(added)} new ID(s) to {TRACKING_FILE.relative_to(WORKSPACE)} "
        f"(total: {len(combined)}). Added: {sorted(added)}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
