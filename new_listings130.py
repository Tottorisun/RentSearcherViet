# -*- coding: utf-8 -*-
"""Думагете, бюджет: 8 объявлений из Facebook Marketplace, 5 сентября 2026.

Это то, чего не даёт ни один портал. dotproperty на весь Думагете держит 13
объявлений агентского жилья и НОЛЬ дешевле 18 000 ₱ -- проверено его же
счётчиком. Facebook за один заход отдал комнату за 2 300, комнату за 3 200,
дом за 8 000 и студию с вайфаем за 10 000. Владелец прав: на Филиппинах это
самый сильный источник по аренде.

Как получено: Marketplace через залогиненный браузер владельца, локация
Dumaguete City в радиусе 40 км, сортировка по свежести, maxPrice=18000.
Числовой идентификатор локации Думагете -- 105448822822691, с ним ссылка
строится напрямую, без выбора города руками:
  /marketplace/105448822822691/propertyrentals/?sortBy=creation_time_descend&maxPrice=18000

Возраст: все восемь остались в выдаче при daysSinceListed=30, то есть 30 дней --
честная верхняя граница, а не выдумка. У двух объявлений Facebook показал
точный возраст (час и сутки) -- у них он и стоит.

Фотографий нет намеренно: ссылки Facebook на изображения подписаны и живут
около четырёх дней, хранить их бессмысленно. Значит, эти строки живут только на
сайте и в телеграм-хаб (порог в 3 фото) не попадают.

Район у Facebook снова врал: 1037905018867640 помечен Сибуланом, а по тексту он
в Каманджаке (Думагете); 1046373474879938 помечен Баконгом, а по тексту --
Кадавинонан. Район везде взят из адреса в тексте.
"""
from listing_lock import insert_listings

IDS = [3000163, 3000164, 3000165, 3000166, 3000167, 3000168, 3000169, 3000170]

NOTE_RU = ("Источник — Facebook Marketplace. Facebook не публикует точную дату размещения для "
           "объявлений этого формата; 30 дней — верхняя граница, объявление было в выдаче с "
           "фильтром «не старше 30 дней». Фотографий нет: ссылки Facebook на изображения "
           "подписаны и живут около четырёх дней, поэтому смотрите фото по ссылке.")
NOTE_EN = ("Source: Facebook Marketplace. Facebook publishes no exact posting date for this listing "
           "format; 30 days is an upper bound — the ad was present in a feed filtered to the last "
           "30 days. No photos: Facebook image links are signed and last about four days, so see "
           "the photos on the listing itself.")
NOTE_DATED_RU = ("Источник — Facebook Marketplace, возраст объявления показан самим Facebook. "
                 "Фотографий нет: ссылки Facebook на изображения подписаны и живут около четырёх "
                 "дней, поэтому смотрите фото по ссылке.")
NOTE_DATED_EN = ("Source: Facebook Marketplace; the age is the one Facebook itself displays. "
                 "No photos: Facebook image links are signed and last about four days, so see the "
                 "photos on the listing itself.")

NEW_SRC = r'''
L(3000163,"dumaguete","dar","Комната",5500,None,
  "Комната на одного, Valencia Drive, барангай Даро, Думагете — свой санузел, кондиционер, интернет включён. Мест немного, сдаются по очереди обращений.",
  "https://www.facebook.com/marketplace/item/1396643125157408/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Single-occupancy room on Valencia Drive, Barangay Daro, Dumaguete — private bathroom, air conditioning, wifi included. Few slots, let on a first-come basis.",
  details={"notice":"REPLACE_NOTE_RU","noticeEn":"REPLACE_NOTE_EN"}),
L(3000164,"dumaguete","pul","Студия",10000,None,
  "Студия рядом с NORECO 2, Пулантубиг, Думагете — закрытый охраняемый двор, интернет, кондиционер, свой санузел, кухонный уголок, парковка для мотоцикла (для машины места нет). До St. Paul и Qualfon 3–5 минут пешком. Рассчитана на двоих. Договор на год, месяц авансом и месяц депозита.",
  "https://www.facebook.com/marketplace/item/4578363462416222/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Studio near NORECO 2, Pulantubig, Dumaguete — gated secure compound, wifi, air conditioning, private bathroom, small kitchen area, motorcycle parking (no car space). Three to five minutes' walk to St Paul and Qualfon. Suits two people. One-year contract, one month in advance and one month deposit.",
  details={"notice":"REPLACE_NOTE_RU","noticeEn":"REPLACE_NOTE_EN"}),
L(3000165,"dumaguete","dar","Студия",13000,None,
  "Студия в здании ATB рядом с бухгалтерской конторой Pelayo, Sto. Rosario Heights, Думагете — интернет и парковка бесплатно, кровать с матрасом, холодильник, телевизор с Netflix, шкафы, обеденный стол на двоих, рисоварка, индукционная плитка, чайник, посуда, водонагреватель в душе, кондиционер, столик на балконе. Электричество и вода отдельно. Договор от года, месяц авансом и два месяца депозита.",
  "https://www.facebook.com/marketplace/item/4411459472442286/","сегодня",0,source="fbmarketplace",cur="PHP",
  descEn="Studio in the ATB Building near Pelayo's accounting office, Sto. Rosario Heights, Dumaguete — free wifi and parking, bed with mattress, fridge, TV with Netflix, cabinets, a two-seat dining table, rice cooker, induction hob, kettle, utensils, water heater in the bathroom, air conditioning, a two-seat balcony table. Electricity and water billed separately. A year minimum, one month in advance and two months deposit.",
  details={"notice":"REPLACE_NOTE_DATED_RU","noticeEn":"REPLACE_NOTE_DATED_EN"}),
L(3000166,"dumaguete","bgy","Дом",15000,None,
  "Таунхаус на 2 спальни в Azumi Residences 2 (модель Satomi), Багакай, Думагете — 1 санузел, кондиционер в главной спальне, двухъярусные кровати с матрасами в обеих комнатах, вытяжка, шкафы и ящики, полностью в плитке, накопительный бак для воды, гараж. Электричество NORECO, вода MDW. Можно с кошкой и собакой.",
  "https://www.facebook.com/marketplace/item/907514992088939/","вчера",1,source="fbmarketplace",cur="PHP",
  descEn="Two-bedroom townhouse in Azumi Residences 2 (Satomi model), Bagacay, Dumaguete — one bathroom, air conditioning in the main bedroom, bunk beds with foam in both rooms, range hood, cabinets and drawers, fully tiled, water pressure tank, garage. NORECO electricity, MDW water. Cats and dogs welcome.",
  details={"notice":"REPLACE_NOTE_DATED_RU","noticeEn":"REPLACE_NOTE_DATED_EN"}),
L(3000167,"dumaguete","bcg","Дом",8000,None,
  "Дом на улице Lopez Jaena, Саксак, Баконг — за средней школой Ong Chete, в сторону моря. Описание у владельца короткое, подробности при осмотре.",
  "https://www.facebook.com/marketplace/item/1578420999785720/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="House on Lopez Jaena Street, Sacsac, Bacong — past Ong Chete high school, towards the sea. The owner's own description is brief; details on viewing.",
  details={"notice":"REPLACE_NOTE_RU","noticeEn":"REPLACE_NOTE_EN"}),
L(3000168,"dumaguete","cmj","Дом",18000,None,
  "Дом на 2 спальни и 2 санузла, Каманджак, Думагете — рядом площадка для пиклбола Bliss. Без мебели, вдоль дороги, охраняемый участок, просторно и тихо. Цена обсуждается. Владелец просит не обращаться агентов.",
  "https://www.facebook.com/marketplace/item/1037905018867640/","вчера",1,source="fbmarketplace",cur="PHP",
  descEn="Two-bedroom, two-bathroom house in Camanjac, Dumaguete — next to the Bliss pickleball court. Unfurnished, along the road, secured area, spacious and quiet. Price negotiable. The owner asks agents not to enquire.",
  details={"notice":"REPLACE_NOTE_DATED_RU","noticeEn":"REPLACE_NOTE_DATED_EN"}),
L(3000169,"dumaguete","cdw","Комната",3200,None,
  "Комната в Purok Nangka, Кадавинонан, Думагете — ориентир: комплекс Ablong рядом с церковью Tabernacle. Вода и электричество включены (техника ограничена), матрас, стул, стол, стеллаж, вентилятор, посуда и диспенсер для воды.",
  "https://www.facebook.com/marketplace/item/2356629705080419/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Room in Purok Nangka, Cadawinonan, Dumaguete — landmark: the Ablong compound beside the Tabernacle church. Water and electricity included (appliance use limited), mattress, chair, table, rack, ceiling fan, crockery and a water dispenser.",
  details={"notice":"REPLACE_NOTE_RU","noticeEn":"REPLACE_NOTE_EN"}),
L(3000170,"dumaguete","cdw","Комната",2300,None,
  "Комната в Star Apple 2, Кадавинонан, Думагете — вода и электричество включены, санузел общий на три комнаты в доме, свободна одна. Парковка только для мотоцикла. Рядом объездная дорога и перекрёсток Кадавинонан, до рынка на педикабе 15 песо.",
  "https://www.facebook.com/marketplace/item/1046373474879938/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Room in Star Apple 2, Cadawinonan, Dumaguete — water and electricity included, bathroom shared between the house's three rooms, one of which is vacant. Motorcycle parking only. Close to the diversion road and the Cadawinonan crossing; a pedicab to the market costs 15 pesos.",
  details={"notice":"REPLACE_NOTE_RU","noticeEn":"REPLACE_NOTE_EN"}),
'''

NEW_SRC = (NEW_SRC
           .replace("REPLACE_NOTE_DATED_RU", NOTE_DATED_RU)
           .replace("REPLACE_NOTE_DATED_EN", NOTE_DATED_EN)
           .replace("REPLACE_NOTE_RU", NOTE_RU)
           .replace("REPLACE_NOTE_EN", NOTE_EN))

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
