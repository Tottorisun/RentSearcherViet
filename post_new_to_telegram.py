# -*- coding: utf-8 -*-
"""
Publish new listings into the Telegram hub for Vietnamese property.

STRUCTURE. One forum supergroup is the hub, and each city -- plus commercial as
a whole -- gets its own topic inside it, rather than a separate group per city.
Ten half-empty groups look abandoned and split the audience; one group with
topics keeps a single join link while letting people mute what they do not
need. The bot posts into a topic via `message_thread_id`: one token, one chat,
every section.

BILINGUAL ON PURPOSE. Every post carries Russian and English. The audience is
Russian- and English-speaking expats, and a single-language post silently
excludes half of them -- the same failure the site itself had until the English
page was fixed on 31 Aug 2026.

RATE LIMIT. Telegram allows a bot about 20 messages per minute into a group.
The default delay stays under that deliberately, and --limit exists so a first
run cannot try to dump the whole catalogue and get throttled.

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

STATE: posted_to_telegram.json remembers what was already sent. The first real
run posts only --limit newest and marks the rest as seen, so switching this on
does not dump two thousand listings into the hub.
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
SITE_URL_EN = "https://tottorisun.github.io/RentSearcherViet/en.html"

# The photo-caption limit is not stated in the Bot API reference, and an
# overlong caption is rejected outright rather than truncated, so this budget
# stays well short of the 1024 characters the API is generally held to allow.
CAPTION_BUDGET = 850

COMMERCIAL = {"Офис", "Торговая площадь", "Склад"}
TYPE_EN = {"Комната": "Room", "Студия": "Studio", "Квартира": "Apartment",
           "Дом": "House", "Другое": "Other", "Офис": "Office",
           "Торговая площадь": "Retail space", "Склад": "Warehouse"}

# Topics exist for the cities that actually carry inventory; everything else
# shares one topic rather than sitting in an empty room of its own.
TOPIC_CITIES = ["ho-chi-minh", "ha-noi", "da-nang", "nha-trang", "binh-duong"]
TOPIC_TITLES = {
    "ho-chi-minh:residential": "Хошимин · жильё / HCMC housing",
    "ha-noi:residential": "Ханой · жильё / Hanoi housing",
    "da-nang:residential": "Дананг · жильё / Da Nang housing",
    "nha-trang:residential": "Нячанг · жильё / Nha Trang housing",
    "binh-duong:residential": "Биньзыонг · жильё / Binh Duong housing",
    "other:residential": "Другие города / Other cities",
    "commercial": "Коммерция · весь Вьетнам / Commercial",
    "default": "Все объявления / All listings",
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
    """Exact topic, then the catch-all, then the group's General topic."""
    for key in (topic_key(l), "default"):
        tid = topics.get(key)
        if tid:
            return tid
    return None


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
        l["_city_en"] = c.get("nameEn", l["city"])
        l["_district"] = next((d["name"] for d in c.get("districts", [])
                               if d["key"] == l["district"]), "")
        out.append(l)
    return out


def fmt_price(v, en=False):
    if v is None:
        return "price on request" if en else "цена по запросу"
    m = v / 1000000
    s = str(int(m)) if m == int(m) else ("%.1f" % m)
    return (s + "M ₫/mo") if en else (s.replace(".", ",") + " млн ₫/мес")


def build_caption(l):
    area = (" · %s м² / m²" % l["area"]) if l.get("area") else ""
    head = [
        "🏠 <b>%s</b> · %s · %s" % (l["type"], l["_city_ru"], fmt_price(l.get("price"))),
        "🏠 <b>%s</b> · %s · %s" % (TYPE_EN.get(l["type"], l["type"]), l["_city_en"],
                                    fmt_price(l.get("price"), en=True)),
        "📍 %s%s" % (l["_district"], area),
        "",
    ]
    tail = ['<a href="%s">Открыть объявление · Open the ad</a>' % l["url"],
            '<a href="%s">все объявления</a> · <a href="%s">all listings</a>'
            % (SITE_URL, SITE_URL_EN)]
    details = l.get("details") or {}
    notice, notice_en = details.get("notice"), details.get("noticeEn")
    fixed = len("\n".join(head + tail)) + len(notice or "") + len(notice_en or "") + 8
    room = max(120, CAPTION_BUDGET - fixed)
    body = [clip(l["desc"], room // 2)]
    if l.get("descEn"):
        body.append(clip(l["descEn"], room // 2))
    if notice:
        body += ["", "⚠ " + notice]
        if notice_en:
            body.append("⚠ " + notice_en)
    caption = "\n".join(head + body + [""] + tail)
    if len(caption) > CAPTION_BUDGET:
        # The per-part budget is an estimate; this is the hard stop. An overlong
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
        state = {"posted": [], "initialised": False}
    posted = set(state.get("posted", []))

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

    if args.dry_run:
        cfg = load_topics() if os.path.exists(TOPICS_FILE) else {"topics": {}}
        print("DRY RUN -- nothing will be sent. %d post(s):\n" % len(to_post))
        for l in to_post:
            cap = build_caption(l)
            print("-" * 66)
            print("topic: %s (thread id %s) | caption %d chars"
                  % (topic_key(l), cfg["topics"].get(topic_key(l)), len(cap)))
            print(re.sub(r"</?b>", "", cap))
            ph = details_photos(l)
            print("[photo: %s]" % ((ph[0][:66] + "...") if ph else "none"))
        return

    if not token:
        sys.exit("TG_BOT_TOKEN must be set (or use --dry-run)")
    cfg = load_topics()

    sent = 0
    for l in to_post:
        caption = build_caption(l)
        thread = thread_for(l, cfg["topics"])
        photos = details_photos(l)
        payload = {"chat_id": cfg["chat_id"], "parse_mode": "HTML"}
        if thread:
            payload["message_thread_id"] = thread
        try:
            if photos:
                api(token, "sendPhoto", dict(payload, photo=photos[0], caption=caption))
            else:
                api(token, "sendMessage",
                    dict(payload, text=caption, disable_web_page_preview="true"))
            posted.add(l["id"])
            sent += 1
            time.sleep(args.delay)
        except Exception as e:
            print("failed on listing %s: %s" % (l["id"], e))
            break

    posted.update(rest)
    json.dump({"posted": sorted(posted), "initialised": True},
              open(STATE_FILE, "w", encoding="utf-8"), indent=1)
    print("posted %d listing(s); %d ids now marked as seen" % (sent, len(posted)))


def details_photos(l):
    return (l.get("details") or {}).get("photos") or []


if __name__ == "__main__":
    main()
