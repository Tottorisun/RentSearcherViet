# -*- coding: utf-8 -*-
# Build real lat/lon data for a genuine Leaflet+OpenStreetMap map: ward boundary rings (raw
# lat/lon, no SVG projection) for the "wards"-type cities, plus final real lat/lon per listing
# (reusing the geocode/ward-centroid resolution already computed in pin_results.json /
# pin_results_nhatrang.json — just skipping the SVG-projection step this time).
import json, re

def load(fname):
    return json.load(open(fname, encoding="utf-8"))

def assemble_rings(ways):
    segs = [list(w) for w in ways if len(w) >= 2]
    rings = []
    used = [False] * len(segs)
    for i in range(len(segs)):
        if used[i]:
            continue
        used[i] = True
        ring = list(segs[i])
        changed = True
        while changed:
            changed = False
            for j in range(len(segs)):
                if used[j]:
                    continue
                s = segs[j]
                if ring[-1] == s[0]:
                    ring.extend(s[1:]); used[j] = True; changed = True
                elif ring[-1] == s[-1]:
                    ring.extend(list(reversed(s))[1:]); used[j] = True; changed = True
                elif ring[0] == s[-1]:
                    ring[0:0] = s[:-1]; used[j] = True; changed = True
                elif ring[0] == s[0]:
                    ring[0:0] = list(reversed(s))[:-1]; used[j] = True; changed = True
        rings.append(ring)
    return rings

def extract_ward(rel):
    outer_ways = []
    for m in rel.get("members", []):
        if m.get("role") == "outer" and m.get("geometry"):
            outer_ways.append([(pt["lat"], pt["lon"]) for pt in m["geometry"]])
    rings = assemble_rings(outer_ways)
    rings = [r for r in rings if len(r) >= 4]
    return rings or None

def simplify(ring, keep_every=3):
    # light thinning for payload size — Leaflet doesn't need the RDP precision the SVG build used
    if len(ring) <= 60:
        return ring
    out = ring[::keep_every]
    if out[-1] != ring[-1]:
        out.append(ring[-1])
    return out

def wards_latlon(elements, want_names, key_map):
    out = {}
    for e in elements:
        name = e.get("tags", {}).get("name")
        if name in want_names:
            rings = extract_ward(e)
            if rings:
                key = key_map.get(name, name)
                out[key] = {"name": name, "rings": [simplify(r) for r in rings]}
    return out

DL_NAMES = ["Phường Xuân Hương - Đà Lạt","Phường Lâm Viên - Đà Lạt","Phường Xuân Trường - Đà Lạt","Phường Cam Ly - Đà Lạt","Phường Lang Biang - Đà Lạt"]
DL_KEYS = {"Phường Xuân Hương - Đà Lạt":"xh","Phường Lâm Viên - Đà Lạt":"lv","Phường Xuân Trường - Đà Lạt":"xt","Phường Cam Ly - Đà Lạt":"cl","Phường Lang Biang - Đà Lạt":"lb"}
DN_NAMES = ["Phường Hải Châu","Phường Hòa Cường","Phường Thanh Khê","Phường An Khê","Phường Cẩm Lệ","Phường Hòa Xuân","Phường Ngũ Hành Sơn","Phường Sơn Trà","Phường An Hải","Phường Liên Chiểu","Phường Hòa Khánh"]
DN_KEYS = {"Phường Hải Châu":"hc","Phường Hòa Cường":"hcg","Phường Thanh Khê":"tk","Phường An Khê":"ak","Phường Cẩm Lệ":"cl2","Phường Hòa Xuân":"hx","Phường Ngũ Hành Sơn":"ns","Phường Sơn Trà":"st","Phường An Hải":"ah","Phường Liên Chiểu":"lc","Phường Hòa Khánh":"hk"}
HA_NAMES = ["Phường Hội An","Phường Hội An Đông","Phường Hội An Tây"]
HA_KEYS = {"Phường Hội An":"ha","Phường Hội An Đông":"had","Phường Hội An Tây":"hat"}
HCMC_NAMES = ["Phường Tân Mỹ","Phường Tân Hưng","Phường An Khánh","Phường Bình Trưng","Phường Bình Quới","Phường Bến Thành","Phường Khánh Hội"]
HCMC_KEYS = {"Phường Tân Mỹ":"tm","Phường Tân Hưng":"th","Phường An Khánh":"ak","Phường Bình Trưng":"btr","Phường Bình Quới":"bq","Phường Bến Thành":"bth","Phường Khánh Hội":"kh"}
VT_NAMES = ["Phường Vũng Tàu","Phường Tam Thắng","Phường Rạch Dừa","Phường Phước Thắng"]
VT_KEYS = {"Phường Vũng Tàu":"vtp","Phường Tam Thắng":"tth","Phường Rạch Dừa":"rd","Phường Phước Thắng":"pth"}
QN_NAMES = ["Phường Quy Nhơn","Phường Quy Nhơn Đông","Phường Quy Nhơn Tây","Phường Quy Nhơn Nam","Phường Quy Nhơn Bắc"]
QN_KEYS = {"Phường Quy Nhơn":"qn","Phường Quy Nhơn Đông":"qnd","Phường Quy Nhơn Tây":"qnt","Phường Quy Nhơn Nam":"qnn","Phường Quy Nhơn Bắc":"qnb"}
PT_NAMES = ["Phường Phan Thiết","Phường Bình Thuận","Phường Phú Thủy","Phường Mũi Né","Phường Tiến Thành","Phường Hàm Thắng"]
PT_KEYS = {"Phường Phan Thiết":"pt","Phường Bình Thuận":"bt","Phường Phú Thủy":"put","Phường Mũi Né":"mn","Phường Tiến Thành":"tt","Phường Hàm Thắng":"hth"}

dl = load("dalat_overpass.json")["elements"]
dn = load("danang_overpass.json")["elements"]
ha = load("hoian_extra_overpass.json")["elements"] + dn
hcmc = load("hcmc_overpass.json")["elements"] + load("hcmc_extra_overpass.json")["elements"]
vt = load("vungtau_overpass.json")["elements"]
qn = load("quynhon_overpass.json")["elements"]
pt = load("phanthiet_overpass.json")["elements"]

ward_boundaries = {
    "da-lat": wards_latlon(dl, DL_NAMES, DL_KEYS),
    "da-nang": wards_latlon(dn, DN_NAMES, DN_KEYS),
    "hoi-an": wards_latlon(ha, HA_NAMES, HA_KEYS),
    "ho-chi-minh": wards_latlon(hcmc, HCMC_NAMES, HCMC_KEYS),
    "vung-tau": wards_latlon(vt, VT_NAMES, VT_KEYS),
    "quy-nhon": wards_latlon(qn, QN_NAMES, QN_KEYS),
    "phan-thiet": wards_latlon(pt, PT_NAMES, PT_KEYS),
}
json.dump(ward_boundaries, open("leaflet_ward_boundaries.json","w",encoding="utf-8"), ensure_ascii=False)
for c,w in ward_boundaries.items():
    print(c, "wards:", len(w))

# --- listing real lat/lon (reuse already-resolved geocode/centroid results) ---
pin_results = load("pin_results.json")           # da-lat, da-nang, hoi-an, ho-chi-minh
projections = load("pin_projections.json")        # ward_centroids per city (already lat/lon)

html = open("vietnam-rent-finder.html", encoding="utf-8").read()
m = re.search(r'var DATA = (\{.*?\});\s*\n', html, re.S)
data = json.loads(m.group(1))
listings = data["LISTINGS"]

# Nha Trang: no real geography — use each district's centroid computed from the *_overpass source
# it never had real modern ward polygons for (see project memory), so fall back to a fixed
# approximate lat/lon per old-style district, hand-mapped to the familiar realtor names.
NT_APPROX = {
    "vh":(12.2775,109.1968),"vp":(12.2721,109.1889),"vt2":(12.2560,109.1975),"ps":(12.2497,109.1898),
    "nh":(12.2469,109.1793),"ph":(12.2438,109.1965),"lt":(12.2408,109.1968),"ph2":(12.2381,109.1902),
    "tl":(12.2367,109.1943),"pl":(12.2280,109.1820),"vt":(12.2223,109.1975),"vn":(12.2140,109.2050),
}

lat_lon = {}
missing = 0
for l in listings:
    city = l["city"]; lid = str(l["id"])
    if city == "nha-trang":
        c = NT_APPROX.get(l["district"])
        if c: lat_lon[lid] = {"lat": c[0], "lon": c[1], "geocoded": False}
        else: missing += 1
        continue
    r = pin_results.get(lid)
    if r:
        lat_lon[lid] = {"lat": r["lat"], "lon": r["lon"], "geocoded": r["source"]=="geocode"}
    else:
        missing += 1

json.dump(lat_lon, open("leaflet_listing_latlon.json","w",encoding="utf-8"), ensure_ascii=False)
print("listings with lat/lon:", len(lat_lon), "missing:", missing)
