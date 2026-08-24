# -*- coding: utf-8 -*-

NEW_SRC = '''
L(1522,"ho-chi-minh","ak","Студия",7500000,40,
  "Студия/1-спальная квартира с балконом, 40м², ул. Trần Não, An Khánh (бывш. Quận 2) — рядом мост через Sài Gòn, удобный выезд в Q1/Q3/Q5/Q10 и Bình Thạnh, полная меблировка, охраняемая парковка, круглосуточная охрана и камеры, не затапливает.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thu-duc-tp-ho-chi-minh/111628706.htm","4 дня назад",4,source="chotot",
  details={"contact":"Ngọc Thịnh Hifriendz","photos":["https://cdn.chotot.com/GsGv0JHV4Pz2i--NY06aRndMXJk14v01g7I-MplZENY/preset:view/plain/fd4990a46412011868767343119075db-2937131054670844901.jpg","https://cdn.chotot.com/7kROGUXTadDnmxK11TaZD65dzduS30IJ-lxsazd0Gl4/preset:view/plain/7db7b0c008224edb7ecb9a3569ea8d03-2937131054798736558.jpg"]}),

L(1523,"ho-chi-minh","th","Комната",5100000,30,
  "Комната с отдельным санузлом в ЖК Phú Hoàng Anh, рядом Phú Mỹ Hưng, ул. Nguyễn Hữu Thọ, Tân Hưng (Q7) — 30м², кровать, кондиционер, общая кухня и стиральная машина. Причина сдачи — переезд хозяина по работе.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134263434.htm","4 дня назад",4,source="chotot",
  details={"contact":"Lin Nguyễn","photos":["https://cdn.chotot.com/GtpXlvUKBITO28qSJ8TqPtznG921gXShDa0A9XSU2_g/preset:view/plain/0b67ca187e810d498fee54800b7544c7-2998497080314364057.jpg","https://cdn.chotot.com/pVkl5U91rX2pEanU8vBJw8jTfqPAncx0UjZmxsit_aw/preset:view/plain/1b0785fe302c9ce2e54f7dce35aba819-2998497080374582387.jpg"]}),

L(1524,"ho-chi-minh","tm","Дом",30000000,80,
  "Дом целиком, 4x20м (80м²), 3 этажа, 6 спален, кухня, 3 с/у, 7 кондиционеров. Tân Mỹ (старая P. Tân Phú, Q7), ~300м от рынка Tân Mỹ, удобно для проживания и бизнеса.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134237230.htm","5 дней назад",5,source="chotot",
  details={"contact":"Thanh Phan","photos":["https://cdn.chotot.com/m-Q-U97hW_juxoFUL9sFYnKvtQ3pXhu5LfK9A7tyZbw/preset:view/plain/3a4cebbd86c5652416f5f2d08b86ea49-2998310724968644761.jpg","https://cdn.chotot.com/PI2TJY7uazMXFgq-xxnBxQNHEjE6a8C-jiRCebv2ZgM/preset:view/plain/43777b6a7bcfb9eea7f5143bcb5f7b5f-2998310724665340817.jpg"]}),

L(1525,"ho-chi-minh","tm","Квартира",40000000,107,
  "3-спальная квартира (2 с/у), 107м², ЖК The Ascentia, ул. Nguyễn Lương Bằng, Tân Mỹ (Phú Mỹ Hưng) — полная меблировка (кондиционеры, кровати, холодильник, плита, ТВ), рядом больница, супермаркет, парк и школы Phú Mỹ Hưng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-the-ascentia-phu-my-hung/cho-3pn-2wc-tai-phuong-tan-tp-chi-minh-pr46221245","сегодня",0,source="batdongsan",
  details={"notice":"дата размещения оценена по диапазону ID объявления Batdongsan (самый свежий на момент проверки) — сайт не публикует исходную дату, это не гарантированно первая публикация. Цена 40 млн ₫ подтверждена дважды — в карточке выдачи и в тексте описания.","contact":"Zoom Land","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152920-ecc5_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152920-e4e0_wm.jpg"]}),

L(1526,"ho-chi-minh","tm","Квартира",30000000,75,
  "2-спальная квартира (2 с/у), 75м², ЖК The Aurora, ул. Nguyễn Lương Bằng, Tân Mỹ (Phú Mỹ Hưng) — новая полная меблировка, свободна, можно въезжать сразу. Цена договорная.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-the-aurora-phu-my-hung/2pn-tang-cao-u-noi-that-cho-gia-30-trieu-thuong-luong-pr46221219","сегодня",0,source="batdongsan",
  details={"notice":"дата размещения оценена по диапазону ID объявления Batdongsan (самый свежий на момент проверки) — сайт не публикует исходную дату. Цена 30 млн ₫ подтверждена дважды — в карточке выдачи и в тексте описания (указана как договорная).","contact":"Huỳnh Quyên","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152632-0010_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152632-8f85_wm.jpg"]}),

L(1527,"ho-chi-minh","tm","Квартира",23000000,49,
  "1-спальная квартира (1 с/у), 49м², ЖК The Aurora (Aurora), Tân Mỹ (Phú Mỹ Hưng) — полная меблировка, свободна, высокий этаж.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-the-aurora-phu-my-hung/1pn-u-noi-that-cho-gia-23-trieu-pr46221176","сегодня",0,source="batdongsan",
  details={"notice":"дата размещения оценена по диапазону ID объявления Batdongsan (самый свежий на момент проверки) — сайт не публикует исходную дату. Цена 23 млн ₫ подтверждена дважды — в карточке выдачи и в тексте описания.","contact":"Huỳnh Quyên","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152138-502c_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152139-6017_wm.jpg"]}),

L(1528,"ho-chi-minh","kh","Дом",15000000,37,
  "Дом целиком, 37м² (1 этаж + 2 этажа + терраса), 4 спальни (1 внизу), 3 с/у, двор на 10 мотобайков, кондиционеры во всех комнатах. Квартал 20 Thước, рядом Hoàng Diệu/Vĩnh Khánh, Khánh Hội (Q4) — ~300м до Q1 и юрфака ĐH Luật.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-20-thuoc-phuong-khanh-hoi-tp-ho-chi-minh/cho-nguyen-can-moi-khu-20-15tr-thang-pr46221305","сегодня",0,source="batdongsan",
  details={"notice":"дата размещения оценена по диапазону ID объявления Batdongsan (самый свежий на момент проверки) — сайт не публикует исходную дату. Цена 15 млн ₫ подтверждена дважды — в карточке выдачи и в тексте описания.","contact":"Tỉnh","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824153850-03a4_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824153851-41f1_wm.jpg"]}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content

new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
assert new_content != content
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", NEW_SRC.count("L("), "listings")
