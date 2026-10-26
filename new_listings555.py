# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 9 объявлений, 2026-10-26.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3002377, 3002378, 3002379, 3002380, 3002381, 3002382, 3002383, 3002384, 3002385]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3002377,"manila","mak","Дом",280000,700,
  "4-спальный дом, 700 м², Dasmariñas Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr1810282","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 700 m², Dasmariñas Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-793757.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-793757_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-793757_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-376168_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-376168_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-694549_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002378,"manila","mak","Дом",750000,1000,
  "5-спальный дом, 1000 м², Dasmariñas Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr0373982","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 1000 m², Dasmariñas Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-792267.JPG", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-792267_orig.JPG?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-792267_orig.JPG?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-634461_orig.JPG?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-634461_orig.JPG?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-371152_orig.JPG?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002379,"manila","mak","Дом",750000,600,
  "4-спальный дом, 600 м², Dasmariñas Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr1739582","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 600 m², Dasmariñas Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-931843.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-931843_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-931843_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-558564_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-558564_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-738374_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002380,"manila","mak","Дом",185000,255,
  "3-спальный дом, 255 м², San Lorenzo Village, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-san-lorenzo-village-rr3381382","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 255 m², San Lorenzo Village, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-571166.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-571166_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-571166_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-921478_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-921478_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-955632_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002381,"manila","mak","Офис",96800,121,
  "Офис, 121 м², Philippine AXA Life Centre, Makati.",
  "https://www.hoppler.com.ph/makati-bel-air-village-philippine-axa-life-centre-cr0768673","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 121 m², Philippine AXA Life Centre, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0768673-124399.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0768673-124399_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0768673-124399_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0768673-316659_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0768673-316659_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0768673-419162_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002382,"manila","mak","Офис",68200,124,
  "Офис, 124 м², Cityland 10, Makati.",
  "https://www.hoppler.com.ph/makati-salcedo-village-cityland-10-cr0815573","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 124 m², Cityland 10, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0815573-519593.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0815573-519593_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0815573-519593_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0815573-493167_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0815573-493167_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0815573-549945_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002383,"manila","bgc","Квартира",160000,120,
  "3-спальная квартира, 120 м², The Almond, BGC / Taguig — 2 санузла.",
  "https://www.hoppler.com.ph/taguig-two-serendra-the-almond-rr3560281","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 120 m², The Almond, BGC / Taguig — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-461613.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-461613_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-461613_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-661449_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-661449_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-878558_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002384,"manila","mdl","Квартира",90000,192,
  "3-спальная квартира, 192 м², Wack Wack Apartments, Mandaluyong — 2 санузла.",
  "https://www.hoppler.com.ph/mandaluyong-wack-wack-wack-wack-apartments-rr3243281","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 192 m², Wack Wack Apartments, Mandaluyong — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-337395.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-337395_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-337395_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-252914_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-252914_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-258975_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002385,"manila","alb","Квартира",117000,101,
  "2-спальная квартира, 101 м², Sonria Condominium, Alabang — 2 санузла.",
  "https://www.hoppler.com.ph/muntinlupa-madrigal-business-park-sonria-condominium-rr3318181","2 дня назад",2,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 101 m², Sonria Condominium, Alabang — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-624154.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-624154_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-624154_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-352893_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-352893_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-834529_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
