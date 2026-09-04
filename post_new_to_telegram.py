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

  Токен берётся из переменной окружения того хаба, в который постим, и никогда
  не пишется в репозиторий: TG_BOT_TOKEN для вьетнамского хаба,
  TG_BOT_TOKEN_PH для филиппинского (@RentPhilippineBot). Хаб выбирается
  ключом --hub vn|ph, по умолчанию vn.

STATE: posted_to_telegram.json remembers what was already sent, and which
message ids each listing produced -- the first run of this script posted with
the wrong photo count and there was no way to find and delete those messages
afterwards, so the ids are now kept for exactly that situation.

FAILURE HANDLING (audit, 2 Sep 2026). A hub post cannot be un-sent, so every
uncertain path stops rather than guesses:
  * state is written after EVERY successful send (tmp + os.replace), never
    only at the end of the run -- a crash or Ctrl+C no longer re-posts the
    whole batch next time;
  * a 4xx from Telegram (bad caption, unknown thread) is read out of the
    HTTPError body and SKIPS that listing, so one bad row no longer blocks
    every listing behind it on every run;
  * 429 sleeps for `retry_after` and retries once;
  * a timeout / connection reset / 5xx after a send leaves the listing in
    `suspect`: Telegram may or may not have delivered it. The run stops and
    the script refuses to post again until you look at the hub and run
    --suspect-posted <ids> (it is there) or --suspect-clear (it is not);
  * dynamic caption fields are HTML-escaped (22 descriptions already contain
    a bare "&"; the first "<" would have been a 400 that blocked the queue);
  * --repost appends message ids instead of overwriting them, so the old
    copy stays deletable by cleanup_telegram_posts.py.
"""
import argparse
import html
import json
import os
import re
import socket
import sys
import time
import urllib.error
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
BUILT_HTML = "vietnam-rent-finder.html"   # index.html is a byte-identical copy; read the canonical one
SITE_URL = "https://tottorisun.github.io/RentSearcherViet/"

# The photo-caption limit is not stated in the Bot API reference, and an
# overlong caption is rejected outright rather than truncated, so this budget
# stays well short of the 1024 characters the API is generally held to allow.
CAPTION_BUDGET = 900

COMMERCIAL = {"Офис", "Торговая площадь", "Склад"}

# Every city on the site gets its own topic -- there is deliberately no
# catch-all "other cities" topic any more (removed 2 Sep 2026 at the owner's
# request: it read as a junk drawer). A city missing from TOPIC_TITLES is a
# bug -- topic_key() below raises rather than silently routing it anywhere.
# ХАБЫ. Один хаб = одна страна = свой бот, своя группа, свой файл разделов.
#
# Почему раздельно, а не один канал с разделами по странам: 4 сентября 2026
# восемь филиппинских объявлений ушли в хаб «Недвижимость Вьетнам», потому что
# города появились на сайте и постеру нечем было их отклонить. Аудитория хаба
# приходила за Вьетнамом. Владелец завёл отдельного бота @RentPhilippineBot --
# страны больше не смешиваются ни при каких обстоятельствах.
#
# Токен каждого хаба берётся из своей переменной окружения и никогда не
# попадает в репозиторий.
HUBS = {
    "vn": {
        "country": "vn",
        "title": "Недвижимость Вьетнам",
        "token_env": "TG_BOT_TOKEN",
        "lang": "ru",
        "topics_file": "telegram_topics.json",
        "topics": {
            "ho-chi-minh:residential": "Хошимин · жильё",
            "ha-noi:residential": "Ханой · жильё",
            "da-nang:residential": "Дананг · жильё",
            "nha-trang:residential": "Нячанг · жильё",
            "binh-duong:residential": "Биньзыонг · жильё",
            "da-lat:residential": "Далат · жильё",
            "vung-tau:residential": "Вунгтау · жильё",
            "quy-nhon:residential": "Куинён · жильё",
            "hoi-an:residential": "Хойан · жильё",
            "phan-thiet:residential": "Фантьет / Муйне · жильё",
            "phu-quoc:residential": "Фукуок · жильё",
            "commercial": "Коммерция · весь Вьетнам",
        },
    },
    "ph": {
        "country": "ph",
        "title": "Rent Philippine (@RentPhilippineBot)",
        "token_env": "TG_BOT_TOKEN_PH",
        "topics_file": "telegram_topics_ph.json",
        # Филиппинский хаб ведётся на английском: аудитория там не русскоязычная.
        # Это меняет не только подписи постов, но и названия разделов.
        "lang": "en",
        "topics": {
            "dumaguete:residential": "Dumaguete · Housing",
            "cebu:residential": "Cebu · Housing",
            "manila:residential": "Manila · Housing",
            "commercial": "Commercial · Philippines",
        },
    },
}

# Выбирается ключом --hub; значения ниже подставляет main() до всякой работы.
HUB = "vn"
HUB_LANG = HUBS["vn"]["lang"]
HUB_COUNTRY = HUBS["vn"]["country"]
TOPIC_TITLES = dict(HUBS["vn"]["topics"])
TOPICS_FILE = HUBS["vn"]["topics_file"]
TOKEN_ENV = HUBS["vn"]["token_env"]


def select_hub(name):
    """Переключает модуль на выбранный хаб. Всё, что дальше по коду читает
    HUB_COUNTRY/TOPIC_TITLES/TOPICS_FILE/TOKEN_ENV, получает значения этого хаба."""
    global HUB, HUB_LANG, HUB_COUNTRY, TOPIC_TITLES, TOPICS_FILE, TOKEN_ENV
    if name not in HUBS:
        sys.exit("неизвестный хаб %r -- есть: %s" % (name, ", ".join(HUBS)))
    h = HUBS[name]
    HUB = name
    HUB_LANG = h.get("lang", "ru")
    HUB_COUNTRY = h["country"]
    TOPIC_TITLES = dict(h["topics"])
    TOPICS_FILE = h["topics_file"]
    TOKEN_ENV = h["token_env"]


class BotRefused(Exception):
    """Telegram answered with a definite refusal (4xx: bad caption, unknown
    thread, too many photos...). This LISTING is wrong; the run is fine --
    skip it, report it, carry on. Nothing was delivered."""


class DeliveryUnknown(Exception):
    """The request may or may not have reached Telegram (timeout, reset,
    5xx). Nothing about this listing can be marked with confidence."""


def api(token, method, payload):
    url = "https://api.telegram.org/bot%s/%s" % (token, method)
    data = urllib.parse.urlencode(payload).encode("utf-8")
    for attempt in (1, 2):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=25) as r:
                out = json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code >= 500:
                raise DeliveryUnknown("%s: HTTP %s from Telegram" % (method, e.code))
            # 4xx: the real reason is in the JSON body, not in str(e)
            try:
                out = json.loads(e.read().decode("utf-8"))
            except Exception:
                out = {"ok": False, "error_code": e.code, "description": str(e)}
        except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError, OSError) as e:
            raise DeliveryUnknown("%s: %s" % (method, e))
        if out.get("ok"):
            return out["result"]
        if out.get("error_code") == 429 and attempt == 1:
            # A 429 means the request was NOT processed, so retrying is safe.
            wait = int((out.get("parameters") or {}).get("retry_after", 5)) + 1
            print("  rate-limited by Telegram, sleeping %ds" % wait)
            time.sleep(wait)
            continue
        raise BotRefused("%s: %s" % (method, out.get("description")))
    raise BotRefused("%s: still rate-limited after one retry" % method)


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
    key = l["city"] + ":residential"
    if key not in TOPIC_TITLES:
        # Fail loudly: a silent fallback here means a listing quietly lands
        # in the wrong topic (or worse, a resurrected catch-all) instead of
        # someone noticing a new city was added to the site without a topic
        # for it in this script.
        sys.exit("no Telegram topic configured for city %r (listing %s) -- "
                  "add it to TOPIC_TITLES and run --setup" % (l["city"], l.get("id")))
    return key


def thread_for(l, topics):
    """The listing's own topic. There is no catch-all topic to fall back to --
    and no thread id at all would post into the group's General topic, which
    is the same junk drawer under another name, so that is refused too."""
    key = topic_key(l)
    thread = topics.get(key)
    if not thread:
        sys.exit("%s has no thread id for %r -- run --setup first; refusing to post "
                 "into the General topic" % (TOPICS_FILE, key))
    return thread


def load_listings():
    from site_data import load_data
    data = load_data(BUILT_HTML)
    cities = data["CITIES"]
    out, skipped_country = [], []
    for l in data["LISTINGS"]:
        if (l.get("details") or {}).get("duplicateOf"):
            continue                    # secondary copy of a listing already shown
        c = cities.get(l["city"], {})
        # Хаб называется «Недвижимость Вьетнам». 4 сентября 2026 сюда ушли восемь
        # филиппинских объявлений (Себу и Манила) -- потому что города завели на
        # сайте, а у постера не было ни одной причины отказать. Аудитория хаба
        # ждёт Вьетнам; вторая страна -- это отдельный канал и отдельное решение
        # владельца, а не следствие того, что город появился в CITIES.
        if c.get("country", "vn") != HUB_COUNTRY:
            skipped_country.append(l.get("id"))
            continue
        en = HUB_LANG == "en"
        l["_city_name"] = (c.get("nameEn") if en else None) or c.get("name", l["city"])
        _d = next((d for d in c.get("districts", []) if d["key"] == l["district"]), None)
        # у района английского имени нет -- оно и так латиницей (Makati, Piapi)
        l["_district"] = (_d or {}).get("name", "")
        out.append(l)
    if skipped_country:
        print("skipping %d listing(s) outside %s -- this hub carries one country only "
              "(--hub %s); the others have their own hub"
              % (len(skipped_country), HUB_COUNTRY.upper(), HUB))
    return out


CUR_SYM = {"VND": "₫", "PHP": "₱"}


def fmt_price(v, cur="VND"):
    """Цена в валюте объявления, на языке хаба. Донг показываем миллионами, как
    на сайте; песо -- целым числом: 15 000 ₱ в виде «0,015 млн» нечитаемо."""
    en = HUB_LANG == "en"
    if v is None:
        return "price on request" if en else "цена по запросу"
    per = "/mo" if en else "/мес"
    if cur == "VND":
        m = v / 1000000
        s = str(int(m)) if m == int(m) else ("%.1f" % m)
        if not en:
            s = s.replace(".", ",")
        return s + (" mln ₫" if en else " млн ₫") + per
    n = "{:,}".format(int(v)).replace(",", " ")
    return "%s %s%s" % (n, CUR_SYM.get(cur, cur), per)


def esc(s):
    """Caption goes out as parse_mode=HTML: a bare '<' or '&' in a description
    is a 400 from Telegram, not text. Escape every dynamic field."""
    return html.escape(str(s), quote=False)


# Типы в данных хранятся по-русски -- для англоязычного хаба переводим.
# Список закрытый, тот же, что проверяет сборка сайта.
TYPE_EN = {"Комната": "Room", "Студия": "Studio", "Квартира": "Apartment",
           "Дом": "House", "Другое": "Other", "Офис": "Office",
           "Торговая площадь": "Retail space", "Склад": "Warehouse"}

LABELS = {
    "ru": {"open": "Открыть объявление", "all": "все объявления", "m2": "м²"},
    "en": {"open": "Open the listing", "all": "all listings", "m2": "m²"},
}


def build_caption(l):
    en = HUB_LANG == "en"
    lab = LABELS["en" if en else "ru"]
    area = (" · %s %s" % (l["area"], lab["m2"])) if l.get("area") else ""
    type_name = TYPE_EN.get(l["type"], l["type"]) if en else l["type"]
    head = [
        "🏠 <b>%s</b> · %s · %s" % (esc(type_name), esc(l["_city_name"]),
                                    fmt_price(l.get("price"), l.get("cur", "VND"))),
        "📍 %s%s" % (esc(l["_district"]), area),
        "",
    ]
    tail = ['<a href="%s">%s</a> · <a href="%s">%s</a>'
            % (html.escape(l["url"], quote=True), lab["open"], SITE_URL, lab["all"])]
    det = l.get("details") or {}
    # На английском хабе берём английские описание и оговорку. Подсунуть русский
    # текст англоязычной аудитории хуже, чем пропустить объявление.
    notice = (det.get("noticeEn") if en else det.get("notice")) or None
    notice_lines = ["", "⚠ " + esc(notice)] if notice else []
    fixed = len("\n".join(head + notice_lines + [""] + tail)) + 1
    room = max(120, CAPTION_BUDGET - fixed)
    # Clip the RAW description, then escape -- never slice escaped text: a cut
    # through "&amp;" leaves a broken entity and Telegram rejects the caption.
    # Escaping only ever lengthens the text, so shrinking `room` converges.
    while True:
        body = (l.get("descEn") if en else None) or l["desc"]
        caption = "\n".join(head + [esc(clip(body, room))] + notice_lines + [""] + tail)
        if len(caption) <= CAPTION_BUDGET or room <= 60:
            return caption
        room -= 40


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
    ap.add_argument("--hub", default="vn", choices=sorted(HUBS),
                    help="which hub to post to: vn (Вьетнам) or ph (Филиппины). "
                         "Each has its own bot, group and topics file; a listing "
                         "only ever goes to the hub of its own country.")
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
    ap.add_argument("--min-photos", type=int, default=3,
                    help="skip listings with fewer photos than this (default 3) -- a "
                    "1-2 photo post looks thin in a public feed; the site itself still "
                    "shows these listings regardless, only the hub feed is pickier")
    ap.add_argument("--suspect-posted", help="comma-separated ids from `suspect` that you "
                    "SAW in the hub: mark them posted and clear them")
    ap.add_argument("--suspect-clear", action="store_true",
                    help="the `suspect` listings are NOT in the hub: clear them so they are sent again")
    args = ap.parse_args()
    select_hub(args.hub)
    print("hub: %s -- %s" % (HUB, HUBS[HUB]["title"]))
    token = os.environ.get(TOKEN_ENV)

    if args.setup:
        if not token:
            sys.exit(TOKEN_ENV + " must be set to create topics")
        do_setup(token, load_topics())
        return

    try:
        state = json.load(open(STATE_FILE, encoding="utf-8"))
    except FileNotFoundError:
        state = {"posted": [], "initialised": False, "message_ids": {}}
    except json.JSONDecodeError as e:
        sys.exit("%s is not valid JSON (%s) -- restore it from a .bak copy. Do NOT delete it: "
                 "that would drop every recorded message id and re-post the whole catalogue."
                 % (STATE_FILE, e))
    state.setdefault("message_ids", {})
    state.setdefault("suspect", [])
    posted = set(state.get("posted", []))

    def save_state():
        state["posted"] = sorted(posted)
        tmp = STATE_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=1)
        os.replace(tmp, STATE_FILE)

    if args.suspect_posted:
        ids = {int(x) for x in args.suspect_posted.split(",")}
        posted.update(ids)
        state["suspect"] = [s for s in state["suspect"] if s not in ids]
        save_state()
        print("marked %d suspect listing(s) as posted (no message ids on record for them); "
              "%d still suspect" % (len(ids), len(state["suspect"])))
        return
    if args.suspect_clear:
        n = len(state["suspect"])
        state["suspect"] = []
        save_state()
        print("cleared %d suspect listing(s); they are eligible to be sent again" % n)
        return
    if state["suspect"]:
        sys.exit("refusing to post: %d listing(s) have UNKNOWN delivery status: %s\n"
                 "Look for them in the hub, then run --suspect-posted <ids> for the ones that are "
                 "there and --suspect-clear for the rest." % (len(state["suspect"]), state["suspect"]))

    listings = load_listings()
    if args.city:
        listings = [l for l in listings if l["city"] == args.city]

    if args.repost:
        force = {int(x) for x in args.repost.split(",")}
        by_id = {l["id"]: l for l in listings}
        to_post = [by_id[i] for i in force if i in by_id]
        rest = []
    else:
        # Not-enough-photos listings are left OUT of `posted` on purpose: a later
        # daily-check run can still backfill photos for one of them, and the next
        # gradual-posting pass will then pick it up instead of it being excluded
        # forever by a decision made when it had fewer photos.
        candidates = [l for l in listings if l["id"] not in posted]
        thin = sum(1 for l in candidates if len(details_photos(l)) < args.min_photos)
        candidates = [l for l in candidates if len(details_photos(l)) >= args.min_photos]
        fresh = sorted(candidates, key=lambda l: (l.get("daysAgo", 99), -l["id"]))
        to_post, rest = fresh[: args.limit], []
        if thin:
            print("skipping %d listing(s) with fewer than %d photos "
                  "(not marked posted -- eligible again if photos are added later)"
                  % (thin, args.min_photos))
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
        sys.exit(TOKEN_ENV + " must be set (or use --dry-run)")
    cfg = load_topics()

    # Resolve every thread id BEFORE the first send: a missing topic must abort
    # the run with nothing delivered, not halfway through a batch.
    threads = {l["id"]: thread_for(l, cfg["topics"]) for l in to_post}

    sent, refused = 0, []
    for l in to_post:
        lid = l["id"]
        try:
            msg_ids = send_listing(token, cfg["chat_id"], threads[lid], l)
        except BotRefused as e:
            # Definitely not delivered. Skip THIS listing, keep the run going --
            # one bad caption must not block every listing behind it forever.
            print("Telegram refused listing %s (skipped, not marked posted): %s" % (lid, e))
            refused.append(lid)
            time.sleep(1)
            continue
        except (DeliveryUnknown, KeyboardInterrupt) as e:
            # Maybe delivered, maybe not. Sending again would risk a duplicate
            # that cannot be un-sent; marking it posted would risk losing it.
            # Park it and stop until a human has looked at the hub.
            state["suspect"].append(lid)
            save_state()
            print("STOPPED: listing %s may or may not have reached the hub (%s: %s). It is recorded "
                  "as SUSPECT; look for it in the hub, then run --suspect-posted %s if it is there "
                  "or --suspect-clear if it is not. Posted before this: %d."
                  % (lid, type(e).__name__, e, lid, sent))
            return
        posted.add(lid)
        # append, never overwrite: after --repost the OLD copy must stay deletable
        state["message_ids"].setdefault(str(lid), []).extend(msg_ids)
        sent += 1
        save_state()                    # after every send, never only at the end
        time.sleep(args.delay)

    posted.update(rest)
    state["initialised"] = True
    save_state()
    print("posted %d listing(s); %d ids now marked as seen" % (sent, len(posted)))
    if refused:
        print("%d listing(s) refused by Telegram and left unposted (fix the data, they will be "
              "retried next run): %s" % (len(refused), refused))


if __name__ == "__main__":
    main()
