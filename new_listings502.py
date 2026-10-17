# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 3 объявлений, 2026-10-18.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3002278, 3002279, 3002280]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3002278,"manila","mak","Дом",750000,600,
  "4-спальный дом, 600 м², Dasmariñas Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr1739582","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 600 m², Dasmariñas Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-931843.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-931843_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-931843_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-558564_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-558564_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1739582-738374_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002279,"manila","mak","Дом",300000,700,
  "4-спальный дом, 700 м², Dasmariñas Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr1810282","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 700 m², Dasmariñas Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-376168.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-376168_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-376168_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-119929_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-119929_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1810282-694549_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002280,"manila","mak","Дом",750000,1,
  "5-спальный дом, 1 м², Dasmariñas Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr0373982","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 1 m², Dasmariñas Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-634461.JPG", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-634461_orig.JPG?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-634461_orig.JPG?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-371152_orig.JPG?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-371152_orig.JPG?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/house-rent-RR0373982-792267_orig.JPG?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
