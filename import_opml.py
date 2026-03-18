#!/usr/bin/env python3
"""Import podcast feeds from a Pocket Casts OPML export into cast2md."""

import sys
import time
import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
import json

API_BASE = "http://127.0.0.1:8000"


def parse_opml(path: str) -> list[dict]:
    tree = ET.parse(path)
    feeds = []
    for outline in tree.iter("outline"):
        url = outline.get("xmlUrl")
        name = outline.get("text")
        if url:
            feeds.append({"url": url, "name": name})
    return feeds


def add_feed(url: str) -> dict:
    data = json.dumps({"url": url}).encode()
    req = urllib.request.Request(
        f"{API_BASE}/api/feeds",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    resp = urllib.request.urlopen(req, timeout=30)
    return json.loads(resp.read())


def main():
    opml_path = sys.argv[1] if len(sys.argv) > 1 else "PocketCasts.opml"
    feeds = parse_opml(opml_path)
    print(f"Found {len(feeds)} feeds in {opml_path}\n")

    success = 0
    failed = []

    for i, feed in enumerate(feeds, 1):
        name = feed["name"] or feed["url"]
        try:
            result = add_feed(feed["url"])
            feed_id = result.get("id", "?")
            print(f"  [{i}/{len(feeds)}] Added: {name} (id={feed_id})")
            success += 1
        except urllib.error.HTTPError as e:
            body = e.read().decode() if e.fp else ""
            if "already exists" in body.lower() or e.code == 409:
                print(f"  [{i}/{len(feeds)}] Skipped (already exists): {name}")
                success += 1
            else:
                print(f"  [{i}/{len(feeds)}] FAILED: {name} — HTTP {e.code}: {body[:100]}")
                failed.append(name)
        except Exception as e:
            print(f"  [{i}/{len(feeds)}] FAILED: {name} — {e}")
            failed.append(name)
        time.sleep(0.2)

    print(f"\nDone: {success} added, {len(failed)} failed")
    if failed:
        print("Failed feeds:")
        for f in failed:
            print(f"  - {f}")


if __name__ == "__main__":
    main()
