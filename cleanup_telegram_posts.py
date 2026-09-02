# -*- coding: utf-8 -*-
"""
Reconcile posted_to_telegram.json against the live site: any listing id that
was previously posted to the Telegram hub but no longer exists in
vietnam-rent-finder.html (purged as stale by purge_old_listings.py, or removed
any other way) gets its Telegram post(s) deleted via the Bot API, then pruned
from the tracking file.

Run this as a normal step in the daily-check pipeline, right after
purge_old_listings.py (which is what actually removes stale L(...) blocks).

Telegram's deleteMessage documents a 48-hour age limit for a bot deleting its
own messages WITHOUT elevated rights -- but this bot is an administrator with
the can_delete_messages right in the hub group (confirmed via getChatMember),
which the same docs describe as letting it "delete any message there," with
no age qualifier restated on that specific bullet -- this is exactly what
ordinary Telegram moderation bots rely on to clean up old messages. If the
Bot API disagrees for a given message anyway, this script reports the
failure and leaves that listing's id tracked (so a future run retries it)
rather than silently losing the id.
"""
import os, re, sys, json, time, urllib.request, urllib.parse

DRY_RUN = "--dry-run" in sys.argv

TOKEN = os.environ.get("TG_BOT_TOKEN")
if not TOKEN and not DRY_RUN:
    raise SystemExit("Set TG_BOT_TOKEN (not needed for --dry-run)")

topics = json.load(open("telegram_topics.json", encoding="utf-8"))
CHAT_ID = topics["chat_id"]

html = open("vietnam-rent-finder.html", encoding="utf-8").read()
m = re.search(r'var DATA = (\{.*?\});\s*\n', html, re.S)
data = json.loads(m.group(1))
live_ids = {str(l["id"]) for l in data["LISTINGS"]}

try:
    state = json.load(open("posted_to_telegram.json", encoding="utf-8"))
except FileNotFoundError:
    raise SystemExit("posted_to_telegram.json not found -- nothing has been posted yet")

message_ids = state.get("message_ids", {})
posted = set(state.get("posted", []))

stale_ids = sorted((lid for lid in message_ids if lid not in live_ids), key=int)

if not stale_ids:
    print("nothing to clean up -- every tracked id is still live")
    raise SystemExit(0)

if DRY_RUN:
    total_msgs = sum(len(message_ids[lid]) for lid in stale_ids)
    print(f"DRY RUN -- would delete {len(stale_ids)} listing(s), {total_msgs} message(s):")
    for lid in stale_ids:
        print(f"  id={lid}: message_ids={message_ids[lid]}")
    raise SystemExit(0)

def api(method, params):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=15) as resp:
        return json.loads(resp.read())

deleted, failed = 0, []
for lid in stale_ids:
    ok_all = True
    for mid in message_ids[lid]:
        result = api("deleteMessage", {"chat_id": CHAT_ID, "message_id": mid})
        if not result.get("ok"):
            ok_all = False
            failed.append((lid, mid, result.get("description")))
        time.sleep(0.35)
    if ok_all:
        del message_ids[lid]
        posted.discard(int(lid))
        deleted += 1

state["message_ids"] = message_ids
state["posted"] = sorted(posted)
json.dump(state, open("posted_to_telegram.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print(f"reconciled: {len(stale_ids)} stale-tracked id(s) found, {deleted} fully deleted from hub")
if failed:
    print(f"{len(failed)} message(s) failed to delete (left tracked, will retry next run):")
    for lid, mid, desc in failed:
        print(f"  id={lid} message_id={mid}: {desc}")
