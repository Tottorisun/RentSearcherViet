# -*- coding: utf-8 -*-
"""Добрать координаты объявлений Chợ Tốt для уже заведённых строк.

ЗАЧЕМ. Каждое объявление Chợ Tốt несёт свои lat/lon, и build_pins_step2_geocode.py
берёт их из chotot_coords.json, минуя Nominatim. Но файл начали заполнять только
2 сентября 2026, а строки заводились с августа: на 9 сентября 948 строк из 1783
не имеют координат объявления и стоят либо по результату геокодирования адреса,
либо в центроиде района со случайным разбросом -- то есть в правильном районе, но
не на своей улице.

Эндпоинт `ad-listing/<list_id>` отдаёт объявление целиком, включая координаты.
404 означает, что объявление снято (это уже проверялось в браузере и записано в
памяти проекта) -- такие строки здесь только считаются и печатаются, удаляет их
remove_gone_listings.py, у которого для этого есть и кэш, и свои предохранители.

Пишет только chotot_coords.json. Ни rebuild_final.py, ни pin_results.json не
трогает: их пересоберёт обычный конвейер.

  python backfill_chotot_coords.py --limit 200      добрать 200 штук
  python backfill_chotot_coords.py --city nha-trang только один город
  python backfill_chotot_coords.py --dry-run        показать, скольким не хватает
"""
import argparse
import json
import os
import re
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
                    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
AD = "https://gateway.chotot.com/v1/public/ad-listing/%s"
COORDS_FILE = "chotot_coords.json"
AD_ID = re.compile(r"/(\d{6,})\.htm")


def load_coords():
    try:
        return json.load(open(COORDS_FILE, encoding="utf-8"))
    except FileNotFoundError:
        return {}


def save_coords(coords):
    """Через временный файл: прогон длинный, и оборвать его на середине записи --
    значит потерять весь накопленный файл, а не одну строку."""
    tmp = COORDS_FILE + ".tmp.%d" % os.getpid()
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(coords, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, COORDS_FILE)


def fetch(list_id, tries=3):
    """(lat, lon) | 'gone' | None. 404 -- объявление снято, а не сбой сети."""
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(AD % list_id, headers=UA),
                                        timeout=30) as r:
                d = json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return "gone"
            if i == tries - 1:
                return None
        except Exception:
            if i == tries - 1:
                return None
        else:
            ad = d.get("ad") or d
            lat, lon = ad.get("latitude"), ad.get("longitude")
            return (lat, lon) if lat and lon else None
        time.sleep(2 + 2 * i)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=250, help="сколько объявлений опросить за прогон")
    ap.add_argument("--city", default=None, help="ограничить одним городом сайта")
    ap.add_argument("--delay", type=float, default=0.5,
                    help="пауза между запросами; два скрипта против API одновременно "
                         "заметно поднимают долю ошибок -- не запускайте параллельно")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    from site_data import load_listings
    coords = load_coords()
    todo = []
    for l in load_listings():
        if l["source"] != "chotot":
            continue
        if a.city and l["city"] != a.city:
            continue
        m = AD_ID.search(l.get("url", ""))
        if not m:
            continue
        aid = m.group(1)
        if str(l["id"]) in coords or aid in coords:
            continue
        todo.append((l["id"], aid, l["city"]))

    print("без координат объявления: %d%s" % (len(todo), "" if not a.city else " (%s)" % a.city))
    if a.dry_run or not todo:
        return 0

    got = gone = failed = 0
    for n, (lid, aid, city) in enumerate(todo[:a.limit], 1):
        res = fetch(aid)
        if res == "gone":
            gone += 1
        elif res:
            coords[aid] = {"lat": res[0], "lon": res[1]}
            got += 1
            if got % 25 == 0:
                save_coords(coords)          # длинный прогон не должен пропадать целиком
        else:
            failed += 1
        if n % 50 == 0:
            print("   ...%d из %d: добыто %d, снято %d, не ответило %d"
                  % (n, min(len(todo), a.limit), got, gone, failed))
        time.sleep(a.delay)

    save_coords(coords)
    print("добыто координат: %d, объявление снято: %d, не ответило: %d (всего в файле %d)"
          % (got, gone, failed, len(coords)))
    if gone:
        print("снятые не удалялись -- это дело remove_gone_listings.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
