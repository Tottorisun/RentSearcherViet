# -*- coding: utf-8 -*-
"""
Recompute each listing's TRUE current age and drop anything older than the
freshness cutoff (7 days), removing its row from listings/<source>/<city>.jsonl.
Run this as a normal step in the daily-check pipeline, BEFORE the final
`python rebuild_final.py` bake-in.

Why this exists: each L(...) call's `daysAgo` argument is a snapshot frozen
at whichever moment that line was written -- it never updates itself as
calendar days pass. Left alone, a listing added "2 days old" a week ago
would still display "2 дня назад" today. This script anchors every listing
to a real absolute post date (backfilled once via git history for anything
already in the file, cached from then on in posted_dates.json) and
recomputes the display fields from that anchor every time it runs.

Where rows live: since 17 Sep 2026 in listings/<source>/<city>.jsonl, one JSON
object per line (listing_lock.load_rows/save_rows); before that they were
L(...) calls inside rebuild_final.py. A row without a plain id, posted label
and daysAgo is reported and left untouched, never guessed at: a regex version
of this script once skipped rows silently, and four Da Nang listings stayed on
the site for ever with a frozen "14 дней назад" label.

The whole read-modify-write runs under listing_lock.listings_write_lock so
a concurrent batch insert from another session can neither be overwritten
by this script nor overwrite it.
"""
import os, json, datetime
from listing_lock import listings_write_lock, load_rows, save_rows, row_path

CUTOFF_DAYS = 7

# Исключений по источнику больше нет -- решение владельца 14.09.2026: «всё, что
# старше 7 дней, у нас убирается». Дата у каждой строки -- день, когда объявление
# выложено (у перевыложенного -- день перевыкладки), и если хозяин выложит его
# снова, оно заводится заново и показывается ещё 7 дней. Раньше dotproperty,
# Facebook Marketplace и группы Facebook были освобождены: у dotproperty дата --
# создание записи на портале, и она не сдвигается, когда агент обновляет
# объявление, а у Marketplace в возрасте стояла верхняя граница «не старше 30
# дней». Цена решения названа владельцу до правки: филиппинские объявления
# dotproperty уходят через 7 дней после создания, даже если квартира ещё
# сдаётся, а строки Marketplace с верхней границей -- сразу.
DATELESS_SOURCES = set()
POSTED_DATES_FILE = "posted_dates.json"

RU_DAY_WORDS = ["день", "дня", "дней"]
def ru_day_word(n):
    n = abs(n)
    if n % 10 == 1 and n % 100 != 11:
        return RU_DAY_WORDS[0]
    if 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
        return RU_DAY_WORDS[1]
    return RU_DAY_WORDS[2]

def posted_label(days_ago):
    if days_ago <= 0:
        return "сегодня"
    if days_ago == 1:
        return "вчера"
    return f"{days_ago} {ru_day_word(days_ago)} назад"

def main():
    today = datetime.date.today()
    try:
        posted_dates = json.load(open(POSTED_DATES_FILE, encoding="utf-8"))
    except FileNotFoundError:
        posted_dates = {}

    with listings_write_lock("purge_old_listings"):
        rows = load_rows()
        plain = [r for r in rows if isinstance(r.get("id"), int) and isinstance(r.get("daysAgo"), int)
                 and isinstance(r.get("posted"), str)]
        if len(plain) != len(rows):
            print(f"WARNING: {len(rows) - len(plain)} row(s) have no plain id/posted/daysAgo and were left untouched:")
            for r in rows:
                if r not in plain:
                    print(f"  {row_path(r)}: id={r.get('id')}")

        kept = 0
        removed_ids = []
        relabelled = 0
        drop = set()
        # С конца порядка сайта, как прежде снизу файла вверх: от порядка зависят
        # список снятых id в выводе и порядок ключей в posted_dates.json.
        for r in reversed(plain):
            lid, posted_old, days_old = str(r["id"]), r["posted"], r["daysAgo"]
            src_kw = r.get("source", "chotot")
            posted_on = r.get("postedOn")
            if lid in posted_dates:
                anchor = datetime.date.fromisoformat(posted_dates[lid])
            else:
                # Дата выкладки из самой строки точнее «сегодня минус daysAgo»:
                # daysAgo считан, когда строку записали, а чистка может впервые
                # увидеть её на следующий день -- так бывает со строками вечернего
                # прогона ПК (см. postedOn в L() шаблона).
                try:
                    anchor = datetime.date.fromisoformat(posted_on) if isinstance(posted_on, str) else None
                except ValueError:
                    anchor = None
                if anchor is None or anchor > today:
                    anchor = today - datetime.timedelta(days=days_old)
                posted_dates[lid] = anchor.isoformat()
            true_days = (today - anchor).days

            if true_days > CUTOFF_DAYS and src_kw not in DATELESS_SOURCES:
                removed_ids.append(lid)
                del posted_dates[lid]
                drop.add(r["id"])
                continue

            kept += 1
            if true_days != days_old or posted_old != posted_label(true_days):
                r["posted"] = posted_label(true_days)
                r["daysAgo"] = true_days
                relabelled += 1

        save_rows([r for r in rows if r["id"] not in drop])

    tmp_pd = POSTED_DATES_FILE + ".tmp"
    with open(tmp_pd, "w", encoding="utf-8") as f:
        json.dump(posted_dates, f, ensure_ascii=False, indent=1)
    os.replace(tmp_pd, POSTED_DATES_FILE)

    print(f"kept: {kept}, relabelled: {relabelled}, removed (>{CUTOFF_DAYS} days old): {len(removed_ids)}")
    if removed_ids:
        print("removed ids:", ", ".join(removed_ids))


if __name__ == "__main__":
    main()
