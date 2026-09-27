# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 2 объявлений, 2026-09-28.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3001600, 3001601]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3001600,"manila","mak","Дом",350000,400,
  "3-спальный дом, 400 м², Dasmariñas Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr0244882","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 400 m², Dasmariñas Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0244882-526398.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0244882-526398_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0244882-526398_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0244882-915462_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0244882-915462_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0244882-838556_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001601,"manila","mak","Дом",400000,450,
  "4-спальный дом, 450 м², Bel-Air Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-bel-air-village-rr1462282","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 450 m², Bel-Air Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1462282-925955.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1462282-925955_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1462282-925955_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1462282-735561_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1462282-735561_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR1462282-231868_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
