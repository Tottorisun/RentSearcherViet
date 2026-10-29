# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 3 объявлений, 2026-10-29.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3002409, 3002410, 3002411]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3002409,"manila","mak","Квартира",45000,58,
  "1-спальная квартира, 58 м², Solstice, Makati — 1 санузел.",
  "https://www.hoppler.com.ph/makati-carmona-solstice-rr3483581","сегодня",0,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 58 m², Solstice, Makati — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3483581-492274.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3483581-492274_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3483581-492274_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3483581-731436_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3483581-731436_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3483581-876632_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002410,"manila","mak","Квартира",80000,148,
  "2-спальная квартира, 148 м², The Renaissance Building, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-legaspi-village-the-renaissance-building-rr3554681","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 148 m², The Renaissance Building, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3554681-549482.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3554681-549482_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3554681-549482_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3554681-147711_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3554681-147711_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3554681-636831_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002411,"manila","mak","Торговая площадь",155200,194,
  "Торговая площадь, 194 м², NorthStar Building, Makati.",
  "https://www.hoppler.com.ph/makati-bel-air-northstar-building-cr0760272","сегодня",0,source="hoppler",cur="PHP",
  descEn="Retail space, 194 m², NorthStar Building, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Commercial_Space-rent-CR0760272-111559.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Commercial_Space-rent-CR0760272-111559_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Commercial_Space-rent-CR0760272-111559_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Commercial_Space-rent-CR0760272-513676_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Commercial_Space-rent-CR0760272-513676_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Commercial_Space-rent-CR0760272-661224_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
