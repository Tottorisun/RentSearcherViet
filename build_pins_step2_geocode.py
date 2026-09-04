# -*- coding: utf-8 -*-
# Extract candidate addresses per listing from Russian-language descriptions (embedded Latin-script
# Vietnamese proper nouns are the only Latin capitalized runs in the text, so a simple regex is a
# reliable extractor here), geocode unique candidates via Nominatim (rate-limited, cached, validated
# against each city's real bounding box), fall back to ward centroid when nothing validates.
import json, re, os, time, urllib.request, urllib.parse, urllib.error

from site_data import load_data
data = load_data()
listings = data["LISTINGS"]

# Source-provided coordinates (Chợ Tốt ships lat/lon with every ad). Kept in
# a tracked file the daily checks append to; ids present here are recorded
# as precise and never sent to Nominatim. Before 2 Sep 2026 the prompt told
# sessions to write these into leaflet_listing_latlon.json, which this
# pipeline regenerates from scratch -- so every such coordinate was lost.
CHOTOT_COORDS_FILE = "chotot_coords.json"
try:
    CHOTOT_COORDS = json.load(open(CHOTOT_COORDS_FILE, encoding="utf-8"))
except FileNotFoundError:
    CHOTOT_COORDS = {}

CITY_VN = {"nha-trang":"Nha Trang","da-lat":"Da Lat","da-nang":"Da Nang","hoi-an":"Hoi An","ho-chi-minh":"Ho Chi Minh City",
           "vung-tau":"Vung Tau","quy-nhon":"Quy Nhon","phan-thiet":"Phan Thiet",
           "ha-noi":"Hanoi","binh-duong":"Binh Duong","phu-quoc":"Phu Quoc","dumaguete":"Dumaguete","cebu":"Cebu","manila":"Manila"}
DIST_NAME = {}
for ckey, cval in data["CITIES"].items():
    for d in cval["districts"]:
        DIST_NAME[(ckey, d["key"])] = d["name"]

projections = json.load(open("pin_projections.json", encoding="utf-8"))
GEO_CITIES = set(projections.keys())

# Cities intentionally not geocoded here. Nha Trang gets its pin positions from
# a separate mosaic-jitter script, so its absence from pin_projections.json is
# expected, not a mistake.
GEO_EXEMPT = {"nha-trang"}

# Fail loudly on a city that is neither projected nor deliberately exempt.
# Previously an unknown city was silently `continue`d in the loop below, so a
# newly added city got zero coordinates and zero map pins while this script
# still reported success -- the worst kind of failure, because nothing in the
# logs says anything is wrong and it only surfaces when someone opens the map.
_unprojected = sorted(set(data["CITIES"]) - GEO_CITIES - GEO_EXEMPT)
if _unprojected:
    raise SystemExit(
        "pin_projections.json has no entry for: " + ", ".join(_unprojected) + "\n"
        "Those cities' listings would be silently skipped and would never get\n"
        "coordinates or map pins. Add a projection (bbox + district centroids;\n"
        "the centroids can be geocoded from Nominatim) before running this, or\n"
        "add the city to GEO_EXEMPT if another script handles its pins."
    )

# Same guard, second list. CITY_VN is a second, independent place a new city
# has to be registered, and its own KeyError doesn't fire at startup -- only
# once a listing from that city is actually processed (which is exactly why
# Phú Quốc slipped through this morning: the city existed but was still empty,
# so no listing ever hit this dict until real data landed on 1 Sep 2026).
_no_city_vn = sorted((set(data["CITIES"]) - GEO_EXEMPT) - set(CITY_VN))
if _no_city_vn:
    raise SystemExit(
        "CITY_VN has no entry for: " + ", ".join(_no_city_vn) + "\n"
        "Geocoding a listing from one of these cities would crash with a bare\n"
        "KeyError the first time it actually had a listing to process, not now\n"
        "while the city is still empty. Add its plain English/Vietnamese name\n"
        "(used only to build a Nominatim search query) to CITY_VN above."
    )

CANDIDATE_RE = re.compile(r'\b(?:[A-ZĐ][a-zà-ỹ]*(?:\s+[A-ZĐ0-9][a-zà-ỹ0-9]*){1,4})')

def candidates_for(desc, district_name):
    found = CANDIDATE_RE.findall(desc)
    out = []
    seen = set()
    for c in found:
        c = c.strip()
        if not c or c in seen:
            continue
        seen.add(c)
        if c in district_name or district_name.startswith(c):
            continue  # no more precise than the ward fallback we already have
        out.append(c)
    out.sort(key=len, reverse=True)
    return out[:2]

try:
    cache = json.load(open("geocode_cache.json", encoding="utf-8"))
except FileNotFoundError:
    cache = {}

_net_failures = []      # consecutive network failures; reset on any success

def geocode(query):
    if query in cache:
        return cache[query]
    params = urllib.parse.urlencode({"q": query, "format": "json", "limit": 1, "countrycodes": "vn"})
    url = "https://nominatim.openstreetmap.org/search?" + params
    req = urllib.request.Request(url, headers={"User-Agent": "rent-searcher-personal-project/1.0 (non-commercial, single-user rental aggregator)"})
    # Only a real answer is cached. A timeout, a 429 or a 5xx used to be
    # stored as `null` -- i.e. "this address does not exist" -- for ever, so
    # one bad Nominatim minute permanently parked every listing it touched on
    # a ward centroid (646 of 1 540 cache entries were null on 2 Sep 2026,
    # and nobody can tell which were genuine). Now: retry with backoff, and
    # if the network keeps failing, stop the run instead of quietly degrading.
    results = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                results = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as ex:
            if ex.code == 429 or ex.code >= 500:
                time.sleep(5 * (attempt + 1))
                continue
            print(f"  geocode: HTTP {ex.code} for {query!r} -- not cached")
            return None
        except Exception as ex:
            time.sleep(5 * (attempt + 1))
            continue
    if results is None:
        _net_failures.append(query)
        print(f"  geocode: network failure for {query!r} after 3 attempts -- NOT cached, retried next run")
        if len(_net_failures) >= 10:
            json.dump(cache, open("geocode_cache.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            raise SystemExit("geocode: 10 consecutive network failures -- Nominatim is down or rate-limiting us. "
                             "Stopping rather than parking every remaining listing on a ward centroid; rerun later.")
        return None
    _net_failures.clear()
    time.sleep(1.1)
    if not results:
        cache[query] = None       # a genuine "nothing found" -- this one IS worth remembering
        return None
    r = results[0]
    result = {"lat": float(r["lat"]), "lon": float(r["lon"]), "display_name": r.get("display_name","")}
    cache[query] = result
    return result

def in_bbox(lat, lon, bbox, margin=0.05):
    return (bbox["minlat"]-margin <= lat <= bbox["maxlat"]+margin) and (bbox["minlon"]-margin <= lon <= bbox["maxlon"]+margin)

pin_results = {}
processed = 0
geocoded_hits = 0

for l in listings:
    city = l["city"]
    if city not in GEO_CITIES:
        continue  # nha-trang handled by a separate mosaic-jitter script
    # Accept either key: the site listing id, or the Chợ Tốt ad id that sits in
    # the listing's URL (/<ad id>.htm) -- the first session to use the file
    # keyed it by ad id, which is the number it actually had in hand.
    ad_id = re.search(r"/(\d{8,9})\.htm", l.get("url", ""))
    src_coords = CHOTOT_COORDS.get(str(l["id"])) or (ad_id and CHOTOT_COORDS.get(ad_id.group(1)))
    if src_coords:
        # The ad itself told us where it is -- no Nominatim guesswork.
        pin_results[l["id"]] = {"lat": float(src_coords["lat"]), "lon": float(src_coords["lon"]),
                                "source": "chotot", "matched": None}
        processed += 1
        continue
    proj = projections[city]
    district_name = DIST_NAME.get((city, l["district"]), "")
    cands = candidates_for(l["desc"], district_name)
    resolved = None
    for cand in cands:
        # Try the candidate with just the city first (Nominatim's free-text parser handles a
        # named POI + city far better than POI + district + city — a district name mixed in
        # broke otherwise-correct lookups like "The Ascentia" during testing). Fall back to
        # appending the district only if the city-scoped query comes up empty.
        for query in (f"{cand}, {CITY_VN[city]}, Vietnam", f"{cand}, {district_name.split(' - ')[0]}, {CITY_VN[city]}, Vietnam"):
            g = geocode(query)
            if g and in_bbox(g["lat"], g["lon"], proj["bbox"]):
                resolved = {"lat": g["lat"], "lon": g["lon"], "source": "geocode", "matched": cand}
                geocoded_hits += 1
                break
        if resolved:
            break
    if resolved is None:
        c = proj["ward_centroids"].get(l["district"])
        if c:
            resolved = {"lat": c["lat"], "lon": c["lon"], "source": "ward-centroid", "matched": None}
    pin_results[l["id"]] = resolved
    processed += 1
    if processed % 25 == 0:
        json.dump(cache, open("geocode_cache.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        json.dump(pin_results, open("pin_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"...{processed} processed, {geocoded_hits} geocoded so far")

json.dump(cache, open("geocode_cache.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(pin_results, open("pin_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"DONE: {processed} listings processed, {geocoded_hits} precisely geocoded, {processed-geocoded_hits} on ward centroid")
