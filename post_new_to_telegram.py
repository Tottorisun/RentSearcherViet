# -*- coding: utf-8 -*-
"""
Publish new listings into the Telegram hub for Vietnamese property.

STRUCTURE. One forum supergroup is the hub, and each city -- plus commercial as
a whole -- gets its own topic inside it, rather than a separate group per city.
Ten half-empty groups look abandoned and split the audience; one group with
topics keeps a single join link while letting people mute what they do not
need. The bot posts into a topic via `message_thread_id`: one token, one chat,
every section.

RUSSIAN ONLY, ON PURPOSE. This hub's audience is Russian-speaking -- confirmed
by the owner on 1 Sep 2026, overriding the bilingual design this file started
with. The SITE stays bilingual (index.html / en.html); this is specifically
about what goes into THIS Telegram group. Do not re-add English here without
being asked again.

ALL PHOTOS, NOT JUST ONE. A listing's `details.photos` can hold several images;
the first version of this script only ever sent photos[0]. That is a real
product gap for a property feed, not a style choice -- fixed by sending every
photo as an album (sendMediaGroup) when there are 2 or more, and a single
sendPhoto only when there is exactly one. Telegram allows 2-10 items per album
and shows a caption only on the first item -- confirmed against the Bot API
reference before relying on it, since getting this wrong a second time would
mean editing or deleting posts again.

RATE LIMIT. Telegram allows a bot about 20 messages per minute into a group.
The default delay stays under that deliberately, and --limit exists so a first
run cannot try to dump the whole catalogue and get throttled. An album counts
as several messages in one API call, so it can spend more of that budget per
listing than a single photo would -- the delay is between LISTINGS, not
between photos within one album, which Telegram sends as a single unit anyway.

SETUP
  1. Create a supergroup, turn Topics on, add your bot as an administrator with
     "Manage topics" and the right to post.
  2. Copy telegram_topics.example.json to telegram_topics.json and put the
     group's chat_id in it (the numeric -100... id, or @name if it is public).
  3. python post_new_to_telegram.py --setup     creates the topics and writes
     their ids back into telegram_topics.json. Run once; it skips anything that
     already has an id, so re-running is harmless.
  4. python post_new_to_telegram.py --dry-run   see exactly what would go out.
  5. python post_new_to_telegram.py             post for real.

  TG_BOT_TOKEN must be set in the environment. It is never written to the repo.

STATE: posted_to_telegram.json remembers what was already sent, and which
message ids each listing produced -- the first run of this script posted with
the wrong photo count and there was no way to find and delete those messages
afterwards, so the ids are now kept for exactly that situation.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

# This machine's console is cp1251 and cannot encode the emoji in the captions.
# reconfigure, never `sys.stdout = io.TextIOWrapper(sys.stdout.buffer, ...)`:
# the replaced wrapper closes the underlying stream when it is garbage
# collected, and every later print then dies with "I/O operation on closed
# file" -- which in a background run reads as a hang rather than an error.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
    except Exception:
        pass

STATE_FILE = "posted_to_telegram.json"
TOPICS_FILE = "telegram_topics.json"
BUILT_HTML = "index.html"
SITE_URL = "https://tottorisun.github.io/RentSearcherViet/"

# The photo-caption limit is not stated in the Bot API reference, and an
# overlong caption is rejected outright rather than truncated, so this budget
# stays well short of the 1024 characters the API is generally held to allow.
CAPTION_BUDGET = 900

COMMERCIAL = {"Офис", "Торговая площадь", "Склад"}

# Topics exist for the cities that actually carry inventory; everything else
# shares one topic rather than sitting in an empty room of its own. There is
# deliberately no catch-all "all listings" topic -- the owner asked for it to
# be removed on 1 Sep 2026.
TOPIC_CITIES = ["ho-chi-minh", "ha-noi", "da-nang", "nha-trang", "binh-duong"]
TOPIC_TITLES = {
    "ho-chi-minh:residential": "Хошимин · жильё",
    "ha-noi:residential": "Ханой · жильё",
    "da-nang:residential": "Дананг · жильё",
    "nha-trang:residential": "Нячанг · жильё",
    "binh-duong:residential": "Биньзыонг · жильё",
    "other:residential": "Другие города",
    "commercial": "Коммерция · весь Вьетнам",
}


def api(token, method, payload):
    url = "https://api.telegram.org/bot%s/%s" % (token, method)
    data = urllib.parse.urlencode(payload).encode("utf-8")
    with urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=25) as r:
        out = json.loads(r.read().decode("utf-8"))
    if not out.get("ok"):
        raise RuntimeError("%s: %s" % (method, out.get("description")))
    return out["result"]


def load_topics():
    try:
        return json.load(open(TOPICS_FILE, encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(TOPICS_FILE + " not found -- copy telegram_topics.example.json "
                 "to it and put your group chat_id in it first")


def kind_of(l):
    return "commercial" if l["type"] in COMMERCIAL else "residential"


def topic_key(l):
    if kind_of(l) == "commercial":
        return "commercial"
    city = l["city"] if l["city"] in TOPIC_CITIES else "other"
    return city + ":residential"


def thread_for(l, topics):
    """The listing's own topic, or the group's General topic if that is
    somehow missing (there is no catch-all topic to fall back to any more)."""
    return topics.get(topic_key(l))


def load_listings():
    src = open(BUILT_HTML, encoding="utf-8").read()
    m = re.search(r"var DATA = (\{.*?\});", src, re.S)
    if not m:
        sys.exit("no DATA in " + BUILT_HTML + " -- run rebuild_final.py first")
    data = json.loads(m.group(1))
    cities = data["CITIES"]
    out = []
    for l in data["LISTINGS"]:
        if (l.get("details") or {}).get("duplicateOf"):
            continue                    # secondary copy of a listing already shown
        c = cities.get(l["city"], {})
        l["_city_ru"] = c.get("name", l["city"])
        l["_district"] = next((d["name"] for d in c.get("districts", [])
                               if d["key"] == l["district"]), "")
        out.append(l)
    return out


def fmt_price(v):
    if v is None:
        return "цена по запросу"
    m = v / 1000000
    s = str(int(m)) if m == int(m) else ("%.1f" % m)
    return s.replace(".", ",") + " млн ₫/мес"


def build_caption(l):
    area = (" · %s м²" % l["area"]) if l.get("area") else ""
    head = [
        "🏠 <b>%s</b> · %s · %s" % (l["type"], l["_city_ru"], fmt_price(l.get("price"))),
        "📍 %s%s" % (l["_district"], area),
        "",
    ]
    tail = ['<a href="%s">Открыть объявление</a> · <a href="%s">все объявления</a>'
            % (l["url"], SITE_URL)]
    notice = (l.get("details") or {}).get("notice")
    fixed = len("\n".join(head + tail)) + len(notice or "") + 4
    room = max(120, CAPTION_BUDGET - fixed)
    body = [clip(l["desc"], room)]
    if notice:
        body += ["", "⚠ " + notice]
    caption = "\n".join(head + body + [""] + tail)
    if len(caption) > CAPTION_BUDGET:
        # The estimate above can still miss; this is the hard stop. An overlong
        # caption is rejected by Telegram outright, so the post would be lost
        # rather than shortened.
        joined = "\n".join(tail)
        keep = CAPTION_BUDGET - len(joined) - 3     # the "…" plus the two newlines
        caption = caption[:keep].rstrip() + "…\n\n" + joined
    return caption


def clip(text, limit):
    """Cut to `limit` on a word boundary -- a caption that stops mid-word reads
    as a bug to the person seeing it, not as a length limit."""
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    space = cut.rfind(" ")
    if space > limit * 0.6:
        cut = cut[:space]
    return cut.rstrip(" ,.;:—-") + "…"


def details_photos(l):
    return (l.get("details") or {}).get("photos") or []


def send_listing(token, chat_id, thread, l):
    """Returns the list of message_id(s) Telegram created for this listing."""
    caption = build_caption(l)
    photos = details_photos(l)[:10]           # sendMediaGroup's own hard cap
    payload = {"chat_id": chat_id, "parse_mode": "HTML"}
    if thread:
        payload["message_thread_id"] = thread

    if len(photos) >= 2:
        # Only the FIRST item's caption is shown for the whole album --
        # confirmed against the Bot API reference, not assumed.
        media = [{"type": "photo", "media": photos[0], "caption": caption,
                  "parse_mode": "HTML"}]
        media += [{"type": "photo", "media": u} for u in photos[1:]]
        result = api(token, "sendMediaGroup", dict(payload, media=json.dumps(media)))
        return [m["message_id"] for m in result]
    if len(photos) == 1:
        result = api(token, "sendPhoto", dict(payload, photo=photos[0], caption=caption))
        return [result["message_id"]]
    result = api(token, "sendMessage",
                 dict(payload, text=caption, disable_web_page_preview="true"))
    return [result["message_id"]]


def do_setup(token, cfg):
    created = 0
    for key, title in TOPIC_TITLES.items():
        if cfg["topics"].get(key):
            print("  %-28s already has id %s" % (key, cfg["topics"][key]))
            continue
        res = api(token, "createForumTopic", {"chat_id": cfg["chat_id"], "name": title})
        cfg["topics"][key] = res["message_thread_id"]
        created += 1
        print("  %-28s created -> %s" % (key, res["message_thread_id"]))
        time.sleep(1)
    json.dump(cfg, open(TOPICS_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("created %d topic(s); ids written to %s" % (created, TOPICS_FILE))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="print what would be sent, send nothing")
    ap.add_argument("--setup", action="store_true",
                    help="create the hub topics and record their ids")
    ap.add_argument("--city", help="only this city key, e.g. ho-chi-minh")
    ap.add_argument("--limit", type=int, default=10, help="max posts per run (default 10)")
    ap.add_argument("--delay", type=float, default=4.0,
                    help="seconds between posts (default 4, under Telegram's ~20/min)")
    ap.add_argument("--repost", help="comma-separated listing ids to force-resend "
                    "(e.g. after a formatting bug) even if already marked posted")
    args = ap.parse_args()
    token = os.environ.get("TG_BOT_TOKEN")

    if args.setup:
        if not token:
            sys.exit("TG_BOT_TOKEN must be set to create topics")
        do_setup(token, load_topics())
        return

    listings = load_listings()
    if args.city:
        listings = [l for l in listings if l["city"] == args.city]

    try:
        state = json.load(open(STATE_FILE, encoding="utf-8"))
    except FileNotFoundError:
        state = {"posted": [], "initialised": False, "message_ids": {}}
    state.setdefault("message_ids", {})
    posted = set(state.get("posted", []))

    if args.repost:
        force = {int(x) for x in args.repost.split(",")}
        by_id = {l["id"]: l for l in listings}
        to_post = [by_id[i] for i in force if i in by_id]
        rest = []
    else:
        fresh = sorted((l for l in listings if l["id"] not in posted),
                       key=lambda l: (l.get("daysAgo", 99), -l["id"]))
        to_post, rest = fresh[: args.limit], []
        if not state.get("initialised"):
            rest = [l["id"] for l in fresh[args.limit:]]
            print("first run: %d existing listings will be marked as seen; "
                  "posting the %d newest" % (len(rest), len(to_post)))

    if not to_post:
        print("nothing new to post")
        return

    cfg = load_topics() if (args.dry_run and os.path.exists(TOPICS_FILE)) else None

    if args.dry_run:
        cfg = cfg or {"topics": {}}
        print("DRY RUN -- nothing will be sent. %d post(s):\n" % len(to_post))
        for l in to_post:
            cap = build_caption(l)
            photos = details_photos(l)
            print("-" * 66)
            print("topic: %s (thread id %s) | caption %d chars | %d photo(s)"
                  % (topic_key(l), cfg["topics"].get(topic_key(l)), len(cap), len(photos)))
            print(re.sub(r"</?b>", "", cap))
            print("[photos: %s]" % (", ".join(p[:40] + "..." for p in photos) or "none"))
        return

    if not token:
        sys.exit("TG_BOT_TOKEN must be set (or use --dry-run)")
    cfg = load_topics()

    sent = 0
    for l in to_post:
        thread = thread_for(l, cfg["topics"])
        try:
            msg_ids = send_listing(token, cfg["chat_id"], thread, l)
            posted.add(l["id"])
            state["message_ids"][str(l["id"])] = msg_ids
            sent += 1
            time.sleep(args.delay)
        except Exception as e:
            print("failed on listing %s: %s" % (l["id"], e))
            break

    posted.update(rest)
    state["posted"] = sorted(posted)
    state["initialised"] = True
    json.dump(state, open(STATE_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("posted %d listing(s); %d ids now marked as seen" % (sent, len(posted)))


if __name__ == "__main__":
    main()
