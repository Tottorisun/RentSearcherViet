# -*- coding: utf-8 -*-
# Facebook Marketplace integration (source="fbmarketplace"), IDs 520-538.
# Source quirk: FB's displayed price field is often 10x lower than the price stated in the
# listing description (e.g. displayed 1,600,000 vs description "16.000.000/thang"). The
# description price is used everywhere below as authoritative; the discrepancy is noted.
NEW_SRC = r'''
L(520,"nha-trang","pl","Квартира",10000000,65,
  "Угловая 2-спальная квартира (2 с/у) с балконом в ЖК CT4 Hud, ул. 28, КГТ Phước Long, полностью меблирована, заезжай с чемоданом.",
  "https://www.facebook.com/marketplace/item/1491098622776266/","проверено 16 авг",1,source="fbmarketplace",
  details={"deposit":"2 месяца","notice":"⚠ на карточке FB отображается цена 1 000 000 ₫ — это баг ввода цены у продавца, в тексте описания указано 10 000 000 ₫/мес, используется цена из описания.","contact":"продавец Lê Đình Ngọc (на FB с 2018)"}),

L(521,"nha-trang","vt","Квартира",16000000,None,
  "3-спальная квартира (2 с/у) с видом на море в Napoleon Seaview Apartments, рядом с Университетом Нячанга, тихий охраняемый район, средний этаж.",
  "https://www.facebook.com/marketplace/item/1379138427501752/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"6-12 месяцев","deposit":"2 месяца","notice":"⚠ на карточке FB отображается цена 1 600 000 ₫ — баг ввода цены, в описании указано 16 000 000 ₫/мес. Тот же комплекс, что и объявление Booking.com (Napoleon Seaview Apartments).","contact":"продавец Phạm Quang Vinh (на FB с 2022)"}),

L(522,"nha-trang","vh","Квартира",14000000,68,
  "2-спальная квартира (2 с/у) + гостиная в ЖК Mường Thanh, ул. Trần Phú, в двух шагах от пляжа Hòn Chồng, высокий этаж с видом на море.",
  "https://www.facebook.com/marketplace/item/1765831987748168/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"6-12 месяцев","notice":"⚠ на карточке FB отображается цена 1 400 000 ₫ — баг ввода цены, в описании указано 14 000 000 ₫/мес.","contact":"продавец Phạm Quang Vinh (тот же, что и предыдущее объявление)"}),

L(523,"nha-trang","pl","Дом",7000000,None,
  "Шопхаус (2 спальни, первый этаж под коммерцию) на красной линии ул. B5, КГТ Vĩnh Điềm Trung — +500 тыс ₫/мес, если нужен кондиционер.",
  "https://www.facebook.com/marketplace/item/1358002595906876/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"договор на 2 года","notice":"Vĩnh Điềm Trung формально не входит в 12 центральных фан/районов Нячанга — район отмечен ориентировочно (ближайший — Phước Long), уточняйте точное расположение у продавца.","contact":"продавец Trần Nga (на FB с 2016)"}),

L(524,"nha-trang","vh","Студия",8500000,30,
  "Студия NVS-101 (первый этаж, отдельный вход) на ул. Ngô Văn Sở, район Vĩnh Hòa, север города, рядом с пляжем, доступна с 19 августа.",
  "https://www.facebook.com/marketplace/item/1831682444660681/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"3-6 месяцев","notice":"свет 5 000 ₫/кВт·ч, вода 100 000 ₫/чел. Разрешено с животными.","amenities":"своя стиральная машина, балкон с видом на горы","contact":"продавец Út Tiên (на FB с 2012)"}),

L(525,"nha-trang","vp","Дом",20000000,120,
  "Дом на красной линии (первый этаж + 2 верхних, 8 комнат, 4 с/у, фасад 4,5 м) под офис/шоурум/учебный центр, рядом с Hòn Chồng и Mường Thanh Viễn Triều.",
  "https://www.facebook.com/marketplace/item/1318995706466092/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 2 000 000 ₫ — баг ввода цены, в описании указано 20 000 000 ₫/мес. Формат — коммерческая недвижимость, а не обычное жильё.","contact":"продавец Thuhien Tranthi (на FB с 2012)"}),

L(526,"nha-trang","lt","Квартира",15000000,51,
  "Меблированная квартира с видом на море в Gold Coast, район Lộc Thọ.",
  "https://www.facebook.com/marketplace/item/1702036000907446/","проверено 16 авг",1,source="fbmarketplace",
  details={"deposit":"2 месяца","notice":"⚠ на карточке FB отображается цена 1 500 000 ₫ — баг ввода цены, в описании указано 15 000 000 ₫/мес. Тот же комплекс Gold Coast, что и объявление Booking.com.","contact":"продавец Lê Đình Ngọc (тот же, что и объявление №520)"}),

L(527,"da-lat","lv","Квартира",19000000,150,
  "3-спальная квартира (2 с/у) с парной, ул. Nguyễn Đình Chiểu, рядом с площадью Lâm Viên и Университетом Далата, 3 мин до озера Xuân Hương.",
  "https://www.facebook.com/marketplace/item/921137010467937/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"6-12 месяцев","notice":"продавец — новый аккаунт на FB (2026 год), доп. проверка не помешает","contact":"продавец Hương Mai"}),

L(528,"da-lat","xh","Дом",5000000,20,
  "3 смежных таунхауса (~20 м² + мансарда каждый, 1 спальня/1 с/у) в Ан Тон, район Xuân Hương Mới — часть ещё в отделке. Подходит под долгосрочное жильё, хоумстей или small business.",
  "https://www.facebook.com/marketplace/item/1702699750842770/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"от 1 года","notice":"3 отдельных юнита по цене 5 / 6 / 7 млн ₫ в месяц соответственно — указана цена самого дешёвого.","contact":"продавец Nhà Đất Đà Lạt (на FB с 2022)"}),

L(529,"da-lat","xh","Дом",5000000,120,
  "Отдельный дом (гостиная + кухня + 1 спальня/1 с/у + двор), без мебели, ул. Mê Linh, Phường 9, рядом с Bách Hóa Xanh и спортзалом, 10 мин до озера Xuân Hương.",
  "https://www.facebook.com/marketplace/item/1372181211516644/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"минимум 1 год","contact":"продавец Hương Mai (та же, что и объявление №527)"}),

L(530,"da-lat","lv","Комната",15750000,None,
  "Номер в формате resort-living с видом на сосны — wifi, уборка 2 раза в неделю, парковка, вода включена, ресторан на территории, свет отдельно. Рассчитано на экспатов и удалёнщиков.",
  "https://www.facebook.com/marketplace/item/1052881520557817/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"минимум 6 месяцев, депозит 1 месяц, оплата раз в 2 месяца вперёд","notice":"точный район не указан в объявлении, данные со страницы поиска","contact":"продавец Samsara Lê (на FB с 2025)"}),

L(531,"da-lat","xh","Квартира",15000000,60,
  "2-спальная квартира (1 с/у) с балконом и видом, полностью меблирована, Phường 6, рядом с Bách Hóa Xanh и школой Lam Sơn, 2,5 км до Ночного рынка.",
  "https://www.facebook.com/marketplace/item/1379400014146019/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"6-12 месяцев","notice":"⚠ на карточке FB отображается цена 1 500 000 ₫ — баг ввода цены, в описании указано 15 000 000 ₫/мес.","contact":"продавец Ngân Go Home (на FB с 2025)"}),

L(532,"nha-trang","vn","Дом",25000000,100,
  "Новый дом на 3 спальни/4 с/у с двором, район Vĩnh Thái / КГТ Mỹ Gia, юг города.",
  "https://www.facebook.com/marketplace/item/1335062435448184/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на FB объявление помечено тегом «Đà Lạt, Lâm Đồng», но в самом тексте описания указаны Vĩnh Thái и КГТ Mỹ Gia — это реальные районы Нячанга, а не Далата. Похоже на неверную привязку города продавцом; в подборке отнесено к Нячангу по содержанию объявления. На карточке FB отображается цена 2 500 000 ₫ — баг ввода цены, в описании указано 25 000 000 ₫/мес.","contact":"продавец Ngan Hong Pham (на FB с 2018, высокий рейтинг)"}),

L(533,"da-nang","cl2","Комната",4000000,25,
  "Комната (269 кв. фут, ~20 м² без балкона) по адресу 16A-18A Nguyễn Quý Đức, Khuê Trung, Cẩm Lệ, рядом с мостом Nguyễn Tri Phương, новое 4-этажное здание с лифтом и электронными воротами.",
  "https://www.facebook.com/marketplace/item/1057757783316746/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"кондиционер, отопление, прачечная, парковка","notice":"цена варьируется 4-5 млн ₫ в зависимости от типа комнаты; только долгосрочным арендаторам","contact":"продавец Homebird Apt (на FB с 2026)"}),

L(534,"da-nang","hx","Квартира",7500000,None,
  "1-спальная квартира (1 с/у) в престижном комплексе, ул. Nguyễn Hiến Lê, район Hòa Cường, полностью меблирована (диван, обеденная группа, бельё), своя стиральная машина, кондиционер в гостиной и спальне.",
  "https://www.facebook.com/marketplace/item/911416194738049/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"доступна для заселения сейчас","contact":"продавец Võ Thị Thảo Nguyên (на FB с 2021)"}),

L(535,"da-nang","tk","Квартира",7000000,None,
  "Новая квартира в центре района Thanh Khê, ул. Hà Huy Tập, рядом с Aeon Mall, Coopmart, университетом Duy Tân, полная меблировка, отдельная прачечная, просторный балкон.",
  "https://www.facebook.com/marketplace/item/1576504187188353/","проверено 16 авг",1,source="fbmarketplace",
  details={"contact":"продавец Nguyen Huyen (на FB с 2022)"}),

L(536,"da-nang","tk","Квартира",7500000,None,
  "Полностью меблированная квартира с оборудованной кухней, ул. Điện Biên Phủ, район Thanh Khê.",
  "https://www.facebook.com/marketplace/item/1811352036957325/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"цена договорная","contact":"продавец Nguyễn Thị Mỹ Diệu (на FB с 2026)"}),

L(537,"da-nang","lc","Квартира",4000000,35,
  "Квартира 35 м² на ул. Âu Cơ, район Liên Chiểu.",
  "https://www.facebook.com/marketplace/item/1014448794912255/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на FB объявление помечено категорией «Quận Cẩm Lệ», но в тексте описания указана улица Âu Cơ в Liên Chiểu — расхождение между тегом и текстом, в подборке отнесено к Liên Chiểu по содержанию описания. Само описание минимальное, деталей мало.","contact":"продавец Trần Uyên (на FB с 2010)"}),

L(538,"hoi-an","ha","Квартира",14000000,None,
  "2-спальная квартира F Home, полностью меблирована.",
  "https://www.facebook.com/marketplace/item/1089695737060971/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 1 400 000 ₫ — баг ввода цены, в описании указано 14 000 000 ₫/мес. Объявление всплыло в выдаче по Дананга (радиус поиска 65 км), но фактически находится в Хойане (~30 км от центра Дананга) — в подборке отнесено к Хойану.","contact":"продавец Quyên Lê (на FB с 2015)"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\nMAPS = {"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n]\n\nMAPS = {", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted fbmarketplace listings")
