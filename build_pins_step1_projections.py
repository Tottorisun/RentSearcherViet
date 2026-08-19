# -*- coding: utf-8 -*-
# Recompute per-city projection params (lat0,lon0,coslat,minx,miny,SCALE) + raw ward centroids,
# identical algorithm/inputs to build_maps.py / build_maps2.py, so listing pins land exactly
# where the already-built ward polygons expect them.
import json, math

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
    label = None
    for m in rel.get("members", []):
        if m.get("role") == "outer" and m.get("geometry"):
            outer_ways.append([(pt["lat"], pt["lon"]) for pt in m["geometry"]])
        if m.get("role") == "label":
            label = (m.get("lat"), m.get("lon"))
    rings = assemble_rings(outer_ways)
    rings = [r for r in rings if len(r) >= 4]
    if not rings:
        return None
    if label is None:
        big = max(rings, key=len)
        label = (sum(p[0] for p in big)/len(big), sum(p[1] for p in big)/len(big))
    return {"rings": rings, "label": label}

def build_projection(elements, want_names, key_map):
    wards = {}
    for e in elements:
        name = e.get("tags", {}).get("name")
        if name in want_names:
            w = extract_ward(e)
            if w:
                wards[name] = w
    all_pts = [pt for w in wards.values() for ring in w["rings"] for pt in ring]
    lats = [p[0] for p in all_pts]; lons = [p[1] for p in all_pts]
    lat0 = (min(lats)+max(lats))/2
    lon0 = (min(lons)+max(lons))/2
    coslat = math.cos(math.radians(lat0))
    def project(lat, lon):
        x = (lon - lon0) * coslat
        y = -(lat - lat0)
        return x, y
    proj_pts = [project(*p) for p in all_pts]
    xs = [p[0] for p in proj_pts]; ys = [p[1] for p in proj_pts]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    W = maxx - minx; H = maxy - miny
    margin = max(W, H) * 0.04
    minx -= margin; miny -= margin; W += 2*margin; H += 2*margin
    SCALE = 1000.0 / max(W, H)
    centroids = {}
    for name, w in wards.items():
        key = key_map.get(name, name)
        centroids[key] = {"lat": w["label"][0], "lon": w["label"][1]}
    # geographic bbox in raw lat/lon, for later sanity-checking geocoder results
    bbox = {"minlat": min(lats), "maxlat": max(lats), "minlon": min(lons), "maxlon": max(lons)}
    return {
        "lat0": lat0, "lon0": lon0, "coslat": coslat,
        "minx": minx, "miny": miny, "scale": SCALE,
        "ward_centroids": centroids, "bbox": bbox
    }

DL_NAMES = ["Phường Xuân Hương - Đà Lạt","Phường Lâm Viên - Đà Lạt","Phường Xuân Trường - Đà Lạt","Phường Cam Ly - Đà Lạt","Phường Lang Biang - Đà Lạt"]
DL_KEYS = {"Phường Xuân Hương - Đà Lạt":"xh","Phường Lâm Viên - Đà Lạt":"lv","Phường Xuân Trường - Đà Lạt":"xt","Phường Cam Ly - Đà Lạt":"cl","Phường Lang Biang - Đà Lạt":"lb"}

DN_NAMES = ["Phường Hải Châu","Phường Hòa Cường","Phường Thanh Khê","Phường An Khê","Phường Cẩm Lệ","Phường Hòa Xuân","Phường Ngũ Hành Sơn","Phường Sơn Trà","Phường An Hải","Phường Liên Chiểu","Phường Hòa Khánh"]
DN_KEYS = {"Phường Hải Châu":"hc","Phường Hòa Cường":"hcg","Phường Thanh Khê":"tk","Phường An Khê":"ak","Phường Cẩm Lệ":"cl2","Phường Hòa Xuân":"hx","Phường Ngũ Hành Sơn":"ns","Phường Sơn Trà":"st","Phường An Hải":"ah","Phường Liên Chiểu":"lc","Phường Hòa Khánh":"hk"}

HA_NAMES = ["Phường Hội An","Phường Hội An Đông","Phường Hội An Tây"]
HA_KEYS = {"Phường Hội An":"ha","Phường Hội An Đông":"had","Phường Hội An Tây":"hat"}

HCMC_NAMES = ["Phường Tân Mỹ","Phường Tân Hưng","Phường An Khánh","Phường Bình Trưng","Phường Bình Quới","Phường Bến Thành","Phường Khánh Hội"]
HCMC_KEYS = {"Phường Tân Mỹ":"tm","Phường Tân Hưng":"th","Phường An Khánh":"ak","Phường Bình Trưng":"btr","Phường Bình Quới":"bq","Phường Bến Thành":"bth","Phường Khánh Hội":"kh"}

# Added so vung-tau / quy-nhon / phan-thiet listings get real geocode/ward-centroid resolution too
# (previously missing here — those 3 cities' first-ever listings landed with lat/lon=null because
# this projections file only covered da-lat/da-nang/hoi-an/ho-chi-minh; nha-trang is handled by a
# separate mosaic-jitter script). Names/keys match build_leaflet_data.py's VT_NAMES/QN_NAMES/PT_NAMES
# exactly so ward centroids line up with the already-built ward polygons.
VT_NAMES = ["Phường Vũng Tàu","Phường Tam Thắng","Phường Rạch Dừa","Phường Phước Thắng"]
VT_KEYS = {"Phường Vũng Tàu":"vtp","Phường Tam Thắng":"tth","Phường Rạch Dừa":"rd","Phường Phước Thắng":"pth"}
QN_NAMES = ["Phường Quy Nhơn","Phường Quy Nhơn Đông","Phường Quy Nhơn Tây","Phường Quy Nhơn Nam","Phường Quy Nhơn Bắc"]
QN_KEYS = {"Phường Quy Nhơn":"qn","Phường Quy Nhơn Đông":"qnd","Phường Quy Nhơn Tây":"qnt","Phường Quy Nhơn Nam":"qnn","Phường Quy Nhơn Bắc":"qnb"}
PT_NAMES = ["Phường Phan Thiết","Phường Bình Thuận","Phường Phú Thủy","Phường Mũi Né","Phường Tiến Thành","Phường Hàm Thắng"]
PT_KEYS = {"Phường Phan Thiết":"pt","Phường Bình Thuận":"bt","Phường Phú Thủy":"put","Phường Mũi Né":"mn","Phường Tiến Thành":"tt","Phường Hàm Thắng":"hth"}

dl_elements = load("dalat_overpass.json")["elements"]
dn_elements = load("danang_overpass.json")["elements"]
ha_elements = load("hoian_extra_overpass.json")["elements"] + load("danang_overpass.json")["elements"]
hcmc_elements = load("hcmc_overpass.json")["elements"] + load("hcmc_extra_overpass.json")["elements"]
vt_elements = load("vungtau_overpass.json")["elements"]
qn_elements = load("quynhon_overpass.json")["elements"]
pt_elements = load("phanthiet_overpass.json")["elements"]

result = {
    "da-lat": build_projection(dl_elements, DL_NAMES, DL_KEYS),
    "da-nang": build_projection(dn_elements, DN_NAMES, DN_KEYS),
    "hoi-an": build_projection(ha_elements, HA_NAMES, HA_KEYS),
    "ho-chi-minh": build_projection(hcmc_elements, HCMC_NAMES, HCMC_KEYS),
    "vung-tau": build_projection(vt_elements, VT_NAMES, VT_KEYS),
    "quy-nhon": build_projection(qn_elements, QN_NAMES, QN_KEYS),
    "phan-thiet": build_projection(pt_elements, PT_NAMES, PT_KEYS),
}

with open("pin_projections.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=1)

for city, d in result.items():
    print(city, "wards with centroids:", len(d["ward_centroids"]), "bbox:", d["bbox"])
