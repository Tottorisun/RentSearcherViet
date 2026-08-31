# -*- coding: utf-8 -*-
NEW_SRC = '''
L(2145,"ho-chi-minh","ak","Дом",45000000,160,
  "Дом целиком, фасад 9,3×17 м, цоколь + 2 этажа + терраса на крыше, 5 спален, 4 с/у, двор и гараж для машины. Закрытый охраняемый квартал (compound), An Khánh, Thủ Đức.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-an-khanh-tp-ho-chi-minh/cho-q2-gia-45tr-thang-pr46244333","сегодня",0,source="batdongsan",
  descEn="Whole house, 9.3x17m frontage, ground floor + 2 floors + rooftop terrace, 5 bedrooms, 4 bathrooms, yard and car garage. Gated security compound, An Khanh, Thu Duc.",
  details={"notice": "дата — по данным сайта batdongsan.com.vn («đăng hôm nay»), точная дата первой публикации не подтверждена.", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831101832-5649_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831101832-8cf6_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831101831-15f2_wm.jpg"]}),
L(2146,"ho-chi-minh","ak","Дом",80000000,250,
  "Вилла в центре Thảo Điền, цоколь + 2 этажа, 4 спальни, 5 с/у, собственный бассейн, большой сад. Есть кондиционеры и часть базовой мебели. Подходит для семьи или под офис.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-an-khanh-tp-ho-chi-minh/cho-biet-thu-san-vuon-boi-khu-thao-ien-gia-80-trieu-pr46240810","2 дня назад",2,source="batdongsan",
  descEn="Villa in central Thao Dien, ground floor + 2 floors, 4 bedrooms, 5 bathrooms, private pool, large garden. AC units and some basic furniture included. Suitable for a family or as an office.",
  details={"notice": "дата — по данным сайта batdongsan.com.vn («đăng hôm nay»), точная дата первой публикации не подтверждена.", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/29/20260829152322-1e1a_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/29/20260829152322-ef1f_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/29/20260829152322-a666_wm.jpg"]}),
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
