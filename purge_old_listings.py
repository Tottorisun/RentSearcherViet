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
"""
import re, json, datetime

CUTOFF_DAYS = 14
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

today = datetime.date.today()

try:
    posted_dates = json.load(open(POSTED_DATES_FILE, encoding="utf-8"))
except FileNotFoundError:
    posted_dates = {}

src = open("rebuild_final.py", encoding="utf-8").read()

# Parse each L(...) call: id, then skip to the daysAgo positional arg (7th
# top-level arg: id,city,district,type,price,area,desc,url,posted,daysAgo,...).
# Full-block regex mirrors the pattern already used elsewhere in this project
# (_dupe_scan.py, _resolve_conflict.py) for locating a listing's whole span.
block_re = re.compile(r'^L\((\d+),.*?\),\s*$', re.M | re.S)

kept = 0
removed_ids = []
new_src_parts = []
last_end = 0

for m in block_re.finditer(src):
    block = m.group(0)
    lid = m.group(1)
    days_m = re.search(r'"[^"]*",(\d+)(?:,\s*(?:source=|details=)|\))', block)
    if not days_m:
        # couldn't confidently locate daysAgo -- leave this block untouched,
        # never guess/delete on uncertain data
        continue
    old_days_ago = int(days_m.group(1))

    if lid in posted_dates:
        anchor = datetime.date.fromisoformat(posted_dates[lid])
    else:
        anchor = today - datetime.timedelta(days=old_days_ago)
        posted_dates[lid] = anchor.isoformat()

    true_days_ago = (today - anchor).days

    if true_days_ago > CUTOFF_DAYS:
        removed_ids.append(lid)
        del posted_dates[lid]
        # drop this block (and its blank line separator) from the output
        new_src_parts.append(src[last_end:m.start()])
        last_end = m.end()
        # also eat one following blank line if present, to avoid double gaps
        if src[last_end:last_end+1] == "\n":
            last_end += 1
        continue

    kept += 1
    if true_days_ago != old_days_ago:
        new_posted = posted_label(true_days_ago)
        # replace the "<old posted label>",<old_days_ago> pair with fresh values,
        # preserving whatever separator follows (,source=  or  ,\s*details=  or  closing paren)
        updated_block = re.sub(
            r'"[^"]*",' + str(old_days_ago) + r'(?=,\s*(?:source=|details=)|\))',
            '"' + new_posted + '",' + str(true_days_ago),
            block, count=1
        )
        new_src_parts.append(src[last_end:m.start()])
        new_src_parts.append(updated_block)
        last_end = m.end()

new_src_parts.append(src[last_end:])
new_src = "".join(new_src_parts)

open("rebuild_final.py", "w", encoding="utf-8").write(new_src)
json.dump(posted_dates, open(POSTED_DATES_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print(f"kept: {kept}, removed (>{CUTOFF_DAYS} days old): {len(removed_ids)}")
if removed_ids:
    print("removed ids:", ", ".join(removed_ids))
