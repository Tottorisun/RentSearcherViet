# -*- coding: utf-8 -*-
"""
Заведение постов из групп Facebook -- без человека, по тем же правилам, что и
телеграмное (ingest_telegram.py, там же подробности про районы).

ЗАЧЕМ. fb_collect.py сам заходит в группы, сам скачивает фотографии и сам
отсеивает мусор (нет цены, нет адреса, не аренда, пост умер, уже на сайте), но
останавливается на файле кандидатов: строку из свободного текста заводил
человек. Пока человек не сядет разбирать, объявления не появляются, а
подписанные ссылки Facebook на фотографии живут около четырёх дней.

ЧТО ЗАВОДИТСЯ. Пост, у которого разобралось ВСЁ: тип жилья, одна-единственная
цена, фотографии на диске, и район доказан одним из трёх способов:
  * пост называет район, который есть на сайте у этого города (или прежний
    квартал из FB_ALIASES, чей нынешний район установлен по адресам OSM);
  * Дананг: улица из адресной строки найдена в OpenStreetMap, и её отрезки
    лежат в границах наших районов (правило четверти и двух третей -- в
    ingest_telegram.py);
  * название из адресной строки уже встречается в ОПИСАНИЯХ не меньше чем двух
    строк сайта этого города, и все они в одном районе.
Два способа дали разное -- пропуск. Ни один не сработал -- пропуск. Всё
непонятое остаётся кандидатом для разбора человеком, как раньше.

ГДЕ ИСКАТЬ РАЙОН -- ТОЛЬКО В АДРЕСНОЙ СТРОКЕ И ЗАГОЛОВКЕ. По всему тексту это
не работает: 12 сентября в постах нашлись «easy access to Makati» (объект в
Paco), «5-min drive to Valencia» (объект в Lower Cantil-e) и «одна поездка до
Malate» (объект в Sampaloc) -- везде слово района есть, а район другой.
Куски, начинающиеся с «near», «walking distance», «5 min to», выбрасываются.

ПРЕЦЕДЕНТ -- ТОЛЬКО ПО НАЗВАНИЮ МЕСТА, И ТРИ СИТА ОТДЕЛЯЮТ ЕГО ОТ РЕКЛАМЫ.
Иначе «уликой» становятся «house for rent», «Cebu City» и «spacious studio»:
12 сентября такое совпадение чуть не завело строку в Bình Trưng только потому,
что два объявления сайта с теми же общими словами стоят там. Сита:
  * слово должно быть редким в описаниях сайта этого города (rare_words);
  * слово не должно бродить по объявлениям РАЗНЫХ городов: топоним привязан к
    одному городу, «full», «nội thất», «spacious», «furnished» -- ко всем
    (ad_cities). Достаточно, чтобы своим было хотя бы одно слово названия;
  * улика должна стоять в ОПИСАНИИ строки сайта, а не в её ссылке (desc_hits):
    ссылка Chợ Tốt -- это заголовок продавца, набранный той же рекламой, что и
    пост, и сравнение двух реклам о месте не говорит ничего.
Порог в 20% от прогона, стоявший здесь раньше, не спасал: 12 сентября «Full
Nội Thất» («полная меблировка») прошло его насквозь и увело пост про Bình
Thạnh/Phú Nhuận в Tân Mỹ -- район 7 на другом конце города.

ЧЕГО ЗДЕСЬ НАМЕРЕННО НЕТ.
  * Цены «на глаз». Если в тексте несколько разных сумм (с мебелью и без,
    «от 10 млн», диапазон) -- строка не заводится: 11 сентября именно на таких
    постах разбор ошибался чаще всего.
  * Даты. Facebook её не публикует, и придумывать её нельзя. Возраст строки --
    это время с проверки: сборщик открыл пост по ссылке и убедился, что он
    жив. Так же заведены и все строки Facebook, сделанные руками.
  * Запуска на сервере. Кандидаты Facebook есть только на ПК владельца: туда
    программа ходит его личным профилем браузера. Поэтому заведение идёт на
    ПК, а публикует потом сервер.

ЗАПУСК
    python ingest_facebook.py                     отчёт: что завелось бы и почему нет
    python ingest_facebook.py --write             записать партию new_listingsNNN.py
    python ingest_facebook.py --write --insert    и вставить её в rebuild_final.py
    python ingest_facebook.py --write --insert --commit   и закоммитить (так зовёт
        run_pipeline.py на ПК: сервер соберёт сайт, только когда строки в репозитории)
"""
import argparse
import collections
import datetime
import glob
import json
import os
import re
import subprocess
import sys

import ingest_telegram as it

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = "facebook_ingest_state.json"
CAND_GLOB = "_fb_*_*.json"
FRESH_HOURS = 30          # файлы кандидатов прошлой ночи и сегодняшнего дня
MAX_PHOTOS = 6
MIN_BODY = 60
SOURCE_BY_MODE = {"group_post": "fbgroup", "marketplace": "fbmarketplace"}
PRICE_LIMITS = {"VND": (1_500_000, 500_000_000), "PHP": (3_000, 500_000), "USD": (100, 20_000)}

# Прежние кварталы и местности, чей нынешний район установлен по адресной
# иерархии OSM (см. память проекта о реформе районов). Дополняют таблицу
# ingest_telegram.WARD_ALIASES, не заменяя её.
FB_ALIASES = {
    "ho-chi-minh": {"thao dien": "ak", "an phu": "ak"},
}

# Пост не про аренду жилья на месяцы, даже если слово «rent» в нём есть.
# Проверка идёт по свёрнутому тексту (it.words): без диакритики, в нижнем
# регистре, без знаков препинания и без переводов строк. Образцы намеренно
# узкие: широкое «looking for» отсеяло пять нормальных объявлений, где хозяин
# ищет арендатора, а не жильё.
NOT_A_RENTAL = (
    (r"\brent to own\b|\brent2own\b", "продажа в рассрочку, а не аренда"),
    (r"\bfor sale\b|\bban nha\b|\bban can ho\b|\bsang nhuong\b", "продажа"),
    (r"\bdown payment\b|\bequity\b|\binstallment\b", "рассрочка"),
    (r"(?:looking for|in search of|ищу|сниму|need).{0,30}(?:roommate|female|соседк|сожител)",
     "ищут соседа, а не сдают"),
    (r"\bcan thue\b|\bищу\b.{0,20}(?:квартир|комнат|дом)|\bсниму\b",
     "это поиск жилья, а не предложение"),
    (r"\bper night\b|\bnightly\b|посуточн|\bdaily rate\b", "посуточно"),
)

# Тип жилья. Порядок важен: «studio apartment» -- студия, а не квартира.
TYPE_RULES = (
    (r"\bstudio\b|студи|\bmini\s?house\b|\bcan ho mini\b|\bchung cu mini\b", "Студия"),
    (r"\bvilla\b|\bbiet thu\b|вилл", "Дом"),
    (r"\btown\s*house\b|\bnha pho\b|таунхаус", "Дом"),
    (r"\bhouse\b|\bnha nguyen can\b|\bдом\b", "Дом"),
    (r"\bapartment\b|\bapt\b|\bflat\b|\bcondo\b|\bcan ho\b|\bchung cu\b|\bpenthouse\b|квартир",
     "Квартира"),
    (r"\broom for rent\b|\bphong tro\b|\bnha tro\b|\bphong cho thue\b|комнат", "Комната"),
)

# Строка адреса: с неё начинается разбор района.
ADDR_LINE = re.compile(
    r"^.{0,4}(?:📍|🏠|🏡|address|adress|location|located\s+(?:in|at|on)|situated\s+in|"
    r"địa chỉ|dia chi|адрес|адресс|находится\s+в)\s*:?\s*(.+)$", re.I | re.M)
# Ориентир -- не адрес: «рядом с Lotte», «5 минут до Mỹ Khê», «easy access to
# Makati». Такие куски выбрасываются, иначе район берётся от соседнего города.
NEARBY = re.compile(r"^\s*(?:near|close to|beside|next to|walking distance|access to|"
                    r"\d+\s*[- ]?(?:min|mins|minute|minutes)|рядом|близко|в \d+ минут)", re.I)
STREET_TAIL = re.compile(r"\b([A-ZĐ][\wÀ-ỹ']*(?:\s+[A-ZĐ0-9][\wÀ-ỹ']*){0,3})\s+(?:street|str\.?|st\.)\b")
STREET_HEAD = re.compile(r"\b(?:đường|duong|street|ул\.)\s+([A-ZĐ][\wÀ-ỹ']*(?:\s+[A-ZĐ0-9][\wÀ-ỹ']*){0,3})")
# Слова, которые в адресной строке ничего не называют, но встречаются в
# описаниях сайта, поэтому дали бы ложный прецедент.
STOP_PHRASES = re.compile(
    r"^(for rent|rent|apartment|apartments|studio|house|villa|room|rooms|condo|unit|new|"
    r"fully furnished|furnished|near|close|beach|city|center|centre|district|ward|"
    r"street|road|floor|bedroom|bedrooms|bathroom|price|month|contact|zalo|whatsapp|"
    r"аренда|квартира|дом|студия|комната|район|улица|рядом|центр|пляж)$")

NOTICE_RU = ("Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому "
             "возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что "
             "он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный "
             "текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки "
             "Facebook на изображения подписаны и живут около четырёх дней. Цену и условия "
             "подтверждайте у автора объявления.")
NOTICE_EN = ("Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown "
             "is the time since the check: the program opened the post and confirmed it is alive. The "
             "description was assembled from the post's fields — type, bedrooms, size, address and "
             "price; the marketing text is not retold. The photos come from the post itself and are "
             "stored on this site, because Facebook's own image links are signed and expire in about "
             "four days. Confirm the price and terms with the poster.")


class Skip(it.Skip):
    """Пост разобран, но заводить его нельзя."""


# ------------------------------------------------------------------ разбор --

def body_of(c):
    return it.nfc(c.get("body") or "")


def rental_or_skip(text):
    f = it.words(text)
    for rx, why in NOT_A_RENTAL:
        if re.search(rx, f):
            raise Skip(why)


def _type_in(src):
    f = it.words(src)
    for rx, typ in TYPE_RULES:
        if re.search(rx, f):
            return typ
    return None


# Сдаётся не дом целиком, а его часть: «bottom part», «silong ra» (по-себуански
# «только низ»), «tầng trệt». Заголовок при этом кричит HOUSE FOR RENT, и тип
# выходил «Дом» -- фильтр показывал бы такую строку тем, кто ищет дом целиком.
# Пост 4606474172943066: «HOUSE FOR RENT... Bottom part lang (SILONG RA), 2 bedroom».
PART_OF_HOUSE = re.compile(
    r"\bbottom part\b|\bsilong\b|\bupper floor only\b|\bground floor only\b|"
    r"\b(?:1st|2nd|first|second) floor only\b|\btang tret\b")


def type_of(text):
    """(тип, спальни). Тип сначала ищется в ЗАГОЛОВКЕ поста и только потом во
    всём тексте: у «1 BEDROOM APARTMENT FOR RENT» ниже по тексту почти всегда
    попадается слово studio, и по всему тексту квартира становилась студией."""
    typ = _type_in(it.first_line(text)) or _type_in(text)
    if not typ:
        raise Skip("тип жилья в тексте не назван")
    beds = it.beds_in(text)
    if typ == "Квартира" and beds == 0:
        typ = "Студия"
    if typ == "Дом" and PART_OF_HOUSE.search(it.words(text)):
        typ = "Квартира"
    if typ == "Студия":
        beds = 0
    return typ, beds


# Любое число с тысячами из текста: ищем вторую цену, которую сборщик не счёл
# ценой. 12 сентября пост про Valencia назвал 25 000 ₱ с мебелью и 18 000 ₱ без
# неё; сборщик вернул одну сумму, и строка ушла бы на сайт с ценой, которой в
# заголовке объявления нет. Отсеиваются только числа того же порядка, что цена
# (от трети до трёх цен): коммуналка, площадь и телефоны в этот коридор не попадают.
AMOUNT_RX = re.compile(r"(?<![\d.,])(\d{1,3}(?:[.,\s]\d{3})+|\d{4,9})(?![\d.,])")


def other_prices(text, price):
    out = set()
    for m in AMOUNT_RX.finditer(text or ""):
        v = int(re.sub(r"\D", "", m.group(1)))
        if 0.3 * price <= v <= 3 * price and abs(v - price) > 0.03 * price:
            out.add(v)
    return sorted(out)


def price_of(c):
    """Одна цена -- или пропуск. Разные суммы в посте (с мебелью и без, «от»,
    диапазон) человек различает по смыслу, программа -- нет."""
    cur = (c.get("currency") or "VND").upper()
    amounts = {x.get("amount") for x in (c.get("price_candidates") or []) if x.get("amount")}
    if c.get("price"):
        amounts.add(c["price"])
    amounts = {int(a) for a in amounts if a}
    if not amounts:
        raise Skip("цены в посте нет")
    if len(amounts) > 1:
        raise Skip("в посте несколько разных цен: %s" % ", ".join(format(a, ",") for a in sorted(amounts)))
    price = amounts.pop()
    lo, hi = PRICE_LIMITS.get(cur, PRICE_LIMITS["VND"])
    if not lo <= price <= hi:
        raise Skip("цена %s %s вне разумных пределов" % (format(price, ","), cur))
    others = other_prices(body_of(c), price)
    if others:
        raise Skip("в тексте есть и другая цена того же порядка: %s против %s"
                   % (", ".join(format(v, ",") for v in others), format(price, ",")))
    return price, cur


def area_of(c):
    vals = {x.get("m2") for x in (c.get("area_candidates") or []) if x.get("m2")}
    if c.get("area_m2"):
        vals.add(c["area_m2"])
    vals = {int(round(v)) for v in vals if v and 10 <= v <= 2000}
    if len(vals) != 1:
        return None          # ноль или спор -- площадь просто не показываем
    return vals.pop()


def photos_of(c):
    """Фотографии, которые действительно лежат на диске. Пустой файл не в счёт:
    os.path.exists его пропускает, а на сайте он выйдет битой картинкой -- так
    выглядит оборванное скачивание, а не отсутствие фотографии."""
    out = []
    for p in c.get("photos") or []:
        f = p.get("file") if isinstance(p, dict) else p
        full = os.path.join(HERE, f) if f else None
        if full and os.path.isfile(full) and os.path.getsize(full) > 0:
            out.append(f.replace("\\", "/"))
    return out[:MAX_PHOTOS]


def address_lines(text):
    """Куски, в которых пост называет адрес: строки с пометкой адреса и
    заголовок, разрезанные по запятым, без ориентиров «рядом с чем-то»."""
    raw = [m.group(1).strip() for m in ADDR_LINE.finditer(text)]
    first = it.first_line(text)
    if first:
        raw.append(first)
    keep = []
    for ln in raw:
        for part in re.split(r"[,;|·•–—]", ln):
            part = part.strip()
            if part and not NEARBY.match(part):
                keep.append(part)
    return keep


def street_from(lines_):
    for ln in lines_:
        for rx in (STREET_HEAD, STREET_TAIL):
            m = rx.search(ln)
            if m:
                return m.group(1).strip()
    return None


def rare_words(ctx, city):
    """Как часто слово встречается в описаниях строк этого города. Название
    места должно состоять из РЕДКИХ слов -- см. заголовок файла."""
    df = collections.Counter()
    rows = [l for l in ctx.by_city.get(city, []) if not l.get("_new")]
    for l in rows:
        for w in set(l["_words"].split()):
            df[w] += 1
    return df, len(rows)


def ad_cities(cands):
    """Слово -> города, в объявлениях которых оно встречалось.

    ЗАЧЕМ ПО ГОРОДАМ, А НЕ ПО ЧАСТОТЕ. Название места привязано к одному
    городу; описательный оборот встречается всюду. Считать одной частотой не
    работает: 12 сентября «Full Nội Thất» («полная меблировка») прошло сквозь
    порог в 20% -- слова «full», «nội», «thất» попались всего в 5-7 постах из
    67, -- и пост про Bình Thạnh/Phú Nhuận уехал в Tân Mỹ, район 7 на другом
    конце города. По городам те же слова видны сразу: каждое из трёх пришло из
    двух-трёх разных городов. Правило работает, только когда прогон
    многогородний -- ночной сбор идёт по всем восьми, но если запустить его на
    одном городе, эта проверка ничего не отсеет."""
    m = collections.defaultdict(set)
    for c in cands:
        for w in set(it.words(body_of(c)).split()):
            m[w].add(c.get("city_key") or "?")
    return m


def named_phrases(lines_, df, nrows, cities=None):
    """Названия-кандидаты из адресных строк: сами куски и заглавные
    словосочетания внутри них -- но только те, где каждое слово редкое в
    описаниях сайта и хотя бы одно не бродит по объявлениям разных городов."""
    limit = max(3, int(0.05 * nrows))

    def ok(phrase):
        w = it.words(phrase)
        if not w or len(w) < 3 or len(w.split()) > 4 or STOP_PHRASES.match(w):
            return False
        if not any(len(t) > 2 and not t.isdigit() for t in w.split()):
            return False
        # Отбрасываем, только если ВСЕ слова разъездные. Достаточно одного
        # своего: «Casa Mira Towers», «Wilshire Plaza», «An Thuong» держатся
        # на «mira», «wilshire», «thuong», хотя «towers», «plaza» и «an»
        # попадаются в других городах, а «Full Nội Thất» и «Spacious Studio»
        # не держатся ни на чём.
        if cities and all(len(cities.get(t, ())) > 1 for t in w.split()):
            return False
        return all(df.get(t, 0) <= limit for t in w.split())

    out = []
    for ln in lines_:
        caps = [m.group(1).strip() for m in
                re.finditer(r"\b([A-ZĐ][\wÀ-ỹ']{2,}(?:\s+[A-ZĐ0-9][\wÀ-ỹ']*){0,3})", ln)]
        for x in [ln.strip(" .-:()!*")] + caps:
            if 3 <= len(x) <= 40 and ok(x):
                out.append(x)
    seen, uniq = set(), []
    for x in out:
        k = it.words(x)
        if k not in seen:
            seen.add(k)
            uniq.append(x)
    return uniq


def place_name(s):
    """Название места без номера дома и без слова «улица».

    ЗАЧЕМ. Для поиска «95 Ocean View Apartment» и «Ocean View Apartment» --
    разные строки: настоящий прецедент не находится, повтор не ловится, а в
    описании на сайте оказывается номер дома из чужого поста."""
    return it.clean_place(s or "").strip() or None


def desc_hits(name, key, city, ctx, exclude):
    """Сколько строк района называют это место в САМОМ ОПИСАНИИ.

    ЗАЧЕМ. it.precedent ищет улику в desc + descEn + ССЫЛКЕ. Ссылка Chợ Tốt --
    это заголовок продавца («cho-thue-nha-full-noi-that-...»), набранный теми
    же рекламными оборотами, что и пост Facebook, так что совпадение двух
    реклам о месте не говорит ничего. 12 сентября «Full Nội Thất» («полная
    меблировка») совпало с четырьмя строками Tân Mỹ -- во всех четырёх только
    в ссылке, а пост был про Bình Thạnh/Phú Nhuận. Описание пишем мы сами, и
    место в нём названо местом, поэтому улику принимаем только оттуда."""
    n = re.sub(r"^(?:жк|комплекс|complex)\s+", "", it.words(name))
    alts = [n] + ([" ".join(n.split()[:2])] if len(n.split()) >= 3 else [])
    alts += [it.words(it.COMPLEX_LATIN[a]) for a in list(alts) if a in it.COMPLEX_LATIN]
    return sum(1 for l in ctx.by_city.get(city, [])
               if l["district"] == key and l["id"] not in exclude and not l.get("_new")
               and any(it.has_words(l["_dwords"], a) for a in alts))


def ward_keys_in(text, city, ctx):
    return {k for w, k in ctx.ward_words.get(city, {}).items() if it.has_words(it.words(text), w)}


def resolve(c, text, city, ctx, exclude):
    """(ключ района, чем доказан, чем подписать место, переехал ли район).
    Правила -- как в ingest_telegram: слово поста, улица, прецедент;
    расхождение между ними -- пропуск."""
    lines_ = address_lines(text)
    if not lines_:
        raise Skip("в посте нет адресной строки")
    if city == "da-nang":
        p = {"city": city, "address": ", ".join(lines_[:3]), "ward_text": " | ".join(lines_)}
        d = it.resolve_da_nang(p, ctx, exclude)
        return (d["key"], d["why"],
                place_name(d.get("street") or d.get("place") or d.get("ward_part")), d["moved"])

    wards = ward_keys_in(" | ".join(lines_), city, ctx)
    if len(wards) > 1:
        raise Skip("адрес называет несколько районов: %s" % ", ".join(sorted(wards)))
    ev, why, place, split, tried = {}, {}, None, [], set()
    if wards:
        ev["ward"] = next(iter(wards))
        why["ward"] = "район назван в адресе поста"
    df, nrows = rare_words(ctx, city)
    for phrase in named_phrases(lines_, df, nrows, getattr(ctx, "ad_cities", None)):
        name = place_name(phrase)
        w = it.words(name or "")
        # Без номера дома «109 Valero» и «Valero» -- одно и то же название, и
        # искать его дважды незачем: в отказе оно печаталось бы два раза.
        if len(w) < 3 or w in tried or w in it.CITY_WORDS.get(city, ()) or w in ctx.ward_words.get(city, {}):
            continue
        tried.add(w)
        # Прецедент -- не меньше двух строк ОДНОГО города (it.precedent ищет
        # только внутри ctx.by_city[city] и требует it.MIN_PRECEDENT), и улика
        # должна стоять в описании строки, а не в ссылке продавца.
        k, cnt = it.precedent(name, city, ctx, exclude)
        if k and desc_hits(name, k, city, ctx, exclude) < it.MIN_PRECEDENT:
            split.append("«%s»: совпало только в ссылках строк %s -- это реклама, а не место"
                         % (name, k))
            k, cnt = None, None
        if k:
            if ev.get("precedent", k) != k:
                raise Skip("названия из адреса стоят на сайте в разных районах")
            ev["precedent"] = k
            why["precedent"] = "«%s»: %d строк сайта, все в %s" % (name, sum(cnt.values()), k)
            place = place or name
        elif cnt:
            split.append("«%s»: %s" % (name, it.fmt_counts(cnt)))
    # Улица как ещё один довод -- там, где это проверяемо (см. OSM_STREET_CITIES).
    # Правило строже дананговского: улица должна почти целиком лежать в одном
    # районе, иначе довода нет. Расхождение с названным районом -- пропуск.
    if city in it.OSM_STREET_CITIES and city != "da-nang":
        street = street_from(lines_)
        st = it.street_counts(street, ctx, city) if street else None
        if st and st["counts"]:
            total = sum(st["counts"].values())
            top, top_n = st["counts"].most_common(1)[0]
            if top != it.OUTSIDE and top_n >= 0.85 * total:
                ev["street"] = top
                why["street"] = "улица %s: %d из %d отрезков в %s" % (
                    " / ".join(st["names"]), top_n, total, top)
                place = place or (st["names"][0] if st["names"] else street)

    keys = set(ev.values())
    if not keys:
        raise Skip("район не определяется по адресу «%s»%s"
                   % (lines_[0][:50], "; прецедент расколот: %s" % "; ".join(split[:2]) if split else ""))
    if len(keys) > 1:
        raise Skip("источники назвали разные районы: %s"
                   % ", ".join("%s=%s" % kv for kv in sorted(ev.items())))
    return keys.pop(), why, place or place_name(street_from(lines_)), False


def describe(typ, beds, baths, area, place, dname):
    if typ == "Студия":
        ru, en = "Студия", "Studio"
    elif typ == "Комната":
        ru, en = "Комната", "Room"
    elif typ == "Дом":
        ru = "%d-спальный дом" % beds if beds else "Дом"
        en = "%d-bedroom house" % beds if beds else "House"
    elif beds:
        ru, en = "%d-спальная квартира" % beds, "%d-bedroom flat" % beds
    else:
        ru, en = "Квартира", "Flat"
    pr, pe = [ru], [en]
    if area:
        pr.append("%d м²" % area)
        pe.append("%d m²" % area)
    pr.append(", ".join(x for x in (place, dname) if x))
    pe.append(", ".join(x for x in (place, dname) if x))
    tail_ru = [it.ru_plural(baths, "санузел", "санузла", "санузлов")] if baths else []
    tail_en = ["%d bathroom%s" % (baths, "" if baths == 1 else "s")] if baths else []
    return (", ".join(pr) + (" — " + ", ".join(tail_ru) if tail_ru else "") + ".",
            ", ".join(pe) + (" — " + ", ".join(tail_en) if tail_en else "") + ".")


def decide(c, ctx, exclude=frozenset()):
    """Кандидат -> строка для партии (dict); None -- разбирать нечего;
    Skip -- разобран, но заводить нельзя."""
    text = body_of(c)
    if len(text) < MIN_BODY:
        return None
    city = c.get("city_key")
    if city not in ctx.dnames:
        return None
    url = it.norm_url(c.get("url") or "")
    known = ctx.urls.get(url)
    if known is not None and known not in exclude:
        raise Skip("уже на сайте: id %s" % known)
    h = it.ftl.text_hash(text)
    if h and ctx.by_hash.get(h) not in (None, *exclude):
        raise Skip("тот же текст уже заведён: id %s" % ctx.by_hash[h])
    rental_or_skip(text)
    typ, beds = type_of(text)
    price, cur = price_of(c)
    area = area_of(c)
    photos = photos_of(c)
    if not photos:
        raise Skip("нет ни одной скачанной фотографии")
    # Строка ссылается на файлы assets/fb_photos/<пост>/NN.webp, и уехать в
    # репозиторий они должны все: недостача -- это оборванное скачивание, а на
    # сайте она выйдет карточкой с пустыми местами вместо снимков.
    want = min(len(c.get("photos") or []), MAX_PHOTOS)
    if len(photos) < want:
        raise Skip("на диске %d фотографий из %d -- скачивание оборвалось" % (len(photos), want))
    key, why, place, moved = resolve(c, text, city, ctx, exclude)

    pv = price if cur == "VND" else int(round(price * ctx.rate(cur)))
    place_w = it.words(place or "")
    # Ни улицы, ни комплекса, ни площади -- строка получается «Студия, Tây Hồ»:
    # посетителю она не говорит ничего, а проверка повторов на ней слепа. 12
    # сентября так завелись две неотличимые студии за 6 млн из одной группы.
    baths = it.baths_in(text)
    if not place_w and not area and not beds and not baths:
        raise Skip("ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы "
                   "«Студия, район» и ни о чём не говорила")
    dup = it.duplicate({"city": city, "type": typ, "beds": beds, "area": area, "cat": None,
                        "block": None}, key, pv, place_w, ctx, exclude)
    if dup:
        raise Skip("похоже на уже заведённое: id %s" % dup["id"])

    dname = ctx.district_label(city, key)
    ru, en = describe(typ, beds, baths, area, place, dname)
    notice, notice_en = NOTICE_RU, NOTICE_EN
    if moved:
        notice, notice_en = notice + it.HOW_RU["moved"], notice_en + it.HOW_EN["moved"]
    elif "street" in why:
        notice, notice_en = notice + it.HOW_RU["street"], notice_en + it.HOW_EN["street"]
    elif set(why) == {"precedent"}:
        notice, notice_en = notice + it.HOW_RU["precedent"], notice_en + it.HOW_EN["precedent"]
    details = {"photos": photos, "notice": notice, "noticeEn": notice_en}
    return {"key": "%s/%s" % (c.get("group_id") or "fb", c.get("post_id")), "url": c["url"],
            "city": city, "district": key, "type": typ, "price": price, "cur": cur, "pv": pv,
            "area": area, "beds": beds, "ru": ru, "en": en, "details": details, "hash": h,
            "source": SOURCE_BY_MODE.get(c.get("kind"), "fbgroup"),
            "why": "; ".join(why[k] for k in ("ward", "district", "street", "precedent") if k in why)}


# ----------------------------------------------------------------- контекст --

class Ctx(it.Ctx):
    """Тот же контекст, что у телеграмного заведения (строки сайта, районы,
    границы, улицы Дананга), плюс свои соответствия кварталов и своя память о
    заведённых постах: ключ у Facebook -- ссылка на пост и текст, номеров
    каталога агентства здесь не бывает."""

    def __init__(self, today):
        super().__init__(today)
        for city, extra in FB_ALIASES.items():
            self.ward_words.setdefault(city, {}).update(extra)
        # Слова ОПИСАНИЯ строки, отдельно от it.Ctx._words, куда подмешана ещё
        # и ссылка. Зачем разделять -- см. desc_hits.
        for rows in self.by_city.values():
            for l in rows:
                l["_dwords"] = it.words((l.get("desc") or "") + " " + (l.get("descEn") or ""))
        self.state = load_state()
        self.forgotten = prune_state(self.state, self.site, today)
        self.by_hash = {}
        for e in self.state["posts"].values():
            if e.get("id") is not None and e.get("hash"):
                self.by_hash[e["hash"]] = e["id"]
        self.cat_of = {}
        self._rates = None

    def rate(self, cur):
        """Сколько донгов в единице валюты -- по курсам самого сайта."""
        if self._rates is None:
            from site_data import load_data
            per = load_data()["RATES"]["perUsd"]
            self._rates = {c: per["VND"] / v for c, v in per.items() if v}
        return self._rates.get(cur, 1)

    def remember(self, r):
        pseudo = {"id": "new:" + r["key"], "city": r["city"], "district": r["district"],
                  "type": r["type"], "area": r["area"], "pv": r["pv"], "_beds": r["beds"],
                  "_words": it.words(r["ru"] + " " + r["en"]),
                  "_dwords": it.words(r["ru"] + " " + r["en"]), "_new": True}
        self.by_city[r["city"]].append(pseudo)
        self.urls[it.norm_url(r["url"])] = pseudo["id"]
        if r["hash"]:
            self.by_hash[r["hash"]] = pseudo["id"]


def load_state():
    try:
        s = json.load(open(STATE, encoding="utf-8"))
    except FileNotFoundError:
        s = {}
    s.setdefault("posts", {})
    return s


# Сколько дней помнить пост, чьей строки на сайте уже не видно. Ноль ставить
# нельзя: заведённая строка попадает в rebuild_final.py сразу, а в
# vietnam-rent-finder.html, откуда Ctx читает сайт, -- только после сборки, а
# сборку с 11 сентября делает сервер. Забыв запись в тот же день, следующий
# прогон завёл бы тот же пост второй раз.
STATE_GRACE_DAYS = 3


def prune_state(state, site, today):
    """Забыть посты, чьих строк на сайте больше нет. Возвращает забытые ссылки.

    ЗАЧЕМ. purge_old_listings.py снимает строки старше 14 дней, а запись в
    состоянии оставалась навсегда. Тот же объект, выложенный заново через
    месяц, молча не заводился -- «тот же текст уже заведён: id 3000123», -- и
    номер в этом отказе указывал на строку, которой давно нет."""
    gone = []
    for url, e in sorted(state["posts"].items()):
        if e.get("id") is None or e["id"] in site:
            continue
        try:
            age = (today - datetime.date.fromisoformat(e.get("checked") or "")).days
        except ValueError:
            continue          # записи без даты не трогаем: гадать не о чем
        if age >= STATE_GRACE_DAYS:
            gone.append(url)
    for url in gone:
        del state["posts"][url]
    return gone


def save_state(state):
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(state, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    os.replace(tmp, STATE)


def candidate_files(pattern, hours):
    now = datetime.datetime.now().timestamp()
    return [f for f in sorted(glob.glob(pattern)) if os.path.getmtime(f) >= now - hours * 3600]


# ------------------------------------------------------------------ партия --

HEADER = '''# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: %(n)s, %(date)s.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
%(accepted)s

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (%(nskip)d):
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


def write_batch(accepted, skipped, ids, today):
    j = lambda s: json.dumps(s, ensure_ascii=False)
    rows = []
    for i, r in zip(ids, accepted):
        rows.append('L(%d,"%s","%s","%s",%d,%s,\n  %s,\n  %s,"сегодня",0,source="%s"%s,\n'
                    '  descEn=%s,\n  details=%s),'
                    % (i, r["city"], r["district"], r["type"], r["price"],
                       r["area"] if r["area"] else "None", j(r["ru"]), j(r["url"]), r["source"],
                       "" if r["cur"] == "VND" else ',cur="%s"' % r["cur"], j(r["en"]),
                       j(r["details"])))
    acc = "\n".join("  * %s -- %s/%s, %s %s: %s"
                    % (r["key"], r["city"], r["district"], format(r["price"], ","), r["cur"], r["why"])
                    for r in accepted)
    skp = "\n".join("  * %s -- %s" % kv for kv in skipped) or "  (нет)"
    nums = [int(re.sub(r"\D", "", f) or 0) for f in glob.glob("new_listings*.py")]
    path = "new_listings%d.py" % (max(nums + [0]) + 1)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HEADER % {"n": it.ru_plural(len(rows), "строка", "строки", "строк"),
                          "date": today.isoformat(), "accepted": it.doc_safe(acc),
                          "nskip": len(skipped), "skipped": it.doc_safe(skp), "ids": ids,
                          "q": "'''", "rows": "\n".join(rows)})
    return path


def git(*args):
    return subprocess.run(["git"] + list(args), capture_output=True, text=True, encoding="utf-8")


def commit(path, accepted):
    """Коммит только своих файлов -- и только если чужой работы в них нет.

    Здесь, в отличие от сервера, репозиторий рабочий: в нём сидит сессия. Если
    rebuild_final.py уже изменён кем-то ещё, `git add` унёс бы чужую работу в
    чужой коммит. Тогда партия просто остаётся на диске."""
    photos = sorted({os.path.dirname(p) for r in accepted for p in r["details"]["photos"]})
    files = ["rebuild_final.py", path] + photos
    # Каталоги с фотографиями должны быть НЕ исключены из репозитория. Сейчас
    # они исключены (.gitignore, правило fb_photos/), и git add на исключённом
    # пути обрывается целиком: не добавляется ни фотография, ни rebuild_final,
    # ни сама партия, а следом падает git commit -- и всё это выглядело как
    # «git commit не прошёл» без единого слова о причине.
    blocked = ((git("check-ignore", "-v", "--", *photos).stdout or "").strip().splitlines())
    if blocked:
        rule, _, first = blocked[0].partition("\t")
        return ("фотографии не идут в репозиторий: %s исключён правилом %s -- партия записана, но "
                "не закоммичена, иначе сервер собрал бы карточки с пустыми местами вместо снимков"
                % (first or photos[0], rule))
    r = git("pull", "--rebase", "--quiet")
    if r.returncode:
        return "git pull --rebase не прошёл (%s) -- партия записана, но не закоммичена" % (r.stderr or "").strip()[:120]
    r = git("add", "--", *files)
    if r.returncode:
        return "git add не прошёл: %s" % ((r.stdout or "") + (r.stderr or "")).strip()[:200]
    msg = ("Facebook groups: %s filed by the program\n\n"
           "ingest_facebook.py read the posts fb_collect.py had collected and filed only those\n"
           "whose type, single price, photos and district all came out of the post itself.\n\n"
           "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
           % it.ru_plural(len(accepted), "строка", "строки", "строк"))
    r = git("commit", "-q", "-m", msg)
    if r.returncode:
        return "git commit не прошёл: %s" % ((r.stdout or "") + (r.stderr or "")).strip()[:160]
    r = git("push", "-q", "origin", "HEAD")
    if r.returncode:
        return "закоммичено, но push не прошёл: %s" % (r.stderr or "").strip()[:160]
    return None


def main():
    ap = argparse.ArgumentParser(description="Заведение постов из групп Facebook")
    ap.add_argument("--files", default=CAND_GLOB, help="маска файлов кандидатов fb_collect.py")
    ap.add_argument("--hours", type=float, default=FRESH_HOURS, help="брать файлы не старше стольких часов")
    ap.add_argument("--limit", type=int, default=30)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--insert", action="store_true")
    ap.add_argument("--commit", action="store_true", help="закоммитить и запушить (только на ПК)")
    a = ap.parse_args()
    os.chdir(HERE)
    sys.stdout.reconfigure(encoding="utf-8")

    files = candidate_files(a.files, a.hours)
    if not files:
        print("свежих файлов кандидатов Facebook нет (маска %s, не старше %g ч)" % (a.files, a.hours))
        return 0
    cands, seen = [], set()
    for f in files:
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            print("не читается %s: %s" % (f, e))
            continue
        if not isinstance(d, dict) or "candidates" not in d:
            # Под маску кандидатов легко попадает чужой файл: 12 сентября это
            # был мой же вывод поиска групп (_fb_group_search.json -- список, а
            # не словарь), и шаг падал целиком, ничего не заведя.
            print("пропускаю %s: это не файл кандидатов fb_collect" % f)
            continue
        for c in d.get("candidates") or []:
            u = it.norm_url(c.get("url") or "")
            if u and u not in seen:
                seen.add(u)
                cands.append(c)
    today = datetime.datetime.now(it.VN_TZ).date()
    ctx = Ctx(today)
    ctx.ad_cities = ad_cities(cands)

    accepted, skipped, unusable = [], [], 0
    for c in cands:
        try:
            r = decide(c, ctx)
        except it.Skip as e:
            skipped.append((c.get("post_id") or "?", str(e)))
            continue
        except Exception as e:
            # Один кривой кандидат не должен обрывать разбор остальных: без
            # этого за прогон не заводится вообще ничего, а причина видна
            # только в трассировке, которой никто не читает.
            skipped.append((c.get("post_id") or "?",
                            "разбор оборвался: %s: %s" % (type(e).__name__, e)))
            continue
        if r is None:
            unusable += 1
            continue
        if len(accepted) >= a.limit:
            skipped.append((r["key"], "лимит прогона (%d) выбран" % a.limit))
            continue
        accepted.append(r)
        ctx.remember(r)

    print("Facebook: файлов %d, кандидатов %d, заводится %d" % (len(files), len(cands), len(accepted)))
    if ctx.forgotten:
        print("  забыто %d записей о постах, чьих строк на сайте больше нет (сняты по возрасту): %s"
              % (len(ctx.forgotten), ", ".join(u.rsplit("/", 1)[-1] for u in ctx.forgotten[:5])))
    for r in accepted:
        print("  + %-28s %s/%-4s %-9s %12s %s  %s м²  -- %s"
              % (r["key"][:28], r["city"], r["district"], r["type"], format(r["price"], ","),
                 r["cur"], r["area"] or "?", r["why"]))
    for k, why in skipped:
        print("  - %-28s %s" % (str(k)[:28], why))
    if unusable:
        print("  без текста или из чужого города: %d" % unusable)

    if not a.write or not accepted:
        return 0
    dirty = (git("status", "--porcelain", "--", "rebuild_final.py").stdout or "").strip()
    if dirty and a.commit:
        print("rebuild_final.py уже изменён кем-то ещё -- заведение отложено, чтобы не смешать работу:")
        print("  %s" % dirty)
        return 0
    # Блок 3000000 -- это Facebook и hoppler; 2000000, который it.allocate
    # берёт по умолчанию, принадлежит Telegram. Номер сам по себе ничего не
    # ломает, но по блоку видно, чей это ряд, и обе программы не должны
    # выедать номера друг у друга.
    ids = it.allocate(len(accepted), block="3000000", owner="ingest_facebook")
    # Освобождение -- в finally на ВЕСЬ путь после резервирования. Раньше оно
    # стояло только вокруг вставки: при --write без --insert и при любом обрыве
    # записи партии номера оставались висеть в ledger'е сутки. Освобождать не
    # опасно: allocate_ids держит высшую отметку (hwm) по каждому блоку и
    # никогда не выдаёт номер повторно, даже если строка ещё не в
    # rebuild_final.py.
    try:
        path = write_batch(accepted, skipped, ids, today)
        print("\nзаписано: %s -- %d строк, id %d..%d" % (path, len(ids), ids[0], ids[-1]))
        if not a.insert:
            save_state(ctx.state)
            print("(--insert не задан: партия записана, но не вставлена)")
            return 0
        subprocess.run([sys.executable, path], check=True)
        for i, r in zip(ids, accepted):
            ctx.state["posts"][it.norm_url(r["url"])] = {"id": i, "hash": r["hash"],
                                                         "checked": today.isoformat()}
        save_state(ctx.state)
        if a.commit:
            err = commit(path, accepted)
            print(err if err else "закоммичено и запушено: %s" % path)
    finally:
        subprocess.run([sys.executable, "allocate_ids.py", "--release", "%d-%d" % (ids[0], ids[-1])])
    return 0


if __name__ == "__main__":
    sys.exit(main())
