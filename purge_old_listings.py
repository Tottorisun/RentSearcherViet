# -*- coding: utf-8 -*-
"""
Recompute each listing's TRUE current age and drop anything older than the
freshness cutoff (14 days), physically removing its L(...) block from
rebuild_final.py. Run this as a normal step in the daily-check pipeline,
BEFORE the final `python rebuild_final.py` bake-in.

Why this exists: each L(...) call's `daysAgo` argument is a snapshot frozen
at whichever moment that line was written -- it never updates itself as
calendar days pass. Left alone, a listing added "2 days old" a week ago
would still display "2 дня назад" today. This script anchors every listing
to a real absolute post date (backfilled once via git history for anything
already in the file, cached from then on in posted_dates.json) and
recomputes the display fields from that anchor every time it runs.

How blocks are located: through `ast`, not regex. rebuild_final.py is valid
Python, so every L(...) element of the LISTINGS list comes with exact
line numbers and its positional args (id is args[0], posted label args[8],
daysAgo args[9]). The previous regex version silently skipped any block
whose daysAgo was followed by `descEn=` (an older row format) -- four
Da Nang listings stayed on the site for ever with a frozen "14 дней назад"
label and no line in the output saying so. With ast there is nothing to
mis-match, and the rewritten file is re-parsed before it is written.

The whole read-modify-write runs under listing_lock.listings_write_lock so
a concurrent batch insert from another session can neither be overwritten
by this script nor overwrite it.
"""
import ast, re, os, json, datetime
from listing_lock import listings_write_lock, write_source_atomic, SOURCE as SRC

CUTOFF_DAYS = 14

# Источники, которые ВООБЩЕ не публикуют дату размещения. Для них возраст в
# daysAgo -- производная величина (для dotproperty.com.ph он декодируется из
# UUIDv7 в идентификаторе объявления, то есть это момент создания строки в их
# базе), а не дата публикации, и он не сдвигается, когда агент обновляет
# залежавшееся объявление.
#
# Правило 14 дней написано под Chợ Tốt и Batdongsan, где объявления
# оборачиваются за дни. Агентский портал -- другая физика: на весь Думагете там
# двенадцать объявлений, и это и есть рынок. Применять к ним возрастную чистку
# значит гарантированно опустошать филиппинские города через две недели после
# каждого захода, независимо от того, сдаются квартиры или нет.
#
# Поэтому такие источники освобождены от чистки ПО ВОЗРАСТУ, но не от проверки
# на живость: remove_gone_listings.py по-прежнему удаляет их, когда страница
# отвечает 404. Живость здесь -- правильный сигнал, возраст -- нет.
# Подпись "N дней назад" им продолжает пересчитываться, так что карточка не врёт
# о своём возрасте, а в notice каждой такой строки сказано, что дата выведенная.
#
# Facebook Marketplace попадает сюда по той же причине, но с другой стороны.
# Точной даты размещения он для формата «Rentals» не показывает вовсе, поэтому в
# daysAgo у таких строк стоит ВЕРХНЯЯ ГРАНИЦА, а не возраст: объявление
# проверено повторным проходом ленты с daysSinceListed=30 и в ней осталось.
# Верхняя граница в 30 больше порога в 14 всегда, и без этого исключения свежее
# объявление, заведённое сегодня, удалялось бы завтрашним прогоном как
# «старше двух недель» -- при том, что оно заведомо моложе тридцати дней.
# У тех редких объявлений, где Facebook возраст всё-таки показал, стоит он сам,
# и они тоже остаются под проверкой на живость.
DATELESS_SOURCES = {"dotproperty", "fbmarketplace"}
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

def const(node):
    return node.value if isinstance(node, ast.Constant) else None


def main():
    today = datetime.date.today()
    try:
        posted_dates = json.load(open(POSTED_DATES_FILE, encoding="utf-8"))
    except FileNotFoundError:
        posted_dates = {}

    with listings_write_lock("purge_old_listings"):
        src = open(SRC, encoding="utf-8").read()
        tree = ast.parse(src)
        lines = src.split("\n")

        listings_assign = [n for n in tree.body
                           if isinstance(n, ast.Assign)
                           and any(getattr(t, "id", None) == "LISTINGS" for t in n.targets)]
        if len(listings_assign) != 1 or not isinstance(listings_assign[0].value, ast.List):
            raise SystemExit("could not find exactly one `LISTINGS = [...]` list in rebuild_final.py -- refusing to touch the file")
        elements = listings_assign[0].value.elts

        blocks = []   # (lineno, end_lineno, id, posted_label_old, days_ago_old)
        skipped = []
        for e in elements:
            ok = (isinstance(e, ast.Call) and getattr(e.func, "id", None) == "L" and len(e.args) >= 10
                  and lines[e.lineno - 1].startswith("L(") and lines[e.end_lineno - 1].rstrip().endswith("),"))
            lid = const(e.args[0]) if ok else None
            posted_old = const(e.args[8]) if ok else None
            days_old = const(e.args[9]) if ok else None
            if not ok or lid is None or not isinstance(days_old, int) or not isinstance(posted_old, str):
                # never guess/delete on a block we don't fully understand -- but SAY so
                skipped.append((getattr(e, "lineno", "?"), lid))
                continue
            src_kw = next((const(k.value) for k in e.keywords if k.arg == "source"), "chotot")
            blocks.append((e.lineno, e.end_lineno, str(lid), posted_old, days_old, src_kw))

        if skipped:
            print(f"WARNING: {len(skipped)} block(s) could not be parsed as a plain L(id,...,posted,daysAgo,...) call and were left untouched:")
            for ln, lid in skipped:
                print(f"  line {ln}: id={lid}")

        kept = 0
        removed_ids = []
        relabelled = 0
        # Edit from the bottom up so earlier line numbers stay valid.
        for lineno, end_lineno, lid, posted_old, days_old, src_kw in sorted(blocks, key=lambda b: b[0], reverse=True):
            if lid in posted_dates:
                anchor = datetime.date.fromisoformat(posted_dates[lid])
            else:
                anchor = today - datetime.timedelta(days=days_old)
                posted_dates[lid] = anchor.isoformat()
            true_days = (today - anchor).days

            if true_days > CUTOFF_DAYS and src_kw not in DATELESS_SOURCES:
                removed_ids.append(lid)
                del posted_dates[lid]
                start, end = lineno - 1, end_lineno          # slice bounds over `lines`
                # also eat one following blank line, so removals don't leave double gaps
                if end < len(lines) and lines[end].strip() == "":
                    end += 1
                del lines[start:end]
                continue

            kept += 1
            if true_days != days_old or posted_old != posted_label(true_days):
                new_label = posted_label(true_days)
                block_text = "\n".join(lines[lineno - 1:end_lineno])
                pattern = '"' + re.escape(posted_old) + '",' + str(days_old)
                new_block, n = re.subn(pattern, '"' + new_label + '",' + str(true_days), block_text, count=1)
                if n != 1:
                    raise SystemExit(f"id {lid}: expected exactly one `\"{posted_old}\",{days_old}` in its block, found {n} -- refusing to write")
                lines[lineno - 1:end_lineno] = new_block.split("\n")
                relabelled += 1

        new_src = "\n".join(lines)

        # Safety net: the result must still parse and hold exactly the expected number of blocks.
        try:
            new_tree = ast.parse(new_src)
        except SyntaxError as ex:
            raise SystemExit(f"rewritten rebuild_final.py does not parse ({ex}) -- NOT written, original left intact")
        new_count = len([n for n in new_tree.body if isinstance(n, ast.Assign)
                         and any(getattr(t, "id", None) == "LISTINGS" for t in n.targets)][0].value.elts)
        expected = len(elements) - len(removed_ids)
        if new_count != expected:
            raise SystemExit(f"block count after rewrite is {new_count}, expected {expected} -- NOT written, original left intact")

        write_source_atomic(new_src)

    tmp_pd = POSTED_DATES_FILE + ".tmp"
    with open(tmp_pd, "w", encoding="utf-8") as f:
        json.dump(posted_dates, f, ensure_ascii=False, indent=1)
    os.replace(tmp_pd, POSTED_DATES_FILE)

    print(f"kept: {kept}, relabelled: {relabelled}, removed (>{CUTOFF_DAYS} days old): {len(removed_ids)}")
    if removed_ids:
        print("removed ids:", ", ".join(removed_ids))


if __name__ == "__main__":
    main()
