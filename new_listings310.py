# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 4 объявлений, 2026-09-24.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3001294, 3001295, 3001296, 3001297]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3001294,"manila","bgc","Квартира",160000,120,
  "3-спальная квартира, 120 м², The Almond, BGC / Taguig — 2 санузла.",
  "https://www.hoppler.com.ph/taguig-two-serendra-the-almond-rr3560281","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 120 m², The Almond, BGC / Taguig — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-461613.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-461613_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-461613_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-661449_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-661449_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3560281-878558_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001295,"manila","mdl","Квартира",90000,192,
  "3-спальная квартира, 192 м², Wack Wack Apartments, Mandaluyong — 2 санузла.",
  "https://www.hoppler.com.ph/mandaluyong-wack-wack-wack-wack-apartments-rr3243281","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 192 m², Wack Wack Apartments, Mandaluyong — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-337395.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-337395_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-337395_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-252914_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-252914_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3243281-258975_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001296,"manila","alb","Квартира",117000,101,
  "2-спальная квартира, 101 м², Sonria Condominium, Alabang — 2 санузла.",
  "https://www.hoppler.com.ph/muntinlupa-madrigal-business-park-sonria-condominium-rr3318181","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 101 m², Sonria Condominium, Alabang — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-624154.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-624154_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-624154_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-352893_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-352893_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3318181-834529_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3001297,"manila","mak","Дом",160000,255,
  "3-спальный дом, 255 м², San Lorenzo Village, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-san-lorenzo-village-rr3381382","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 255 m², San Lorenzo Village, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-571166.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-571166_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-571166_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-921478_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-921478_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR3381382-955632_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
