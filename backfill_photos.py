# -*- coding: utf-8 -*-
"""
Fill in the photos the daily checks left behind.

Measured 3 Sep 2026: the site stores at most 3 photos per listing while Chợ
Tốt carries 6-12 for the same ad -- every batch file ever written took
`images[:3]`. Two costs: a rental page shows a third of the gallery it
could, and 283 listings sit at 0-2 photos, which is below the hub's
--min-photos 3 threshold, so they are never posted at all.

This script fetches the ad's full image list from the same endpoint
check_freshness uses, keeps the first CAP of them, and rewrites the
`details.photos` list of that L(...) row in rebuild_final.py -- under the
write lock, located through ast (never a regex over the whole file), with
the result re-parsed and every touched row's photo list read back before
anything is written.

CAP is 6, not "all": the URLs live in the page's inline JSON, so photos
cost page weight even before a single image is fetched. Measured 3 Sep
2026 on 1 800 listings: going 3 -> 6 adds ~0.7 MB raw across the base
(+418 KB on the largest per-city page), which the URL compaction in
rebuild_final.py/site_data.py roughly cancels out; 8 would be +1.2 MB and
12 well over two, for photos most people never scroll to.

  python backfill_photos.py --dry-run          # report only
  python backfill_photos.py --limit 300        # default: 300 least-recently-tried rows
  python backfill_photos.py --thin-only        # only rows below the hub threshold
  python backfill_photos.py --all

Progress lives in photos_backfill_cache.json (tracked), so runs resume
where the last one stopped and a row is not re-fetched for nothing.
"""
import ast, json, os, re, sys, time

from site_data import load_listings
from listing_lock import listings_write_lock, write_source_atomic, find_blocks, SOURCE
import check_freshness as cf

CAP = 6
CACHE_FILE = "photos_backfill_cache.json"

args = sys.argv[1:]
DRY = "--dry-run" in args
ALL = "--all" in args
THIN_ONLY = "--thin-only" in args
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


def ad_id_of(l):
    m = re.search(r"/(\d{8,9})\.htm", l.get("url", ""))
    return m.group(1) if m else None


def photos_of(l):
    return (l.get("details") or {}).get("photos") or []


def main():
    cache = load_json(CACHE_FILE, {})            # listing id -> last attempt (unix ts)
    rows = []
    for l in load_listings():
        if l.get("source") != "chotot" or not ad_id_of(l):
            continue
        have = len(photos_of(l))
        if have >= CAP:
            continue
        if THIN_ONLY and have >= 3:
            continue
        rows.append((l["id"], ad_id_of(l), have, l["city"]))
    rows.sort(key=lambda r: cache.get(str(r[0]), 0))
    todo = rows if ALL else rows[:LIMIT]
    print("photos: %d Chợ Tốt row(s) below %d photos, fetching %d%s"
          % (len(rows), CAP, len(todo), " (dry run)" if DRY else ""))

    # --- network phase, outside the lock: a 10-minute hold would block the
    # liveness sweep and every daily batch insert.
    found, errors, unchanged = {}, 0, 0
    now = int(time.time())
    t0 = time.time()
    for lid, ad_id, have, city in todo:
        try:
            ad = cf.fetch(int(ad_id))
        except cf.Gone:
            # remove_gone_listings.py owns that decision; here it just means
            # "no photos to add", and the row keeps whatever it has.
            cache[str(lid)] = now
            time.sleep(0.3)
            continue
        except Exception as ex:
            errors += 1
            print("  %s (listing %s): %s" % (ad_id, lid, type(ex).__name__))
            if errors >= 10 and not found:
                sys.exit("photos: 10 errors and nothing fetched -- Chợ Tốt is unreachable, stopping without changes")
            time.sleep(0.3)
            continue
        imgs = [u for u in (ad.get("images") or []) if isinstance(u, str) and u.startswith("http")][:CAP]
        cache[str(lid)] = now
        if len(imgs) > have:
            found[lid] = imgs
        else:
            unchanged += 1
        time.sleep(0.3)

    gained = sum(len(v) for v in found.values()) - sum(h for lid, _, h, _ in todo if lid in found)
    print("fetched %d in %.0fs: %d row(s) get more photos (+%d images), %d already complete, %d error(s)"
          % (len(todo), time.time() - t0, len(found), gained, unchanged, errors))
    for lid, imgs in list(found.items())[:10]:
        had = next(h for i, _, h, _ in todo if i == lid)
        print("  listing %-8s %d -> %d photos" % (lid, had, len(imgs)))
    if len(found) > 10:
        print("  ... and %d more" % (len(found) - 10))

    if DRY:
        print("DRY RUN -- nothing written")
        return
    if not found:
        save_json(CACHE_FILE, cache)
        print("nothing to write")
        return

    # --- write phase, under the lock, offsets computed from the file as it is
    # right now (the sweep or a batch insert may have changed it meanwhile).
    with listings_write_lock("backfill_photos"):
        src = open(SOURCE, encoding="utf-8").read()
        tree = ast.parse(src)
        calls = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and getattr(node.func, "id", None) == "L" \
                    and node.args and isinstance(node.args[0], ast.Constant):
                calls[int(node.args[0].value)] = node
        edits = []          # (start_offset, end_offset, replacement)
        skipped = []
        for lid, imgs in found.items():
            call = calls.get(lid)
            if call is None:
                skipped.append((lid, "row is no longer in the file"))
                continue
            details = next((k.value for k in call.keywords if k.arg == "details"), None)
            new_list = "[" + ", ".join(json.dumps(u, ensure_ascii=False) for u in imgs) + "]"
            if details is None:
                # No details= at all (common among the 0-photo rows): add one,
                # just before the call's closing paren. Keyword order is free.
                at = _off(src, call.end_lineno, call.end_col_offset) - 1
                if src[at] != ")":
                    skipped.append((lid, "could not locate the call's closing paren"))
                    continue
                edits.append((at, at, ',\n  details={"photos": ' + new_list + "}"))
                continue
            if not isinstance(details, ast.Dict):
                skipped.append((lid, "details= is not a literal dict"))
                continue
            photos_val = None
            for k, v in zip(details.keys, details.values):
                if isinstance(k, ast.Constant) and k.value == "photos":
                    photos_val = v
            if photos_val is not None:
                if not isinstance(photos_val, ast.List):
                    skipped.append((lid, "details['photos'] is not a literal list"))
                    continue
                edits.append((_off(src, photos_val.lineno, photos_val.col_offset),
                              _off(src, photos_val.end_lineno, photos_val.end_col_offset), new_list))
            else:
                # insert `"photos": [...], ` right after the opening brace
                at = _off(src, details.lineno, details.col_offset) + 1
                edits.append((at, at, '"photos": ' + new_list + ", "))
        edits.sort(key=lambda e: e[0], reverse=True)
        out = src
        for start, end, text in edits:
            out = out[:start] + text + out[end:]

        # verify before writing: still parses, same number of rows, and every
        # touched row really holds the photo list we meant to put there.
        try:
            new_tree = ast.parse(out)
        except SyntaxError as ex:
            raise SystemExit("rewritten %s does not parse (%s) -- nothing written" % (SOURCE, ex))
        if len(find_blocks(out)) != len(find_blocks(src)):
            raise SystemExit("row count changed during the rewrite -- nothing written")
        check = {}
        for node in ast.walk(new_tree):
            if isinstance(node, ast.Call) and getattr(node.func, "id", None) == "L" \
                    and node.args and isinstance(node.args[0], ast.Constant):
                d = next((k.value for k in node.keywords if k.arg == "details"), None)
                if isinstance(d, ast.Dict):
                    for k, v in zip(d.keys, d.values):
                        if isinstance(k, ast.Constant) and k.value == "photos":
                            try:
                                check[int(node.args[0].value)] = ast.literal_eval(v)
                            except Exception:
                                pass
        bad = [lid for lid, imgs in found.items()
               if lid not in [s[0] for s in skipped] and check.get(lid) != imgs]
        if bad:
            raise SystemExit("photo list did not read back correctly for %s -- nothing written" % bad[:5])
        write_source_atomic(out)

    save_json(CACHE_FILE, cache)
    print("updated %d listing(s) in %s (+%d photos)" % (len(found) - len(skipped), SOURCE, gained))
    for lid, why in skipped:
        print("  skipped %s: %s" % (lid, why))
    print("now rebuild: python rebuild_final.py")


def _off(src, lineno, col):
    """ast gives (line, column); text splicing needs a character offset. Columns
    are UTF-8 byte offsets, so the line is measured the same way."""
    pos = 0
    for _ in range(lineno - 1):
        pos = src.index("\n", pos) + 1
    return pos + len(src[pos:].split("\n")[0].encode("utf-8")[:col].decode("utf-8", "ignore"))


if __name__ == "__main__":
    main()
