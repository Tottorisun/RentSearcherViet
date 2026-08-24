NEW_SRC = '''
L(1582,"ho-chi-minh","tm","Дом",25000000,48,
  "Дом на красной линии, фасад 10м, 48м² (4×12м, 1 этаж + 2 этажа), ул. Đường Số 1, Tân Mỹ (быв. Tân Phú, Q7) — 4 спальни, 3 с/у, просторная гостиная, электрический рулонный ставень, кондиционеры, водонагреватель на солнечных батареях; подходит для жилья или под офис/компанию.",
  "https://batdongsan.com.vn/cho-thue-nha-mat-pho-duong-so-1-phuong-tan-my-tp-ho-chi-minh/cho-tien-uong-10m-phu-q7-phu-hop-mo-cong-ty-van-phong-25-tr-pr46222623","сегодня",0,source="batdongsan",
  details={"photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824231318-e550_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824231318-c44a_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824231318-60a8_wm.jpg"], "notice": "batdongsan.com.vn не публикует точную дату размещения — указан статус сайта, дата не проверена независимо"}),

L(1583,"ho-chi-minh","tm","Квартира",5000000,30,
  "Сервисная квартира-дуплекс с балконом, 1 спальня, 1 с/у, 30м², ул. Nguyễn Thị Thập, Tân Mỹ (Phú Mỹ Hưng) — базовая мебель, рядом медпункт квартала Tân Mỹ, больницы Tâm Đức и FV, университет Tài chính — Marketing.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-nguyen-thi-thap-phuong-tan-my-tp-ho-chi-minh/cho-duplex-ban-cong-30m2-5tr-o-uoc-3-nguoi-gan-phu-hung-ufm-crescent-mall-pr46222389","сегодня",0,source="batdongsan",
  details={"photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824211625-81dd_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824211626-1c5b_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824211626-dff1_wm.jpg"], "notice": "batdongsan.com.vn не публикует точную дату размещения — указан статус сайта, дата не проверена независимо"}),

L(1584,"ho-chi-minh","bth","Квартира",10500000,45,
  "Сервисная 1-спальная квартира, 45м², ул. Nguyễn Thái Bình, Bến Thành (Q1) — полная меблировка, готова к заезду, Wi-Fi на каждом этаже, разрешены небольшие домашние животные, в нескольких минутах ходьбы от рынка Bến Thành, Vincom Center, Takashimaya и пешеходной ул. Nguyễn Huệ.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-nguyen-thai-binh-phuong-ben-thanh-tp-ho-chi-minh/cho-dich-vu-1pn-rong-rai-quan-1-pr46222285","сегодня",0,source="batdongsan",
  details={"photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824202943-a3db_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824202944-05c5_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824202945-80c6_wm.jpg"], "notice": "batdongsan.com.vn не публикует точную дату размещения — указан статус сайта, дата не проверена независимо"}),

L(1585,"ho-chi-minh","kh","Студия",12000000,30,
  "Студия с отдельной кухонной зоной, 30м², ЖК Masteri Millennium, 132 Bến Vân Đồn, Khánh Hội (Q4) — полная меблировка, светлая и просторная; бассейн, спортзал, шопхаус с кафе/рестораном/банком в комплексе; залог 2 месяца, договор на 1 год.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-masteri-millennium/studio-tach-bep-full-noi-that-view-thoang-ep-gym-boi-mien-phi-pr46222193","сегодня",0,source="batdongsan",
  details={"contact": "Nguyễn Hạnh Dung", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824194256-1f28_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824194256-f397_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824194256-c29f_wm.jpg"], "notice": "batdongsan.com.vn не публикует точную дату размещения — указан статус сайта, дата не проверена независимо"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content

new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
assert new_content != content
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", NEW_SRC.count("L("), "listings")
