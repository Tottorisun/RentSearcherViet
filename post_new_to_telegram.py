# -*- coding: utf-8 -*-
"""
Post newly-added listings to a Telegram channel.

WHY: the competitor's strongest retention feature is "new matches reach you
immediately, instead of when you finally scroll to them" -- good listings are
taken within the hour. A real push service needs a backend we do not have,
but the daily checks already run on a schedule, so publishing new listings to
a Telegram channel gives the same "it comes to you" effect on infrastructure
that already exists -- and the channel doubles as a growth surface.

USAGE
  # see exactly what would be posted, no token needed, nothing sent:
  python post_new_to_telegram.py --dry-run

  # really post (needs the two env vars below):
  set TG_BOT_TOKEN=...            # from @BotFather
  set TG_CHANNEL=@your_channel    # bot must be an ADMIN of this channel
  python post_new_to_telegram.py

  # optional: restrict to one city, e.g. --city ho-chi-minh
  # optional: --limit N  (default 10 per run, so a first run cannot flood)

STATE: posted_to_telegram.json remembers which listing ids were already sent,
so re-running never double-posts. The first real run only sends --limit newest
listings and marks EVERYTHING ELSE as already-seen, so switching this on does
not dump 1800 listings into the channel.

The token is read from the environment and never stored in this repo.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

# This machine's console is cp1251, which cannot encode the emoji used in the
# post captions -- without this, --dry-run dies with a UnicodeEncodeError
# before printing anything useful.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

STATE_FILE = "posted_to_telegram.json"
BUILT_HTML = "index.html"
SITE_URL = "https://tottorisun.github.io/RentSearcherViet/"

CITY_RU = {
    "nha-trang": "Нячанг", "da-lat": "Далат", "da-nang": "Дананг",
    "hoi-an": "Хойан", "vung-tau": "Вунгтау", "quy-nhon": "Куинён",
    "phan-thiet": "Фантьет", "ho-chi-minh": "Хошимин",
}


def load_listings():
    src = open(BUILT_HTML, encoding="utf-8").read()
    m = re.search(r"var DATA = (\{.*?\});", src, re.S)
    if not m:
        sys.exit("could not find DATA in " + BUILT_HTML + " -- run rebuild_final.py first")
    data = json.loads(m.group(1))
    cities = data["CITIES"]
    out = []
    for l in data["LISTINGS"]:
        if (l.get("details") or {}).get("duplicateOf"):
            continue  # secondary copy of a listing we already show
        dname = ""
        for d in cities.get(l["city"], {}).get("districts", []):
            if d["key"] == l["district"]:
                dname = d["name"]
                break
        l["_district_name"] = dname
        out.append(l)
    return out


def fmt_price(v):
    if v is None:
        return "цена по запросу"
    m = v / 1000000
    s = str(int(m)) if m == int(m) else ("%.1f" % m).replace(".", ",")
    return s + " млн ₫/мес"


def build_caption(l):
    parts = [
        "🏠 <b>%s</b> · %s" % (l["type"], CITY_RU.get(l["city"], l["city"])),
        "📍 %s%s" % (l["_district_name"], (" · %s м²" % l["area"]) if l.get("area") else ""),
        "💰 <b>%s</b>" % fmt_price(l.get("price")),
        "",
        l["desc"][:400],
        "",
        '<a href="%s">Открыть объявление</a> · <a href="%s">все объявления</a>' % (l["url"], SITE_URL),
    ]
    return "\n".join(parts)


def api(token, method, payload):
    url = "https://api.telegram.org/bot%s/%s" % (token, method)
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="print what would be sent, send nothing")
    ap.add_argument("--city", help="only this city key, e.g. ho-chi-minh")
    ap.add_argument("--limit", type=int, default=10, help="max posts per run (default 10)")
    args = ap.parse_args()

    listings = load_listings()
    if args.city:
        listings = [l for l in listings if l["city"] == args.city]

    try:
        state = json.load(open(STATE_FILE, encoding="utf-8"))
    except FileNotFoundError:
        state = {"posted": [], "initialised": False}
    posted = set(state.get("posted", []))

    fresh = [l for l in listings if l["id"] not in posted]
    # newest first
    fresh.sort(key=lambda l: (l.get("daysAgo", 99), -l["id"]))

    if not state.get("initialised"):
        # First ever run: post only the newest few, treat the rest as seen,
        # so enabling this never floods the channel with the whole backlog.
        to_post = fresh[: args.limit]
        rest = [l["id"] for l in fresh[args.limit:]]
        print("first run: %d listings already in the catalogue will be marked as seen, "
              "posting only the %d newest" % (len(rest), len(to_post)))
    else:
        to_post = fresh[: args.limit]
        rest = []

    if not to_post:
        print("nothing new to post")
        return

    token = os.environ.get("TG_BOT_TOKEN")
    channel = os.environ.get("TG_CHANNEL")

    if args.dry_run:
        print("DRY RUN -- nothing will be sent. %d post(s):\n" % len(to_post))
        for l in to_post:
            print("-" * 60)
            print(build_caption(l).replace("<b>", "").replace("</b>", ""))
            ph = (l.get("details") or {}).get("photos") or []
            print("[photo: %s]" % (ph[0] if ph else "none"))
        return

    if not token or not channel:
        sys.exit("TG_BOT_TOKEN and TG_CHANNEL must be set (or use --dry-run)")

    sent = 0
    for l in to_post:
        caption = build_caption(l)
        photos = (l.get("details") or {}).get("photos") or []
        try:
            if photos:
                api(token, "sendPhoto", {
                    "chat_id": channel, "photo": photos[0],
                    "caption": caption, "parse_mode": "HTML",
                })
            else:
                api(token, "sendMessage", {
                    "chat_id": channel, "text": caption,
                    "parse_mode": "HTML", "disable_web_page_preview": "true",
                })
            posted.add(l["id"])
            sent += 1
            time.sleep(3)  # stay well under Telegram's ~20 messages/minute channel limit
        except Exception as e:
            print("failed on listing %s: %s" % (l["id"], e))
            break

    posted.update(rest)
    json.dump({"posted": sorted(posted), "initialised": True},
              open(STATE_FILE, "w", encoding="utf-8"), indent=1)
    print("posted %d listing(s); %d ids now marked as seen" % (sent, len(posted)))


if __name__ == "__main__":
    main()
