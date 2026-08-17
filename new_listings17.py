# -*- coding: utf-8 -*-
# Ho Chi Minh City batch 2/4 — Batdongsan.com.vn, IDs 572-596.
# Wards per source's own breadcrumb tags. Estella Heights/Palm Heights are tagged "Bình Trưng mới" (btr),
# distinct from Lumière Riverside which is "An Khánh mới" (ak) — confirmed via OSM as two separate official wards.
# Thanh Đa is tagged "Bình Quới mới" (bq), not "Bình Thạnh". Many listings carry an expired listing-date flag
# (still shown live in search) — noted per-listing where the source flagged it.
NEW_SRC = r'''
L(572,"ho-chi-minh","tm","Квартира",19000000,48,
  "1-спальная квартира в The Ascentia, «самая низкая цена на рынке», вид на виллы, полная мебель.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-phuong-tan-phu-19-the-ascentia-phu-my-hung/gia-re-nhat-thi-truong-cho-1pn-gia-chi-19-trieu-lh-pr45752155","опубл. 18.05.26",90,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления уже прошла (25.05.26), карточка всё ещё в живом поиске — актуальность стоит уточнить.","contact":"Tiên Cara Pmh, 0909 854 ***"}),

L(573,"ho-chi-minh","tm","Квартира",27000000,80,
  "2-спальная квартира (2 с/у) в The Ascentia, полная мебель, окна на восток. Рядом Công viên Ánh Sao, Sakura Park, Winmart+.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-phuong-tan-phu-19-the-ascentia-phu-my-hung/cho-cc-2pn-2wc-80m2-tai-nha-ep-nhu-hinh-pr46165843","5 дней назад",5,source="batdongsan",
  details={"amenities":"242 квартиры в комплексе (1-3PN + дуплексы), бассейны, спортзал, йога, сауна, сад на крыше","contact":"Nhật Huy, 0989 920 ***"}),

L(574,"ho-chi-minh","tm","Квартира",35000000,107,
  "3-спальная квартира (2 с/у) в The Ascentia, вид на виллы (Chateau, Midtown), 10-15 мин до Q1/Q2/Q4. Полная премиум-мебель.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-phuong-tan-phu-19-the-ascentia-phu-my-hung/cho-ascentina-3pn-full-noi-that-view-biet-thu-lh-van-anh-pr43320826","вчера",1,source="batdongsan",
  details={"amenities":"рядом парк Sakura, школы SSIS/Canadian/Japanese","contact":"Văn Anh, 0849 160 ***"}),

L(575,"ho-chi-minh","tm","Квартира",55000000,112,
  "3-спальная квартира (2 с/у), премиум-сегмент, The Ascentia, рядом Crescent Mall и Hồ Bán Nguyệt. Полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-phuong-tan-phu-19-the-ascentia-phu-my-hung/cho-pmh-q7-3pn-2wc-full-noi-that-cao-cap-view-ep-gia-55-trieu-thang-pr46095736","опубл. 25.07.26",90,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления уже прошла (09.08.26), карточка всё ещё в живом поиске.","contact":"Từ Nguyễn, 0337 959 ***"}),

L(576,"ho-chi-minh","th","Квартира",22000000,87,
  "3-спальная квартира (2 с/у), ядро Phú Mỹ Hưng, рядом Crescent Mall, международные школы, финансовый квартал, SECC. Импортная мебель.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-tan-phong-9-phu-my-hung/cho-cao-cap-ngay-crescent-mall-87m2-3pn-2wc-noi-that-moi-tinh-o-ngay-pr46180136","2 дня назад",2,source="batdongsan",
  details={"contact":"агентство Green House (4 офиса в PMH)"}),

L(577,"ho-chi-minh","th","Квартира",30000000,98,
  "3-спальная квартира (2 с/у) у моста Cầu Ánh Sao, 5 мин до рынка Tân Mỹ, импортная премиум-мебель.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-tan-phong-9-phu-my-hung/cho-cao-cap-cau-anh-sao-98m2-3pn-2wc-noi-that-cao-cap-nhap-khau-o-ngay-pr46168150","5 дней назад",5,source="batdongsan",
  details={"contact":"Green House, Ngọc Hân, 0773 962 ***"}),

L(578,"ho-chi-minh","th","Квартира",23000000,110,
  "3-спальная квартира (2 с/у) на главной улице Nguyễn Đức Cảnh, рядом школа SSIS. Мебель полная или базовая на выбор.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-tan-phong-9-phu-my-hung/chuyen-cho-110m2-3-ngu-ke-ben-truong-ssis-lh-em-huong-pr46166277","5 дней назад",5,source="batdongsan",
  details={"contact":"Nguyễn Hường (специалист по аренде в PMH), 0919 949 ***"}),

L(579,"ho-chi-minh","tm","Квартира",12000000,88,
  "Belleza Apartment, 2-спальная угловая квартира (2 с/у), свежий ремонт, не хватает части бытовой техники.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-pham-huu-lau-phuong-phu-my-9-belleza-apartment/cho-q7-88m2-2pn-2wc-noi-that-gan-u-gia-12tr-10-8-o-uoc-pr46067134","5 дней назад",5,source="batdongsan",
  details={"deposit":"2 месяца","contact":"Nguyễn Thị Hưng"}),

L(580,"ho-chi-minh","tm","Квартира",11500000,70,
  "Q7 Boulevard, 2-спальная квартира (2 с/у), 15 мин до PMH/SC VivoCity/RMIT, 10 мин до Crescent Mall/Lotte Mart.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-phuong-phu-my-9-q7-boulevard/gio-hang-cho-chon-loc-re-ep-sach-se-view-ep-thoang-yen-tinh-pr45661907","11 дней назад",11,source="batdongsan",
  details={"notice":"агентство NewHouse (офис B1.OF.14 прямо в здании) предлагает помощь с ВНЖ/визой арендаторам","contact":"Chí Tiền, 0963 214 ***"}),

L(581,"ho-chi-minh","ak","Квартира",25000000,50,
  "1-спальная квартира (1 с/у), ул. Võ Trường Toản, Thảo Điền, полная мебель, торг возможен.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-truong-toan-phuong-thao-dien-q2-thao-dien/ien-cho-1pn-full-nt-gia-25-trieu-thang-con-thuong-luong-pr45991617","11 дней назад",11,source="batdongsan",
  details={"contact":"Phúc Nguyễn, 0903 933 ***"}),

L(582,"ho-chi-minh","ak","Квартира",33000000,72,
  "2-спальная квартира (2 с/у), башня T2, отдельный лифтовой холл на этаж (приватность), 100% новая мебель, инфинити-бассейн, спортзал на крыше, библиотека.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-truong-toan-phuong-thao-dien-q2-thao-dien/cho-2pn-full-nt-hiem-ien-loi-thang-may-rieng-yen-tinh-pr45876268","3 дня назад",3,source="batdongsan",
  details={"contact":"Nhất Thạch, 0932 641 ***"}),

L(583,"ho-chi-minh","ak","Квартира",45000000,112,
  "3-спальная квартира (2 с/у) в ЖК Fraser, вид на реку, от собственника напрямую.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-truong-toan-phuong-thao-dien-q2-thao-dien/cho-3pn-ien-full-noi-that-view-song-chi-45-trieu-pr46064002","опубл. 18.07.26",30,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления — 17.08.26 (истекает буквально на днях от момента проверки)","contact":"собственник Nguyễn Thành Định, 0708 248 ***"}),

L(584,"ho-chi-minh","ak","Квартира",140000000,182,
  "Люкс-сегмент: 4-спальная квартира (3 с/у), 32-этажная башня застройщика Frasers Centrepoint (Сингапур), 300 квартир + 100+ сервисных апартаментов, вид на реку.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-truong-toan-phuong-thao-dien-q2-thao-dien/duy-nhat-4pn-3wc-182m2-140tr-thang-bao-khong-noi-that-tang-cao-view-song-xem-nha-24-7-pr46175001","3 дня назад",3,source="batdongsan",
  details={"notice":"без мебели («bao không nội thất»), топ-сегмент цен для ориентира","amenities":"рядом парки Thảo Điền/An Phú, госпиталь AIH, международные школы","contact":"Lê Thanh Tuấn, 0931 219 ***"}),

L(585,"ho-chi-minh","ak","Квартира",16000000,55,
  "Masteri Thảo Điền, самая большая 1-спальная планировка в комплексе, вид на Landmark 81, смарт-ТВ, полная кухонная техника.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-xa-lo-ha-noi-phuong-thao-dien-masteri-thao-dien/cho-1pn-re-nhat-co-ban-cong-pr39203415","6 дней назад",6,source="batdongsan",
  details={"amenities":"бесплатно бассейн/зал/BBQ/парк, рядом Vincom Mega Mall","contact":"Hoàng Phong"}),

L(586,"ho-chi-minh","ak","Квартира",18000000,70,
  "Masteri Thảo Điền, 2-спальная квартира (2 с/у), полная мебель, у того же агента широкий выбор планировок 1-4PN.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-xa-lo-ha-noi-phuong-thao-dien-masteri-thao-dien/gia-cuc-tot-cho-2-phong-ngu-tai-ien-chi-tu-18-trieu-pr46079479","опубл. 22.07.26",25,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа — 21.08.26 (через несколько дней от момента проверки)","contact":"Dư Huyền, 0943 707 ***"}),

L(587,"ho-chi-minh","btr","Квартира",26000000,89,
  "Estella Heights, 2-спальная квартира (2 с/у), ул. Song Hành. У агента полный прайс-лист здания (1PN от 22 до 4PN за 90-128 млн). Управление — Savills.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-song-hanh-phuong-an-phu-estella-heights/toan-bo-cho-thang-01-2026-chinh-chu-khong-gia-ao-lh-pr44943253","5 дней назад",5,source="batdongsan",
  details={"notice":"формально это Phường Bình Trưng (соседняя с An Khánh/Thảo Điền), не путать с историческим центром Thảo Điền","fees":"обслуживание 23 500 ₫/м²/мес, паркинг авто 1 080 000 ₫/мес, мотобайк 162 000 ₫/мес","amenities":"pet-friendly, помощь с временной регистрацией и налогами","contact":"Phan Thanh Trí Tâm, +8490 987 8***"}),

L(588,"ho-chi-minh","btr","Квартира",16000000,80,
  "Palm Heights, 2-спальная квартира (2 с/у), застройщик Keppel Land + Tiến Phước/Trần Thái, 3 башни по 34 этажа, 816 квартир вдоль рек. 8 км до Q1.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-song-hanh-phuong-an-phu-palm-heights/xanh-tai-cao-cap-cho-ngay-hom-nay-pr43626987","2 дня назад",2,source="batdongsan",
  details={"notice":"формально это Phường Bình Trưng, не An Khánh","amenities":"рядом Vincom Mega Mall/Estella Place","contact":"Ngô Hoàng Hiệp (говорит по-английски), 0375 786 ***"}),

L(589,"ho-chi-minh","ak","Квартира",35000000,77,
  "Lumière Riverside, 2-спальная квартира (2 с/у), вид на реку Сайгон, высокий этаж, широкий балкон.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-nguyen-giap-phuong-an-phu-lumiere-riverside/2pn-gia-35-trieu-thang-view-song-full-noi-that-cao-cap-pr46059606","вчера",1,source="batdongsan",
  details={"notice":"офис агента прямо на территории ЖК; у агента полный прайс здания (1PN от 25 млн, 3PN от 50 млн)","contact":"Yến Lumiere, 0986 581 ***"}),

L(590,"ho-chi-minh","bq","Квартира",3000000,30,
  "1-спальная квартира (1 с/у) в кооперативном доме («cư xá»), этаж 1, блок 10 (132B lô10), отдельные счётчики по гостарифу, рядом рынок и набережная. От собственника напрямую.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-cu-xa-thanh-da-phuong-27-66/cho-lau-1-lo-10-a-27-quan-binh-3tr-thang-pr45428887","опубл. 30.03.26",140,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления — 14.04.26 (почти 4,5 месяца назад), актуальность под вопросом.","contact":"собственник Nguyen Phong Vinh, 0985 345 ***"}),

L(591,"ho-chi-minh","bq","Комната",4500000,24,
  "1-спальная комната, этаж 4, блок S, прямо у реки, вид на Thảo Điền и Landmark 81 (видны салюты по праздникам). Без мебели, торг уместен.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-cu-xa-thanh-da-phuong-27-66/cho-a-1-2-phong-ngu-pr45636505","опубл. 27.04.26",111,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (07.05.26)","contact":"владелица Cô Liên"}),

L(592,"ho-chi-minh","bq","Квартира",21000000,120,
  "Thanh Đa View, 3-спальная квартира (2 с/у), рядом мост Thanh Đa и рынок, бассейн, спортзал, магазин у дома, вид на реку Сайгон.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-thanh-da-phuong-27-thanh-da-view/cho-3pn-a-so-7-a-p-27-quan-binh-dien-pr46066498","опубл. 04.08.26",13,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления — 14.08.26 (пару дней назад)","contact":"Nguyễn Tấn Huy, 0937 833 ***"}),

L(593,"ho-chi-minh","bq","Квартира",12000000,81,
  "2-спальная квартира (2 с/у), цокольный этаж, полностью отремонтирована (плитка, шторы, встроенная кухня, индукционная плита), рядом администрация/банки/рынок Thanh Đa. Без посредника.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-thanh-da-phuong-27-66/nha-cho-nc-tang-tret-cc-cxt-uong-t-bq-p-27-quan-bt-tp-hcm-pr45823390","опубл. 29.05.26",80,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (13.06.26). «Miễn trung gian» — от собственника напрямую.","contact":"владелец Gia Thái, 0938 738 ***"}),

L(594,"ho-chi-minh","bq","Комната",4200000,40,
  "Отдельная комната-лофт на 2-4 человек, кондиционер, шкаф, своя зона стирки/сушки, охрана 24/7, рядом университет Hutech — больше подходит студентам, чем удалёнщикам.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-thanh-da-phuong-27-66/khai-truong-gac-cao-ung-uoc-ay-u-noi-that-o-2-4-nguoi-gan-hutech-khu-u-gtvt-ngoai-thuong-pr46069905","опубл. 20.07.26",28,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления — 04.08.26","contact":"агент Quỳnh Hương Uni"}),

L(595,"ho-chi-minh","bq","Студия",3700000,30,
  "Студия с базовой мебелью, балкон на восток, 2 км до супермаркетов и парка Tầm Vu.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-thanh-da-phuong-27-khu-do-thi-moi-binh-quoi-thanh-da/cho-tai-o-a-3-7-trieu-30-m2-pr45866853","опубл. 06.06.26",72,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (21.06.26)","contact":"владелец Đỗ Đan Việt, 0559 567 ***"}),

L(596,"ho-chi-minh","bq","Комната",3500000,32,
  "1-спальная комната (1 с/у), точный адрес 1/50/13 đường Thanh Đa. Аренда от 1 года, рядом мед. центр, парки Thanh Đa и Tầm Vu, международная школа Wisdomland, супермаркеты.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-thanh-da-phuong-27-66/cho-1pn-1wc-32m2-3-5-trieu-tai-1-50-13-a-p-27-q-binh-hcm-pr45543757","опубл. 13.04.26",126,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (28.04.26)","contact":"владелец Trần Minh Thắng, 0933 148 ***"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted HCMC batdongsan listings")
