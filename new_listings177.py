# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 2 объявлений, 2026-09-12.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 14 дней.
"""
from listing_lock import insert_listings

IDS = [3000556, 3000557]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3000556,"manila","bgc","Квартира",250000,204,
  "3-спальная квартира, 204 м², Arya Residences, BGC / Taguig — 5 санузлов.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-arya-residences-rr3556181","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 204 m², Arya Residences, BGC / Taguig — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-179888.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-179888_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-179888_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-732916_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-732916_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3556181-873753_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3000557,"manila","ort","Офис",65000,102,
  "Офис, 102 м², Jollibee Plaza, Ortigas / Pasig.",
  "https://www.hoppler.com.ph/pasig-ortigas-center-jollibee-plaza-cr0000373","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 102 m², Jollibee Plaza, Ortigas / Pasig.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-752938.jpg", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-752938_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-752938_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-853184_orig.jpg?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-853184_orig.jpg?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/office_space-rent-CR0000373-235811_orig.jpg?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
