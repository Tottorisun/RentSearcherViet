# -*- coding: utf-8 -*-
"""Автономный сборщик объявлений с hoppler.com.ph -- без модели в контуре.

ЧЕТВЁРТЫЙ источник, ставший программой, после Chợ Tốt и dotproperty. Портал
работает только по Метро Маниле, поэтому все строки попадают в город manila.

ПОЧЕМУ ЕГО УДАЛОСЬ ВЗЯТЬ. Карточка в списке несёт всё нужное сразу -- тип,
город, название дома, цену, спальни, санузлы и площадь, -- так что разбирать
приходится не вёрстку объявления, а короткий кусок текста вокруг ссылки.
Списки отсортированы по дате изменения, новые первыми, и это тоже используется:
дойдя до объявления старше порога, раздел можно бросать.

  robots.txt портала (проверен 10 сентября 2026) закрывает только /_blog/.

ДАТА -- САМОЕ СЛАБОЕ МЕСТО, и это надо знать. Портал печатает не дату
размещения, а «Last Updated». Возраст считается по ней, то есть объявление
могло быть создано заметно раньше, а обновление -- это правка агентом, а не
подтверждение, что жильё свободно. Ровно так же датированы 17 строк hoppler,
заведённых до этого скрипта, и оговорка в каждой строке говорит об этом прямо.
Даты нет в списке, только на самой карточке, поэтому за ней приходится ходить
отдельным запросом.

РАЙОН НЕ УГАДЫВАЕТСЯ. Портал делит объявления по городам Метро Манилы, и семь
из них однозначно совпадают с нашими районами (Макати, Тагиг, Пасиг и так
далее). Города, для которых однозначного ключа нет, пропускаются целиком:
  * «manila» -- это весь город Манила, а наш ключ mla -- только Малате и
    Эрмита. Приписать одно к другому значило бы соврать примерно в половине
    случаев;
  * Лас-Пиньяс и Сан-Хуан ключа не имеют вовсе.

  python collect_hoppler.py --days 30              посмотреть, что нашлось
  python collect_hoppler.py --days 30 --write      записать файл партии
  python collect_hoppler.py --days 30 --write --insert   и сразу вставить
"""
import argparse
import ast
import collections
import datetime
import glob
import html as _html
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
      "Accept-Language": "en;q=0.9"}
BASE = "https://www.hoppler.com.ph"

# Город портала -> ключ района на сайте (город у всех строк один: manila).
CITY_DISTRICT = {
    "makati": "mak", "taguig": "bgc", "pasig": "ort", "quezon-city": "qzc",
    "mandaluyong": "mdl", "muntinlupa": "alb", "paranaque": "prq",
}
# Раздел портала -> тип объекта на сайте. Участки (lots-for-rent) не жильё,
# здания целиком (buildings-for-rent) -- не то, что ищет частный арендатор.
KINDS = {
    "condominiums-for-rent": "Квартира",
    "house-and-lots-for-rent": "Дом",
    "townhouses-for-rent": "Дом",
    "office-spaces-for-rent": "Офис",
    "commercial-spaces-for-rent": "Торговая площадь",
    "warehouses-for-rent": "Склад",
}

# У карточки ДВЕ ссылки на один слаг: на картинке и на заголовке. Поля идут
# только за первой; сразу за второй начинается уже следующая карточка, и её
# данные были бы приписаны этой. Поэтому берём только ту, за которой стоит
# <img> -- это ссылка на картинке.
LINK_RE = re.compile(r'class="d-block"\s+href="/([a-z0-9\-]+-(?:rr|cr)\d{6,})"', re.I)
PRICE_RE = re.compile(r"₱\s*([\d,]+)\s*/month")
BEDS_RE = re.compile(r"(\d+)\s*Bed")
BATHS_RE = re.compile(r"(\d+)\s*Baths?")
AREA_RE = re.compile(r"([\d,]+)\s*sqm")
IMG_RE = re.compile(r'data-src="(https://[^"]+cloudfront[^"]+)"')
UPDATED_RE = re.compile(r"Last Updated\s*</?[^>]*>?\s*([A-Z][a-z]+ \d{1,2}, 20\d\d)")
OG_UPDATED_RE = re.compile(r'og:description"[^>]+content="([A-Z][a-z]{2} \d{2}, 20\d\d)')
PAGE_IMG_RE = re.compile(r'https://[a-z0-9]+\.cloudfront\.net/hoppler/properties/[^"\')\s]+')


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return None
            if i == tries - 1:
                return None
        except Exception:
            # У портала регулярно обрывается ответ на середине (IncompleteRead),
            # поэтому повтор здесь не роскошь, а обычный режим работы.
            if i == tries - 1:
                return None
        time.sleep(2 + 2 * i)
    return None


def plain(s):
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def cards(index_html):
    """[поля] по каждой карточке списка -- из текста ПОСЛЕ ссылки.

    Порядок в разметке такой: ссылка -> картинка с alt -> «Condominium • Makati
    <дом> PHP ₱ <цена> /month <N> Bed s <M> Baths <S> sqm». Поля, стоящие ПЕРЕД
    ссылкой, принадлежат предыдущей карточке -- на этом я попался 10 сентября
    2026: у garden-towers (сайт: 2BR) получалось «The Salcedo Park, 3 спальни,
    180 м²», то есть строка вышла бы полностью чужой при верной ссылке.

    Атрибут alt картинки несёт число спален отдельно («2BR Condominium for
    Rent-...»), и оно сверяется с разобранным. Расхождение означает, что окно
    опять съехало, и такая карточка отбрасывается, а не заводится молча."""
    seen, out, mismatched = set(), [], 0
    # Окно каждой карточки -- от её ссылки до следующей. Фиксированная длина не
    # годится: у карточек с длинной каруселью цена уезжает дальше девяти тысяч
    # символов, и такая карточка молча пропадала (10 из 24 на первой странице).
    spots = [(mm.group(1), mm.start()) for mm in LINK_RE.finditer(index_html)]
    for n, (slug, i) in enumerate(spots):
        if slug in seen:
            continue
        seen.add(slug)
        end = spots[n + 1][1] if n + 1 < len(spots) else len(index_html)
        raw = index_html[i:end]
        w = plain(raw)
        price = PRICE_RE.search(w)
        if not price:
            continue                      # не карточка объявления, а ссылка в подборке
        tail = w[price.end(): price.end() + 160]
        beds = BEDS_RE.search(tail)
        baths = BATHS_RE.search(tail)
        area = AREA_RE.search(tail)
        name = re.search(r"•\s*[A-Za-z ]+?\s+(.+?)\s+PHP\b", w[: price.start()] + " PHP")
        alt = re.search(r'alt="([^"]*)"', raw)
        alt_beds = re.search(r"(\d+)BR", alt.group(1)) if alt else None
        beds_n = int(beds.group(1)) if beds else None
        if alt_beds and beds_n is not None and int(alt_beds.group(1)) != beds_n:
            mismatched += 1
            continue
        out.append({
            "slug": slug,
            # Портал называет студию студией в alt картинки, а спален у неё нет.
            # Без этого она заводилась как «Квартира, 34 м²» -- тип беднее, чем
            # сказал сам источник.
            "studio": bool(alt and re.match(r"\s*Studio\b", alt.group(1), re.I)),
            "price": int(price.group(1).replace(",", "")),
            "beds": beds_n,
            "baths": int(baths.group(1)) if baths else None,
            "area": int(area.group(1).replace(",", "")) if area else None,
            "name": (name.group(1).strip() if name else ""),
        })
    if mismatched:
        print("   карточек отброшено по расхождению спален с alt: %d" % mismatched)
    return out


MONTHS = {m: i + 1 for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"])}
MONTHS_SHORT = {m[:3]: i + 1 for m, i in MONTHS.items()}


def updated_date(page_html):
    m = UPDATED_RE.search(page_html)
    if m:
        mon, day, year = re.match(r"([A-Z][a-z]+) (\d{1,2}), (20\d\d)", m.group(1)).groups()
        if mon in MONTHS:
            return datetime.date(int(year), MONTHS[mon], int(day))
    m = OG_UPDATED_RE.search(page_html)
    if m:
        mon, day, year = re.match(r"([A-Z][a-z]{2}) (\d{2}), (20\d\d)", m.group(1)).groups()
        if mon in MONTHS_SHORT:
            return datetime.date(int(year), MONTHS_SHORT[mon], int(day))
    return None


def site_district_names():
    src = open("rebuild_final.py", encoding="utf-8").read()
    node = next(n for n in ast.walk(ast.parse(src))
                if isinstance(n, ast.Assign) and any(getattr(t, "id", None) == "CITIES" for t in n.targets))
    cities = ast.literal_eval(node.value)
    return {d["key"]: d["name"] for d in cities["manila"]["districts"]}


def ru_plural(n, one, few, many):
    a = abs(n)
    if a % 10 == 1 and a % 100 != 11:
        return "%d %s" % (n, one)
    if 2 <= a % 10 <= 4 and not 12 <= a % 100 <= 14:
        return "%d %s" % (n, few)
    return "%d %s" % (n, many)


def describe(c, type_ru, district_name):
    """Описание из ПОЛЕЙ карточки. Рекламный текст объявления не пересказан."""
    head_en = {"Квартира": "flat", "Студия": "studio", "Дом": "house", "Офис": "office",
               "Торговая площадь": "retail space", "Склад": "warehouse"}[type_ru]
    if c["beds"] and type_ru in ("Квартира", "Дом"):
        ru = "%d-спальн%s %s" % (c["beds"], "ая" if type_ru == "Квартира" else "ый", type_ru.lower())
        en = "%d-bedroom %s" % (c["beds"], head_en)
    else:
        ru, en = type_ru, head_en.capitalize()
    parts_ru, parts_en = [ru[0].upper() + ru[1:]], [en[0].upper() + en[1:]]
    if c["area"]:
        parts_ru.append("%d м²" % c["area"])
        parts_en.append("%d m²" % c["area"])
    place = ", ".join(x for x in (c["name"], district_name) if x)
    parts_ru.append(place)
    parts_en.append(place)
    tail_ru = [ru_plural(c["baths"], "санузел", "санузла", "санузлов")] if c["baths"] else []
    tail_en = ["%d bathroom%s" % (c["baths"], "" if c["baths"] == 1 else "s")] if c["baths"] else []
    return (", ".join(parts_ru) + (" — " + ", ".join(tail_ru) + "." if tail_ru else "."),
            ", ".join(parts_en) + (" — " + ", ".join(tail_en) + "." if tail_en else "."))


NOTICE_RU = ("Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, "
             "санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. "
             "hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст "
             "считается по ней, и объявление могло быть создано раньше.")
NOTICE_EN = ("This description was assembled by a program from the listing card on hoppler.com.ph — "
             "type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is "
             "not retold. Hoppler publishes a last-updated date rather than a posting date: the age "
             "is counted from it, and the listing may have been created earlier.")

HEADER = '''# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: %d объявлений, %s.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше %d дней.
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


def posted_label(n):
    src = open("rebuild_final.py", encoding="utf-8").read()
    fn = next(x for x in ast.walk(ast.parse(src))
              if isinstance(x, ast.FunctionDef) and x.name == "_ru_days_label")
    ns = {}
    exec(ast.unparse(fn), ns)
    return ns["_ru_days_label"](n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=float, default=30.0, help="не старше стольких дней по дате изменения")
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--pages", type=int, default=3)
    ap.add_argument("--delay", type=float, default=0.6)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--insert", action="store_true")
    a = ap.parse_args()

    from site_data import load_listings
    known = {l["url"].split("?")[0].rstrip("/") for l in load_listings()}
    dnames = site_district_names()
    today = datetime.date.today()
    picked, skipped = [], collections.Counter()

    # ПЕРВЫЙ ПРОХОД -- только списки: они дешёвы, и по ним ещё не видно даты.
    sections, seen_slugs = collections.OrderedDict(), set()
    for city_slug, dkey in CITY_DISTRICT.items():
        for kind, type_ru in KINDS.items():
            queue = []
            for page in range(1, a.pages + 1):
                u = "%s/%s/%s%s" % (BASE, kind, city_slug, "" if page == 1 else "?page=%d" % page)
                idx = get(u)
                time.sleep(a.delay)
                if not idx:
                    continue
                for c in cards(idx):
                    url = "%s/%s" % (BASE, c["slug"])
                    if url in known:
                        skipped["уже есть"] += 1
                        continue
                    if c["slug"] in seen_slugs:
                        # Одно и то же объявление попадается на соседних
                        # страницах, когда выдача сдвигается между запросами.
                        skipped["дубль в выдаче"] += 1
                        continue
                    seen_slugs.add(c["slug"])
                    queue.append((c, url, dkey, type_ru))
            if queue:
                sections[(city_slug, kind)] = queue
    print("кандидатов со списков: %d" % sum(len(q) for q in sections.values()))

    # ВТОРОЙ ПРОХОД -- за датами, ПО КРУГУ ГОРОДОВ, по карточке за оборот.
    #
    # ЗАЧЕМ КРУГ. Раньше лимит тратился прямо в обходе, город за городом, и
    # первый же город выбирал его целиком: 10 сентября 2026 в партии из 40
    # строк все 40 оказались из Макати, и так было бы каждый раз -- шесть
    # остальных городов не попали бы на сайт никогда. Круг тратит лимит
    # поровну, а порядок внутри города сохраняется, поэтому берутся всё равно
    # самые свежие объявления города.
    pos = {k: 0 for k in sections}
    order = [c for c in CITY_DISTRICT if any(k[0] == c for k in sections)]
    while order and len(picked) < a.limit:
        for city_slug in list(order):
            if len(picked) >= a.limit:
                break
            live = [k for k in sections if k[0] == city_slug and pos[k] < len(sections[k])]
            if not live:
                order.remove(city_slug)
                continue
            key = live[0]
            c, url, dkey, type_ru = sections[key][pos[key]]
            pos[key] += 1
            page_html = get(url)
            time.sleep(a.delay)
            if not page_html:
                skipped["страница не открылась"] += 1
                continue
            d = updated_date(page_html)
            if not d:
                skipped["нет даты"] += 1
                continue
            age = (today - d).days
            if age > a.days:
                # Список отсортирован по дате изменения, новые первыми,
                # поэтому дальше в этом разделе только старее.
                skipped["старое"] += 1
                pos[key] = len(sections[key])
                continue
            photos = []
            for p in PAGE_IMG_RE.findall(page_html):
                if p not in photos:
                    photos.append(p)
            if not photos:
                skipped["без фото"] += 1
                continue
            c["photos"] = photos[:6]
            t = "Студия" if (c.get("studio") and type_ru == "Квартира") else type_ru
            picked.append((dkey, t, c, max(0, age), url))
    left = sum(len(q) - pos[k] for k, q in sections.items())
    if left:
        skipped["не дошли, лимит выбран"] = left

    picked.sort(key=lambda p: p[3])
    print("найдено пригодных: %d (не старше %.0f дн. по дате изменения)" % (len(picked), a.days))
    print("пропущено:", ", ".join("%s %d" % kv for kv in skipped.most_common()) or "ничего")
    print("по районам:", ", ".join("%s %d" % kv for kv in collections.Counter(p[0] for p in picked).most_common()) or "—")
    for dkey, type_ru, c, age, _u in picked[:12]:
        print("  %-4s %-16s %2d дн. %9s ₱  %s" % (dkey, type_ru, age, format(c["price"], ","), c["name"][:44]))

    if not a.write or not picked:
        return 0

    out = subprocess.run([sys.executable, "allocate_ids.py", "--block", "3000000",
                          "--count", str(len(picked)), "--owner", "collect_hoppler"],
                         capture_output=True, text=True, encoding="utf-8")
    m = re.search(r"FIRST=(\d+) LAST=(\d+)", out.stdout or "")
    if not m:
        sys.exit("не удалось зарезервировать id:\n%s%s" % (out.stdout, out.stderr))
    first, last = int(m.group(1)), int(m.group(2))
    ids = list(range(first, last + 1))

    rows = []
    j = lambda s: json.dumps(s, ensure_ascii=False)
    for n, (dkey, type_ru, c, age, url) in enumerate(picked):
        ru, en = describe(c, type_ru, dnames.get(dkey, ""))
        det = {"photos": c["photos"], "notice": "RU_N", "noticeEn": "EN_N"}
        rows.append('L(%d,"manila","%s","%s",%d,%s,\n  %s,\n  %s,%s,%d,source="hoppler",cur="PHP",\n'
                    '  descEn=%s,\n  details=%s),'
                    % (ids[n], dkey, type_ru, c["price"], c["area"] if c["area"] else "None",
                       j(ru), j(url), j(posted_label(age)), age, j(en),
                       json.dumps(det, ensure_ascii=False)))

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


if __name__ == "__main__":
    sys.exit(main())
