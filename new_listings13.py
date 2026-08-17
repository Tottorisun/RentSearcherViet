# -*- coding: utf-8 -*-
# Booking.com Extended Stays integration (source="booking"), IDs 506-519. 30-night stay.
NEW_SRC = r'''
L(506,"nha-trang","vt","Квартира",19960000,70,
  "2-спальная квартира Napoleon Seaview Apartments, ул. Nguyễn Đình Chiểu, ~3,5 км до центра, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/ubuntu-napoleon-nha-trang-apartment.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей (скидка за длительное проживание уже применена)","notice":"рейтинг 7.5 «Хорошо» (160 отзывов)","amenities":"кухня, собственная ванная с биде, ТВ, холодильник, плита, балкон с видом на город, общая гостиная","policy":"бесплатная отмена"}),

L(507,"nha-trang","lt","Квартира",31370000,52,
  "1-спальная квартира Cozy GoldCoast Apartment, ул. Trần Hưng Đạo, район Lộc Thọ, 500 м до пляжа Nha Trang.",
  "https://www.booking.com/hotel/vn/cozy-gold-coast-nha-trang.ru.html","проверено 15 авг",1,source="booking",
  details={"deposit":"1 000 000 ₫ наличными при заселении (возвратный)","contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 8.9 «Хорошо» (27 отзывов). Оплата и депозит — только наличными.","amenities":"бар, вид на море, кухня с микроволновкой, прокат велосипедов, открытый бассейн","policy":"дешёвый тариф без возврата; более дорогие тарифы — с бесплатной отменой; животные не допускаются"}),

L(508,"nha-trang","lt","Квартира",42340000,35,
  "1-спальная квартира в комплексе Grands StarCity, 0,6 км до центра, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/grands-starcity.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.1 «Превосходно» (85 отзывов)","policy":"бесплатная отмена"}),

L(509,"nha-trang","lt","Квартира",15450000,30,
  "1-спальная квартира Laholm Hotel, 0,6 км до центра, на первой линии пляжа — самый бюджетный вариант подборки Booking.com.",
  "https://www.booking.com/hotel/vn/laholm-nha-trang.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 7.1 «Хорошо» (41 отзыв)","policy":"бесплатная отмена"}),

L(510,"nha-trang","vn","Квартира",26360000,68,
  "2-спальная квартира Sweet Homestay Sea View, ~4,1 км до центра, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/sweet-homestay-nha-trang.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 7.3 «Хорошо» (148 отзывов)","policy":"бесплатная отмена"}),

L(511,"da-lat","xh","Квартира",11240000,40,
  "1-спальная квартира CozyNook Boutique Apartments, ул. 3 tháng 2, 250 м до центра.",
  "https://www.booking.com/hotel/vn/cozynook-3-boutique-apartments.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.4 «Превосходно» (229 отзывов). Отопления нет почти ни у кого в Далате из-за прохладного климата — это норма, не недостаток.","amenities":"сад и терраса, прокат велосипедов и авто на месте, кухня (холодильник, микроволновка), быстрый wifi 128 Мбит/с","policy":"бесплатная отмена до 17.08.2026"}),

L(512,"da-lat","xh","Квартира",19230000,18,
  "1-спальная квартира Khách Sạn Căn Hộ XP, 100 м до центра.",
  "https://www.booking.com/hotel/vn/khach-san-can-ho-xp-da-lat.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"новый объект, отзывов пока нет"},
  ),

L(513,"da-lat","xh","Квартира",9830000,30,
  "1-спальная квартира All Be Condotel, 1,2 км до центра — самый бюджетный вариант подборки Booking.com в Далате.",
  "https://www.booking.com/hotel/vn/all-be-condotel.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг не показан на странице поиска","policy":"бесплатная отмена"}),

L(514,"da-lat","xh","Дом",26230000,60,
  "2-спальный дом Dalat Family House, 1,8 км до центра.",
  "https://www.booking.com/hotel/vn/dalat-family-house-thanh-pho-da-lat.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 8.5 «Хорошо» (123 отзыва)","policy":"бесплатная отмена"}),

L(515,"da-lat","xh","Студия",22580000,23,
  "Студия Feliz Dalat Homestay, 300 м до центра.",
  "https://www.booking.com/hotel/vn/dalat-feliz-home.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.6 «Превосходно» (444 отзыва) — один из самых высоко оценённых вариантов в подборке"}),

L(516,"da-nang","ah","Квартира",17790000,36,
  "1-спальные апартаменты ZENITH STAY by Lan's, ул. Ngô Quyền, 1,8 км до моста Rồng, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/zenith-stay-by-lans.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.8 «Превосходно» (15 отзывов) — гости отмечают быструю связь с хозяином и новое состояние жилья","amenities":"бесплатная частная парковка, пляжная зона, своя ванная, терраса, фен","policy":"бесплатная отмена до 19.08.2026"}),

L(517,"da-nang","ns","Квартира",12270000,35,
  "1-спальная квартира Papa Danang Beach Apartment, ~5,8 км до центра, 900 м до пляжа.",
  "https://www.booking.com/hotel/vn/papa-danang-beach-apartment.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.5 «Превосходно» (2 отзыва, новый объект)"}),

L(518,"da-nang","hc","Квартира",20660000,None,
  "1-спальная квартира с садом Sweet Garden Homestay, самый центр (0,8 км), район Hải Châu.",
  "https://www.booking.com/hotel/vn/sweet-garden-homestay-hai-chau.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 10 «Превосходно» (6 отзывов) — максимальная оценка в подборке Booking.com"}),

L(519,"da-nang","st","Квартира",15420000,27,
  "1-спальная квартира My Suites Danang Beach, ~2,6 км до центра, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/my-suites-danang-beach.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 7.7 «Хорошо» (113 отзывов)","policy":"бесплатная отмена"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted booking.com listings")
