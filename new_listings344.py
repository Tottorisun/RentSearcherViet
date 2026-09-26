# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 2 объявлений, 2026-09-27.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3001522, 3001523]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3001522,"manila","bgc","Квартира",160000,138,
  "2-спальная квартира, 138 м², Arya Residences, BGC / Taguig — 2 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-arya-residences-rr2553881","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 138 m², Arya Residences, BGC / Taguig — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-516177.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-516177_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-516177_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-892213_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-892213_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2553881-826165_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001523,"manila","mak","Дом",300000,500,
  "4-спальный дом, 500 м², Bel-Air Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-bel-air-village-rr3543682","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 500 m², Bel-Air Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-297799.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-297799_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-297799_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-913659_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-913659_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3543682-628343_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
