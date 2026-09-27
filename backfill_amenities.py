# -*- coding: utf-8 -*-
"""
Дозаполнить удобства и этаж (amenities.py) у строк, заведённых до 27.09.2026.

Новые строки получают их при сборе (collect_chotot, ingest_facebook,
ingest_telegram). Строки живут на сайте неделю, так что это разовая работа --
и ещё на случай, когда правила amenities.py поменяются (--refresh).

Две фазы, чтобы долгая сеть не держала блокировку и не пересекалась с прогоном
сервера:
  1. сбор (без блокировки): полный текст объявления Chợ Tốt по API, текст поста
     Facebook -- из файлов кандидатов fb_collect, Telegram -- со страницы поста
     t.me (batdongsan закрыт Cloudflare -- его строки получают разбор только
     при сборе); разбор кладётся в кэш daily_check_logs/amenities_cache.json
     (id -> {"am", "fl", "flHigh"}), и прерванный сбор продолжается с места;
  2. --apply: под блокировкой строк -- положить разобранное в details тех строк,
     у которых его ещё нет. Быстро; делать между прогонами сервера.

    python backfill_amenities.py                 сбор, сколько успеет (Ctrl+C -- не беда)
    python backfill_amenities.py --limit 500
    python backfill_amenities.py --apply         записать в строки
    python backfill_amenities.py --refresh       собрать заново и для строк, где уже есть
"""
import argparse
import glob
import json
import os
import re
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

import amenities
import check_freshness as cf
import fetch_telegram_listings as ftl
from listing_lock import listings_write_lock, load_rows, save_rows

CACHE = os.path.join("daily_check_logs", "amenities_cache.json")
KEYS = ("am", "fl", "flHigh")


def load_cache():
    try:
        return json.load(open(CACHE, encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return {}


def save_cache(c):
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    tmp = CACHE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(c, f, ensure_ascii=False)
    os.replace(tmp, CACHE)


def fb_bodies():
    out = {}
    for f in glob.glob("_fb_*_*.json"):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if isinstance(d, dict):
            for c in d.get("candidates") or []:
                u = (c.get("url") or "").split("?")[0].rstrip("/")
                if u and c.get("body"):
                    out[u] = c["body"]
    return out


def has_any(r):
    return any(k in (r.get("details") or {}) for k in KEYS)


def collect(a):
    cache = load_cache()
    rows = load_rows()
    todo = [r for r in rows if str(r["id"]) not in cache and (a.refresh or not has_any(r))]
    fb = fb_bodies()
    done = gone = err = 0
    t0 = time.time()
    try:
        for r in todo:
            if a.limit and done >= a.limit:
                break
            src = r.get("source") or "chotot"
            text = None
            if src == "chotot":
                m = re.search(r"/(\d{8,9})\.htm", r["url"])
                if not m:
                    continue
                try:
                    ad = cf.fetch(int(m.group(1)))
                    text = "%s\n%s" % (ad.get("subject") or "", ad.get("body") or "")
                except cf.Gone:
                    gone += 1          # снятое снимет remove_gone_listings; здесь -- просто нечего разбирать
                    cache[str(r["id"])] = {"gone": True}
                    continue
                except Exception:
                    err += 1
                    time.sleep(2)
                    continue
                time.sleep(0.3)
            elif src == "fbgroup":
                text = fb.get(r["url"].split("?")[0].rstrip("/"))
            elif src == "telegram":
                # Один пост -- страница-встраивание t.me, её отдают без входа.
                try:
                    h = ftl.http_get(r["url"].split("?")[0] + "?embed=1&mode=tme")
                except RuntimeError:
                    err += 1
                    continue
                tm = ftl.TEXT_RE.search(h)
                text = ftl.strip_tags(ftl.inner_div(h, tm.start())) if tm else ""
                time.sleep(0.5)
            if not text:
                continue
            got = amenities.extract(text)
            cache[str(r["id"])] = {k: got[k] for k in KEYS if k in got}
            done += 1
            if done % 200 == 0:
                save_cache(cache)
                print("  %d разобрано, %d снято, %d ошибок, %.0f с" % (done, gone, err, time.time() - t0))
    except KeyboardInterrupt:
        print("прервано -- разобранное сохранено, следующий запуск продолжит")
    save_cache(cache)
    left = sum(1 for r in todo if str(r["id"]) not in cache)
    print("разобрано %d, снято %d, ошибок %d; строк без разбора осталось %d (из %d)"
          % (done, gone, err, left, len(rows)))


def apply():
    cache = load_cache()
    with listings_write_lock("backfill_amenities"):
        rows = load_rows()
        n = 0
        for r in rows:
            got = cache.get(str(r["id"]))
            if not got or got.get("gone"):
                continue
            det = r.setdefault("details", {})
            before = {k: det.get(k) for k in KEYS}
            for k in KEYS:
                det.pop(k, None)
            # На место перед оговоркой: photos, am, fl, flHigh, notice, noticeEn -- как у новых строк.
            tail = {k: det.pop(k) for k in ("notice", "noticeEn") if k in det}
            for k in KEYS:
                if got.get(k) and (k == "am" or amenities.floor_applies(r.get("type"))):
                    det[k] = 1 if k == "flHigh" else got[k]   # в кэше до 27.09 -- True
            det.update(tail)
            if {k: det.get(k) for k in KEYS} != before:
                n += 1
        save_rows(rows)
    print("записано в строки: %d" % n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    if a.apply:
        apply()
    else:
        collect(a)


if __name__ == "__main__":
    main()
