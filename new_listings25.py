# -*- coding: utf-8 -*-
# Ho Chi Minh City refresh round 2 — batch 3/5: Facebook Marketplace (14 listings), IDs 694-707.
NEW_SRC = r'''
L(694,"ho-chi-minh","bth","Квартира",12000000,None,
  "2-спальная квартира, этаж 6, лифт, большой балкон, можно с животными. Ул. Điện Biên Phủ, Quận 1.",
  "https://www.facebook.com/marketplace/item/1131674932395559/","проверено 17 авг",0,source="fbmarketplace",
  details={"fees":"обслуживание 400 000 ₫/мес, паркинг 300 000 ₫/машину, вода 150 000 ₫/чел.","electricity":"4 000 ₫/кВт·ч","contract":"от 1 года (базовая ставка без скидки — 12,5 млн ₫)","contact":"Nick Huynh (Zalo/WhatsApp)"}),

L(695,"ho-chi-minh","bth","Квартира",17000000,None,
  "Люкс-дуплекс апартаменты, ул. Nguyễn Bỉnh Khiêm, район Đa Kao — соседний с Bến Thành район старого Quận 1.",
  "https://www.facebook.com/marketplace/item/1370031828418845/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ формально это Phường Đa Kao, не Bến Thành — отдельных границ этого фыонга у нас пока нет, отнесено к Bến Thành приближённо (соседний район старого Quận 1).","electricity":"по гостарифу","contact":"Trần Trọng Trí"}),

L(696,"ho-chi-minh","bth","Квартира",9000000,45,
  "Сервисная 1-спальная квартира, полная мебель, бесплатная парковка мопеда. Переулок 121 Lê Thị Riêng, Phường Bến Thành.",
  "https://www.facebook.com/marketplace/item/2047820999471241/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 9 000 ₫ — баг ввода цены, в описании 9 млн ₫/мес (2-спальный вариант в этом же доме — 11 млн ₫).","electricity":"4 000 ₫/кВт·ч","water":"100 000 ₫/чел.","fees":"управление 200 000 ₫/комната","contact":"Zalo 093 250 1428"}),

L(697,"ho-chi-minh","bth","Квартира",5200000,None,
  "Квартира на 4 этаже без лифта, «заезжай с чемоданом», Quận 1 (точный адрес не указан).",
  "https://www.facebook.com/marketplace/item/1264979902190261/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"мало деталей в объявлении — площадь и точный адрес не указаны, продавец не назван."}),

L(698,"ho-chi-minh","kh","Квартира",21000000,74,
  "2-спальная квартира (2 с/у) в Masteri Millennium, балкон с видом на реку, заезд с 1 сентября. В этом же доме у продавца есть и другие юниты: 1BR/53м²/18тр, 2BR/74м²/22тр, 3BR/107м²/31тр, 3BR/100м²/32тр. 132 Đ. Bến Vân Đồn.",
  "https://www.facebook.com/marketplace/item/1780671263120441/","проверено 17 авг",0,source="fbmarketplace",
  details={"amenities":"спортзал, бассейн, BBQ","contact":"Tấn Huy"}),

L(699,"ho-chi-minh","kh","Квартира",17000000,65,
  "2-спальная квартира (1 с/у) в The Gold View, полная мебель, 3 мин до Q1. У того же агента в доме есть и другие юниты (81-123 м², 17-28 млн). 346 Bến Vân Đồn.",
  "https://www.facebook.com/marketplace/item/1064838342932304/","проверено 17 авг",0,source="fbmarketplace",
  details={"amenities":"спортзал, бассейн, BBQ, супермаркет, кинотеатр, кафе","contact":"Huy"}),

L(700,"ho-chi-minh","kh","Квартира",31000000,117,
  "3-спальная квартира (2 с/у) в The Gold View, полная мебель — другой юнит в том же доме, что и предыдущее объявление, у того же агента.",
  "https://www.facebook.com/marketplace/item/1391839039543431/","проверено 17 авг",0,source="fbmarketplace",
  details={"contact":"Huy"}),

L(701,"ho-chi-minh","kh","Комната",15000000,50,
  "1-спальная квартира (1 с/у) в ICON56, полная мебель, 5 мин до Q1. У продавца в доме также есть 3BR/90м² за 25 млн. 56 Bến Vân Đồn.",
  "https://www.facebook.com/marketplace/item/28805881365679369/","проверено 17 авг",0,source="fbmarketplace",
  details={"amenities":"бассейн, спортзал, магазин у дома","contact":"Tấn Huy (тот же агент, что и Masteri Millennium выше)"}),

L(702,"ho-chi-minh","kh","Комната",6000000,None,
  "1-спальный юнит у моста Khánh Hội, на границе с Q1/Q7. У хозяина есть прайс-лист: студия от 4 млн, дуплекс-антресоль от 5 млн, 1-спальная (это объявление) от 6 млн, 2-спальная от 8 млн.",
  "https://www.facebook.com/marketplace/item/1979493175975172/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 10 000 ₫ — баг ввода цены. В описании нет единой цены, только стартовая планка «от 6 млн» — финальная цена не подтверждена, указана стартовая.","amenities":"полная мебель, охрана 24/7"}),

L(703,"ho-chi-minh","tm","Квартира",22000000,55,
  "1-спальная квартира (1 с/у) в The Ascentia, высокий этаж, ул. Nguyễn Lương Bằng. Бассейны (взрослый+детский), спортзал, BBQ, парк, детская площадка, сад на крыше, рядом Crescent Mall/SC VivoCity/SECC и международные школы.",
  "https://www.facebook.com/marketplace/item/963438706325513/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 2 200 000 ₫ — баг ввода цены ровно в 10 раз, в описании 22 млн ₫/мес.","contact":"Phúc Hiền"}),

L(704,"ho-chi-minh","ak","Квартира",50000000,98,
  "3-спальная квартира (2 с/у) в Masteri Thảo Điền, высокий этаж, вид на город, торг возможен. 159 Võ Nguyên Giáp.",
  "https://www.facebook.com/marketplace/item/1202361709619200/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"цена без учёта платы за управление","amenities":"бассейн, спортзал, BBQ, детская площадка, магазин, ТЦ","contact":"Đỗ Thủy (тот же агент, что и объявление по Ascentia выше)"}),

L(705,"ho-chi-minh","ak","Квартира",27000000,None,
  "2-спальная квартира с прямым видом на реку в Masteri Thảo Điền, полная мебель. 159 Võ Nguyên Giáp.",
  "https://www.facebook.com/marketplace/item/955157487332449/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"цена net, без платы за управление","contact":"Mr. Phong"}),

L(706,"ho-chi-minh","bq","Дом",12000000,96,
  "Отдельный дом целиком (8×12м, 1 этаж + мансарда), свой двор/паркинг, 3 спальни (3 кондиционера), подходит для жизни или онлайн-бизнеса, торг возможен. Рядом рынок Thanh Đa.",
  "https://www.facebook.com/marketplace/item/1544404080572328/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 1 200 000 ₫ — баг ввода цены ровно в 10 раз, в описании 12 млн ₫/мес.","contact":"Ngọc Lành — от собственника напрямую («chính chủ»), редкая находка для этого района"}),

L(707,"ho-chi-minh","bq","Квартира",21000000,120,
  "Угловая 3-спальная квартира (2 с/у) в ЖК Thanh Đa View, балкон, бассейн, спортзал, магазин у дома, напротив рынка Thanh Đa, у моста, вокруг река Сайгон.",
  "https://www.facebook.com/marketplace/item/1043456721722228/","проверено 17 авг",0,source="fbmarketplace",
  details={"contact":"Tấn Huy (тот же агент, что и объявления по Q4 выше)"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted round-2 batch 3 (fb marketplace)")
