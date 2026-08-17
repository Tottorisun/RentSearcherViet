# -*- coding: utf-8 -*-
# Second Facebook Marketplace pass — Da Nang "Apartments for Rent" subcategory, IDs 539-546.
# 3 of the 11 candidates found were dropped: one marked "Сдано в аренду" (rented) on FB,
# two had no price anywhere (neither displayed field nor description) — never fabricated.
NEW_SRC = r'''
L(539,"da-nang","ns","Квартира",7000000,40,
  "1-спальная квартира (1 с/у) в An Thượng 18, район Mỹ An, рядом с Torina Restaurant & Bakery, 1 мин на байке / 10 мин пешком до пляжа Mỹ Khê.",
  "https://www.facebook.com/marketplace/item/228701932045345/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"2 кондиционера, скоростной wifi, смарт-ТВ, полная кухня, своя стиральная машина, видеонаблюдение, паркинг в цоколе, лифт, кофейня и крыша в здании, уборка 2 раза/нед","electricity":"3 500 ₫/кВт·ч","water":"50 000 ₫/чел.","notice":"цена и все условия включены в аренду, кроме света и воды","contact":"facebook.com/DanangApartmentRentals, тел. 077 955 0817 / 056 391 9736, Zalo 078 566 8719"}),

L(540,"da-nang","st","Студия",5900000,None,
  "Меблированная студия в районе Sơn Trà, рядом с пляжем Phước Mỹ, вид из окна.",
  "https://www.facebook.com/marketplace/item/858766315655085/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"доступ к бассейну","notice":"локация на карте — ориентировочная метка, точный адрес не указан; контакты продавца скрыты без входа в FB"}),

L(541,"da-nang","st","Квартира",8000000,37,
  "Квартира на 21 этаже в Wyndham Golden Bay Da Nang, ул. Lê Văn Duyệt, район Nại Hiên Đông, Sơn Trà.",
  "https://www.facebook.com/marketplace/item/1241672263555919/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"инфинити-бассейн с позолотой, ресторан, бар, казино, конференц-зал, супермаркет, спортзал, охрана 24/7, рядом парк «7 Wonders»","notice":"контакты продавца скрыты без входа в FB"}),

L(542,"da-nang","st","Квартира",5500000,None,
  "1-спальная квартира на ул. Dương Tử Quan, район Sơn Trà, большой балкон с видом на море и город.",
  "https://www.facebook.com/marketplace/item/302415622710644/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 5 000 ₫ — баг ввода цены, в описании указано 5,5 млн ₫/мес. Контакты продавца скрыты без входа в FB (предлагает Zalo/WhatsApp/Messenger)."}),

L(543,"da-nang","st","Квартира",16000000,67,
  "Угловая 2-спальная квартира (2 с/у) в Hiyori Garden Tower, Sơn Trà, вид на мост Dragon Bridge из спальни, 700 м до пляжа Mỹ Khê, 100 м до моста.",
  "https://www.facebook.com/marketplace/item/997903025322091/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"полностью меблирована, бассейн, спортзал, паркинг, охрана 24/7, лобби","notice":"⚠ на карточке FB отображается цена 16 000 ₫ — баг ввода цены, в описании указано 16 млн ₫/мес (≈630 USD) с учётом сервисного сбора.","contact":"+84 931 914 941 (iMessage/звонок/Zalo/Viber/WhatsApp/KakaoTalk)"}),

L(544,"da-nang","st","Квартира",17000000,70,
  "Угловая 2-спальная квартира (2 с/у) в Sam Towers (Risemount Apartment Đà Nẵng), Sơn Trà, у реки, вид на реку Хан.",
  "https://www.facebook.com/marketplace/item/330540726796895/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"мебель высокого класса, гостиная, кухня, балкон, ресторан, кафе, инфинити-бассейн, спортзал, мини-маркет, ресепшн, охрана","notice":"⚠ на карточке FB отображается цена 17 ₫ — баг ввода цены, в описании указан диапазон 17-25 млн ₫/мес в зависимости от юнита, использована нижняя граница. Тот же продавец (Ms. Hiền, +84 931 914 941), что и предыдущее объявление — похоже, агент по нескольким комплексам.","contact":"Ms. Hiền, +84 931 914 941"}),

L(545,"da-nang","hc","Квартира",17000000,65,
  "Отдельная 1-спальная комната/квартира 65 м² на ул. Bạch Đằng, район Hải Châu, рядом с мостами Han River Bridge и Dragon Bridge, полностью меблирована, бассейн, спортзал, большой балкон.",
  "https://www.facebook.com/marketplace/item/1853075222160688/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена не указана (0 ₫), в описании — 17 млн ₫/мес, использована цена из описания. Метка на карте объявления показывает район Ngũ Hành Sơn, но текст описания прямо называет Bạch Đằng/Hải Châu — расхождение между меткой и текстом, в подборке отнесено к Hải Châu по содержанию описания.","contact":"Mr. Tâm, 0395736699 (Zalo)"}),

L(546,"da-nang","hc","Квартира",38000000,None,
  "Люксовая 2-спальная квартира в The Filmore, район Hải Châu, панорамный вид на город и реку, окна в пол.",
  "https://www.facebook.com/marketplace/item/1068616929196867/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"холодильник Toshiba, стиральная машина LG ThinQ с фронтальной загрузкой, центральный кондиционер, обеденная группа, встроенные шкафы; в аренду включены сервисный сбор здания и скоростной wifi","notice":"⚠ дорогой люксовый вариант (≈1500 USD/мес). Продавец не заполнил номер телефона в объявлении (поле буквально гласит «(Insert your phone number)») — связаться можно только через Messenger по ссылке на объявление."}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted second-pass fbmarketplace listings")
