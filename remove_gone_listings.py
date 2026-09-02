# -*- coding: utf-8 -*-
"""
Drop listings whose ad has been taken down at the source.

The 14-day purge only knows a listing's age. A flat that gets rented on day
3 stays on the site for another 11 days with a dead link -- measured at
~4-5% of the base at any moment (31 Aug 2026: ~4% overall; 2 Sep 2026: 2 of
the 40 oldest Chợ Tốt rows). This script asks Chợ Tốt whether each ad still
exists (check_freshness.fetch: 404/410 = GONE, anything else = still there
or a transport error, which never counts as gone) and removes the GONE
rows from rebuild_final.py under the write lock, then drops their
posted_dates anchors. Run it BEFORE purge_old_listings.py in the daily
pipeline; cleanup_telegram_posts.py later deletes their hub posts.

A full pass over ~1 800 Chợ Tốt rows takes ~40 minutes at the polite 0.3 s
spacing, so by default a run checks only the --limit (300) rows checked
longest ago (never-checked first), remembering when each ad was last seen
alive in liveness_cache.json (tracked, so the rotation survives across
sessions). Six daily runs cover the whole base.

  python remove_gone_listings.py                 # 300 rows, remove GONE ones
  python remove_gone_listings.py --dry-run       # report only
  python remove_gone_listings.py --all           # whole base (slow)
  python remove_gone_listings.py --limit 100

Only Chợ Tốt rows are checked (93% of the base); Batdongsan, Facebook and
Telegram rows are left to the age purge.
"""
import json, os, re, sys, time
from site_data import load_listings
from listing_lock import remove_listings
import check_freshness as cf

CACHE_FILE = "liveness_cache.json"
POSTED_DATES_FILE = "posted_dates.json"

args = sys.argv[1:]
DRY = "--dry-run" in args
ALL = "--all" in args
LIMIT = int(args[args.index("--limit") + 1]) if "--limit" in args else 300


def load_json(path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except FileNotFoundError:
        return default


def save_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


cache = load_json(CACHE_FILE, {})          # ad id -> {"checked": unix ts, "listing": id}
rows = []
for l in load_listings():
    if l.get("source") != "chotot":
        continue
    m = re.search(r"/(\d{8,9})\.htm", l.get("url", ""))
    if m:
        rows.append((int(m.group(1)), int(l["id"]), l["city"]))

# least-recently-checked first; never-checked rows come before everything
rows.sort(key=lambda r: cache.get(str(r[0]), {}).get("checked", 0))
todo = rows if ALL else rows[:LIMIT]
print("liveness: %d Chợ Tốt rows in the base, checking %d%s" % (len(rows), len(todo), " (dry run)" if DRY else ""))

gone, errors, alive = [], 0, 0
t0 = time.time()
for ad_id, lid, city in todo:
    try:
        cf.fetch(ad_id)
        alive += 1
        cache[str(ad_id)] = {"checked": int(time.time()), "listing": lid}
    except cf.Gone:
        gone.append((lid, ad_id, city))
        cache[str(ad_id)] = {"checked": int(time.time()), "listing": lid, "gone": True}
    except Exception as ex:
        errors += 1
        print("  %s (listing %s): %s -- not counted as gone" % (ad_id, lid, type(ex).__name__))
        if errors >= 10 and alive + len(gone) == 0:
            sys.exit("liveness: 10 transport errors in a row and no answers -- Chợ Tốt is unreachable, stopping without changes")
    time.sleep(0.3)

print("checked %d in %.0fs: alive %d, GONE %d, errors %d" % (len(todo), time.time() - t0, alive, len(gone), errors))
for lid, ad_id, city in gone:
    print("  GONE  listing %s  (%s, ad %s)" % (lid, city, ad_id))

if not DRY:
    # forget cache entries whose listing left the base by any other route
    live_ads = {str(r[0]) for r in rows}
    for k in [k for k in cache if k not in live_ads]:
        del cache[k]
    save_json(CACHE_FILE, cache)

if not gone:
    print("nothing to remove")
    sys.exit(0)
if DRY:
    print("DRY RUN -- %d listing(s) would be removed" % len(gone))
    sys.exit(0)

removed = remove_listings([lid for lid, _, _ in gone], owner="remove_gone_listings")
pd = load_json(POSTED_DATES_FILE, {})
for lid in removed:
    pd.pop(str(lid), None)
save_json(POSTED_DATES_FILE, pd)
print("removed %d listing(s) taken down at the source: %s" % (len(removed), removed))
print("now rebuild (rebuild_final.py -> build_leaflet_data.py -> rebuild_final.py) and run cleanup_telegram_posts.py")
