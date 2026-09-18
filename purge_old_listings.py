# -*- coding: utf-8 -*-
"""
Work out each listing's TRUE current age and drop anything older than the
freshness cutoff (7 days), removing its row from listings/<source>/<city>.jsonl.
Run this as a normal step in the daily-check pipeline, BEFORE the final
`python rebuild_final.py` bake-in.

Why this exists: each L(...) call's `daysAgo` argument is a snapshot frozen
at whichever moment that line was written -- it never updates itself as
calendar days pass. Left alone, a listing added "2 days old" a week ago
would still display "2 дня назад" today. This script anchors every listing
to a real absolute post date (backfilled once via git history for anything
already in the file, cached from then on in posted_dates.json). Since 18 Sep
2026 it no longer rewrites the display fields (posted, daysAgo) in the rows:
the build computes them from the same anchor (listing_lock.with_current_age),
so a purge changes a row file only when it removes a row.

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
from listing_lock import listings_write_lock, load_rows, save_rows, row_path, row_anchor

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
        drop = set()
        # С конца порядка сайта, как прежде снизу файла вверх: от порядка зависят
        # список снятых id в выводе и порядок ключей в posted_dates.json.
        for r in reversed(plain):
            lid = str(r["id"])
            src_kw = r.get("source", "chotot")
            # Дата выкладки: записанная раньше, иначе postedOn самой строки (он
            # точнее «сегодня минус daysAgo»: чистка может впервые увидеть строку
            # на следующий день -- так бывает со строками вечернего прогона ПК),
            # иначе -- сегодня минус daysAgo, записанный при заведении.
            anchor = row_anchor(r, posted_dates, today)
            if anchor is None:
                anchor = today - datetime.timedelta(days=r["daysAgo"])
            posted_dates.setdefault(lid, anchor.isoformat())
            true_days = (today - anchor).days

            if true_days > CUTOFF_DAYS and src_kw not in DATELESS_SOURCES:
                removed_ids.append(lid)
                del posted_dates[lid]
                drop.add(r["id"])
                continue
            kept += 1

        # Метки posted/daysAgo в строках не переписываются: возраст на сегодня
        # считает сборка от posted_dates.json (listing_lock.with_current_age).
        if drop:
            save_rows([r for r in rows if r["id"] not in drop])

    tmp_pd = POSTED_DATES_FILE + ".tmp"
    with open(tmp_pd, "w", encoding="utf-8") as f:
        json.dump(posted_dates, f, ensure_ascii=False, indent=1)
    os.replace(tmp_pd, POSTED_DATES_FILE)

    print(f"kept: {kept}, removed (>{CUTOFF_DAYS} days old): {len(removed_ids)}")
    if removed_ids:
        print("removed ids:", ", ".join(removed_ids))


if __name__ == "__main__":
    main()
