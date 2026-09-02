# -*- coding: utf-8 -*-
# Combine geocoded/ward-centroid lat-lon results with each city's stored projection params to get
# final SVG (x,y) per listing, in the exact same coordinate space as the already-built ward polygons.
# Ward-centroid fallback pins get a deterministic jitter (scattered around the centroid) so dozens of
# listings sharing one district don't all stack on a single point; precisely-geocoded pins get a much
# smaller jitter only to separate exact duplicates (same building, several listings).
import json, math, hashlib

projections = json.load(open("pin_projections.json", encoding="utf-8"))
pin_results = json.load(open("pin_results.json", encoding="utf-8"))
nt_pins = json.load(open("pin_results_nhatrang.json", encoding="utf-8"))

from site_data import load_listings
listings = load_listings()

def stable_unit(seed_str):
    h = hashlib.md5(seed_str.encode("utf-8")).hexdigest()
    a = int(h[:8], 16) / 0xFFFFFFFF
    b = int(h[8:16], 16) / 0xFFFFFFFF
    return a, b

final_pins = {}
skipped = 0

for l in listings:
    city = l["city"]
    lid = l["id"]
    if city == "nha-trang":
        p = nt_pins.get(str(lid))
        if p:
            final_pins[lid] = {"x": p["x"], "y": p["y"], "geocoded": False}
        else:
            skipped += 1
        continue
    if city not in projections:
        skipped += 1
        continue
    proj = projections[city]
    if "lon0" not in proj:
        # binh-duong/phu-quoc etc: manually authored bbox+ward_centroids only, no real OSM
        # ward polygons to project onto (see pin_projections.json comments in the pipeline
        # scripts) -- these cities render on the Leaflet map only, not the SVG mosaic map.
        skipped += 1
        continue
    r = pin_results.get(str(lid))
    if not r:
        skipped += 1
        continue
    lat, lon, source = r["lat"], r["lon"], r["source"]
    x = (lon - proj["lon0"]) * proj["coslat"]
    y = -(lat - proj["lat0"])
    x = (x - proj["minx"]) * proj["scale"]
    y = (y - proj["miny"]) * proj["scale"]
    a, b = stable_unit(str(lid))
    angle = a * 2 * math.pi
    if source == "geocode":
        radius = 3 + b * 5  # tight jitter, just to separate exact duplicates
    else:
        radius = 18 + b * 22  # wider scatter around the ward centroid
    x += math.cos(angle) * radius
    y += math.sin(angle) * radius
    final_pins[lid] = {"x": round(x, 1), "y": round(y, 1), "geocoded": source == "geocode"}

json.dump(final_pins, open("final_pins.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"final pins: {len(final_pins)}, skipped: {skipped}")
geocoded_count = sum(1 for v in final_pins.values() if v.get("geocoded"))
print(f"precisely geocoded: {geocoded_count} / {len(final_pins)}")
