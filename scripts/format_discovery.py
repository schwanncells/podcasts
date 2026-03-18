#!/usr/bin/env python3
"""
Format discovery JSON output for Slack display.

Usage:
    python scripts/format_discovery.py < latest-discovery.json

Output:
    Slack-formatted message with episode numbers, podcast names, titles, and transcript emoji.
"""

import sys
import json
from collections import defaultdict

SLACK_EMOJI = [
    ":one:", ":two:", ":three:", ":four:", ":five:",
    ":six:", ":seven:", ":eight:", ":nine:", ":keycap_ten:"
]


def format_discovery(data: dict) -> str:
    """Format discovery JSON into Slack message."""
    episodes = data.get("episodes", [])
    unsummarized = [e for e in episodes if not e.get("summary_exists", False)]
    
    if not unsummarized:
        return ":studio_microphone: *Podcast Discovery* — No new unsummarized episodes found."
    
    # Group by date (newest first)
    by_date = defaultdict(list)
    for ep in sorted(unsummarized, key=lambda e: e["published_at"], reverse=True):
        date = ep["published_at"][:10]
        by_date[date].append(ep)
    
    # Build message
    lines = [f":studio_microphone: *Podcast Discovery — {len(unsummarized)} new episode(s)*\n"]
    
    episode_num = 1
    for date in sorted(by_date.keys(), reverse=True):
        lines.append(f"**{date}**")
        for ep in by_date[date]:
            emoji = SLACK_EMOJI[episode_num - 1] if episode_num <= 10 else f"{episode_num}."
            transcript_emoji = ep.get("transcript_emoji", ":speaker:")
            lines.append(
                f"{emoji} **{ep['feed_title']}** — {ep['title']} {transcript_emoji}"
            )
            episode_num += 1
    
    lines.append("\nWhich would you like to process? (numbers, ranges, or \"all\")")
    return "\n".join(lines)


if __name__ == "__main__":
    data = json.load(sys.stdin)
    print(format_discovery(data))
