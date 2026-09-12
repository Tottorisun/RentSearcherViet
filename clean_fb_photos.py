# -*- coding: utf-8 -*-
"""Удаление скачанных фотографий Facebook, которые ни одной строке сайта не нужны.

ЗАЧЕМ. fb_collect.py скачивает фотографии КАЖДОГО кандидата -- иначе их негде
взять потом: ссылки Facebook на изображения подписаны и живут около четырёх
дней. Но заводится из кандидатов меньшинство, и папки остальных остаются на
диске навсегда. 12 сентября 2026 их набралось шесть десятков на сотню с лишним
мегабайт, и все они висели в `git status` неотслеживаемыми -- то есть любая
команда `git add -A` могла смести их в публичный репозиторий целиком.

ЧТО УДАЛЯЕТСЯ. Папка assets/fb_photos/<post_id>, если:
  * ни одна строка сайта на неё не ссылается (site_data -- единственный
    читатель данных), И
  * она не отслеживается git (то есть её фотографии не опубликованы), И
  * она старше MIN_AGE_HOURS часов -- свежие не трогаем: кандидат этого
    прогона может быть заведён сессией вручную через час.

Потерять этим нельзя ничего, кроме повторного скачивания: если пост позже
всё-таки заводят, а фотографий уже нет, ingest_facebook.py такую строку просто
не заведёт (он проверяет файлы на диске), и кандидат снова попадёт в сбор.

    python clean_fb_photos.py            показать, что удалилось бы
    python clean_fb_photos.py --apply    удалить
"""
import argparse
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO_DIR = os.path.join("assets", "fb_photos")
MIN_AGE_HOURS = 36


def dir_size(path):
    total = 0
    for root, _dirs, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total


def main():
    ap = argparse.ArgumentParser(description="чистка неиспользуемых фотографий Facebook")
    ap.add_argument("--apply", action="store_true", help="удалить (без него -- только отчёт)")
    ap.add_argument("--hours", type=float, default=MIN_AGE_HOURS)
    a = ap.parse_args()
    os.chdir(HERE)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not os.path.isdir(PHOTO_DIR):
        print("нет каталога %s -- нечего чистить" % PHOTO_DIR)
        return 0

    from site_data import load_listings
    used = set()
    for l in load_listings():
        for p in (l.get("details") or {}).get("photos", []) or []:
            if p.startswith("assets/fb_photos/"):
                used.add(p.split("/")[2])
    tracked = set()
    out = subprocess.run(["git", "ls-files", PHOTO_DIR], capture_output=True, text=True,
                         encoding="utf-8").stdout.split()
    for f in out:
        parts = f.split("/")
        if len(parts) > 2:
            tracked.add(parts[2])

    import time
    now = time.time()
    victims, kept_fresh, total = [], 0, 0
    for name in sorted(os.listdir(PHOTO_DIR)):
        path = os.path.join(PHOTO_DIR, name)
        if not os.path.isdir(path):
            continue
        total += 1
        if name in used or name in tracked:
            continue
        if now - os.path.getmtime(path) < a.hours * 3600:
            kept_fresh += 1
            continue
        victims.append((path, dir_size(path)))

    mb = sum(s for _p, s in victims) / 1048576.0
    print("папок всего %d; на сайте нужны %d; свежих (моложе %g ч) оставлено %d; "
          "к удалению %d (%.1f МБ)" % (total, len(used), a.hours, kept_fresh, len(victims), mb))
    if not victims:
        return 0
    if not a.apply:
        for p, s in victims[:10]:
            print("  %s  %.1f МБ" % (p, s / 1048576.0))
        if len(victims) > 10:
            print("  ... и ещё %d" % (len(victims) - 10))
        print("режим отчёта -- ничего не удалено; удалить: python clean_fb_photos.py --apply")
        return 0
    for p, _s in victims:
        shutil.rmtree(p, ignore_errors=True)
    print("удалено папок: %d, освобождено %.1f МБ" % (len(victims), mb))
    return 0


if __name__ == "__main__":
    sys.exit(main())
