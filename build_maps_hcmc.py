# -*- coding: utf-8 -*-
import json
from build_maps2 import build_city_from_elements, load

HCMC_NAMES = ["Phường Tân Mỹ","Phường Tân Hưng","Phường An Khánh","Phường Bình Trưng","Phường Bình Quới"]
HCMC_KEYS = {"Phường Tân Mỹ":"tm","Phường Tân Hưng":"th","Phường An Khánh":"ak","Phường Bình Trưng":"btr","Phường Bình Quới":"bq"}

hcmc_elements = load("hcmc_overpass.json")["elements"]
result = {"ho-chi-minh": build_city_from_elements(hcmc_elements, HCMC_NAMES, HCMC_KEYS)}

existing = load("maps_data.json")
existing.update(result)
with open("maps_data.json", "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=1)

for city, d in result.items():
    print(city, "wards found:", len(d["wards"]), "viewBox:", d["viewBox"])
    for w in d["wards"]:
        print("  ", w["key"], w["name"], "path len:", len(w["d"]))
