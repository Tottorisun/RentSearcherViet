# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 4 объявлений, 2026-10-28.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3002400, 3002401, 3002402, 3002403]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3002400,"manila","mak","Студия",38000,34,
  "Студия, 34 м², Senta, Makati — 1 санузел.",
  "https://www.hoppler.com.ph/makati-legaspi-village-senta-rr3034881","сегодня",0,source="hoppler",cur="PHP",
  descEn="Studio, 34 m², Senta, Makati — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3034881-245215.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3034881-245215_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3034881-245215_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3034881-686297_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3034881-686297_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3034881-233291_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002401,"manila","bgc","Квартира",75000,65,
  "1-спальная квартира, 65 м², Verve Residences, BGC / Taguig — 1 санузел.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-verve-residences-rr3475881","сегодня",0,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 65 m², Verve Residences, BGC / Taguig — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3475881-755639.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3475881-755639_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3475881-755639_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3475881-261522_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3475881-261522_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3475881-554375_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002402,"manila","mak","Дом",350000,450,
  "4-спальный дом, 450 м², Dasmariñas Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr3366882","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 450 m², Dasmariñas Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3366882-524825.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3366882-524825_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3366882-524825_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3366882-421932_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3366882-421932_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3366882-941329_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002403,"manila","bgc","Офис",238350,158,
  "Офис, 158 м², One Global Place, BGC / Taguig.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-one-global-place-cr0794273","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 158 m², One Global Place, BGC / Taguig.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0794273-456767.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0794273-456767_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0794273-456767_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0794273-822375_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0794273-822375_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0794273-774887_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
