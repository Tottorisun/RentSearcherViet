# -*- coding: utf-8 -*-
import json, math

W = "C:/Users/User/AppData/Local/Temp/claude/D-----------------Rent-Searcher/8ee03ce4-8da9-4f83-bde7-358c449cdd8c/scratchpad"

def assemble_rings(ways):
    segs = [list(w) for w in ways if len(w) >= 2]
    rings = []
    used = [False]*len(segs)
    for i in range(len(segs)):
        if used[i]: continue
        used[i] = True
        ring = list(segs[i])
        changed = True
        while changed:
            changed = False
            for j in range(len(segs)):
                if used[j]: continue
                s = segs[j]
                if ring[-1] == s[0]: ring.extend(s[1:]); used[j]=True; changed=True
                elif ring[-1] == s[-1]: ring.extend(list(reversed(s))[1:]); used[j]=True; changed=True
                elif ring[0] == s[-1]: ring[0:0]=s[:-1]; used[j]=True; changed=True
                elif ring[0] == s[0]: ring[0:0]=list(reversed(s))[:-1]; used[j]=True; changed=True
        rings.append(ring)
    return [r for r in rings if len(r) >= 4]

def point_in_ring(x, y, ring):
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        yi, xi = ring[i][0], ring[i][1]
        yj, xj = ring[j][0], ring[j][1]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-15) + xi):
            inside = not inside
        j = i
    return inside

def point_in_rings(lon, lat, rings):
    for r in rings:
        if point_in_ring(lon, lat, r):
            return True
    return False

data = json.load(open(W + "/nt_overpass.json", encoding="utf-8"))
WANT = ["Phường Nha Trang","Phường Bắc Nha Trang","Phường Nam Nha Trang","Phường Tây Nha Trang"]
all_rings = []
for e in data["elements"]:
    if e.get("tags",{}).get("name") in WANT:
        outer = [[(pt["lat"],pt["lon"]) for pt in m["geometry"]] for m in e.get("members",[]) if m.get("role")=="outer" and m.get("geometry")]
        all_rings.extend(assemble_rings(outer))

NEI = {
    "vh": ("Vĩnh Hải", 12.2884474, 109.1989944),
    "vp": ("Vĩnh Phước", 12.2739933, 109.2013551),
    "vt2": ("Vạn Thạnh", 12.2633018, 109.1956961),
    "ps": ("Phương Sài", 12.2537024, 109.1818496),
    "nh": ("Ngọc Hiệp", 12.2536684, 109.184387),
    "ph": ("Phước Hải", 12.2445653, 109.1820899),
    "lt": ("Lộc Thọ", 12.2380498, 109.1915043),
    "ph2": ("Phước Hòa", 12.2357258, 109.1834644),
    "tl": ("Tân Lập", 12.2320652, 109.1951414),
    "pl": ("Phước Long", 12.2166063, 109.188334),
    "vt": ("Vĩnh Trường", 12.1974641, 109.2091372),
    "vn": ("Vĩnh Nguyên", 12.1800, 109.2050),
}

LAT_MIN, LAT_MAX = 12.165, 12.300
LON_MIN, LON_MAX = 109.135, 109.225
lat0 = (LAT_MIN+LAT_MAX)/2
coslat = math.cos(math.radians(lat0))
def project(lat, lon):
    x = (lon - LON_MIN) * coslat
    y = -(lat - LAT_MIN)
    return x, y

x1,y1 = project(LAT_MAX, LON_MAX)
x0,y0 = project(LAT_MIN, LON_MIN)
W_span = x1 - x0
H_span = y0 - y1
SCALE = 1000.0 / max(W_span, H_span)
ref_x, ref_y = project(LAT_MAX, LON_MIN)

COLS, ROWS = 130, 145
cellW = (LON_MAX-LON_MIN)/COLS
cellH = (LAT_MAX-LAT_MIN)/ROWS
cellPxW = cellW*coslat*SCALE
cellPxH = cellH*SCALE

grid = {}
for gy in range(ROWS):
    lat = LAT_MAX - (gy+0.5)*cellH
    for gx in range(COLS):
        lon = LON_MIN + (gx+0.5)*cellW
        if not point_in_rings(lon, lat, all_rings):
            continue
        best_key, best_d = None, 1e18
        for key,(name, nlat, nlon) in NEI.items():
            dx = (lon-nlon)*coslat
            dy = (lat-nlat)
            d = dx*dx+dy*dy
            if d < best_d:
                best_d = d; best_key = key
        grid[(gx,gy)] = best_key

print("land cells:", len(grid))
counts = {}
for k in grid.values(): counts[k] = counts.get(k,0)+1
print(counts)

def cell_corner(gx, gy):
    lat_top = LAT_MAX - gy*cellH
    lon_left = LON_MIN + gx*cellW
    x,y = project(lat_top, lon_left)
    return (round((x-ref_x)*SCALE,1), round((y-ref_y)*SCALE,1))

out_cells = []
for (gx,gy),key in grid.items():
    px,py = cell_corner(gx,gy)
    out_cells.append({"x":px, "y":py, "key":key})

# ---- boundary segment extraction (dedup) ----
border_set = set()
def add_edge(p1, p2):
    e = (p1,p2) if p1 <= p2 else (p2,p1)
    border_set.add(e)

for (gx,gy),key in grid.items():
    tl = cell_corner(gx,gy)
    tr = cell_corner(gx+1,gy)
    bl = cell_corner(gx,gy+1)
    br = cell_corner(gx+1,gy+1)
    # right neighbor
    rk = grid.get((gx+1,gy))
    if rk != key: add_edge(tr, br)
    # left neighbor
    lk = grid.get((gx-1,gy))
    if lk != key: add_edge(tl, bl)
    # bottom neighbor
    dk = grid.get((gx,gy+1))
    if dk != key: add_edge(bl, br)
    # top neighbor
    uk = grid.get((gx,gy-1))
    if uk != key: add_edge(tl, tr)

print("border segments:", len(border_set))

LABEL_NUDGE = {"ps": (-24, -10), "nh": (28, 14), "ph": (-6, 4)}
labels = {}
for k,(name,lat,lon) in NEI.items():
    x,y = project(lat,lon)
    px = (x-ref_x)*SCALE
    py = (y-ref_y)*SCALE
    nx, ny = LABEL_NUDGE.get(k, (0,0))
    labels[k] = {"name":name, "x":round(px+nx,1), "y":round(py+ny,1)}

canvasW = (project(LAT_MIN,LON_MAX)[0]-ref_x)*SCALE
canvasH = (project(LAT_MIN,LON_MIN)[1]-ref_y)*SCALE

result = {
    "viewBox": f"0 0 {canvasW:.1f} {canvasH:.1f}",
    "cellW": round(cellPxW,2), "cellH": round(cellPxH,2),
    "cells": out_cells,
    "borders": [[p1,p2] for p1,p2 in border_set],
    "labels": labels
}
json.dump(result, open(W+"/nt_realtor_map.json","w",encoding="utf-8"), ensure_ascii=False)
print("wrote nt_realtor_map.json, cells:", len(out_cells), "borders:", len(border_set))
