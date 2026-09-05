# -*- coding: utf-8 -*-
"""Себу и Манила из Facebook Marketplace, 5 сентября 2026: 11 объявлений.

Без ценового потолка -- владелец попросил весь диапазон. Вышло от 3 500 ₱
(койко-место в Макати) до 200 000 ₱ (дом в Ayala Alabang Village).

Слаги локаций Marketplace, чтобы не возиться с выбором города руками:
  Себу     /marketplace/cebucity/propertyrentals/
  Манила   /marketplace/manila/propertyrentals/
  Думагете /marketplace/105448822822691/propertyrentals/   (числовой id)
Дальше: ?sortBy=creation_time_descend&daysSinceListed=7&exact=false

Отсеяно на месте: продажи под видом аренды («RFO STUDIO» на Boni Ave оказался
рассрочкой -- в описании «monthly amortization», категория Home sales), объекты
в городах, которых нет в списке районов сайта (Сан-Педро, Бакоор, Танай,
Родригес, Марикина), и объявления со сломанной ценой (PHP4, PHP9, PHP50).

Район Facebook снова врал: койко-место помечено Пасаем, а по тексту оно в
Бангкале (Макати); лофт помечен Мандауэ, а ориентир в тексте -- Пит-ос. Район
везде взят из текста объявления.

Возраст: вся выдача бралась с фильтром daysSinceListed=7, поэтому 7 дней --
честная верхняя граница. Фотографий нет: ссылки Facebook подписаны и живут
около четырёх дней.
"""
from listing_lock import insert_listings

IDS = [3000171, 3000172, 3000173, 3000174, 3000175, 3000176,
       3000177, 3000178, 3000179, 3000180, 3000181]

N_RU = ("Источник — Facebook Marketplace. Точной даты размещения Facebook для этого формата не "
        "публикует; 7 дней — верхняя граница, объявление было в выдаче с фильтром «не старше "
        "7 дней». Фотографий нет: ссылки Facebook на изображения подписаны и живут около четырёх "
        "дней, смотрите фото по ссылке.")
N_EN = ("Source: Facebook Marketplace. Facebook publishes no exact posting date for this format; "
        "7 days is an upper bound — the ad was present in a feed filtered to the last 7 days. "
        "No photos: Facebook image links are signed and last about four days, so see the photos "
        "on the listing itself.")

NEW_SRC = r'''
L(3000171,"cebu","itp","Студия",13000,None,
  "Студия вплотную к IT Park, Себу — договор от года, коммунальные и взносы товарищества сверх аренды. Сдаёт собственник напрямую, без посредников; краткосрочно и с животными нельзя.",
  "https://www.facebook.com/marketplace/item/1096497229574367/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="Studio right beside IT Park, Cebu — a year's contract, with utilities and association dues on top of the rent. Let directly by the owner, no agents; no short lets and no pets.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000172,"cebu","tlm","Квартира",15000,32,
  "Двухуровневая квартира-лофт 32 м² с балконом, рядом с барангай-холлом Пит-ос и ACT, Себу — полная меблировка. При долгом сроке цена обсуждается. Месяц авансом и месяц депозита.",
  "https://www.facebook.com/marketplace/item/1379848401031260/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="Loft-type apartment, 32 m², with a balcony, near the Pit-os barangay hall and ACT, Cebu — fully furnished. Negotiable for a long let. One month in advance and one month deposit.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000173,"cebu","lah","Комната",5000,None,
  "Комната на Nivel Hills, Лахуг, Себу — свой санузел и кухня, крытая охраняемая парковка для мотоцикла. До IT Park 5 минут. Депозита нет, базовые коммунальные включены. Сдают только при личном осмотре, без предоплаты и брони.",
  "https://www.facebook.com/marketplace/item/920951160637422/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="Room on Nivel Hills, Lahug, Cebu — its own bathroom and kitchen, sheltered gated motorcycle parking. Five minutes from IT Park. No deposit, basic utilities included. Let on the spot only — no online reservations or advance payment.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000174,"cebu","cap","Дом",35000,None,
  "Двухэтажный таунхаус с мебелью в Capitol Site, Себу — 2 спальни (в главной балкон), 2 санузла, внутри охраняемого посёлка с круглосуточной охраной. В стоимость входят взносы товарищества и интернет. На территории клубный дом и бассейн, рядом прачечная. Для семьи до четырёх человек. Договор от года, месяц авансом и два месяца депозита.",
  "https://www.facebook.com/marketplace/item/1286982680137576/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="Furnished two-storey townhouse in Capitol Site, Cebu — 2 bedrooms (the master with a balcony), 2 bathrooms, inside a gated subdivision with 24-hour security. Association dues and wifi are included. Clubhouse and swimming pool on site, a laundry nearby. Suits a family of up to four. A year's contract, one month in advance and two months deposit.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000175,"cebu","tls","Дом",16000,56,
  "Двухэтажный таунхаус 56 м² в посёлке PreciousVille, Лагтанг, Талисай — 2 спальни, 1 санузел.",
  "https://www.facebook.com/marketplace/item/1390160582542970/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="Two-storey townhouse, 56 m², in PreciousVille Subdivision, Lagtang, Talisay — 2 bedrooms, 1 bathroom.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000176,"cebu","man","Квартира",120000,None,
  "Двухуровневый пентхаус-сад в Mandani Bay Suites, башня 1, Мандауэ — 3 спальни плюс комната для помощницы, 4 санузла, балкон 23 м², окна на море. Пятый этаж, то есть бассейн и спортзал на том же уровне. Два места на парковке друг за другом, взносы кондоминиума включены. Сдаётся с базовой меблировкой: кондиционеры и матрасы. Только долгосрочно.",
  "https://www.facebook.com/marketplace/item/1957583811585398/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="Two-floor garden penthouse at Mandani Bay Suites Tower 1, Mandaue — 3 bedrooms plus a maid's room, 4 bathrooms, a 23 m² balcony, sea-facing. On the fifth floor, the same level as the pool and gym. Two-car tandem parking, condo dues included. Let semi-furnished, with air conditioning and mattresses. Long term only.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000177,"manila","ort","Квартира",18000,None,
  "2-спальная квартира без отделки с участком-садом в кондоминиуме Sorrento Oasis, Пасиг — взносы товарищества включены. На территории клубный дом, бассейн, спортзал, детские площадки в помещении и на улице, теннисный и баскетбольный корты, охрана круглосуточно. Два месяца депозита и месяц авансом.",
  "https://www.facebook.com/marketplace/item/1092620203109807/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="Two-bedroom bare unit with a garden lot at Sorrento Oasis Condominium, Pasig — association dues included. The grounds have a clubhouse, swimming pool, gym, indoor and outdoor children's play areas, tennis and basketball courts, and 24-hour security. Two months deposit and one month in advance.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000178,"manila","alb","Квартира",18000,40,
  "1-спальная квартира 40 м² с балконом в Asia Enclaves, Алабанг, Мунтинлупа — частичная меблировка, взносы кондоминиума включены. Рядом Southridge, Alabang Hills, госпиталь Asian, Festival Mall, Northgate и San Beda. Договор от года, месяц авансом и месяц депозита. Собственник просит агентов не обращаться.",
  "https://www.facebook.com/marketplace/item/1449839643682053/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="One-bedroom flat, 40 m², with a balcony at Asia Enclaves, Alabang, Muntinlupa — semi-furnished, condo dues included. Southridge, Alabang Hills, Asian Hospital, Festival Mall, Northgate and San Beda are all nearby. A year minimum, one month in advance and one month deposit. The owner asks agents not to enquire.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000179,"manila","alb","Дом",200000,None,
  "Дом в Ayala Alabang Village, район 7, Мунтинлупа — участок около 650 м², после недавнего ремонта. Наверху 4 спальни и 3 санузла, в хозяйской ванне отдельная ванна и две раковины; внизу кабинет со своим санузлом. Бассейн, просторные комнаты для помощницы и водителя со своими санузлами, основная и рабочая кухни, кладовая.",
  "https://www.facebook.com/marketplace/item/1407150731376167/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="House in Ayala Alabang Village, District 7, Muntinlupa — a plot of about 650 m², newly renovated. Upstairs: 4 bedrooms and 3 bathrooms, the master with a bathtub and his-and-hers sinks; downstairs a den with its own bathroom. Swimming pool, spacious helper's and driver's rooms each with a bathroom, a main and a service kitchen, and a pantry.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000180,"manila","mak","Комната",3500,None,
  "Койко-место для женщин в Бангкале, Макати — сплит-кондиционер и холодильник. Только для работающих в дневную смену. Рядом торговая улица Evangelista, круглосуточная аптека Mercury Drug, развязка Магальянес и станция метро MRT Magallanes, выход на EDSA.",
  "https://www.facebook.com/marketplace/item/1979207219670223/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="Female bedspace in Bangkal, Makati — split-type air conditioning and a fridge. Daytime working professionals only. Close to the Evangelista commercial strip, a 24-hour Mercury Drug, the Magallanes interchange and MRT Magallanes station, with access to EDSA.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
L(3000181,"manila","qzc","Комната",4000,None,
  "Отдельная комната на Stanford St, Кубао, Кесон-Сити — санузел и мойка общие. Рядом станции MRT Cubao и LRT Araneta Cubao, выход на EDSA и Aurora Blvd, рынок рядом. До Farmers Plaza и Gateway 15 минут пешком, до SM Cubao и Ali Mall 10–15.",
  "https://www.facebook.com/marketplace/item/1311812520872671/","7 дней назад",7,source="fbmarketplace",cur="PHP",
  descEn="Solo room on Stanford St, Cubao, Quezon City — shared bathroom and sink. Close to MRT Cubao and LRT Araneta Cubao stations, with access to EDSA and Aurora Blvd, and a market nearby. Fifteen minutes' walk to Farmers Plaza and Gateway, ten to fifteen to SM Cubao and Ali Mall.",
  details={"notice":"RU_NOTE","noticeEn":"EN_NOTE"}),
'''

NEW_SRC = NEW_SRC.replace("RU_NOTE", N_RU).replace("EN_NOTE", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
