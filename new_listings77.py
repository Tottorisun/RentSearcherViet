# -*- coding: utf-8 -*-
NEW_SRC = '''
L(1831,"ho-chi-minh","th","Дом",13500000,60,
  "Дом целиком, 5x12 м (60м²), 3 спальни, 2 с/у, просторная терраса на крыше. Пер. 791 Trần Xuân Soạn, район Kiều Đàm, Tân Hưng — можно жить, под VP/nail-spa/онлайн-продажи или большую семью; охраняемый квартал, заезд на машине.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134365107.htm","1 день назад",1,source="chotot",
  details={"photos": ["https://cdn.chotot.com/Ql38MAWc4pI5UpSKZlxRREu42dBXm7X_lY1YFWsF2Ws/preset:view/plain/09ef4d0b99fe5234f19569ce58a3c092-2999305389148934171.jpg", "https://cdn.chotot.com/YyvLuefRMFyR9O5dnni_no3-c2TCIxPQAtxF92fXyfQ/preset:view/plain/f3c3c14d7d115d9741a8a7482e803b96-2999305389350116627.jpg", "https://cdn.chotot.com/Qmnj4GE7X5SPe4RuZKOKl4-_gUvaF4L31QaJ714_uQ0/preset:view/plain/2671b917b79cfa9eee60034b4caea0b4-2999305389331321823.jpg"]}),
L(1832,"ho-chi-minh","th","Дом",17000000,70,
  "Дом целиком, 70м², 2 спальни, 3 с/у, полная меблировка, можно въезжать сразу. Ул. Trần Xuân Soạn, Tân Hưng — рядом RMIT Nam Sài Gòn, Đại học Tôn Đức Thắng, UFM, удобно до Phú Mỹ Hưng и Lotte Mart.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-tran-xuan-soan-phuong-tan-hung-14-59/cho-nguyen-can-p-quan-7-pr46233798","сегодня",0,source="batdongsan",
  details={"photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/27/20260827153123-e150_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/27/20260827153121-9ce7_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/27/20260827153124-e475_wm.jpg"],"notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления (pr46233798) — выше максимального ID, зафиксированного ранее (pr46229962), и фото загружены сегодня (27.08). Цена подтверждена дважды: в карточке поиска и на странице объявления (поле «Khoảng giá»)."}),
L(1833,"ho-chi-minh","tm","Дом",19000000,40,
  "Дом целиком, 4x10 м (40м²), цоколь + антресоль + 2 этажа + терраса на крыше, 5 спален, 3 с/у. Ул. Tân Mỹ, Phường Tân Phú (новая Tân Mỹ), Q7 — подходит для семьи, офиса компании или онлайн-бизнеса.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-tan-my-phuong-tan-phu-19-59/pho-3-lau-cho-tai-canh-hung-pr46232300","сегодня",0,source="batdongsan",
  details={"photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/27/20260827104158-7596_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/27/20260827104201-08e6_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/27/20260827104204-2f61_wm.jpg"],"notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления (pr46232300) — выше максимального ID, зафиксированного ранее (pr46229962), и фото загружены сегодня (27.08). Цена подтверждена дважды: в карточке поиска и на странице объявления (поле «Khoảng giá»)."}),
'''

import re

with open("rebuild_final.py", "r", encoding="utf-8") as f:
    content = f.read()

marker = "]\n\n# Real lat/lon"
idx = content.find(marker)
if idx == -1:
    raise SystemExit("marker not found")

new_content = content[:idx] + NEW_SRC + content[idx:]

with open("rebuild_final.py", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Inserted", NEW_SRC.count("\nL("), "new listings")

# Cross-source duplicate: pr46231464 (Tan My, 4x20/80m2, 300m from Tan My market,
# 30tr/month) matches the already-tracked property at L(873) exactly on price,
# lot dimensions and market-distance landmark -- add as an alsoOn entry, not a
# new card.
old_alsoOn = '"alsoOn":[{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134234709.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134273497.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134254961.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134244463.htm"}]'
new_alsoOn = '"alsoOn":[{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134234709.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134273497.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134254961.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134244463.htm"},{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-tan-phu-19/cho-nguyen-can-p-quan-7-nay-la-my-tp-hcm-pr46231464"}]'

with open("rebuild_final.py", "r", encoding="utf-8") as f:
    content = f.read()

if old_alsoOn not in content:
    raise SystemExit("alsoOn block for L(873) not found -- aborting to avoid silent no-op")

content = content.replace(old_alsoOn, new_alsoOn, 1)

with open("rebuild_final.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated L(873) alsoOn with new batdongsan re-post pr46231464")
