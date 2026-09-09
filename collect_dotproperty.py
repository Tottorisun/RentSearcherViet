# -*- coding: utf-8 -*-
"""Автономный сборщик объявлений с dotproperty.com.ph -- без модели в контуре.

ЗАЧЕМ. После collect_chotot.py программой стал главный вьетнамский источник, а
все филиппинские строки по-прежнему заводились руками. dotproperty оказался
пригоден для программы: страницы отдаются обычным запросом (batdongsan.com.vn
для сравнения отвечает 403 даже на robots.txt), а на каждой карточке лежит
schema.org-разметка ld+json со всеми нужными полями -- спальни, санузлы,
площадь, цена, локальность. Разбирать вёрстку не требуется.

robots.txt портала (проверен 9 сентября 2026) закрывает панели, формы запроса и
блог; страницы объявлений открыты.

КАК СТАВИТСЯ РАЙОН -- тремя способами, в порядке убывания надёжности:
  1. локальность из ld+json точно совпадает с названием района в CITIES;
  2. прецедент: та же локальность уже заведена на сайте под одним и тем же
     ключом. Таблица строится ПРИ ЗАПУСКЕ из самих строк сайта, а не пишется
     руками, поэтому она растёт вместе с данными и ничего не выдумывает.
     Локальность, заведённая под ДВУМЯ разными ключами, считается
     неоднозначной и не используется;
  3. никак -- строка не заводится и попадает в счёт пропущенных.

ОГОВОРКА, КОТОРУЮ ВАЖНО ЗНАТЬ. Локальность портала иногда расходится с адресом
в тексте объявления. На сайте есть две такие строки: 3000016 лежит под слагом
candau-ay, а в объявлении адрес «E.J. Blanco Avenue, ECCA Homes, Пиапи», и
3000017 -- наоборот. Тогда сессия пошла за текстом. Программа так не умеет: она
берёт структурное поле портала и прямо говорит об этом в оговорке строки.

ДАТА. Портал не публикует дату размещения, но идентификатор записи -- UUIDv7, а
в нём первые 48 бит это время создания в миллисекундах. Возраст выводится
оттуда и означает «не моложе». Ровно так же датированы 99 строк, заведённых до
этого скрипта.

  python collect_dotproperty.py --days 14              посмотреть, что нашлось
  python collect_dotproperty.py --days 14 --write      записать файл партии
  python collect_dotproperty.py --days 14 --write --insert  и сразу вставить
"""
import argparse
import ast
import collections
import datetime
import glob
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
      "Accept-Language": "en;q=0.9"}
BASE = "https://www.dotproperty.com.ph"

# (город сайта, кусок адреса на портале)
TARGETS = [("cebu", "cebu"), ("manila", "metro-manila"), ("dumaguete", "negros-oriental")]
# Раздел портала -> тип объекта на сайте.
KINDS = {"apartments-for-rent": "Квартира", "condos-for-rent": "Квартира",
         "houses-for-rent": "Дом", "townhouses-for-rent": "Дом"}

ADS_RE = re.compile(r'/ads/([a-z0-9\-%]+_[0-9a-f]{8,}(?:-[0-9a-f]{2,})*)')
LD_RE = re.compile(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', re.S)
IMG_RE = re.compile(r'https://pix\.dotproperty\.co\.th/[A-Za-z0-9+/=]{40,}')
# «... listing #<uuid> in <Локальность>, <Город> with 1 bedroom, 1 bathroom, 55 sq.m. price at ₱ 50,000»
DESC_RE = re.compile(r"listing #([0-9a-f\-]{30,40}) in (.+?), ([^,]+?) with (.+)$")
BEDS_RE = re.compile(r"(\d+)\s+bedrooms?")
BATHS_RE = re.compile(r"(\d+)\s+bathrooms?")
AREA_RE = re.compile(r"([\d.,]+)\s*sq\.?m")


def slugify(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=35) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return None
            if i == tries - 1:
                return None
        except Exception:
            if i == tries - 1:
                return None
        time.sleep(2 + 2 * i)
    return None


def site_districts():
    """{(город, slug названия района): ключ} -- прямо из CITIES."""
    src = open("rebuild_final.py", encoding="utf-8").read()
    node = next(n for n in ast.walk(ast.parse(src))
                if isinstance(n, ast.Assign) and any(getattr(t, "id", None) == "CITIES" for t in n.targets))
    cities = ast.literal_eval(node.value)
    out = {}
    for city, c in cities.items():
        for d in c["districts"]:
            out[(city, slugify(d["name"]))] = d["key"]
    return out


def precedent_map(listings):
    """{(город, slug локальности): ключ} по уже заведённым строкам dotproperty.

    Локальность берётся из адреса строки: в нём она стоит между `for-rent-in-`
    и хвостом города. Если одна и та же локальность заведена под разными
    ключами -- прецедента нет, такие в таблицу не попадают."""
    seen = collections.defaultdict(collections.Counter)
    for l in listings:
        if l.get("source") != "dotproperty":
            continue
        m = re.search(r"/ads/(.+?)_[0-9a-f]{8}", l.get("url", ""))
        if not m:
            continue
        q = re.search(r"for-rent-in-(.+)$", urllib.parse.unquote(m.group(1)))
        if not q:
            continue
        loc = q.group(1)
        for _city, tail in TARGETS:
            if loc.endswith("-" + tail):
                loc = loc[: -len(tail) - 1]
        seen[(l["city"], slugify(loc))][l["district"]] += 1
    return {k: c.most_common(1)[0][0] for k, c in seen.items() if len(c) == 1}


def uuid7_age_days(uuid, today):
    """UUIDv7 несёт время создания в первых 48 битах (миллисекунды)."""
    try:
        ms = int(uuid.replace("-", "")[:12], 16)
        d = datetime.datetime.fromtimestamp(ms / 1000, datetime.UTC).date()
    except Exception:
        return None
    age = (today - d).days
    return age if 0 <= age < 3650 else None


def parse_ad(html):
    m = LD_RE.search(html)
    if not m:
        return None
    try:
        d = json.loads(m.group(1))
    except Exception:
        return None
    q = DESC_RE.search(d.get("description", ""))
    if not q:
        return None
    uuid, locality, city_name, tail = q.group(1), q.group(2).strip(), q.group(3).strip(), q.group(4)
    try:
        price = int(float(d["offers"]["priceSpecification"]["price"]))
    except Exception:
        price = 0
    beds = BEDS_RE.search(tail)
    baths = BATHS_RE.search(tail)
    area = AREA_RE.search(tail)
    return {
        "uuid": uuid, "locality": locality, "city_name": city_name, "price": price,
        "beds": int(beds.group(1)) if beds else None,
        "baths": int(baths.group(1)) if baths else None,
        "area": int(float(area.group(1).replace(",", ""))) if area else None,
        "photos": sorted(set(IMG_RE.findall(html)))[:6],
        "name": d.get("name", ""),
    }


def ru_plural(n, one, few, many):
    a = abs(n)
    if a % 10 == 1 and a % 100 != 11:
        return "%d %s" % (n, one)
    if 2 <= a % 10 <= 4 and not 12 <= a % 100 <= 14:
        return "%d %s" % (n, few)
    return "%d %s" % (n, many)


CITY_RU = {"cebu": "Себу", "manila": "Манила", "dumaguete": "Думагете"}


def describe(ad, type_ru, city):
    """Описание из ПОЛЕЙ разметки. Рекламный текст объявления не пересказан."""
    head_en = {"Квартира": "flat", "Дом": "house"}[type_ru]
    if ad["beds"]:
        ru = "%d-спальн%s %s" % (ad["beds"], "ая" if type_ru == "Квартира" else "ый", type_ru.lower())
        en = "%d-bedroom %s" % (ad["beds"], head_en)
    else:
        ru, en = type_ru, head_en.capitalize()
    parts_ru, parts_en = [ru[0].upper() + ru[1:]], [en[0].upper() + en[1:]]
    if ad["area"]:
        parts_ru.append("%d м²" % ad["area"])
        parts_en.append("%d m²" % ad["area"])
    parts_ru.append("%s, %s" % (ad["locality"], CITY_RU[city]))
    parts_en.append("%s, %s" % (ad["locality"], ad["city_name"]))
    tail_ru = [ru_plural(ad["baths"], "санузел", "санузла", "санузлов")] if ad["baths"] else []
    tail_en = ["%d bathroom%s" % (ad["baths"], "" if ad["baths"] == 1 else "s")] if ad["baths"] else []
    return (", ".join(parts_ru) + (" — " + ", ".join(tail_ru) + "." if tail_ru else "."),
            ", ".join(parts_en) + (" — " + ", ".join(tail_en) + "." if tail_en else "."))


NOTICE_RU = ("Описание собрано программой из разметки объявления на dotproperty.com.ph — тип, "
             "спальни, санузлы, площадь, локальность и цена. Рекламный текст объявления не "
             "пересказан. Район поставлен по локальности из той же разметки; она изредка расходится "
             "с адресом в тексте объявления, поэтому адрес стоит сверить по ссылке. Дату размещения "
             "портал не публикует: возраст выведен из идентификатора записи (UUIDv7 хранит время "
             "создания) и означает «не моложе».")
NOTICE_EN = ("This description was assembled by a program from the ad's own schema.org markup on "
             "dotproperty.com.ph — type, bedrooms, bathrooms, size, locality and price. The ad's "
             "marketing text is not retold. The district comes from the locality in that same "
             "markup, which occasionally disagrees with the address written in the ad, so check the "
             "address at the source. The portal publishes no posting date: the age is derived from "
             "the record id (a UUIDv7 carries its creation time) and means 'no newer than'.")

HEADER = '''# -*- coding: utf-8 -*-
"""dotproperty.com.ph, автоматический сбор: %d объявлений, %s.

Партию собрал collect_dotproperty.py -- без модели в контуре. Район взят из
разметки объявления (точное совпадение с CITIES либо однозначный прецедент на
сайте), описание собрано из полей разметки, возраст выведен из UUIDv7 в
идентификаторе записи и не превышает %d дней.

Объявления, локальность которых не совпала ни с одним нашим районом и не имеет
однозначного прецедента, пропущены, а не приписаны к соседнему.
"""
from listing_lock import insert_listings

IDS = %r

N_RU = %s
N_EN = %s

NEW_SRC = r%s
%s
%s

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=float, default=14.0, help="брать записи не старше стольких дней")
    ap.add_argument("--limit", type=int, default=60, help="максимум строк за прогон")
    ap.add_argument("--pages", type=int, default=3, help="страниц списка на раздел")
    ap.add_argument("--delay", type=float, default=0.6)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--insert", action="store_true")
    a = ap.parse_args()

    from site_data import load_listings
    listings = load_listings()
    districts = site_districts()
    precedent = precedent_map(listings)
    known = {l["url"].split("?")[0].rstrip("/") for l in listings}
    print("прецедентов локальностей: %d" % len(precedent))

    today = datetime.date.today()
    picked, skipped = [], collections.Counter()
    seen_slugs = set()

    for city, city_slug in TARGETS:
        for kind, type_ru in KINDS.items():
            for page in range(1, a.pages + 1):
                u = "%s/%s/%s%s" % (BASE, kind, city_slug, "" if page == 1 else "?page=%d" % page)
                html = get(u)
                time.sleep(a.delay)
                if not html:
                    continue
                for slug in ADS_RE.findall(html):
                    if slug in seen_slugs:
                        continue
                    seen_slugs.add(slug)
                    url = "%s/ads/%s" % (BASE, slug)
                    if url in known:
                        skipped["уже есть"] += 1
                        continue
                    if len(picked) >= a.limit:
                        skipped["сверх лимита"] += 1
                        continue
                    page_html = get(url)
                    time.sleep(a.delay)
                    if not page_html:
                        skipped["страница не открылась"] += 1
                        continue
                    ad = parse_ad(page_html)
                    if not ad:
                        skipped["нет разметки"] += 1
                        continue
                    age = uuid7_age_days(ad["uuid"], today)
                    if age is None or age > a.days:
                        skipped["старое"] += 1
                        continue
                    if not ad["price"]:
                        skipped["без цены"] += 1
                        continue
                    if not ad["photos"]:
                        skipped["без фото"] += 1
                        continue
                    loc = slugify(ad["locality"])
                    key = districts.get((city, loc)) or precedent.get((city, loc))
                    if not key:
                        skipped["чужой район"] += 1
                        continue
                    picked.append((city, key, type_ru, ad, age, url))

    picked.sort(key=lambda p: p[4])
    print("найдено пригодных: %d (не старше %.0f дн.)" % (len(picked), a.days))
    print("пропущено:", ", ".join("%s %d" % (k, v) for k, v in skipped.items() if v) or "ничего")
    by_city = collections.Counter(p[0] for p in picked)
    print("по городам:", ", ".join("%s %d" % kv for kv in by_city.most_common()) or "—")
    for city, key, type_ru, ad, age, url in picked[:12]:
        print("  %-4s %-9s %2d дн. %8s ₱  %s" % (key, type_ru, age, format(ad["price"], ","), ad["name"][:52]))

    if not a.write or not picked:
        print("\n(--write не задан либо нечего писать)" if not picked or not a.write else "")
        return 0

    out = subprocess.run([sys.executable, "allocate_ids.py", "--block", "3000000",
                          "--count", str(len(picked)), "--owner", "collect_dotproperty"],
                         capture_output=True, text=True, encoding="utf-8")
    m = re.search(r"FIRST=(\d+) LAST=(\d+)", out.stdout or "")
    if not m:
        sys.exit("не удалось зарезервировать id:\n%s%s" % (out.stdout, out.stderr))
    first, last = int(m.group(1)), int(m.group(2))
    ids = list(range(first, last + 1))

    rows = []
    for n, (city, key, type_ru, ad, age, url) in enumerate(picked):
        ru, en = describe(ad, type_ru, city)
        det = {"photos": ad["photos"], "notice": "RU_N", "noticeEn": "EN_N"}
        j = lambda s: json.dumps(s, ensure_ascii=False)
        rows.append('L(%d,"%s","%s","%s",%d,%s,\n  %s,\n  %s,%s,%d,source="dotproperty",cur="PHP",\n'
                    '  descEn=%s,\n  details=%s),'
                    % (ids[n], city, key, type_ru, ad["price"],
                       ad["area"] if ad["area"] else "None", j(ru), j(url),
                       j(posted_label(age)), age, j(en), json.dumps(det, ensure_ascii=False)))

    nums = [int(re.sub(r"\D", "", f) or 0) for f in glob.glob("new_listings*.py")]
    path = "new_listings%d.py" % (max(nums + [0]) + 1)
    q = "'''"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HEADER % (len(rows), today.isoformat(), int(a.days), ids,
                          json.dumps(NOTICE_RU, ensure_ascii=False),
                          json.dumps(NOTICE_EN, ensure_ascii=False),
                          q, "\n".join(rows), q))
    print("\nзаписано: %s -- %d строк, id %d..%d" % (path, len(rows), first, last))

    print("\n-- check_repost.py, справочно (на машинных описаниях он шумит):")
    subprocess.run([sys.executable, "check_repost.py", "--file", path])
    if not a.insert:
        print("\n(--insert не задан: партия записана, но не вставлена)")
        return 0
    subprocess.run([sys.executable, path], check=True)
    subprocess.run([sys.executable, "allocate_ids.py", "--release", "%d-%d" % (first, last)], check=True)
    return 0


def posted_label(n):
    """Та же функция, что и у сборки: посты и daysAgo обязаны совпадать."""
    src = open("rebuild_final.py", encoding="utf-8").read()
    fn = next(x for x in ast.walk(ast.parse(src))
              if isinstance(x, ast.FunctionDef) and x.name == "_ru_days_label")
    ns = {}
    exec(ast.unparse(fn), ns)
    return ns["_ru_days_label"](n)


if __name__ == "__main__":
    sys.exit(main())
