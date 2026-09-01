# -*- coding: utf-8 -*-
# Extract candidate addresses per listing from Russian-language descriptions (embedded Latin-script
# Vietnamese proper nouns are the only Latin capitalized runs in the text, so a simple regex is a
# reliable extractor here), geocode unique candidates via Nominatim (rate-limited, cached, validated
# against each city's real bounding box), fall back to ward centroid when nothing validates.
import json, re, time, urllib.request, urllib.parse

html = open("vietnam-rent-finder.html", encoding="utf-8").read()
m = re.search(r'var DATA = (\{.*?\});\s*\n', html, re.S)
data = json.loads(m.group(1))
listings = data["LISTINGS"]

CITY_VN = {"nha-trang":"Nha Trang","da-lat":"Da Lat","da-nang":"Da Nang","hoi-an":"Hoi An","ho-chi-minh":"Ho Chi Minh City",
           "vung-tau":"Vung Tau","quy-nhon":"Quy Nhon","phan-thiet":"Phan Thiet",
           "ha-noi":"Hanoi","binh-duong":"Binh Duong"}
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

def geocode(query):
    if query in cache:
        return cache[query]
    params = urllib.parse.urlencode({"q": query, "format": "json", "limit": 1, "countrycodes": "vn"})
    url = "https://nominatim.openstreetmap.org/search?" + params
    req = urllib.request.Request(url, headers={"User-Agent": "rent-searcher-personal-project/1.0 (non-commercial, single-user rental aggregator)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            results = json.loads(resp.read().decode("utf-8"))
    except Exception as ex:
        cache[query] = None
        return None
    time.sleep(1.1)
    if not results:
        cache[query] = None
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
