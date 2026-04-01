#!/usr/bin/env python3
"""
Format discovery JSON output for Slack display.

Usage:
    python scripts/format_discovery.py < latest-discovery.json

Output:
    - Slack-formatted message with episode numbers, podcast names, titles, and transcript emoji
    - Numbered mapping file (latest-discovery.md) for resolving episode numbers to IDs
"""

import sys
import json
from datetime import datetime
from pathlib import Path

def format_discovery(data: dict) -> tuple[str, list]:
    """
    Format discovery JSON into Slack message and numbered episode list.
    
    Returns:
        (slack_message, episodes_with_numbers)
    """
    episodes = data.get("episodes", [])
    unsummarized = [e for e in episodes if not e.get("summary_exists", False)]
    
    if not unsummarized:
        return ":studio_microphone: **Podcast Discovery** — No new unsummarized episodes found.", []
    
    # Build headline — use since_timestamp if available (from --since-last-run),
    # otherwise fall back to the most recent episode date
    since_ts = data.get("since_timestamp")
    if since_ts:
        dt = datetime.fromisoformat(since_ts.replace('Z', '+00:00'))
        date_str = dt.strftime("%m-%d-%y %I:%M %p").lstrip('0').replace(' 0', ' ')
        headline_suffix = f"since last run ({date_str})"
    else:
        most_recent = unsummarized[0]["published_at"]
        dt = datetime.fromisoformat(most_recent.replace('Z', '+00:00'))
        date_str = dt.strftime("%m-%d-%y %I:%M %p").lstrip('0').replace(' 0', ' ')
        headline_suffix = f"since {date_str}"
    
    # Build Slack message
    lines = [f":studio_microphone: **Podcast Discovery** — {len(unsummarized)} new episode(s) found {headline_suffix}\n"]
    
    numbered_episodes = []
    downgraded_count = 0
    for i, ep in enumerate(unsummarized, 1):
        transcript_emoji = ep.get("transcript_emoji", ":speaker:")
        ep_dt = datetime.fromisoformat(ep["published_at"].replace('Z', '+00:00'))
        ep_date_str = ep_dt.strftime("%m-%d-%y").lstrip('0').replace('-0', '-')
        lines.append(
            f"{i}. **{ep['feed_title']}** - {ep['title']} _{ep_date_str}_ {transcript_emoji}"
        )
        numbered_episodes.append((i, ep))
        if ep.get("transcript_downgraded", False):
            downgraded_count += 1

    if downgraded_count > 0:
        lines.append(
            f"\n_⚠️ {downgraded_count} episode(s) had transcript flags but failed verification — marked as needing AssemblyAI._"
        )

    return "\n".join(lines), numbered_episodes


def write_numbered_mapping(episodes_with_numbers: list, output_path: Path = None) -> None:
    """
    Write a numbered mapping file for resolving episode numbers to IDs.
    
    This ensures that when a user says "process 1, 3, 5", the numbers refer to
    the display order they saw in Slack, not any internal JSON order.
    """
    if output_path is None:
        output_path = Path(__file__).parent.parent / "data" / "latest-discovery.md"
    
    if not episodes_with_numbers:
        output_path.write_text("")
        return
    
    # Get date info from first episode
    first_ep = episodes_with_numbers[0][1]
    dt = datetime.fromisoformat(first_ep["published_at"].replace('Z', '+00:00'))
    discovery_date = dt.strftime("%Y-%m-%d %H:%M UTC").lstrip('0').replace(' 0', ' ')
    
    lines = [
        "# Podcast Discovery Results",
        f"**Date:** {discovery_date}",
        f"**Total Episodes:** {len(episodes_with_numbers)}",
        f"**Unsummarized:** {len(episodes_with_numbers)}",
        "",
        "---",
        "",
        "## Episode Mapping (Display Order)",
        "",
    ]
    
    for display_num, ep in episodes_with_numbers:
        ep_date = datetime.fromisoformat(ep["published_at"].replace('Z', '+00:00')).strftime("%b %d, %Y")
        lines.append(f"**{display_num}. {ep['feed_title']}**")
        lines.append(f"Episode ID: {ep['id']} | Feed ID: {ep['feed_id']}")
        lines.append(f"Title: {ep['title']}")
        lines.append(f"Date: {ep_date} | Status: {ep['status']}")
        lines.append("")
    
    output_path.write_text("\n".join(lines))


if __name__ == "__main__":
    data = json.load(sys.stdin)
    slack_message, numbered_eps = format_discovery(data)
    
    # Print Slack message to stdout
    print(slack_message)
    
    # Write numbered mapping file
    write_numbered_mapping(numbered_eps)
    
    # Write discovery state (tracks last successful discovery for --since-last-run)
    state_path = Path(__file__).parent.parent / "data" / "discovery-state.json"
    state_path.write_text(json.dumps(
        {"last_discovery_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")},
        indent=2
    ))
