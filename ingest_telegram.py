# -*- coding: utf-8 -*-
"""
Заведение телеграм-постов, написанных по шаблону агентства, -- без человека.

ЗАЧЕМ. fetch_telegram_listings.py только собирает кандидатов, и до 12 сентября
2026 каждого из них заводила сессия на ПК владельца: ПК выключен -- Telegram на
сайте не пополняется. Но большую часть постов в Дананге и Нячанге пишут шесть
агентств, и каждое -- по своему шаблону: адрес, спальни, площадь и цена стоят в
одних и тех же строках. Такие посты программа заводит сама; всё, что в шаблон
не укладывается, остаётся кандидатом для ручного разбора, как раньше.

ЧТО ЗАВОДИТСЯ. Пост совпал с шаблоном (TEMPLATES) целиком, свежее MAX_AGE_DAYS
дней, есть фото, цена одна и в пределах PRICE_LIMITS, район определён без
противоречий, и пост не повторяет уже заведённое. Не выполнено одно -- пропуск,
причина в отчёте и в шапке партии.

РАЙОН -- ТОЛЬКО ИЗ ПРОВЕРЯЕМОГО:
  * пост называет район, который есть на сайте (или прежний квартал из
    WARD_ALIASES, чей нынешний район установлен по адресам OSM);
  * Дананг, улица: её отрезки из OpenStreetMap (osm_streets_da-nang.json) лежат
    в границах наших районов -- тех же, что на карте (leaflet_ward_boundaries.json);
  * жилой комплекс или посёлок: не меньше MIN_PRECEDENT строк сайта с этим
    названием, и все в одном районе.
Источники назвали разное -- пропуск. Ни один не сработал -- пропуск.

ДАНАНГ: СЛОВО ПОСТА -- ПРЕЖНИЙ РАЙОН. Агентства подписывают адрес районами
города до реформы 2025 года («Son Tra», «Hai Chau»), и каждый из них у нас
распался на два. Поэтому это слово -- не ответ, а ограничение: ответ обязан
быть одним из «наследников» (OLD_DISTRICTS). Улица через несколько районов:
район с именем из поста, если на него приходится не меньше четверти отрезков;
иначе район большинства, если у него не меньше двух третей; иначе пропуск.
Правило выведено на ручных решениях 11 сентября; на исходных текстах всех
заведённых вручную телеграм-строк оно даёт те же районы или пропуск, но не
другой район.

Посты пишут улицы без диакритики, а в OSM они с ней. Без диакритики разные
улицы иногда сливаются: «Doan Khue» -- это и Đoàn Khuê (Ngũ Hành Sơn), и
Doãn Khuê (Hòa Cường). Если такие двойники лежат в разных районах, улица
считается неизвестной.

ПОВТОРЫ. Ссылка на пост уже на сайте (в том числе в alsoOn); тот же номер
каталога агентства или тот же текст, что у заведённого (telegram_ingest_state.json);
та же улица или комплекс, район, тип и спальни, что у строки сайта, площадь не
расходится, а цена -- в пределах REPOST_PRICE_TOL. Квартира в комплексе, у
которого на сайте уже есть строки, без площади, корпуса и номера каталога не
заводится вовсе: агентства перевыкладывают одни и те же квартиры, и отличить
её не по чему. Перепост того же текста в другом канале, собранный тем же
прогоном, не заводится отдельно, а записывается в alsoOn.

ЗАПУСК
    python ingest_telegram.py                  отчёт: что завелось бы и почему нет
    python ingest_telegram.py --write          записать партию new_listingsNNN.py
    python ingest_telegram.py --write --insert записать и вставить (так зовёт run_pipeline.py)
    python ingest_telegram.py --refresh-osm    обновить выгрузку улиц Дананга
"""
import argparse
import ast
import collections
import datetime
import functools
import glob
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

import fetch_telegram_listings as ftl

HERE = os.path.dirname(os.path.abspath(__file__))
CANDIDATES = "telegram_candidates.json"
STATE = "telegram_ingest_state.json"
OSM_CACHE = "osm_streets_da-nang.json"
# Города, где район можно ставить по улице: выгрузка улиц есть, и границы
# районов карты совпадают с районами сайта. Хошимина здесь нет намеренно --
# в нём улицы нумерованные и одноимённые в разных кварталах.
OSM_STREET_CITIES = ("da-nang", "ha-noi")
BOUNDS = "leaflet_ward_boundaries.json"

# Дананг в границах города до слияния провинций: без Хойана и Тамки, где после
# 2025 года нашлись бы улицы с теми же именами.
OSM_BBOX = (15.90, 108.00, 16.25, 108.35)
OVERPASS = "https://overpass-api.de/api/interpreter"
UA = "RentSearcher/1.0 (+https://tottorisun.github.io/RentSearcherViet/)"

VN_TZ = datetime.timezone(datetime.timedelta(hours=7))
MAX_AGE_DAYS = 13        # purge_old_listings.py снимает строки старше 14 дней
MAX_PHOTOS = 6
MIN_PRECEDENT = 2
PRICE_LIMITS = {"VND": (1_500_000, 500_000_000), "USD": (100, 20_000)}
SEED_FETCHES = 60        # страниц t.me за прогон на сверку заведённых раньше
TYPES = ("Комната", "Студия", "Квартира", "Дом")
OUTSIDE = "вне"

# Прежние районы Дананга, которыми агентства подписывают адрес ->
# (район сайта с тем же именем, районы сайта, на которые прежний распался).
OLD_DISTRICTS = {
    "da-nang": {
        "son tra": ("st", ("st", "ah")),
        "hai chau": ("hc", ("hc", "hcg")),
        "lien chieu": ("lc", ("lc", "hk")),
        "thanh khe": ("tk", ("tk", "ak")),
        "cam le": ("cl2", ("cl2", "hx")),
        "ngu hanh son": ("ns", ("ns",)),
    },
    "nha-trang": {},
}
# Прежние кварталы, которых нет среди районов сайта, но чей нынешний район
# установлен по адресной иерархии OSM (10-11 сентября 2026).
WARD_ALIASES = {
    "da-nang": {"my an": "ns", "khue my": "ns", "hoa hai": "ns", "phuoc my": "ah"},
    "nha-trang": {"vinh hoa": "btr"},
}
# Район, названный как сам город, встречается в любом тексте про этот город --
# совпадением с районом он не считается.
# Район, названный как сам город, встречается в любом тексте про этот город --
# совпадением с районом он не считается. Ловушка не выдумана: в Нячанге,
# Куинёне, Хойане, Вунгтау и Буонметхуоте реформа 2025 года создала район с
# именем города («Phường Nha Trang», «Phường Quy Nhơn»), и слово из любого
# объявления попадало бы в него.
CITY_WORDS = {
    "da-nang": {"da nang", "danang"},
    "nha-trang": {"nha trang", "nhatrang"},
    "ho-chi-minh": {"ho chi minh", "hochiminh", "sai gon", "saigon", "tphcm", "hcm"},
    "ha-noi": {"ha noi", "hanoi"},
    "hai-phong": {"hai phong", "haiphong"},
    "can-tho": {"can tho", "cantho"},
    "hue": {"hue", "thua thien hue"},
    "buon-ma-thuot": {"buon ma thuot", "bmt", "dak lak", "daklak"},
    "quy-nhon": {"quy nhon", "quynhon"},
    "hoi-an": {"hoi an", "hoian"},
    "vung-tau": {"vung tau", "vungtau"},
    "da-lat": {"da lat", "dalat"},
    "phu-quoc": {"phu quoc", "phuquoc"},
    "phan-thiet": {"phan thiet", "mui ne", "muine"},
    "binh-duong": {"binh duong", "binhduong"},
    "cebu": {"cebu", "cebu city"},
    "manila": {"manila", "metro manila", "ncr"},
    "dumaguete": {"dumaguete", "dumaguete city", "negros oriental"},
}
# Места, чей район установлен по источнику, а не по прецеденту сайта:
# Nominatim назвал объект (искомое имя стоит в его display_name), а точка ответа
# попала в границы района на нашей карте. Проверено 12 сентября 2026. Прецедент
# живёт лишь пока строки не сняты чисткой по возрасту -- в тот же день на глазах
# рассыпался прецедент Mường Thanh Viễn Triều, когда сняли единственную строку;
# таблица от этого не зависит.
#
# Сюда НЕ вошли: Champa Island (OSM относит точку к Bắc Nha Trang, наши границы
# -- к Tây Nha Trang, а посты пишут «центр»: три ответа, ни одного совпадения);
# Panorama и Star City (источник даёт только укрупнённый nt, а строки сайта
# стоят в прежних lt/ph2 -- прежний квартал OSM уже не различает); Vega City,
# Maple, An Viên, Mỹ Gia (источник молчит или спорит с существующей строкой).
PLACE_WARDS = {
    "nha-trang": {
        # Oceanus держится и на прецеденте (14 строк, все vp), но прецедент живёт
        # лишь пока строки не сняты чисткой; в OSM это Muong Thanh Oceanus Apartment.
        "oceanus": "vp",
        "океанус": "vp",
        # Mỹ Gia нашёлся только запросом с ограничением по карте Нячанга: без
        # него Nominatim отдавал ресторан в Хошимине. Четыре объекта района Mỹ
        # Gia -- парк, два поля и ресторан -- все в ntr. Раскол ntr/vt на сайте
        # даёт единственная негеокодированная строка 2000498.
        "my gia": "ntr",
        "muong thanh vien trieu": "vp",
        "napoleon castle": "vp",
        "napoleon": "vp",
        "hon chong": "vp",
        "hon xen": "vh",
        "scenia bay": "btr",     # снимает раскол vh/vp: обе внутри укрупнённого btr
        "ba lang": "btr",
        "ana marina": "btr",
        "po nagar": "btr",
        "cho dam": "nt",
        "ct2 vcn phuoc hai": "ph",
    },
}

# Комплексы, которые агентства пишут по-русски, -> латинское имя (оно же в descEn).
COMPLEX_LATIN = {"океанус": "Oceanus"}

NOTICE_RU = ("Описание собрано программой из полей телеграм-поста агентства — тип, спальни, санузлы, "
             "площадь, адрес и цена; рекламный текст не пересказан. Ссылка ведёт на сам пост, дата "
             "размещения взята из него. Фотографии из того же поста и лежат на серверах Telegram. Цену "
             "и условия подтверждайте у автора объявления.")
NOTICE_EN = ("This description was assembled by a program from the fields of an agency's Telegram post — "
             "type, bedrooms, bathrooms, size, address and price; the marketing text is not retold. The "
             "link points at the post itself and the posting date is taken from it. The photos come from "
             "the same post and are hosted by Telegram. Confirm the price and terms with the poster.")
USD_RU = " Цена в объявлении названа только в долларах и так здесь и указана."
USD_EN = " The ad quotes the rent in US dollars only, and so does this listing."
HOW_RU = {
    "moved": (" Район определён по улице: пост называет прежний район города, а после реформы 2025 года "
              "улица лежит в районе, указанном здесь."),
    "street": " Район определён по улице и границам районов на карте.",
    "precedent": (" Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят "
                  "в этом районе."),
}
HOW_EN = {
    "moved": (" The district comes from the street: the post names the city's former district, and since "
              "the 2025 reform the street lies in the district shown here."),
    "street": " The district comes from the street and the district borders on the map.",
    "precedent": (" The district comes from the residential complex: every listing on the site from this "
                  "complex is in this district."),
}


class Skip(Exception):
    """Пост по шаблону, но заводить его нельзя; текст -- причина для отчёта."""


# ------------------------------------------------------------------ текст --

def nfc(s):
    return unicodedata.normalize("NFC", s or "")


def fold(s):
    return ftl.fold(nfc(s)).lower()


def words(s):
    """Сравнимая форма: без диакритики, нижний регистр, только буквы и цифры."""
    return re.sub(r"[^a-z0-9а-я]+", " ", fold(s)).strip()


def has_words(hay, needle):
    return bool(needle) and (" %s " % needle) in (" %s " % hay)


def lines(text):
    return [ln.strip() for ln in nfc(text).split("\n")]


def first_line(text):
    return next((ln for ln in lines(text) if ln), "")


def first_of(fn, items):
    return next((v for v in map(fn, items) if v is not None), None)


def ru_plural(n, one, few, many):
    a = abs(n)
    if a % 10 == 1 and a % 100 != 11:
        return "%d %s" % (n, one)
    if 2 <= a % 10 <= 4 and not 12 <= a % 100 <= 14:
        return "%d %s" % (n, few)
    return "%d %s" % (n, many)


_NUM = r"(\d+|од\w*|дв\w*|тр\w*|четыр\w*|пят\w*|one|two|three|four|five)"
_NUMS = (("од", 1), ("one", 1), ("дв", 2), ("two", 2), ("тр", 3), ("three", 3),
         ("четыр", 4), ("four", 4), ("пят", 5), ("five", 5))


def to_int(tok):
    t = fold(tok)
    if t.isdigit():
        return int(t)
    return next((n for pre, n in _NUMS if t.startswith(pre)), None)


def beds_in(s):
    m = re.search(_NUM + r"[\s_-]*(?:отдельн\w*\s+)?(?:спал\w*|спален|bed(?:room)?s?\b|br\b)", fold(s))
    return to_int(m.group(1)) if m else None


def baths_in(s):
    m = re.search(r"(\d+)\s*(?:wc\b|санузл\w*|сан\.?\s*узл\w*|ванн\w*|bath(?:room)?s?\b)", fold(s))
    return int(m.group(1)) if m else None


def area_in(s):
    m = re.search(r"(\d{2,4}(?:[.,]\d{1,2})?)\s*(?:m²|м²|m2|м2|sqm|кв\.?\s*м)", fold(s))
    if not m:
        return None
    v = float(m.group(1).replace(",", "."))
    return int(round(v)) if 10 <= v <= 2000 else None


def money(s):
    """(сумма, валюта) из ОДНОЙ строки цены, иначе None. Диапазон и «от» -- None:
    какую из двух цен ставить, решает человек, а не программа."""
    f = fold(s)
    if re.search(r"\bот\b|\bfrom\b|\bдо\b|\d\s*[-–—~]\s*\d", f):
        return None
    m = re.search(r"(\d{1,3}(?:[.,\s]\d{3}){1,3})\s*(?:vnd|₫|донг\w*|d(?![a-z]))", f)
    if m:
        return int(re.sub(r"\D", "", m.group(1))), "VND"
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:млн|mln|million|mil|trieu|tr)(?![a-z])", f)
    if m:
        return int(round(float(m.group(1).replace(",", ".")) * 1_000_000)), "VND"
    # Слева от числа не должно быть цифры или разделителя: без этого «1.500$»
    # читалось как 500 -- цена втрое ниже настоящей, и в разумные пределы она
    # укладывается, то есть ошибка прошла бы молча.
    m = (re.search(r"(?<![\d.,])(\d{1,3}(?:[.,\s]\d{3})+|\d{2,5})\s*(?:\$|usd)", f)
         or re.search(r"\$\s*(\d{1,3}(?:[.,\s]\d{3})+|\d{2,5})(?![\d.,])", f))
    if m:
        return int(re.sub(r"\D", "", m.group(1))), "USD"
    return None


def one_price(price_lines, label):
    vals = {money(ln) for ln in price_lines} - {None}
    if not vals:
        raise Skip("%s: цены нет или она не читается (диапазон, «от»)" % label)
    if len(vals) > 1:
        raise Skip("%s: в посте разные цены: %s" % (label, ", ".join("%s %s" % v for v in sorted(vals))))
    price, cur = vals.pop()
    lo, hi = PRICE_LIMITS[cur]
    if not lo <= price <= hi:
        raise Skip("%s: цена %s %s вне разумных пределов" % (label, price, cur))
    return price, cur


def term_months(s):
    f = fold(s or "")
    m = re.search(r"(\d+)\s*[-–]\s*\d+\s*(?:мес|month)", f)
    if m:
        return int(m.group(1))
    m = re.search(r"(?:от|from|>|min\w*)\s*:?\s*(\d+)?\s*(мес\w*|months?|год\w*|years?|лет)", f)
    if m:
        n = int(m.group(1)) if m.group(1) else 1
        return n * 12 if m.group(2).startswith(("год", "year", "лет")) else n
    m = re.search(r"(\d+)\s*(?:мес\w*|months?)", f)
    return int(m.group(1)) if m else None


def field(label, text):
    """Значение поля «Метка: значение» -- с эмодзи-номером (0️⃣) перед меткой или без."""
    m = re.search(r"^.{0,6}?\b%s\b\s*:?\s*(.*)$" % label, nfc(text), re.I | re.M)
    return m.group(1).strip() if m else None


def section(text, header_rx, bullets=True):
    """Строки раздела после заголовка -- до пустой строки (или до не-пункта)."""
    ls = lines(text)
    for i, ln in enumerate(ls):
        if re.search(header_rx, ln, re.I):
            out = []
            for s in ls[i + 1:]:
                if not s:
                    if out:
                        break
                    continue
                if bullets:
                    if not s.startswith("•"):
                        break
                    s = s[1:].strip()
                out.append(s)
            return out
    return []


def kind_of(title):
    """Тип по заголовку: (тип, вилла ли)."""
    f = fold(title)
    if "студи" in f or "studio" in f:
        return "Студия", False
    if re.search(r"квартир|апартамент|apartment|\bflat\b", f):
        return "Квартира", False
    if re.search(r"вилл|villa", f):
        return "Дом", True
    if re.search(r"\bдом|house|таунхаус", f):
        return "Дом", False
    return None, False


def new_parsed(template, city):
    return {"template": template, "city": city, "type": None, "villa": False, "floors": None,
            "beds": None, "baths": None, "area": None, "price": None, "cur": None, "term": None,
            "address": None, "complexes": [], "block": None, "ward_text": "", "cat": None}


# --------------------------------------------------------------- шаблоны --
# Каждый разборщик: None -- пост не его шаблона; Skip -- его, но с изъяном;
# иначе -- словарь полей (new_parsed).

def parse_vne(text):
    """VNE Property: Danang_House и vietnam_nedvijimost (один и тот же пост),
    дома и виллы; квартиры -- с подписью их же Danang_Apartments."""
    if not re.search(r"t\.me/Danang_(?:House|Apartments)\b", text, re.I):
        return None
    p = new_parsed("VNE Property", "da-nang")
    if re.search(r"#\s*(?:rented|sold)\b|\bđã (?:cho )?thuê\b", nfc(text), re.I):
        raise Skip("VNE: пост о сданном объекте")
    head = re.search(r"^\W*(house|villa|townhouse)\s*(\d+)?\s*floors?\s*:\s*(.+)$", text, re.I | re.M)
    if head:
        spec = head.group(3)
        p["type"], p["villa"] = "Дом", head.group(1).lower() == "villa"
        p["floors"] = int(head.group(2)) if head.group(2) else None
    elif re.search(r"apartment for rent|t\.me/Danang_Apartments", text, re.I):
        m = re.search(r"^\W*(?:\d+\s*bed(?:room)?s?|studio)\b.*$", text, re.I | re.M)
        if not m:
            raise Skip("VNE: у квартиры нет строки со спальнями")
        spec = m.group(0)
        p["type"] = "Студия" if "studio" in fold(spec) else "Квартира"
    else:
        raise Skip("VNE: тип не распознан (не дом, не вилла, не квартира)")
    p["beds"], p["baths"], p["area"] = beds_in(spec), baths_in(spec), area_in(spec)
    addr = re.search(r"^\W*(?:address|location)\s*:\s*(.+)$", text, re.I | re.M)
    if not addr:
        raise Skip("VNE: нет адреса")
    p["address"] = addr.group(1).strip()
    p["price"], p["cur"] = one_price([ln for ln in lines(text) if "💵" in ln], "VNE")
    term = re.search(r"^\W*contract\s*:\s*(.+)$", text, re.I | re.M)
    p["term"] = term_months(term.group(1)) if term else None
    return p


def parse_minhouse(text):
    """Minhouse, канал DaNangRentAFlat: пронумерованные поля 0️⃣-🔟."""
    if field("square meters", text) is None or field("price for 1 month", text) is None:
        return None
    p = new_parsed("Minhouse", "da-nang")
    title = first_line(text)
    kind = words(field("type", text) or "")
    rooms = field("rooms", text) or ""
    if "studio" in words(rooms) or "studio" in kind:
        p["type"], p["beds"] = "Студия", 0
    elif re.search(r"apartment|flat", kind):
        p["type"] = "Квартира"
    elif re.search(r"house|villa", kind):
        p["type"], p["villa"] = "Дом", "villa" in kind
    else:
        raise Skip("Minhouse: тип «%s» не жилой или не распознан" % kind)
    if p["beds"] is None:
        p["beds"] = beds_in(rooms) if beds_in(rooms) is not None else beds_in(title)
    sq = field("square meters", text) or ""
    p["area"] = area_in(sq)
    if p["area"] is None:
        m = re.match(r"\D*(\d{2,4})\b", sq)
        p["area"] = int(m.group(1)) if m and 10 <= int(m.group(1)) <= 2000 else None
    p["address"] = field("address", text)
    if not p["address"]:
        raise Skip("Minhouse: нет адреса")
    p["price"], p["cur"] = one_price([field("price for 1 month", text)], "Minhouse")
    p["term"] = term_months(field("minimum rental period", text))
    p["ward_text"] = title
    m = re.search(r"[-–—]\s*([A-Z]\d{3,4})\s*$", title)
    p["cat"] = "minhouse:" + m.group(1) if m else None
    return p


def parse_sunset(text):
    """Sunset Group, канал Arenda_Nyachang_Zhilye: номер каталога, ЖК, цена в долларах."""
    m = re.search(r"\(\s*ID\s*([A-ZА-Я]\d+)\s*\)", text)
    if not m or not re.search(r"^ЖК\s+\S", text, re.M):
        return None
    p = new_parsed("Sunset Group", "nha-trang")
    title = text[: m.start()]
    p["cat"] = "sunset:" + m.group(1).upper().replace("А", "A")
    p["type"], p["villa"] = kind_of(title)
    if not p["type"]:
        raise Skip("Sunset: тип не распознан")
    specs = [ln for ln in lines(text) if ln.startswith("🔸")]
    if p["type"] == "Студия":
        p["beds"] = 0
    else:
        p["beds"] = beds_in(title) if beds_in(title) is not None else first_of(beds_in, specs)
    p["baths"] = first_of(baths_in, specs)
    p["area"] = first_of(area_in, specs)
    p["complexes"] = [re.search(r"^ЖК\s+(.+)$", text, re.M).group(1).strip()]
    p["ward_text"] = " | ".join([title] + [ln for ln in lines(text) if re.match(r"(?:Район|ЖК)\b", ln)])
    p["price"], p["cur"] = one_price([ln for ln in lines(text)
                                      if ln.startswith("✅") and re.search(r"в месяц", ln, re.I)], "Sunset")
    p["term"] = first_of(term_months, [ln for ln in lines(text) if re.search(r"аренда от", ln, re.I)])
    return p


def _location_segments(segs):
    """Отбросить «рядом с ...», «≈ N минут» и «Север/Центр Нячанга»: это не адрес."""
    out = []
    for s in segs:
        s = s.strip()
        fs = fold(s)
        if not s or re.match(r"(?:≈|~|рядом|near)", fs) or "нячанг" in fs:
            continue
        out.append(s)
    return out


def _complex_of(seg, p):
    m = re.match(r"(?:ЖК|жк)\s+(.+?)(?:,\s*корпус\s+(\S+))?$", seg)
    if not m:
        return None
    if m.group(2):
        p["block"] = m.group(2)
    return m.group(1).strip()


def parse_anhome(text):
    """AN-HOME, канал nyachang_arenda: разделы «Локация», «О квартире», «Условия аренды»."""
    if not first_line(text).upper().startswith("AN-HOME"):
        return None
    p = new_parsed("AN-HOME", "nha-trang")
    title = next((ln for ln in lines(text) if ln.startswith("🌿")), "")
    loc = section(text, r"^📍\s*Локация")
    about = section(text, r"^🟢\s*О\s")
    cond = section(text, r"^🟡\s*Условия")
    if not title or not loc or not cond:
        raise Skip("AN-HOME: нет заголовка, локации или условий")
    p["type"], p["villa"] = kind_of(title)
    if not p["type"]:
        raise Skip("AN-HOME: тип не распознан")
    if p["type"] == "Студия":
        p["beds"] = 0
    else:
        p["beds"] = first_of(beds_in, about)
        if p["beds"] is None:
            p["beds"] = beds_in(title)
    p["baths"] = first_of(baths_in, about)
    p["area"] = first_of(area_in, [a for a in about if not re.search(r"общ|участ|земл", fold(a))])
    p["price"], p["cur"] = one_price([c for c in cond if fold(c).startswith("цена")], "AN-HOME")
    p["term"] = first_of(term_months, [c for c in cond if fold(c).startswith("контракт")])
    kept = _location_segments(loc)
    p["complexes"] = [c for c in (_complex_of(s, p) for s in kept) if c]
    p["ward_text"] = " | ".join(kept)
    return p


def parse_ruzik(text):
    """Nhatranghomes: «🔑 тип | комплекс» и «📍 часть города | квартал | ЖК»."""
    ls = lines(text)
    title = next((ln for ln in ls if ln.startswith("🔑")), None)
    loc = next((ln for ln in ls if ln.startswith("📍") and "|" in ln), None)
    if not title or not loc:
        return None
    p = new_parsed("Nhatranghomes", "nha-trang")
    tsegs = [s.strip() for s in title.lstrip("🔑").split("|")]
    p["type"], p["villa"] = kind_of(tsegs[0])
    if not p["type"]:
        raise Skip("Nhatranghomes: тип не распознан")
    about = section(text, r"^🏡\s*О\s", bullets=False)
    cond = section(text, r"^✨\s*Условия", bullets=False)
    if p["type"] == "Студия":
        p["beds"] = 0
    else:
        p["beds"] = first_of(beds_in, about)
        if p["beds"] is None:
            p["beds"] = beds_in(tsegs[0])
    p["baths"] = first_of(baths_in, about)
    p["area"] = first_of(area_in, [a for a in about if not re.search(r"общ|участ|земл", fold(a))])
    p["price"], p["cur"] = one_price([ln for ln in ls if ln.startswith("💵")], "Nhatranghomes")
    p["term"] = first_of(term_months, [c for c in cond if fold(c).startswith("контракт")])
    kept = _location_segments(loc.lstrip("📍").split("|") + tsegs[1:])
    names = []
    for s in kept:
        name = _complex_of(s, p) or s
        if words(name) not in {words(n) for n in names}:
            names.append(name)
    p["complexes"] = names
    p["ward_text"] = " | ".join(kept)
    return p


def parse_vietlife(text):
    """Viet Life, канал Viet_life_niachang (их перепосты -- и в nyachang_arenda):
    поля в заголовке через «|»."""
    if not re.search(r"viet[_ ]?life", text, re.I):
        return None
    p = new_parsed("Viet Life", "nha-trang")
    title = first_line(text)
    segs = [s.strip() for s in re.sub(r"^\W+", "", title).split("|")]
    if len(segs) < 3:
        raise Skip("Viet Life: в заголовке нет полей через «|»")
    m = re.match(r"аренда\s+(квартир|студи|дом|вилл)\w*", fold(segs[0]))
    if m:
        name, fields = segs[1], segs[2:]
        p["type"], p["villa"] = kind_of(m.group(0))
    else:
        name, fields = segs[0], segs[1:]
        p["type"], p["villa"] = ("Студия", False) if "студи" in fold(title) else ("Квартира", False)
    p["complexes"] = [name]
    joined = " | ".join(fields)
    body = lines(text)
    if p["type"] == "Студия":
        p["beds"] = 0
    else:
        p["beds"] = beds_in(joined)
        if p["beds"] is None:
            p["beds"] = first_of(beds_in, [ln for ln in body if ln.startswith(("—", "🔹", "-"))])
    p["baths"] = first_of(baths_in, [ln for ln in body if ln.startswith(("—", "🔹", "-"))])
    p["area"] = area_in(joined)
    if p["area"] is None:
        p["area"] = first_of(area_in, [ln for ln in body if ln.startswith(("📐", "🔹"))])
    p["price"], p["cur"] = one_price([f for f in fields if money(f)] +
                                     [ln for ln in body if ln.startswith("💰")], "Viet Life")
    p["term"] = first_of(term_months, [ln for ln in body if "контракт" in fold(ln)])
    p["ward_text"] = " | ".join([title] + [ln for ln in body
                                           if ln.startswith(("📍", "🏡", "🏝", "🏙")) or "район" in fold(ln)])
    return p


TEMPLATES = (parse_vne, parse_minhouse, parse_sunset, parse_anhome, parse_ruzik, parse_vietlife)


def parse_post(text):
    for fn in TEMPLATES:
        p = fn(text)
        if p is not None:
            return p
    return None


# ------------------------------------------------------ улицы и границы --

STREET_PREFIX = re.compile(r"^(?:đường|phố)\s+", re.I)


def refresh_osm(path=OSM_CACHE):
    """Одна выгрузка всех именованных улиц и местностей Дананга. Посты пишут
    улицу без диакритики, Overpass так искать не умеет -- поэтому сопоставление
    идёт локально, по этой выгрузке, а не запросом на каждую улицу."""
    bb = "%s,%s,%s,%s" % OSM_BBOX
    q = ('[out:json][timeout:180];(way["highway"]["name"](%s);nwr["place"]["name"](%s);'
         'nwr["landuse"="residential"]["name"](%s););out center tags;') % (bb, bb, bb)
    req = urllib.request.Request(OVERPASS, data=urllib.parse.urlencode({"data": q}).encode(),
                                 headers={"User-Agent": UA})
    raw, last = None, None
    for attempt in range(3):
        try:
            raw = urllib.request.urlopen(req, timeout=240).read()
            break
        except Exception as e:
            last = e
            time.sleep(20 * (attempt + 1))
    if raw is None:
        raise SystemExit("Overpass не ответил: %s" % last)
    names = collections.defaultdict(list)
    for el in json.loads(raw)["elements"]:
        c = el.get("center") or ({"lat": el["lat"], "lon": el["lon"]} if "lat" in el else None)
        if c and el.get("tags", {}).get("name"):
            names[nfc(el["tags"]["name"])].append([round(c["lat"], 5), round(c["lon"], 5)])
    out = {"generated": datetime.date.today().isoformat(), "bbox": OSM_BBOX,
           "source": "© OpenStreetMap contributors, ODbL; Overpass API",
           "names": {k: sorted(v) for k, v in sorted(names.items())}}
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, path)
    return len(names)


def load_osm(path=None):
    try:
        data = json.load(open(path or OSM_CACHE, encoding="utf-8"))
    except FileNotFoundError:
        return {}
    idx = collections.defaultdict(dict)
    for name, pts in data["names"].items():
        clean = STREET_PREFIX.sub("", nfc(name)).strip()
        idx[words(clean)].setdefault(clean, []).extend(pts)
    return idx


def inside(lat, lon, ring):
    ins, j = False, len(ring) - 1
    for i in range(len(ring)):
        yi, xi = ring[i]
        yj, xj = ring[j]
        if (xi > lon) != (xj > lon) and lat < (yj - yi) * (lon - xi) / ((xj - xi) or 1e-12) + yi:
            ins = not ins
        j = i
    return ins


def clean_place(s):
    s = nfc(s).strip()
    s = re.sub(r"^(?:(?:số|so|no\.?|kiệt|kiet|k|hẻm|hem|ngõ|ngo)\s*)?\d+[\w/.\-]*\s+", "", s, flags=re.I)
    s = re.sub(r"\s+(?:street|st\.?|road|rd\.?|area)$", "", s, flags=re.I)
    return STREET_PREFIX.sub("", s).strip()


def district_word(s):
    w = re.sub(r"^(?:quan|q|phuong|p)\s+", "", words(s))
    return re.sub(r"\s+(?:area|district|ward|city)$", "", w)


def fmt_counts(c):
    return ", ".join("%s %d" % kv for kv in c.most_common())


# --------------------------------------------------------------- контекст --

def norm_url(u):
    return (u or "").strip().split("?")[0].rstrip("/").lower()


def beds_from_words(w):
    # Одно слово между числом и спальнями допустимо: «3 отдельные спальни»,
    # «three separate bedrooms». Без этого у такой строки спальни неизвестны,
    # и 3-спальная сошла бы за повтор 2-спальной той же площади.
    m = re.search(r"\b(\d+|one|two|three|four|five) (?:[a-zа-я]+ )?(?:спальн\w*|спален|bedrooms?)\b", w)
    return to_int(m.group(1)) if m else None


class Ctx:
    """Всё, с чем сверяется пост: строки сайта, районы, улицы, память о заведённом."""

    def __init__(self, today):
        from site_data import load_data
        data = load_data()
        self.today = today
        cities = data["CITIES"]
        self.dnames = {c: {d["key"]: d["name"] for d in v.get("districts", [])} for c, v in cities.items()}
        # По ВСЕМ городам, а не только по двум. 12 сентября 2026 заведение
        # Facebook по девяти новым городам дало ноль строк: посты называли район
        # прямо («Khu vực trung tâm Ninh Kiều»), но сравнивать было не с чем --
        # список строился только для Дананга и Нячанга.
        self.ward_words = {}
        for city, names in self.dnames.items():
            m = {}
            for k, name in names.items():
                w = words(re.sub(r"^(?:Phường|Quận|Đặc khu|Xã|Thị trấn)\s+", "", name))
                if w and w not in CITY_WORDS.get(city, ()) and w not in OLD_DISTRICTS.get(city, {}):
                    m[w] = k
            m.update(WARD_ALIASES.get(city, {}))
            self.ward_words[city] = m
        self.bounds = json.load(open(BOUNDS, encoding="utf-8"))
        self.osm = load_osm()
        self.by_city, self.urls, self.site = collections.defaultdict(list), {}, {}
        for l in data["LISTINGS"]:
            r = dict(l)
            r["_words"] = words(" ".join([l.get("desc") or "", l.get("descEn") or "",
                                          re.sub(r"[-_/]", " ", l.get("url") or "")]))
            r["_beds"] = 0 if l.get("type") == "Студия" else beds_from_words(r["_words"])
            self.by_city[l["city"]].append(r)
            self.site[l["id"]] = r
            for u in [l.get("url")] + [x.get("url") for x in (l.get("details") or {}).get("alsoOn") or []]:
                if u:
                    self.urls[norm_url(u)] = l["id"]
        self.usd = float(data["RATES"]["perUsd"]["VND"])
        self.state = load_state()
        self.by_hash, self.by_cat, self.cat_of = {}, {}, {}
        for e in self.state["posts"].values():
            # Запись о снятой строке -- мёртвая блокировка: purge_old_listings
            # снимает строку через 14 дней, а тот же номер каталога агентство
            # выложит снова. Помним ровно столько, сколько строка стоит.
            if e.get("id") is None or e["id"] not in self.site:
                continue
            if e.get("hash"):
                self.by_hash[e["hash"]] = e["id"]
            if e.get("cat"):
                self.by_cat[e["cat"]] = e["id"]
                self.cat_of[e["id"]] = e["cat"]
        self._wcache = {}

    def ward_of(self, city, lat, lon):
        k = (city, lat, lon)
        if k not in self._wcache:
            self._wcache[k] = next((key for key, v in self.bounds.get(city, {}).items()
                                    if any(inside(lat, lon, r) for r in v["rings"])), OUTSIDE)
        return self._wcache[k]

    def district_label(self, city, key):
        return re.sub(r"^Phường\s+", "", self.dnames.get(city, {}).get(key, key))

    def remember(self, r):
        """Заведённое в этом прогоне -- тоже «уже на сайте» для следующих постов."""
        pseudo = {"id": "new:" + r["key"], "city": r["city"], "district": r["district"],
                  "type": r["type"], "area": r["area"], "pv": r["pv"], "_beds": r["beds"],
                  "_words": words(r["ru"] + " " + r["en"]), "_new": True}
        self.by_city[r["city"]].append(pseudo)
        for u in [r["permalink"]] + [x["url"] for x in r["details"].get("alsoOn", [])]:
            self.urls[norm_url(u)] = pseudo["id"]
        if r["hash"]:
            self.by_hash[r["hash"]] = pseudo["id"]
        if r["cat"]:
            self.by_cat[r["cat"]] = pseudo["id"]
            self.cat_of[pseudo["id"]] = r["cat"]


def load_state():
    try:
        s = json.load(open(STATE, encoding="utf-8"))
    except FileNotFoundError:
        s = {}
    s.setdefault("posts", {})
    return s


def save_state(state):
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(state, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    os.replace(tmp, STATE)


# ----------------------------------------------------------------- район --

_OSM_BY_CITY = {}


def osm_index(city):
    """Указатель улиц города; читается один раз за прогон."""
    if city not in _OSM_BY_CITY:
        _OSM_BY_CITY[city] = (ctx_osm_da_nang() if city == "da-nang"
                              else load_osm("osm_streets_%s.json" % city))
    return _OSM_BY_CITY[city]


def ctx_osm_da_nang():
    return load_osm(OSM_CACHE)


def street_counts(place, ctx, city="da-nang"):
    """Отрезки улицы по районам: {"counts", "names", "ambiguous"}."""
    k = words(clean_place(place))
    if not k:
        return {"counts": None, "names": [], "ambiguous": False}
    keys = [k] + ([k[len("duong "):]] if k.startswith("duong ") else [])
    index = ctx.osm if city == "da-nang" else osm_index(city)
    groups = {}
    for kk in keys:
        for name, pts in index.get(kk, {}).items():
            groups.setdefault(name, []).extend(pts)
    if not groups:
        return {"counts": None, "names": [], "ambiguous": False}
    per = {n: collections.Counter(ctx.ward_of(city, la, lo) for la, lo in pts) for n, pts in groups.items()}
    if len({c.most_common(1)[0][0] for c in per.values()}) > 1:
        return {"counts": None, "names": sorted(per), "ambiguous": True}
    total = collections.Counter()
    for c in per.values():
        total.update(c)
    return {"counts": total, "names": sorted(per), "ambiguous": False}


def precedent(name, city, ctx, exclude):
    """(район, счётчик): район -- если строк с этим названием не меньше
    MIN_PRECEDENT и все в одном районе. Заведённое этим же прогоном не в счёт."""
    n = re.sub(r"^(?:жк|комплекс|complex)\s+", "", words(name))
    if len(n) < 3 or n in CITY_WORDS.get(city, ()):
        return None, collections.Counter()
    # Раньше, если полного названия на сайте не находилось, искались его первые
    # два слова. Это ловило рекламные обороты: «Ocean View Apartment» находило
    # две строки со словами «ocean view» и уверенно ставило район -- да ещё и с
    # оговоркой «все объявления сайта из этого комплекса стоят в этом районе».
    # Ищется только полное название.
    alts = {n} | ({words(COMPLEX_LATIN[n])} if n in COMPLEX_LATIN else set())
    c = collections.Counter(l["district"] for l in ctx.by_city.get(city, [])
                            if l["id"] not in exclude and not l.get("_new")
                            and any(has_words(l["_words"], x) for x in alts))
    ok = len(c) == 1 and sum(c.values()) >= MIN_PRECEDENT
    return (next(iter(c)) if ok else None), c


def resolve_da_nang(p, ctx, exclude):
    city = "da-nang"
    wmap, olds = ctx.ward_words[city], OLD_DISTRICTS.get(city, {})
    parts = [x.strip() for x in re.split(r"[,;]", p.get("address") or "") if x.strip()]
    parts = [x for x in parts if district_word(x) not in CITY_WORDS[city]]
    old = None
    if parts and district_word(parts[-1]) in olds:
        old, parts = district_word(parts[-1]), parts[:-1]
    wards, place, ward_part = set(), None, None
    for part in parts:
        w = district_word(part)
        if w in wmap:
            wards.add(wmap[w])
            ward_part = ward_part or part
        elif w in olds:
            # Одно и то же слово прежнего района встречается в адресе дважды --
            # в заголовке и в строке адреса. Это не противоречие; противоречие --
            # только два РАЗНЫХ прежних района.
            if old and w != old:
                raise Skip("в адресе два прежних района: «%s»" % p["address"])
            old = w
        elif place is None:
            place = part
    tw = words(p.get("ward_text") or "")
    wards |= {k for w, k in wmap.items() if has_words(tw, w)}
    if old is None:
        named = [w for w in olds if has_words(tw, w)]
        if len(named) > 1:
            raise Skip("пост называет два прежних района: %s" % ", ".join(named))
        old = named[0] if named else None
    word_key, children = olds[old] if old else (None, None)
    if len(wards) > 1:
        raise Skip("пост называет несколько районов: %s" % ", ".join(sorted(wards)))
    ev, why = {}, {}
    if wards:
        ev["ward"] = next(iter(wards))
        why["ward"] = "район назван в посте"
    if children and len(children) == 1:
        ev["district"] = children[0]
        why["district"] = "прежний район %s весь вошёл в этот" % old.title()
    st = None
    if place:
        st = street_counts(place, ctx)
        counts = st["counts"]
        if counts:
            total = sum(counts.values())
            top, top_n = counts.most_common(1)[0]
            ward = ev.get("ward")
            if ward and counts.get(ward, 0) * 4 >= total:
                # Пост назвал НАСТОЯЩИЙ район сайта -- это довод, и четверти
                # отрезков хватает, чтобы ему поверить.
                k = ward
            elif children and len(children) > 1:
                # Пост назвал ПРЕЖНИЙ район, распавшийся на два. Он не говорит,
                # в каком из наследников дом, и голоса не имеет: Ngô Quyền лежит
                # на 36 отрезков в Sơn Trà и на 47 в An Hải, и по слову поста
                # («Son Tra») квартира с ан-хайского конца уезжала не туда.
                # Поэтому либо улица хотя бы на три четверти в одном районе,
                # либо пропуск. Три четверти -- не круглое число с потолка:
                # при 85% пропускалась Huỳnh Ngọc Huệ (7 отрезков из 9 в
                # Thanh Khê), а спорные Hoàng Diệu (62%) и Ngô Quyền (55%)
                # отсеиваются и так.
                if top_n < total * 0.75:
                    raise Skip("улица %s идёт через несколько районов (%s), а пост называет "
                               "только прежний район %s"
                               % (" / ".join(st["names"]), fmt_counts(counts), old.title()))
                k = top
            elif top_n * 3 >= total * 2:
                k = top
            else:
                raise Skip("улица %s идёт через несколько районов (%s)" % (" / ".join(st["names"]), fmt_counts(counts)))
            if k == OUTSIDE:
                raise Skip("улица %s лежит вне районов сайта (%s)" % (" / ".join(st["names"]), fmt_counts(counts)))
            ev["street"] = k
            why["street"] = "улица %s: %d из %d отрезков в %s%s" % (
                " / ".join(st["names"]), counts[k], total, k, "; пост: %s" % old.title() if old else "")
        else:
            k, c = precedent(clean_place(place), city, ctx, exclude)
            if k:
                ev["precedent"] = k
                why["precedent"] = "«%s»: %d строк сайта, все в %s" % (place, sum(c.values()), k)
    keys = set(ev.values())
    if not keys:
        if old and len(children) > 1 and not place:
            raise Skip("назван только прежний район %s, а он разделён на %s" % (old.title(), "/".join(children)))
        extra = ""
        if st and st["ambiguous"]:
            extra = "; без диакритики это разные улицы: %s" % ", ".join(st["names"])
        raise Skip("район не определяется: «%s»%s" % (p.get("address"), extra))
    if len(keys) > 1:
        raise Skip("источники назвали разные районы: %s" % ", ".join("%s=%s" % kv for kv in sorted(ev.items())))
    key = keys.pop()
    if children and key not in children:
        raise Skip("район %s не входит в прежний район %s из поста" % (key, old.title()))
    street_name = st["names"][0] if st and st["counts"] and len(st["names"]) == 1 else None
    return {"key": key, "how": ev, "why": why, "moved": bool(old) and "street" in ev and key != word_key,
            "place": place, "street": street_name, "ward_part": ward_part}


def resolve_nha_trang(p, ctx, exclude):
    city = "nha-trang"
    wmap = ctx.ward_words[city]
    tw = words(p.get("ward_text") or "")
    wards = {k for w, k in wmap.items() if has_words(tw, w)}
    if len(wards) > 1:
        raise Skip("пост называет несколько районов: %s" % ", ".join(sorted(wards)))
    ev, why, split = {}, {}, []
    if wards:
        ev["ward"] = wards.pop()
        why["ward"] = "район назван в посте"
    for name in p.get("complexes") or []:
        w = words(name)
        if w in wmap:
            continue
        known = PLACE_WARDS.get(city, {}).get(w)
        if known:
            if ev.get("precedent", known) != known:
                raise Skip("места из поста стоят в разных районах")
            ev["precedent"] = known
            why["precedent"] = "«%s» -- проверенное место, район %s" % (name, known)
            continue
        k, c = precedent(name, city, ctx, exclude)
        if k:
            if ev.get("precedent", k) != k:
                raise Skip("комплексы из поста стоят в разных районах")
            ev["precedent"] = k
            why["precedent"] = "«%s»: %d строк сайта, все в %s" % (name, sum(c.values()), k)
        elif c:
            split.append("«%s»: %s" % (name, fmt_counts(c)))
    keys = set(ev.values())
    if not keys:
        names = [n for n in p.get("complexes") or [] if words(n) not in wmap]
        if split:
            raise Skip("район не определяется: прецедент расколот (%s)" % "; ".join(split))
        if names:
            raise Skip("район не определяется: пост не называет района, а %s на сайте не встречается"
                       % ", ".join("«%s»" % n for n in names))
        raise Skip("район не определяется: пост не называет ни района, ни комплекса")
    if len(keys) > 1:
        raise Skip("источники назвали разные районы: %s" % ", ".join("%s=%s" % kv for kv in sorted(ev.items())))
    return {"key": keys.pop(), "how": ev, "why": why, "moved": False, "place": None, "street": None,
            "ward_part": None}


def resolve(p, ctx, exclude):
    return (resolve_da_nang if p["city"] == "da-nang" else resolve_nha_trang)(p, ctx, exclude)


# ----------------------------------------------------------------- повторы --

def close(a, b, tol=0.03):
    return bool(a) and bool(b) and abs(a - b) <= tol * max(a, b)


# Насколько может разойтись цена у повтора. Проверено на всех заведённых
# вручную телеграм-строках (12 сентября 2026):
#   * квартира -- 3 %. В одном комплексе сотни квартир одной планировки по
#     близкой цене; при 12 % повтором оказывались юниты разных корпусов и
#     этажей, то есть заведомо разные квартиры. Перепост того же объявления
#     переписывает цену как есть -- ему хватает 3 %;
#   * дом на той же улице -- 15 %: домов с тем же числом спален на одной улице
#     единицы, а цену перевыложенного объявления агентства двигают (Tan Tra:
#     35 и 40 млн -- один дом). Без предела цены совпадали разные дома одной
#     улицы: Dũng Sĩ Thanh Khê за 16 и за 25 млн.
REPOST_PRICE_TOL = {"flat": 0.03, "house": 0.15}
# Корпус во вьетнамских комплексах чаще буквенный, чем цифровой: «block A»,
# «корпус Б». Пока цифра была обязательной, правило «разные корпуса -- разные
# квартиры» просто не срабатывало.
BLOCK_RX = re.compile(r"\b(?:корпус\w*|корп|block|tower)\s+([a-zа-я]{0,3}\d{0,3}[a-zа-я]?)\b")


def block_of(w):
    m = BLOCK_RX.search(w or "")
    return m.group(1) if m else None


def duplicate(p, key, pv, place_w, ctx, exclude):
    """Строка сайта, которая, по всей видимости, и есть этот объект.

    Номер каталога агентства решает сразу: тот же -- повтор, другой -- другая
    квартира. Разные корпуса -- тоже разные квартиры. Если в адресе поста нет
    ни улицы, ни комплекса, а только район, совпадения района, типа и цены
    мало: нужна ещё та же площадь."""
    flat = p["type"] != "Дом"
    blk = (p["block"] or "").lower() or None
    for l in ctx.by_city.get(p["city"], []):
        if l["id"] in exclude or l["district"] != key or l["type"] != p["type"]:
            continue
        other_cat = ctx.cat_of.get(l["id"])
        if p["cat"] and other_cat:
            if other_cat == p["cat"]:
                return l
            continue
        if p["beds"] is not None and l["_beds"] is not None and p["beds"] != l["_beds"]:
            continue
        if p["area"] and l.get("area") and not close(p["area"], l["area"]):
            continue
        other_blk = block_of(l["_words"])
        if blk and other_blk and other_blk != blk:
            continue
        if place_w:
            if not has_words(l["_words"], place_w):
                continue
            if not close(l.get("pv"), pv, REPOST_PRICE_TOL["flat" if flat else "house"]):
                continue
        elif not (close(l.get("pv"), pv, REPOST_PRICE_TOL["flat"])
                  and ((p["area"] and l.get("area") and close(p["area"], l["area"]))
                       or (p["beds"] is not None and l["_beds"] is not None
                           and p["beds"] == l["_beds"]))):
            # Без улицы и комплекса сравнивать больше не с чем: нужна та же цена
            # и либо та же площадь, либо то же число спален. 12 сентября две
            # студии «Студия, Tây Hồ» за 6 млн без площади разошлись по сайту
            # двумя строками именно потому, что площади не было ни у одной.
            continue
        return l
    return None


# ------------------------------------------------------------------ строка --

def complex_display(name):
    """Латинское имя, если известно; КАПС из заголовка -- в обычный регистр."""
    lat = COMPLEX_LATIN.get(words(name))
    if lat:
        return lat
    if name.isupper():
        return " ".join(t.capitalize() if re.search(r"[aeiouy]", fold(t)) and not re.search(r"\d", t) else t
                        for t in name.split())
    return name


def describe(p, dname, place_ru, place_en):
    t = p["type"]
    if t == "Дом":
        noun_ru, noun_en = ("Вилла", "Villa") if p["villa"] else ("Дом", "House")
        if p["floors"]:
            head_ru = "%s в %s" % (noun_ru, ru_plural(p["floors"], "этаж", "этажа", "этажей"))
            head_en = "%s on %d floor%s" % (noun_en, p["floors"], "" if p["floors"] == 1 else "s")
        else:
            head_ru, head_en = noun_ru, noun_en
    elif t == "Студия":
        head_ru, head_en = "Студия", "Studio"
    elif p["beds"]:
        head_ru, head_en = "%d-спальная квартира" % p["beds"], "%d-bedroom flat" % p["beds"]
    else:
        head_ru, head_en = "Квартира", "Flat"
    ru, en = [head_ru], [head_en]
    if p["area"]:
        ru.append("%d м²" % p["area"])
        en.append("%d m²" % p["area"])
    ru.append(", ".join(x for x in (place_ru, dname) if x))
    en.append(", ".join(x for x in (place_en, dname) if x))
    tail_ru, tail_en = [], []
    if t == "Дом" and p["beds"]:
        tail_ru.append(ru_plural(p["beds"], "спальня", "спальни", "спален"))
        tail_en.append("%d bedroom%s" % (p["beds"], "" if p["beds"] == 1 else "s"))
    if p["baths"]:
        tail_ru.append(ru_plural(p["baths"], "санузел", "санузла", "санузлов"))
        tail_en.append("%d bathroom%s" % (p["baths"], "" if p["baths"] == 1 else "s"))
    ru_s = ", ".join(ru) + (" — " + ", ".join(tail_ru) if tail_ru else "") + "."
    en_s = ", ".join(en) + (" — " + ", ".join(tail_en) if tail_en else "") + "."
    m = p["term"]
    if m:
        if m % 12 == 0:
            ru_s += " Договор от года." if m == 12 else " Договор от %d лет." % (m // 12)
            en_s += " Contract from one year." if m == 12 else " Contract from %d years." % (m // 12)
        else:
            ru_s += " Аренда от %s." % ru_plural(m, "месяца", "месяцев", "месяцев")
            en_s += " Minimum %d month%s." % (m, "" if m == 1 else "s")
    return ru_s, en_s


def post_date(c):
    d = (c.get("date") or "").strip()
    if not d:
        raise Skip("в посте нет даты размещения")
    try:
        return datetime.datetime.fromisoformat(d).astimezone(VN_TZ).date()
    except ValueError:
        raise Skip("дата поста не читается: %r" % d[:30])


def short(permalink):
    return "/".join(permalink.rstrip("/").split("/")[-2:])


def decide(c, ctx, exclude=frozenset(), check_age=True):
    """Кандидат -> строка для партии (dict); None -- пост не по шаблону;
    Skip -- по шаблону, но заводить нельзя."""
    text = c.get("text") or ""
    if not text.strip():
        return None
    p = parse_post(text)
    if p is None:
        return None
    known = ctx.urls.get(norm_url(c["permalink"]))
    if known is not None and known not in exclude:
        raise Skip("уже на сайте: id %s" % known)
    h = ftl.text_hash(text)
    if h and ctx.by_hash.get(h) not in (None, *exclude):
        raise Skip("тот же текст уже заведён: id %s" % ctx.by_hash[h])
    if p["cat"] and ctx.by_cat.get(p["cat"]) not in (None, *exclude):
        raise Skip("номер каталога %s уже заведён: id %s" % (p["cat"].split(":")[1], ctx.by_cat[p["cat"]]))
    if p["type"] not in TYPES:
        raise Skip("тип %s не заводится" % p["type"])
    age = max(0, (ctx.today - post_date(c)).days)
    if check_age and age > MAX_AGE_DAYS:
        raise Skip("пост старше %d дней (%d)" % (MAX_AGE_DAYS, age))
    photos = [u for u in c.get("photos") or [] if re.match(r"https?://", u or "")][:MAX_PHOTOS]
    if not photos:
        raise Skip("в посте нет фотографий")
    d = resolve(p, ctx, exclude)
    key = d["key"]
    pv = p["price"] if p["cur"] == "VND" else int(round(p["price"] * ctx.usd))

    if p["city"] == "da-nang":
        place_ru = ("ул. " + d["street"]) if d["street"] else (d["place"] or d["ward_part"] or "")
        place_en = d["street"] or d["place"] or d["ward_part"] or ""
        place_w = words(d["street"] or d["place"] or "")
    else:
        name = next((n for n in p["complexes"] if words(n) not in ctx.ward_words["nha-trang"]), None)
        disp = complex_display(name) if name else ""
        place_ru = ("ЖК %s%s" % (disp, ", корпус %s" % p["block"] if p["block"] else "")) if disp else ""
        place_en = ("%s%s" % (disp, ", block %s" % p["block"] if p["block"] else "")) if disp else ""
        place_w = words(disp)
        # Правило ручного разбора 10-11 сентября: квартира в комплексе, у
        # которого уже есть строки на сайте, без площади, корпуса и номера
        # каталога -- от них не отличима, а цена у перепостов гуляет.
        if (p["type"] != "Дом" and "precedent" in d["how"]
                and not (p["area"] or p["block"] or p["cat"])):
            raise Skip("квартира в «%s» без площади, корпуса и номера каталога: от уже стоящих строк "
                       "этого комплекса её не отличить" % disp)
    dup = duplicate(p, key, pv, place_w, ctx, exclude)
    if dup:
        same = close(dup.get("pv"), pv)
        raise Skip("похоже на уже заведённое: id %s (%s)" % (
            dup["id"], "та же цена" if same else "цена на сайте %s, в посте %s %s" % (dup.get("price"), p["price"], p["cur"])))

    dname = ctx.district_label(p["city"], key)
    ru, en = describe(p, dname, place_ru, place_en)
    notice, notice_en = NOTICE_RU, NOTICE_EN
    if p["cur"] == "USD":
        notice, notice_en = notice + USD_RU, notice_en + USD_EN
    method = ("moved" if d["moved"] else "street" if "street" in d["how"] and "ward" not in d["how"]
              else "precedent" if set(d["how"]) == {"precedent"} else None)
    if method:
        notice, notice_en = notice + HOW_RU[method], notice_en + HOW_EN[method]
    details = {"photos": photos, "notice": notice, "noticeEn": notice_en}
    also = [{"source": "telegram", "url": x["permalink"]} for x in c.get("duplicates") or []
            if x.get("permalink") and norm_url(x["permalink"]) != norm_url(c["permalink"])]
    if also:
        details["alsoOn"] = also
    return {"key": short(c["permalink"]), "permalink": c["permalink"], "city": p["city"], "district": key,
            "type": p["type"], "price": p["price"], "cur": p["cur"], "pv": pv, "area": p["area"],
            "beds": p["beds"], "ru": ru, "en": en, "age": age, "details": details, "hash": h,
            "cat": p["cat"], "template": p["template"],
            "why": "; ".join(d["why"][k] for k in ("ward", "district", "street", "precedent") if k in d["why"])}


# ------------------------------------------- сверка с заведённым раньше --

def seed_state(ctx, budget=SEED_FETCHES):
    """Номера каталога и тексты уже заведённых телеграм-строк, в том числе
    заведённых вручную: без них перепост того же объекта через неделю завёлся
    бы второй раз. Посты читаются один раз и запоминаются в STATE. Попутно --
    что за это время случилось с постом: удалён или цена в нём другая."""
    posts, report = ctx.state["posts"], []
    need = collections.defaultdict(dict)
    for city_rows in ctx.by_city.values():
        for l in city_rows:
            if l.get("_new") or l.get("source") != "telegram":
                continue
            m = re.match(r"https?://t\.me/([^/]+)/(\d+)$", (l.get("url") or "").rstrip("/"))
            if m and norm_url(l["url"]) not in posts:
                need[m.group(1)][int(m.group(2))] = l
    fetched = 0
    for ch, ids in need.items():
        todo = set(ids)
        while todo and fetched < budget:
            top = max(todo)
            try:
                html = ftl.http_get("https://t.me/s/%s?before=%d" % (ch, top + 1))
            except Exception as e:
                report.append("  %s: не открылся (%s) -- сверка в следующий раз" % (ch, type(e).__name__))
                break
            fetched += 1
            page, _ = ftl.parse_page(html, ch)
            if not page and "tgme_widget_message" not in html:
                # 200 с чужим телом (заглушка, антибот) разбирается в пустой
                # список -- и каждый непроверенный пост объявлялся удалённым.
                report.append("  %s: страница канала не прочиталась -- сверка в следующий раз" % ch)
                break
            got = {q["msg_id"]: q for q in page}
            low = min(got) if got else top
            for i in sorted(todo, reverse=True):
                if i < low:
                    continue
                l = ids[i]
                todo.discard(i)
                if i not in got:
                    posts[norm_url(l["url"])] = {"id": l["id"], "missing": ctx.today.isoformat()}
                    report.append("  %s/%d (id %s): поста в канале больше нет" % (ch, i, l["id"]))
                    continue
                q = got[i]
                e = {"id": l["id"], "hash": ftl.text_hash(q["text"]), "checked": ctx.today.isoformat()}
                try:
                    pp = parse_post(q["text"] or "")
                except Skip:
                    pp = None
                if pp:
                    e["cat"] = pp["cat"]
                    if pp["price"] and (pp["cur"] == (l.get("cur") or "VND")) and pp["price"] != l.get("price"):
                        report.append("  %s/%d (id %s): цена в посте %s, на сайте %s"
                                      % (ch, i, l["id"], pp["price"], l.get("price")))
                posts[norm_url(l["url"])] = e
                if e.get("hash"):
                    ctx.by_hash[e["hash"]] = l["id"]
                if e.get("cat"):
                    ctx.by_cat[e["cat"]] = l["id"]
                    ctx.cat_of[l["id"]] = e["cat"]
            time.sleep(1.0)
    return report


# ------------------------------------------------------------------ партия --

HEADER = '''# -*- coding: utf-8 -*-
"""Telegram, заведение по шаблонам агентств: %(n)s, %(date)s.

Партию собрал ingest_telegram.py -- без модели в контуре. Заведены только посты,
целиком совпавшие с шаблоном агентства. Район -- из слов поста, по улице (её
отрезки из OpenStreetMap в границах районов карты) или по жилому комплексу, все
строки которого на сайте стоят в одном районе; правила -- в начале
ingest_telegram.py.

ЗАВЕДЕНО:
%(accepted)s

ПО ШАБЛОНУ, НО НЕ ЗАВЕДЕНО (%(nskip)d):
%(skipped)s
"""
from listing_lock import insert_listings

IDS = %(ids)r

NEW_SRC = r%(q)s
%(rows)s
%(q)s

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
'''


def doc_safe(s):
    return s.replace("\\", "/").replace('"""', '"')


@functools.lru_cache(maxsize=None)
def _days_label_fn():
    src = open("rebuild_final.py", encoding="utf-8").read()
    fn = next(x for x in ast.walk(ast.parse(src))
              if isinstance(x, ast.FunctionDef) and x.name == "_ru_days_label")
    ns = {}
    exec(ast.unparse(fn), ns)
    return ns["_ru_days_label"]


def posted_label(n):
    return _days_label_fn()(n)


def write_batch(accepted, skipped, ids, today):
    j = lambda s: json.dumps(s, ensure_ascii=False)
    rows = []
    for i, r in zip(ids, accepted):
        rows.append('L(%d,"%s","%s","%s",%d,%s,\n  %s,\n  %s,%s,%d,source="telegram"%s,\n'
                    '  descEn=%s,\n  details=%s),'
                    % (i, r["city"], r["district"], r["type"], r["price"],
                       r["area"] if r["area"] else "None", j(r["ru"]), j(r["permalink"]),
                       j(posted_label(r["age"])), r["age"], ',cur="USD"' if r["cur"] == "USD" else "",
                       j(r["en"]), j(r["details"])))
    acc = "\n".join("  * %s -- %s/%s, %s: %s" % (r["key"], r["city"], r["district"], r["template"], r["why"])
                    for r in accepted)
    skp = "\n".join("  * %s -- %s" % kv for kv in skipped) or "  (нет)"
    nums = [int(re.sub(r"\D", "", f) or 0) for f in glob.glob("new_listings*.py")]
    path = "new_listings%d.py" % (max(nums + [0]) + 1)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HEADER % {"n": ru_plural(len(rows), "строка", "строки", "строк"),
                          "date": today.isoformat(), "accepted": doc_safe(acc),
                          "nskip": len(skipped), "skipped": doc_safe(skp), "ids": ids,
                          "q": "'''", "rows": "\n".join(rows)})
    return path


def allocate(n, block="2000000", owner="ingest_telegram"):
    """Блок id по источнику: 2000000 -- Telegram, 3000000 -- hoppler и Facebook."""
    out = subprocess.run([sys.executable, "allocate_ids.py", "--block", block, "--count", str(n),
                          "--owner", owner], capture_output=True, text=True, encoding="utf-8")
    m = re.search(r"FIRST=(\d+) LAST=(\d+)", out.stdout or "")
    if not m:
        sys.exit("не удалось зарезервировать id:\n%s%s" % (out.stdout, out.stderr))
    return list(range(int(m.group(1)), int(m.group(2)) + 1))


def main():
    ap = argparse.ArgumentParser(description="Заведение телеграм-постов по шаблонам агентств")
    ap.add_argument("--candidates", default=CANDIDATES)
    ap.add_argument("--limit", type=int, default=40, help="не больше стольких строк за прогон")
    ap.add_argument("--write", action="store_true", help="записать партию new_listingsNNN.py")
    ap.add_argument("--insert", action="store_true", help="и вставить её в rebuild_final.py")
    ap.add_argument("--refresh-osm", action="store_true", help="обновить выгрузку улиц Дананга")
    ap.add_argument("--no-seed", action="store_true", help="не читать посты уже заведённых строк")
    a = ap.parse_args()
    os.chdir(HERE)
    sys.stdout.reconfigure(encoding="utf-8")

    if a.refresh_osm or not os.path.exists(OSM_CACHE):
        print("улицы Дананга из OpenStreetMap: %d названий" % refresh_osm())
    try:
        payload = json.load(open(a.candidates, encoding="utf-8"))
    except FileNotFoundError:
        print("нет %s -- сборщик каналов в этом прогоне не запускался, заводить нечего" % a.candidates)
        return 0
    today = datetime.datetime.now(VN_TZ).date()
    ctx = Ctx(today)
    if not a.no_seed:
        rep = seed_state(ctx)
        if rep:
            print("сверка заведённых раньше телеграм-строк:")
            print("\n".join(rep))

    accepted, skipped, manual = [], [], collections.Counter()
    for c in payload.get("candidates") or []:
        try:
            r = decide(c, ctx)
        except Skip as e:
            skipped.append((short(c["permalink"]), str(e)))
            continue
        except Exception as e:
            # Разбор пятидесяти постов не должен зависеть от пятьдесят первого:
            # кандидат с неожиданными данными уходит в отчёт, а не роняет шаг.
            skipped.append((short(c.get("permalink") or "?"),
                            "разбор сорвался: %s: %s" % (type(e).__name__, e)))
            continue
        if r is None:
            manual[c.get("channel", "?")] += 1
            continue
        if len(accepted) >= a.limit:
            skipped.append((r["key"], "лимит прогона (%d) выбран" % a.limit))
            continue
        accepted.append(r)
        ctx.remember(r)

    print("Телеграм-шаблоны: кандидатов %d, по шаблону %d, заводится %d"
          % (len(payload.get("candidates") or []), len(accepted) + len(skipped), len(accepted)))
    for r in accepted:
        print("  + %-30s %s/%-4s %-9s %12s %s  %s м²  -- %s"
              % (r["key"], r["city"], r["district"], r["type"], format(r["price"], ","), r["cur"],
                 r["area"] or "?", r["why"]))
    for k, why in skipped:
        print("  - %-30s %s" % (k, why))
    if manual:
        print("  не по шаблону, оставлены для ручного разбора: %s"
              % ", ".join("%s %d" % kv for kv in manual.most_common()))

    if not a.write:
        return 0
    if not accepted:
        save_state(ctx.state)
        return 0
    ids = allocate(len(accepted))
    inserted = False
    try:
        path = write_batch(accepted, skipped, ids, today)
        print("\nзаписано: %s -- %d строк, id %d..%d" % (path, len(ids), ids[0], ids[-1]))
        if not a.insert:
            save_state(ctx.state)
            print("(--insert не задан: партия записана, но не вставлена)")
            return 0
        subprocess.run([sys.executable, path], check=True)
        inserted = True
    finally:
        # Бронь снимается в любом случае: и после вставки, и если партия не
        # записалась. Иначе номера выпадали из оборота на сутки после каждого
        # прогона с --write без --insert.
        subprocess.run([sys.executable, "allocate_ids.py", "--release", "%d-%d" % (ids[0], ids[-1])])
        if not inserted:
            print("вставка не состоялась -- зарезервированные id освобождены")
    for i, r in zip(ids, accepted):
        entry = {"id": i, "hash": r["hash"], "cat": r["cat"], "checked": today.isoformat()}
        ctx.state["posts"][norm_url(r["permalink"])] = entry
        for x in r["details"].get("alsoOn", []):
            ctx.state["posts"][norm_url(x["url"])] = {"id": i, "checked": today.isoformat()}
    save_state(ctx.state)
    return 0


if __name__ == "__main__":
    sys.exit(main())
