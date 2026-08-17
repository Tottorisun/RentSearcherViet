# -*- coding: utf-8 -*-
# Ho Chi Minh City refresh round 2 — batch 4/5: Airbnb/Booking.com/Trip.com for the 2 new districts
# (42 listings), IDs 708-749. All prices are real quoted 30-night totals (Booking/Trip: Sep1-Oct1 2026
# window; Airbnb: live monthly-discount total for its own nearby date window, noted per listing).
# Several D1 addresses are technically in neighboring old-Quận-1 wards (Đa Kao, Cầu Ông Lãnh, Phạm Ngũ
# Lão, Tân Định) rather than Bến Thành itself — we don't have separate boundary data for those yet,
# so they're placed on Bến Thành with the real sub-area named in the description.
NEW_SRC = r'''
L(708,"ho-chi-minh","bth","Квартира",27966263,20,
  "Mersey Central Saigon Apart'Hotel, студия/1-спальная, ул. Yersin, Q1.",
  "https://www.booking.com/hotel/vn/mersey-central-saigon.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей (1-30 сент. 2026)."}),

L(709,"ho-chi-minh","bth","Студия",24161253,40,
  "Nicecy Hotel & Apartment, студия, ул. Trần Hưng Đạo, Phường Bến Thành.",
  "https://www.booking.com/hotel/vn/nicecy-amp-apartment-ho-chi-minh.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка от базовой цены 61,9 млн ₫."}),

L(710,"ho-chi-minh","bth","Квартира",27744000,27,
  "INDO Serviced Apartment, 1-спальная, ул. Thái Văn Lung, Q1.",
  "https://www.booking.com/hotel/vn/indo-serviced-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(711,"ho-chi-minh","bth","Студия",30492000,29,
  "International Residence (CityNest Saigon), студия с балконом, ул. Phạm Ngũ Lão, Q1.",
  "https://www.booking.com/hotel/vn/citynest-saigon-residence.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка от базовой цены 50,8 млн ₫."}),

L(712,"ho-chi-minh","bth","Квартира",44625000,40,
  "Journey Central – SOHO Residence, 1-спальная, ул. Cô Giang, Q1.",
  "https://www.booking.com/hotel/vn/the-lumiere-saigon-central.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей (со скидкой)."}),

L(713,"ho-chi-minh","bth","Квартира",65484000,60,
  "Yu Stay Apartment, Soho D1, 2-спальная, 100 Cô Giang, Q1.",
  "https://www.booking.com/hotel/vn/yu-stay.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(714,"ho-chi-minh","bth","Студия",79916099,35,
  "Soho Residences D1 (Veluxe Stay), студия, 100 Cô Giang, Q1.",
  "https://www.booking.com/hotel/vn/instaworthy-2br-central-prime-spot-wcity-views.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей — цена высокая для студии, возможно премиум-этаж/вид."}),

L(715,"ho-chi-minh","bth","Студия",37270800,35,
  "Aris Soho Balcony Suites, студия с балконом, 100 Cô Giang, Q1.",
  "https://www.booking.com/hotel/vn/anthesis-riverside-apartment-masteri-millennium.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(716,"ho-chi-minh","bth","Студия",30213000,36,
  "Chilli & Chum Apartment, студия, ул. Hồ Hảo Hớn, Q1.",
  "https://www.booking.com/hotel/vn/chilli-and-chum-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(717,"ho-chi-minh","bth","Квартира",19002454,30,
  "Wabi Sabi Saigon Hideout, вся квартира, 1 спальня, ул. Cô Giang, Q1.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=120250970","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(718,"ho-chi-minh","bth","Комната",17986066,None,
  "Peanuts Home Lê Lai, номер, ул. Lê Lai, Phường Bến Thành.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=132689258","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(719,"ho-chi-minh","bth","Студия",16872600,None,
  "Hearth and Home De Thám, делюкс-студия, ул. Đề Thám, район Cầu Ông Lãnh (соседний со старым Q1).",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=130052850","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей. Формально Phường Cầu Ông Lãnh, а не Bến Thành — отдельных границ пока нет."}),

L(720,"ho-chi-minh","bth","Комната",24891294,None,
  "Mari Queen Hotel, номер (double), ул. Bùi Thị Xuân, район Phạm Ngũ Lão.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=63988006","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей, завтрак включён."}),

L(721,"ho-chi-minh","bth","Комната",37070324,None,
  "A25 Premium Hotel, номер superior с завтраком, ул. Lê Anh Xuân, Phường Bến Thành.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=703836","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(722,"ho-chi-minh","bth","Дом",71033126,None,
  "Таунхаус 3 спальни/3,5 с/у с террасой и BBQ на крыше, центр Q1.",
  "https://www.airbnb.com/rooms/1747239434091228240","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (22 авг - 19 сент), скидка от 88,3 млн ₫."}),

L(723,"ho-chi-minh","bth","Квартира",20563986,None,
  "Студия Nomah, рядом с розовой церковью Тân Định.",
  "https://www.airbnb.com/rooms/1745711185555765792","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (24 авг - 21 сент), скидка от 26,5 млн ₫. Формально Phường Tân Định, соседний со старым Q1."}),

L(724,"ho-chi-minh","bth","Студия",29978283,45,
  "Студия рядом с рынком Bến Thành.",
  "https://www.airbnb.com/rooms/1729749566721861030","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (18 ноя - 16 дек), скидка от 36,4 млн ₫."}),

L(725,"ho-chi-minh","bth","Дом",81618003,None,
  "Ambré Suites, 3 спальни/4 кровати/2 с/у, 5 мин до Bùi Viện.",
  "https://www.airbnb.com/rooms/1743932104867038611","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 99 млн ₫."}),

L(726,"ho-chi-minh","bth","Дом",44668179,None,
  "Дом 2 спальни/3 с/у, пешком до ул. Nguyễn Huệ.",
  "https://www.airbnb.com/rooms/1740629101657606884","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (14 сент - 12 окт), скидка от 51,2 млн ₫."}),

L(727,"ho-chi-minh","bth","Студия",11013207,None,
  "Тихая студия в переулке, Q1 — самый бюджетный вариант в подборке по D1.",
  "https://www.airbnb.com/rooms/1714347796029268086","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 15,2 млн ₫."}),

L(728,"ho-chi-minh","bth","Дом",149851979,None,
  "Люксовый дуплекс 3 спальни/6 кроватей/2 с/у, бассейн и спортзал, Q1.",
  "https://www.airbnb.com/rooms/1744123735364525509","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 173,2 млн ₫ — топ-сегмент цен для ориентира."}),

L(729,"ho-chi-minh","kh","Студия",23680800,30,
  "S Lux Apartment, студия, ул. Nguyễn Trường Tộ, Q4.",
  "https://www.booking.com/hotel/vn/s-lux-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(730,"ho-chi-minh","kh","Студия",27816000,28,
  "Key & Code Serviced Apartments, студия, ЖК Rivergate Residence.",
  "https://www.booking.com/hotel/vn/key-amp-code-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(731,"ho-chi-minh","kh","Студия",23259428,28,
  "Refined Saigon, студия в ЖК River Gate, 155 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/saigon-memories-free-city-walk-experience-amazing-infinity-pool-amp-free-4g-sim.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(732,"ho-chi-minh","kh","Студия",34800000,40,
  "A&L Service Apartment, студия в ЖК Rivergate Residence, 154 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/a-amp-l-service-apartment-by-me-in-rivergate-building.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(733,"ho-chi-minh","kh","Квартира",34929312,35,
  "Smile Home, 1-спальная в ЖК Tresor, 39 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/tresor-cozy-and-spacious-studio-bitexco-view.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(734,"ho-chi-minh","kh","Квартира",52992000,80,
  "Lovely Apartment, 2-спальная в ЖК Goldview, ул. Khánh Hội.",
  "https://www.booking.com/hotel/vn/lovely-apartment-goldview-ben-van-don.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(735,"ho-chi-minh","kh","Квартира",24000000,55,
  "Loft Bedroom Apartment, 1-спальная, 34-35 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/loft-bedroom-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(736,"ho-chi-minh","kh","Студия",83303712,35,
  "Tresor Apartments D4 (Veluxe Stay), студия, 39 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/la-vela-homes-premium-studios-2-amp-3-br-apartments-tresor-apartments-d4-5mins-t.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей — цена высокая для студии, возможно верхний этаж/премиум."}),

L(737,"ho-chi-minh","kh","Студия",37320750,37,
  "Saigon Royal Apartment, студия, 34-35 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/saigon-royal-apartment-ho-chi-minh.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(738,"ho-chi-minh","kh","Студия",28898440,None,
  "Rivergate Central, студия-сюит с кухней и видом на город, 151 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=23519757","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(739,"ho-chi-minh","kh","Студия",27958306,None,
  "MIN' Apartment, стандартная студия в ЖК Rivergate Residence, 151 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=113290340","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(740,"ho-chi-minh","kh","Студия",26070630,28,
  "RiverGate Saigon, студия/1-спальная, 151-155 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=134812647","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(741,"ho-chi-minh","kh","Квартира",32072906,30,
  "GobyHome, 1-спальная в ЖК Rivergate Residence, 151-155 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=135371761","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(742,"ho-chi-minh","kh","Студия",32294450,None,
  "Chau Apartments, студия, 155 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=25208785","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(743,"ho-chi-minh","kh","Квартира",26087888,None,
  "Студия в ЖК Tresor, центральное расположение.",
  "https://www.airbnb.com/rooms/894482406449428240","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 28,3 млн ₫."}),

L(744,"ho-chi-minh","kh","Квартира",33289874,None,
  "Уютная 1-спальная квартира в ЖК Tresor.",
  "https://www.airbnb.com/rooms/1728983336700006983","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (10 сент - 8 окт), скидка от 40,4 млн ₫."}),

L(745,"ho-chi-minh","kh","Квартира",40387920,50,
  "1-спальная квартира в ЖК Tresor, 50 м².",
  "https://www.airbnb.com/rooms/1743356139409084608","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (10 сент - 8 окт), скидка от 52,1 млн ₫."}),

L(746,"ho-chi-minh","kh","Квартира",19306712,None,
  "1-спальная квартира в Saigon Royal, самый доступный вариант в подборке по D4.",
  "https://www.airbnb.com/rooms/1700801896456964053","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 24,9 млн ₫."}),

L(747,"ho-chi-minh","kh","Квартира",31371425,None,
  "The Burgundy House, 1-спальная квартира, Quận 4.",
  "https://www.airbnb.com/rooms/1496811395593577343","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (20 окт - 17 ноя)."}),

L(748,"ho-chi-minh","kh","Квартира",43012450,None,
  "2-спальная квартира в ЖК Tresor, вид на город.",
  "https://www.airbnb.com/rooms/1739773704635725660","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 55,4 млн ₫."}),

L(749,"ho-chi-minh","kh","Квартира",47698352,None,
  "2-спальная квартира (2 с/у) в ЖК Tresor, 5 мин до рынка Bến Thành.",
  "https://www.airbnb.com/rooms/1728145041120427061","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (8 сент - 6 окт), скидка от 58,5 млн ₫."}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted round-2 batch 4 (airbnb/booking/trip for D1+D4)")
