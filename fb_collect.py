# -*- coding: utf-8 -*-
"""
Standalone, schedulable Facebook rental collector -- GROUPS first, Marketplace second.

WHAT THIS IS
============
`facebook_check_prompt.txt` describes the Facebook pass as it was run by hand on
4 Sep 2026: an interactive assistant driving the OWNER'S OWN Chrome through the
`claude-in-chrome` tools. That cannot be scheduled -- the scheduled runner is a
headless `claude -p` session with no browser attached, and even if it had one it
would seize the owner's Chrome window at 05:00.

This script removes that dependency. It drives its OWN browser out of its OWN
persistent profile directory (`_fb_profile/`, git-ignored), so:
  * the login survives between runs -- log in once, by hand, with `--login`;
  * nothing touches the owner's Chrome, its tabs or its cookies;
  * it can be started by Task Scheduler, by run_daily_check.ps1, or by hand.

TWO SOURCES, AND WHICH ONE MATTERS
==================================
  * GROUPS (`--groups`) is the primary path. The owner has deliberately joined
    29 rental groups; 22 of them were read out of their account on 4 Sep 2026
    and are registered in GROUPS below -- three in Dumaguete, eight in Cebu,
    seven around Manila, three Vietnamese ones (HCMC, Nha Trang, Da Nang) and
    one whose city is unconfirmed. That list, not Marketplace, is the actual
    source of Philippine listings. The other seven joined groups were not
    captured and are still missing; a Da Lat group is among the gaps. Group
    posts are free text, so the body-parsing rules that facebook_check_prompt.txt
    worked out for Marketplace apply here too, only harder.
  * MARKETPLACE (`--marketplace`) is the secondary path, and works exactly as
    the prompt file describes: a filtered category feed plus item pages.

Everything the parsing knows about Marketplace was measured by hand and is
written down in `facebook_check_prompt.txt`. Read that before changing it.
The group-side observations came from a second hand-check on 4 Sep 2026 and are
noted inline as they come up. Anything I could NOT verify is marked UNVERIFIED
in a comment; do not read those as measurements.

READ-ONLY INVARIANT (this is the contract, not an accident of the code)
======================================================================
This script must never write anything to Facebook. Concretely, it must never:
  * message a seller, open a Messenger thread, or load any /messages/ URL;
  * click "Send", "Notify me", "Save", "Share", "Follow", "Like", "Comment",
    "Join group", "Make offer", or any other button that changes state;
  * type into any Facebook input, submit any form, post anything anywhere;
  * accept, decline or dismiss any consent, terms or permission dialog;
  * attempt to solve, bypass or work around a CAPTCHA, a checkpoint, or any
    other bot-detection challenge. If one appears the run STOPS and says so.

The enforcement lives in `_safe_click()`: it is the only place in this file that
clicks anything, and it refuses any element whose accessible name is not on
`ALLOWED_CLICK_LABELS` -- currently "See more" (expand a truncated post) and the
photo-gallery "Next photo" arrow, both pure view operations. There is also a
request-level backstop (`_block_writes`) that aborts navigations to Messenger
and composer URLs. Adding a click means adding it to the allowlist and
justifying it here.

It also makes no attempt to look like a human to Facebook's bot detection: no
stealth flags, no webdriver masking, no user-agent spoofing. The only defence
against getting the account flagged is doing very little, slowly -- see
`--max-items`, the randomised delays, and the account-risk note in the report.

WHAT ONE GROUP RUN DOES
=======================
  1. opens its own browser on the persistent profile, checks the `c_user`
     cookie, and stops with instructions if the session is gone;
  2. for each group in the city's list: loads the group, WAITS for real posts
     (the feed renders lazily -- right after load most cards are skeletons and
     `[role="article"]` matches two or three nodes), then scrolls in small steps;
  3. reads each top-level post: permalink, author, timestamp text, body, photos.
     Nested `[role="article"]` nodes are comments and are skipped;
  4. sanitises the text: strips zero-width and combining-joiner characters used
     by spam to evade moderation, drops the runs of the literal word "Facebook"
     that hidden nodes contribute, and rejects a post whose text is still
     letter-by-letter obfuscated;
  5. drops posts already on the site, posts with no address in the body, posts
     with no price in the body, sales, and the off-topic majority (the group
     called HOUSE AND ROOMS FOR RENT DUMAGUETE was showing footwear at PHP 85);
  6. opens each survivor's permalink for the untruncated text and better photos,
     downloads up to 6 photos inside the authenticated session, downscales them
     and saves them to `assets/fb_photos/<post id>/NN.webp`;
  7. writes a candidates JSON with every survivor AND every rejection with its
     reason, so nothing is silently dropped.

It does NOT write listing rows, does not touch rebuild_final.py, does not run
the pin pipeline and does not commit anything. A human (or an assistant session)
reads the candidates JSON and writes `new_listings<N>.py` the usual way.

DATES
=====
Downstream refuses to publish a listing with a fabricated date, so this script
never invents one. `age_days: null` means the post published nothing parseable.
Group posts are better than Marketplace here: a group post normally carries a
relative or absolute timestamp in its permalink anchor ("3h", "2d",
"September 1 at 10:04"), which is a real signal -- but only once the card has
finished rendering, and Facebook rounds the relative forms ("1w" is somewhere in
7-13 days). `age_precision` says which kind it was.

PHOTOS
======
The interactive pass could not do photos: Facebook image URLs are signed (the
`oe` parameter measured on 4 Sep 2026 expired in four days) and the assistant's
harness refuses to carry signed URLs out of the browser at all. A standalone
script has neither problem -- it fetches the bytes itself, in the same logged-in
context, and stores the pixels rather than a URL that will 403 by Friday.
  * the files are relative paths, so they render on GitHub Pages but NOT inside
    the claude.ai Artifact copy of the site (an Artifact cannot load repo files);
  * they are real bytes in a git repo -- 40-120 KB each after downscaling, so
    roughly 0.3-0.7 MB per listing. `--prune-photos` deletes the directories of
    listings that are no longer on the site.

USAGE
=====
  python fb_collect.py --login                       # once, by hand
  python fb_collect.py --selftest                    # parsers only, no network
  python fb_collect.py --groups --city dumaguete
  python fb_collect.py --groups --group 153191128587086 --city-key dumaguete
  python fb_collect.py --groups --city cebu --max-items 15 --max-groups 3
  python fb_collect.py --marketplace --city hochiminhcity --max-items 20
  python fb_collect.py --prune-photos [--apply]
"""
import argparse
import io
import json
import os
import random
import re
import shutil
import sys
import time
import unicodedata
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SCRIPT_VERSION = "1.1 (2026-09-04, groups-first)"

HERE = os.path.dirname(os.path.abspath(__file__))
PROFILE_DIR = os.path.join(HERE, "_fb_profile")          # git-ignored (_*)
PHOTO_ROOT = os.path.join(HERE, "assets", "fb_photos")   # tracked, served by Pages
PHOTO_REL_ROOT = "assets/fb_photos"

# --------------------------------------------------------------------------
# The owner's joined rental groups, read out of their own account on
# 4 Sep 2026. `name` is filled in where it was recorded. A group is addressed
# by numeric id or by URL slug -- both work in /groups/<x>.
# --------------------------------------------------------------------------
GROUPS = {
    "dumaguete": [
        {"id": "1996683940588782", "name": "HOUSE AND ROOMS FOR RENT DUMAGUETE"},
        {"id": "153191128587086", "name": "Dumaguete Rentals And Sale (Real Estate)"},
        {"id": "346330203591713", "name": "DUMAGUETE CITY HOUSE FOR RENT, BOARDING HOUSE, APARTMENTS, TRANSIENT"},
    ],
    "cebu": [
        {"id": "563896434149922", "name": None},
        {"id": "1735327053393688", "name": None},
        {"id": "993673090964916", "name": None},
        {"id": "3914645581932487", "name": None},
        {"id": "994303254903669", "name": None},
        {"id": "652674525365824", "name": None},
        {"id": "rentcebu", "name": None},
        {"id": "cebu.tambayan.2", "name": None},
    ],
    "manila": [
        {"id": "224805677963542", "name": "Makati, BGC, Manila, Mandaluyong & QC"},
        {"id": "190166981724964", "name": "University Belt"},
        {"id": "299437881275577", "name": "Quezon City & Manila"},
        {"id": "715451165293916", "name": "pet-friendly NCR"},
        {"id": "995479814463151", "name": "Manila, Pasay, Pasig, Makati"},
        {"id": "1972633726399858", "name": None},
        {"id": "1319639041431566", "name": None},
    ],
    "ho-chi-minh": [
        {"id": "chungcumini.canhodichvu.phongtrotphcm", "name": None},
    ],
    "nha-trang": [
        {"id": "chothuecanhogiarenhatrang", "name": None},
    ],
    "da-nang": [
        {"id": "canhochothuedanangtot", "name": None},
    ],
    # City not confirmed: the slug says "commercial rentals" and nothing more.
    # Left unassigned on purpose rather than guessed into a city bucket.
    "_unassigned": [
        {"id": "chothuethuongmai", "name": "commercial rentals -- city unconfirmed"},
    ],
}

GROUP_URL = "https://www.facebook.com/groups/{gid}"
# UNVERIFIED: sorting_setting=CHRONOLOGICAL is the documented way to ask a group
# feed for newest-first instead of Facebook's "top posts" ordering, but it was
# not confirmed on a live group during this work. If a run comes back with
# obviously stale posts, check this first.
GROUP_SORT_PARAM = "?sorting_setting=CHRONOLOGICAL"

FEED_BASE = "https://www.facebook.com/marketplace/{city}/{category}"
ITEM_URL = "https://www.facebook.com/marketplace/item/{id}/"

CITY_SLUG_TO_KEY = {
    "hochiminhcity": "ho-chi-minh", "hanoi": "ha-noi", "danang": "da-nang",
    "nhatrang": "nha-trang", "dalat": "da-lat", "vungtau": "vung-tau",
    "quynhon": "quy-nhon", "hoian": "hoi-an", "phanthiet": "phan-thiet",
    "phuquoc": "phu-quoc", "binhduong": "binh-duong",
    "manila": "manila", "cebu": "cebu", "dumaguete": "dumaguete",
}
PH_CITIES = {"manila", "cebu", "dumaguete"}
CATEGORIES = ("propertyrentals", "apartments-for-rent", "condos-for-rent",
              "houses-for-rent", "townhouses-for-rent")

# The ONLY clicks this script is allowed to perform. Both are view operations.
ALLOWED_CLICK_LABELS = re.compile(
    r"^(see more|see\s?more\.\.\.|xem thêm|next photo|next|ảnh tiếp theo|"
    r"hình ảnh tiếp theo)$", re.I)

BLOCKED_URL_BITS = ("/messages/", "messenger.com", "/composer/", "/ajax/ufi/",
                    "/marketplace/inbox", "/groups/create")

MP_ITEM_ID_RE = re.compile(r"/marketplace/item/(\d{6,})")
GROUP_POST_ID_RE = re.compile(r"/groups/[^/]+/(?:posts|permalink)/(\d{6,})")
# The feed aria-label shape: "<title>, ₫<price>, <place>, listing <id>". The
# price group must allow the thousands comma inside ₫13,500 -- a [^,]* there
# stops at that comma and the whole match slides one field to the left.
ARIA_RE = re.compile(r"^(?P<title>.*?),\s*(?P<price>[₫$₱][\d.,]*|Free|Miễn phí)?,?\s*"
                     r"(?P<place>[^,]*),\s*listing\s*(?P<id>\d+)\s*$", re.I)


# ==========================================================================
# Text sanitising. Group feeds are dirtier than Marketplace item pages.
# ==========================================================================

# Invisible characters spam uses to break up words so moderation cannot read
# them: the combining grapheme joiner, zero-width space/joiner/non-joiner, the
# bidi marks, word joiner, soft hyphen, Mongolian vowel separator.
INVISIBLE_RE = re.compile("[͏​-‏⁠-⁤⁪-⁯"
                          "﻿­᠎]")
# Hidden accessibility nodes contribute long runs of the bare word "Facebook".
FACEBOOK_RUN_RE = re.compile(r"(?:\bFacebook\b[ \t ]*){2,}")


def clean_text(s):
    """NFC-normalise, drop invisible spam separators, collapse hidden-node noise.

    Deliberately does NOT strip combining marks in general: Vietnamese is built
    out of them, and normalising to NFC first composes ế, ộ, ữ back into single
    characters so only the genuinely invisible leftovers remain.
    """
    if not s:
        return ""
    s = unicodedata.normalize("NFC", s)
    s = INVISIBLE_RE.sub("", s)
    s = FACEBOOK_RUN_RE.sub(" ", s)
    s = s.replace(" ", " ")
    lines = []
    for line in s.split("\n"):
        line = re.sub(r"[ \t]+", " ", line).strip()
        if line.lower() == "facebook":
            continue
        lines.append(line)
    out = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", out).strip()


def looks_obfuscated(s):
    """True for the character-by-character spam ('d r n p s ...').

    Once the invisible joiners are stripped, that text is a long run of
    single-character tokens. Real ads are not.
    """
    toks = [t for t in re.split(r"\s+", s or "") if t]
    if len(toks) < 12:
        return False
    singles = sum(1 for t in toks if len(t) == 1)
    return singles / float(len(toks)) > 0.35


UNAVAILABLE_RE = re.compile(
    r"this content isn'?t available|nội dung này hiện không có|"
    r"content not available|bài viết không có sẵn", re.I)


def _norm(s):
    return re.sub(r"[ \t ]+", " ", (s or "")).strip()


# ==========================================================================
# Money, area, address, rental/not. Currency-aware: the Philippine groups price
# in pesos, the Vietnamese ones in đồng. Nothing is converted -- a hardcoded
# rate would rot silently, and the site has no PHP convention yet.
# ==========================================================================

# Trap 3 from the prompt file: any figure in tỷ is a purchase price sitting in
# the rentals category. Bare "ty"/"ti" only counts glued to digits ("7ty",
# "5xty"), because "ti vi" would otherwise fire constantly.
SALE_RE = re.compile(r"(\d+(?:[.,]\d+)?)\s*(?:tỷ|tỉ)\b|\b\d+\s*x?\s*ty\b|\btỷ\b", re.I)

NON_RENTAL_RE = re.compile(
    r"sơn nhà|sơn sửa|dịch vụ sơn|sửa chữa nhà|chống thấm|thi công|"
    r"chuyển nhà trọn gói|taxi tải|thiết kế nội thất|vay vốn|cho vay|"
    r"tuyển dụng|tuyển nhân viên|massage|cắt tóc|giặt là|dọn vệ sinh|"
    r"bảo hiểm|du lịch giá rẻ|"
    r"\bloan\b|\blending\b|\bhiring\b|\bjob opening\b|\binsurance\b|"
    r"\bfootwear\b|\bshoes for sale\b|\bsandals\b|\bpre-?order\b|\bfree shipping\b|"
    r"\bcod\b|\bmeet ?up\b.{0,20}\bmall\b", re.I)

RENT_CUE_RE = re.compile(
    r"cho thuê|cần thuê|thuê nhà|thuê phòng|thuê căn hộ|/\s*tháng|"
    r"triệu\s*/\s*th|tr\s*/\s*th|\bthuê\b|"
    r"for rent|to let|for lease|\brental\b|\brenting\b|per month|/\s*month|"
    r"\bmonthly\b|\bmo\.\b|bedspace|bed space|boarding house|\btransient\b|"
    r"\bstudio type\b|\bunit available\b|\bfor occupancy\b|\brent\b", re.I)

SALE_CUE_RE = re.compile(
    r"\bcần bán\b|\bchính chủ bán\b|\bbán gấp\b|\bfor sale\b|\brush sale\b|"
    r"\bselling\b|\bbrand new for sale\b|\bpre-?selling\b", re.I)

# Money figures that are not the rent. Checked in the 30 characters BEFORE the
# figure (deposit and bill words precede their amount) and, for unit noise, in
# the 14 characters after.
PRICE_NOISE_BEFORE_RE = re.compile(
    r"cọc|đặt cọc|tiền điện|tiền nước|điện|nước|phí dịch vụ|phí quản lý|"
    r"quản lý|rác|internet|wifi|giữ xe|gửi xe|môi giới|hoa hồng|"
    r"deposit|advance|adv\.|security bond|assoc(?:iation)? dues|dues|"
    r"electric|water bill|utilit|maintenance|parking|association", re.I)
PRICE_NOISE_AFTER_RE = re.compile(
    r"^\s*(?:đ|vnđ|vnd|php|₱)?\s*/\s*(?:số|kwh|người|đầu người|xe|m2|m²|"
    r"head|person|pax|sqm|kwh)", re.I)

CURRENCY_FLOOR = {"VND": 500_000, "PHP": 1_500}
CURRENCY_CEIL = {"VND": 500_000_000, "PHP": 500_000}


def _noise_around(text, m):
    before = text[max(0, m.start() - 30):m.start()]
    after = text[m.end():m.end() + 14]
    return bool(PRICE_NOISE_BEFORE_RE.search(before)) or bool(PRICE_NOISE_AFTER_RE.match(after))


def parse_prices(text, currency="VND"):
    """Every rent-shaped figure in the body, as (amount, snippet) pairs.

    Trap 2 from the prompt file: Facebook's own price field is not a price.
    Measured in one Marketplace pass: ₫13,500 for 13.5 million, ₫1,400,000 for
    14 million, ₫4,000,000 for 40 million, and ₫8 / ₫105 / "Free" for real
    rentals. Sellers type millions as plain numbers and the platform believes
    them. Group posts have no price field at all, so the body is the only
    source either way.
    """
    if not text:
        return []
    floor, ceil = CURRENCY_FLOOR[currency], CURRENCY_CEIL[currency]
    out, spans = [], []

    def add(value, m):
        value = int(round(value))
        if not (floor <= value <= ceil):
            return
        if _noise_around(text, m):
            return
        for a, b in spans:
            if m.start() < b and a < m.end():
                return
        spans.append((m.start(), m.end()))
        out.append((value, _norm(m.group(0))))

    if currency == "VND":
        # "4tr9", "13tr5" -- X million plus Y hundred thousand, glued.
        for m in re.finditer(r"(?<![\d.,])(\d{1,3})tr(\d)(?![\d])", text, re.I):
            add((int(m.group(1)) + int(m.group(2)) / 10.0) * 1_000_000, m)
        # "13.5 triệu", "13,5tr", "8 triệu", "8tr"
        for m in re.finditer(r"(?<![\d.,])(\d{1,3}(?:[.,]\d{1,2})?)\s*(?:triệu|tr)\b(?!\w)",
                             text, re.I):
            val = float(m.group(1).replace(",", "."))
            if 0.3 <= val <= 500:
                add(val * 1_000_000, m)

    # Grouped numbers: 4.900.000 / 8,000,000 / 12 000 / 15,000
    for m in re.finditer(r"(?<![\d.,])(\d{1,3}(?:[.,\s]\d{3}){1,3})(?![\d])", text):
        raw = m.group(1)
        if raw.lstrip().startswith("0"):          # phone number, not money
            continue
        add(int(re.sub(r"[.,\s]", "", raw)), m)

    # "12k", "5500k"
    for m in re.finditer(r"(?<![\d.,])(\d{1,5})\s*k\b", text, re.I):
        add(int(m.group(1)) * 1000, m)

    if currency == "PHP":
        # "PHP 12000", "₱12000", "P12000" without separators
        for m in re.finditer(r"(?:php|₱|p)\s*(\d{4,6})(?![\d])", text, re.I):
            add(int(m.group(1)), m)

    out.sort(key=lambda p: p[0])
    return out


def parse_prices_usd(text):
    """USD asking prices, recorded but never converted."""
    if not text:
        return []
    out = []
    for m in re.finditer(r"(?<![\d.,])(\d{2,5})\s*(?:usd|đô la|đô)\b", text, re.I):
        out.append((int(m.group(1)), _norm(m.group(0))))
    for m in re.finditer(r"\$\s*(\d{2,5})(?![\d])", text):
        out.append((int(m.group(1)), _norm(m.group(0))))
    seen, uniq = set(), []
    for v, s in out:
        if v not in seen:
            seen.add(v)
            uniq.append((v, s))
    return sorted(uniq)


def parse_fb_price_field(s):
    """Marketplace's own price string -> int, or None. Kept for the discrepancy."""
    if not s:
        return None
    if re.search(r"^\s*(free|miễn phí)\s*$", s, re.I):
        return 0
    m = re.search(r"[₫đ₱$]\s*([\d.,]+)", s) or re.search(r"([\d.,]{2,})", s)
    if not m:
        return None
    digits = re.sub(r"[.,\s]", "", m.group(1))
    return int(digits) if digits.isdigit() else None


def parse_area(text):
    """Every area figure in m², as (m2, snippet). '30m2-35m2' yields both."""
    if not text:
        return []
    out = []
    for m in re.finditer(r"(?<![\d.,])(\d{1,4}(?:[.,]\d{1,2})?)\s*"
                         r"(?:m2|m²|sqm|sq\.?\s?m|mét vuông|met vuong)\b", text, re.I):
        val = float(m.group(1).replace(",", "."))
        if 8 <= val <= 2000:
            out.append((val, _norm(m.group(0))))
    for m in re.finditer(r"(?<![\d.,])(\d{1,3}(?:[.,]\d)?)\s*[x×]\s*(\d{1,3}(?:[.,]\d)?)\s*m\b",
                         text, re.I):
        val = float(m.group(1).replace(",", ".")) * float(m.group(2).replace(",", "."))
        if 8 <= val <= 2000:
            out.append((val, _norm(m.group(0))))
    seen, uniq = set(), []
    for v, s in out:
        if v not in seen:
            seen.add(v)
            uniq.append((v, s))
    return sorted(uniq)


ADDR_MARKER_RE = re.compile(
    r"địa chỉ|đ/c\b|\bdc\s*[:.]|số nhà|\bđường\b|\bphố\b|\bngõ\b|\bhẻm\b|"
    r"\bquận\b|\bphường\b|\bkhu phố\b|\bkdc\b|chung cư|tòa nhà|toà nhà|"
    r"\bstreet\b|\bst\.\b|\baddress\b|\blocated (?:at|in)\b|\bnear\b|"
    r"\bbarangay\b|\bbrgy\.?\b|\bsubdivision\b|\bsubd\.?\b|\bavenue\b|\bave\.\b|"
    r"\bward\b|\bdistrict\b|\bcity\b|\bpurok\b|\bsitio\b", re.I)
ADDR_NUMBER_RE = re.compile(r"\b\d{1,4}[A-Za-z]?[/\-]?\d{0,3}\s+(?:[^\W\d_]{2,}\s?){1,4}")


def find_address(text):
    """The address line out of the BODY. Trap 1: Facebook's district field lies.

    The Marketplace ad measured on 4 Sep 2026 said "Listed in Quận Đống Đa"
    while its own body gave 47 Nam Dư, Hoàng Mai -- the other side of Hanoi, and
    Facebook prints "Location is approximate" on its own map. Group posts have
    no district field at all, so the body is the only source. A post with no
    address is disqualified: that is already the site's rule and it removes a
    large share of Facebook posts.
    """
    if not text:
        return None
    # A Facebook post is often one long paragraph, so work at sentence level
    # too -- otherwise the "address" comes back as the whole ad.
    chunks = []
    for line in text.splitlines():
        line = _norm(line)
        if len(line) < 6:
            continue
        if len(line) <= 120:
            chunks.append(line)
        else:
            parts = [p for p in re.split(r"(?<=[.!?;•|])\s+|\s+[-–—]\s+", line) if p]
            chunks.extend(_norm(p) for p in parts if len(_norm(p)) >= 6)
    strong = re.compile(r"địa chỉ|đ/c\b|\baddress\b|\blocated (?:at|in)\b|\blocation\b", re.I)
    for c in chunks:
        if strong.search(c):
            return c
    for c in chunks:
        if ADDR_MARKER_RE.search(c) and ADDR_NUMBER_RE.search(c):
            return c
    for c in chunks:
        if ADDR_MARKER_RE.search(c):
            return c
    return None


AGENCY_RE = re.compile(
    r"\bland\b|\bbđs\b|\bbds\b|bất động sản|real ?estate|\bagency\b|\bbroker\b|"
    r"\brealty\b|\brealtor\b|\bproperties\b|\bco\.,? ?ltd\b|\bmôi giới\b|"
    r"#chothue|#bds|\blicensed\b", re.I)


def guess_seller_kind(seller_name, body):
    """Marketplace's "individuals only" switch does not exclude agencies -- the
    best find of the first pass was posted by "Thảo (Khải Lộc Land)". Groups
    have no such switch at all. Record a guess, not a verdict."""
    if AGENCY_RE.search(seller_name or ""):
        return "agency"
    if AGENCY_RE.search(" ".join(x for x in (seller_name, body) if x)):
        return "probably-agency"
    return "unknown"


# ---- dates ----------------------------------------------------------------

MONTHS = {m: i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"])}
MONTHS.update({m[:3]: i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"])})

REL_PATTERNS = [
    (re.compile(r"^(just now|vừa xong|mới đây)$", re.I), lambda m: (0, "relative-minutes")),
    (re.compile(r"^(\d+)\s*(?:m|min|mins|minutes?|phút)( ago| trước)?$", re.I),
     lambda m: (0, "relative-minutes")),
    (re.compile(r"^(\d+)\s*(?:h|hr|hrs|hours?|giờ)( ago| trước)?$", re.I),
     lambda m: (0, "relative-hours")),
    (re.compile(r"^(\d+)\s*(?:d|days?|ngày)( ago| trước)?$", re.I),
     lambda m: (int(m.group(1)), "relative-days")),
    (re.compile(r"^(\d+)\s*(?:w|wks?|weeks?|tuần)( ago| trước)?$", re.I),
     lambda m: (int(m.group(1)) * 7, "relative-weeks")),
    (re.compile(r"^(yesterday|hôm qua)\b", re.I), lambda m: (1, "relative-days")),
    (re.compile(r"^(today|hôm nay)\b", re.I), lambda m: (0, "relative-days")),
    (re.compile(r"^listed\s+(\d+)\s+days?\s+ago$", re.I),
     lambda m: (int(m.group(1)), "relative-days")),
    (re.compile(r"^listed\s+(\d+)\s+weeks?\s+ago$", re.I),
     lambda m: (int(m.group(1)) * 7, "relative-weeks")),
    (re.compile(r"^listed\s+(\d+)\s+(?:hours?|minutes?)\s+ago$", re.I),
     lambda m: (0, "relative-hours")),
    (re.compile(r"^just listed$", re.I), lambda m: (0, "relative-hours")),
]
ABS_DATE_RE = re.compile(
    r"^(?:(?P<d1>\d{1,2})\s+(?P<mon1>[A-Za-zÀ-ỹ]{3,12})|"
    r"(?P<mon2>[A-Za-zÀ-ỹ]{3,12})\s+(?P<d2>\d{1,2}))"
    r"(?:,?\s*(?P<year>20\d{2}))?(?:\s+at\b.*)?$", re.I)


def parse_timestamp(text, today=None):
    """(days_ago, raw, precision) or (None, None, None).

    NEVER invent a number here. `None` means the page published nothing
    parseable, and downstream refuses to publish those -- a made-up `daysAgo`
    would be a lie in the one field this whole site is built on.
    """
    s = _norm(text)
    if not s or len(s) > 40:
        return (None, None, None)
    for rx, fn in REL_PATTERNS:
        m = rx.match(s)
        if m:
            days, prec = fn(m)
            return (days, s, prec)
    m = ABS_DATE_RE.match(s)
    if m:
        mon = (m.group("mon1") or m.group("mon2") or "").lower()
        day = m.group("d1") or m.group("d2")
        num = MONTHS.get(mon) or MONTHS.get(mon[:3])
        if num and day:
            today = today or datetime.now().date()
            year = int(m.group("year")) if m.group("year") else today.year
            try:
                d = datetime(year, num, int(day)).date()
            except ValueError:
                return (None, None, None)
            if not m.group("year") and d > today:
                d = datetime(year - 1, num, int(day)).date()
            return ((today - d).days, s, "absolute-date")
    return (None, None, None)


def pick_timestamp(strings, today=None):
    for s in strings or []:
        days, raw, prec = parse_timestamp(s, today=today)
        if days is not None:
            return days, raw, prec
    return (None, None, None)


# ---- classification -------------------------------------------------------

def classify(title, body, currency="VND"):
    """(ok, reason).

    On Marketplace roughly one listing in seven survived the first real pass.
    In groups it will be worse: off-topic posts are the norm, not the exception
    -- the group titled HOUSE AND ROOMS FOR RENT DUMAGUETE was showing footwear
    at PHP 85 when it was opened by hand on 4 Sep 2026.
    """
    blob = "%s\n%s" % (title or "", body or "")
    if not body or len(body) < 20:
        return False, "no usable text (skeleton card, or an image-only post)"
    if UNAVAILABLE_RE.search(blob):
        return False, "Facebook says the content is not available"
    if looks_obfuscated(body):
        return False, "text obfuscated character-by-character (moderation-evasion spam)"
    if currency == "VND" and SALE_RE.search(blob):
        return False, "sale, not a rental (figure in tỷ: %r)" % _norm(SALE_RE.search(blob).group(0))
    if NON_RENTAL_RE.search(blob):
        return False, "not a rental post (%r)" % _norm(NON_RENTAL_RE.search(blob).group(0))
    if SALE_CUE_RE.search(blob) and not RENT_CUE_RE.search(blob):
        return False, "reads as a sale, no rental cue in the text"
    if not RENT_CUE_RE.search(blob):
        return False, "no rental cue ('for rent' / 'cho thuê' / '/month')"
    return True, None


# ==========================================================================
# Browser
# ==========================================================================

def _sleep(a, b):
    time.sleep(random.uniform(a, b))


def _block_writes(route):
    """Request-level backstop for the read-only invariant."""
    req = route.request
    if any(bit in req.url for bit in BLOCKED_URL_BITS) and req.is_navigation_request():
        return route.abort()
    return route.continue_()


def _safe_click(page, locator, label):
    """The ONLY click in this file. Refuses anything not on the allowlist."""
    if not ALLOWED_CLICK_LABELS.match(_norm(label)):
        raise RuntimeError("refusing to click %r -- not on ALLOWED_CLICK_LABELS "
                           "(read-only invariant, see the module docstring)" % label)
    locator.click(timeout=4000)


CHECKPOINT_RE = re.compile(
    r"/checkpoint/|confirm your identity|xác nhận danh tính|"
    r"we've temporarily|tạm thời bị khóa|security check|kiểm tra bảo mật|"
    r"unusual activity|hoạt động bất thường", re.I)


def check_alive(page):
    """Stop the whole run on a login wall or a checkpoint.

    Nothing here tries to answer a challenge -- that is exactly the line this
    script does not cross. It stops and tells the owner, who decides.
    """
    url = page.url or ""
    if "/login" in url or "/checkpoint" in url:
        raise SystemExit(
            "STOP: Facebook redirected to %s.\n"
            "Either the saved session expired (run `python fb_collect.py --login`)\n"
            "or the account has been checkpointed. Do NOT re-run this script until\n"
            "you have opened Facebook by hand and confirmed the account is fine." % url)
    try:
        head = page.inner_text("body", timeout=3000)[:4000]
    except Exception:
        return
    if CHECKPOINT_RE.search(head):
        raise SystemExit(
            "STOP: the page looks like a security checkpoint or an identity check.\n"
            "This script will not answer one. Open Facebook by hand, resolve it there,\n"
            "and consider whether this collector should keep running at all.")


def open_context(pw, headless, channel):
    os.makedirs(PROFILE_DIR, exist_ok=True)
    kwargs = dict(
        user_data_dir=PROFILE_DIR,
        headless=headless,
        viewport={"width": 1440, "height": 950},
        locale="en-US",
        timezone_id="Asia/Ho_Chi_Minh",
        accept_downloads=False,
    )
    try:
        ctx = (pw.chromium.launch_persistent_context(channel=channel, **kwargs)
               if channel else pw.chromium.launch_persistent_context(**kwargs))
    except Exception as e:
        if not channel:
            raise
        print("could not launch channel=%s (%s); falling back to bundled Chromium"
              % (channel, e))
        ctx = pw.chromium.launch_persistent_context(**kwargs)
    ctx.set_default_timeout(45000)
    ctx.route("**/*", _block_writes)
    return ctx


def is_logged_in(ctx):
    for c in ctx.cookies("https://www.facebook.com/"):
        if c.get("name") == "c_user" and c.get("value"):
            return True
    return False


def do_login(headless, channel):
    from playwright.sync_api import sync_playwright
    if headless:
        raise SystemExit("--login needs a visible window; drop --headless")
    with sync_playwright() as pw:
        ctx = open_context(pw, headless=False, channel=channel)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto("https://www.facebook.com/", wait_until="domcontentloaded")
        print("\nA browser window is open on its OWN profile (%s)." % PROFILE_DIR)
        print("Log in there by hand -- type the password yourself, this script never")
        print("touches credentials. Two-factor, 'save this browser', all of it is yours")
        print("to click. When Facebook shows your normal feed, come back here.\n")
        try:
            input("Press Enter when you are logged in... ")
        except EOFError:
            print("(no stdin -- waiting 120 s instead)")
            time.sleep(120)
        ok = is_logged_in(ctx)
        print("logged in: %s" % ("YES -- the session is saved in the profile" if ok else
                                 "NO -- no c_user cookie; nothing was saved"))
        ctx.close()
        return 0 if ok else 1


SEE_MORE_RE = re.compile(r"^(see more|xem thêm)\.{0,3}$", re.I)


def expand_text(page, limit=6):
    """Click 'See more' so post bodies are not truncated. Allowlisted, view-only."""
    try:
        buttons = page.locator('div[role="button"], span[role="button"], button')
        n = min(buttons.count(), 120)
    except Exception:
        return
    clicked = 0
    for i in range(n):
        if clicked >= limit:
            return
        b = buttons.nth(i)
        try:
            label = _norm(b.inner_text(timeout=600))
        except Exception:
            continue
        if SEE_MORE_RE.match(label):
            try:
                _safe_click(page, b, label)
                clicked += 1
                _sleep(0.3, 0.7)
            except Exception:
                pass


FB_IMG_RE = re.compile(r"(scontent|fbcdn)", re.I)
FB_IMG_KEY_RE = re.compile(r"/(\d+_\d+_\d+_[a-z]\.(?:jpg|jpeg|png|webp))")


def _img_key(src):
    m = FB_IMG_KEY_RE.search(src)
    return m.group(1) if m else src.split("?")[0]


def pick_images(images, cap, min_w=400, min_h=300):
    """Listing photos out of a pile of <img>: fbcdn only, big enough to be a
    real photo rather than an avatar or a reaction icon, biggest first."""
    found = {}
    for im in images or []:
        src = im.get("src") or ""
        if not FB_IMG_RE.search(src):
            continue
        w, h = im.get("w") or 0, im.get("h") or 0
        if w < min_w or h < min_h:
            continue
        k = _img_key(src)
        if k not in found or w * h > found[k][1]:
            found[k] = (src, w * h)
    return [src for src, _ in sorted(found.values(), key=lambda t: -t[1])[:cap]]


def fetch_bytes(ctx, page, url):
    """Fetch inside the authenticated session. The API context carries the
    browser's cookies; the in-page fetch is the fallback."""
    try:
        r = ctx.request.get(url, timeout=30000)
        if r.ok:
            return r.body()
    except Exception:
        pass
    try:
        import base64
        b64 = page.evaluate(
            """async (u) => {
                 const r = await fetch(u, {credentials: 'include'});
                 if (!r.ok) return null;
                 const buf = new Uint8Array(await r.arrayBuffer());
                 let s = '';
                 for (let i = 0; i < buf.length; i++) s += String.fromCharCode(buf[i]);
                 return btoa(s);
               }""", url)
        if b64:
            return base64.b64decode(b64)
    except Exception:
        pass
    return None


def downscale(raw, max_edge=1200, budget=150_000):
    """-> (bytes, ext, w, h). WebP, longest edge 1200, well under 150 KB."""
    from PIL import Image
    im = Image.open(io.BytesIO(raw))
    if im.mode not in ("RGB", "L"):
        im = im.convert("RGB")
    im.thumbnail((max_edge, max_edge), Image.LANCZOS)
    for quality in (82, 72, 62):
        buf = io.BytesIO()
        im.save(buf, "WEBP", quality=quality, method=6)
        data = buf.getvalue()
        if len(data) <= budget:
            return data, "webp", im.width, im.height
    im.thumbnail((1000, 1000), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=60, method=6)
    return buf.getvalue(), "webp", im.width, im.height


def save_photos(ctx, page, key, urls, photo_root=PHOTO_ROOT):
    out_dir = os.path.join(photo_root, str(key))
    saved = []
    for i, url in enumerate(urls, 1):
        raw = fetch_bytes(ctx, page, url)
        if not raw:
            continue
        try:
            data, ext, w, h = downscale(raw)
        except Exception as e:
            print("    photo %d: could not process (%s)" % (i, e))
            continue
        os.makedirs(out_dir, exist_ok=True)
        name = "%02d.%s" % (i, ext)
        with open(os.path.join(out_dir, name), "wb") as fh:
            fh.write(data)
        saved.append({"file": "%s/%s/%s" % (PHOTO_REL_ROOT, key, name),
                      "bytes": len(data), "w": w, "h": h})
        _sleep(0.3, 0.8)
    return saved


PHOTO_NOTE = ("Downloaded inside the logged-in session and re-encoded locally. "
              "Facebook's own image URLs are signed and expire in about four days, "
              "so they are never stored. Relative paths render on GitHub Pages; they "
              "do NOT render inside the claude.ai Artifact copy of the site.")


# ---- site dedupe ----------------------------------------------------------

def site_fb_ids():
    """Facebook ids already on the built site -- both Marketplace item ids and
    group post ids -- so a run does not re-offer what is published."""
    try:
        from site_data import load_listings
        listings = load_listings(os.path.join(HERE, "vietnam-rent-finder.html"))
    except SystemExit as e:
        print("note: could not read the built site (%s) -- no dedupe this run" % e)
        return set()
    except Exception as e:
        print("note: site_data unavailable (%s) -- no dedupe this run" % e)
        return set()
    ids = set()

    def eat(u):
        for rx in (MP_ITEM_ID_RE, GROUP_POST_ID_RE):
            m = rx.search(u or "")
            if m:
                ids.add(m.group(1))

    for l in listings:
        eat(l.get("url"))
        for alt in (l.get("details") or {}).get("alsoOn", []) or []:
            eat(alt.get("url"))
    return ids


# ==========================================================================
# GROUPS -- the primary path
# ==========================================================================

GROUP_JS = r"""
() => {
  const posts = [];
  for (const art of document.querySelectorAll('div[role="article"]')) {
    // Comments render as nested articles. Only top-level nodes are posts.
    if (art.parentElement && art.parentElement.closest('[role="article"]')) continue;

    const links = [];
    for (const a of art.querySelectorAll('a[href]')) {
      const h = a.href || '';
      if (/\/groups\/[^\/]+\/(posts|permalink)\//.test(h) ||
          h.indexOf('multi_permalink_id') >= 0) {
        links.push({href: h, text: (a.innerText || '').trim().slice(0, 60)});
      }
    }
    const authors = [];
    for (const a of art.querySelectorAll(
          'a[href*="/groups/"][href*="/user/"], h3 a[href], strong a[href], a[href*="profile.php"]')) {
      const t = (a.innerText || '').trim();
      if (t && t.length < 80) authors.push({name: t, href: a.href});
      if (authors.length >= 4) break;
    }
    const images = [];
    for (const im of art.querySelectorAll('img')) {
      const src = im.currentSrc || im.src || '';
      if (!src || src.startsWith('data:') || src.startsWith('blob:')) continue;
      images.push({src: src, w: im.naturalWidth || 0, h: im.naturalHeight || 0});
    }
    posts.push({
      text: art.innerText || '',
      links: links,
      authors: authors,
      images: images,
      aria: art.getAttribute('aria-label') || ''
    });
  }
  return posts;
}
"""

# The engagement furniture at the bottom of every card, and the header noise at
# the top. Dropped line-by-line so the body is the post itself.
POST_CHROME_RE = re.compile(
    r"^(like|comment|share|send|reply|view \d+ (more )?comments?|"
    r"all reactions?|top contributor|admin|moderator|author|follow|"
    r"see more|xem thêm|thích|bình luận|chia sẻ|\d+ comments?|\d+ shares?|"
    r"\d+[km]?( reactions?)?|·|shared with .*|public|group by .*|"
    r"most relevant|newest|write a comment|viết bình luận)$", re.I)


def clean_post_body(text, author_name=None, time_raw=None):
    """The post itself, out of a feed card's innerText."""
    txt = clean_text(text)
    lines = []
    for raw in txt.split("\n"):
        l = _norm(raw)
        if not l or POST_CHROME_RE.match(l):
            continue
        if author_name and l == _norm(author_name):
            continue
        if time_raw and l == _norm(time_raw):
            continue
        lines.append(l)
    return "\n".join(lines).strip()


def wait_for_posts(page, want, budget_s):
    """Group feeds render lazily: right after load, `[role="article"]` matches
    two or three nodes and most cards are still skeletons. Poll instead of
    trusting the load event."""
    deadline = time.time() + budget_s
    while time.time() < deadline:
        try:
            posts = page.evaluate(GROUP_JS)
        except Exception:
            posts = []
        real = [p for p in posts if len(p.get("text") or "") > 120 and p.get("links")]
        if len(real) >= want:
            return real
        time.sleep(1.5)
    return []


def harvest_group(page, want, max_scrolls, verbose=True):
    """Small, slow scroll steps -- a big jump outruns the lazy renderer."""
    seen, out = set(), []
    stale = 0
    for i in range(max_scrolls):
        real = wait_for_posts(page, want=1, budget_s=12)
        before = len(out)
        for p in real:
            pid = None
            for l in p.get("links") or []:
                m = GROUP_POST_ID_RE.search(l.get("href") or "")
                if m:
                    pid = m.group(1)
                    break
            if not pid or pid in seen:
                continue
            seen.add(pid)
            p["post_id"] = pid
            out.append(p)
        if verbose:
            print("  scroll %d: %d posts so far" % (i + 1, len(out)))
        if len(out) >= want:
            break
        stale = stale + 1 if len(out) == before else 0
        if stale >= 3:
            if verbose:
                print("  feed stopped producing new posts")
            break
        page.mouse.wheel(0, 1200)
        _sleep(2.0, 4.0)
    return out


def post_permalink(post, gid):
    for l in post.get("links") or []:
        h = l.get("href") or ""
        if GROUP_POST_ID_RE.search(h):
            return h.split("?")[0]
    return GROUP_URL.format(gid=gid)


def post_author(post):
    for a in post.get("authors") or []:
        name = _norm(a.get("name"))
        if not name or len(name) > 60:
            continue
        if parse_timestamp(name)[0] is not None:   # that anchor was the timestamp
            continue
        if POST_CHROME_RE.match(name):
            continue
        return a
    return {}


def post_timestamp(post, today=None):
    """The timestamp lives in the permalink anchor's text ('3h', '2d',
    'September 1 at 10:04'). Facebook rounds the relative forms, so '1w' means
    somewhere in 7-13 days -- `age_precision` carries that caveat forward."""
    strings = [l.get("text") for l in post.get("links") or []]
    strings += [s for s in (post.get("aria") or "").split("\n")]
    return pick_timestamp(strings, today=today)


def collect_groups(args, ctx, page, result, known):
    city_key = args.city_key or CITY_SLUG_TO_KEY.get(args.city) or args.city
    currency = "PHP" if city_key in PH_CITIES else "VND"

    if args.group:
        # An explicit --group list is the owner asking for exactly those.
        groups = [{"id": g, "name": None} for g in args.group]
    else:
        groups = GROUPS.get(city_key) or []
        if not groups:
            raise SystemExit("no groups registered for city key %r. Known: %s"
                             % (city_key, ", ".join(sorted(k for k in GROUPS if k != "_unassigned"))))
        groups = groups[:args.max_groups]
    result["run"]["groups"] = groups
    result["run"]["currency"] = currency
    print("city %s (%s), %d group(s), cap %d posts total"
          % (city_key, currency, len(groups), args.max_items))

    budget = args.max_items
    for gi, g in enumerate(groups, 1):
        if budget <= 0:
            break
        gid = g["id"]
        url = GROUP_URL.format(gid=gid) + (GROUP_SORT_PARAM if args.chronological else "")
        print("\n[group %d/%d] %s %s" % (gi, len(groups), gid, g.get("name") or ""))
        try:
            page.goto(url, wait_until="domcontentloaded")
            _sleep(4.0, 7.0)
            check_alive(page)
            expand_text(page)
            posts = harvest_group(page, want=min(budget * 3, 40), max_scrolls=args.max_scrolls)
        except SystemExit:
            raise
        except Exception as e:
            result["errors"].append({"group": gid, "error": str(e)[:300]})
            print("  error: %s" % str(e)[:160])
            continue

        print("  %d post(s) harvested" % len(posts))
        for post in posts:
            if budget <= 0:
                break
            pid = post["post_id"]
            permalink = post_permalink(post, gid)
            if pid in known:
                result["rejected"].append({"post_id": pid, "url": permalink,
                                           "group": gid, "reason": "already on the site"})
                continue
            author = post_author(post)
            days, time_raw, precision = post_timestamp(post)
            body = clean_post_body(post.get("text"), author.get("name"), time_raw)
            ok, reason = classify(None, body, currency=currency)
            if not ok:
                result["rejected"].append({"post_id": pid, "url": permalink, "group": gid,
                                           "reason": reason, "excerpt": body[:160]})
                continue
            address = find_address(body)
            if not address:
                result["rejected"].append({"post_id": pid, "url": permalink, "group": gid,
                                           "reason": "no address in the post text",
                                           "excerpt": body[:160]})
                continue
            prices = parse_prices(body, currency)
            usd = parse_prices_usd(body)
            if not prices and not usd:
                result["rejected"].append({"post_id": pid, "url": permalink, "group": gid,
                                           "reason": "no price in the post text",
                                           "excerpt": body[:160]})
                continue

            budget -= 1
            images = post.get("images") or []
            full_body = body

            if args.open_permalinks:
                print("  opening %s" % permalink)
                try:
                    page.goto(permalink, wait_until="domcontentloaded")
                    _sleep(3.0, 5.0)
                    check_alive(page)
                    expand_text(page, limit=3)
                    detail = page.evaluate(GROUP_JS)
                    if detail:
                        d = detail[0]
                        d_author = post_author(d) or author
                        d_days, d_raw, d_prec = post_timestamp(d)
                        d_body = clean_post_body(d.get("text"), d_author.get("name"), d_raw)
                        if len(d_body) > len(full_body):
                            full_body = d_body
                        if d_days is not None and days is None:
                            days, time_raw, precision = d_days, d_raw, d_prec
                        if d.get("images"):
                            images = d["images"]
                        author = d_author or author
                except SystemExit:
                    raise
                except Exception as e:
                    result["errors"].append({"post_id": pid, "url": permalink,
                                             "error": str(e)[:300]})

            prices = parse_prices(full_body, currency) or prices
            areas = parse_area(full_body)
            cand = {
                "kind": "group_post",
                "post_id": pid,
                "group_id": gid,
                "group_name": g.get("name"),
                "url": permalink,
                "city_key": city_key,
                "district": None,
                "district_hint_from_address": find_address(full_body) or address,
                "currency": currency,
                "price": prices[0][0] if prices else None,
                "price_snippet": prices[0][1] if prices else None,
                "price_candidates": [{"amount": v, "snippet": s} for v, s in prices],
                "usd_price_candidates": [{"usd": v, "snippet": s} for v, s in usd],
                "area_m2": areas[0][0] if areas else None,
                "area_candidates": [{"m2": v, "snippet": s} for v, s in areas],
                "author_name": author.get("name"),
                "author_url": author.get("href"),
                "seller_kind_guess": guess_seller_kind(author.get("name"), full_body),
                "age_days": days,
                "age_raw": time_raw,
                "age_precision": precision,
                "age_note": age_note(days, time_raw, precision),
                "body": full_body,
                "photos": [],
                "collected_at": datetime.now(timezone.utc).isoformat(),
                "notice_seed": notice_seed(days, precision, currency),
            }
            if not args.no_photos:
                urls = pick_images(images, args.max_photos)
                cand["photos"] = save_photos(ctx, page, pid, urls)
                cand["photo_note"] = PHOTO_NOTE
                print("    %d photo(s), %d KB"
                      % (len(cand["photos"]), sum(p["bytes"] for p in cand["photos"]) // 1024))
            result["candidates"].append(cand)
            print("    kept: %s | %s %s | %s"
                  % ((cand["body"].splitlines() or [""])[0][:50],
                     "{:,}".format(cand["price"]) if cand["price"] else "?",
                     currency, (cand["district_hint_from_address"] or "")[:40]))
            _sleep(args.pause_min, args.pause_max)
    return result


def age_note(days, raw, precision):
    if days is None:
        return ("Facebook published no parseable timestamp on this post. `age_days` is "
                "null on purpose -- downstream refuses to publish a listing without a "
                "date, and inventing one would be a lie in the one field this whole "
                "site is built on.")
    if precision == "absolute-date":
        return ("Posted %s -- an absolute date off the post header, %d day(s) ago."
                % (raw, days))
    if precision == "relative-weeks":
        return ("Facebook showed %r. It rounds weeks down, so this is somewhere in "
                "%d-%d days, not exactly %d." % (raw, days, days + 6, days))
    return "Facebook showed %r, i.e. about %d day(s) ago." % (raw, days)


def notice_seed(days, precision, currency):
    """Half-written `notice` text for whoever writes the listing row. Facts only."""
    bits = []
    if days is None:
        bits.append("Facebook did not publish a date for this post.")
    elif precision == "relative-weeks":
        bits.append("Facebook gives the age only in whole weeks, so the date is "
                    "accurate to about a week.")
    else:
        bits.append("The date comes from Facebook's own relative timestamp on the post.")
    bits.append("The price and the address were read out of the post text -- a Facebook "
                "post has no structured price or address field.")
    if currency == "PHP":
        bits.append("The price is in Philippine pesos, as written in the post; it has not "
                    "been converted.")
    return " ".join(bits)


# ==========================================================================
# MARKETPLACE -- the secondary path
# ==========================================================================

def build_feed_url(city, category, days, radius, c2c):
    q = ["sortBy=creation_time_descend", "exact=false"]
    if days:
        q.append("daysSinceListed=%d" % days)
    if radius:
        q.append("radius=%d" % radius)
    if c2c:
        q.append("isC2CListingOnly=1")
    return FEED_BASE.format(city=city, category=category) + "?" + "&".join(q)


FEED_JS = r"""
() => {
  const out = [], seen = new Set();
  for (const a of document.querySelectorAll('a[href*="/marketplace/item/"]')) {
    const m = (a.getAttribute('href') || '').match(/\/marketplace\/item\/(\d{6,})/);
    if (!m || seen.has(m[1])) continue;
    seen.add(m[1]);
    out.push({id: m[1], aria: a.getAttribute('aria-label') || '',
              text: (a.innerText || '').trim().slice(0, 300)});
  }
  return out;
}
"""

ITEM_JS = r"""
() => {
  const main = document.querySelector('div[role="main"]') || document.body;
  const cuts = ["Today's picks", "Gợi ý hôm nay", "More like this",
                "Similar listings", "Sản phẩm tương tự", "Related searches",
                "You might also like", "Xem thêm mặt hàng"];
  let text = main.innerText || "";
  let at = -1;
  for (const c of cuts) {
    const i = text.indexOf(c);
    if (i > 150 && (at < 0 || i < at)) at = i;
  }
  if (at > 0) text = text.slice(0, at);

  const h1 = main.querySelector('h1');
  const leaves = [], seen = new Set();
  for (const el of main.querySelectorAll('*')) {
    if (el.children.length) continue;
    const t = (el.innerText || el.textContent || '').trim();
    if (!t || t.length > 60 || seen.has(t)) continue;
    seen.add(t); leaves.push(t);
    if (leaves.length >= 400) break;
  }
  const sellers = [];
  for (const a of main.querySelectorAll(
        'a[href*="/marketplace/profile/"], a[href*="profile.php"], a[href*="/people/"]')) {
    const t = (a.innerText || '').trim();
    if (t && t.length < 80) sellers.push({name: t, href: a.href});
  }
  const images = [];
  for (const im of main.querySelectorAll('img')) {
    const src = im.currentSrc || im.src || '';
    if (!src || src.startsWith('data:') || src.startsWith('blob:')) continue;
    images.push({src: src, w: im.naturalWidth || 0, h: im.naturalHeight || 0});
  }
  return {title: h1 ? h1.innerText.trim() : '', text: text, leaves: leaves,
          sellers: sellers, images: images, url: location.href};
}
"""

DESC_HEAD_RE = re.compile(r"^(description|mô tả|details|chi tiết|thông tin chi tiết)$", re.I)
DESC_TAIL_RE = re.compile(
    r"^(seller information|thông tin người bán|message|nhắn tin|send seller a message|"
    r"location is approximate|vị trí chỉ là tương đối|report listing|báo cáo tin|"
    r"meet the seller)$", re.I)
PLACE_LINE_RE = re.compile(
    r"^(?:listed in|rental location|đã đăng tại|vị trí cho thuê|location)\s*[:\-]?\s*(.+)$",
    re.I)


def extract_body(text):
    """The ad text out of a Marketplace item page.

    The first pass learned this the hard way: hand-slicing document.body.innerText
    kept returning the "Today's picks" rail instead of the listing, prices and
    all. ITEM_JS already cuts the rail off; this takes the block after the
    Description/Details heading when there is one, and otherwise everything
    between the price line and the seller block.
    """
    lines = [_norm(l) for l in clean_text(text).splitlines()]
    start = None
    for i, l in enumerate(lines):
        if DESC_HEAD_RE.match(l):
            start = i + 1
            break
    if start is None:
        for i, l in enumerate(lines):
            if re.match(r"^[₫$₱][\d.,]+", l) or re.match(r"^(free|miễn phí)$", l, re.I):
                start = i + 1
                break
    if start is None:
        start = 0
    out = []
    for l in lines[start:]:
        if DESC_TAIL_RE.match(l):
            break
        out.append(l)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out).strip())


def find_fb_place(text, leaves):
    for src in (text or "").splitlines():
        m = PLACE_LINE_RE.match(_norm(src))
        if m and m.group(1):
            return _norm(m.group(1))
    lines = [_norm(l) for l in (text or "").splitlines()]
    for i, l in enumerate(lines):
        if re.match(r"^(rental location|listed in|vị trí cho thuê)$", l, re.I):
            for nxt in lines[i + 1:i + 3]:
                if nxt:
                    return nxt
    for t in leaves or []:
        m = PLACE_LINE_RE.match(_norm(t))
        if m and m.group(1):
            return _norm(m.group(1))
    return None


def parse_aria(aria):
    m = ARIA_RE.match(_norm(aria or ""))
    if not m:
        return {}
    return {"title": _norm(m.group("title")),
            "price_field": _norm(m.group("price") or "").rstrip(",."),
            "place": _norm(m.group("place") or "")}


def harvest_feed(page, want, max_scrolls, verbose=True):
    found, stale = {}, 0
    for i in range(max_scrolls):
        for row in page.evaluate(FEED_JS):
            found.setdefault(row["id"], row)
        if verbose:
            print("  scroll %d: %d listings so far" % (i + 1, len(found)))
        if len(found) >= want:
            break
        before = len(found)
        page.mouse.wheel(0, 2400)
        _sleep(1.8, 3.4)
        stale = stale + 1 if len(page.evaluate(FEED_JS)) <= before else 0
        if stale >= 2:
            if verbose:
                print("  feed stopped producing new listings")
            break
    return list(found.values())


def collect_photo_urls_mp(page, cap, gallery_clicks):
    """Marketplace photos. Stepping the carousel is the second allowlisted click:
    without it the DOM usually holds a single full-size image."""
    found = {}

    def sweep():
        try:
            data = page.evaluate(ITEM_JS)
        except Exception:
            return
        for src in pick_images(data.get("images"), cap * 3):
            found.setdefault(_img_key(src), src)

    sweep()
    for _ in range(max(0, gallery_clicks)):
        if len(found) >= cap:
            break
        before, moved = len(found), False
        for name in ("Next photo", "Next", "Ảnh tiếp theo"):
            try:
                btn = page.get_by_label(name, exact=True).first
                if btn.count() and btn.is_visible():
                    _safe_click(page, btn, name)
                    moved = True
                    break
            except Exception:
                continue
        if not moved:
            break
        _sleep(0.7, 1.4)
        sweep()
        if len(found) == before:
            break
    return list(found.values())[:cap]


def collect_marketplace(args, ctx, page, result, known):
    city_key = args.city_key or CITY_SLUG_TO_KEY.get(args.city)
    currency = "PHP" if city_key in PH_CITIES else "VND"
    feed_url = args.feed_url or build_feed_url(args.city, args.category, args.days,
                                               args.radius, not args.no_c2c)
    result["run"]["feed_url"] = feed_url
    result["run"]["currency"] = currency
    print("feed: %s" % feed_url)

    page.goto(feed_url, wait_until="domcontentloaded")
    _sleep(3.0, 5.0)
    check_alive(page)
    rows = harvest_feed(page, want=args.max_items * 3, max_scrolls=args.max_scrolls)
    print("feed gave %d distinct listings" % len(rows))
    result["run"]["feed_listings_seen"] = len(rows)

    queue = []
    for r in rows:
        meta = parse_aria(r.get("aria"))
        if r["id"] in known:
            result["rejected"].append({"fb_id": r["id"], "url": ITEM_URL.format(id=r["id"]),
                                       "title": meta.get("title"),
                                       "reason": "already on the site"})
            continue
        queue.append((r, meta))
    queue = queue[:args.max_items]
    print("opening %d item pages (cap %d)" % (len(queue), args.max_items))

    if args.feed_only:
        for r, meta in queue:
            result["candidates"].append({
                "kind": "marketplace_feed_only", "fb_id": r["id"],
                "url": ITEM_URL.format(id=r["id"]), "title": meta.get("title"),
                "feed_aria": r.get("aria"), "fb_price_field_text": meta.get("price_field"),
                "fb_place_field": meta.get("place"),
                "note": "feed-only run: the item page was not opened"})
        return result

    blank_streak = 0
    for n, (r, meta) in enumerate(queue, 1):
        fb_id = r["id"]
        url = ITEM_URL.format(id=fb_id)
        print("[%d/%d] %s" % (n, len(queue), url))
        try:
            page.goto(url, wait_until="domcontentloaded")
            _sleep(2.5, 4.5)
            check_alive(page)
            expand_text(page, limit=2)
            data = page.evaluate(ITEM_JS)
        except SystemExit:
            raise
        except Exception as e:
            result["errors"].append({"fb_id": fb_id, "url": url, "error": str(e)[:300]})
            print("    error: %s" % str(e)[:160])
            _sleep(args.pause_min, args.pause_max)
            continue

        title = _norm(clean_text(data.get("title"))) or meta.get("title") or ""
        if not title:
            blank_streak += 1
            result["rejected"].append({"fb_id": fb_id, "url": url,
                                       "reason": "item page returned no title "
                                                 "(logged out, rate-limited or gone)"})
            if blank_streak >= 2:
                raise SystemExit("STOP: two item pages in a row came back empty. That "
                                 "usually means Facebook has started throttling this "
                                 "session. Stop for today.")
            _sleep(args.pause_min, args.pause_max)
            continue
        blank_streak = 0

        page_text = clean_text(data.get("text"))
        leaves = [clean_text(t) for t in (data.get("leaves") or [])]
        body = extract_body(page_text)
        blob = "%s\n%s" % (title, body)

        ok, reason = classify(title, body, currency=currency)
        if not ok:
            result["rejected"].append({"fb_id": fb_id, "url": url, "title": title,
                                       "reason": reason})
            print("    dropped: %s" % reason)
            _sleep(args.pause_min, args.pause_max)
            continue
        address = find_address(body) or find_address(blob)
        if not address:
            result["rejected"].append({"fb_id": fb_id, "url": url, "title": title,
                                       "reason": "no address in the body (the site's own "
                                                 "rule; it disqualifies a large share of "
                                                 "Facebook posts)"})
            print("    dropped: no address in the body")
            _sleep(args.pause_min, args.pause_max)
            continue
        prices = parse_prices(blob, currency)
        usd = parse_prices_usd(blob)
        if not prices and not usd:
            result["rejected"].append({"fb_id": fb_id, "url": url, "title": title,
                                       "reason": "no price anywhere in the body"})
            print("    dropped: no price in the body")
            _sleep(args.pause_min, args.pause_max)
            continue

        body_price = prices[0][0] if prices else None
        fb_price_text = meta.get("price_field") or ""
        if not fb_price_text:
            for t in leaves:
                if re.match(r"^[₫$₱][\d.,]+", _norm(t)):
                    fb_price_text = _norm(t)
                    break
        fb_price = parse_fb_price_field(fb_price_text)
        factor = round(body_price / float(fb_price), 2) if (fb_price and body_price) else None
        areas = parse_area(blob)
        days, raw, precision = pick_timestamp(leaves)
        seller = (data.get("sellers") or [{}])[0]

        cand = {
            "kind": "marketplace_item",
            "fb_id": fb_id, "url": url, "title": title, "city_key": city_key,
            "district": None, "district_hint_from_address": address,
            "fb_place_field": find_fb_place(page_text, leaves) or meta.get("place"),
            "district_warning": "Facebook's place field contradicted the address in the "
                                "body in the very first sample -- assign the district key "
                                "from the address, never from this field.",
            "currency": currency,
            "price": body_price, "price_snippet": prices[0][1] if prices else None,
            "price_candidates": [{"amount": v, "snippet": s} for v, s in prices],
            "usd_price_candidates": [{"usd": v, "snippet": s} for v, s in usd],
            "fb_price_field_text": fb_price_text or None,
            "fb_price_field_value": fb_price,
            "price_discrepancy_factor": factor,
            "area_m2": areas[0][0] if areas else None,
            "area_candidates": [{"m2": v, "snippet": s} for v, s in areas],
            "seller_name": seller.get("name"), "seller_url": seller.get("href"),
            "seller_kind_guess": guess_seller_kind(seller.get("name"), blob),
            "age_days": days, "age_raw": raw, "age_precision": precision,
            "age_bound_days": args.days,
            "age_note": (age_note(days, raw, precision) if days is not None else
                         "Facebook published no age on this item page (the newer "
                         "'Rentals' layout carries none at all). `age_days` is null on "
                         "purpose. The only thing known is that the feed was filtered to "
                         "the last %d days, so %d days is an UPPER BOUND, not a "
                         "publication date." % (args.days, args.days)),
            "body": body, "photos": [],
            "collected_at": datetime.now(timezone.utc).isoformat(),
            "notice_seed": notice_seed(days, precision, currency),
        }
        if not args.no_photos:
            urls = collect_photo_urls_mp(page, args.max_photos, args.gallery_clicks)
            cand["photos"] = save_photos(ctx, page, fb_id, urls)
            cand["photo_note"] = PHOTO_NOTE
            print("    %d photo(s), %d KB"
                  % (len(cand["photos"]), sum(p["bytes"] for p in cand["photos"]) // 1024))
        result["candidates"].append(cand)
        print("    kept: %s | %s | %s" % (title[:55],
                                          "{:,}".format(body_price) if body_price else "?",
                                          address[:40]))
        _sleep(args.pause_min, args.pause_max)
    return result


# ==========================================================================
# Run wrapper
# ==========================================================================

def run(args):
    from playwright.sync_api import sync_playwright
    started = datetime.now(timezone.utc)
    mode = "groups" if args.groups else "marketplace"
    city_key = args.city_key or CITY_SLUG_TO_KEY.get(args.city) or args.city
    out_path = args.out or os.path.join(
        HERE, "_fb_%s_%s_%s.json" % (mode, city_key, started.strftime("%Y%m%d_%H%M")))
    known = set() if args.no_site_dedupe else site_fb_ids()
    print("mode: %s   city key: %s   already on the site: %d Facebook ids"
          % (mode, city_key, len(known)))

    result = {
        "run": {
            "script": os.path.basename(__file__), "script_version": SCRIPT_VERSION,
            "mode": mode, "started": started.isoformat(),
            "city_slug": args.city, "city_key": city_key,
            "max_items": args.max_items, "photos": not args.no_photos,
            "read_only": True,
        },
        "candidates": [], "rejected": [], "errors": [],
    }
    with sync_playwright() as pw:
        ctx = open_context(pw, headless=args.headless, channel=args.channel or None)
        try:
            if not is_logged_in(ctx):
                raise SystemExit(
                    "not logged in: the profile at %s has no c_user cookie.\n"
                    "Run `python fb_collect.py --login` once, by hand." % PROFILE_DIR)
            page = ctx.pages[0] if ctx.pages else ctx.new_page()
            if args.groups:
                collect_groups(args, ctx, page, result, known)
            else:
                collect_marketplace(args, ctx, page, result, known)
        finally:
            try:
                ctx.close()
            except Exception:
                pass
    return finish(result, out_path, started)


def finish(result, out_path, started):
    now = datetime.now(timezone.utc)
    result["run"]["finished"] = now.isoformat()
    result["run"]["elapsed_s"] = round((now - started).total_seconds(), 1)
    cands = result["candidates"]
    result["stats"] = {
        "kept": len(cands), "rejected": len(result["rejected"]),
        "errors": len(result["errors"]),
        "with_photos": sum(1 for c in cands if c.get("photos")),
        "with_date": sum(1 for c in cands if c.get("age_days") is not None),
        "photo_bytes": sum(p["bytes"] for c in cands for p in c.get("photos", [])),
    }
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
    s = result["stats"]
    print("\n%d kept, %d rejected, %d errors, %d with photos (%d KB), %d with a real date"
          % (s["kept"], s["rejected"], s["errors"], s["with_photos"],
             s["photo_bytes"] // 1024, s["with_date"]))
    print("wrote %s" % out_path)
    if s["kept"] > s["with_date"]:
        print("NOTE: %d kept post(s) have age_days: null. Those must NOT be written into "
              "the dataset with an invented date." % (s["kept"] - s["with_date"]))
    return 0


def prune_photos(apply_it):
    """Delete photo directories for listings no longer on the site.

    purge_old_listings.py removes rows after 14 days; without this the pixels
    stay in the repo forever.
    """
    if not os.path.isdir(PHOTO_ROOT):
        print("no %s yet -- nothing to prune" % PHOTO_REL_ROOT)
        return 0
    keep = site_fb_ids()
    if not keep:
        print("refusing to prune: the site produced no Facebook ids at all (unbuilt page, "
              "or site_data failed). That would delete everything.")
        return 1
    total = 0
    for name in sorted(os.listdir(PHOTO_ROOT)):
        d = os.path.join(PHOTO_ROOT, name)
        if not os.path.isdir(d) or name in keep:
            continue
        size = sum(os.path.getsize(os.path.join(d, f)) for f in os.listdir(d))
        total += size
        print("%s %s (%d KB)" % ("deleting" if apply_it else "would delete",
                                 name, size // 1024))
        if apply_it:
            shutil.rmtree(d)
    print("%s %d KB" % ("freed" if apply_it else "would free", total // 1024))
    if not apply_it:
        print("(dry run -- add --apply to actually delete)")
    return 0


# ==========================================================================
# Selftest: the parsers, against the strings actually observed on 4 Sep 2026.
# No browser, no network, no Facebook contact.
# ==========================================================================

def selftest():
    fails = []

    def check(name, got, want):
        if got != want:
            fails.append("%s: got %r, want %r" % (name, got, want))

    # -- Marketplace price traps (measured, facebook_check_prompt.txt) --------
    check("13tr5", parse_prices("Giá 13tr5/tháng")[0][0], 13_500_000)
    check("4tr9", parse_prices("Phòng 30m2, 4tr9 và 5tr2")[0][0], 4_900_000)
    check("4tr9 count", len(parse_prices("Phòng 30m2, 4tr9 và 5tr2")), 2)
    check("13.5 trieu", parse_prices("cho thuê 13.5 triệu/tháng")[0][0], 13_500_000)
    check("grouped vnd", parse_prices("Giá thuê 4.900.000 đ/tháng")[0][0], 4_900_000)
    check("5500k", parse_prices("giá 5500k/tháng")[0][0], 5_500_000)
    check("phone-not-money", parse_prices("LH 0901.234.567"), [])
    check("deposit-skipped", [v for v, _ in parse_prices("Giá 8 triệu, cọc 16 triệu")],
          [8_000_000])
    check("electricity-skipped",
          [v for v, _ in parse_prices("Giá 6 triệu, tiền điện 4.000 đ/số")], [6_000_000])
    check("fb-13500", parse_fb_price_field("₫13,500"), 13500)
    check("fb-1.4M", parse_fb_price_field("₫1,400,000"), 1400000)
    check("fb-free", parse_fb_price_field("Free"), 0)
    check("fb-month", parse_fb_price_field("₫4,000,000 / Month"), 4000000)

    # -- Philippine group prices ---------------------------------------------
    check("php-grouped", parse_prices("For rent 12,000 monthly", "PHP")[0][0], 12000)
    check("php-symbol", parse_prices("Rent ₱15000/month", "PHP")[0][0], 15000)
    check("php-word", parse_prices("PHP 8500 per month", "PHP")[0][0], 8500)
    check("php-k", parse_prices("Rent is 12k a month", "PHP")[0][0], 12000)
    check("php-footwear-85", parse_prices("Brand new sandals PHP 85", "PHP"), [])
    check("php-deposit-skipped",
          [v for v, _ in parse_prices("Rent 9,000. Deposit 18,000 and advance 9,000", "PHP")],
          [9000])

    # -- sales, services, off-topic ------------------------------------------
    ok, _ = classify("Park 2ngủ 75m nhỉnh 7tỷ", "Cho thuê căn hộ Park, 75m2, nhỉnh 7 tỷ")
    check("sale-ty", ok, False)
    ok, _ = classify("Sơn nhà giá rẻ", "Dịch vụ sơn nhà giá rẻ, thuê thợ, gọi ngay")
    check("painting", ok, False)
    ok, _ = classify(None, "Brand new sandals, size 7-10, PHP 85 only, free shipping, COD",
                     currency="PHP")
    check("footwear", ok, False)
    ok, _ = classify(None, "Cần bán căn hộ 2 phòng ngủ, sổ hồng chính chủ")
    check("sale-cue", ok, False)
    ok, why = classify("Cho thuê chung cư mini tại 47 Nam Dư",
                       "Địa chỉ: 47 Nam Dư, Hoàng Mai, Hà Nội. Phòng 30m2, 4tr9/tháng")
    check("real-rental-vn", (ok, why), (True, None))
    ok, why = classify(None, "House for rent in Piapi, Dumaguete City. 2 bedrooms, "
                             "12,000 monthly. Located at 15 Hibbard Avenue.", currency="PHP")
    check("real-rental-ph", (ok, why), (True, None))
    ok, _ = classify(None, "This content isn't available right now")
    check("unavailable", ok, False)

    # -- the spam the coordinator saw: invisible joiners, then single letters --
    spam = "d͏ r͏ n͏ p͏ s͏ m͏ l͏ k͏ " \
           "j͏ h͏ g͏ f͏ d͏ s͏ a͏"
    cleaned = clean_text(spam)
    check("cgj-stripped", "͏" in cleaned, False)
    check("obfuscated-detected", looks_obfuscated(cleaned), True)
    ok, reason = classify(None, cleaned)
    check("obfuscated-rejected", ok, False)
    check("obfuscated-reason", "obfuscated" in (reason or ""), True)
    # Vietnamese diacritics must survive the same cleaning.
    check("vn-survives", clean_text("Cho thuê căn hộ ở Quận 7, đường Nguyễn Thị Thập"),
          "Cho thuê căn hộ ở Quận 7, đường Nguyễn Thị Thập")
    check("facebook-runs",
          clean_text("Facebook Facebook Facebook\nHouse for rent in Daro"),
          "House for rent in Daro")

    # -- addresses ------------------------------------------------------------
    body = ("🏡 Địa chỉ : 47 Nam Dư, Hoàng Mai, Hà Nội\n"
            "Phòng 30m2-35m2, 4tr9 và 5tr2, máy giặt chung, cửa sổ to")
    check("address-vn", find_address(body), "🏡 Địa chỉ : 47 Nam Dư, Hoàng Mai, Hà Nội")
    check("address-ph", find_address("2BR unit, 12k monthly\n"
                                     "Located at 15 Hibbard Avenue, Piapi, Dumaguete"),
          "Located at 15 Hibbard Avenue, Piapi, Dumaguete")
    check("address-brgy", find_address("Nice room\nBrgy. Taclobo near Silliman"),
          "Brgy. Taclobo near Silliman")
    check("no-address", find_address("Phòng đẹp, giá tốt, liên hệ ngay"), None)
    # A whole post on one line: the address must come back as its own sentence,
    # not as the entire ad.
    check("address-one-paragraph", find_address(
        "House for rent in Piapi, Dumaguete City. 2 bedrooms, 45 sqm, 12,000 monthly. "
        "Deposit 24,000 and advance 12,000. Located at 15 Hibbard Avenue, Piapi. "
        "Message me for viewing."),
        "Located at 15 Hibbard Avenue, Piapi.")
    check("fb-place", find_fb_place("Listed in Quận Đống Đa, Hà Nội\n", []),
          "Quận Đống Đa, Hà Nội")

    # -- areas ----------------------------------------------------------------
    check("area-range", [v for v, _ in parse_area("Phòng 30m2-35m2 full đồ")], [30.0, 35.0])
    check("area-wxh", parse_area("nhà 4x15m, 1 trệt 4 lầu")[0][0], 60.0)
    check("area-sqm", parse_area("Unit is 45 sqm with balcony")[0][0], 45.0)

    # -- dates: group posts carry them, the Marketplace Rentals layout does not
    today = datetime(2026, 9, 4).date()
    check("ts-3h", parse_timestamp("3h", today), (0, "3h", "relative-hours"))
    check("ts-2d", parse_timestamp("2d", today), (2, "2d", "relative-days"))
    check("ts-1w", parse_timestamp("1w", today), (7, "1w", "relative-weeks"))
    check("ts-yesterday", parse_timestamp("Yesterday at 5:03 PM", today)[0], 1)
    check("ts-abs", parse_timestamp("September 1 at 10:04 AM", today),
          (3, "September 1 at 10:04 AM", "absolute-date"))
    check("ts-abs-dmy", parse_timestamp("1 September at 10:04", today)[0], 3)
    check("ts-lastyear", parse_timestamp("December 30", today)[0], 248)
    check("ts-none", parse_timestamp("Rental Location", today), (None, None, None))
    check("ts-pick-none", pick_timestamp(["₫4,000,000 / Month", "Rental Location"]),
          (None, None, None))
    check("ts-note-null", "null on purpose" in age_note(None, None, None), True)
    check("ts-note-week", "7-13 days" in age_note(7, "1w", "relative-weeks"), True)

    # -- group card cleanup ---------------------------------------------------
    card = ("Maria Santos\n2d\n·\nHouse for rent in Piapi, Dumaguete\n"
            "2 bedrooms, 12,000 monthly\nLike\nComment\nShare\n8 comments")
    check("post-body", clean_post_body(card, "Maria Santos", "2d"),
          "House for rent in Piapi, Dumaguete\n2 bedrooms, 12,000 monthly")

    # -- Marketplace layouts, both of them ------------------------------------
    check("layout-new", extract_body(
        "₫4,000,000 / Month\nRental Location\nQuận 7, Hồ Chí Minh\nDescription\n"
        "Cho thuê căn hộ 40m2 tại 12 Nguyễn Văn Linh, Tân Hưng\nSeller information\nA"),
        "Cho thuê căn hộ 40m2 tại 12 Nguyễn Văn Linh, Tân Hưng")
    check("layout-old", extract_body(
        "₫13,500\n· In stock\nListed in Thủ Đức\nDetails\n"
        "Cho thuê studio 38m2 đường số 64, Thảo Điền, 13tr5/tháng\nSeller information\nB"),
        "Cho thuê studio 38m2 đường số 64, Thảo Điền, 13tr5/tháng")
    a = parse_aria("Cho thuê phòng trọ, ₫13,500, Thủ Đức, listing 2620808191683838")
    check("aria", (a.get("title"), a.get("price_field"), a.get("place")),
          ("Cho thuê phòng trọ", "₫13,500", "Thủ Đức"))

    # -- ids ------------------------------------------------------------------
    check("group-post-id",
          GROUP_POST_ID_RE.search(
              "https://www.facebook.com/groups/975470559939040/posts/2337289520423797"
          ).group(1), "2337289520423797")
    check("mp-item-id",
          MP_ITEM_ID_RE.search("/marketplace/item/2620808191683838/").group(1),
          "2620808191683838")

    # -- the read-only invariant is enforced, not merely documented ------------
    for bad in ("Send message", "Make offer", "Join group", "Like", "Comment", "Share"):
        try:
            _safe_click(None, None, bad)
            fails.append("_safe_click accepted %r" % bad)
        except RuntimeError:
            pass
    if not ALLOWED_CLICK_LABELS.match("See more"):
        fails.append("_safe_click would refuse 'See more'")

    # -- the photo pipeline, on a synthetic image -- no Facebook contact -------
    try:
        from PIL import Image
        src = Image.new("RGB", (2400, 1600))
        for x in range(0, 2400, 8):
            for y in range(0, 1600, 8):
                src.paste(((x * 7) % 256, (y * 11) % 256, (x + y) % 256), (x, y, x + 8, y + 8))
        buf = io.BytesIO()
        src.save(buf, "JPEG", quality=95)
        data, ext, w, h = downscale(buf.getvalue())
        if max(w, h) != 1200:
            fails.append("downscale: longest edge %d, want 1200" % max(w, h))
        if ext != "webp":
            fails.append("downscale: ext %s" % ext)
        if len(data) > 150_000:
            fails.append("downscale: %d bytes, want <=150000" % len(data))
        print("photo pipeline: 2400x1600 JPEG -> %dx%d %s, %d KB"
              % (w, h, ext, len(data) // 1024))
    except ImportError:
        fails.append("Pillow is not installed (pip install pillow)")

    # -- the group registry is well-formed ------------------------------------
    n = sum(len(v) for v in GROUPS.values())
    if n < 20:
        fails.append("GROUPS registry has only %d entries" % n)
    for city, gs in GROUPS.items():
        for g in gs:
            if not re.match(r"^[\w.]+$", g["id"]):
                fails.append("bad group id %r in %s" % (g["id"], city))
    print("group registry: %d groups across %d cities" % (n, len(GROUPS) - 1))

    if fails:
        print("\nSELFTEST FAILED:")
        for f in fails:
            print("  - %s" % f)
        return 1
    print("selftest: all parser, date, cleaning and photo checks passed")
    return 0


# ==========================================================================

def main(argv=None):
    p = argparse.ArgumentParser(
        description="Read-only Facebook rental collector: groups first, Marketplace "
                    "second. Own browser profile, schedulable.",
        epilog="Read facebook_check_prompt.txt before changing the parsing.")
    p.add_argument("--login", action="store_true",
                   help="open a visible browser so a human can log in once, then exit")
    p.add_argument("--selftest", action="store_true",
                   help="run the parser, date, cleaning and photo checks; no network")
    p.add_argument("--prune-photos", action="store_true",
                   help="list photo directories whose listing is gone from the site")
    p.add_argument("--apply", action="store_true", help="with --prune-photos: actually delete")

    p.add_argument("--groups", action="store_true", help="collect from Facebook groups (default)")
    p.add_argument("--marketplace", action="store_true", help="collect from Marketplace instead")
    p.add_argument("--group", action="append", default=None,
                   help="one group id or slug; repeatable. Overrides the city's list")
    p.add_argument("--max-groups", type=int, default=3,
                   help="groups per run (default 3 -- a whole city in one go is a lot "
                        "of Facebook traffic from one account)")
    p.add_argument("--chronological", dest="chronological", action="store_true", default=True,
                   help="ask the group feed for newest-first (default; UNVERIFIED param)")
    p.add_argument("--no-chronological", dest="chronological", action="store_false")
    p.add_argument("--open-permalinks", dest="open_permalinks", action="store_true", default=True,
                   help="open each surviving post's permalink for untruncated text and "
                        "better photos (default on)")
    p.add_argument("--no-permalinks", dest="open_permalinks", action="store_false")

    p.add_argument("--city", default="dumaguete",
                   help="city: a project city key (dumaguete, cebu, manila, ho-chi-minh...) "
                        "for --groups, or a Marketplace slug (hochiminhcity, hanoi...) "
                        "for --marketplace")
    p.add_argument("--city-key", default=None, help="this project's city key, explicitly")
    p.add_argument("--category", default="propertyrentals", choices=CATEGORIES,
                   help="Marketplace only")
    p.add_argument("--days", type=int, default=7,
                   help="Marketplace daysSinceListed filter; this is the age UPPER BOUND")
    p.add_argument("--radius", type=int, default=30, help="Marketplace radius, km")
    p.add_argument("--no-c2c", action="store_true",
                   help="Marketplace: drop isC2CListingOnly=1 (the individuals-only "
                        "switch, which thins agency reposts but does not remove them)")
    p.add_argument("--feed-url", default=None, help="Marketplace: use this URL verbatim")
    p.add_argument("--feed-only", action="store_true",
                   help="Marketplace: harvest the feed and stop")

    p.add_argument("--max-items", type=int, default=20,
                   help="hard cap on posts/items kept per run (default 20, ceiling 60)")
    p.add_argument("--max-scrolls", type=int, default=12)
    p.add_argument("--pause-min", type=float, default=4.0,
                   help="seconds between page loads, lower bound (default 4)")
    p.add_argument("--pause-max", type=float, default=9.0)
    p.add_argument("--no-photos", action="store_true")
    p.add_argument("--max-photos", type=int, default=6)
    p.add_argument("--gallery-clicks", type=int, default=6,
                   help="Marketplace: how many times the photo carousel may be stepped")
    p.add_argument("--no-site-dedupe", action="store_true")
    p.add_argument("--out", default=None, help="candidates JSON path")
    p.add_argument("--headless", action="store_true",
                   help="no window. Headless is more likely to be challenged by Facebook; "
                        "prefer a visible window when you can.")
    p.add_argument("--channel", default="chrome",
                   help="browser channel ('chrome', 'msedge', or '' for bundled Chromium)")
    args = p.parse_args(argv)

    if args.selftest:
        return selftest()
    if args.prune_photos:
        return prune_photos(args.apply)
    if args.login:
        return do_login(args.headless, args.channel or None)

    args.groups = not args.marketplace
    if args.max_items > 60:
        raise SystemExit("--max-items above 60 is not allowed: a big sweep is exactly what "
                         "gets a personal Facebook account checkpointed. Run several small "
                         "passes on different days instead.")
    if args.pause_min < 2.0:
        raise SystemExit("--pause-min below 2 s is not allowed (human pace is the whole "
                         "defence this script has).")
    if args.groups:
        key = args.city_key or CITY_SLUG_TO_KEY.get(args.city) or args.city
        if not args.group and key not in GROUPS:
            raise SystemExit("no groups registered for %r. Known city keys: %s\n"
                             "Or pass --group <id> explicitly."
                             % (key, ", ".join(sorted(k for k in GROUPS if k != "_unassigned"))))
    elif not args.city_key and args.city not in CITY_SLUG_TO_KEY:
        raise SystemExit("unknown Marketplace city slug %r -- pass --city-key too" % args.city)
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
