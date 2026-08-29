# -*- coding: utf-8 -*-
NEW_SRC = '''
L(2124,"ho-chi-minh","tm","Квартира",35000000,150,
  "Midtown M5, 2-спальная квартира + отдельный кабинет, 2 с/у, 150 м², полная меблировка, можно заезжать сразу. Подходит для семьи, специалистов или иностранцев. Ул. 17/4, Tân Mỹ (Phú Mỹ Hưng), Q7.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-midtown-phu-my-hung/cho-m5-2pn-phong-lam-viec-150m-35-trieu-thang-pr46240701","сегодня",0,source="batdongsan",
  descEn="Midtown M5, 2-bedroom apartment + separate office room, 2 bathrooms, 150m2, fully furnished, move-in ready. Suitable for a family, professionals, or expats. 17/4 St., Tan My (Phu My Hung), District 7.",
  details={"notice": "дата — по данным сайта batdongsan.com.vn («đăng hôm nay»), точная дата первой публикации не подтверждена.", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/29/20260829145838-07b1_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/29/20260829145838-0898_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/29/20260829145838-d359_wm.jpg"]}),
L(2125,"ho-chi-minh","tm","Дом",55000000,126,
  "Дом целиком 7x18 м (126 м²), 3 этажа, 4 спальни, полная меблировка. Цена 55 млн ₫/мес, торг уместен. KDC Nam Viên, Tân Mỹ (Phú Mỹ Hưng), Q7.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-17-4-khu-dan-cu-nam-vien/cho-phu-my-hung-dien-tich-126m2-full-noi-that-55-trieu-thang-thuong-luong-pr46240181","сегодня",0,source="batdongsan",
  descEn="Whole house 7x18m (126m2), 3 floors, 4 bedrooms, fully furnished. Price 55 million VND/month, negotiable. KDC Nam Vien, Tan My (Phu My Hung), District 7.",
  details={"notice": "дата — по данным сайта batdongsan.com.vn («đăng hôm nay»), точная дата первой публикации не подтверждена.", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/29/20260829121915-5076_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/29/20260829121917-3bab_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/29/20260829121919-3d7e_wm.jpg"]}),
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
