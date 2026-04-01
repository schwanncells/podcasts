#!/usr/bin/env python3
"""
Manage podcast exclusions from discovery.

Usage:
    python scripts/exclude_podcasts.py exclude <podcast_name_or_id>
    python scripts/exclude_podcasts.py include <podcast_name_or_id>
    python scripts/exclude_podcasts.py list
    python scripts/exclude_podcasts.py status

Examples:
    python scripts/exclude_podcasts.py exclude "In Our Headphones"
    python scripts/exclude_podcasts.py exclude 54
    python scripts/exclude_podcasts.py include "Uhh Yeah Dude"
    python scripts/exclude_podcasts.py list
    python scripts/exclude_podcasts.py status
"""

import sys
import os
from difflib import SequenceMatcher
from datetime import datetime

import psycopg2


def get_db_connection():
    """Get a database connection."""
    database_url = os.getenv("DATABASE_URL", "postgresql://cast2md:dev@localhost:5432/cast2md")
    try:
        return psycopg2.connect(database_url)
    except psycopg2.OperationalError as e:
        print(f"Error: Could not connect to database: {e}", file=sys.stderr)
        sys.exit(1)


def find_feed_by_name(conn, name: str) -> tuple[dict | None, bool]:
    """Find a feed by name (exact or fuzzy match).

    Returns:
        (feed_dict, is_fuzzy) - the feed and whether it was a fuzzy match.
    """
    cur = conn.cursor()
    cur.execute("SELECT id, title, excluded FROM feed ORDER BY title")
    feeds = [{"id": row[0], "title": row[1], "excluded": row[2]} for row in cur.fetchall()]
    cur.close()

    # Exact match (case-insensitive)
    for feed in feeds:
        if feed["title"].lower() == name.lower():
            return feed, False

    # Fuzzy match
    best_match = None
    best_score = 0.6  # Minimum threshold
    for feed in feeds:
        score = SequenceMatcher(None, name.lower(), feed["title"].lower()).ratio()
        if score > best_score:
            best_score = score
            best_match = feed

    return best_match, best_match is not None


def find_feed_by_id(conn, feed_id: int) -> dict | None:
    """Find a feed by ID."""
    cur = conn.cursor()
    cur.execute("SELECT id, title, excluded FROM feed WHERE id = %s", (feed_id,))
    row = cur.fetchone()
    cur.close()

    if row:
        return {"id": row[0], "title": row[1], "excluded": row[2]}
    return None


def resolve_feed(conn, identifier: str) -> tuple[dict | None, bool]:
    """Resolve a feed by name or ID.

    Returns:
        (feed_dict, is_fuzzy) - the feed and whether it was a fuzzy match.
    """
    # Try as integer ID first
    try:
        feed_id = int(identifier)
        feed = find_feed_by_id(conn, feed_id)
        return feed, False
    except ValueError:
        pass

    # Try as name
    return find_feed_by_name(conn, identifier)


def confirm_fuzzy_match(feed: dict) -> bool:
    """Prompt user to confirm a fuzzy match."""
    try:
        response = input(f"Did you mean '{feed['title']}'? (y/n) ").strip().lower()
        return response in ("y", "yes")
    except (EOFError, KeyboardInterrupt):
        print()
        return False


def exclude_podcast(identifier: str) -> None:
    """Exclude a podcast from discovery."""
    conn = get_db_connection()
    try:
        feed, is_fuzzy = resolve_feed(conn, identifier)
        if not feed:
            print(f"Error: Could not find podcast '{identifier}'", file=sys.stderr)
            sys.exit(1)

        if is_fuzzy and not confirm_fuzzy_match(feed):
            print("Cancelled.")
            return

        if feed["excluded"]:
            print(f"Already excluded: {feed['title']}")
            return

        cur = conn.cursor()
        now = datetime.now().isoformat()
        cur.execute(
            "UPDATE feed SET excluded = true, excluded_at = %s, updated_at = %s WHERE id = %s",
            (now, now, feed["id"]),
        )
        conn.commit()
        cur.close()

        print(f"✓ Excluded: {feed['title']}")
    finally:
        conn.close()


def include_podcast(identifier: str) -> None:
    """Include a podcast back in discovery."""
    conn = get_db_connection()
    try:
        feed, is_fuzzy = resolve_feed(conn, identifier)
        if not feed:
            print(f"Error: Could not find podcast '{identifier}'", file=sys.stderr)
            sys.exit(1)

        if is_fuzzy and not confirm_fuzzy_match(feed):
            print("Cancelled.")
            return

        if not feed["excluded"]:
            print(f"Already included: {feed['title']}")
            return

        cur = conn.cursor()
        now = datetime.now().isoformat()
        cur.execute(
            "UPDATE feed SET excluded = false, excluded_at = NULL, updated_at = %s WHERE id = %s",
            (now, feed["id"]),
        )
        conn.commit()
        cur.close()

        print(f"✓ Included: {feed['title']}")
    finally:
        conn.close()


def list_excluded() -> None:
    """List all excluded podcasts."""
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, title, excluded_at FROM feed WHERE excluded = true ORDER BY title"
        )
        feeds = cur.fetchall()
        cur.close()

        if not feeds:
            print("No excluded podcasts.")
            return

        print(f"Excluded podcasts ({len(feeds)}):\n")
        for feed_id, title, excluded_at in feeds:
            ts = f"  (since {excluded_at:%Y-%m-%d})" if excluded_at else ""
            print(f"  ID {feed_id:3d}  {title}{ts}")
    finally:
        conn.close()


def show_status() -> None:
    """Show all feeds with active/excluded status."""
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, title, excluded FROM feed ORDER BY title")
        feeds = cur.fetchall()
        cur.close()

        if not feeds:
            print("No feeds found.")
            return

        active = sum(1 for _, _, excluded in feeds if not excluded)
        excluded = len(feeds) - active

        print(f"Feed status ({len(feeds)} total: {active} active, {excluded} excluded):\n")
        for feed_id, title, is_excluded in feeds:
            marker = "✗" if is_excluded else "✓"
            print(f"  {marker}  ID {feed_id:3d}  {title}")
    finally:
        conn.close()


def main() -> None:
    """Main entry point."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "exclude" and len(sys.argv) > 2:
        identifier = " ".join(sys.argv[2:])
        exclude_podcast(identifier)
    elif command == "include" and len(sys.argv) > 2:
        identifier = " ".join(sys.argv[2:])
        include_podcast(identifier)
    elif command == "list":
        list_excluded()
    elif command == "status":
        show_status()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
