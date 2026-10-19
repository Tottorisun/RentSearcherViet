# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 6 объявлений, 2026-10-19.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3002289, 3002290, 3002291, 3002292, 3002293, 3002294]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3002289,"manila","bgc","Квартира",200000,186,
  "3-спальная квартира, 186 м², One McKinley Place, BGC / Taguig — 4 санузла.",
  "https://www.hoppler.com.ph/taguig-bgc-bonifacio-global-city-one-mckinley-place-rr0177281","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom flat, 186 m², One McKinley Place, BGC / Taguig — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0177281-159536.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0177281-159536_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0177281-159536_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0177281-255447_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0177281-255447_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0177281-629493_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002290,"manila","ort","Квартира",29500,34,
  "1-спальная квартира, 34 м², S Tower at SYNC, Ortigas / Pasig — 1 санузел.",
  "https://www.hoppler.com.ph/pasig-bagong-ilog-s-tower-at-sync-rr3543381","сегодня",0,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 34 m², S Tower at SYNC, Ortigas / Pasig — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3543381-117767.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3543381-117767_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3543381-117767_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3543381-348932_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3543381-348932_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3543381-541655_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002291,"manila","mak","Дом",320000,500,
  "3-спальный дом, 500 м², Dasmariñas Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr2018382","сегодня",0,source="hoppler",cur="PHP",
  descEn="3-bedroom house, 500 m², Dasmariñas Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2018382-852831.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2018382-852831_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2018382-852831_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2018382-286466_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2018382-286466_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2018382-818568_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002292,"manila","qzc","Дом",160000,420,
  "5-спальный дом, 420 м², City Bagong Pag-Asa, Quezon City — 5 санузлов.",
  "https://www.hoppler.com.ph/quezon-city-bagong-pag-asa-rr2823082","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 420 m², City Bagong Pag-Asa, Quezon City — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2823082-467126.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2823082-467126_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2823082-467126_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2823082-351717_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2823082-351717_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR2823082-998173_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002293,"manila","mak","Офис",320000,400,
  "Офис, 400 м², The World Centre, Makati.",
  "https://www.hoppler.com.ph/makati-salcedo-village-the-world-centre-cr0765473","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 400 m², The World Centre, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0765473-622465.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0765473-622465_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0765473-622465_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0765473-626734_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0765473-626734_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0765473-725789_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002294,"manila","mak","Офис",560000,700,
  "Офис, 700 м², The World Centre, Makati.",
  "https://www.hoppler.com.ph/makati-salcedo-village-the-world-centre-cr0842573","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 700 m², The World Centre, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0842573-512383.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0842573-512383_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0842573-512383_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0842573-567299_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0842573-567299_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0842573-125255_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
