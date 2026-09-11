# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 1 объявлений, 2026-09-12.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 14 дней.
"""
from listing_lock import insert_listings

IDS = [3000544]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3000544,"manila","mak","Склад",1800000,1500,
  "Склад, 1500 м², makati city, Makati.",
  "https://www.hoppler.com.ph/makati-makati-city-cr0836874","сегодня",0,source="hoppler",cur="PHP",
  descEn="Warehouse, 1500 m², makati city, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-853112.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-853112_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-853112_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-791139_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-791139_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Warehouse-rent-CR0836874-876859_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
