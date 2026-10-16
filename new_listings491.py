# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 6 объявлений, 2026-10-16.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3002242, 3002243, 3002244, 3002245, 3002246, 3002247]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3002242,"manila","mak","Студия",25000,24,
  "Студия, 24 м², The Oriental Place, Makati — 1 санузел.",
  "https://www.hoppler.com.ph/makati-pio-del-pilar-the-oriental-place-rr3532481","сегодня",0,source="hoppler",cur="PHP",
  descEn="Studio, 24 m², The Oriental Place, Makati — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3532481-416666.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3532481-416666_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3532481-416666_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3532481-331643_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3532481-331643_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3532481-227552_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002243,"manila","ort","Студия",20000,21,
  "Студия, 21 м², The Grove by Rockwell, Ortigas / Pasig — 1 санузел.",
  "https://www.hoppler.com.ph/pasig-ugong-the-grove-by-rockwell-rr2739581","сегодня",0,source="hoppler",cur="PHP",
  descEn="Studio, 21 m², The Grove by Rockwell, Ortigas / Pasig — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2739581-183334.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2739581-183334_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2739581-183334_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2739581-842399_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2739581-842399_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2739581-656777_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002244,"manila","mdl","Студия",42000,35,
  "Студия, 35 м², One Shangri-La Place, Mandaluyong — 1 санузел.",
  "https://www.hoppler.com.ph/mandaluyong-ortigas-center-one-shangri-la-place-rr2730481","сегодня",0,source="hoppler",cur="PHP",
  descEn="Studio, 35 m², One Shangri-La Place, Mandaluyong — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2730481-859496.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2730481-859496_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2730481-859496_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2730481-872879_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2730481-872879_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2730481-153148_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002245,"manila","mak","Дом",420000,550,
  "4-спальный дом, 550 м², Dasmariñas Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr2157582","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 550 m², Dasmariñas Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2157582-126835.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2157582-126835_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2157582-126835_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2157582-495339_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2157582-495339_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2157582-186459_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002246,"manila","mak","Дом",400000,600,
  "4-спальный дом, 600 м², Dasmariñas Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr1530882","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 600 m², Dasmariñas Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1530882-218294.JPG", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1530882-218294_orig.JPG?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1530882-218294_orig.JPG?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3333482-347384_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3333482-463117_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3333482-283834_orig.png?sg=propertycard"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002247,"manila","mak","Офис",35000,80,
  "Офис, 80 м², San Antonio Village, Makati.",
  "https://www.hoppler.com.ph/makati-san-antonio-village-9542-cr0793673","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 80 m², San Antonio Village, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0793673-459795.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0793673-459795_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0793673-459795_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0793673-934577_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0793673-934577_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0793673-262394_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
