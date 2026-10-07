# -*- coding: utf-8 -*-
"""hoppler.com.ph, автоматический сбор: 9 объявлений, 2026-10-07.

Партию собрал collect_hoppler.py -- без модели в контуре. Район взят из города
Метро Манилы, к которому объявление отнёс сам портал; города без однозначного
ключа (сама Манила, Лас-Пиньяс, Сан-Хуан) пропущены целиком. Описание собрано из
полей карточки, возраст -- по дате последнего изменения, не старше 7 дней.
"""
from listing_lock import insert_listings

IDS = [3002071, 3002072, 3002073, 3002074, 3002075, 3002076, 3002077, 3002078, 3002079]

N_RU = "Описание собрано программой из карточки объявления на hoppler.com.ph — тип, спальни, санузлы, площадь, название дома и цена. Рекламный текст объявления не пересказан. hoppler публикует не дату размещения, а дату последнего изменения объявления: возраст считается по ней, и объявление могло быть создано раньше."
N_EN = "This description was assembled by a program from the listing card on hoppler.com.ph — type, bedrooms, bathrooms, size, building name and price. The ad's marketing text is not retold. Hoppler publishes a last-updated date rather than a posting date: the age is counted from it, and the listing may have been created earlier."

NEW_SRC = r'''
L(3002071,"manila","mak","Квартира",290000,281,
  "4-спальная квартира, 281 м², Edades Tower and Garden Villas, Makati — 3 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-edades-tower-and-garden-villas-rr2731781","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom flat, 281 m², Edades Tower and Garden Villas, Makati — 3 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2731781-828246.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2731781-828246_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2731781-828246_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2731781-786413_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2731781-786413_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2731781-743456_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002072,"manila","mak","Квартира",65000,51,
  "1-спальная квартира, 51 м², Escala Salcedo, Makati — 1 санузел.",
  "https://www.hoppler.com.ph/makati-salcedo-village-escala-salcedo-rr2600081","сегодня",0,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 51 m², Escala Salcedo, Makati — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2600081-373611.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2600081-373611_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2600081-373611_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2600081-168423_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2600081-168423_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR2600081-439188_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002073,"manila","mak","Квартира",70000,50,
  "1-спальная квартира, 50 м², Escala Salcedo, Makati — 1 санузел.",
  "https://www.hoppler.com.ph/makati-salcedo-village-escala-salcedo-rr3545381","сегодня",0,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 50 m², Escala Salcedo, Makati — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545381-346529.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545381-346529_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545381-346529_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545381-452452_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545381-452452_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3545381-596458_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002074,"manila","mak","Квартира",70000,137,
  "2-спальная квартира, 137 м², Manhattan Square, Makati — 1 санузел.",
  "https://www.hoppler.com.ph/makati-salcedo-village-manhattan-square-rr3536281","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 137 m², Manhattan Square, Makati — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3536281-214373.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3536281-214373_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3536281-214373_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3536281-854847_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3536281-854847_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3536281-814932_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002075,"manila","mak","Квартира",59500,51,
  "1-спальная квартира, 51 м², Escala Salcedo, Makati — 1 санузел.",
  "https://www.hoppler.com.ph/makati-salcedo-village-escala-salcedo-rr3552681","сегодня",0,source="hoppler",cur="PHP",
  descEn="1-bedroom flat, 51 m², Escala Salcedo, Makati — 1 bathroom.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3552681-282495.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3552681-282495_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3552681-282495_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3552681-664515_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3552681-664515_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR3552681-741739_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002076,"manila","mak","Квартира",140000,98,
  "2-спальная квартира, 98 м², Edades Tower and Garden Villas, Makati — 2 санузла.",
  "https://www.hoppler.com.ph/makati-rockwell-center-edades-tower-and-garden-villas-rr0805181","сегодня",0,source="hoppler",cur="PHP",
  descEn="2-bedroom flat, 98 m², Edades Tower and Garden Villas, Makati — 2 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0805181-333945.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0805181-333945_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0805181-333945_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0805181-786661_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0805181-786661_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/Condominium-rent-RR0805181-816962_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002077,"manila","mak","Дом",350000,850,
  "5-спальный дом, 850 м², Dasmariñas Village, Makati — 5 санузлов.",
  "https://www.hoppler.com.ph/makati-dasmarinas-village-rr0674682","сегодня",0,source="hoppler",cur="PHP",
  descEn="5-bedroom house, 850 m², Dasmariñas Village, Makati — 5 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0674682-599149.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0674682-599149_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0674682-599149_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0674682-373212_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0674682-373212_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0674682-799766_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002078,"manila","mak","Дом",170000,280,
  "4-спальный дом, 280 м², San Lorenzo Village, Makati — 4 санузла.",
  "https://www.hoppler.com.ph/makati-san-lorenzo-village-rr0250682","сегодня",0,source="hoppler",cur="PHP",
  descEn="4-bedroom house, 280 m², San Lorenzo Village, Makati — 4 bathrooms.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0250682-322267.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0250682-322267_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0250682-322267_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0250682-766136_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0250682-766136_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/residential/House_and_Lot-rent-RR0250682-912363_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(3002079,"manila","mak","Офис",116350,179,
  "Офис, 179 м², 139 Corporate Center, Makati.",
  "https://www.hoppler.com.ph/makati-salcedo-village-139-corporate-center-cr0714373","сегодня",0,source="hoppler",cur="PHP",
  descEn="Office, 179 m², 139 Corporate Center, Makati.",
  details={"photos": ["https://dzjqf1alh39sw.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0714373-939372.png", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0714373-939372_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0714373-939372_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0714373-693719_orig.png?sg=propertypage", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0714373-693719_orig.png?sg=propertycard", "https://d2wy52y0hrt3v.cloudfront.net/hoppler/properties/commercial/Office_Space-rent-CR0714373-728218_orig.png?sg=propertypage"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
