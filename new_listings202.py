# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 10 объявлений, 2026-09-14.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3000646, 3000647, 3000648, 3000649, 3000650, 3000651, 3000652, 3000653, 3000654, 3000655]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3000646,"manila","mak","Квартира",250000,200,
  "3-спальная квартира, 200 м², Sakura at The Proscenium, Rockwell Center, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-sakura-at-the-proscenium-rockwell-center-rr3013681","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 200 m², Sakura at The Proscenium, Rockwell Center, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-641576.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-641576_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-641576_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-838526_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-838526_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3013681-129638_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000647,"manila","bgc","Квартира",35000,32,
  "1-спальная квартира, 32 м², One Uptown Residence, BGC / Taguig — 1 санузел.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-one-uptown-residence-rr2808381","сегодня",0,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 32 m², One Uptown Residence, BGC / Taguig — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-741724.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-741724_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-741724_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-795671_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-795671_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2808381-453273_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000648,"manila","ort","Квартира",55000,68,
  "1-спальная квартира, 68 м², The Grove by Rockwell, Ortigas / Pasig — 1 санузел.",
  "https://www.hoppler.com.ph/pasig-ugong-the-grove-by-rockwell-rr2735281","сегодня",0,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 68 m², The Grove by Rockwell, Ortigas / Pasig — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2735281-692112.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2735281-692112_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2735281-692112_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2735281-957822_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2735281-957822_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2735281-447622_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000649,"manila","mak","Квартира",400000,331,
  "3-спальная квартира, 331 м², Two Roxas Triangle, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-salcedo-village-two-roxas-triangle-rr3559281","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 331 m², Two Roxas Triangle, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-722164.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-722164_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-722164_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-261866_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-261866_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3559281-272627_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000650,"manila","prq","Дом",85000,450,
  "4-спальный дом, 450 м², Parañaque / BF Homes — 4 санузла.",
  "https://www.hoppler.com.ph/paranaque-south-bay-gardens-rr1925082","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 450 m², Parañaque / BF Homes — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-938632.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-938632_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-938632_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-721528_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-721528_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1925082-794742_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000651,"manila","mak","Дом",380000,700,
  "4-спальный дом, 700 м², Dasmariñas Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr3361682","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 700 m², Dasmariñas Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-871411.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-871411_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-871411_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-176315_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-176315_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3361682-249745_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000652,"manila","mak","Дом",700000,1300,
  "4-спальный дом, 1300 м², Forbes Park, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-forbes-park-rr2262982","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 1300 m², Forbes Park, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-636947.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-636947_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-636947_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-244665_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-244665_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2262982-616587_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000653,"manila","mak","Дом",800000,685,
  "4-спальный дом, 685 м², Forbes Park, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-forbes-park-rr3359782","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 685 m², Forbes Park, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3359782-164243.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3359782-164243_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3359782-164243_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0238982-554831_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0238982-997683_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0238982-964799_orig.png?sg=propertycard"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000654,"manila","mak","Дом",750000,940,
  "5-спальный дом, 940 м², Forbes Park, Makati — 6 санузлов.",
  "https://www.hoppler.com.ph/makati-forbes-park-rr0511782","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 940 m², Forbes Park, Makati — 6 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0511782-329636.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0511782-329636_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0511782-329636_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0511782-723934_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0511782-723934_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0511782-587231_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000655,"manila","mak","Дом",750000,650,
  "5-спальный дом, 650 м², Urdaneta Village, Makati — 8 санузлов.",
  "https://www.hoppler.com.ph/makati-urdaneta-village-rr2826382","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 650 m², Urdaneta Village, Makati — 8 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-887245.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-887245_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-887245_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-278291_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-278291_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2826382-679992_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
