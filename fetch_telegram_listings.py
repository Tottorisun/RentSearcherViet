# -*- coding: utf-8 -*-
"""
fetch_telegram_listings.py -- read-only harvester of public Telegram CHANNEL
web previews (https://t.me/s/<channel>) for the Rent Searcher project.

It fetches, parses and de-duplicates rental posts and writes
`telegram_candidates.json` -- a list of *candidates* that a human (or the
daily-check agent) must verify before anything is inserted into
rebuild_final.py.

This script NEVER writes to rebuild_final.py, never inserts listings and never
assigns a project district key: the address text needs judgement, so district
assignment stays with the reviewer. `district_hits` / `landmark_hits` /
`address_lines` are hints only.

Usage:
    python fetch_telegram_listings.py --pages 2
    python fetch_telegram_listings.py --channels danangrentaflat,nyachang_arenda --pages 3
"""

import sys

# This machine's console is cp1251 and cannot print emoji / Vietnamese.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import argparse
import hashlib
import html as _html
import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- channels --

# channel -> city key used by the project (hint only; the reviewer confirms)
CHANNELS = {
    # Da Nang
    "danangrentaflat":        "da-nang",
    "vietnam_nedvijimost":    "da-nang",
    "danang_house":           "da-nang",
    "danang_rent":            "da-nang",
    # Nha Trang
    "nyachang_arenda":        "nha-trang",
    "Nhatranghomes":          "nha-trang",
    "arenda_vietnam":         "nha-trang",
    "Viet_life_niachang":     "nha-trang",
    "Arenda_Nyachang_Zhilye": "nha-trang",
    "arenda_nhatrang":        "nha-trang",
}

# Known cross-posting pairs: the same flat is published in both channels.
CROSSPOST_PAIRS = [
    ("danang_house", "vietnam_nedvijimost"),
    ("nyachang_arenda", "arenda_vietnam"),
]

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

DEFAULT_USD_RATE = 25200  # the rate already used by existing listings

# ------------------------------------------------------------------- utils --

_DMAP = {"đ": "d", "Đ": "D"}  # Vietnamese d-with-stroke


def fold(s):
    """Strip diacritics WITHOUT changing string length, so regex match offsets
    stay valid against the original string (needed to report raw substrings)."""
    out = []
    for ch in s:
        if ch in _DMAP:
            out.append(_DMAP[ch])
            continue
        d = unicodedata.normalize("NFD", ch)
        b = "".join(c for c in d if not unicodedata.combining(c))
        out.append(b if len(b) == 1 else ch)
    return "".join(out)


def http_get(url, timeout=25, tries=3):
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8,vi;q=0.7",
        })
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:          # network hiccup, 429, 5xx ...
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError("GET failed %s: %s" % (url, last))


def strip_tags(fragment):
    s = re.sub(r"(?is)<br\s*/?>", "\n", fragment)
    s = re.sub(r"(?is)</(p|div|blockquote)\s*>", "\n", s)
    s = re.sub(r"(?is)<[^>]+>", "", s)
    s = _html.unescape(s)
    s = s.replace("​", "").replace("\xa0", " ")
    lines = [ln.rstrip() for ln in s.split("\n")]
    out, blank = [], 0
    for ln in lines:                     # collapse runs of blank lines
        if ln.strip():
            blank = 0
            out.append(ln)
        else:
            blank += 1
            if blank <= 1:
                out.append("")
    return "\n".join(out).strip()


def inner_div(html, tag_start):
    """Return the inner HTML of the <div ...> starting at tag_start, honouring
    nested <div>s (Telegram nests expandable-text blocks inside message text)."""
    i = html.find(">", tag_start)
    if i < 0:
        return ""
    depth = 1
    pos = i + 1
    pat = re.compile(r"<(/?)div\b", re.I)
    while True:
        m = pat.search(html, pos)
        if not m:
            return html[i + 1:]
        if m.group(1):
            depth -= 1
            if depth == 0:
                return html[i + 1:m.start()]
        else:
            depth += 1
        pos = m.end()


# ------------------------------------------------------------ page parsing --

MSG_OPEN = re.compile(
    r'<div class="tgme_widget_message[^"]*js-widget_message"[^>]*data-post="([^"/]+)/(\d+)"',
    re.I)
PHOTO_RE = re.compile(
    r"tgme_widget_message_photo_wrap[^>]*?background-image:\s*url\('([^']+)'\)", re.I)
VIDEO_RE = re.compile(
    r"tgme_widget_message_video_thumb[^>]*?background-image:\s*url\('([^']+)'\)", re.I)
TIME_RE = re.compile(r'<time[^>]*datetime="([^"]+)"', re.I)
TEXT_RE = re.compile(r'<div class="tgme_widget_message_text[^"]*js-message_text"', re.I)
MORE_RE = re.compile(r'js-messages_more"[^>]*data-before="(\d+)"', re.I)
FWD_RE = re.compile(
    r'tgme_widget_message_forwarded_from_name"[^>]*>(?:<span[^>]*>)?([^<]*)', re.I)


def parse_page(html, channel):
    """Return (posts, next_before)."""
    starts = list(MSG_OPEN.finditer(html))
    posts = []
    for idx, m in enumerate(starts):
        end = starts[idx + 1].start() if idx + 1 < len(starts) else len(html)
        sl = html[m.start():end]
        chan_real, msg_id = m.group(1), int(m.group(2))

        tm = TEXT_RE.search(sl)
        text = strip_tags(inner_div(sl, tm.start())) if tm else ""

        photos, seen = [], set()
        for pm in PHOTO_RE.finditer(sl):
            u = _html.unescape(pm.group(1))
            if u not in seen:
                seen.add(u)
                photos.append(u)
        videos = []
        for vm in VIDEO_RE.finditer(sl):
            u = _html.unescape(vm.group(1))
            if u not in seen:
                seen.add(u)
                videos.append(u)

        times = TIME_RE.findall(sl)
        fwd = FWD_RE.search(sl)

        posts.append({
            "channel": chan_real,
            "msg_id": msg_id,
            "permalink": "https://t.me/%s/%d" % (chan_real, msg_id),
            "date": times[-1] if times else None,
            "text": text,
            "photos": photos,
            "videos": videos,
            "forwarded_from": (_html.unescape(fwd.group(1)).strip() if fwd else None),
        })

    mm = MORE_RE.search(html)
    next_before = int(mm.group(1)) if mm else None
    return posts, next_before


# ------------------------------------------------------------ price parsing --
# The highest-risk part. Rental posts state utility fees, deposits and phone
# numbers in exactly the same shapes as rent, so: never guess. If the post does
# not carry ONE unambiguous monthly rent, price stays null and every candidate
# amount is kept in `price_candidates` for the reviewer.

# A line mentioning any of these is NOT a rent line (fee, deposit, contact...).
EXCLUDE_WORDS = [
    # RU
    "депозит", "залог", "предоплат", "электрич", "электро", "вода", "воду", "воды",
    "интернет", "менеджмент", "управлен", "обслуживан", "уборк", "мусор", "питом",
    "животн", "парков", "охран", "комисс", "страхов", "налог", "тариф", "квт",
    "чел.", "человек", "за комнату", "/комнат", "сервис", "штраф", "счётчик",
    "счетчик", "коммунал", "телефон", "вотсап", "ватсап", "вайбер",
    # EN (matched against the diacritics-folded, lowercased line)
    "deposit", "electric", "water", "internet", "wifi", "management", "manage",
    "maintenance", "cleaning", "garbage", "pet", "parking", "security",
    "commission", "service charge", "utilit", "kwh", "per person", "per room",
    "whatsapp", "zalo", "viber", "wechat", "phone", "contact", "+84",
    # VI (folded)
    "dien ", "nuoc ", "coc ", "phi ", "quan ly", "ve sinh", "rac ",
    # Channel footers advertise other services at monthly prices -- a bike at
    # "1,5млн/месяц" must never be mistaken for the flat's rent. Daily rates too.
    "байк", "скутер", "мотоцикл", "мопед", "прокат", "аренда авто", "автомобил",
    "трансфер", "виза", "экскурс", "обмен валют", "сутки", "/сут", "в день",
    "за ночь", "bike", "scooter", "motorbike", "car rental", "visa", "transfer",
    "per day", "/day", "per night", "/night", "sim card",
]

# A line that talks about rent for a period.
RENT_CUES = [
    "цена", "стоимост", "аренд", "в месяц", "/мес", "месяц", "мес.",
    "price", "rent", "month", "gia", "thue", "per month",
]
# Strong cues, used to break ties when several amounts disagree.
STRONG_CUES = ["цена", "стоимост", "price", "gia:", "gia ", "rent", "арендная плата"]

RX_USD_SUF = re.compile(r"(\d[\d ., ]*\d|\d)\s*(?:\$|usd\b|us\$|dollars?\b)", re.I)
RX_USD_PRE = re.compile(r"(?:\$|usd\b|us\$)\s*(\d[\d ., ]*\d|\d)", re.I)
RX_MLN = re.compile(
    r"(\d[\d ., ]*\d|\d)\s*(?:млн|миллион\w*|trieu\b|tr\b|million\b)", re.I)
RX_VND_BIG = re.compile(r"(\d{1,3}(?:[ ., ]\d{3}){2,})")
RX_PLAIN = re.compile(r"(?<![\d+])(\d{7,9})(?!\d)")

URL_RE = re.compile(r"https?://\S+|t\.me/\S+|www\.\S+", re.I)

# Some channels spell the rent out in keycap emoji ("1️⃣1️⃣⚪️5️⃣0️⃣0️⃣⚪️0️⃣0️⃣0️⃣ VND / мес")
# to dodge scrapers. Undo that before parsing (only for parsing -- the stored
# `text` keeps the original so a reviewer sees the post as published).
RX_KEYCAP = re.compile("([0-9])\ufe0f?\u20e3")
RX_EMOJI_SEP = re.compile(
    "(?<=\\d)[\u2190-\u27bf\u2b00-\u2bff\ufe0f\u200d\U0001f000-\U0001faff]+(?=\\d)")
# Exclusion words are checked per SEGMENT, not per line: "Цена: 11,5 млн/мес
# (депозит 1+1)" is a rent line whose parenthetical merely mentions a deposit.
# Separators only where they cannot sit inside a number: "13.5"/"25.000.000"/
# "1,400" keep their dots and commas because those are not followed by a space.
# " - " is deliberately NOT a separator ("25$ - Охрана и обслуживание здания").
RX_SEP = re.compile(r"[()\[\]{}|•;]+|[.,](?=\s)|\s[—–]\s")


def segments(line):
    out, last = [], 0
    for m in RX_SEP.finditer(line):
        if m.start() > last:
            out.append(line[last:m.start()])
        last = m.end()
    if last < len(line):
        out.append(line[last:])
    return out
# "4-6 млн", "от 4 до 6 млн", "300 - 500 USD": a range is not a price. Refuse it.
UNIT = r"(?:млн|миллион|trieu|tr\b|million|\$|usd|vnd|₫|d\b|дон)"
NUMBIT = r"\d[\d .,]*"
RX_RANGE = re.compile("|".join([
    NUMBIT + r"\s*[-–—]\s*" + NUMBIT + r"\s*" + UNIT,
    NUMBIT + r"\s*" + UNIT + r"\s*[-–—]\s*" + NUMBIT + r"\s*" + UNIT,
    r"от\s*" + NUMBIT + r"\s*(?:" + UNIT + r")?\s*до\s*" + NUMBIT + r"\s*" + UNIT,
]), re.I)


def deobfuscate(line):
    return RX_EMOJI_SEP.sub("", RX_KEYCAP.sub(r"\1", line))


def parse_number(tok):
    """'25,000,000'->25000000  '15.000.000'->15000000  '8,5'->8.5  '6.5'->6.5"""
    t = re.sub(r"[\s ]+", "", (tok or "").strip())
    if not t:
        return None
    if re.fullmatch(r"\d+", t):
        return float(t)
    if re.fullmatch(r"\d{1,3}(?:[.,]\d{3})+", t):
        return float(re.sub(r"[.,]", "", t))
    m = re.fullmatch(r"(\d{1,3}(?:[.,]\d{3})*)([.,]\d{1,2})", t)
    if m:
        return float(re.sub(r"[.,]", "", m.group(1)) + "." + m.group(2)[1:])
    if re.fullmatch(r"\d+[.,]\d+", t):
        return float(t.replace(",", "."))
    return None


def _line_candidates(orig_line, folded_line, usd_rate):
    """Every plausible monthly-rent amount stated on one line."""
    out = []

    def add(kind, num_tok, span, vnd, usd=None):
        out.append({
            "kind": kind,
            "raw": orig_line[span[0]:span[1]].strip(),   # fold() is length-preserving
            "number": num_tok,
            "price_vnd": int(round(vnd)),
            "price_usd": usd,
        })

    for rx in (RX_USD_SUF, RX_USD_PRE):
        for m in rx.finditer(folded_line):
            n = parse_number(m.group(1))
            if n is not None and 50 <= n <= 20000:
                add("usd", m.group(1), m.span(), n * usd_rate, n)

    for m in RX_MLN.finditer(folded_line):
        n = parse_number(m.group(1))
        if n is not None and 0.5 <= n <= 300:
            add("millions", m.group(1), m.span(), n * 1000000)

    for rx, kind in ((RX_VND_BIG, "vnd_grouped"), (RX_PLAIN, "vnd_plain")):
        for m in rx.finditer(folded_line):
            n = parse_number(m.group(1))
            if n is None or not (1000000 <= n <= 300000000):
                continue
            add(kind, m.group(1), m.span(), n)

    uniq, seen = [], set()
    for c in out:
        if c["price_vnd"] in seen:
            continue
        seen.add(c["price_vnd"])
        uniq.append(c)
    return uniq


def _cluster_ok(values, tol=0.03):
    """True when every amount agrees within tol, e.g. '690$ (17,4 млн)'."""
    return bool(values) and (max(values) / min(values)) <= (1.0 + tol)


def parse_price(text, usd_rate):
    res = {"price_vnd": None, "price_usd": None, "price_currency": None,
           "price_raw": None, "price_line": None, "price_confidence": "none",
           "price_candidates": [], "price_range_lines": []}
    if not text:
        return res

    allowed = []
    for raw_line in text.split("\n"):
        line = deobfuscate(URL_RE.sub(" ", raw_line))
        if not re.search(r"\d", line):
            continue
        line_fl = fold(line).lower()
        strong = any(c in line_fl for c in STRONG_CUES)
        weak = any(c in line_fl for c in RENT_CUES)
        # Without a strong rent cue, one fee word anywhere disqualifies the whole
        # line ("Депозит (1 месяц) 15 000 000"). With one, fall through to the
        # per-segment check so a parenthetical aside cannot hide the rent.
        if not strong and any(w in line_fl for w in EXCLUDE_WORDS):
            continue
        if (strong or weak) and RX_RANGE.search(line_fl):
            res["price_range_lines"].append(raw_line.strip())
            continue
        for segment in segments(line):
            if not re.search(r"\d", segment):
                continue
            folded = fold(segment)
            if any(w in folded.lower() for w in EXCLUDE_WORDS):
                continue
            cands = _line_candidates(segment, folded, usd_rate)
            for c in cands:
                c["line"] = raw_line.strip()
                c["cue"] = "strong" if strong else ("weak" if weak else "none")
            allowed.extend(cands)

    res["price_candidates"] = allowed
    if res["price_range_lines"]:
        # The post advertises a range ("4-6 млн"). Any single number would be a
        # guess, so leave it to the reviewer.
        res["price_confidence"] = "range"
        return res
    if not allowed:
        return res

    def pick(pool, confidence):
        if not _cluster_ok([c["price_vnd"] for c in pool]):
            return False
        best = pool[0]
        res.update({
            "price_vnd": best["price_vnd"],
            "price_usd": best["price_usd"],
            "price_currency": "USD" if best["kind"] == "usd" else "VND",
            "price_raw": best["raw"],
            "price_line": best["line"],
            "price_confidence": confidence,
        })
        return True

    pools = (
        (allowed, "high"),
        ([c for c in allowed if c["cue"] == "strong"], "strong-cue"),
        ([c for c in allowed if c["cue"] in ("strong", "weak")], "cue"),
    )
    for pool, conf in pools:
        if pool and pick(pool, conf):
            return res

    # "325 USD/month (8.500.000 VND/month)": the landlord quoted the same rent
    # twice at their own USD rate. Not a guess -- prefer the VND-native figure
    # (that is what is actually charged) when the two agree within 15%.
    for pool in (p for p, _ in pools if p):
        native = [c for c in pool if c["kind"] != "usd"]
        usd = [c for c in pool if c["kind"] == "usd"]
        vals = {c["price_vnd"] for c in native}
        if len(vals) == 1 and usd and len(native) + len(usd) == len(pool):
            v = native[0]["price_vnd"]
            if all(0.85 <= c["price_vnd"] / v <= 1.15 for c in usd):
                if pick(native, "usd-vnd-reconciled"):
                    return res

    res["price_confidence"] = "ambiguous"   # several disagreeing amounts
    return res


# ----------------------------------------------------- area / rooms / type --

RX_AREA = re.compile(
    r"(\d{1,4}(?:[.,]\d{1,2})?)\s*"
    r"(?:m2\b|m²|м2\b|м²|sqm\b|sq\.?\s?m\b|"
    r"кв\.?\s?м\b|m\^2)", re.I)
# "3️⃣ Square meters: 50" / "Площадь: 50" -- the unit is in the label, not the value
RX_AREA_LABEL = re.compile(
    r"(?:square\s*met(?:er|re)s?|площад[ьи]|dien tich|area)\s*[:\-]?\s*"
    r"(\d{1,4}(?:[.,]\d{1,2})?)", re.I)
RX_BR = re.compile(
    r"(\d{1,2})\s*[- ]?\s*(?:bedrooms?\b|br\b|bed\b|"
    r"спальн\w*|спален\b|"
    r"phong ngu\b|pn\b)", re.I)
# [^\S\n] not \s -- otherwise "1 bedrooms\n7️⃣ Minimum rental period" reads the
# next template line's number as the bedroom count.
RX_BR_POST = re.compile(
    r"(?:bedrooms?|rooms?|спальн\w*)[^\S\n]*[:\-]?[^\S\n]*(\d{1,2})", re.I)
RU_NUMWORDS = {"одной": 1, "одна": 1, "однои": 1, "двумя": 2, "две": 2, "два": 2,
               "тремя": 3, "три": 3, "четырьмя": 4, "четыре": 4, "пятью": 5, "пять": 5}
RX_RU_BR_WORD = re.compile(r"(" + "|".join(RU_NUMWORDS) + r")\s+спальн", re.I)

# Checked in priority order; word-boundaried so "Minhouse"/"АРЕНДА ДОМОВ"
# boilerplate in a channel footer cannot re-label an apartment as a house.
TYPE_HINTS = [
    ("Студия", re.compile(r"студи|\bstudio\b", re.I)),
    ("Квартира", re.compile(r"квартир|апартамент|\bapartments?\b|\bcan ho\b|\bcondo\b|"
                            r"\bflat\b|\d\s*br\b", re.I)),
    ("Дом", re.compile(r"\bвилл|\bдом[аеу]?\b|таунхаус|\bhouse\b|\bvilla\b|\btownhouse\b|"
                       r"\bnha rieng\b|\bbiet thu\b", re.I)),
    ("Комната", re.compile(r"комнат|\brooms?\b|\bphong tro\b", re.I)),
]

RENTAL_POS = ["сдается", "сдаётся", "сдам", "аренд", "rent", "cho thue",
              "квартир", "студи", "apartment", "house", "villa", "вилл", "дом",
              "комнат", "room", "available"]
RENTAL_NEG = ["ищу ", "ищем ", "сниму", "looking for", "wanted", "продается",
              "продаётся", "продажа", "for sale", "ban nha", "куплю"]


def parse_area(text):
    cands = []
    for raw_line in text.split("\n"):
        fl = fold(raw_line)
        for rx in (RX_AREA, RX_AREA_LABEL):
            for m in rx.finditer(fl):
                v = parse_number(m.group(1))
                if v is not None and 8 <= v <= 2000:
                    cands.append({
                        "area": (int(v) if float(v).is_integer() else round(v, 1)),
                        "raw": raw_line[m.start():m.end()].strip(),
                        "line": raw_line.strip(),
                    })
    uniq, seen = [], set()
    for c in cands:                       # same value found twice on one line
        k = (c["area"], c["line"])
        if k not in seen:
            seen.add(k)
            uniq.append(c)
    if not uniq:
        return None, "none", []
    vals = {c["area"] for c in uniq}
    return uniq[0]["area"], ("high" if len(vals) == 1 else "ambiguous"), uniq


def parse_rooms(text):
    fl = fold(text).lower()
    if "студи" in fl or "studio" in fl:
        return 0, "studio"
    vals = []
    for rx in (RX_BR, RX_BR_POST):
        for m in rx.finditer(fl):
            try:
                n = int(m.group(1))
            except ValueError:
                continue
            if 1 <= n <= 8:
                vals.append(n)
    m = RX_RU_BR_WORD.search(fl)
    if m:
        vals.append(RU_NUMWORDS[m.group(1).lower()])
    if not vals:
        return None, "none"
    uniq = sorted(set(vals))
    return uniq[0], ("high" if len(uniq) == 1 else "ambiguous")


def parse_type(text):
    fl = fold(text).lower()
    # An explicit template field ("0️⃣ Type: apartment") beats free prose.
    m = re.search(r"(?:^|\n)[^\n]{0,6}(?:type|тип)\s*[:\-]\s*([^\n]{0,40})", fl, re.I)
    scopes = [m.group(1)] if m else []
    # Then the opening lines: a channel footer ("Большой выбор квартир и домов",
    # "#квартира_нячанг") must not re-label the house announced in the title.
    head = [ln for ln in fl.split("\n") if ln.strip()][:5]
    scopes.append("\n".join(head))
    scopes.append(fl)
    for scope in scopes:
        for label, rx in TYPE_HINTS:
            if rx.search(scope):
                return label
    return None


def looks_like_rental(text):
    if not text or len(text) < 40:
        return False, "no text / too short"
    fl = fold(text).lower()
    for n in RENTAL_NEG:
        if n in fl:
            return False, "negative keyword: %s" % n.strip()
    for p in RENTAL_POS:
        if p in fl:
            return True, "keyword: %s" % p.strip()
    return False, "no rental keyword"


# -------------------------------------------------------------- geography ---

LANDMARKS = {
    "nha-trang": ["oceanus", "muong thanh", "panorama", "gold coast", "scenia bay",
                  "vega city", "libera", "an vien", "hud", "maple", "ariyana",
                  "cham oasis", "napoleon", "virgo", "the costa", "my gia",
                  "hon chong", "tran phu", "hung vuong", "nguyen thien thuat",
                  "vinpearl", "bai dai", "cho dam", "xom moi",
                  "океанус", "муонг тхань", "хон чонг", "чан фу", "хунг выонг",
                  "винперл", "панорама", "вега сити"],
    "da-nang": ["my khe", "son tra", "an thuong", "hai chau", "thanh khe",
                "cam le", "ngu hanh son", "lien chieu", "hoa xuan", "hoa khanh",
                "cau rong", "song han", "muong thanh", "monarchy", "fpt",
                "asia park", "lotte", "azura", "hiyori", "risemount",
                "nguyen van thoai", "vo nguyen giap", "le dinh ly", "tran cao van"],
}
ADDR_CUES = re.compile(
    r"(?:адрес|address|локац|location|район|district|улиц|street|"
    r"dia chi|duong|жк\b|комплекс|complex|building|toa nha|phuong|quan\b)", re.I)


def parse_geo(text, city, city_districts):
    fl = fold(text).lower()
    squashed = re.sub(r"[^a-z0-9]+", "", fl)   # matches hashtags like #NguHanhSon
    addr_lines = [ln.strip() for ln in text.split("\n")
                  if ln.strip() and ADDR_CUES.search(fold(ln))]

    def present(needle):
        if len(needle) < 4:
            return False
        if needle in fl:
            return True
        sq = re.sub(r"[^a-z0-9]+", "", needle)
        return len(sq) >= 6 and sq in squashed

    hits = []
    for d in city_districts:
        name = fold(d.get("name", "")).lower()
        name = re.sub(r"^(phuong|quan|xa)\s+", "", name)
        name = name.replace(" - da lat", "").strip()
        if present(name):
            hits.append({"key": d.get("key"), "name": d.get("name")})
    lands = [k for k in LANDMARKS.get(city or "", []) if present(k)]
    return addr_lines[:6], hits, lands


# ------------------------------------------------------------------ dedupe --

RX_LISTING_ID = re.compile(r"\bID\s*[:#]?\s*([A-ZА-Я]{1,3}\s?\d{2,6})\b", re.I)


def norm_text(t):
    if not t:
        return ""
    t = URL_RE.sub(" ", t)
    t = re.sub(r"@\w+", " ", t)      # contact handles differ between cross-posts
    t = re.sub(r"#\w+", " ", t)      # so do hashtags
    t = fold(t).lower()
    return re.sub(r"[^0-9a-zа-яё]+", "", t)


def text_hash(t):
    n = norm_text(t)
    return hashlib.sha1(n.encode("utf-8")).hexdigest() if len(n) >= 30 else None


def listing_id_key(t):
    m = RX_LISTING_ID.search(t or "")
    if not m:
        return None
    return re.sub(r"\s+", "", m.group(1)).upper().replace("А", "A")


# ------------------------------------------------------- existing listings --

def load_existing(index_path):
    """Parse `var DATA = {...};` out of the built index.html."""
    out = {"urls": set(), "hashes": set(), "photos": set(), "id_keys": set(),
           "cities": {}, "count": 0, "ok": False, "error": None}
    try:
        with open(index_path, encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        out["error"] = "cannot read %s: %s" % (index_path, e)
        return out
    m = re.search(r"var DATA = (\{.*?\});\s*\n", html, re.S)
    if not m:
        out["error"] = "`var DATA = {...};` not found in %s" % index_path
        return out
    try:
        data = json.loads(m.group(1))
    except Exception as e:
        out["error"] = "DATA is not valid JSON: %s" % e
        return out

    out["ok"] = True
    out["cities"] = {k: v.get("districts", []) for k, v in data.get("CITIES", {}).items()}
    for l in data.get("LISTINGS", []):
        out["count"] += 1
        u = (l.get("url") or "").strip().rstrip("/").lower()
        if u:
            out["urls"].add(u)
        for field in ("desc", "descEn"):
            h = text_hash(l.get(field))
            if h:
                out["hashes"].add(h)
        for p in (l.get("details") or {}).get("photos", []) or []:
            out["photos"].add(p.strip())
        k = listing_id_key(json.dumps(l, ensure_ascii=False))
        if k:
            out["id_keys"].add(k)
    return out


# -------------------------------------------------------------------- main --

def harvest_channel(channel, pages, delay, usd_rate, cities):
    city = CHANNELS.get(channel)
    posts, before, seen_ids, errors = [], None, set(), []
    for _ in range(max(1, pages)):
        url = "https://t.me/s/%s" % channel
        if before:
            url += "?before=%d" % before
        try:
            html = http_get(url)
        except Exception as e:
            errors.append(str(e))
            break
        page_posts, next_before = parse_page(html, channel)
        new = [p for p in page_posts if p["msg_id"] not in seen_ids]
        seen_ids.update(p["msg_id"] for p in new)
        posts.extend(new)
        if not new or not next_before or next_before == before:
            break
        before = next_before
        time.sleep(delay)
    time.sleep(delay)

    districts = cities.get(city, []) if city else []
    for p in posts:
        p["city_hint"] = city
        txt = p["text"]
        p.update(parse_price(txt, usd_rate))
        area, area_conf, area_c = parse_area(txt)
        p["area_m2"] = area
        p["area_confidence"] = area_conf
        p["area_candidates"] = area_c
        rooms, rooms_conf = parse_rooms(txt)
        p["bedrooms"] = rooms
        p["bedrooms_confidence"] = rooms_conf
        p["type_hint"] = parse_type(txt)
        is_rent, why = looks_like_rental(txt)
        p["is_rental"] = is_rent
        p["rental_reason"] = why
        addr, dhits, lands = parse_geo(txt, city, districts)
        p["address_lines"] = addr
        p["district_hits"] = dhits
        p["landmark_hits"] = lands
        p["text_hash"] = text_hash(txt)
        p["listing_id_key"] = listing_id_key(txt)
        p["photo_count"] = len(p["photos"])
        p["review_flags"] = review_flags(p)
    return posts, errors


RX_SHORT_TERM = re.compile(
    r"посуточн|краткосрочн|short.?term|per night|daily rental|по суткам", re.I)


def review_flags(p):
    """Cheap flags telling the reviewer what still needs a human decision."""
    f = []
    if not p["text"]:
        f.append("no_text")
    if not p["is_rental"]:
        f.append("not_recognised_as_rental")
    if not p["price_vnd"]:
        f.append("price_%s" % p["price_confidence"])
    if not p["area_m2"]:
        f.append("no_area")
    if not p["photos"]:
        f.append("no_photos")
    if not (p["district_hits"] or p["address_lines"] or p["landmark_hits"]):
        f.append("no_location_signal")
    elif not p["district_hits"]:
        f.append("district_needs_judgement")
    if RX_SHORT_TERM.search(fold(p["text"])):
        f.append("short_term_rental_mentioned")
    if p["price_confidence"] == "usd-vnd-reconciled":
        f.append("price_quoted_in_two_currencies")
    return f


def main():
    ap = argparse.ArgumentParser(
        description="Fetch rental candidates from public Telegram channels (read-only).")
    ap.add_argument("--channels", default=",".join(CHANNELS),
                    help="comma-separated channel names (default: all known)")
    ap.add_argument("--pages", type=int, default=3,
                    help="pages to walk back per channel via ?before= (default 3)")
    ap.add_argument("--usd-rate", type=float, default=DEFAULT_USD_RATE,
                    help="USD->VND rate (default %d, as used by existing listings)"
                         % DEFAULT_USD_RATE)
    ap.add_argument("--delay", type=float, default=0.5,
                    help="seconds between fetches (default 0.5)")
    ap.add_argument("--out", default=os.path.join(HERE, "telegram_candidates.json"))
    ap.add_argument("--index", default=os.path.join(HERE, "index.html"))
    ap.add_argument("--min-price", type=float, default=0,
                    help="drop priced candidates below this many VND")
    ap.add_argument("--max-price", type=float, default=0,
                    help="drop priced candidates above this many VND (0 = off)")
    args = ap.parse_args()

    wanted = [c.strip() for c in args.channels.split(",") if c.strip()]
    existing = load_existing(args.index)
    if not existing["ok"]:
        print("[warn] existing-listing dedup DISABLED: %s" % existing["error"])
    cities = existing["cities"]

    per_channel, all_posts, fetch_errors = {}, [], {}
    for ch in wanted:
        posts, errs = harvest_channel(ch, args.pages, args.delay, args.usd_rate, cities)
        if errs:
            fetch_errors[ch] = errs
        st = {"fetched": len(posts), "with_text": 0, "rental": 0, "with_price": 0,
              "after_run_dedup": 0, "after_existing_dedup": 0}
        for p in posts:
            if p["text"]:
                st["with_text"] += 1
            if p["is_rental"]:
                st["rental"] += 1
                if p["price_vnd"]:
                    st["with_price"] += 1
        per_channel[ch] = st
        all_posts.extend(posts)

    # ---- dedupe within the run -------------------------------------------
    kept, by_key, dup_count = [], {}, 0
    for p in all_posts:
        keys = []
        if p["listing_id_key"]:
            keys.append("ID:" + p["listing_id_key"])
        if p["text_hash"]:
            keys.append("TX:" + p["text_hash"])
        matched = next((k for k in keys if k in by_key), None)
        if matched:
            hit = by_key[matched]
            dup_count += 1
            hit.setdefault("duplicates", []).append({
                "channel": p["channel"], "permalink": p["permalink"],
                "date": p["date"],
                "matched_on": "listing_id" if matched.startswith("ID:") else "text_hash",
            })
            if p["channel"] != hit["channel"]:
                hit["cross_channel_duplicate"] = True
            for k in keys:
                by_key.setdefault(k, hit)
            continue
        for k in keys:
            by_key[k] = p
        kept.append(p)

    dup_groups = []
    for p in kept:
        if p.get("duplicates"):
            spans = sorted({p["channel"]} | {d["channel"] for d in p["duplicates"]})
            dup_groups.append((spans, len(p["duplicates"]),
                               p["duplicates"][0]["matched_on"]))

    # soft cross-post flag: same city + price + area seen in a different channel
    sig, soft = {}, 0
    for p in kept:
        if p["price_vnd"] and p["area_m2"]:
            sig.setdefault((p["city_hint"], p["price_vnd"], p["area_m2"]), []).append(p)
    for group in sig.values():
        if len(group) > 1 and len({g["channel"] for g in group}) > 1:
            for g in group:
                g["possible_crosspost_with"] = sorted(
                    o["permalink"] for o in group if o is not g)
                soft += 1

    # ---- dedupe against what we already have ------------------------------
    survivors = []
    drops = {"permalink": 0, "text_hash": 0, "photo_url": 0, "listing_id": 0}
    for p in kept:
        reason = None
        if p["permalink"].lower().rstrip("/") in existing["urls"]:
            reason = "permalink"
        elif p["text_hash"] and p["text_hash"] in existing["hashes"]:
            reason = "text_hash"
        elif any(u in existing["photos"] for u in p["photos"]):
            reason = "photo_url"
        elif p["listing_id_key"] and p["listing_id_key"] in existing["id_keys"]:
            reason = "listing_id"
        if reason:
            drops[reason] += 1
            p["dropped_because"] = reason
            continue
        survivors.append(p)

    if args.min_price or args.max_price:
        survivors = [p for p in survivors
                     if not p["price_vnd"]
                     or (p["price_vnd"] >= args.min_price
                         and (not args.max_price or p["price_vnd"] <= args.max_price))]

    # Telegram echoes the channel's canonical casing (DaNangRentAFlat), which may
    # differ from the name asked for on the command line -- compare case-folded.
    for ch in per_channel:
        low = ch.lower()
        per_channel[ch]["after_run_dedup"] = sum(
            1 for p in kept if p["channel"].lower() == low)
        per_channel[ch]["after_existing_dedup"] = sum(
            1 for p in survivors if p["channel"].lower() == low)

    payload = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "usd_rate": args.usd_rate,
        "pages_per_channel": args.pages,
        "channels": wanted,
        "existing_source": args.index if existing["ok"] else None,
        "existing_listings": existing["count"],
        "stats": {
            "fetched": len(all_posts),
            "after_run_dedup": len(kept),
            "run_duplicates_collapsed": dup_count,
            "possible_crossposts_flagged": soft,
            "dropped_as_already_known": sum(drops.values()),
            "dropped_breakdown": drops,
            "candidates": len(survivors),
            "candidates_with_price": sum(1 for p in survivors if p["price_vnd"]),
        },
        "per_channel": per_channel,
        "fetch_errors": fetch_errors,
        "candidates": survivors,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)

    # ---- summary ----------------------------------------------------------
    print("=" * 78)
    print("Telegram candidate harvest  (%s, %d page(s)/channel, USD->VND %d)"
          % (payload["generated"], args.pages, int(args.usd_rate)))
    print("=" * 78)
    hdr = "%-24s %6s %6s %7s %7s %6s %5s" % (
        "channel", "posts", "text", "rental", "priced", "uniq", "new")
    print(hdr)
    print("-" * len(hdr))
    for ch in wanted:
        s = per_channel.get(ch, {})
        print("%-24s %6d %6d %7d %7d %6d %5d" % (
            ch[:24], s.get("fetched", 0), s.get("with_text", 0), s.get("rental", 0),
            s.get("with_price", 0), s.get("after_run_dedup", 0),
            s.get("after_existing_dedup", 0)))
        for e in fetch_errors.get(ch, []):
            print("      ! %s" % e[:110])
    print("-" * len(hdr))
    st = payload["stats"]
    print("%-24s %6d %6s %7s %7d %6d %5d" % (
        "TOTAL", st["fetched"], "-", "-",
        sum(v.get("with_price", 0) for v in per_channel.values()),
        st["after_run_dedup"], st["candidates"]))
    print()
    print("within-run duplicates collapsed  : %d" % dup_count)
    for spans, n, how in dup_groups:
        where = " + ".join(spans) if len(spans) > 1 else spans[0] + " (repost in same channel)"
        print("   %d copy(ies) via %-10s spanned: %s" % (n, how, where))
    print("possible cross-post pairs flagged: %d  (same city+price+area, different channel)" % soft)
    print("dropped as already in index.html : %d  %s" % (sum(drops.values()), drops))
    print("candidates written               : %d  (%d with a parsed price)"
          % (len(survivors), st["candidates_with_price"]))
    print("output                           : %s" % args.out)
    if not existing["ok"]:
        print("NOTE: existing-listing dedup was disabled (%s)" % existing["error"])


if __name__ == "__main__":
    main()
