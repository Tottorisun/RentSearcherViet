# -*- coding: utf-8 -*-
# Ho Chi Minh City batch 4/4 — Airbnb, Booking.com, Trip.com extended-stay listings, IDs 611-630.
# Vrbo returned zero data (blocked by anti-bot challenge across two attempts) — source omitted, not padded.
# Airbnb prices are nightly-rate x30 estimates (agent's own math). Booking.com and Trip.com prices are
# real quoted 30-night totals (Booking: VND; Trip.com: USD, converted here at ~25000 VND/USD to match
# the rest of the database). Multi-unit posts use the cheapest listed unit as price, with the range noted.
# Thanh Đa: confirmed empty across all three platforms (no geo-tagged inventory on the peninsula) — omitted, not padded.
NEW_SRC = r'''
L(611,"ho-chi-minh","ak","Квартира",58200000,None,
  "Masteri Thảo Điền, угловая 2-спальная квартира, высокий этаж, вид на город.",
  "https://www.airbnb.com/rooms/1694147022114299071","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈1 940 000 ₫/сутки), реальную месячную цену Airbnb на эти даты не показал. Хозяин прямо пишет, что юнит подходит для долгосрочной аренды."}),

L(612,"ho-chi-minh","ak","Квартира",46600000,None,
  "Lumière Riverside, 1-спальная квартира с садом, «в сердце Thảo Điền», у реки.",
  "https://www.airbnb.com/rooms/1729523314432103971","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈1 552 000 ₫/сутки)."}),

L(613,"ho-chi-minh","ak","Квартира",46800000,None,
  "Masteri An Phú, 2-спальная квартира с видом на реку («Breeze Retreat»).",
  "https://www.airbnb.com/rooms/1672976370663587539","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈1 560 000 ₫/сутки)."}),

L(614,"ho-chi-minh","ak","Квартира",72100000,None,
  "Masteri Thảo Điền, 3-спальная квартира рядом с линией метро.",
  "https://www.airbnb.com/rooms/1319897937522165158","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена со скидкой — оценка по суточной ставке ×30 (≈2 403 742 ₫/сутки)."}),

L(615,"ho-chi-minh","tm","Квартира",62500000,None,
  "The Ascentia, «стильная» 2-спальная квартира виллового формата.",
  "https://www.airbnb.com/rooms/1662111483009910968","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈2 084 475 ₫/сутки)."}),

L(616,"ho-chi-minh","tm","Квартира",80600000,None,
  "The Ascentia, «A1206 Royal State», 2-спальная квартира — подтверждено, что реально внутри комплекса The Ascentia, КГТ Phú Mỹ Hưng.",
  "https://www.airbnb.com/rooms/980222889414625674","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈2 685 925 ₫/сутки)."}),

L(617,"ho-chi-minh","tm","Квартира",72000000,None,
  "The Antonia (соседнее с The Ascentia здание), 2-спальная квартира, Quận 7.",
  "https://www.airbnb.com/rooms/997286756324926973","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена со скидкой — оценка по суточной ставке ×30 (≈2 399 999 ₫/сутки)."}),

L(618,"ho-chi-minh","ak","Квартира",50903829,80,
  "Glenwood Residences, 2-спальная квартира, ул. Nguyễn Văn Hưởng, Thảo Điền — «идеально для проживания от 30 ночей», как указано у площадки.",
  "https://www.booking.com/hotel/vn/glenwood-residence.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка Booking.com за 30 ночей (скидка от базовой цены 83,4 млн ₫)."}),

L(619,"ho-chi-minh","ak","Студия",36450000,35,
  "CHOWA HOME Thảo Điền (DNM Hospitality), ул. Xuân Thủy, Phường An Khánh — сервисный апарт-отель, есть варианты 1-спальных юнитов дороже.",
  "https://www.booking.com/hotel/vn/chowa-home-aparthotel-thao-dien-area.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, указана цена самого дешёвого юнита (студия 35 м²). В здании также: 1PN 45 м² за 40,5 млн, 1PN+балкон 48 м² за 41,31 млн."}),

L(620,"ho-chi-minh","ak","Квартира",57600000,50,
  "Masteri Thảo Điền Apartment (управляется M Living), ул. Xa lộ Hà Nội — сервисная аренда, доступны 1-3-спальные варианты.",
  "https://www.booking.com/hotel/vn/masteri-thao-dien-apartment-quan-22.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, указана цена самого дешёвого юнита (1PN 50 м²). Также: 2PN 70 м² за 60,48-63 млн, есть и 3PN 90 м²."}),

L(621,"ho-chi-minh","tm","Квартира",39600000,88,
  "Ascentia Serviced Apartment in Central Phu My Hung — подтверждённый адрес внутри The Ascentia, рядом Sakura Park PMH/SECC/Crescent Mall.",
  "https://www.booking.com/hotel/vn/ascentia-serviced-apartment-in-central-phu-my-hung.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, указана цена самого дешёвого юнита (2PN 88 м²). Также: 3PN+балкон 130 м² за 69,3-126 млн."}),

L(622,"ho-chi-minh","ak","Студия",26350000,None,
  "CHOWA HOME Thảo Điền (DNM Hospitality) — тот же объект, что и на Booking.com (проверка перекрёстно подтвердила существование), скидка 66%.",
  "https://www.trip.com/hotels/detail/?hotelId=132385067&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1054), переведено по курсу ~25000 ₫/$."}),

L(623,"ho-chi-minh","ak","Комната",25400000,None,
  "The Ninety Six Thảo Điền (DNM Hospitality), стандартный 1-спальный номер.",
  "https://www.trip.com/hotels/detail/?hotelId=134911274&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1016), переведено по курсу ~25000 ₫/$."}),

L(624,"ho-chi-minh","ak","Студия",26875000,None,
  "Express by M Village 59 Thảo Điền — реальный вьетнамский сеть сервисных апарт-отелей M Village, стандартная студия.",
  "https://www.trip.com/hotels/detail/?hotelId=114422004&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1075), переведено по курсу ~25000 ₫/$."}),

L(625,"ho-chi-minh","ak","Квартира",25125000,None,
  "Uhouse — MELIA Thảo Điền Hotel & Apartment, 1-спальная квартира с видом на город.",
  "https://www.trip.com/hotels/detail/?hotelId=132379263&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1005), переведено по курсу ~25000 ₫/$."}),

L(626,"ho-chi-minh","ak","Квартира",46025000,None,
  "Indochine Casa, Thảo Điền.",
  "https://www.trip.com/hotels/detail/?hotelId=134006768&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1841), переведено по курсу ~25000 ₫/$."}),

'''
# Note: 4 Trip.com Phú Mỹ Hưng listings (Siris Mia Residence, Saigon South Serviced Apartments x2,
# Hearth and Home Lavida) were intentionally left out of this batch — the source report didn't give
# real hotelIds for them and reusing another listing's ID would mean a fabricated URL. Pending a
# follow-up from the research agent with the real links; will add as IDs 627+ in a later batch.

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted HCMC extended-stay listings")
