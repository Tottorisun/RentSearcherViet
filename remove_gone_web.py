# -*- coding: utf-8 -*-
"""Проверка на живость для источников, которые опрашиваются обычным запросом.

Зачем это понадобилось. remove_gone_listings.py проверяет ТОЛЬКО Chợ Tốt --
`if l.get("source") != "chotot": continue`. А dotproperty, hoppler и оба
фейсбучных источника вдобавок освобождены от чистки по возрасту
(DATELESS_SOURCES в purge_old_listings.py), потому что настоящей даты
размещения не публикуют. Вместе это значит, что их не удаляло НИЧТО: ни по
возрасту, ни по живости. На 8 сентября 2026 таких строк 219 -- все филиппинские
объявления сайта, -- и снятые из них не исчезали бы никогда.

Оговорки в этих строках обещают ровно обратное: «объявление проверено и было
доступно». Этот скрипт делает обещание правдой для тех источников, где хватает
простого запроса.

Что проверяется и что нет:
  dotproperty, hoppler -- обычный GET, 404/410 = снято.
  fbmarketplace, fbgroup -- ЗДЕСЬ НЕ ПРОВЕРЯЮТСЯ. Facebook отдаёт стену входа
    любому неавторизованному запросу, поэтому «снято» и «нужен вход» с этой
    стороны неразличимы, а принимать одно за другое значит вычистить живые
    объявления. Их проверяет ручной заход через залогиненный браузер
    (facebook_check_prompt.txt, fb_groups_howto.md). Скрипт печатает, сколько
    таких строк осталось непроверенными, чтобы дыра была видна, а не забыта.

  python remove_gone_web.py --dry-run        только отчёт
  python remove_gone_web.py                  удалить снятые (по умолчанию 120 строк)
  python remove_gone_web.py --all            весь массив (медленно)
  python remove_gone_web.py --limit 50
"""
import json, os, sys, time, urllib.error, urllib.request

from site_data import load_listings
from listing_lock import remove_listings

DRY = "--dry-run" in sys.argv
ALL = "--all" in sys.argv
LIMIT = 120
if "--limit" in sys.argv:
    LIMIT = int(sys.argv[sys.argv.index("--limit") + 1])

CACHE_FILE = "liveness_web_cache.json"
CHECKABLE = {"dotproperty", "hoppler"}
# Facebook отдаёт стену входа, а не 404 -- различить снятое и требующее входа
# без сессии нельзя, поэтому даже не пытаемся.
BROWSER_ONLY = {"fbmarketplace", "fbgroup"}
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
# Портал может ответить 200 и страницей «объявление снято» -- по коду это не
# поймать, поэтому смотрим ещё и в текст.
GONE_MARKERS = ("no longer available", "listing not found", "property not found",
                "this property has been removed", "page not found")


def load_json(path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return default


def save_json(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def check(url):
    """('gone'|'alive'|'error', пояснение). Ошибка транспорта НИКОГДА не 'gone'."""
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            body = r.read(60000).decode("utf-8", "replace").lower()
            for mark in GONE_MARKERS:
                if mark in body:
                    return "gone", "страница отвечает 200, но говорит «%s»" % mark
            return "alive", "%s" % r.status
    except urllib.error.HTTPError as ex:
        if ex.code in (404, 410):
            return "gone", "HTTP %d" % ex.code
        return "error", "HTTP %d" % ex.code
    except Exception as ex:
        return "error", type(ex).__name__


def main():
    listings = load_listings()
    rows = [(l["id"], l["city"], l.get("source"), l["url"])
            for l in listings if l.get("source") in CHECKABLE]
    skipped = [l for l in listings if l.get("source") in BROWSER_ONLY]

    cache = load_json(CACHE_FILE, {})
    rows.sort(key=lambda r: cache.get(str(r[0]), {}).get("checked", 0))
    todo = rows if ALL else rows[:LIMIT]
    print("проверяемых запросом строк: %d (%s), проверяю %d%s"
          % (len(rows), ", ".join(sorted(CHECKABLE)), len(todo), " — сухой прогон" if DRY else ""))
    if skipped:
        print("НЕ проверяется здесь: %d строк Facebook (%s) — только ручным заходом "
              "через залогиненный браузер" % (len(skipped), ", ".join(sorted(BROWSER_ONLY))))

    gone, alive, errors = [], 0, 0
    now = int(time.time())
    t0 = time.time()
    for lid, city, src, url in todo:
        verdict, why = check(url)
        if verdict == "gone":
            gone.append((lid, city, src, why))
            cache[str(lid)] = {"checked": now, "gone": True}
        elif verdict == "alive":
            alive += 1
            cache[str(lid)] = {"checked": now}
        else:
            errors += 1
            print("  %s (%s): %s — снятым НЕ считаю" % (lid, src, why))
            # Портал лёг целиком -- останавливаемся, а не выкашиваем базу.
            if errors >= 10 and alive == 0 and not gone:
                sys.exit("10 ошибок подряд и ни одного ответа — источник недоступен, "
                         "выхожу без изменений")
        time.sleep(0.4)

    print("проверено %d за %.0f с: живых %d, снятых %d, ошибок %d"
          % (len(todo), time.time() - t0, alive, len(gone), errors))
    for lid, city, src, why in gone:
        print("  СНЯТО  %s  (%s, %s): %s" % (lid, city, src, why))

    if DRY:
        print("сухой прогон — ничего не удалено")
        return
    if gone:
        # Блокировку берёт сама remove_listings (listing_lock.py:142). Обёртка
        # снаружи была бы самозахватом: тот же процесс ждал бы замок, который
        # держит он сам, и висел бы до таймаута.
        removed = remove_listings([g[0] for g in gone], owner=__file__)
        print("удалено из rebuild_final.py: %d" % len(removed))
        for lid in [g[0] for g in gone]:
            cache.pop(str(lid), None)
    save_json(CACHE_FILE, cache)


if __name__ == "__main__":
    main()
