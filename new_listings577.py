# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 16 объявлений, 2026-10-29.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3002412, 3002413, 3002414, 3002415, 3002416, 3002417, 3002418, 3002419, 3002420, 3002421, 3002422, 3002423, 3002424, 3002425, 3002426, 3002427]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3002412,"manila","mak","Квартира",230000,247,
  "3-спальная квартира, 247 м², Luna Gardens, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-luna-gardens-rr2133381","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 247 m², Luna Gardens, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2133381-514168.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2133381-514168_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2133381-514168_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2133381-535454_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2133381-535454_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2133381-498773_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002413,"manila","bgc","Квартира",115000,91,
  "2-спальная квартира, 91 м², Bellagio II, BGC / Taguig — 2 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-bellagio-ii-rr0848581","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 91 m², Bellagio II, BGC / Taguig — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0848581-287224.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0848581-287224_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0848581-287224_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0848581-956168_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0848581-956168_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0848581-716895_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002414,"manila","mak","Квартира",75000,79,
  "2-спальная квартира, 79 м², Joya Lofts and Towers, Makati — 2 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-joya-lofts-and-towers-rr3549081","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 79 m², Joya Lofts and Towers, Makati — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3549081-682624.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3549081-682624_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3549081-682624_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3549081-477493_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3549081-477493_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3549081-874465_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002415,"manila","bgc","Квартира",220000,137,
  "2-спальная квартира, 137 м², The Suites at One Bonifacio High Street, BGC / Taguig — 2 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-the-suites-at-one-bonifacio-high-street-rr3493181","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 137 m², The Suites at One Bonifacio High Street, BGC / Taguig — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3493181-664796.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3493181-664796_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3493181-664796_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3493181-232516_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3493181-232516_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3493181-352623_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002416,"manila","bgc","Квартира",100000,117,
  "3-спальная квартира, 117 м², Park Cascade, BGC / Taguig — 4 санузла.",
  "https://www.hoppler.com.ph/taguig-arca-south-park-cascade-rr3545481","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 117 m², Park Cascade, BGC / Taguig — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545481-241567.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545481-241567_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545481-241567_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545481-111856_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545481-111856_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545481-651417_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002417,"manila","mak","Дом",450000,650,
  "5-спальный дом, 650 м², Dasmariñas Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr3315182","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 650 m², Dasmariñas Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3315182-293956.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3315182-293956_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3315182-293956_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3315182-829537_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3315182-829537_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3315182-819187_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002418,"manila","mak","Дом",600000,450,
  "5-спальный дом, 450 м², Dasmariñas Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr3523482","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 450 m², Dasmariñas Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3523482-169145.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3523482-169145_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3523482-169145_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3523482-845894_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3523482-845894_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3523482-567856_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002419,"manila","bgc","Офис",135200,104,
  "Офис, 104 м², High Street South Corporate Plaza, BGC / Taguig.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-high-street-south-corporate-plaza-cr0636373","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 104 m², High Street South Corporate Plaza, BGC / Taguig.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0636373-635471.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0636373-635471_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0636373-635471_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0636373-338549_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0636373-338549_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0768573-333135_orig.png?sg=propertycard"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002420,"manila","alb","Дом",160000,442,
  "4-спальный дом, 442 м², Ayala Alabang Village, Alabang — 4 санузла.",
  "https://www.hoppler.com.ph/muntinlupa-ayala-alabang-village-rr2524482","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 442 m², Ayala Alabang Village, Alabang — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2524482-242373.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2524482-242373_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2524482-242373_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2524482-536351_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2524482-536351_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2524482-793377_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002421,"manila","mak","Квартира",70000,62,
  "1-спальная квартира, 62 м², Senta, Makati — 1 санузел.",
  "https://www.hoppler.com.ph/makati-legaspi-village-senta-rr3504581","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 62 m², Senta, Makati — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3504581-163481.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3504581-163481_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3504581-163481_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3504581-158956_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3504581-158956_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3504581-832124_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002422,"manila","alb","Дом",300000,600,
  "4-спальный дом, 600 м², Ayala Alabang Village, Alabang — 5 санузлов.",
  "https://www.hoppler.com.ph/muntinlupa-ayala-alabang-village-rr3509882","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 600 m², Ayala Alabang Village, Alabang — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3509882-885496.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3509882-885496_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3509882-885496_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3509882-225698_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3509882-225698_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3509882-587628_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002423,"manila","mak","Квартира",130000,180,
  "3-спальная квартира, 180 м², The Salcedo Park, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-salcedo-village-the-salcedo-park-rr2130681","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 180 m², The Salcedo Park, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2130681-738255.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2130681-738255_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2130681-738255_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2130681-225933_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2130681-225933_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2130681-395458_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002424,"manila","mak","Дом",210000,200,
  "3-спальный дом, 200 м², Bel-Air Village, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-bel-air-village-rr0024982","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 200 m², Bel-Air Village, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0024982-461231.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0024982-461231_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0024982-461231_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0024982-326148_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0024982-326148_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0024982-463318_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002425,"manila","bgc","Квартира",160000,138,
  "2-спальная квартира, 138 м², Arya Residences, BGC / Taguig — 2 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-arya-residences-rr2553881","3 дня назад",3,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 138 m², Arya Residences, BGC / Taguig — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-516177.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-516177_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-516177_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-892213_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-892213_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-826165_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002426,"manila","mak","Дом",300000,500,
  "4-спальный дом, 500 м², Bel-Air Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-bel-air-village-rr3543682","3 дня назад",3,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 500 m², Bel-Air Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-297799.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-297799_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-297799_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-913659_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-913659_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-628343_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002427,"manila","mak","Квартира",195000,285,
  "3-спальная квартира, 285 м², Pacific Plaza Ayala, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-urdaneta-village-pacific-plaza-ayala-rr0152281","6 дней назад",6,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 285 m², Pacific Plaza Ayala, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0152281-435491.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0152281-435491_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0152281-435491_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0152281-356848_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0152281-356848_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0152281-637228_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
