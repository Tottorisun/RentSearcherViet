# -*- coding: utf-8 -*-
NEW_SRC = '''
L(1000117,"ho-chi-minh","kh","Квартира",21000000,65,
  "2-спальная квартира (2 с/у), 65 м², ЖК Masteri Millennium, ул. Bến Vân Đồn, Khánh Hội, Q4. Балкон, вид на реку, продувается. Рядом Q1/Q2 (5 минут).",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-masteri-millennium/gap-2pn-65m2-ban-cong-view-song-thoang-on-quan-4-sat-q1-q2-lh-pr46244746","сегодня",0,source="batdongsan",
  descEn="2-bedroom apartment (2 bathrooms), 65m2, Masteri Millennium complex, Ben Van Don St, Khanh Hoi, District 4. Balcony, river view, airy/breezy. Near District 1/2 (5 minutes).",
  details={"notice": "точная дата первой публикации не подтверждена; оценка «сегодня» сделана по дате загрузки фото на batdongsan.com.vn (31 авг). Цена подтверждена в описании объявления (21 триệu VND/tháng).", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831125304-9048_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831125306-6a45_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831125308-94be_wm.jpg"]}),
L(1000118,"ho-chi-minh","tm","Квартира",11000000,147,
  "3-спальная квартира (4 с/у), 147 м², ЖК Era Town, ул. 15B Nguyễn Lương Bằng, Tân Mỹ (Phú Mỹ Hưng), Q7. Свежий ремонт (покраска), средний этаж.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-the-era-town/eratown-nha-moi-son-sua-moi-ep-tang-trung-gia-11tr-thang-lh-ms-hien-pr46244864","сегодня",0,source="batdongsan",
  descEn="3-bedroom apartment (4 bathrooms), 147m2, Era Town complex, 15B Nguyen Luong Bang St, Tan My (Phu My Hung), District 7. Freshly repainted, mid floor.",
  details={"notice": "точная дата первой публикации не подтверждена; оценка «сегодня» сделана по дате загрузки фото на batdongsan.com.vn (31 авг). Цена подтверждена в описании объявления (11 triệu VND/tháng). В базе уже есть несколько других юнитов в ЖК Era Town другой площади — это отдельный юнит (147 м²).", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831135553-50c3_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831135553-5118_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831135553-389a_wm.jpg"]}),
L(1000119,"ho-chi-minh","tm","Квартира",24000000,76,
  "2-спальная квартира (2 с/у), 76 м², ЖК The Aurora, ул. Nguyễn Lương Bằng, Tân Mỹ (Phú Mỹ Hưng), Q7. Новая полная меблировка (100%).",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-the-aurora-phu-my-hung/cho-noi-that-moi-gia-tot-lh-pr46244846","сегодня",0,source="batdongsan",
  descEn="2-bedroom apartment (2 bathrooms), 76m2, The Aurora complex, Nguyen Luong Bang St, Tan My (Phu My Hung), District 7. New, 100% furnished.",
  details={"notice": "точная дата первой публикации не подтверждена; оценка «сегодня» сделана по дате загрузки фото на batdongsan.com.vn (31 авг). Цена подтверждена в описании объявления (24 triệu/tháng).", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831134611-6162_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831134612-d17d_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/31/20260831134613-38e6_wm.jpg"]}),
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
