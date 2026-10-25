# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 18 объявлений, 2026-10-25.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3002354, 3002355, 3002356, 3002357, 3002358, 3002359, 3002360, 3002361, 3002362, 3002363, 3002364, 3002365, 3002366, 3002367, 3002368, 3002369, 3002370, 3002371]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3002354,"manila","mak","Квартира",110000,99,
  "2-спальная квартира, 99 м², Edades Tower and Garden Villas, Makati — 2 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-edades-tower-and-garden-villas-rr1617481","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 99 m², Edades Tower and Garden Villas, Makati — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1617481-552853.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1617481-552853_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1617481-552853_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1617481-793785_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1617481-793785_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1617481-348535_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002355,"manila","bgc","Квартира",190000,133,
  "3-спальная квартира, 133 м², Grand Hyatt Manila Residences, BGC / Taguig — 3 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-grand-hyatt-manila-residences-rr3517581","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 133 m², Grand Hyatt Manila Residences, BGC / Taguig — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-732543.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-732543_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-732543_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-713159_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-713159_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-516861_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002356,"manila","bgc","Квартира",270000,236,
  "3-спальная квартира, 236 м², Arya Residences, BGC / Taguig — 3 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-arya-residences-rr2074681","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 236 m², Arya Residences, BGC / Taguig — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-615474.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-615474_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-615474_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-546837_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-546837_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-895697_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002357,"manila","qzc","Дом",140000,300,
  "3-спальный дом, 300 м², City Capitol Hills, Quezon City — 4 санузла.",
  "https://www.hoppler.com.ph/quezon-city-capitol-hills-rr3560683","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 300 m², City Capitol Hills, Quezon City — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-552668.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-552668_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-552668_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-757893_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-757893_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-735334_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002358,"manila","prq","Дом",50000,200,
  "3-спальный дом, 200 м², Parañaque / BF Homes — 3 санузла.",
  "https://www.hoppler.com.ph/paranaque-greenville-subdivision-rr3085882","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 200 m², Parañaque / BF Homes — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-314799.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-314799_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-314799_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-952624_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-952624_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-294289_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002359,"manila","bgc","Квартира",210000,133,
  "3-спальная квартира, 133 м², Grand Hyatt Manila Residences, BGC / Taguig — 3 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-grand-hyatt-manila-residences-rr3517481","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 133 m², Grand Hyatt Manila Residences, BGC / Taguig — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-615412.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-615412_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-615412_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-594434_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-594434_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-647791_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002360,"manila","mak","Дом",700000,1300,
  "4-спальный дом, 1300 м², Forbes Park, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-forbes-park-rr2262982","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 1300 m², Forbes Park, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-636947.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-636947_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-636947_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-244665_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-244665_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-616587_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002361,"manila","mak","Дом",380000,700,
  "4-спальный дом, 700 м², Dasmariñas Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr3361682","вчера",1,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 700 m², Dasmariñas Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-871411.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-871411_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-871411_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-176315_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-176315_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-249745_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002362,"manila","mak","Квартира",135000,125,
  "2-спальная квартира, 125 м², One Rockwell, Makati — 2 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-one-rockwell-rr0314981","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 125 m², One Rockwell, Makati — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/condo-rent-RR0314981-832963.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3516681-395437_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3516681-872916_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3516681-974214_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3516681-656763_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3516681-876265_orig.png?sg=propertycard"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002363,"manila","mak","Квартира",110000,100,
  "2-спальная квартира, 100 м², Joya Lofts and Towers, Makati — 2 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-joya-lofts-and-towers-rr1699181","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 100 m², Joya Lofts and Towers, Makati — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1699181-373435.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1699181-373435_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1699181-373435_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1699181-352725_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1699181-352725_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1699181-822126_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002364,"manila","bgc","Квартира",150000,98,
  "2-спальная квартира, 98 м², Fort Victoria, BGC / Taguig — 2 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-fort-victoria-rr3526081","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 98 m², Fort Victoria, BGC / Taguig — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3526081-232126.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3526081-232126_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3526081-232126_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3526081-395749_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3526081-395749_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3526081-387741_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002365,"manila","bgc","Квартира",275000,305,
  "3-спальная квартира, 305 м², Pacific Plaza Towers, BGC / Taguig — 3 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-pacific-plaza-towers-rr3559981","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 305 m², Pacific Plaza Towers, BGC / Taguig — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559981-649337.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559981-649337_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559981-649337_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559981-737895_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559981-737895_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559981-331318_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002366,"manila","bgc","Квартира",155000,145,
  "2-спальная квартира, 145 м², Arya Residences, BGC / Taguig — 2 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-arya-residences-rr1472181","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 145 m², Arya Residences, BGC / Taguig — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1472181-778195.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1472181-778195_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1472181-778195_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1472181-296912_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1472181-296912_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR1472181-653871_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002367,"manila","mak","Квартира",60000,110,
  "2-спальная квартира, 110 м², One Lafayette Square, Makati — 2 санузла.",
  "https://www.hoppler.com.ph/makati-salcedo-village-one-lafayette-square-rr0593281","3 дня назад",3,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 110 m², One Lafayette Square, Makati — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-674256.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-674256_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-674256_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-114773_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-114773_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-977737_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002368,"manila","mak","Квартира",230000,313,
  "3-спальная квартира, 313 м², One Roxas Triangle, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-urdaneta-village-one-roxas-triangle-rr3559381","3 дня назад",3,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 313 m², One Roxas Triangle, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-493449.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-493449_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-493449_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-793829_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-793829_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-647483_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002369,"manila","mak","Дом",300000,521,
  "3-спальный дом, 521 м², Bel-Air Village, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-bel-air-village-rr3559482","3 дня назад",3,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 521 m², Bel-Air Village, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-997628.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-997628_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-997628_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-384438_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-384438_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-889755_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002370,"manila","mak","Дом",500000,800,
  "4-спальный дом, 800 м², Forbes Park, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-forbes-park-rr3458482","3 дня назад",3,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 800 m², Forbes Park, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-182632.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-182632_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-182632_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-552773_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-552773_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-492178_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002371,"manila","mak","Дом",325000,450,
  "4-спальный дом, 450 м², Urdaneta Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-urdaneta-village-rr0945682","3 дня назад",3,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 450 m², Urdaneta Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-885894.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-885894_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-885894_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-658799_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-658799_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-718691_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
