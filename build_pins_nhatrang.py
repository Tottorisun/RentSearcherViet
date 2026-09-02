# -*- coding: utf-8 -*-
# Nha Trang has no real ward-level geographic boundaries post-2025 (see project footer note) — its
# map is a synthetic "mosaic" grid of realtor-familiar district names laid over the city's real outline,
# not a real projection. Real street-level geocoding can't be meaningfully placed on it. Instead, place
# each listing's pin at a deterministic (stable per listing id, not random-per-render) position inside
# one of its own district's mosaic cells, so pins land in the correct neighborhood shape and don't all
# stack on one point, without pretending to street-level accuracy.
import json, hashlib

nt = json.load(open("nt_realtor_map.json", encoding="utf-8"))
cellW, cellH = nt["cellW"], nt["cellH"]
cells_by_key = {}
for c in nt["cells"]:
    cells_by_key.setdefault(c["key"], []).append(c)

from site_data import load_listings
listings = [l for l in load_listings() if l["city"] == "nha-trang"]

def stable_unit(seed_str):
    h = hashlib.md5(seed_str.encode("utf-8")).hexdigest()
    a = int(h[:8], 16) / 0xFFFFFFFF
    b = int(h[8:16], 16) / 0xFFFFFFFF
    return a, b

pins = {}
missing_keys = set()
for l in listings:
    cells = cells_by_key.get(l["district"])
    if not cells:
        missing_keys.add(l["district"])
        continue
    a, b = stable_unit(str(l["id"]))
    cell = cells[int(a * len(cells)) % len(cells)]
    x = cell["x"] + b * cellW
    y = cell["y"] + ((int(a*997) % 1000)/1000.0) * cellH
    pins[l["id"]] = {"x": round(x, 1), "y": round(y, 1)}

json.dump(pins, open("pin_results_nhatrang.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"placed {len(pins)} Nha Trang pins, missing district keys: {missing_keys}")
