# -*- coding: utf-8 -*-
"""
Reconcile posted_to_telegram.json against the live site: any listing id that
was previously posted to the Telegram hub but no longer exists in
vietnam-rent-finder.html (purged as stale by purge_old_listings.py, or removed
any other way) gets its Telegram post(s) deleted via the Bot API, then pruned
from the tracking file.

Run this as a normal step in the daily-check pipeline, AFTER the site has
been rebuilt (it reads the built HTML to know which ids are still live).

Failure handling, because a live hub is a one-way street:
  * Telegram reports refusals as HTTP 400 with a JSON body; urllib raises
    HTTPError for those, so the body is read out of the exception and
    treated like a normal reply -- the script never crashes on a refusal.
  * "message to delete not found" counts as success (already gone).
  * 429 is retried once after `retry_after` seconds.
  * State is written after EVERY listing (tmp + os.replace), so a crash or
    network drop mid-run never re-deletes what already went, and never
    forgets what still has to go.
  * A message the API genuinely refuses stays tracked and is reported, so
    the next run retries it instead of silently dropping the id.
  * Posts made before message ids were recorded (1 Sep 2026) can never be
    found by the bot; those ids are dropped from `posted` with a count in
    the output rather than pretended-deleted.

Telegram's deleteMessage docs give a 48-hour age limit for a bot deleting
its own messages without elevated rights; this bot is an administrator with
can_delete_messages (confirmed via getChatMember), which the same docs
describe as "can delete any message there". Whether that lifts the age
limit is only settled by a real refusal -- and a refusal is reported, not
hidden, so the answer will be visible in this script's output.
"""
import os, re, sys, json, time, urllib.request, urllib.parse, urllib.error

DRY_RUN = "--dry-run" in sys.argv
STATE_FILE = "posted_to_telegram.json"

TOKEN = os.environ.get("TG_BOT_TOKEN")
if not TOKEN and not DRY_RUN:
    raise SystemExit("Set TG_BOT_TOKEN (not needed for --dry-run)")

topics = json.load(open("telegram_topics.json", encoding="utf-8"))
CHAT_ID = topics["chat_id"]

from site_data import load_listings
live_ids = {str(l["id"]) for l in load_listings()}

try:
    state = json.load(open(STATE_FILE, encoding="utf-8"))
except FileNotFoundError:
    raise SystemExit(f"{STATE_FILE} not found -- nothing has been posted yet")
except json.JSONDecodeError as ex:
    raise SystemExit(f"{STATE_FILE} is not valid JSON ({ex}) -- fix or restore it from the .bak copy; do NOT delete it, that would lose every recorded message id")

message_ids = state.setdefault("message_ids", {})
posted = set(state.get("posted", []))

def save_state():
    state["message_ids"] = message_ids
    state["posted"] = sorted(posted)
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1)
    os.replace(tmp, STATE_FILE)

# Two kinds of stale entry:
#   deletable   -- gone from the site, message ids on record -> deleteMessage
#   undeletable -- gone from the site, no message ids (posted before 1 Sep 2026)
deletable = sorted((lid for lid in message_ids if lid not in live_ids), key=int)
undeletable = sorted(p for p in posted if str(p) not in live_ids and str(p) not in message_ids)

if not deletable and not undeletable:
    print("nothing to clean up -- every tracked id is still live")
    raise SystemExit(0)

if DRY_RUN:
    total_msgs = sum(len(message_ids[lid]) for lid in deletable)
    print(f"DRY RUN -- would delete {len(deletable)} listing(s), {total_msgs} message(s):")
    for lid in deletable:
        print(f"  id={lid}: message_ids={message_ids[lid]}")
    if undeletable:
        print(f"{len(undeletable)} gone listing(s) were posted before message ids were recorded -- the bot cannot find those posts; "
              f"they would be dropped from tracking (manual cleanup in the app only): {undeletable[:20]}{' ...' if len(undeletable) > 20 else ''}")
    raise SystemExit(0)

def api(method, params):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        # Telegram puts the real reason in the body of a 4xx; keep it.
        try:
            return json.loads(e.read())
        except Exception:
            return {"ok": False, "error_code": e.code, "description": str(e)}

def delete_one(mid):
    """Returns (gone: bool, description). gone=True also when the message no longer exists."""
    r = api("deleteMessage", {"chat_id": CHAT_ID, "message_id": mid})
    if r.get("error_code") == 429:
        wait = int((r.get("parameters") or {}).get("retry_after", 5)) + 1
        print(f"  rate-limited, sleeping {wait}s")
        time.sleep(wait)
        r = api("deleteMessage", {"chat_id": CHAT_ID, "message_id": mid})
    if r.get("ok"):
        return True, "deleted"
    desc = (r.get("description") or "")
    if "message to delete not found" in desc.lower() or "message_id_invalid" in desc.lower():
        return True, "already gone"
    return False, desc

deleted, failed = 0, []
try:
    for lid in deletable:
        remaining = []
        for mid in message_ids[lid]:
            gone, desc = delete_one(mid)
            if not gone:
                remaining.append(mid)
                failed.append((lid, mid, desc))
            time.sleep(0.35)
        if remaining:
            message_ids[lid] = remaining          # retry exactly these next run
        else:
            del message_ids[lid]
            posted.discard(int(lid))
            deleted += 1
        save_state()                              # after every listing, never only at the end
except urllib.error.URLError as ex:
    save_state()
    raise SystemExit(f"network error ({ex.reason}) -- stopped; state saved, rerun later. Deleted so far: {deleted}")

for p in undeletable:
    posted.discard(p)
save_state()

print(f"reconciled: {len(deletable)} stale-tracked id(s) found, {deleted} fully deleted from hub")
if undeletable:
    print(f"{len(undeletable)} gone listing(s) had no message ids on record (posted before 1 Sep 2026) -- "
          f"the bot cannot delete those; dropped from tracking, clean them up in the app if needed")
if failed:
    print(f"{len(failed)} message(s) REFUSED by Telegram (left tracked, will retry next run):")
    for lid, mid, desc in failed:
        print(f"  id={lid} message_id={mid}: {desc}")
