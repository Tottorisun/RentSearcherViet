# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 18 объявлений, 2026-10-01.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3001775, 3001776, 3001777, 3001778, 3001779, 3001780, 3001781, 3001782, 3001783, 3001784, 3001785, 3001786, 3001787, 3001788, 3001789, 3001790, 3001791, 3001792]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3001775,"manila","mak","Квартира",60000,110,
  "2-спальная квартира, 110 м², One Lafayette Square, Makati — 2 санузла.",
  "https://www.hoppler.com.ph/makati-salcedo-village-one-lafayette-square-rr0593281","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 110 m², One Lafayette Square, Makati — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-674256.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-674256_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-674256_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-114773_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-114773_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0593281-977737_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001776,"manila","bgc","Квартира",190000,133,
  "3-спальная квартира, 133 м², Grand Hyatt Manila Residences, BGC / Taguig — 3 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-grand-hyatt-manila-residences-rr3517581","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 133 m², Grand Hyatt Manila Residences, BGC / Taguig — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-732543.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-732543_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-732543_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-713159_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-713159_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517581-516861_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001777,"manila","mak","Квартира",230000,313,
  "3-спальная квартира, 313 м², One Roxas Triangle, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-urdaneta-village-one-roxas-triangle-rr3559381","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 313 m², One Roxas Triangle, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-493449.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-493449_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-493449_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-793829_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-793829_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559381-647483_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001778,"manila","bgc","Квартира",270000,236,
  "3-спальная квартира, 236 м², Arya Residences, BGC / Taguig — 3 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-arya-residences-rr2074681","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 236 m², Arya Residences, BGC / Taguig — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-615474.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-615474_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-615474_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-546837_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-546837_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2074681-895697_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001779,"manila","qzc","Дом",140000,300,
  "3-спальный дом, 300 м², City Capitol Hills, Quezon City — 4 санузла.",
  "https://www.hoppler.com.ph/quezon-city-capitol-hills-rr3560683","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 300 m², City Capitol Hills, Quezon City — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-552668.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-552668_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-552668_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-757893_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-757893_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Townhouse-rent-RR3560683-735334_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001780,"manila","prq","Дом",50000,200,
  "3-спальный дом, 200 м², Parañaque / BF Homes — 3 санузла.",
  "https://www.hoppler.com.ph/paranaque-greenville-subdivision-rr3085882","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 200 m², Parañaque / BF Homes — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-314799.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-314799_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-314799_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-952624_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-952624_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3085882-294289_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001781,"manila","mak","Квартира",250000,200,
  "3-спальная квартира, 200 м², Sakura at The Proscenium, Rockwell Center, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-sakura-at-the-proscenium-rockwell-center-rr3013681","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 200 m², Sakura at The Proscenium, Rockwell Center, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-641576.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-641576_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-641576_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-838526_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-838526_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-129638_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001782,"manila","bgc","Квартира",210000,133,
  "3-спальная квартира, 133 м², Grand Hyatt Manila Residences, BGC / Taguig — 3 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-grand-hyatt-manila-residences-rr3517481","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 133 m², Grand Hyatt Manila Residences, BGC / Taguig — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-615412.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-615412_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-615412_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-594434_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-594434_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3517481-647791_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001783,"manila","prq","Дом",85000,450,
  "4-спальный дом, 450 м², Parañaque / BF Homes — 4 санузла.",
  "https://www.hoppler.com.ph/paranaque-south-bay-gardens-rr1925082","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 450 m², Parañaque / BF Homes — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-938632.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-938632_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-938632_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-721528_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-721528_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-794742_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001784,"manila","mak","Квартира",400000,331,
  "3-спальная квартира, 331 м², Two Roxas Triangle, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-salcedo-village-two-roxas-triangle-rr3559281","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 331 m², Two Roxas Triangle, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-722164.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-722164_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-722164_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-261866_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-261866_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-272627_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001785,"manila","mak","Дом",700000,1300,
  "4-спальный дом, 1300 м², Forbes Park, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-forbes-park-rr2262982","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 1300 m², Forbes Park, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-636947.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-636947_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-636947_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-244665_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-244665_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-616587_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001786,"manila","mak","Дом",380000,700,
  "4-спальный дом, 700 м², Dasmariñas Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr3361682","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 700 m², Dasmariñas Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-871411.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-871411_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-871411_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-176315_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-176315_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-249745_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001787,"manila","mak","Дом",300000,521,
  "3-спальный дом, 521 м², Bel-Air Village, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-bel-air-village-rr3559482","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 521 m², Bel-Air Village, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-997628.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-997628_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-997628_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-384438_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-384438_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3559482-889755_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001788,"manila","mak","Дом",500000,800,
  "4-спальный дом, 800 м², Forbes Park, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-forbes-park-rr3458482","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 800 m², Forbes Park, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-182632.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-182632_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-182632_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-552773_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-552773_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3458482-492178_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001789,"manila","mak","Дом",325000,450,
  "4-спальный дом, 450 м², Urdaneta Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-urdaneta-village-rr0945682","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 450 m², Urdaneta Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-885894.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-885894_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-885894_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-658799_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-658799_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0945682-718691_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001790,"manila","mak","Дом",800000,685,
  "4-спальный дом, 685 м², Forbes Park, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-forbes-park-rr3359782","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 685 m², Forbes Park, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3359782-164243.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3359782-164243_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3359782-164243_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0238982-554831_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0238982-997683_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0238982-964799_orig.png?sg=propertycard"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001791,"manila","mak","Дом",750000,650,
  "5-спальный дом, 650 м², Urdaneta Village, Makati — 8 санузлов.",
  "https://www.hoppler.com.ph/makati-urdaneta-village-rr2826382","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 650 m², Urdaneta Village, Makati — 8 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-887245.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-887245_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-887245_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-278291_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-278291_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-679992_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001792,"manila","bgc","Квартира",35000,32,
  "1-спальная квартира, 32 м², One Uptown Residence, BGC / Taguig — 1 санузел.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-one-uptown-residence-rr2808381","вчера",1,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 32 m², One Uptown Residence, BGC / Taguig — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-741724.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-741724_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-741724_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-795671_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-795671_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-453273_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
