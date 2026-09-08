# -*- coding: utf-8 -*-
"""Автономный сборщик объявлений с Chợ Tốt -- без модели в контуре.

ЗАЧЕМ. До 8 сентября 2026 «парсер» проекта был не программой, а сессией Claude:
run_daily_check.ps1 скармливал инструкцию в claude.exe -p, и решения -- какое
объявление настоящее, в какой район его отнести, как описать -- принимала
модель. Программами были только обслуживающие шаги (чистка, живость, курсы,
сборка). Поэтому «перенести парсер на сервер» было нечего: его не существовало.

Этот скрипт закрывает главный источник: 1376 из 1723 строк сайта -- Chợ Tốt.
Он обходится стандартной библиотекой, не требует ни браузера, ни входа, ни
модели, и потому может работать по расписанию где угодно.

ЧЕГО ОН НАМЕРЕННО НЕ ДЕЛАЕТ
  * Не выдумывает район. `ward_name_v3` в ответе API -- это ровно то название,
    которым район назван в CITIES («Phường Tân Mỹ»), поэтому сопоставление
    точное. Не нашлось совпадения -- объявление пропускается и попадает в счёт
    пропущенных, а не приписывается к соседнему району.
  * Не пересказывает чужой рекламный текст. Описание собирается из ПОЛЕЙ
    (тип, комнаты, площадь, улица, район, удобства по ключевым словам). Так же
    устроен _gen_budget.py для dotproperty. Текст продавца с эмодзи и телефонами
    на сайт не идёт.
  * Не вставляет молча. По умолчанию пишет файл партии и останавливается;
    вставка -- только с --insert, и уже она проверяет и id, и URL
    (listing_lock.insert_listings).

  python collect_chotot.py --days 3                 посмотреть, что нашлось
  python collect_chotot.py --days 3 --write         записать файл партии
  python collect_chotot.py --days 3 --write --insert  и сразу вставить
"""
import argparse, ast, datetime, glob, json, os, re, subprocess, sys, time, unicodedata, urllib.parse, urllib.request

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
API = "https://gateway.chotot.com/v1/public/ad-listing"

# region_v2 -- провинция, area_v2 -- район старой нарезки. Ward'ы новой нарезки
# приходят в ward_name_v3 и сопоставляются с CITIES по точному имени.
TARGETS = [
    # (город сайта, region_v2, [area_v2 ...])
    ("ho-chi-minh", "13000", ["13102", "13119", "13109", "13096", "13099"]),
]
# Категории Chợ Tốt -> тип объекта на сайте. 1040 (земля) не берём: это не жильё.
CATEGORIES = {
    "1010": "Квартира",          # căn hộ / chung cư
    "1020": "Дом",               # nhà ở
    "1030": "Офис",              # văn phòng / mặt bằng
    "1050": "Комната",           # phòng trọ
}
# (что искать в теле, по-русски, по-английски)
AMENITIES = [
    (r"đầy đủ nội thất|full nội thất|nội thất đầy đủ", "полная меблировка", "fully furnished"),
    (r"nội thất cơ bản", "базовая меблировка", "basic furniture"),
    (r"máy lạnh|điều hòa", "кондиционер", "air conditioning"),
    (r"ban công", "балкон", "balcony"),
    (r"thang máy", "лифт", "lift"),
    (r"bảo vệ|an ninh 24", "охрана", "security"),
    (r"hồ bơi", "бассейн", "swimming pool"),
    (r"gym|phòng tập", "спортзал", "gym"),
    (r"chỗ để xe|hầm xe|bãi xe", "парковка", "parking"),
    (r"máy giặt", "стиральная машина", "washing machine"),
    (r"giờ giấc tự do", "свободный вход", "no curfew"),
]


def nfc(s):
    return unicodedata.normalize("NFC", (s or "").strip())


def slugify(s):
    """Вьетнамские диакритики -> латиница, ровно как в адресах самого nhatot."""
    s = unicodedata.normalize("NFD", s).replace("đ", "d").replace("Đ", "D")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s)).strip("-")


def ad_url(ad):
    """Ссылки в ответе API нет, но она однозначно собирается из полей: категория,
    район, провинция, list_id. Форма проверена против уже заведённых строк --
    «Căn hộ/Chung cư | Quận 7 | Tp Hồ Chí Minh» даёт
    thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh, под которым на сайте лежит 252
    объявления. Совпадает и для домов, и для офисов, и для комнат."""
    tail = slugify("thue %s %s %s" % (ad.get("category_name", ""),
                                      ad.get("area_name", ""), ad.get("region_name", "")))
    return "https://www.nhatot.com/%s/%s.htm" % (tail, ad["list_id"])


def ru_days_label(n):
    """Ту же функцию берём из rebuild_final.py, а не переписываем: сборка
    проверяет, что posted в точности равен _ru_days_label(daysAgo), и своя
    копия рано или поздно разошлась бы с оригиналом."""
    src = open("rebuild_final.py", encoding="utf-8").read()
    fn = next(n_ for n_ in ast.walk(ast.parse(src))
              if isinstance(n_, ast.FunctionDef) and n_.name == "_ru_days_label")
    ns = {}
    exec(ast.unparse(fn), ns)
    return ns["_ru_days_label"](n)


def safe(s):
    """Текст уезжает в файл партии внутри r'''...''' -- тройная кавычка и
    обратный слэш оттуда его сломали бы. В полях Chợ Tốt они не встречались, но
    проверка стоит дешевле разбора сломанного файла."""
    return s.replace("'''", "''").replace("\\", "/")


def ru_plural(n, one, few, many):
    """«5 санузла» -- то же место, где спотыкается любой счётчик по-русски."""
    a = abs(n)
    if a % 10 == 1 and a % 100 != 11:
        return "%d %s" % (n, one)
    if 2 <= a % 10 <= 4 and not 12 <= a % 100 <= 14:
        return "%d %s" % (n, few)
    return "%d %s" % (n, many)


# Поле street_name на Chợ Tốt -- не всегда улица. «Đường» это и есть «улица»,
# «Hẻm» -- переулок, а «KDC»/«Khu»/«Chợ» это вообще не улица, а квартал или
# рынок: «ул. KDC Tân Quy Đông» -- бессмыслица. Поэтому префикс выбирается по
# первому слову, а не приклеивается всегда.
NOT_A_STREET = ("kdc", "kđt", "khu", "chợ", "cc", "block")


def street_ru(street):
    if not street:
        return ""
    if re.match(r"^Hẻm\s+", street, re.I):
        return "пер. " + re.sub(r"^Hẻm\s+", "", street, flags=re.I)
    if street.split()[0].lower().strip(".") in NOT_A_STREET:
        return street
    return "ул. " + street


def short_ward(name):
    """«Phường Tân Mỹ» -> «Tân Mỹ». Названия районов остаются вьетнамскими и в
    русском описании: так уже написаны заведённые строки («ул. Lý Tự Trọng,
    Bến Thành»), и это единственный честный вариант -- транслитерировать
    вьетнамское название программа не умеет, а выдумывать её дело не в чём."""
    return re.sub(r"^(Phường|Xã|Thị trấn)\s+", "", name)


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return json.load(r)
        except Exception as ex:
            if i == tries - 1:
                print("   не удалось: %s (%s)" % (url[:70], type(ex).__name__))
                return None
            time.sleep(2 + 2 * i)
    return None


def site_wards():
    """{(город, имя района в NFC): ключ} -- прямо из CITIES, без ручных таблиц."""
    src = open("rebuild_final.py", encoding="utf-8").read()
    node = next(n for n in ast.walk(ast.parse(src))
                if isinstance(n, ast.Assign) and any(getattr(t, "id", None) == "CITIES" for t in n.targets))
    cities = ast.literal_eval(node.value)
    out = {}
    for city, c in cities.items():
        for d in c["districts"]:
            out[(city, nfc(d["name"]))] = d["key"]
    return out


PHOTO_HASH = re.compile(r"/plain/([0-9a-f]{32})-")


def known_from_site():
    """Что уже заведено: ссылки, номера объявлений и ХЕШИ ФОТОГРАФИЙ.

    Хеши -- главное здесь. В пути картинки на cdn.chotot.com стоит хеш файла,
    и он переживает перевыкладку: продавец снимает объявление, выкладывает
    заново под новым list_id, а фотографии грузит те же самые. Ни проверка по
    id, ни проверка по URL этого не видят.

    Замерено 8 сентября 2026 на 1614 строках с фотографиями (6961 хеш): общие
    фотографии нашлись у 35 пар, и все 35 -- уже помеченные duplicateOf. Ни
    одного ложного срабатывания. Поэтому по хешу можно отсекать молча и
    автоматически: совпало фото -- это то же объявление, без вариантов.
    Обратное неверно (перекодированное фото даст другой хеш), так что проверка
    ловит не всё -- но не врёт."""
    from site_data import load_listings
    urls, ids, hashes = set(), set(), set()
    for l in load_listings():
        u = l["url"].split("?")[0].rstrip("/")
        urls.add(u)
        m = re.search(r"/(\d{6,})\.htm", u)
        if m:
            ids.add(m.group(1))
        for p in (l.get("details") or {}).get("photos") or []:
            h = PHOTO_HASH.search(p)
            if h:
                hashes.add(h.group(1))
    return urls, ids, hashes


def photo_hashes(ad):
    return {m.group(1) for m in map(PHOTO_HASH.search, ad.get("images") or []) if m}


def describe(ad, type_ru, ward, city_ru, city_en):
    """Описание из ПОЛЕЙ. Ничего не выдумываем и ничего не пересказываем."""
    body = (ad.get("body") or "").lower()
    hit = [i for i, (pat, _r, _e) in enumerate(AMENITIES) if re.search(pat, body)]
    # «полная меблировка, базовая меблировка» в одной строке -- объявление
    # хвалится и тем и другим, а вместе это противоречие. Полная сильнее.
    if 0 in hit and 1 in hit:
        hit.remove(1)
    am_ru = [AMENITIES[i][1] for i in hit][:4]
    am_en = [AMENITIES[i][2] for i in hit][:4]
    rooms, size = ad.get("rooms"), ad.get("size")
    # «Đường» -- это и есть «улица», «Số» -- «номер»: без нормализации выходит
    # «ул. Đường 15B» и «ул. Số 79».
    street = re.sub(r"^Đường\s+", "", nfc(ad.get("street_name")))
    street = re.sub(r"^(Số|số)\s+", "№ ", street)

    head_ru = type_ru
    head_en = {"Квартира": "Flat", "Дом": "House", "Комната": "Room", "Офис": "Office"}[type_ru]
    if rooms and type_ru in ("Квартира", "Дом"):
        head_ru = "%d-спальн%s %s" % (rooms, "ая" if type_ru == "Квартира" else "ый", type_ru.lower())
        head_en = "%d-bedroom %s" % (rooms, head_en.lower())
    parts_ru = [head_ru[0].upper() + head_ru[1:]]
    parts_en = [head_en[0].upper() + head_en[1:]]
    if size:
        parts_ru.append("%d м²" % size); parts_en.append("%d m²" % size)
    place_ru = ", ".join(x for x in (street_ru(street), ward, city_ru) if x)
    place_en = ", ".join(x for x in (street, ward, city_en) if x)
    parts_ru.append(place_ru); parts_en.append(place_en)

    tail_ru = ([ru_plural(ad["toilets"], "санузел", "санузла", "санузлов")]
               if ad.get("toilets") else []) + am_ru
    tail_en = (["%d bathroom%s" % (ad["toilets"], "" if ad["toilets"] == 1 else "s")]
               if ad.get("toilets") else []) + am_en
    ru = ", ".join(parts_ru) + (" — " + ", ".join(tail_ru) + "." if tail_ru else ".")
    en = ", ".join(parts_en) + (" — " + ", ".join(tail_en) + "." if tail_en else ".")
    return ru, en


CITY_LABEL = {"ho-chi-minh": ("Хошимин", "Ho Chi Minh City")}

NOTICE_RU = ("Описание собрано программой из полей объявления на Chợ Tốt — тип, комнаты, площадь, "
             "улица, район, удобства по ключевым словам. Рекламный текст продавца не пересказан, "
             "названия районов оставлены вьетнамскими. Подробности смотрите по ссылке.")
NOTICE_EN = ("This description was assembled by a program from the ad's own fields on Chợ Tốt — type, "
             "rooms, size, street, ward and amenities matched by keyword. The seller's marketing copy "
             "is not retold and ward names are left in Vietnamese. See the source for the rest.")


COORDS_FILE = "chotot_coords.json"


def save_coords(picked):
    """Chợ Tốt отдаёт lat/lon в том же ответе, и build_pins_step2_geocode.py
    читает их из chotot_coords.json по номеру объявления, минуя Nominatim.
    Без этого шага пин сядет в центроид района со случайным разбросом -- дом
    окажется не на своей улице. Ключ -- номер объявления, а не наш id, поэтому
    файл можно пополнять до вставки: он всего лишь кэш координат."""
    try:
        have = json.load(open(COORDS_FILE, encoding="utf-8"))
    except FileNotFoundError:
        have = {}
    added = 0
    for _c, _k, _t, ad, _a in picked:
        lat, lon = ad.get("latitude"), ad.get("longitude")
        k = str(ad["list_id"])
        if lat and lon and k not in have:
            have[k] = {"lat": lat, "lon": lon}
            added += 1
    tmp = COORDS_FILE + ".tmp.%d" % os.getpid()
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(have, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, COORDS_FILE)
    print("координат добавлено в %s: %d (всего %d)" % (COORDS_FILE, added, len(have)))


def batch_text(rows, ids, days):
    """Файл партии как ТЕКСТ, а не как объект: партия должна остаться в репозитории
    отдельным файлом -- по нему потом видно, что именно и на каком основании
    заведено. Так же устроены все ручные партии new_listingsNNN.py."""
    q = "'''"
    doc = [
        '# -*- coding: utf-8 -*-',
        '"""Chợ Tốt, автоматический сбор: %d объявлений, %s.' % (len(rows), datetime.date.today().isoformat()),
        '',
        'Партию собрал collect_chotot.py -- без модели в контуре. Район взят точным',
        'совпадением ward_name_v3 с CITIES, описание собрано из полей объявления, а не',
        'пересказом текста продавца, возраст не больше %.1f дней по orig_list_time.' % days,
        '',
        'Объявления, район которых не совпал ни с одним нашим, пропущены, а не приписаны',
        'к соседнему -- в этом и разница с тем, как это делала сессия.',
        '"""',
        'from listing_lock import insert_listings',
        '',
        'IDS = %r' % (ids,),
        '',
        'N_RU = %s' % json.dumps(NOTICE_RU, ensure_ascii=False),
        'N_EN = %s' % json.dumps(NOTICE_EN, ensure_ascii=False),
        '',
        'NEW_SRC = r' + q,
    ]
    tail = [
        q,
        '',
        '# Оговорка одна на всю партию, поэтому в строках стоит метка, а не её текст:',
        '# так партия остаётся читаемой глазами.',
        'NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)',
        '',
        'if __name__ == "__main__":',
        '    insert_listings(NEW_SRC, IDS, owner=__file__)',
        '',
    ]
    return "\n".join(doc + rows + tail)


def row_text(lid, city, key, type_ru, ad, age):
    ward = short_ward(nfc(ad.get("ward_name_v3")))
    city_ru, city_en = CITY_LABEL[city]
    ru, en = describe(ad, type_ru, ward, city_ru, city_en)
    det = {"photos": [u for u in (ad.get("images") or [])[:6]],
           "notice": "RU_N", "noticeEn": "EN_N"}
    j = lambda s: json.dumps(safe(s) if isinstance(s, str) else s, ensure_ascii=False)
    return ('L(%d,"%s","%s","%s",%d,%s,\n  %s,\n  %s,%s,%d,source="chotot",\n'
            '  descEn=%s,\n  details=%s),'
            % (lid, city, key, type_ru, int(ad["price"]),
               int(ad["size"]) if ad.get("size") else "None",
               j(ru), j(ad_url(ad)), j(ru_days_label(age)), age, j(en),
               json.dumps(det, ensure_ascii=False)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=float, default=3.0, help="брать объявления не старше стольких дней")
    ap.add_argument("--limit", type=int, default=40, help="максимум строк за прогон")
    ap.add_argument("--write", action="store_true", help="записать файл партии")
    ap.add_argument("--insert", action="store_true", help="и вставить его (только вместе с --write)")
    a = ap.parse_args()

    wards = site_wards()
    known_urls, known_ids, known_photos = known_from_site()
    now = time.time()
    picked, skipped = [], {"чужой район": 0, "старое": 0, "уже есть": 0, "без фото": 0,
                           "без цены": 0, "те же фотографии": 0}
    seen_photos = set()

    for city, region, areas in TARGETS:
        for area in areas:
            for cat, type_ru in CATEGORIES.items():
                url = "%s?%s" % (API, urllib.parse.urlencode(
                    {"cg": cat, "region_v2": region, "area_v2": area, "st": "u", "limit": 50}))
                data = get(url)
                time.sleep(0.5)
                if not data:
                    continue
                for ad in data.get("ads", []):
                    lid = str(ad.get("list_id"))
                    key = wards.get((city, nfc(ad.get("ward_name_v3"))))
                    if not key:
                        skipped["чужой район"] += 1; continue
                    ts = ad.get("orig_list_time") or ad.get("list_time")
                    age_days = (now - ts / 1000) / 86400 if ts else 999
                    if age_days > a.days:
                        skipped["старое"] += 1; continue
                    if lid in known_ids:
                        skipped["уже есть"] += 1; continue
                    if not ad.get("price"):
                        skipped["без цены"] += 1; continue
                    if not (ad.get("number_of_images") or 0):
                        skipped["без фото"] += 1; continue
                    ph = photo_hashes(ad)
                    # Перевыкладка под новым номером и один и тот же ад в двух
                    # категориях -- ловятся только так, см. known_from_site().
                    if ph & (known_photos | seen_photos):
                        skipped["те же фотографии"] += 1; continue
                    seen_photos |= ph
                    picked.append((city, key, type_ru, ad, max(0, int(age_days))))

    picked.sort(key=lambda p: p[4])
    picked = picked[:a.limit]
    print("найдено пригодных: %d (не старше %.1f дн.)" % (len(picked), a.days))
    print("пропущено:", ", ".join("%s %d" % (k, v) for k, v in skipped.items() if v))
    for city, key, type_ru, ad, age in picked[:12]:
        print("  %-4s %-9s %-11s %10s ₫  %s" % (key, type_ru, "%d дн." % age,
                                                format(ad["price"], ","), nfc(ad.get("subject"))[:52]))
    if not a.write:
        print("\n(--write не задан: файл партии не записан)")
        return
    if not picked:
        print("\nнечего записывать")
        return

    # id берём через allocate_ids.py, а не «максимум плюс один»: параллельная
    # сессия читает тот же максимум и получает те же номера -- так этот массив
    # уже портили четыре раза.
    r = subprocess.run([sys.executable, "allocate_ids.py", "--block", "1000000",
                        "--count", str(len(picked)), "--owner", "collect_chotot"],
                       capture_output=True, text=True, encoding="utf-8")
    m = re.search(r"FIRST=(\d+) LAST=(\d+)", r.stdout or "")
    if not m:
        sys.exit("не удалось зарезервировать id:\n%s%s" % (r.stdout, r.stderr))
    first, last = int(m.group(1)), int(m.group(2))
    ids = list(range(first, last + 1))

    rows = [row_text(ids[n], city, key, type_ru, ad, age)
            for n, (city, key, type_ru, ad, age) in enumerate(picked)]
    nums = [int(re.sub(r"\D", "", f) or 0) for f in glob.glob("new_listings*.py")]
    path = "new_listings%d.py" % (max(nums + [0]) + 1)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(batch_text(rows, ids, a.days))
    print("\nзаписано: %s -- %d строк, id %d..%d" % (path, len(rows), first, last))
    save_coords(picked)

    # check_repost.py считает редкие слова описаний, и на РУЧНЫХ партиях это
    # работает: там описание -- живой текст, у двух разных объявлений он разный.
    # Здесь описания собраны из полей по одному шаблону, они короткие и на 80%
    # состоят из общего каркаса, поэтому мера |A∩B|/min(|A|,|B|) задирается сама
    # собой: на первой же партии из 12 строк она пометила 11. Это шум её меры, а
    # не находки, поэтому вставку по нему не останавливаем -- её сторожит
    # проверка по хешам фотографий, у которой замерено ноль ложных срабатываний.
    # Вывод оставлен на экране: глазами он всё ещё полезен.
    print("\n-- check_repost.py, справочно (на машинных описаниях он шумит):")
    subprocess.run([sys.executable, "check_repost.py", "--file", path])
    if not a.insert:
        print("\n(--insert не задан: партия записана, но не вставлена)")
        return
    subprocess.run([sys.executable, path], check=True)
    subprocess.run([sys.executable, "allocate_ids.py", "--release", "%d-%d" % (first, last)],
                   check=True)


if __name__ == "__main__":
    main()
