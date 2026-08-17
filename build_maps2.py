# -*- coding: utf-8 -*-
import json, math

def load(fname):
    return json.load(open(fname, encoding="utf-8"))

def rdp(points, epsilon):
    if len(points) < 3:
        return points
    def perp_dist(pt, a, b):
        (x, y), (x1, y1), (x2, y2) = pt, a, b
        dx, dy = x2 - x1, y2 - y1
        if dx == 0 and dy == 0:
            return math.hypot(x - x1, y - y1)
        t = ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)
        px, py = x1 + t * dx, y1 + t * dy
        return math.hypot(x - px, y - py)
    dmax, idx = 0.0, 0
    for i in range(1, len(points) - 1):
        d = perp_dist(points[i], points[0], points[-1])
        if d > dmax:
            dmax, idx = d, i
    if dmax > epsilon:
        left = rdp(points[:idx+1], epsilon)
        right = rdp(points[idx:], epsilon)
        return left[:-1] + right
    else:
        return [points[0], points[-1]]

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

def build_city_from_elements(elements, want_names, key_map):
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
    out_wards = []
    for name, w in wards.items():
        paths = []
        for ring in w["rings"]:
            pts = [project(lat, lon) for lat, lon in ring]
            pts = [((x-minx)*SCALE, (y-miny)*SCALE) for x,y in pts]
            simp = rdp(pts, 0.6)
            if len(simp) < 3:
                simp = pts
            d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x,y in simp) + " Z"
            paths.append(d)
        lx, ly = project(*w["label"])
        lx, ly = (lx-minx)*SCALE, (ly-miny)*SCALE
        key = key_map.get(name, name)
        out_wards.append({"key": key, "name": name, "d": " ".join(paths), "lx": round(lx,1), "ly": round(ly,1)})
    vbW, vbH = W*SCALE, H*SCALE
    print(name, "found", len(out_wards), "of", len(want_names), "wanted")
    return {"viewBox": f"0 0 {vbW:.1f} {vbH:.1f}", "wards": out_wards}

VT_NAMES = ["Phường Vũng Tàu","Phường Tam Thắng","Phường Rạch Dừa","Phường Phước Thắng"]
VT_KEYS = {"Phường Vũng Tàu":"vtp","Phường Tam Thắng":"tth","Phường Rạch Dừa":"rd","Phường Phước Thắng":"pth"}

QN_NAMES = ["Phường Quy Nhơn","Phường Quy Nhơn Đông","Phường Quy Nhơn Tây","Phường Quy Nhơn Nam","Phường Quy Nhơn Bắc"]
QN_KEYS = {"Phường Quy Nhơn":"qn","Phường Quy Nhơn Đông":"qnd","Phường Quy Nhơn Tây":"qnt","Phường Quy Nhơn Nam":"qnn","Phường Quy Nhơn Bắc":"qnb"}

HA_NAMES = ["Phường Hội An","Phường Hội An Đông","Phường Hội An Tây"]
HA_KEYS = {"Phường Hội An":"ha","Phường Hội An Đông":"had","Phường Hội An Tây":"hat"}

PT_NAMES = ["Phường Phan Thiết","Phường Bình Thuận","Phường Phú Thủy","Phường Mũi Né","Phường Tiến Thành","Phường Hàm Thắng"]
PT_KEYS = {"Phường Phan Thiết":"pt","Phường Bình Thuận":"bt","Phường Phú Thủy":"put","Phường Mũi Né":"mn","Phường Tiến Thành":"tt","Phường Hàm Thắng":"hth"}

vt_elements = load("vungtau_overpass.json")["elements"]
qn_elements = load("quynhon_overpass.json")["elements"]
pt_elements = load("phanthiet_overpass.json")["elements"]
ha_elements = load("hoian_extra_overpass.json")["elements"] + load("danang_overpass.json")["elements"]

result = {
    "vung-tau": build_city_from_elements(vt_elements, VT_NAMES, VT_KEYS),
    "quy-nhon": build_city_from_elements(qn_elements, QN_NAMES, QN_KEYS),
    "hoi-an": build_city_from_elements(ha_elements, HA_NAMES, HA_KEYS),
    "phan-thiet": build_city_from_elements(pt_elements, PT_NAMES, PT_KEYS),
}

existing = load("maps_data.json")
existing.update(result)
with open("maps_data.json", "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=1)

for city, d in result.items():
    print(city, "wards found:", len(d["wards"]), "viewBox:", d["viewBox"])
    for w in d["wards"]:
        print("  ", w["key"], w["name"], "path len:", len(w["d"]))
