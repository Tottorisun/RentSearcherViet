# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 9 объявлений, 2026-09-20.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3001045, 3001046, 3001047, 3001048, 3001049, 3001050, 3001051, 3001052, 3001053]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3001045,"manila","mak","Квартира",120000,106,
  "2-спальная квартира, 106 м², One Rockwell, Makati — 2 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-one-rockwell-rr3540981","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 106 m², One Rockwell, Makati — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3540981-784793.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3540981-784793_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3540981-784793_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3540981-215397_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3540981-215397_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3540981-848158_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001046,"manila","bgc","Квартира",250000,204,
  "3-спальная квартира, 204 м², Arya Residences, BGC / Taguig — 5 санузлов.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-arya-residences-rr3556181","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 204 m², Arya Residences, BGC / Taguig — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-179888.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-179888_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-179888_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-732916_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-732916_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-873753_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001047,"manila","mak","Дом",700000,600,
  "5-спальный дом, 600 м², Dasmariñas Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr2861882","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 600 m², Dasmariñas Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2861882-564348.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2861882-564348_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2861882-564348_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2861882-495631_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2861882-495631_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2861882-241825_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001048,"manila","ort","Офис",65000,102,
  "Офис, 102 м², Jollibee Plaza, Ortigas / Pasig.",
  "https://www.hoppler.com.ph/pasig-ortigas-center-jollibee-plaza-cr0000373","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 102 m², Jollibee Plaza, Ortigas / Pasig.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-752938.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-752938_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-752938_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-853184_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-853184_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-235811_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001049,"manila","mak","Офис",88578,126,
  "Офис, 126 м², Burgundy Corporate Tower, Makati.",
  "https://www.hoppler.com.ph/makati-san-lorenzo-village-burgundy-corporate-tower-cr0766473","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 126 m², Burgundy Corporate Tower, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0766473-652181.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0766473-652181_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0766473-652181_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0766473-153294_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0766473-153294_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0766473-937512_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001050,"manila","mak","Офис",374790,374,
  "Офис, 374 м², Insular Life Makati, Makati.",
  "https://www.hoppler.com.ph/makati-paseo-de-roxas-insular-life-makati-cr0747473","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 374 m², Insular Life Makati, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747473-829235.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747473-829235_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747473-829235_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747473-739616_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747473-739616_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747473-479288_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001051,"manila","mak","Офис",718470,798,
  "Офис, 798 м², Insular Life Makati, Makati.",
  "https://www.hoppler.com.ph/makati-paseo-de-roxas-insular-life-makati-cr0747073","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 798 m², Insular Life Makati, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747073-262221.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747073-262221_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747073-262221_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747073-317455_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747073-317455_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0747073-391169_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001052,"manila","mak","Склад",1800000,1500,
  "Склад, 1500 м², makati city, Makati.",
  "https://www.hoppler.com.ph/makati-makati-city-cr0836874","сегодня",0,source="hoppler",cur="PHP",
  descEn="Warehouse, 1500 m², makati city, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-853112.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-853112_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-853112_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-791139_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-791139_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-876859_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001053,"manila","mak","Дом",325000,500,
  "4-спальный дом, 500 м², Bel-Air Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-bel-air-village-rr0222782","вчера",1,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 500 m², Bel-Air Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0222782-375515.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0222782-375515_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0222782-375515_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0222782-163419_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0222782-163419_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0222782-827799_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
