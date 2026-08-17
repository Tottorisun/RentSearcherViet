# -*- coding: utf-8 -*-
# Ho Chi Minh City batch 5/4 (addendum) — remaining 4 Trip.com PMH listings with real hotelIds
# confirmed by the research agent on follow-up. Ward corrected to "th" (Tân Hưng) per each
# listing's real address (Tân Phong/Tân Hưng), not "tm" as originally guessed. IDs 631-634.
NEW_SRC = r'''
L(631,"ho-chi-minh","th","Квартира",12525000,None,
  "Siris Mia Residence – Self Check In, квартира на цокольном этаже, 1 спальня. Адрес: 94 Đặng Đại Độ, 260 м от торгового центра Phú Mỹ Hưng.",
  "https://www.trip.com/hotels/detail/?hotelId=128666857&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($501), переведено по курсу ~25000 ₫/$."}),

L(632,"ho-chi-minh","th","Студия",24050000,None,
  "Phu My Hung – Saigon South Serviced Apartments (корпус 1), студия делюкс, рядом Vivo City Mall. Адрес: R4-88 Hưng Phước 1, Phú Mỹ Hưng, Tân Phong Ward.",
  "https://www.trip.com/hotels/detail/?hotelId=129333067&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($962), переведено по курсу ~25000 ₫/$."}),

L(633,"ho-chi-minh","th","Студия",16025000,None,
  "Phu My Hung – Saigon South Serviced Apartments (корпус 2), студия супериор. Адрес: R4-35 Hưng Phước 4.",
  "https://www.trip.com/hotels/detail/?hotelId=6231550&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($641), переведено по курсу ~25000 ₫/$."}),

L(634,"ho-chi-minh","th","Студия",22525000,None,
  "Hearth and Home Lavida, студия с балконом и видом на город (реальный комплекс Lavida в Phú Mỹ Hưng), 10 мин до Korea Town. Адрес: 1181 Nguyễn Văn Linh, Tân Phong.",
  "https://www.trip.com/hotels/detail/?hotelId=127834611&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($901), переведено по курсу ~25000 ₫/$."}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted final 4 HCMC trip.com listings")
