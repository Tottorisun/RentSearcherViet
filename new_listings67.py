NEW_SRC = '''
L(1642,"ho-chi-minh","kh","Квартира",18000000,75,
  "2-спальная квартира, 75м², 2 с/у, ЖК Masteri Millennium, ул. Bến Vân Đồn, Khánh Hội — кондиционер, кровать, холодильник в комплекте.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-masteri-millennium/cho-2pn-2wc-75m2-chi-voi-18-trieu-tai-quan-4-tp-hcm-pr46226152","сегодня",0,source="batdongsan",
  details={"photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825164216-f8d5_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825164216-8df7_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825164216-b90c_wm.jpg"]}),

L(1643,"ho-chi-minh","bth","Квартира",None,35,
  "Квартира на первой линии ул. Trần Hưng Đạo, Bến Thành Q1, 35м² (полезная площадь) — есть лифт, полная меблировка, подходит и для проживания, и для маленького бизнеса (нейл-салон, спа, парикмахерская); рядом Q1, Q4, Q5, Bình Thạnh.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-ben-thanh-tp-ho-chi-minh/cho-thang-may-mat-tien-ao-full-noi-that-pr46225725","сегодня",0,source="batdongsan",
  details={"notice": "цена по запросу — не указана ни в заголовке, ни в тексте объявления", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825153518-0585_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825153514-80d2_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825153516-4607_wm.jpg"]}),

L(1644,"ho-chi-minh","ak","Дом",100000000,250,
  "Вилла целиком, участок 230м² / жилая площадь 250м² + сад, Trệt + 1 этаж, 5 спален, 5 с/у, собственный бассейн, сауна, комната отдыха, ул. Trần Não, An Khánh — полная меблировка, подходит для семьи или иностранных специалистов.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-tran-nao-phuong-an-khanh-tp-ho-chi-minh/cho-villa-5-phong-full-noi-that-boi-gia-100-trieu-pr46225147","сегодня",0,source="batdongsan",
  details={"photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825142323-666d_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825142323-bfd5_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825142323-b1ba_wm.jpg"]}),

L(1645,"ho-chi-minh","kh","Квартира",32000000,103,
  "3-спальная квартира, 103м², 2 с/у, ЖК Masteri Millennium, 132 Bến Vân Đồn, Q4 — широкий балкон, вид на город, бассейн-инфинити, тренажёрный зал, зона BBQ, ресепшен и охрана 24/7.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-masteri-millennium/cho-quan-4-3pn-103m-full-noi-that-view-song-cau-ba-son-sat-q1-lh-pr46223393","сегодня",0,source="batdongsan",
  details={"photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825092908-0dad_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825092908-7cb3_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/08/25/20260825092908-c79e_wm.jpg"]}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content

new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
assert new_content != content
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", NEW_SRC.count("L("), "listings")
