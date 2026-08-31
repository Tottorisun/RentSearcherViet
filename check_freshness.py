# -*- coding: utf-8 -*-
"""Verify how old a Chợ Tốt ad really is, before it is added to the base.

Why this exists. The daily checks decide freshness from whatever the fetch
script happened to print. On 31 Aug 2026 five listings went in dated "today"
while being 2 to 12.3 days old: the detail responses had contained
`orig_list_time` all along, but the script that printed them showed
subject/price/ward/body and not that field, so nobody saw it. The data was
there; the summary hid it. This tool prints the verdict itself instead of
raw fields, so it cannot be skimmed past.

Verdicts:
  FRESH        orig_list_time present and within --max-days
  STALE        orig_list_time present and older, OR list_time alone is older
               (an ad cannot be newer than its own last re-push, so an old
               list_time is proof of age even with no original stamp)
  UNVERIFIABLE orig_list_time absent and list_time is recent -- the original
               post date is not obtainable from this API. Measured 31 Aug 2026
               at 34.5% of ads (138 of 400), stable per ad: re-fetching does
               not recover it, and the ad's list_id cannot substitute (id
               ranges of verified-fresh and verified-old ads overlap).
               Per the daily-check prompts: skip these.

Exit code is 1 unless every ad checked is FRESH, so a wrapper cannot ignore
the result by accident.

Usage:
  python check_freshness.py 134447676 134132556
  python check_freshness.py --from-json candidates.json     # reads list_id keys
  python check_freshness.py --from-file ids.txt             # one id per line
  python check_freshness.py --in-base                       # re-check what is
                                                            # already stored
Options:
  --max-days N   freshness cutoff (default 14, the site's own cutoff)
"""
import json, re, sys, time, urllib.request

# reconfigure, never `sys.stdout = io.TextIOWrapper(sys.stdout.buffer, ...)`:
# that wrapper closes the underlying stream when it is garbage-collected, and
# every later print dies with "I/O operation on closed file". In a background
# run it looks like a hang -- process alive, log empty.
sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
DETAIL = "https://gateway.chotot.com/v2/public/ad-listing/{}"


def fetch(list_id):
    req = urllib.request.Request(DETAIL.format(list_id), headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8")).get("ad", {})


def verdict(ad, now, max_days):
    orig, last = ad.get("orig_list_time"), ad.get("list_time")
    if orig:
        age = (now - orig / 1000) / 86400
        return ("FRESH" if age <= max_days else "STALE"), age, "orig_list_time"
    if last:
        age = (now - last / 1000) / 86400
        # list_time is the LAST re-push: old here proves the ad is old, but
        # recent here proves nothing about the original posting.
        if age > max_days:
            return "STALE", age, "list_time (re-push)"
        return "UNVERIFIABLE", age, "list_time (re-push) only"
    return "UNVERIFIABLE", None, "no timestamp at all"


def days_ago(age):
    """Whole days, rounded down: an ad 1.9 days old is "1 day ago", not 2."""
    return int(age)


def ru_posted(age):
    """The Russian `posted` string for that age, with correct plural forms
    (2-4 take "дня", 5-20 take "дней"), so the two fields cannot disagree."""
    n = days_ago(age)
    if n == 0:
        return "сегодня"
    if n == 1:
        return "вчера"
    if 11 <= n % 100 <= 14:          # 11-14 take "дней" despite ending in 1-4
        return f"{n} дней назад"
    last = n % 10
    if last == 1:
        return f"{n} день назад"     # 21, 31, ... -- singular nominative
    if last in (2, 3, 4):
        return f"{n} дня назад"
    return f"{n} дней назад"


def collect_ids(argv):
    ids, i = [], 0
    while i < len(argv):
        a = argv[i]
        if a == "--from-json":
            i += 1
            data = json.load(open(argv[i], encoding="utf-8"))
            rows = data.values() if isinstance(data, dict) else data
            for r in rows:
                if isinstance(r, dict) and r.get("list_id"):
                    ids.append(r["list_id"])
                elif isinstance(r, (int, str)) and str(r).isdigit():
                    ids.append(int(r))
        elif a == "--from-file":
            i += 1
            ids += [int(l.strip()) for l in open(argv[i], encoding="utf-8")
                    if l.strip().isdigit()]
        elif a == "--in-base":
            html = open("vietnam-rent-finder.html", encoding="utf-8").read()
            data = json.loads(re.search(r"var DATA = (\{.*?\});\s*\n", html, re.S).group(1))
            for l in data["LISTINGS"]:
                if l.get("source") == "chotot":
                    m = re.search(r"/(\d{8,9})\.htm", l.get("url", ""))
                    if m:
                        ids.append(int(m.group(1)))
        elif a.isdigit():
            ids.append(int(a))
        i += 1
    return ids


def main():
    argv = sys.argv[1:]
    max_days = 14.0
    if "--max-days" in argv:
        k = argv.index("--max-days")
        max_days = float(argv[k + 1])
        del argv[k:k + 2]

    ids = collect_ids(argv)
    if not ids:
        sys.exit(__doc__)

    now = time.time()
    counts = {"FRESH": 0, "STALE": 0, "UNVERIFIABLE": 0, "ERROR": 0}
    for lid in ids:
        try:
            v, age, src = verdict(fetch(lid), now, max_days)
        except Exception as ex:
            counts["ERROR"] += 1
            print(f"{lid}  ERROR         {type(ex).__name__}: {ex}")
            continue
        counts[v] += 1
        age_s = f"{age:6.2f}d" if age is not None else "     ?"
        line = f"{lid}  {v:<13} {age_s}  via {src}"
        if v == "FRESH":
            # Hand back the exact field values to write, so the date is never
            # re-derived by eye. Getting this wrong is the whole failure this
            # tool exists for: five listings went in stamped "today" while
            # being 2 to 12 days old.
            line += f'   ->  daysAgo={days_ago(age)}, posted="{ru_posted(age)}"'
        print(line)
        time.sleep(0.3)

    print(f"\nchecked {len(ids)}: " + ", ".join(f"{k} {v}" for k, v in counts.items() if v))
    if counts["STALE"]:
        print("STALE ads are older than the cutoff -- do not add them, and correct "
              "any already in the base.")
    if counts["UNVERIFIABLE"]:
        print("UNVERIFIABLE ads have no obtainable original date -- skip them. Do not "
              "fall back to list_time, and do not try to date them by list_id.")
    sys.exit(0 if counts["FRESH"] == len(ids) else 1)


if __name__ == "__main__":
    main()
