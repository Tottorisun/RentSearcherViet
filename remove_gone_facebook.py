# -*- coding: utf-8 -*-
"""Проверка «жив ли пост» для строк Facebook -- входом владельца, на ПК.

ЗАЧЕМ. Строки Facebook (fbgroup, fbmarketplace) не проверял никто. Серверный
remove_gone_web.py пишет прямо: «НЕ проверяется здесь: строки Facebook -- на
запрос без сессии он отвечает HTTP 400 одинаково на живое и на снятое». Строка
висела до чистки по возрасту, а возраст у Facebook отсчитывается от проверки:
14.09.2026 на сайте было 45 строк «37 дней назад». Владелец разрешил проверять
своим входом (14.09.2026). Здесь тот же профиль _fb_profile, то же видимое окно
Chrome и тот же перехват пишущих запросов, что у ежедневного fb_collect.py, --
для Facebook это не новое поведение, а те же просмотры.

ЧТО СЧИТАЕТСЯ ПРОПАЖЕЙ. Замерено 14.09.2026 на восьми страницах этим профилем:
  живой пост группы            текст 2200-2950 знаков, role="article" 2-10
  живое объявление Marketplace  текст 2300-2700, статьи нет, заголовок «Marketplace - ...»
  несуществующий пост           текст 268 знаков, заголовок «Facebook»,
  и объявление                  «This content isn't available right now»
Пропажа -- только надпись о недоступности (fb_collect.UNAVAILABLE_RE) на почти
пустой странице без статьи. Всё незнакомое -- «неясно», строка остаётся.

У MARKETPLACE СВОЙ ПРИЗНАК -- замерено тем же днём на двух объявлениях, которые
первый живой отчёт оставил «неясными»: Facebook перенаправляет на
/marketplace/<город>/?unavailable_product=1 и пишет «This listing isn't available
anymore. It may have been sold or expired», а ниже -- лента чужих объявлений,
поэтому страница длинная и под правило «почти пустой страницы» не подходит.
Параметр в адресе -- признак самого Facebook, надёжнее текста; текст -- запасной.

ТА ЖЕ НАДПИСЬ -- И У СКРЫТОГО. Facebook пишет «isn't available» и про удалённый
пост, и про пост, который аккаунту не виден: владелец вышел из группы, группу
закрыли. Поэтому если в прогоне у одной группы пропали HIDDEN_GROUP_MIN постов и
больше, а живых из неё не видно ни одного, эти строки не снимаются: это
разбирает человек, и шаг завершается с кодом 1, чтобы сводка его назвала.

ПОТОЛОК. MAX_GONE пропаж или больше MAX_GONE_SHARE проверенных -- не снимается
ничего: так выглядит стена Facebook или сломанный разбор, а не удалённые посты.
Стена входа или проверка безопасности -- немедленная остановка
(fb_collect.check_alive); отвечать на неё скрипт не будет.

ФОТОГРАФИИ. Снимки строк Facebook лежат в репозитории (assets/fb_photos/<пост>).
Папка снятой строки удаляется тем же коммитом, если на неё не ссылается другая
строка, -- иначе её не удалил бы никто: clean_fb_photos.py трогает только
неотслеживаемые папки.

    python remove_gone_facebook.py                   отчёт по DEFAULT_LIMIT строк
    python remove_gone_facebook.py --limit 6         отчёт по 6
    python remove_gone_facebook.py --apply           снять пропавшие
    python remove_gone_facebook.py --apply --commit  снять и закоммитить (прогон ПК)
"""
import argparse
import collections
import json
import os
import random
import re
import shutil
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

import fb_collect as fc
import repo_sync
from listing_lock import listing_ids, remove_listings
from site_data import load_listings

# Не «_fb_…»: под этот шаблон ingest_facebook.py ищет файлы кандидатов, и память
# проверки печаталась в его логе как «это не файл кандидатов fb_collect».
CACHE_FILE = "_liveness_facebook_cache.json"   # git-ignored (_*): знание этой машины
OLD_CACHE_FILE = "_fb_liveness_cache.json"     # прежнее имя, переносится при первом чтении
DEFAULT_LIMIT = 25
MAX_GONE = 15
# Половина, а не четверть, как у Telegram: проверяются в первую очередь самые
# давно не проверенные строки, и среди них доля настоящих пропаж выше.
MAX_GONE_SHARE = 0.5
HIDDEN_GROUP_MIN = 3
SHORT_PAGE = 1200                        # живые страницы замера -- от 2200 знаков
GROUP_POST = re.compile(r"facebook\.com/groups/([^/?#]+)/posts/(\d+)")
MARKET_ITEM = re.compile(r"facebook\.com/marketplace/item/(\d+)")
MARKET_TITLE = re.compile(r"^(?:\(\d+\)\s*)?Marketplace\s*[-–]", re.I)
MARKET_GONE_TEXT = re.compile(r"this listing isn'?t available anymore|tin rao này không còn", re.I)


def verdict(title, body, articles, url, final_url=""):
    """(gone | alive | unclear, почему) -- по признакам, замеренным 14.09.2026."""
    body = body or ""
    if MARKET_ITEM.search(url or ""):
        if "unavailable_product=1" in (final_url or ""):
            return "gone", "Marketplace: объявление снято или продано (unavailable_product)"
        if MARKET_GONE_TEXT.search(body):
            return "gone", "Marketplace: «This listing isn't available anymore»"
    if fc.UNAVAILABLE_RE.search(body):
        if len(body) < SHORT_PAGE and not articles:
            return "gone", "Facebook: «This content isn't available»"
        return "unclear", "надпись о недоступности на полной странице"
    if GROUP_POST.search(url or ""):
        if articles:
            return "alive", None
        return "unclear", "страница поста без статьи и без надписи о недоступности"
    if MARKET_ITEM.search(url or ""):
        if MARKET_TITLE.search(title or "") and len(body) >= SHORT_PAGE:
            return "alive", None
        return "unclear", "страница не похожа на объявление Marketplace"
    return "unclear", "ссылка не на пост и не на объявление"


def load_cache():
    if not os.path.exists(CACHE_FILE) and os.path.exists(OLD_CACHE_FILE):
        os.replace(OLD_CACHE_FILE, CACHE_FILE)
    try:
        return json.load(open(CACHE_FILE, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_cache(cache):
    tmp = CACHE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, CACHE_FILE)


def group_of(url):
    m = GROUP_POST.search(url or "")
    return m.group(1) if m else None


def photo_dirs(rows):
    out = set()
    for l in rows:
        for p in (l.get("details") or {}).get("photos") or []:
            if isinstance(p, str) and p.startswith("assets/fb_photos/"):
                out.add(os.path.dirname(p))
    return out


def check_rows(todo, cache):
    """Открывает посты по одному. (gone, alive, unclear) или None, если выходить."""
    from playwright.sync_api import sync_playwright
    gone, alive, unclear = [], [], []
    now = int(time.time())
    with sync_playwright() as pw:
        ctx = fc.open_context(pw, headless=False, channel="chrome")
        try:
            if not fc.is_logged_in(ctx):
                print("профиль Facebook не залогинен -- нужен вход руками: python fb_collect.py --login")
                return None
            page = ctx.pages[0] if ctx.pages else ctx.new_page()
            for i, l in enumerate(todo):
                url = l["url"]
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=60000)
                    time.sleep(random.uniform(5, 8))
                    fc.check_alive(page)             # стена входа / проверка -- SystemExit
                    body = page.inner_text("body", timeout=8000)
                    title = page.title()
                    articles = page.locator('[role="article"]').count()
                    final_url = page.url
                except SystemExit:
                    raise
                except Exception as e:
                    unclear.append((l, "страница не открылась: %s" % str(e).splitlines()[0][:90]))
                    continue
                v, why = verdict(title, body, articles, url, final_url)
                if v == "alive":
                    alive.append(l)
                    cache[str(l["id"])] = {"checked": now}
                elif v == "gone":
                    gone.append((l, why))
                else:
                    unclear.append((l, why))
                if len(unclear) >= 8 and not alive and not gone:
                    print("8 незнакомых страниц и ни одной живой -- Facebook отдаёт что-то другое; "
                          "выхожу без изменений")
                    return None
                if i + 1 < len(todo):
                    time.sleep(random.uniform(8, 15))
        finally:
            ctx.close()
    return gone, alive, unclear


def main():
    ap = argparse.ArgumentParser(description="снятые посты Facebook: проверка входом владельца")
    ap.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    ap.add_argument("--all", action="store_true", help="все проверяемые строки за прогон")
    ap.add_argument("--apply", action="store_true", help="снять пропавшие строки")
    ap.add_argument("--commit", action="store_true", help="закоммитить снятие (вместе с --apply)")
    a = ap.parse_args()

    listings = load_listings()
    # Строки берутся из собранной страницы, а она на ПК свежа лишь на момент последней
    # подтяжки репозитория. 15.09 утром проверка снова «нашла пропавшими» 3000232 и
    # 3000237, снятые накануне: страница была ещё вчерашней, потому что шаг Facebook
    # перед проверкой ничего не завёл и репозиторий не подтягивал. Две из 25 проверок
    # ушли впустую. Проверяются только строки, которые есть в самом rebuild_final.py.
    present = set(listing_ids())
    fb = [l for l in listings if (l.get("source") or "").startswith("fb") and l["id"] in present]
    rows = [l for l in fb if GROUP_POST.search(l.get("url") or "") or MARKET_ITEM.search(l.get("url") or "")]
    cache = load_cache()
    rows.sort(key=lambda l: cache.get(str(l["id"]), {}).get("checked", 0))
    todo = rows if a.all else rows[:a.limit]
    print("строк Facebook на сайте: %d, со ссылкой на пост или объявление: %d, проверяю %d%s"
          % (len(fb), len(rows), len(todo), "" if a.apply else " -- режим отчёта, ничего не снимаю"))
    if len(fb) > len(rows):
        print("НЕ проверяется: %d строк ссылаются на группу без номера поста -- по такой ссылке "
              "не видно, что стало с объявлением" % (len(fb) - len(rows)))
    if not todo:
        return 0

    t0 = time.time()
    res = check_rows(todo, cache)
    save_cache(cache)
    if res is None:
        return 1
    gone, alive, unclear = res

    alive_groups = collections.Counter(group_of(l["url"]) for l in alive)
    by_group = collections.defaultdict(list)
    for item in gone:
        by_group[group_of(item[0]["url"])].append(item)
    hidden = [item for g, items in by_group.items()
              if g and len(items) >= HIDDEN_GROUP_MIN and not alive_groups.get(g) for item in items]
    gone = [item for item in gone if item not in hidden]

    print("проверено %d за %.0f с: живых %d, пропало %d, неясных %d, скрыто группой %d"
          % (len(todo), time.time() - t0, len(alive), len(gone), len(unclear), len(hidden)))
    for l, why in gone:
        print("  ПРОПАЛ  %s  (%s, %s): %s" % (l["id"], l["city"], l["url"], why))
    for l, why in unclear:
        print("  неясно  %s  (%s): %s -- пропавшим НЕ считаю" % (l["id"], l["url"], why))
    for g in sorted({group_of(l["url"]) for l, _ in hidden}):
        print("  ГРУППА НЕДОСТУПНА  %s: %d постов «isn't available», живых нет -- похоже, аккаунт "
              "вышел из группы или её закрыли; строки НЕ сняты, проверьте руками"
              % (g, sum(1 for l, _ in hidden if group_of(l["url"]) == g)))

    if not a.apply:
        print("режим отчёта -- ничего не снято; снять: python remove_gone_facebook.py --apply")
        return 0
    if not gone:
        return 1 if hidden else 0
    if len(gone) >= MAX_GONE or len(gone) > len(todo) * MAX_GONE_SHARE:
        print("пропавших %d из %d проверенных -- на удалённые посты это не похоже (потолок: %d штук "
              "или половина проверенных); ничего не снято, разберитесь глазами"
              % (len(gone), len(todo), MAX_GONE))
        return 1

    ids = sorted(l["id"] for l, _ in gone)
    if a.commit:
        why = repo_sync.prepare(["listings"])
        if why:
            print("снятие отложено -- %s" % why)
            return 1
    keep = photo_dirs([l for l in listings if l["id"] not in set(ids)])
    dirs = sorted(photo_dirs([l for l, _ in gone]) - keep)
    tracked = [d for d in dirs if (repo_sync.git("ls-files", "--", d).stdout or "").strip()]
    removed = remove_listings(ids, owner=__file__)
    for d in dirs:
        if os.path.isdir(d):
            shutil.rmtree(d)
    for i in ids:
        cache.pop(str(i), None)
    save_cache(cache)
    print("снято строк: %d (%s); папок фото удалено: %d" % (len(removed), ", ".join(map(str, removed)), len(dirs)))
    if not a.commit or not removed:
        return 0 if not hidden else 1

    msg = ("Facebook: %d removed by the program -- the posts are gone\n\n"
           "remove_gone_facebook.py opened each post with the owner's Facebook session and\n"
           "found \"This content isn't available\" on an almost empty page:\n%s\n\n"
           "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
           % (len(removed), "\n".join("  %s  %s  %s" % (l["id"], l["city"], l["url"]) for l, _ in gone)))
    err = repo_sync.commit_and_push(["listings"] + tracked, msg,
                                    redo=lambda: None if remove_listings(ids, owner=__file__) is not None
                                    else "снятие не повторилось")
    print(err if err else "закоммичено и запушено: снято %d" % len(removed))
    return 1 if (err or hidden) else 0


if __name__ == "__main__":
    sys.exit(main())
