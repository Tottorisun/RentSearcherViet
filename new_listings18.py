# -*- coding: utf-8 -*-
# Ho Chi Minh City batch 3/4 — Facebook Marketplace (12) + Facebook groups (2), IDs 597-610.
NEW_SRC = r'''
L(597,"ho-chi-minh","th","Квартира",27000000,124,
  "3-спальная квартира в ЖК Nam Khang, рядом школа BCIS, Нам Сайгон.",
  "https://www.facebook.com/marketplace/item/1188672412601724/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 2 700 000 ₫ — баг ввода цены, в описании указано ~1100$ (≈27 млн ₫/мес).","amenities":"машиноместо","contact":"em Hùng, 0979555019"}),

L(598,"ho-chi-minh","tm","Квартира",70000000,125,
  "3-спальная квартира (2 с/у) с видом на реку, Hồ Bán Nguyệt, Phú Mỹ Hưng.",
  "https://www.facebook.com/marketplace/item/3579590115526281/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 7 000 000 ₫ — баг ввода цены ровно в 10 раз, в описании указано 70 млн ₫/мес.","amenities":"полная меблировка, 4 подземных паркинга, бассейн, спортзал, рядом шопхаусы","contact":"Mai Nguyễn"}),

L(599,"ho-chi-minh","tm","Квартира",27000000,84,
  "2-спальная квартира (2 с/у) в The Ascentia, вид на ул. Nguyễn Lương Bằng, цена договорная.",
  "https://www.facebook.com/marketplace/item/1915299205818961/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 27 000 ₫ — тот же баг округления, в описании 27 млн ₫/мес.","contact":"Đỗ Thủy"}),

L(600,"ho-chi-minh","tm","Квартира",40000000,None,
  "Угловая 3-спальная квартира (2 с/у) в The Ascentia, полная меблировка, 1 машиноместо.",
  "https://www.facebook.com/marketplace/item/1289312213382216/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 40 000 ₫, в описании 40 млн ₫/мес."}),

L(601,"ho-chi-minh","tm","Квартира",28000000,None,
  "2-спальная квартира (2 с/у) в The Ascentia, средний этаж, полная меблировка.",
  "https://www.facebook.com/marketplace/item/2074602626776916/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 28 000 ₫, в описании 28 млн ₫/мес («net price»).","amenities":"бассейн Oasis, джакузи, спортзал, рядом международные школы и банки","contact":"Hoang"}),

L(602,"ho-chi-minh","ak","Квартира",33000000,None,
  "Пентхаус, 2 спальни, собственная просторная терраса на крыше, ул. Nguyễn Thị Định, рядом An Phú, Thảo Điền, Thủ Thiêm, метро An Phú.",
  "https://www.facebook.com/marketplace/item/1364525298528370/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 33 ₫, в описании 33 млн ₫/мес. Свободна с 18.08.","amenities":"полная меблировка, можно с животными, уборка 2 раза/нед","contact":"Cảnh Kiều"}),

L(603,"ho-chi-minh","ak","Квартира",30000000,115,
  "Угловая 2-спальная квартира в Thảo Điền Pearl, свободна с 1 сентября.",
  "https://www.facebook.com/marketplace/item/1051717207346683/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"цена на карточке и в описании совпадают — редкий случай без расхождения."}),

L(604,"ho-chi-minh","ak","Квартира",25000000,140,
  "3-спальная квартира в ЖК Fideco, Thảo Điền.",
  "https://www.facebook.com/marketplace/item/1378751054224604/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 25 000 ₫, в описании 25 млн ₫/мес."}),

L(605,"ho-chi-minh","bq","Квартира",14000000,None,
  "2-спальная квартира (можно перегородить на 3), первый этаж, кооперативный дом («cư xá») Thanh Đa.",
  "https://www.facebook.com/marketplace/item/2784338871929282/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 14 000 ₫, в описании 14 млн ₫/мес. Метка местоположения на FB ошибочно показывала «Quận 3».","contact":"Chi"}),

L(606,"ho-chi-minh","bq","Квартира",21000000,120,
  "Угловая 3-спальная квартира (2 с/у) в комплексе Thanh Đa View №7, у моста Thanh Đa, напротив рынка, вид на реку Сайгон.",
  "https://www.facebook.com/marketplace/item/1578595263909443/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 21 000 ₫, в описании 21 млн ₫/мес.","amenities":"бассейн, спортзал, мини-маркет","contact":"Tấn Huy"}),

L(607,"ho-chi-minh","bq","Квартира",21000000,130,
  "3-спальная квартира (2 с/у) в охраняемом комплексе Thanh Đa View, бассейн, бесплатный спортзал, супермаркет.",
  "https://www.facebook.com/marketplace/item/1330550035468360/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 1 ₫ (баг), в описании указано «21TR» (21 млн ₫/мес)."}),

L(608,"ho-chi-minh","bq","Дом",8000000,100,
  "Отдельный 3-этажный дом, 3 спальни/3 с/у, точный адрес 28/3 Thanh Đa (район «Cháo Vịt»), рядом вузы (HUTECH, ГТВТ, Ngoại Thương, Văn Lang), рынок ~100м.",
  "https://www.facebook.com/marketplace/item/1552697653227922/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"цена на карточке и в описании совпадают.","contact":"Mr. Đức, 0903.67.0123"}),

L(609,"ho-chi-minh","tm","Квартира",25000000,84,
  "2-спальная квартира (2 с/у), The Ascentia, найдена через агентство VN Space (офисы Phú Mỹ Hưng и An Phú), торг возможен.",
  "https://www.facebook.com/vnspacehcm/posts/2br-fully-furnished-apartment-the-ascentia-phu-my-hung-dist-72-bedrooms-2-bathro/1511976834266386/","проверено 17 авг",1,source="facebook",
  details={"notice":"цена указана $1200/мес, переведено по курсу ~25000. Полная меблировка.","amenities":"бассейн, фитнес, йога-комната, детская площадка, сауна","contact":"агентство VN Space, офис PMH +84 28 5412 1570, офис An Phú +84 28 3740 6177"}),

L(610,"ho-chi-minh","ak","Квартира",22000000,None,
  "2-спальная квартира в Masteri Thảo Điền, современный ремонт.",
  "https://www.facebook.com/groups/1939999392801882/posts/masteri-thao-dien-2-bedroom-apartment-for-rent-ho-chi-minh-city-apartment-for-re/3747635085371628/","проверено 17 авг",1,source="facebook",
  details={"notice":"площадь и контакты не удалось подтвердить — карточка группы за логин-стеной Facebook, известна только цена и общее описание."}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted HCMC fb marketplace + fb groups listings")
