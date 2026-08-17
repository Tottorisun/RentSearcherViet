# -*- coding: utf-8 -*-
# Ho Chi Minh City refresh round 2 — batch 1/5: Facebook groups (1) + Batdongsan (17), IDs 654-671.
# New wards this round: bth (Phường Bến Thành, old Quận 1 downtown), kh (Phường Khánh Hội, old Quận 4).
# Duplicates against the first HCMC round (same exact URL) were dropped by the researching agents
# themselves or excluded during integration — every ID below is a genuinely new listing.
NEW_SRC = r'''
L(654,"ho-chi-minh","ak","Квартира",25800000,None,
  "Masteri Thảo Điền, 2-спальная квартира (2 с/у), полная мебель, вид на реку, бассейн/зал/BBQ/охрана 24/7.",
  "https://www.facebook.com/groups/masterithaodien.hcmc/posts/2042173693083446/","проверено 17 авг",0,source="facebook",
  details={"contact":"Noodle Chan, 0902836054"}),

L(655,"ho-chi-minh","bth","Комната",8000000,25,
  "Студия с балконом, ул. Nguyễn Thái Bình, Bến Thành. Старое здание пешком, полная мебель, камеры/пожарная сигнализация.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-thai-binh-phuong-ben-thanh-53/studio-25m2-balcony-decor-cuc-xinh-thoang-mat-tien-hay-ham-nghi-q1-pr45996596","7 дней назад",7,source="batdongsan",
  details={"deposit":"2 месяца, оплата за период вперёд, договор на 1 год (депозит можно обсудить)","fees":"вода 21 500 ₫/м³, лифт 30 000 ₫/чел, мусор 105 000 ₫/мес, паркинг от 150 000 ₫","notice":"разрешён небольшой бизнес (салон/ногтевая студия), Airbnb не разрешён","contact":"агент Nguyễn Nhất Hoàng HiFriendz (171 активное объявление — крупный брокер)"}),

L(656,"ho-chi-minh","bth","Квартира",27000000,100,
  "2-спальная квартира (1 с/у), 5 мин до рынка Bến Thành и делового квартала, этаж 4 без лифта, ул. Lý Tự Trọng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ly-tu-trong-phuong-ben-thanh-53/cho-mat-tien-trung-tam-q1-30tr-thang-vi-tri-sam-uat-thuan-tien-di-chuyen-pr44602783","11 дней назад",11,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (16.08.26, вчера) — сайт сам помечает «возможно ещё актуально».","contact":"агент NHƯ NGỌC BCONS"}),

L(657,"ho-chi-minh","bth","Квартира",9000000,32,
  "Дуплекс, 1 спальня/1 с/у, ул. Nguyễn Thái Bình, Bến Thành. Можно жить самому или сдавать под Airbnb.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-thai-binh-phuong-ben-thanh-53/cho-45-47-quan-1-pr46120468","17 дней назад",17,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (15.08.26, 2 дня назад).","contact":"Duy Khang Nguyễn (похоже на частное лицо, 3 объявления)"}),

L(658,"ho-chi-minh","bth","Квартира",14000000,110,
  "5-спальная квартира (3 с/у) в старом здании прямо у рынка Bến Thành, ул. Nguyễn Công Trứ, этаж 2, можно перепланировать под бизнес.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-cong-tru-phuong-ben-thanh-53/110m2-5pn-3wc-kinh-doanh-tu-do-phu-hop-shop-o-kho-hang-online-ngay-cho-q1-pr46091668","24 дня назад",24,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (08.08.26, 9 дней назад). Объект верифицирован сайтом (Tin xác thực).","contact":"агент Nguyễn Nhất Hoàng HiFriendz"}),

L(659,"ho-chi-minh","bth","Квартира",8000000,52,
  "2-спальная квартира (1 с/у), этаж 3, балкон с видом на Q1/Q4, ул. Võ Văn Kiệt, рядом мост Ông Lãnh.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-van-kiet-phuong-ben-thanh-53/cho-194-q1-2pn-8tr-pr46031934","27 дней назад",27,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (05.08.26, 12 дней назад).","contact":"Nguyendangphuong (14 объявлений)"}),

L(660,"ho-chi-minh","kh","Студия",13000000,38,
  "Студия в Masteri Millennium, полная премиум-мебель, балкон, ориентация северо-запад. 132 Bến Vân Đồn.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-phuong-6-masteri-millennium/studio-full-noi-that-o-lien-lh-pr43746813","12 дней назад",12,source="batdongsan",
  details={"contact":"Phạm Minh Quân"}),

L(661,"ho-chi-minh","kh","Квартира",25000000,74,
  "Угловая 2-спальная квартира (2 с/у) в Masteri Millennium, вид на реку и башню Bitexco, бассейн/спортзал/охрана 24/7, 3 мин до Q1. 132 Bến Vân Đồn.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-phuong-6-masteri-millennium/goc-view-song-bitexco-cuc-ep-2pn-tang-cao-vao-o-ngay-pr45668681","5 дней назад",5,source="batdongsan",
  details={"notice":"верифицировано сайтом 13.08.26","contact":"Hồng Ngô Việt"}),

L(662,"ho-chi-minh","kh","Квартира",28000000,103,
  "3-спальная квартира (2 с/у) в Masteri Millennium, вид на город, бассейн-инфинити, спортзал, BBQ, терраса, рецепция, рядом Q1/Bitexco/Ba Son. 132 Bến Vân Đồn.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-phuong-6-masteri-millennium/gia-tot-nhat-3pn-103m-view-thanh-pho-full-noi-that-chi-28-trieu-lh-pr46193082","опубликовано сегодня",0,source="batdongsan",
  details={"contact":"агент Đặng Đình Thịnh (435 активных объявлений — крупное агентство)"}),

L(663,"ho-chi-minh","kh","Дом",8500000,27,
  "Отдельный дом целиком, 2 спальни/2 с/у, свежий ремонт, световой колодец, свет/вода по гостарифу, без платы за паркинг/управление. От собственника напрямую («chính chủ»). Переулок 1, ул. Tôn Đản.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ton-dan-phuong-15-56/quan-4-chinh-chu-cho-moi-nguyen-can-hem-1-an-2pn-2wc-pr45398771","2 дня назад",2,source="batdongsan",
  details={"contact":"собственница «Trâm»"}),

L(664,"ho-chi-minh","kh","Дом",14000000,48,
  "Дом в переулке (3×16м), 2 спальни/1 с/у, первый этаж + антресоль, 2 кондиционера, рядом мост Ông Lãnh. Ул. Bến Vân Đồn.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ben-van-don-phuong-phuong-9-2-56/cho-hem-3-5m-xh-on-p-9-q-4-14tr-pr46175440","4 дня назад",4,source="batdongsan",
  details={"contact":"агентство Nhà Đất Minh Đức (575 объявлений, 13 лет на рынке)"}),

L(665,"ho-chi-minh","kh","Дом",11000000,18,
  "Дом целиком (фасад 6м, 3 этажа), 3 спальни/3 с/у, 2 кондиционера, 3 камеры, напротив пагоды Giác Nguyên. Ул. Số 41.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-so-41-phuong-6-56/cho-nguyen-can-dai-han-uong-41-khanh-hoi-tp-hcm-oi-dien-chua-giac-nguyen-pr46165994","6 дней назад",6,source="batdongsan",
  details={"contact":"«Tan» (похоже на частное лицо)"}),

L(666,"ho-chi-minh","th","Квартира",26000000,80,
  "Угловая 2-спальная квартира (2 с/у) в Urban Hill, Phú Mỹ Hưng, новый ремонт, рядом VivoCity/Crescent Mall/международная школа Nam Sài Gòn. Ул. Nguyễn Văn Linh.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-van-linh-phuong-tan-phong-9-urban-hill/cho-80m2-26-trieu-vnd-2pn-2wc-full-noi-that-cao-cap-moi-99-lh-pr45693876","проверено 17 авг",0,source="batdongsan",
  details={"contact":"Mr. Đức Huy"}),

L(667,"ho-chi-minh","ak","Квартира",23000000,54,
  "1-спальная квартира (1 с/у, площадь по стенам 54 м² / по факту 46,8 м²) в Masteri An Phú, вид на реку. Ул. Xa Lộ Hà Nội.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-xa-lo-ha-noi-phuong-thao-dien-masteri-an-phu/cho-1pn-23tr-net-chuyen-gio-hang-gia-tot-cam-ket-uy-tin-bao-gia-that-pr46179485","3 дня назад",3,source="batdongsan",
  details={"notice":"цена указана как net (чистыми), верифицировано сайтом 14.08.26","contact":"агент Tuấn Sang Masteri (28 объявлений)"}),

L(668,"ho-chi-minh","ak","Квартира",40000000,88,
  "Угловая 2-спальная квартира (2 с/у) в Thảo Điền Green, вид на реку и Landmark 81, бассейн-инфинити, минимум год аренды. Ул. Nguyễn Văn Hưởng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-van-huong-phuong-thao-dien-thao-dien-green/goc-2pn-2wc-88m2-50tr-thang-tai-ien-om-tron-view-song-view-landmark81-xem-de-pr46074041","1 день назад",1,source="batdongsan",
  details={"contact":"агент Lê Thanh Tuấn (116 объявлений)"}),

L(669,"ho-chi-minh","ak","Квартира",20000000,70,
  "2-спальная квартира (2 с/у) в Masteri An Phú, полная мебель, свободна, можно смотреть в любое время. Ул. Xa Lộ Hà Nội.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-xa-lo-ha-noi-phuong-thao-dien-masteri-an-phu/for-rent-2-bedrooms-20-000-000-vnd-month-pr45195500","опубликовано сегодня",0,source="batdongsan",
  details={"contact":"агент Serena Juan (26 объявлений)"}),

L(670,"ho-chi-minh","bq","Студия",8500000,40,
  "Новая студия, замок по отпечатку пальца, камеры 24/7, без общего хозяина, рядом университет HUTECH. Ул. Thanh Đa.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-thanh-da-phuong-27-66/moi-khai-truong-studio-1-phong-ngu-full-noi-that-gan-ai-hoc-hutech-pr46177370","4 дня назад",4,source="batdongsan",
  details={"notice":"верифицировано сайтом 13.08.26","contact":"агент «Toàn Căn Hộ Đẹp»"}),

L(671,"ho-chi-minh","bq","Квартира",10000000,50,
  "1-спальная мини-квартира рядом с мостом Cầu Kinh, лифт, большой подземный паркинг, есть зарядка для электровелосипедов. Ул. Thanh Đa.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-thanh-da-phuong-27-66/1pn-ngay-cau-kinh-a-thang-may-ham-xe-lon-co-nhan-xe-ien-pr46146130","11 дней назад",11,source="batdongsan",
  details={"notice":"верифицировано сайтом 06.08.26","contact":"агент Thanh Duy - Uni Living (49 объявлений)"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted round-2 batch 1 (fb groups + batdongsan)")
