# -*- coding: utf-8 -*-
import re, json

W = "C:/Users/User/AppData/Local/Temp/claude/D-----------------Rent-Searcher/8ee03ce4-8da9-4f83-bde7-358c449cdd8c/scratchpad"

# existing IDs already in rebuild_final.py
content = open(W + "/rebuild_final.py", encoding="utf-8").read()
existing_ids = set(re.findall(r'/(\d{6,9})\.htm', content))
print("existing numeric IDs count:", len(existing_ids))

NT_MAP = {
    "Phường Lộc Thọ":"lt","Phường Tân Lập":"tl","Phường Phương Sài":"ps","Phường Ngọc Hiệp":"nh",
    "Phường Phước Hải":"ph","Phường Phước Hòa":"ph2","Phường Phước Long":"pl","Phường Vĩnh Trường":"vt",
    "Phường Vĩnh Nguyên":"vn","Phường Vĩnh Hải":"vh","Phường Vĩnh Phước":"vp","Phường Vạn Thạnh":"vt2",
    "Phường Vĩnh Hòa":"vh","Phường Xương Huân":"vt2","Xã Vĩnh Trung":"ps","Xã Vĩnh Hiệp":"ps","Phường Phương Sơn":"ps",
}
DL_MAP = {"Phường 1":"xh","Phường 2":"xh","Phường 3":"xh","Phường 4":"xh","Phường 10":"xh",
          "Phường 8":"lv","Phường 9":"lv","Phường 5":"cl","Phường 6":"cl","Phường 7":"lb"}
DN_MAP = {
    "Q. Hải Châu":"hc","Q. Hải Châu (P. Hòa Cường mới)":"hcg",
    "Q. Sơn Trà":"st","Q. Sơn Trà (P. An Hải mới)":"ah",
    "Q. Ngũ Hành Sơn":"ns",
    "Q. Thanh Khê":"tk","Q. Thanh Khê (P. An Khê mới)":"ak",
    "Q. Cẩm Lệ":"cl2","Q. Cẩm Lệ (P. Hòa Xuân mới)":"hx","Q. Cẩm Lệ (P. An Khê mới)":"ak",
    "Q. Liên Chiểu":"lc","Q. Liên Chiểu (P. Hòa Khánh mới)":"hk","Q. Liên Chiểu (P. Hải Vân mới)":"lc",
}
CITY_MAP = {"Da Nang":("da-nang",DN_MAP),"Nha Trang":("nha-trang",NT_MAP),"Da Lat":("da-lat",DL_MAP)}
FURN_RU = {"Nội thất đầy đủ":"с полной мебелью","Nội thất cao cấp":"с мебелью повышенной комфортности","Nhà trống":"без мебели"}
TYPE_RU = {"room":"Комната","apartment":"Квартира"}

def posted_to_days(p):
    p = p.strip()
    if p in ("Tin ưu tiên","актуально"): return 0
    m = re.match(r'(\d+)\s*giờ', p)
    if m: return 0
    m = re.match(r'(\d+)\s*ngày', p)
    if m: return int(m.group(1))
    m = re.match(r'(\d+)\s*tuần', p)
    if m: return int(m.group(1))*7
    return 0

def posted_ru(p):
    p = p.strip()
    if p in ("Tin ưu tiên","актуально"): return "актуально"
    m = re.match(r'(\d+)\s*giờ', p)
    if m: return f"{m.group(1)} ч. назад"
    m = re.match(r'(\d+)\s*ngày', p)
    if m:
        n = int(m.group(1))
        return "вчера" if n==1 else f"{n} дн. назад"
    m = re.match(r'(\d+)\s*tuần', p)
    if m:
        n = int(m.group(1))
        return f"{n} нед. назад"
    return p

rows = []
skipped_dup = skipped_unmapped = 0
for line in open(W+"/raw_batch5.txt", encoding="utf-8"):
    line = line.strip()
    if not line: continue
    parts = [p.strip() for p in line.split("|")]
    if len(parts) != 8: continue
    city_txt, district_txt, kind, price, area, furn, url, posted = parts
    m = re.search(r'/(\d{6,9})\.htm', url)
    if not m: continue
    numid = m.group(1)
    if numid in existing_ids:
        skipped_dup += 1
        continue
    existing_ids.add(numid)  # dedupe within this batch too
    city_key, dmap = CITY_MAP[city_txt]
    lookup_txt = district_txt
    if city_txt in ("Nha Trang","Da Lat"):
        lookup_txt = re.sub(r'\s*\(P\..*?mới\)\s*$', '', district_txt).strip()
    key = dmap.get(lookup_txt)
    if key is None:
        skipped_unmapped += 1
        continue
    price_i = int(price)
    area_v = None if area.lower() in ("none","không ghi") else int(area)
    furn_v = None if furn == "không ghi" else furn
    rows.append((city_key, key, kind, price_i, area_v, furn_v, url, posted))

print("new rows:", len(rows), "skipped_dup:", skipped_dup, "skipped_unmapped:", skipped_unmapped)

lines = []
# find current max id in file
existing_L_ids = [int(x) for x in re.findall(r'\nL\((\d+),', content)]
id_counter = max(existing_L_ids) + 1
print("starting id:", id_counter)

for city_key, dkey, kind, price, area, furn, url, posted in rows:
    type_ru = TYPE_RU[kind]
    furn_txt = (", " + FURN_RU[furn]) if furn in FURN_RU else ""
    desc = f"{type_ru}{furn_txt}."
    area_lit = "None" if area is None else str(area)
    days = posted_to_days(posted)
    posted_txt = posted_ru(posted)
    lines.append(
        f'L({id_counter},"{city_key}","{dkey}","{type_ru}",{price},{area_lit},\n'
        f'  "{desc}",\n'
        f'  "{url}","{posted_txt}",{days},source="chotot"),\n'
    )
    id_counter += 1

NEW_SRC = "\n".join(lines)

listings_end_idx = content.rfind("]\n\nMAPS = {")
assert listings_end_idx != -1
insertion_point = listings_end_idx  # position of the "]"
new_content = content[:insertion_point] + NEW_SRC.strip() + "\n" + content[insertion_point:]
open(W+"/rebuild_final.py","w",encoding="utf-8").write(new_content)
print("inserted", len(rows), "listings")
