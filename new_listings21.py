# -*- coding: utf-8 -*-
# Ho Chi Minh City batch 6 — FB Marketplace second pass (remaining unopened candidates), IDs 635-643.
# Agent cross-checked against the original 12 and excluded 2 duplicate Ascentia units listed by other brokers.
NEW_SRC = r'''
L(635,"ho-chi-minh","tm","Квартира",33000000,89,
  "2-спальная квартира (2 с/у) в Midtown M8, Phú Mỹ Hưng, рядом парк Sakura, бассейн, спортзал, охрана 24/7.",
  "https://www.facebook.com/marketplace/item/1611784017021810/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 33 000 ₫, в описании 33 млн ₫/мес.","contact":"Em Tuyết"}),

L(636,"ho-chi-minh","th","Квартира",16000000,None,
  "2-спальная квартира (2 с/у) в Scenic Valley, Phú Mỹ Hưng, рядом Crescent Mall, SECC.",
  "https://www.facebook.com/marketplace/item/1549785510228320/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 16 ₫ (баг), в описании 16 млн ₫/мес."}),

L(637,"ho-chi-minh","th","Квартира",25000000,90,
  "2-спальная квартира (2 с/у) в Hưng Phúc 1, Phú Mỹ Hưng, вид на реку, машиноместо.",
  "https://www.facebook.com/marketplace/item/1634051588728434/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 25 000 ₫, в описании 25 млн ₫/мес.","contact":"Em Tuyết"}),

L(638,"ho-chi-minh","tm","Квартира",23000000,70,
  "2-спальная квартира (2 с/у) в The Aurora, Phú Mỹ Hưng.",
  "https://www.facebook.com/marketplace/item/2606394956497598/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 23 ₫ (баг), в описании 23 млн ₫/мес.","contact":"Vàng"}),

L(639,"ho-chi-minh","tm","Квартира",50000000,None,
  "3-спальная квартира (2 с/у) в The Ascentia, гибкая тарифная сетка: посуточно 2,8 млн ₫/ночь, помесячно (краткий срок) 60 млн ₫, при долгосрочной аренде — 50 млн ₫/мес.",
  "https://www.facebook.com/marketplace/item/1802640117824551/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 1 000 ₫ (баг). Указана цена именно для долгосрочной аренды (50 млн), а не посуточного/помесячного краткосрочного тарифа.","contact":"Em Chiến"}),

L(640,"ho-chi-minh","ak","Квартира",18000000,71,
  "2-спальная квартира (2 с/у) в Masteri Thảo Điền, 159 Võ Nguyên Giáp, свободна с конца августа.",
  "https://www.facebook.com/marketplace/item/1118026880887837/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 1 ₫ (баг), в описании 18 млн ₫/мес."}),

L(641,"ho-chi-minh","ak","Квартира",23000000,87,
  "Угловая квартира (2 спальни + доп. помещение, 2 с/у) в Tropic Garden, Thảo Điền, вид на реку.",
  "https://www.facebook.com/marketplace/item/4478437129035950/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 23 ₫ (баг), в описании «23tr net».","contact":"Mai Hà"}),

L(642,"ho-chi-minh","ak","Квартира",55000000,92,
  "2-спальная квартира в The Berkley, центр Thảo Điền — премиум-бутик комплекс (~85 квартир всего), вид на Landmark 81.",
  "https://www.facebook.com/marketplace/item/1375278774568712/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 1$ (валютный баг), в описании 55 млн ₫/мес включая плату за управление.","contact":"Thịnh Trần, 0862.101.239"}),

L(643,"ho-chi-minh","ak","Комната",14000000,None,
  "1-спальная квартира с балконом, восточная сторона, вид на реку, Thảo Điền, Thủ Đức.",
  "https://www.facebook.com/marketplace/item/1248260610704261/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 14 000 ₫, в описании 14 млн ₫/мес.","deposit":"1 месяц","amenities":"уборка 2 раза/нед, смена белья 1 раз/нед, wifi, бесплатный мопед, спортзал, BBQ, крыша","contact":"Anh Thi Min"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted second-pass fbmarketplace HCMC listings")
