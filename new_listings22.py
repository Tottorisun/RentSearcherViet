# -*- coding: utf-8 -*-
# Ho Chi Minh City batch 7 — Booking.com follow-up (real 30-night prices for previously-unpriced candidates), IDs 644-653.
# Same Sept 1 - Oct 1, 2026 date range as the original Booking.com batch, for apples-to-apples comparison.
NEW_SRC = r'''
L(644,"ho-chi-minh","ak","Комната",33264000,40,
  "The Ninety Six Thảo Điền (DNM Hospitality), 1-спальный номер, ул. Quốc Hương, Phường An Khánh.",
  "https://www.booking.com/hotel/vn/the-ninety-six-thao-dien-by-dnm-hospitality.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка 52% от базовой цены 69,3 млн ₫."}),

L(645,"ho-chi-minh","ak","Квартира",33889500,40,
  "Kim Apartment, уютная 1-спальная квартира «для пар», переулок 49 Đường Võ Nguyên Giáp, Thảo Điền.",
  "https://www.booking.com/hotel/vn/kim-apartment-cozy-1br-for-couples-in-thao-dien.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка 15% от базовой цены."}),

L(646,"ho-chi-minh","ak","Студия",28240380,None,
  "Harbor Point, ул. Quốc Hương, Thảo Điền — сервисный апарт-отель, доступна студия (queen) и 1-спальный юнит 45 м².",
  "https://www.booking.com/hotel/vn/harbor-point-quoc-huong.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей (скидка 24%), указана цена самой дешёвой студии. 1-спальный юнит 45 м² — 30 098 520 ₫/30 ночей."}),

L(647,"ho-chi-minh","ak","Квартира",43116756,75,
  "Glenwood Suites, 2-спальная квартира, ул. 65, District 2 (Thảo Điền).",
  "https://www.booking.com/hotel/vn/glenwood-suites.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка 11% от базовой цены 48,4 млн ₫."}),

L(648,"ho-chi-minh","th","Квартира",49974030,90,
  "Scenic Valley 2, 2-спальная квартира с видом на сад, ул. Nguyễn Văn Linh, 200 м от SECC. Также доступны варианты 2PN/80 м² с балконом и 3PN+балкон/120 м².",
  "https://www.booking.com/hotel/vn/scenic-valley-2-ho-chi-minh.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей. Другие юниты в том же комплексе: 2PN/80м² с балконом — 49 976 973 ₫; 3PN+балкон/120м² — 82 523 670 ₫."}),

L(649,"ho-chi-minh","th","Квартира",34149600,99,
  "Starhill Phú Mỹ Hưng, 2-спальная квартира, блок E, рядом SECC.",
  "https://www.booking.com/hotel/vn/can-ho-2pn-starhill-phu-my-hung-q7.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка 38% от базовой цены 55,08 млн ₫ (самый дешёвый тариф)."}),

L(650,"ho-chi-minh","th","Квартира",31594500,74,
  "Lavida Plus, «2-спальная» квартира, ул. Nguyễn Văn Linh, District 7.",
  "https://www.booking.com/hotel/vn/lavida-plus-thanh-pho-ho-chi-minh.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей. ⚠ на странице объекта указано «2 спальни», но список кроватей показывает только 1 односпальную + диван-кровать — возможна неточность в карточке, уточняйте у площадки перед бронированием."}),

L(651,"ho-chi-minh","th","Комната",29054700,25,
  "La Serena Phú Mỹ Hưng — стандартный номер отеля (King, 25 м²), завтрак включён. R4-56/57, Hưng Phước 4, Phường Tân Phong.",
  "https://www.booking.com/hotel/vn/la-serena-phu-my-hung.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"⚠ это обычный номер 3-звёздочного отеля, а не квартира — нет кухни. Реальная котировка за 30 ночей (самый дешёвый тариф)."}),

L(652,"ho-chi-minh","th","Комната",36720000,20,
  "El Ocaso Phú Mỹ Hưng — стандартный номер отеля (double, 20 м²). R21/R4-59, Hưng Phước 2/5, District 7.",
  "https://www.booking.com/hotel/vn/el-ocaso-phu-my-hung.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"⚠ это обычный номер 3-звёздочного отеля, а не квартира — нет кухни. Реальная котировка за 30 ночей."}),

L(653,"ho-chi-minh","th","Квартира",27600000,30,
  "Ngan Ha 2 Apartment, 1-спальная квартира, ул. Cao Triều Phát, District 7. Также доступен вариант 47 м².",
  "https://www.booking.com/hotel/vn/jack-apartment.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей (скидка 20%), указан самый дешёвый юнит (30 м²). Вариант 47 м² — 36 000 000 ₫/30 ночей (та же скидка)."}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted booking.com follow-up HCMC listings")
