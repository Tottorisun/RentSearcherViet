# -*- coding: utf-8 -*-
"""Полный обход всех 22 групп Facebook, 9 сентября 2026. Вьетнам и Филиппины.

Проход сделан через личный Chrome владельца (claude-in-chrome): вход в отдельном
профиле `_fb_profile/`, которым ходит fb_collect.py, так и не поднялся — Facebook
не завершал форму входа, и куки `c_user` в профиле нет. Метод — из
fb_groups_howto.md: поиск по группе, разбор JSON из <script>, проверка каждого
поста по прямой ссылке.

ОБОЙДЕНЫ ВСЕ 22 ГРУППЫ: 3 в Думагете, 8 в Себу, 7 в Маниле, по одной в Хошимине,
Нячанге и Дананге плюс коммерческая без города. По Хошимину пришлось искать
отдельно по районам (Тхао Дьен, Фу Ми Хынг, Тхань Да): общий запрос «cho thuê»
выдаёт Куан 3, Тан Бинь и Фу Тхо, а таких районов у нас нет.

ИЗ 43 ОТОБРАННЫХ ДОШЛИ 27.
  * 7 уже были на сайте — сверка по id до проверок сэкономила семь загрузок.
  * 4 оказались снятыми при живой выдаче поиска: квартира на Junquera Extension,
    Victoria Sports Tower, студия в Мангахане и 1BR на Пиапи у Hibbard.
  * 3 живы, но без цены: Тхао Дьен (Đường số 64), студия на Бинь Кыой и
    Congressional Town Center (он ещё и «for sale / for rent»).
  * 2 не удалось честно отнести к району. «Cầu Kinh Thanh Đa — Xô Viết Nghệ Tĩnh
    — Ung Văn Khiêm» за 4,9 млн: три ориентира сразу, и два из них на материковой
    стороне моста, а наш ключ bq — это сам полуостров. И «Panorama, Nha Trang»
    за 14 млн — в тексте нет ни района, ни площади, ни числа комнат, а
    check_repost.py показал на сайте строку из Телеграма с ТОЙ ЖЕ ценой и с
    адресом «Panorama Empyrean, Hùng Vương, Phước Hòa». То есть район у неё был
    бы выбран мной, а не сказан продавцом, и с приличной вероятностью неверно.

ЛОЖНОЕ «СНЯТО». Пост 28402515499411889 (Гуадалупе, 22 000 ₱) сначала дал пустой
результат: в payload не оказалось текста. Живым его показал ЗАГОЛОВОК страницы —
у живого поста это «... | <начало поста> | Facebook», у снятого просто
«(20+) Facebook». Проверять надо оба признака, иначе живые строки уходят в отсев.

ЧЕГО НЕ ВЗЯЛИ ОСОЗНАННО: Cantil-E, San Jose Extension, Булакао, Бакаян, Банава,
Пит-ос, Лилоан, Яти, Сампалок, Санта-Меса, Тондо, Пако, Санта-Ана, Тхань Ми Тэй,
Кэн 1, Кэн 3, Тан Бинь, Нья Бэ и Тху Дык — районов с такими ключами у нас нет.
Плюс прайс-листы комплексов (Aura Living, Golden Star, City Garden Villas),
rent-to-own (это продажа), объявления «ищу жильё» и три поста Sunshine Sky City:
такая квартира на сайте уже задвоена между Batdongsan и Chợ Tốt, третья копия
сделала бы только хуже.

ФОТОГРАФИЙ НЕТ: ссылки Facebook на изображения подписаны и живут около четырёх
дней.
"""
from listing_lock import insert_listings

IDS = [1000715, 2000549, 2000550, 2000551,
       3000260, 3000261, 3000262, 3000263, 3000264, 3000265, 3000266, 3000267,
       3000268, 3000269, 3000270, 3000271, 3000272, 3000273, 3000274, 3000275,
       3000276, 3000277, 3000278, 3000279, 3000280, 3000281, 3000282]

N_RU = ("Источник — пост в группе Facebook. Точной даты размещения группа не отдаёт: в данных "
        "страницы её нет, а видимые метки времени принадлежат комментариям. Указанный возраст — "
        "это время с проверки: 9 сентября 2026 объявление было открыто по прямой ссылке и "
        "подтверждено живым. Фотографий нет: ссылки Facebook на изображения подписаны и живут "
        "около четырёх дней, смотрите фото по ссылке.")
N_EN = ("Source: a post in a Facebook group. The group gives no exact posting date — it is absent "
        "from the page data, and the visible timestamps belong to comments. The age shown is time "
        "since verification: on 9 September 2026 the post was opened at its permalink and confirmed "
        "live. No photos: Facebook image links are signed and last about four days, so see the "
        "photos on the post.")

NEW_SRC = r'''
L(1000715,"ho-chi-minh","ak","Квартира",22000000,None,
  "Квартира в башне T2 комплекса Masteri Thảo Điền — 2 спальни, 2 санузла. Цена указана как «net», то есть без коммунальных платежей сверху. В комплексе бассейн, спортзал и охрана круглосуточно; на первых этажах Vincom Mega Mall, рядом станция метро Тхао Дьен.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1797240251594698/","сегодня",0,source="fbgroup",
  descEn="A flat in tower T2 of Masteri Thảo Điền — 2 bedrooms, 2 bathrooms. The rent is quoted as net, i.e. with no service charge on top. The complex has a swimming pool, a gym and 24/7 security; Vincom Mega Mall occupies the podium and Thảo Điền metro station is next door.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(2000549,"nha-trang","tl","Квартира",20000000,60,
  "Квартира 60 м² в HUD Building на ул. Нгуен Тхиен Тхуат, 4 — 2 спальни, 2 санузла, гостиная и лоджия, вся мебель новая. Диван раскладывается в спальное место, то есть при необходимости квартира работает как трёхкомнатная. Пешком до пляжа на набережной Чан Фу; вокруг рестораны, кафе, торговые центры и ночной рынок. Срок от 6 до 12 месяцев, депозит два месяца, оплата раз в два месяца.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2050251082475660/","сегодня",0,source="fbgroup",
  descEn="A 60 m² flat in the HUD Building at 4 Nguyễn Thiện Thuật — 2 bedrooms, 2 bathrooms, a living room and a loggia, all furniture new. The sofa converts into a separate bed, so the flat works as a three-bedroom when needed. The Trần Phú seafront is a short walk away, with restaurants, cafés, malls and the night market around. Six to twelve months, two months' deposit, paid every two months.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(2000550,"da-nang","st","Квартира",8000000,None,
  "Квартира на ул. Нгуен Конг Чы, Шон Ча — одна спальня, до трёх человек. Кондиционер, стиральная машина, холодильник, электроплита, посудная мойка, водонагреватель, кровать с матрасом, шкаф, обеденная группа; вай-фай бесплатный. Рядом Драконов мост, университеты, больница, супермаркет и рынок; район не топит. Парковка просторная.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2207281353232857/","сегодня",0,source="fbgroup",
  descEn="A flat on Nguyễn Công Trứ, Sơn Trà — one bedroom, up to three people. Air conditioning, washing machine, fridge, electric hob, sink, water heater, bed with mattress, wardrobe and a dining set; WiFi is free. The Dragon Bridge, universities, a hospital, a supermarket and a market are all nearby, and the area does not flood. Parking is roomy.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(2000551,"da-nang","ah","Квартира",13000000,None,
  "Квартира на ул. Зыонг Динь Нге, Ан Хай — 2 спальни, до четырёх человек. Электричество и вода включены в плату, стиральная машина своя. Лифта в доме нет, животных нельзя; иностранцев берут.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2198260160801643/","сегодня",0,source="fbgroup",
  descEn="A flat on Dương Đình Nghệ, An Hải — 2 bedrooms, up to four people. Electricity and water are included in the rent and the washing machine is private. The building has no lift and pets are not allowed; foreign tenants are welcome.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000260,"dumaguete","pia","Дом",30000,None,
  "Дом в Пиапи, Думагете — 3 спальни с кондиционерами, 2 санузла, в одном ванна. Частичная меблировка, просторная гостиная, с животными можно. Пешком до набережной Boulevard, несколько минут до школ, больниц, торговых центров и автобусных остановок. Договор на год: месяц авансом и два месяца депозита.",
  "https://www.facebook.com/groups/1996683940588782/posts/4542058159384668/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A house in Piapi, Dumaguete — 3 air-conditioned bedrooms and 2 bathrooms, one with a bathtub. Semi-furnished, with a spacious living area, and pets are allowed. The Boulevard is within walking distance, and schools, hospitals, malls and bus stops are a few minutes away. One-year contract: one month advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000261,"dumaguete","pia","Студия",30000,None,
  "Студия в кондоминиуме Marina Spatial, барангай Пиапи, Думагете — шестой этаж, полная меблировка, кровать размера queen, обеденная зона, санузел и полный набор техники. Парковка в подземном этаже. До центра города 10–15 минут.",
  "https://www.facebook.com/groups/1996683940588782/posts/4527164180874066/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A studio in Marina Spatial Condominium, Barangay Piapi, Dumaguete — sixth floor, fully furnished, queen-size bed, dining area, bathroom and a full set of appliances. Parking in the basement. Downtown is 10-15 minutes away.",
  details={"notice":"RU_N2","noticeEn":"EN_N2"}),
L(3000262,"dumaguete","pia","Студия",8500,None,
  "Студия в Пиапи, Думагете — свой санузел, кухонная мойка со шкафами, задняя дверь в прачечную зону, двухъярусная кровать, мини-холодильник, стол со стульями, вентилятор, вай-фай бесплатный. Свои счётчики воды и электричества, свой водяной насос, решётки и москитные сетки на окнах, видеонаблюдение, аварийное освещение и датчик дыма, солнечные фонари, общий балкон. Стоит внутри закрытого семейного двора с большой парковкой, тихо и продувается. На двоих взрослых, гостей пускают. Рядом стадион Силлиман и медцентр SUMC.",
  "https://www.facebook.com/groups/1996683940588782/posts/4524907314433086/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A studio in Piapi, Dumaguete — its own bathroom, a kitchen sink with cabinets, a back door to the laundry area, a double-deck bed, a mini fridge, table and chairs, a wall fan and free WiFi. Its own water and electricity meters, its own water booster pump, window grilles and screens, CCTV, emergency lighting and a smoke detector, solar lights and a shared balcony. It sits inside a gated family compound with a large parking lot, quiet and airy. Good for two adults; visitors are allowed. Silliman ballfield and the SUMC medical centre are close by.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000263,"cebu","tis","Квартира",18000,None,
  "Квартира на границе Тисы и Лабангона, Себу — 2 спальни, без мебели. Парковочное место рядом с домом за 1 000 ₱ в месяц, животных нельзя. Рядом университет CIT-U и центр GERTC Labangon, одна поездка до USC, USJ-R, UC, UV и MHAM. Договор от года: два месяца депозита и месяц авансом.",
  "https://www.facebook.com/groups/993673090964916/posts/3076351556030382/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A flat on the Tisa-Labangon boundary in Cebu City — 2 bedrooms, unfurnished. A parking slot near the building costs PHP 1,000 a month; no pets. CIT-U and GERTC Labangon are nearby, and USC, USJ-R, UC, UV and MHAM are one ride away. One-year minimum: two months deposit and one month advance.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000264,"cebu","mac","Дом",60000,133,
  "Двухэтажный дом 133 м² в посёлке Astele, Буйонг Роуд, Лапу-Лапу — 4 спальни, включая большую хозяйскую с телевизором, 3 санузла, комната для прислуги со своим санузлом, балкон, навес для машины, мини-бар. Полная меблировка: кондиционеры, быстрый интернет, телевизоры, холодильник, плита. Участок 150 м². Договор от года: месяц авансом, два депозита.",
  "https://www.facebook.com/groups/993673090964916/posts/3072642076401330/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A two-storey 133 m² house in Astele Subdivision, Buyong Road, Lapu-Lapu — 4 bedrooms including a large master with a TV, 3 bathrooms, a maid's room with its own bathroom, a balcony, a carport and a mini bar. Fully furnished: air conditioning, high-speed WiFi, televisions, fridge and cooking range. Lot area 150 m². One-year minimum: one month advance, two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000265,"cebu","gua","Квартира",30000,None,
  "Квартира в Гуадалупе, Себу — 3 спальни, 4 санузла, просторная кухня с хозяйственной зоной, прачечная, кладовая, место на одну машину. Территория закрытая, с видеонаблюдением. Без мебели, животных нельзя. Месяц авансом и два месяца депозита.",
  "https://www.facebook.com/groups/994303254903669/posts/1804356743898312/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A flat in Guadalupe, Cebu City — 3 bedrooms, 4 bathrooms, a large kitchen with a service area, a laundry area, a storage room and parking for one car. The property is gated with CCTV. Unfurnished, no pets. One month advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000266,"cebu","tis","Дом",35000,250,
  "Двухэтажный дом 250 м² в закрытом посёлке в Тисе, Себу — 4 спальни, 3 санузла, полная меблировка, вид на город и горы. На территории посёлка корт для пиклбола. Участок 150 м².",
  "https://www.facebook.com/groups/994303254903669/posts/1807967166870603/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A two-storey 250 m² house in a private subdivision in Tisa, Cebu City — 4 bedrooms, 3 bathrooms, fully furnished, with city and mountain views. The subdivision has its own pickleball court. Lot area 150 m².",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000267,"cebu","gua","Квартира",14000,None,
  "Квартира 25–30 м² в районе Water Network на Монтеразас Роуд, Гуадалупе, Себу — спальня, санузел, без мебели, до четырёх человек. Двор закрыт воротами, парковка платная. Освобождается в октябре. Рядом Puregold Guadalupe, Robinsons Casa Mira, торговый центр One Pavilion и церковь Гуадалупе. Договор от года: два месяца депозита и месяц авансом.",
  "https://www.facebook.com/groups/994303254903669/posts/1810852693248717/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A 25-30 m² flat in the Water Network area on Monterazas Road, Guadalupe, Cebu City — one bedroom, one bathroom, unfurnished, up to four people. The compound is gated and parking is paid. Free from October. Puregold Guadalupe, Robinsons Casa Mira, One Pavilion Mall and Guadalupe Church are nearby. One-year minimum: two months deposit and one month advance.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000268,"cebu","mac","Квартира",15000,None,
  "Квартира в комплексе Plumera Mactan, Лапу-Лапу — полная меблировка, заезжать можно сразу. В цену включены взносы кондоминиума. До университета Indiana Aerospace 700 м, до больницы Mactan Doctors 1,2 км, до торгового центра Gaisano Grand 1,7 км.",
  "https://www.facebook.com/groups/994303254903669/posts/1811929839807669/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A flat in Plumera Mactan, Lapu-Lapu City — fully furnished and ready to move into. Condo dues are included in the rent. Indiana Aerospace University is 700 m away, Mactan Doctors Hospital 1.2 km, and Gaisano Grand Mall 1.7 km.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000269,"cebu","lah","Квартира",65000,None,
  "Квартира в первой башне Marco Polo Residences, Себу — 3 спальни, 3 санузла, парковочное место, интернет. Взносы кондоминиума оплачиваются отдельно. Срок 6 или 12 месяцев.",
  "https://www.facebook.com/groups/3914645581932487/posts/28400246309612407/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A flat in Marco Polo Residences Tower 1, Cebu City — 3 bedrooms, 3 bathrooms, a parking slot and internet. Condo dues are paid separately. Lease of six or twelve months.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000270,"cebu","tls","Студия",5500,None,
  "Студия в Талисае, Себу — своя кухонная мойка, свой санузел, отдельные счётчики воды и электричества, парковка для мотоцикла. Только для взрослых, животных нельзя. Одна поездка до IT Park, площади Fuente Osmeña и медцентра Vicente Sotto. Свободна одна квартира; месяц авансом и два месяца депозита, просмотр по записи за сутки.",
  "https://www.facebook.com/groups/652674525365824/posts/2111831782783417/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A studio in Talisay, Cebu — its own kitchen sink, its own bathroom, separate water and electricity submeters and motorcycle parking. Adults only, no pets. IT Park, Fuente Osmeña and the Vicente Sotto medical centre are each one ride away. One unit is free; one month advance and two months deposit, viewing by appointment a day ahead.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000271,"cebu","tls","Квартира",15000,None,
  "Новая квартира на Мансуэто Роуд, Табунок, Талисай — спальня, свой санузел, место для машины. Вода включена в плату. Стоит у шоссе, рядом Gaisano, Robinsons (STC), банки и Mr. DIY.",
  "https://www.facebook.com/groups/652674525365824/posts/2115687289064533/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A new flat on Mansueto Road, Tabunok, Talisay City — one bedroom, its own bathroom and a car space. Water is included in the rent. It stands by the highway, with Gaisano, Robinsons (STC), banks and Mr. DIY nearby.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000272,"cebu","gua","Квартира",22000,None,
  "Квартира в Гуадалупе, Себу — 2 спальни, из мебели двухъярусная кровать и шкаф, парковка только для мотоцикла. Одна поездка до площади Fuente, улицы Колон и торгового центра Ayala; рядом больницы. Месяц авансом и два месяца депозита, просмотр по записи за сутки.",
  "https://www.facebook.com/groups/cebu.tambayan.2/posts/28402515499411889/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A flat in Guadalupe, Cebu City — 2 bedrooms, furnished with a double-deck bed and a cabinet, motorcycle parking only. Fuente, Colon and Ayala Mall are each one ride away, and hospitals are close. One month advance and two months deposit, viewing by appointment a day ahead.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000273,"cebu","itp","Студия",18000,None,
  "Студия в башне 2 комплекса Avida Towers Cebu IT Park — пятый этаж, частичная меблировка. Взносы кондоминиума включены в плату. Животных не разрешает управляющая компания. Пять минут пешком до Ayala Central Bloc, рынка Sugbo Mercado и автостанции. Месяц авансом и два месяца депозита.",
  "https://www.facebook.com/groups/563896434149922/posts/2355696241636590/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A studio in tower 2 of Avida Towers Cebu IT Park — fifth floor, semi-furnished. Condo dues are included in the rent. Pets are not allowed by building management. Ayala Central Bloc, Sugbo Mercado and the bus terminal are a five-minute walk away. One month advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000274,"manila","qzc","Квартира",25000,58,
  "Двухуровневая квартира 58 м² в Xavier Hills Condominium на углу улиц Н. Доминго и Гранада, Кесон-Сити — 2 спальни, 2 санузла, большая кухня, кладовая и прачечная зона, до 3–4 человек. Дом свежепокрашен, в комплексе бассейн и охрана круглосуточно. Парковки нет. Пешком до Robinsons Magnolia, рядом станция Gilmore и Santolan Town Plaza; до Мандалуйонга 10 минут, до Макати полчаса. Договор от года с постдатированными чеками: месяц авансом и два месяца депозита.",
  "https://www.facebook.com/groups/299437881275577/posts/1728741158345235/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A 58 m² loft flat in Xavier Hills Condominium at N. Domingo corner Granada, Quezon City — 2 bedrooms, 2 bathrooms, a big kitchen, a storage room and a laundry area, for three to four people. Newly painted, with a swimming pool and 24/7 security in the building. No parking. Robinsons Magnolia is a walk away, Gilmore station and Santolan Town Plaza are close, Mandaluyong is 10 minutes and Makati about 30. One-year lease with post-dated cheques: one month advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000275,"manila","qzc","Студия",22000,30,
  "Студия 30,2 м² с балконом в башне 1 комплекса Manhattan Plaza, Кубао, Кесон-Сити — шестнадцатый этаж, полная меблировка. В цену включены взносы кондоминиума. Из обстановки: телевизор Samsung 55 дюймов, инверторные кондиционер и холодильник, двуспальная кровать с ящиками, раскладной диван, обеденный стол на двоих, стойка для одежды, плотные шторы, зеркало в рост. Кухня с вытяжкой, индукционной плитой и микроволновкой, посуда и утварь на месте; в санузле водонагреватель и биде. В доме спортзал, бассейн с душевыми, сад, игровая комната и детская площадка. До трёх человек, срок от года.",
  "https://www.facebook.com/groups/299437881275577/posts/1783011332918217/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A 30.2 m² studio with a balcony in Manhattan Plaza Tower 1, Cubao, Quezon City — sixteenth floor, fully furnished, association dues included in the rent. It comes with a 55-inch Samsung TV, inverter air conditioner and fridge, a double bed with under-bed storage, a foldable sofa bed, a dining table for two, a clothes rack, blackout curtains and a full-body mirror. The kitchen has a range hood, an induction hob and a microwave, with plates, utensils and cookware; the bathroom has a water heater and a bidet. The building has a gym, a pool with showers, a garden, a game room and a playground. Up to three occupants, one-year minimum.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000276,"manila","qzc","Квартира",27000,32,
  "Квартира 32 м² в Infina Towers на бульваре Аврора, Кубао, Кесон-Сити — спальня, сороковой этаж северного корпуса, окна во двор с зонами отдыха, частичная меблировка. Рядом станция LRT-2 Anonas, больницы World Citi и Quirino, недалеко университеты Ateneo de Manila и UP Diliman. Срок от 12 месяцев: два месяца депозита и месяц авансом, оплата постдатированными чеками.",
  "https://www.facebook.com/groups/1972633726399858/posts/4398397977156742/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A 32 m² flat in Infina Towers on Aurora Blvd., Cubao, Quezon City — one bedroom, fortieth floor of the north building, facing the amenity deck, semi-furnished. LRT-2 Anonas station, World Citi and Quirino medical centres are nearby, with Ateneo de Manila and UP Diliman not far. Twelve-month minimum: two months deposit and one month advance, paid by post-dated cheque.",
  details={"notice":"RU_N3","noticeEn":"EN_N3"}),
L(3000277,"manila","ort","Квартира",25000,90,
  "Двухэтажная квартира 90 м² в Villa Alegre, Пинагбухатан, Пасиг — 2 спальни со встроенными шкафами, санузел, просторная прачечная зона, место для машины, в хозяйской спальне свой балкон. Сдаётся без отделки и мебели. Пешком до рынков, рядом общественный транспорт, недалеко деловые районы Пасига. Два месяца депозита и два месяца авансом.",
  "https://www.facebook.com/groups/995479814463151/posts/2013255359352253/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A two-storey 90 m² flat in Villa Alegre, Pinagbuhatan, Pasig — 2 bedrooms with built-in cabinets, one bathroom, a spacious laundry area, a parking space, and a private balcony off the master bedroom. Let bare. Markets are within walking distance, public transport is at hand and Pasig's business districts are a short commute. Two months deposit and two months advance.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000278,"manila","mdl","Квартира",25000,None,
  "Квартира в Pioneer Woodlands на углу EDSA и улицы Pioneer, Мандалуйонг — 2 спальни, полная меблировка (раньше сдавалась посуточно). Взносы кондоминиума 3 522 ₱ в месяц платит арендатор, парковочное место в цену не входит. Одно животное разрешено. Дом напротив станции MRT Boni, рядом Light Mall, башня Globe, Cybergate 3 и офисы Accenture и Sitel. Срок от года: месяц депозита и месяц авансом.",
  "https://www.facebook.com/groups/715451165293916/posts/3424627771042895/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A flat in Pioneer Woodlands at EDSA corner Pioneer St., Mandaluyong — 2 bedrooms, fully furnished (previously let nightly). The tenant pays association dues of PHP 3,522 a month and no parking slot is included. One pet is allowed. The building faces MRT Boni station, with Light Mall, Globe Tower, Cybergate 3 and the Accenture and Sitel offices nearby. One-year minimum: one month deposit and one month advance.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000279,"manila","mdl","Дом",40000,None,
  "Четырёхэтажный таунхаус в Bamboo Grove Residences, барангай Плейнвью, Мандалуйонг — 3 спальни, 2 санузла, частичная меблировка, в двух комнатах кондиционеры, свой бак для воды, кухня со встроенной техникой и вытяжкой, парковка. Посёлок закрытый, охрана круглосуточно, с животными можно. В цену включены взносы товарищества. До Rockwell 5 минут, до площади Мандалуйонга 2 минуты на машине; рядом Макати, BGC и Ортигас. Месяц авансом и два месяца депозита.",
  "https://www.facebook.com/groups/715451165293916/posts/3382349201937419/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A four-storey townhouse in Bamboo Grove Residences, Brgy. Plainview, Mandaluyong — 3 bedrooms, 2 bathrooms, semi-furnished with air conditioning in two rooms, its own water tank, a fitted kitchen with a range hood, and parking. The community is gated with 24/7 security and pets are welcome. Association dues are included in the rent. Rockwell is five minutes away and Mandaluyong Circle a two-minute drive, with Makati, BGC and Ortigas close by. One month advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000280,"manila","mla","Комната",6500,None,
  "Комната-студия в здании PAW на ул. Сан-Андрес, 1117, Малате, Манила (барангай 743, зона 80) — третий этаж, сдаётся без мебели. Свой санузел и раковина, свои счётчики Maynilad и Meralco. С животными и с детьми можно, дети считаются в число жильцов; гостей пускают, ночевать им нельзя. Парковки нет, только вдоль тротуара; крупную технику — холодильник, стиральную машину, кондиционер — ставить не разрешают. На двоих. Дом стоит напротив вторых ворот школы St Anthony, над пекарней Red Ribbon и рядом с Chowking; до станции LRT Quirino 5–10 минут пешком. Два месяца депозита, месяц авансом, договор на год с продлением.",
  "https://www.facebook.com/groups/1972633726399858/posts/4398052960524577/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A bare studio room in the PAW Building at 1117 San Andres St., Malate, Manila (Barangay 743, Zone 80) — third floor. It has its own bathroom and sink and its own Maynilad and Meralco submeters. Pets and children are allowed, with children counted in the headcount; visitors may come but not stay overnight. There is no parking beyond the sidewalk, and large appliances - fridge, washing machine, air conditioner - are not permitted. Good for two. The building faces the second gate of St Anthony school, above the Red Ribbon bakeshop and beside Chowking, a 5-10 minute walk from LRT Quirino station. Two months deposit, one month advance, a renewable one-year contract.",
  details={"notice":"RU_N4","noticeEn":"EN_N4"}),
L(3000281,"manila","mla","Квартира",25000,None,
  "Квартира в The Camden Place, Малате, Манила — одна спальня, полная меблировка. Владелец сдаёт напрямую и просит агентов не обращаться. Пешком до университета De La Salle, колледжа Saint Benilde и колледжа St. Scholastica, до станции LRT-1 Vito Cruz; проспект Тафт и улица П. Окампо рядом — оттуда идут джипни, маршрутки и автобусы. Поблизости торговый центр R Square, University Mall, супермаркеты Weshop и Fortunes Mart, прачечные, клиника Adventist Medical Center, отделения BDO, BPI и Metrobank, спортзал Anytime Fitness. Месяц авансом и два месяца депозита.",
  "https://www.facebook.com/groups/1972633726399858/posts/4403087026687837/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A flat in The Camden Place, Malate, Manila — one bedroom, fully furnished. The owner lets directly and asks agents not to enquire. De La Salle University, College of Saint Benilde and St. Scholastica's College are within walking distance, as is LRT-1 Vito Cruz; Taft Avenue and P. Ocampo Street are the arteries for jeepneys, UV Express vans and buses. R Square Mall, University Mall, the Weshop and Fortunes Mart groceries, laundromats, the Adventist Medical Center, BDO, BPI and Metrobank branches and an Anytime Fitness gym are all close. One month advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000282,"manila","mak","Квартира",30000,40,
  "Квартира 40 м² в Antel Serenity Suites на ул. Саламанка, Побласьон, Макати — 2 спальни, тридцать первый этаж, балкона нет. Срок от года, оплата по схеме «два плюс один».",
  "https://www.facebook.com/groups/1319639041431566/posts/28554200947548674/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A 40 m² flat in Antel Serenity Suites on Salamanca St., Poblacion, Makati — 2 bedrooms, thirty-first floor, no balcony. One-year minimum, on two-plus-one terms.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
'''

# Оговорки, которые касаются одной строки, а не всей партии.
N_RU2 = N_RU + (" Владелец сдаёт эту студию и посуточно — 1 800 ₱ за ночь плюс 350 ₱ за уборку; "
                "на сайте записана месячная цена по годовому договору.")
N_EN2 = N_EN + (" The owner also lets this studio nightly - PHP 1,800 a night plus a PHP 350 "
                "cleaning fee; the monthly rate on a one-year contract is what is recorded here.")
N_RU3 = N_RU + (" В заголовке объявления площадь указана как 31 м², а в списке характеристик — "
                "32 м²; записана вторая. Уточняйте при обращении.")
N_EN3 = N_EN + (" The ad's headline says 31 m² while its own details say 32 m²; the latter is "
                "what is recorded. Confirm when you enquire.")
N_RU4 = N_RU + (" В объявлении несколько комнат: за 6 500 ₱ свободны две (одна с антресолью), "
                "комнаты за 7 000 и 8 000 ₱ помечены как сданные.")
N_EN4 = N_EN + (" The ad covers several rooms: two are free at PHP 6,500 (one with a deck), while "
                "the PHP 7,000 and PHP 8,000 rooms are marked taken.")

for _tag, _val in (("RU_N2", N_RU2), ("EN_N2", N_EN2), ("RU_N3", N_RU3), ("EN_N3", N_EN3),
                   ("RU_N4", N_RU4), ("EN_N4", N_EN4), ("RU_N", N_RU), ("EN_N", N_EN)):
    NEW_SRC = NEW_SRC.replace(_tag, _val)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
