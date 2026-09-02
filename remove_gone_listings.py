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
posted_dates anchors. The same answer carries the ad's own timestamps, so
it also (a) removes rows Chợ Tốt itself proves are older than 14 whole
days (STALE -- a session once dated five listings "today" that were 2-12
days old) and (b) corrects the posted_dates anchor of every FRESH row
whose recorded date differs from orig_list_time, so the age purge and the
"N дней назад" label rest on the source's date, not on an estimate. Run
it BEFORE purge_old_listings.py in the daily pipeline;
cleanup_telegram_posts.py later deletes the removed rows' hub posts.

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

MAX_DAYS = 14.0
pd = load_json(POSTED_DATES_FILE, {})
now = time.time()
gone, stale, redated, errors, alive = [], [], [], 0, 0
t0 = time.time()
for ad_id, lid, city in todo:
    try:
        ad = cf.fetch(ad_id)
    except cf.Gone:
        gone.append((lid, ad_id, city))
        cache[str(ad_id)] = {"checked": int(now), "listing": lid, "gone": True}
        time.sleep(0.3)
        continue
    except Exception as ex:
        errors += 1
        print("  %s (listing %s): %s -- not counted as gone" % (ad_id, lid, type(ex).__name__))
        if errors >= 10 and alive + len(gone) == 0:
            sys.exit("liveness: 10 transport errors in a row and no answers -- Chợ Tốt is unreachable, stopping without changes")
        time.sleep(0.3)
        continue
    alive += 1
    cache[str(ad_id)] = {"checked": int(now), "listing": lid}
    # The same answer carries the ad's own timestamps -- use them. Chợ Tốt's
    # verdict (check_freshness.verdict) is the source of truth the site's
    # anchor date was only ever an estimate of: a session once dated five
    # listings "today" that were 2-12 days old.
    v, age, via = cf.verdict(ad, now, MAX_DAYS)
    # Same rule as purge_old_listings.py: gone when OLDER THAN 14 whole days,
    # so a 14.3-day-old ad is not removed half a day before the age purge
    # would have removed it anyway. (cf.verdict says STALE from 14.0.)
    if v == "STALE" and age is not None and int(age) > MAX_DAYS:
        stale.append((lid, ad_id, city, age, via))
    elif v == "FRESH" and ad.get("orig_list_time"):
        true_anchor = time.strftime("%Y-%m-%d", time.localtime(ad["orig_list_time"] / 1000))
        if pd.get(str(lid)) != true_anchor:
            redated.append((lid, pd.get(str(lid)), true_anchor))
            pd[str(lid)] = true_anchor
    time.sleep(0.3)

print("checked %d in %.0fs: alive %d, GONE %d, STALE %d, re-dated %d, errors %d"
      % (len(todo), time.time() - t0, alive, len(gone), len(stale), len(redated), errors))
for lid, ad_id, city in gone:
    print("  GONE   listing %s  (%s, ad %s)" % (lid, city, ad_id))
for lid, ad_id, city, age, via in stale:
    print("  STALE  listing %s  (%s, ad %s): %.1f days old via %s" % (lid, city, ad_id, age, via))
for lid, old, new in redated:
    print("  DATE   listing %s: anchor %s -> %s (Chợ Tốt orig_list_time)" % (lid, old, new))

if not DRY:
    # forget cache entries whose listing left the base by any other route
    live_ads = {str(r[0]) for r in rows}
    for k in [k for k in cache if k not in live_ads]:
        del cache[k]
    save_json(CACHE_FILE, cache)

to_remove = [lid for lid, _, _ in gone] + [lid for lid, _, _, _, _ in stale]
if not to_remove and not redated:
    print("nothing to change")
    sys.exit(0)
if DRY:
    print("DRY RUN -- %d listing(s) would be removed (%d gone, %d stale), %d anchor date(s) corrected"
          % (len(to_remove), len(gone), len(stale), len(redated)))
    sys.exit(0)

removed = remove_listings(to_remove, owner="remove_gone_listings") if to_remove else []
for lid in removed:
    pd.pop(str(lid), None)
save_json(POSTED_DATES_FILE, pd)
print("removed %d listing(s) (%d taken down, %d provably older than %d days): %s"
      % (len(removed), len(gone), len(stale), int(MAX_DAYS), removed))
if redated:
    print("corrected %d anchor date(s) in %s; purge_old_listings.py will relabel them" % (len(redated), POSTED_DATES_FILE))
print("now run purge_old_listings.py, rebuild (rebuild_final.py -> build_leaflet_data.py -> rebuild_final.py) and cleanup_telegram_posts.py")
