# -*- coding: utf-8 -*-
NEW_SRC = r'''
L(296,"nha-trang","vp","Квартира",6000000,52,
  "Квартира с видом, ул. 2/4, этаж 2, комната D2.2, район Vĩnh Phước.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-2-4-phuong-vinh-phuoc-350/cho-2-4-gia-4-trieu-52-m2-2-pn-view-dep-pr41413787",
  "актуально",0,source="batdongsan",
  details={"amenities":"кухня видна на фото (гарнитур, мойка), 2 спальни, 1 санузел","notice":"брокер Lê Tài, 11 лет на площадке, 101 активное объявление"}),

L(297,"nha-trang","ps","Квартира",6000000,51,
  "CT6 Vĩnh Điềm Trung, базовая (не полная) мебель, район X. Vĩnh Hiệp.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-xa-vinh-hiep-1-khu-do-thi-vinh-diem-trung/cho-ct6-iem-tay-nha-trang-51m2-2pn-6tr-thang-noi-that-co-ban-pr46183236",
  "актуально",0,source="batdongsan",
  details={"amenities":"2 спальни, 2 санузла","notice":"меблировка базовая (nội thất cơ bản), не полная — уточняйте состав"}),

L(298,"nha-trang","pl","Квартира",7000000,67,
  "Chung cư XH1 VCN Phước Long.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-28-phuong-phuoc-long-khu-do-thi-vcn-phuoc-long-2/cho-xh1-nha-trang-7-trieu-thang-pr46183238",
  "актуально",0,source="batdongsan",
  details={"amenities":"2 спальни, 1 санузел","notice":"комплекс XH1 VCN Phước Long"}),

L(299,"nha-trang","tl","Квартира",6000000,None,
  "Căn hộ 2 phòng ngủ trung tâm Nha Trang — Nguyễn Thiện Thuật, тайng 6.",
  "https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u",
  "26 июня",30,source="facebook",
  details={"amenities":"2 спальни, 1 санузел, гостиная с ТВ, обеденный стол","notice":"автор Dương Yến. Прямой ссылки на пост нет — ссылка открывает поиск «6 triệu» в группе, пост среди первых результатов"}),

L(300,"nha-trang","vh","Квартира",6000000,None,
  "Chung cư Hoàng Quân — căn trống (пустая квартира без мебели).",
  "https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u",
  "16 часов назад",0,source="facebook",
  details={"amenities":"2 спальни, 2 санузла","policy":"без мебели и техники","notice":"автор Bích Lê, заселение 20 сентября. Ссылка открывает поиск «6 triệu» в группе"}),

L(301,"nha-trang","pl","Квартира",6500000,None,
  "Căn hộ 1PN khu vực Phước Long.",
  "https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u",
  "актуально",0,source="facebook",
  details={"amenities":"1 спальня, кухня и кондиционер видны на фото","notice":"автор Hồng Liên, контакт +84 819 070 270 (WhatsApp/Zalo). Ссылка открывает поиск «6 triệu» в группе"}),

L(302,"nha-trang","vp","Квартира",6000000,None,
  "Căn hộ 1 phòng ngủ — Lê Văn Huân, Phía Bắc Nha Trang.",
  "https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u",
  "актуально",0,source="facebook",
  details={"amenities":"1 спальня","notice":"автор Nguyễn Thị Mỹ Hiệp. Ссылка открывает поиск «6 triệu» в группе"}),

L(303,"nha-trang","ps","Квартира",6500000,None,
  "Chung cư CT5 Vĩnh Điềm Trung, полная мебель по фото.",
  "https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u",
  "актуально",0,source="facebook",
  details={"amenities":"гостиная с диваном, обеденная зона, кухонный уголок","notice":"автор Kim Qui, свободна с 22 июня. Ссылка открывает поиск «6 triệu» в группе"}),

L(304,"nha-trang","lt","Квартира",6000000,None,
  "Căn hộ new — полностью новая мебель и техника, современный ремонт.",
  "https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u",
  "актуально",0,source="facebook",
  details={"amenities":"кухня со встроенной техникой (варочная панель, духовка) видна на фото","notice":"автор Thuý Quỳnh. Ссылка открывает поиск «6 triệu» в группе"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted 9 listings")
