# -*- coding: utf-8 -*-
"""
Сбор объявлений об аренде с batdongsan.com.vn -- крупнейшего портала недвижимости
Вьетнама.

ЗАЧЕМ. У Chợ Tốt по нашим городам тонко там, где у batdongsan густо: 23 тысячи
объявлений аренды по Хошимину и 12 тысяч по Ханою против сотен. Но главное даже
не объём. После реформы 2025 года Chợ Tốt пишет адреса по ПРЕЖНЕМУ делению, а
batdongsan печатает оба сразу -- в карточке списка стоит «TP. Nha Trang
(P. Bắc Nha Trang mới)», а прежний квартал лежит в адресе ссылки
(«...phuong-vinh-phuoc...»). Поэтому район здесь не приходится доказывать по
улице или прецеденту: его называет сам источник, и притом в обоих видах.

ДОСТУП -- ТОЛЬКО НАСТОЯЩИМ БРАУЗЕРОМ. Cloudflare отдаёт 403 и обычному GET, и
подмене отпечатка TLS: проверено 12 сентября 2026. Видимое окно решает
испытание само за несколько секунд, кука cf_clearance живёт год, и дальше
работает headless на том же профиле. Профиль -- `_bds_profile/`, отдельный от
фейсбучного, в репозиторий не идёт. Первый раз (и после смены адреса или
переустановки браузера):

    python collect_batdongsan.py --warmup

СВЕЖЕСТЬ -- ПО ДВУМ КЛЮЧАМ. «Ngày đăng» сбрасывается при перевыкладке: 12
сентября объявление с номером девятимесячной давности показывалось как
«Đăng hôm nay». Поэтому кроме даты проверяется сам номер объявления (prid): он
сквозной по стране и растёт примерно на 4500 в сутки, так что старый номер со
свежей датой -- это витрина агентства, а не новое объявление.

ЧТО НЕ ДЕЛАЕТСЯ. Не трогается `/microservice-architecture-router/` -- он прямо
запрещён в их robots.txt (всё остальное там разрешено). Не нажимается «Hiện số»
(показать телефон): это действие на их сайте, а не чтение. Фотографии не
скачиваются, а берутся ссылкой на их же CDN -- так же, как у 79 строк
batdongsan, заведённых руками раньше.

    python collect_batdongsan.py --city nha-trang            отчёт
    python collect_batdongsan.py --city nha-trang --write --insert
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
import time

import ingest_telegram as it

HERE = os.path.dirname(os.path.abspath(__file__))
PROFILE = os.path.join(HERE, "_bds_profile")   # переопределяется ключом --profile
BASE = "https://batdongsan.com.vn"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

# Город проекта -> кусок их адреса. Проверяется по хлебным крошкам их же
# страницы: Khánh Hòa -> Nha Trang -> «nha-trang-kh».
CITY_SLUG = {
    "nha-trang": "nha-trang-kh",
    "da-nang": "tp-da-nang",
    "ho-chi-minh": "tp-hcm",
    "ha-noi": "ha-noi",
    "can-tho": "can-tho",
    "hai-phong": "hai-phong",
    "hue": "hue-tth",
    "da-lat": "da-lat-ld",
    "vung-tau": "vung-tau-brvt",
    "quy-nhon": "quy-nhon-bd",
    "hoi-an": "hoi-an-qna",
    "phan-thiet": "phan-thiet-bt",
    "buon-ma-thuot": "buon-ma-thuot-dl",
    "phu-quoc": "phu-quoc-kg",
}
# Раздел -> тип жилья у нас. Только жильё: офисы, склады и киоски пропускаем,
# как и в остальных сборщиках.
CATEGORIES = (
    ("cho-thue-can-ho-chung-cu", "Квартира"),
    ("cho-thue-nha-rieng", "Дом"),
    ("cho-thue-nha-tro-phong-tro", "Комната"),
    ("cho-thue-nha-biet-thu-lien-ke", "Дом"),
)
MAX_AGE_DAYS = 13          # purge_old_listings.py снимает строки старше 14 дней
PRID_PER_DAY = 4500        # сквозная нумерация по стране, замер 12.09.2026
MAX_PHOTOS = 6
PRICE_LIMITS = (1_500_000, 500_000_000)

CARDS_JS = """() => {
  const out = [];
  document.querySelectorAll('.js__card-full-web').forEach(c => {
    const a = c.querySelector('a[href]');
    const t = s => { const e = c.querySelector(s); return e ? e.innerText.trim() : ''; };
    out.push({href: a ? a.href : null, title: t('.re__card-title'),
              price: t('.re__card-config-price'), area: t('.re__card-config-area'),
              beds: t('.re__card-config-bedroom'), wc: t('.re__card-config-toilet'),
              loc: t('.re__card-location'), when: t('.re__card-published-info-published-at')});
  });
  return out;
}"""
DETAIL_JS = """() => {
  const short = {};
  document.querySelectorAll('.re__pr-short-info-item').forEach(i => {
    const t = i.querySelector('.title'), v = i.querySelector('.value');
    if (t) short[t.innerText.trim()] = v ? v.innerText.trim() : '';
  });
  const spec = {};
  document.querySelectorAll('.re__pr-specs-content-item').forEach(i => {
    const t = i.querySelector('.re__pr-specs-content-item-title');
    const v = i.querySelector('.re__pr-specs-content-item-value');
    if (t) spec[t.innerText.trim()] = v ? v.innerText.trim() : '';
  });
  const imgs = [...new Set([...document.querySelectorAll('img')].map(i => i.src)
      .filter(s => s && s.includes('file4.batdongsan.com.vn')))];
  const ld = [...document.querySelectorAll('script[type="application/ld+json"]')]
      .map(s => s.textContent).join(' ');
  return {short: short, spec: spec, imgs: imgs, ld: ld,
          tracking: window.pageTrackingData ? JSON.stringify(window.pageTrackingData) : ''};
}"""

PRID = re.compile(r"-pr(\d+)(?:$|[/?#])")
# В адресе объявления квартал стоит рядом с названием ЖК и номером дома:
# «...phuong-vinh-hoa-2-libera-nha-trang». Где кончается квартал, разметка не
# говорит, поэтому берём самый длинный кусок, который знает наш сайт: «loc tho»
# из «phuong-loc-tho-350», а не «loc».
WARD_IN_SLUG = re.compile(r"phuong-([a-z0-9-]+)", re.I)
NEW_WARD = re.compile(r"\(\s*(?:P\.|Phường|X\.|Xã)?\s*([^()]+?)\s+mới\s*\)", re.I)
OLD_MARK = re.compile(r"\(\s*(?:P\.|Phường|Q\.|Quận|TP\.)?\s*([^()]+?)\s+cũ\s*\)", re.I)
DATE_LD = re.compile(r'"@datePublished"\s*:\s*"([\d-]{10})')
NUM = re.compile(r"([\d.,]+)")


class Skip(Exception):
    pass


# ------------------------------------------------------------------ разбор --

def price_vnd(text):
    """«15 triệu/tháng» -> 15000000. Диапазон и «thỏa thuận» -- не цена."""
    f = it.words(text)
    if not f or "thoa thuan" in f or re.search(r"\d\s*-\s*\d", f):
        return None
    m = re.search(r"([\d.,]+)\s*(ty|trieu|nghin)", f)
    if not m:
        return None
    v = float(m.group(1).replace(".", "").replace(",", "."))
    mult = {"ty": 1_000_000_000, "trieu": 1_000_000, "nghin": 1_000}[m.group(2)]
    v = int(round(v * mult))
    return v if PRICE_LIMITS[0] <= v <= PRICE_LIMITS[1] else None


def area_m2(text):
    m = re.search(r"([\d.,]+)\s*m", it.words(text) or "")
    if not m:
        return None
    v = float(m.group(1).replace(".", "").replace(",", "."))
    return int(round(v)) if 10 <= v <= 2000 else None


def small_int(text):
    m = re.search(r"\d+", text or "")
    return int(m.group(0)) if m else None


def days_ago(when, today):
    """«Đăng hôm nay» / «Đăng 4 ngày trước» / «Đăng 12/09/2026» -> дней."""
    f = it.words(when)
    if "hom nay" in f:
        return 0
    if "hom qua" in f:
        return 1
    m = re.search(r"(\d+)\s*(ngay|tuan|thang)", f)
    if m:
        n = int(m.group(1))
        return n * {"ngay": 1, "tuan": 7, "thang": 30}[m.group(2)]
    m = re.search(r"(\d{2})/(\d{2})/(\d{4})", when or "")
    if m:
        d = datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        return (today - d).days
    return None


def coarse_keys(city):
    """Ключи укрупнённых районов реформы 2025 года -- по подписи в CITIES."""
    from site_data import load_data
    out = set()
    for d in load_data()["CITIES"].get(city, {}).get("districts", []):
        if "укрупн" in (d.get("hint") or "") or "enlarged" in (d.get("hintEn") or ""):
            out.add(d["key"])
    return out


def ward_from(card_loc, href, city, ctx, coarse=None):
    """Район -- словами самого источника, и из двух названий берётся точное.

    Портал печатает нынешний район в карточке («P. Bắc Nha Trang mới») и
    квартал в адресе объявления («phuong-vinh-phuoc»). В адресе бывает и то и
    другое: у свежих объявлений там уже новый район. Поэтому собираем обе
    догадки и предпочитаем ту, что не укрупнённая."""
    wmap = ctx.ward_words.get(city, {})
    # Полный список названий районов сайта -- включая тот, что назван как сам
    # город («Phường Nha Trang»). В свободном тексте такое совпадение запрещено,
    # здесь можно: это поле источника с пометкой «mới», а не слово из рекламы.
    full = {it.words(re.sub(r"^(?:Phường|Quận|Đặc khu|Xã)\s+", "", n)): k
            for k, n in ctx.dnames.get(city, {}).items()}
    coarse = coarse_keys(city) if coarse is None else coarse
    found, tried = [], []

    # Где кончается квартал, разметка адреса не говорит («phuong-loc-tho-350»),
    # поэтому берём самый длинный кусок, который знает сайт.
    for m in WARD_IN_SLUG.finditer(href or ""):
        toks = [t for t in m.group(1).split("-") if t]
        hit = None
        for n in range(min(4, len(toks)), 0, -1):
            w = it.words(" ".join(toks[:n]))
            if w in wmap or w in full:
                hit = (wmap.get(w) or full[w], "квартал в адресе объявления: %s" % w)
                break
        if hit:
            found.append(hit)
        else:
            tried.append(" ".join(toks[:3]))

    m = NEW_WARD.search(card_loc or "")
    if m:
        w = it.words(m.group(1))
        tried.append(w)
        if w in wmap or w in full:
            found.append(((wmap.get(w) or full[w]),
                          "нынешний район назван в карточке: %s" % m.group(1).strip()))

    for key, why in found:
        if key not in coarse:
            return key, why
    if found:
        return found[0]
    return None, "район не назван так, как его знает сайт (%s)" % (", ".join(tried) or "нет данных")


def describe(typ, beds, baths, area, place, dname, furnished):
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
    if furnished:
        tail_ru.append("полная меблировка")
        tail_en.append("fully furnished")
    return (", ".join(pr) + (" — " + ", ".join(tail_ru) if tail_ru else "") + ".",
            ", ".join(pe) + (" — " + ", ".join(tail_en) if tail_en else "") + ".")


NOTICE_RU = ("Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, "
             "санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван "
             "самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны "
             "ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при "
             "перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру "
             "объявления.")
NOTICE_EN = ("This description was assembled by a program from the ad's own fields on "
             "batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's "
             "marketing copy is not retold. The district comes from the source itself: the portal "
             "prints both the current ward and the former one. The photos are shown as links to "
             "batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset "
             "it when they repost, so freshness is checked against the ad's number as well.")


# ------------------------------------------------------------------ браузер --

def open_ctx(pw, headless, profile=None):
    # Один каталог профиля -- один процесс Chrome. Если профиль занят другим
    # прогоном, запуск падает с TargetClosedError, поэтому профиль выбирается.
    return pw.chromium.launch_persistent_context(
        user_data_dir=profile or PROFILE, headless=headless, channel="chrome", user_agent=UA,
        viewport={"width": 1400, "height": 950}, locale="vi-VN",
        args=["--disable-blink-features=AutomationControlled"])


def wait_cf(page, tries=12):
    for _ in range(tries):
        title = (page.title() or "").lower()
        if "just a moment" not in title and "attention required" not in title:
            return True
        time.sleep(2.5)
    return False


def fetch_list(page, url):
    page.goto(url, wait_until="domcontentloaded", timeout=90000)
    if not wait_cf(page):
        raise Skip("Cloudflare не пропустил: нужен прогрев (python collect_batdongsan.py --warmup)")
    time.sleep(2.0)
    return page.evaluate(CARDS_JS)


def fetch_detail(page, url):
    page.goto(url, wait_until="domcontentloaded", timeout=90000)
    if not wait_cf(page):
        raise Skip("Cloudflare не пропустил на карточке")
    time.sleep(1.5)
    return page.evaluate(DETAIL_JS)


# ------------------------------------------------------------------ партия --

HEADER = '''# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: %(n)s, %(date)s, город %(city)s.

Партию собрал collect_batdongsan.py -- без модели в контуре. Район не выведен, а
взят у самого источника: портал печатает нынешний квартал в карточке («P. Bắc
Nha Trang mới») и прежний в адресе объявления («phuong-vinh-phuoc»); строка
заводится, только если один из них совпал с районом нашего сайта. Описание
собрано из полей объявления, рекламный текст не пересказан. Фотографии --
ссылками на batdongsan, у них же и хранятся.

Свежесть проверена дважды: по дате объявления и по его номеру. Номер сквозной по
стране, поэтому старый номер со свежей датой -- это перевыкладка, а не новое
объявление, и такие отброшены.

ЗАВЕДЕНО:
%(accepted)s

ОТСЕЯНО (%(nskip)d):
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


def allocate(n):
    """Свой блок номеров: 3000000 -- общий для «прочих» источников (hoppler,
    dotproperty), а не телеграмный 2000000."""
    out = subprocess.run([sys.executable, "allocate_ids.py", "--block", "3000000",
                          "--count", str(n), "--owner", "collect_batdongsan"],
                         capture_output=True, text=True, encoding="utf-8")
    m = re.search(r"FIRST=(\d+) LAST=(\d+)", out.stdout or "")
    if not m:
        sys.exit("не удалось зарезервировать id:\n%s%s" % (out.stdout, out.stderr))
    return list(range(int(m.group(1)), int(m.group(2)) + 1))


def write_batch(rows_data, skipped, ids, today, city):
    j = lambda s: json.dumps(s, ensure_ascii=False)
    rows = []
    for i, r in zip(ids, rows_data):
        rows.append('L(%d,"%s","%s","%s",%d,%s,\n  %s,\n  %s,%s,%d,source="batdongsan",\n'
                    '  descEn=%s,\n  details=%s),'
                    % (i, r["city"], r["district"], r["type"], r["price"],
                       r["area"] if r["area"] else "None", j(r["ru"]), j(r["url"]),
                       j(it.posted_label(r["age"])), r["age"], j(r["en"]), j(r["details"])))
    acc = "\n".join("  * %s -- %s, %s ₫%s: %s"
                    % (r["prid"], r["district"], format(r["price"], ","),
                       ", %d м²" % r["area"] if r["area"] else "", r["why"]) for r in rows_data)
    skp = "\n".join("  * %s -- %s" % kv for kv in skipped[:40]) or "  (нет)"
    nums = [int(re.sub(r"\D", "", f) or 0) for f in glob.glob("new_listings*.py")]
    path = "new_listings%d.py" % (max(nums + [0]) + 1)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HEADER % {"n": it.ru_plural(len(rows), "строка", "строки", "строк"),
                          "date": today.isoformat(), "city": city, "accepted": it.doc_safe(acc),
                          "nskip": len(skipped), "skipped": it.doc_safe(skp), "ids": ids,
                          "q": "'''", "rows": "\n".join(rows)})
    return path


def main():
    ap = argparse.ArgumentParser(description="сбор аренды с batdongsan.com.vn")
    ap.add_argument("--city", default="nha-trang")
    ap.add_argument("--pages", type=int, default=2, help="страниц списка на раздел")
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--warmup", action="store_true", help="видимое окно, пройти Cloudflare один раз")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--insert", action="store_true")
    ap.add_argument("--delay", type=float, default=3.5)
    ap.add_argument("--profile", default=PROFILE, help="каталог профиля браузера")
    a = ap.parse_args()
    os.chdir(HERE)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    from playwright.sync_api import sync_playwright

    if a.warmup:
        with sync_playwright() as pw:
            ctx = open_ctx(pw, headless=False, profile=a.profile)
            page = ctx.pages[0] if ctx.pages else ctx.new_page()
            page.goto(BASE + "/nha-dat-cho-thue", wait_until="domcontentloaded", timeout=120000)
            ok = wait_cf(page, tries=24)
            has = any(c["name"] == "cf_clearance" for c in ctx.cookies())
            print("Cloudflare пройден: %s, кука cf_clearance: %s" % (ok, "есть" if has else "нет"))
            ctx.close()
        return 0 if has else 1

    slug = CITY_SLUG.get(a.city)
    if not slug:
        sys.exit("для города %s не задан кусок адреса batdongsan (CITY_SLUG)" % a.city)
    today = datetime.date.today()
    ctx_site = it.Ctx(today)
    known = set(ctx_site.urls)
    accepted, skipped, seen = [], [], set()
    max_prid = 0

    with sync_playwright() as pw:
        br = open_ctx(pw, headless=True, profile=a.profile)
        page = br.pages[0] if br.pages else br.new_page()
        try:
            cards = []
            for cat, typ in CATEGORIES:
                for p in range(1, a.pages + 1):
                    url = "%s/%s-%s%s" % (BASE, cat, slug, "" if p == 1 else "/p%d" % p)
                    try:
                        got = fetch_list(page, url)
                    except Skip as e:
                        print("  %s: %s" % (url, e))
                        break
                    print("  %-58s карточек %d" % (url.replace(BASE, ""), len(got)))
                    for c in got:
                        c["type"] = typ
                    cards += got
                    time.sleep(a.delay)
                    if len(got) < 20:
                        break

            for c in cards:
                href = (c.get("href") or "").split("?")[0]
                m = PRID.search(href)
                if not href or not m:
                    continue
                prid = int(m.group(1))
                if prid in seen:
                    continue
                seen.add(prid)
                max_prid = max(max_prid, prid)
                key = str(prid)
                if it.norm_url(href) in known:
                    skipped.append((key, "уже на сайте"))
                    continue
                age = days_ago(c.get("when"), today)
                if age is None or age > MAX_AGE_DAYS:
                    skipped.append((key, "старее %d дней (%s)" % (MAX_AGE_DAYS, c.get("when"))))
                    continue
                price = price_vnd(c.get("price"))
                if not price:
                    skipped.append((key, "цена не читается: %s" % c.get("price")))
                    continue
                area = area_m2(c.get("area"))
                beds = small_int(c.get("beds"))
                dkey, why = ward_from(c.get("loc"), href, a.city, ctx_site)
                if not dkey:
                    skipped.append((key, why))
                    continue
                typ = c["type"]
                if typ == "Квартира" and area and area <= 32 and not beds:
                    typ = "Студия"
                if len(accepted) >= a.limit:
                    skipped.append((key, "лимит прогона выбран"))
                    continue
                try:
                    d = fetch_detail(page, href)
                except Skip as e:
                    skipped.append((key, str(e)))
                    continue
                time.sleep(a.delay)
                photos = [u for u in (d.get("imgs") or []) if "file4.batdongsan" in u][:MAX_PHOTOS]
                if not photos:
                    skipped.append((key, "нет фотографий"))
                    continue
                short, spec = d.get("short") or {}, d.get("spec") or {}
                baths = small_int(spec.get("Số phòng tắm, vệ sinh") or "")
                area = area or area_m2(short.get("Diện tích") or "")
                beds = beds or small_int(spec.get("Số phòng ngủ") or "")
                furnished = "day du" in it.words(spec.get("Nội thất") or "")
                ld = DATE_LD.search(d.get("ld") or "")
                if ld:
                    try:
                        age = (today - datetime.date(*map(int, ld.group(1).split("-")))).days
                    except ValueError:
                        pass
                pv = price
                place = None
                mproj = re.search(r"/cho-thue-[a-z-]+?-([a-z0-9-]+)/", href)
                dup = it.duplicate({"city": a.city, "type": typ, "beds": beds, "area": area,
                                    "cat": None, "block": None}, dkey, pv, "", ctx_site, frozenset())
                if dup:
                    skipped.append((key, "похоже на уже заведённое: id %s" % dup["id"]))
                    continue
                dname = ctx_site.district_label(a.city, dkey)
                ru, en = describe(typ, beds, baths, area, place, dname, furnished)
                accepted.append({"prid": prid, "url": href, "city": a.city, "district": dkey,
                                 "type": typ, "price": price, "area": area, "beds": beds,
                                 "age": max(0, age), "ru": ru, "en": en, "why": why,
                                 "details": {"photos": photos, "notice": NOTICE_RU,
                                             "noticeEn": NOTICE_EN}})
                ctx_site.by_city[a.city].append(
                    {"id": "new:%d" % prid, "city": a.city, "district": dkey, "type": typ,
                     "area": area, "pv": pv, "_beds": beds, "_words": it.words(ru + " " + en),
                     "_new": True})
        finally:
            br.close()

    # Старый номер при свежей дате -- перевыкладка витрины, а не новое объявление.
    if max_prid:
        floor = max_prid - PRID_PER_DAY * (MAX_AGE_DAYS + 1)
        old = [r for r in accepted if r["prid"] < floor]
        for r in old:
            skipped.append((str(r["prid"]), "номер объявления старый при свежей дате -- перевыкладка"))
        accepted = [r for r in accepted if r["prid"] >= floor]

    print("\nbatdongsan, %s: карточек %d, заводится %d" % (a.city, len(seen), len(accepted)))
    for r in accepted:
        print("  + %-10s %-4s %-9s %12s ₫  %s м²  -- %s"
              % (r["prid"], r["district"], r["type"], format(r["price"], ","), r["area"] or "?", r["why"]))
    for k, why in skipped[:25]:
        print("  - %-10s %s" % (k, why))
    if len(skipped) > 25:
        print("  ... и ещё %d отсеяно" % (len(skipped) - 25))

    if not a.write or not accepted:
        return 0
    ids = allocate(len(accepted))
    inserted = False
    try:
        path = write_batch(accepted, skipped, ids, today, a.city)
        print("\nзаписано: %s -- %d строк, id %d..%d" % (path, len(ids), ids[0], ids[-1]))
        if not a.insert:
            return 0
        subprocess.run([sys.executable, path], check=True)
        inserted = True
    finally:
        subprocess.run([sys.executable, "allocate_ids.py", "--release", "%d-%d" % (ids[0], ids[-1])])
        if not inserted and a.insert:
            print("вставка не состоялась -- зарезервированные id освобождены")
    return 0


if __name__ == "__main__":
    sys.exit(main())
