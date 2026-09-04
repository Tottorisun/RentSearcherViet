# -*- coding: utf-8 -*-
"""
Find the numeric chat_id of a group the bot has just been added to.

Telegram's API never asks you to type an id -- it hands one out through
getUpdates once the bot has seen at least one message in the chat. This script
saves opening that JSON in a browser and hunting through it by hand.

USAGE
  1. Add your bot to the group (as a member is enough for this step; it needs
     to be an admin only for posting into topics later).
  2. Send any message in the group -- literally "test" is fine.
  3. set TG_BOT_TOKEN=...      (the token from @BotFather)
     python find_chat_id.py
  4. Copy the printed id into telegram_topics.json's "chat_id" field.

If nothing prints, Telegram has no update to show yet -- send a fresh message
in the group (getUpdates only returns what arrived after the bot joined) and
run this again.
"""
import json
import os
import sys
import urllib.request

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
    except Exception:
        pass

# Ботов теперь два: вьетнамский и филиппинский (@RentPhilippineBot). Какой
# именно опрашивать -- решает ключ --hub, чтобы не искать чат вьетнамского бота
# в филиппинской группе и наоборот.
_HUB_ENV = {"vn": "TG_BOT_TOKEN", "ph": "TG_BOT_TOKEN_PH"}
_hub = "vn"
for _i, _a in enumerate(sys.argv):
    if _a == "--hub" and _i + 1 < len(sys.argv):
        _hub = sys.argv[_i + 1]
if _hub not in _HUB_ENV:
    sys.exit("неизвестный хаб %r -- есть: %s" % (_hub, ", ".join(_HUB_ENV)))
_ENV = _HUB_ENV[_hub]
print("hub: %s (токен из %s)" % (_hub, _ENV))
token = os.environ.get(_ENV)
if not token:
    sys.exit("set " + _ENV + " first (the token @BotFather gave you)")

url = "https://api.telegram.org/bot%s/getUpdates" % token
with urllib.request.urlopen(url, timeout=20) as r:
    data = json.loads(r.read().decode("utf-8"))

if not data.get("ok"):
    sys.exit("Telegram returned an error: %s" % data.get("description"))

seen = {}
for upd in data.get("result", []):
    msg = upd.get("message") or upd.get("channel_post") or {}
    chat = msg.get("chat")
    if chat and chat.get("type") in ("group", "supergroup", "channel"):
        seen[chat["id"]] = chat

if not seen:
    print("no group/channel messages found yet.")
    print("Make sure the bot is IN the group and that you sent a message AFTER adding it, then run this again.")
    sys.exit(1)

print("found %d chat(s):\n" % len(seen))
for cid, chat in seen.items():
    print("  chat_id: %s" % cid)
    print("  title  : %s" % chat.get("title"))
    print("  type   : %s" % chat.get("type"))
    print("  forum  : %s" % chat.get("is_forum", False))
    print()
print('Put the right one into telegram_topics.json as "chat_id".')
