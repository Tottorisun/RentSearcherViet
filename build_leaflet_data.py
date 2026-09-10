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
# Hanoi: the site groups listings by the 12 pre-2025 urban districts (quận) --
# that is how every landlord, agent and expat still names the area. OSM keeps
# those as boundary=historic (end_date 2025-06-30), which is exactly the
# polygon set we want; the post-reform wards that reuse the same names
# ("Phường Tây Hồ") cover only a fraction of the old district and would put
# listings outside their own outline.
HN_NAMES = ["Quận Tây Hồ","Quận Ba Đình","Quận Hoàn Kiếm","Quận Cầu Giấy","Quận Nam Từ Liêm","Quận Đống Đa","Quận Hai Bà Trưng","Quận Long Biên","Quận Thanh Xuân","Quận Hoàng Mai","Quận Bắc Từ Liêm","Quận Hà Đông"]
HN_KEYS = {"Quận Tây Hồ":"tyh","Quận Ba Đình":"bd","Quận Hoàn Kiếm":"hkm","Quận Cầu Giấy":"cg","Quận Nam Từ Liêm":"ntl","Quận Đống Đa":"dd","Quận Hai Bà Trưng":"hbt","Quận Long Biên":"lbn","Quận Thanh Xuân":"tx","Quận Hoàng Mai":"hm","Quận Bắc Từ Liêm":"btl","Quận Hà Đông":"hd"}
# Former Bình Dương (merged into HCMC in 2025): the five post-reform wards map 1:1 onto the site's keys.
BD_NAMES = ["Phường Thuận An","Phường Dĩ An","Phường Thủ Dầu Một","Phường Bến Cát","Phường Tân Uyên"]
BD_KEYS = {"Phường Thuận An":"ta","Phường Dĩ An":"da","Phường Thủ Dầu Một":"tdm","Phường Bến Cát":"bc","Phường Tân Uyên":"tu"}

dl = load("dalat_overpass.json")["elements"]
dn = load("danang_overpass.json")["elements"]
ha = load("hoian_extra_overpass.json")["elements"] + dn
hcmc = load("hcmc_overpass.json")["elements"] + load("hcmc_extra_overpass.json")["elements"]
vt = load("vungtau_overpass.json")["elements"]
qn = load("quynhon_overpass.json")["elements"]
pt = load("phanthiet_overpass.json")["elements"]
hn = load("hanoi_overpass.json")["elements"]        # 12 boundary=historic quận, fetched 2 Sep 2026
bd = load("binhduong_overpass.json")["elements"]    # 5 post-reform phường, fetched 2 Sep 2026
# Nha Trang: the four enlarged post-2025 wards DO have real OSM polygons, and
# they were sitting unused in nt_overpass.json all along. The city's twelve
# familiar old wards have none -- OSM keeps only the historic city outline, not
# the pre-reform wards -- so this covers 4 of the site's 16 Nha Trang keys and
# the rest keep the pin-only view. Which is still four more than before.
nt = load("nt_overpass.json")["elements"]
NT_NAMES = ["Phường Nha Trang","Phường Bắc Nha Trang","Phường Tây Nha Trang","Phường Nam Nha Trang"]
NT_KEYS = {"Phường Nha Trang":"nt","Phường Bắc Nha Trang":"btr","Phường Tây Nha Trang":"ttr","Phường Nam Nha Trang":"ntr"}

ward_boundaries = {
    "da-lat": wards_latlon(dl, DL_NAMES, DL_KEYS),
    "da-nang": wards_latlon(dn, DN_NAMES, DN_KEYS),
    "hoi-an": wards_latlon(ha, HA_NAMES, HA_KEYS),
    "ho-chi-minh": wards_latlon(hcmc, HCMC_NAMES, HCMC_KEYS),
    "vung-tau": wards_latlon(vt, VT_NAMES, VT_KEYS),
    "quy-nhon": wards_latlon(qn, QN_NAMES, QN_KEYS),
    "phan-thiet": wards_latlon(pt, PT_NAMES, PT_KEYS),
    "ha-noi": wards_latlon(hn, HN_NAMES, HN_KEYS),
    "binh-duong": wards_latlon(bd, BD_NAMES, BD_KEYS),
    "nha-trang": wards_latlon(nt, NT_NAMES, NT_KEYS),
}
# Every key the site knows for these two cities must have come back with a
# polygon -- a silent miss here shows up only as a district with no outline.
for _city, _keys in (("ha-noi", HN_KEYS), ("binh-duong", BD_KEYS)):
    _missing = sorted(set(_keys.values()) - set(ward_boundaries[_city]))
    if _missing:
        raise SystemExit("%s: no boundary polygon extracted for district key(s) %s -- check the overpass dump" % (_city, _missing))
json.dump(ward_boundaries, open("leaflet_ward_boundaries.json","w",encoding="utf-8"), ensure_ascii=False)
for c,w in ward_boundaries.items():
    print(c, "wards:", len(w))

# --- listing real lat/lon (reuse already-resolved geocode/centroid results) ---
pin_results = load("pin_results.json")           # da-lat, da-nang, hoi-an, ho-chi-minh
projections = load("pin_projections.json")        # ward_centroids per city (already lat/lon)

from site_data import load_listings
listings = load_listings()

# Nha Trang: no real geography — use each district's centroid computed from the *_overpass source
# it never had real modern ward polygons for (see project memory), so fall back to a fixed
# approximate lat/lon per old-style district, hand-mapped to the familiar realtor names.
NT_APPROX = {
    "vh":(12.2775,109.1968),"vp":(12.2721,109.1889),"vt2":(12.2560,109.1975),"ps":(12.2497,109.1898),
    "nh":(12.2469,109.1793),"ph":(12.2438,109.1965),"lt":(12.2408,109.1968),"ph2":(12.2381,109.1902),
    "tl":(12.2367,109.1943),"pl":(12.2280,109.1820),"vt":(12.2223,109.1975),"vn":(12.2140,109.2050),
}
# Четыре укрупнённых района реформы в NT_APPROX не входят и входить не должны:
# у них, в отличие от двенадцати старых, есть НАСТОЯЩИЕ границы, и точку можно
# не назначать рукой, а посчитать из них. До 10 сентября 2026 это было неважно --
# все строки таких районов приходили с Chợ Tốt со своими координатами. Первые же
# три телеграм-строки в Бак Нячанге остались вовсе без координат: у объявления
# координат нет, а запасного центра для ключа не существует. На карте это не
# ошибка, а пропажа -- пина просто нет, и объявление с карты не найти.


def ring_centre(rings):
    """Точка внутри района -- центр тяжести самого большого кольца границы.

    Кольцо выбирается ПО ПЛОЩАДИ, а не по числу точек. Это не придирка: у
    Phường Nha Trang восемнадцать колец, и самое подробное из них -- остров
    Хон Че, чья изрезанная береговая линия описана гуще, чем городской берег.
    По числу точек побеждал остров, и «центр района» оказывался в море в восьми
    километрах от набережной."""
    area = lambda r: abs(sum(r[i][1] * r[(i + 1) % len(r)][0] - r[(i + 1) % len(r)][1] * r[i][0]
                             for i in range(len(r)))) / 2
    ring = max(rings, key=area)
    a = cx = cy = 0.0
    for i in range(len(ring)):
        y1, x1 = ring[i]
        y2, x2 = ring[(i + 1) % len(ring)]
        f = x1 * y2 - x2 * y1
        a += f
        cx += (x1 + x2) * f
        cy += (y1 + y2) * f
    if abs(a) < 1e-12:
        return (sum(p[0] for p in ring) / len(ring), sum(p[1] for p in ring) / len(ring))
    lat, lon = cy / (3 * a), cx / (3 * a)
    # У вогнутого или прибрежного контура центр тяжести может оказаться снаружи
    # -- тогда берём ближайшую точку самой границы, а не красивое, но чужое
    # место.
    x, y, inside, j = lon, lat, False, len(ring) - 1
    for i in range(len(ring)):
        yi, xi = ring[i]
        yj, xj = ring[j]
        if ((xi > x) != (xj > x)) and (y < (yj - yi) * (x - xi) / ((xj - xi) or 1e-12) + yi):
            inside = not inside
        j = i
    if not inside:
        return min(ring, key=lambda p: (p[0] - lat) ** 2 + (p[1] - lon) ** 2)
    return (lat, lon)


def nt_fallback_point(key, rings):
    """Запасная точка укрупнённого района: сначала по своим же объявлениям.

    ГЕОМЕТРИЧЕСКИЙ ЦЕНТР ЗДЕСЬ ПЛОХ САМ ПО СЕБЕ. Phường Nha Trang вобрал в себя
    Винь Нгуен вместе с островом Хон Че, и остров по площади больше городской
    суши -- центр тяжести района лежит в море, в восьми километрах от
    набережной. Формально это и правда центр района; для пина с подписью
    «приблизительно -- центр района» -- бесполезная точка.
    Поэтому, когда у района уже есть объявления с настоящими координатами (их
    привозит с собой Chợ Tốt), берётся их середина: это не «центр многоугольника»,
    а «где в этом районе вообще сдают». Трёх точек хватает, чтобы одна случайная
    не определяла район в одиночку. Нет ни одной -- остаётся центр границы, и он
    сам себя исправит, как только появится первая строка с координатами."""
    own = [(r["lat"], r["lon"]) for l in listings
           if l["city"] == "nha-trang" and l["district"] == key
           for r in [pin_results.get(str(l["id"]))] if r]
    if len(own) >= 3:
        return (sum(p[0] for p in own) / len(own), sum(p[1] for p in own) / len(own))
    return ring_centre(rings)


NT_APPROX.update({k: nt_fallback_point(k, v["rings"])
                  for k, v in ward_boundaries["nha-trang"].items()})

lat_lon = {}
missing = 0
for l in listings:
    city = l["city"]; lid = str(l["id"])
    if city == "nha-trang":
        # Real coordinates first. NT_APPROX is a fallback, not the rule: since
        # 9 Sep 2026 step2 records the ad's own lat/lon for Nha Trang too, and
        # backfill_chotot_coords.py filled them in for the older rows. A pin on
        # the ad's own coordinates is worth more than one of twelve fixed points.
        r = pin_results.get(lid)
        if r:
            lat_lon[lid] = {"lat": r["lat"], "lon": r["lon"], "geocoded": r["source"] in ("geocode", "chotot")}
            continue
        c = NT_APPROX.get(l["district"])
        if c: lat_lon[lid] = {"lat": c[0], "lon": c[1], "geocoded": False}
        else: missing += 1
        continue
    r = pin_results.get(lid)
    if r:
        # "chotot" = coordinates shipped by the ad itself (chotot_coords.json), as precise as it gets
        lat_lon[lid] = {"lat": r["lat"], "lon": r["lon"], "geocoded": r["source"] in ("geocode", "chotot")}
    else:
        missing += 1

json.dump(lat_lon, open("leaflet_listing_latlon.json","w",encoding="utf-8"), ensure_ascii=False)
print("listings with lat/lon:", len(lat_lon), "missing:", missing)
