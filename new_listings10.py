# -*- coding: utf-8 -*-
exec(open("new_listings10_data.py", encoding="utf-8").read())

def fmt_area(a):
    if a is None: return None
    if a == int(a): return str(int(a))
    return str(a)

def fmt_vnd(v):
    return "{:,}".format(v).replace(",", " ")

lines = []
next_id = 416
for (city, dist, type_, price, area, desc, url, orig_total, usd, extra) in ROWS:
    notice = ("Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), "
               "не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: " +
               fmt_vnd(orig_total) + " ₫ (≈" + str(usd) + " $).")
    details = {"notice": notice}
    if extra:
        details["policy"] = extra
    area_s = fmt_area(area)
    line = 'L(%d,"%s","%s","%s",%d,%s,"%s","%s","проверено 15 авг",1,source="airbnb",details=%r),' % (
        next_id, city, dist, type_, price,
        (area_s if area_s is not None else "None"),
        desc.replace('"','\\"'), url, details
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
print("inserted", len(lines), "airbnb listings, ids", 416, "..", next_id-1)
