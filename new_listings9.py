# -*- coding: utf-8 -*-
exec(open("new_listings9_data.py", encoding="utf-8").read())

def fmt_area(a):
    if a is None: return None
    if a == int(a): return str(int(a))
    return str(a)

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

NOTICE = ("массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при "
          "бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026")

lines = []
next_id = 350
for (city, dist, type_, price, area, beds, desc), url in zip(ROWS, URLS):
    details = {"notice": NOTICE}
    if beds:
        details["amenities"] = str(beds) + (" спальня" if beds == 1 else (" спальни" if beds < 5 else " спален"))
    area_s = fmt_area(area)
    line = 'L(%d,"%s","%s","%s",%d,%s,"%s","%s","проверено 15 авг",1,source="batdongsan",details=%r),' % (
        next_id, city, dist, type_, price,
        (area_s if area_s is not None else "None"),
        esc(desc), url, details
    )
    lines.append(line)
    next_id += 1

NEW_SRC = "\n".join(lines)

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", len(lines), "batdongsan listings, ids", 350, "..", next_id-1)
