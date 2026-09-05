# -*- coding: utf-8 -*-
"""Филиппины из Facebook Marketplace, 5 сентября 2026: 44 объявления, весь диапазон цен.

Почему в прошлые разы выходило мало. Лента Marketplace обрывается на 24 карточках
и дальше не догружается, сколько её ни листай -- это не наша ошибка сбора, а
потолок самой ленты. Обходится ценовыми полосами: каждая полоса (?minPrice=&maxPrice=)
отдаёт свои 24 самых свежих. Девять полос на город вместо одной ленты -- и вместо
24 карточек по Себу их стало под две сотни.

Вторая ловушка: лента виртуализирована, карточки, ушедшие за экран, удаляются из
DOM. Одноразовый съём после прокрутки систематически недосчитывает; нужен
накопитель, снимающий DOM по таймеру во время прокрутки.

ВОЗРАСТ. Полосы шли с sortBy=creation_time_descend, но без фильтра по дате, а он
и есть единственное честное основание для «не старше N дней». Поэтому каждое
объявление отдельно проверено повторным проходом той же полосы с
daysSinceListed=30: если оно там осталось -- 30 дней это доказанная верхняя
граница. У пяти объявлений Facebook показал точный возраст, у них он и стоит.
Одно (Apple One Banawa, 25 000 ₱) подтвердить не удалось -- полоса обрезается на
24 карточках, и отсутствие ничего не доказывает; оно выброшено, а не заведено с
выдуманной датой. Вместе с ним убран район Банава, который остался бы пустым.

ЧТО ОТСЕЯНО. Продажи под видом аренды («Stop renting and start owning» в
Oriental Residences -- два объявления, дом на Boni Ave с «monthly amortization»),
посуточная сдача под видом месячной (Sunvida Tower, 2 300 ₱ ОКАЗАЛИСЬ ЗА НОЧЬ),
участок 6 980 м² под склад в Калабнугане (не жильё), объявления со сломанной
ценой (PHP3, PHP20, PHP9), клоны одного продавца без адреса («2k package na
naanay tubig og kurente», три штуки) и всё, где нет адреса точнее города:
район на сайте должен браться из текста, а не угадываться.

РАЙОН. Facebook снова врал: 1081036401124983 помечен Думагете -- по тексту
Баконг; 28486934477660811 помечен Думагете -- по тексту Сибулан. Район везде из
адреса в тексте объявления.

ФОТО. Ссылки Facebook на изображения подписаны и живут около четырёх дней,
поэтому фотографий здесь нет намеренно -- иначе на карточках остались бы битые
картинки. Значит, эти строки не проходят порог телеграм-хаба в 3 фото и живут
только на сайте.
"""
from listing_lock import insert_listings

IDS = list(range(3000182, 3000226))

N_RU = ("Источник — Facebook Marketplace. Точной даты размещения Facebook для этого формата не "
        "публикует; 30 дней — проверенная верхняя граница: объявление осталось в выдаче при "
        "фильтре «не старше 30 дней». Фотографий нет: ссылки Facebook на изображения подписаны "
        "и живут около четырёх дней, смотрите фото по ссылке.")
N_EN = ("Source: Facebook Marketplace. Facebook publishes no exact posting date for this format; "
        "30 days is a verified upper bound — the ad was still present with the «last 30 days» "
        "filter applied. No photos: Facebook image links are signed and last about four days, so "
        "see the photos on the listing itself.")
D_RU = ("Источник — Facebook Marketplace, возраст показан самим Facebook. Фотографий нет: ссылки "
        "Facebook на изображения подписаны и живут около четырёх дней, смотрите фото по ссылке.")
D_EN = ("Source: Facebook Marketplace; the age is the one Facebook itself displays. No photos: "
        "Facebook image links are signed and last about four days, so see the photos on the "
        "listing itself.")
P125_RU = (N_RU + " В поле цены Facebook у этого объявления стоит «125», а в тексте владельца — "
           "125 000 ₱ в месяц; здесь взята цена из текста.")
P125_EN = (N_EN + " Facebook's price field reads «125» on this ad, while the owner's own text says "
           "PHP 125,000 a month; the figure here is taken from the text.")
P5K_RU = (N_RU + " В карточке Facebook цена стоит как 4 999 ₱, в тексте объявления — 5 000 ₱; "
          "здесь взята цена из текста.")
P5K_EN = (N_EN + " Facebook's card shows PHP 4,999 while the ad's own text says PHP 5,000; the "
          "figure here is taken from the text.")
B5_RU = (N_RU + " В заголовке объявления написано «5 спален», а в описании — три; здесь взято "
         "описание.")
B5_EN = (N_EN + " The ad's headline says «5 bedroom» while its own description says three; the "
         "description is what is used here.")

NEW_SRC = r'''
L(3000182,"dumaguete","jnb","Квартира",15000,45,
  "2-спальная квартира 45 м² (дверь 2) в посёлке Sto. Rosario Heights, Хуноб, Думагете — без мебели, в каждой спальне новый кондиционер, 1 санузел, просторная постирочная с летней кухней, навес для небольшой машины. Свежая покраска и мелкий ремонт. До LP Hypermart 5 минут на транспорте. Счётчик отдельный, электричество и вода сверх аренды. Договор от года, месяц авансом и месяц депозита. С животными нельзя, субаренда запрещена, максимум 4–5 человек. Собственник просит агентов не обращаться.",
  "https://www.facebook.com/marketplace/item/1628504552247223/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Two-bedroom flat, 45 m² (Door 2), in Sto. Rosario Heights Subdivision, Junob, Dumaguete — unfurnished, a brand-new air conditioner in each bedroom, one bathroom, a spacious laundry area with an outdoor kitchen, and a carport for a small car. Freshly painted with minor renovations. Five minutes' ride from LP Hypermart. Separate meter; electricity and water on top of the rent. A year minimum, one month in advance and one month deposit. No pets, no subleasing, four to five people maximum. The owner asks agents not to enquire.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000183,"dumaguete","bcg","Дом",18000,None,
  "Дом с полной меблировкой в посёлке Richwood Homes, Исуган, Баконг — 2 спальни, 2 санузла с горячей и холодной водой, смарт-телевизор, интернет, холодильник, кулер с горячей и холодной водой. На территории бассейн, баскетбольная площадка и круглосуточная охрана.",
  "https://www.facebook.com/marketplace/item/1081036401124983/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Fully furnished house in Richwood Homes, Isugan, Bacong — 2 bedrooms, 2 bathrooms with hot and cold showers, a smart TV, wifi, a fridge and a hot-and-cold water dispenser. The grounds have a swimming pool, a basketball court and 24-hour security.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000184,"dumaguete","bnd","Дом",35000,None,
  "Дом в Баниладе, Думагете — 2 комнаты, 2 санузла, полная меблировка, вдоль бетонной дороги.",
  "https://www.facebook.com/marketplace/item/1028754236864535/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="House in Banilad, Dumaguete — 2 rooms, 2 bathrooms, fully furnished, along a concrete road.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000185,"dumaguete","val","Квартира",27000,None,
  "Большая квартира (юнит N10) на первом этаже в Latino Apartments, Бонг-ао, на границе Валенсии и Думагете. Подробностей владелец не приводит — всё при осмотре.",
  "https://www.facebook.com/marketplace/item/875770082133528/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Large ground-floor flat (unit N10) at Latino Apartments, Bong-ao, on the Valencia–Dumaguete boundary. The owner gives no further detail; everything is shown on viewing.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000186,"dumaguete","val","Дом",27000,None,
  "Дом в Валенсии — 2 спальни (в одной кондиционер), 2 санузла (в одном горячая и холодная вода), интернет, участок полностью в заборе с воротами, крытый гараж. Свободен с 22 сентября 2026 года.",
  "https://www.facebook.com/marketplace/item/923413987020326/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="House in Valencia — 2 bedrooms (one with air conditioning), 2 bathrooms (one with a hot-and-cold shower), an internet connection, fully fenced and gated, with a covered garage. Available from 22 September 2026.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000187,"dumaguete","sib","Дом",18000,None,
  "Новый дом в Кампаклане, Сибулан — 3 спальни, 1 санузел, небольшой балкон, рядом шоссе. Ориентир: начальная школа Магсайсай.",
  "https://www.facebook.com/marketplace/item/28486934477660811/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Newly built house in Campaclan, Sibulan — 3 bedrooms, 1 bathroom, a small balcony, close to the highway. Landmark: Magsaysay Elementary School.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000188,"dumaguete","bcg","Квартира",30000,None,
  "Квартира с полной меблировкой в Баконге, Негрос-Ориенталь — до пляжа несколько шагов. 3 спальни, 3 санузла, кондиционеры и потолочные вентиляторы по всей квартире. Тихий район, рядом магазины, кафе и транспорт. Сдаёт лицензированный брокер.",
  "https://www.facebook.com/marketplace/item/866182099795218/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Fully furnished flat in Bacong, Negros Oriental — a few steps from the beach. Three bedrooms, three bathrooms, air conditioning and ceiling fans throughout. A quiet neighbourhood with shops, cafés and transport nearby. Let by a licensed broker.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000189,"dumaguete","val","Комната",3000,None,
  "Комната на втором этаже в конце улицы Palmey Way, Западный Балабаг, Валенсия — на одного, свободны две. Санузел общий. Вода, электричество и интернет включены (электричество — на вентилятор, свет и мелкую технику). В доме солнечные панели, поэтому при отключениях свет обычно есть. Месяц авансом и 1 000 ₱ депозита. Гости только с 9 до 18 и по одному.",
  "https://www.facebook.com/marketplace/item/1382504990045693/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Second-floor room at the end of Palmey Way, West Balabag, Valencia — single occupancy, two rooms free. Shared bathroom. Water, electricity and wifi included (electricity covers a fan, lights and small personal devices). The house runs a solar system, so there is usually power during a brownout. One month in advance and a PHP 1,000 deposit. Visitors between 9am and 6pm only, one at a time.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000190,"dumaguete","dau","Дом",125000,None,
  "Дом на первой линии пляжа в Дауине — 5 спален, 4 санузла, полная меблировка. Наверху три комнаты, в хозяйской своя ванная с ванной и гардеробная; внизу две, в одной свой санузел со шкафами. Закрытая территория с видеонаблюдением и охраной, своя скважина с насосной станцией, центральный бойлер, интернет Starlink, генератор. В аренду входят садовник трижды в неделю и помощница дважды. Рассчитан на семью или долгий срок.",
  "https://www.facebook.com/marketplace/item/2762643574138084/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Beachfront house in Dauin — 5 bedrooms, 4 bathrooms, fully furnished. Three rooms upstairs, the master with an ensuite, a bathtub and a walk-in closet; two downstairs, one with its own bathroom and cabinets. Inside a secure compound with CCTV and a guard on duty, with its own deepwell and pressure tank, a central hot-water tank, free Starlink wifi and a generator. A gardener three times a week and a helper twice a week are included. Suited to families or a long let.",
  details={"notice":"RU_P125","noticeEn":"EN_P125"}),
L(3000191,"dumaguete","cdy","Дом",25000,None,
  "Таунхаус в Кандау-ай, Думагете — 2 спальни, санузел с душем, полная меблировка, встроенные шкафы, небольшой сад, крытая летняя кухня. Кондиционер, место под стирку, парковка. До центра и колледжа DCC 10 минут. Договор от года, месяц авансом и месяц депозита.",
  "https://www.facebook.com/marketplace/item/1024416883934083/","4 дня назад",4,source="fbmarketplace",cur="PHP",
  descEn="Townhouse in Candau-ay, Dumaguete — 2 bedrooms, a toilet-and-shower room, fully furnished, with built-in cabinets, a small garden and an extended dirty kitchen. Air conditioning, a laundry area and parking. Ten minutes to downtown and to DCC. A year minimum, one month in advance and one month deposit.",
  details={"notice":"RU_D","noticeEn":"EN_D"}),
L(3000192,"dumaguete","val","Квартира",25000,None,
  "Новая квартира в Валенсии — 3 просторные спальни (одна на первом этаже), 2 санузла (по одному на этаж), полная меблировка, кондиционеры, участок в заборе с воротами, большая парковка. Вода бесплатно. Рядом школа, до площади Валенсии 5 минут, до Думагете 15. Месяц авансом и месяц депозита. Без мебели — 18 000 ₱.",
  "https://www.facebook.com/marketplace/item/949266157494624/","4 дня назад",4,source="fbmarketplace",cur="PHP",
  descEn="Brand-new flat in Valencia — 3 spacious bedrooms (one on the ground floor), 2 bathrooms (one per floor), fully furnished, air-conditioned, fenced and gated with generous car parking. Water is free. A school is nearby, Valencia plaza is five minutes away and Dumaguete fifteen. One month in advance and one month deposit. Unfurnished it is PHP 18,000.",
  details={"notice":"RU_D","noticeEn":"EN_D"}),
L(3000193,"dumaguete","bcg","Квартира",45000,None,
  "Квартира в Баконге — 3 спальни, 4 санузла. Свободна с 4 сентября 2026 года. Больше подробностей владелец не приводит.",
  "https://www.facebook.com/marketplace/item/1043794735218757/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Flat in Bacong — 3 bedrooms, 4 bathrooms. Available from 4 September 2026. The owner gives no further detail.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000194,"dumaguete","sib","Дом",30000,None,
  "Таунхаус с полной меблировкой в Orient Wood Residences, Сибулан. Подробности при осмотре.",
  "https://www.facebook.com/marketplace/item/1044980134836614/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Fully furnished townhouse at Orient Wood Residences, Sibulan. Details on viewing.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000195,"dumaguete","tly","Квартира",25000,None,
  "Квартира с частичной меблировкой в Талае, Думагете — 3 спальни, 2 санузла, свои ворота, гараж на одну машину. До Robinsons Hypermarket 10 минут на машине, до центра Валенсии 5, рядом школа Хуноб и 7-Eleven. Договор от года, два месяца депозита и месяц авансом. Сдаёт лицензированный брокер.",
  "https://www.facebook.com/marketplace/item/3335725303279011/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Semi-furnished flat in Talay, Dumaguete — 3 bedrooms, 2 bathrooms, its own gate and a one-car garage. Ten minutes' drive to Robinsons Hypermarket, five to Valencia proper, with Junob School and a 7-Eleven nearby. A year minimum, two months deposit and one month in advance. Let by a licensed broker.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000196,"dumaguete","bgy","Дом",35000,None,
  "Дом в Багакае, Думагете — 3 спальни, 2 санузла, до рынка и магазинов пешком. Договор на год, два месяца депозита и месяц авансом.",
  "https://www.facebook.com/marketplace/item/1622417932935381/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="House in Bagacay, Dumaguete — 3 bedrooms, 2 bathrooms, within walking distance of the market and shops. A one-year contract, two months deposit and one month in advance.",
  details={"notice":"RU_B5","noticeEn":"EN_B5"}),
L(3000197,"dumaguete","sib","Дом",20000,None,
  "Таунхаус в барангае Тубтубон, Сибулан — 2 спальни, 2 санузла, полная меблировка, кондиционеры, гараж.",
  "https://www.facebook.com/marketplace/item/1103562022342613/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Townhouse in Barangay Tubtubon, Sibulan — 2 bedrooms, 2 bathrooms, fully furnished, air-conditioned, with a garage.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000198,"dumaguete","val","Дом",60000,None,
  "Дом в Липтонге, Валенсия — 3 спальни, в каждой сплит-кондиционер, 2 санузла с горячей и холодной водой. В хозяйской спальне своя ванная и гардеробная. Кухня на заказ с большим количеством шкафов и своим кондиционером, просторные гостиная и столовая, полная меблировка, постирочная со стиральной машиной, крытая веранда, большой сад, накопительный бак для воды, навес для машины. Договор от года.",
  "https://www.facebook.com/marketplace/item/1678814379849965/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="House in Liptong, Valencia — 3 bedrooms, each with a split-type air conditioner, and 2 bathrooms with hot-and-cold showers. The master has an ensuite and a walk-in closet. A custom kitchen with ample storage and its own air conditioner, comfortable sala and dining areas, fully furnished, a laundry room with a washing machine, a covered porch, a spacious green garden, a water storage tank and a carport. A year minimum.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000199,"dumaguete","zmb","Дом",28000,None,
  "Дом на первой линии в Замбоангите — одна спальня с кондиционером и одна комната с вентилятором. Месяц авансом и два месяца депозита.",
  "https://www.facebook.com/marketplace/item/27680729104956729/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Beachfront house in Zamboanguita — one bedroom with air conditioning and one room with a fan. One month in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000200,"cebu","man","Комната",3500,None,
  "Комната в Мандауэ на троих — место для мотоцикла, район не топит. Одна поездка до Ayala, IT Park, SM, Parkmall, Банилада или Консоласьона.",
  "https://www.facebook.com/marketplace/item/1335472455325589/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Room in Mandaue for up to three people — motorcycle parking, and the area does not flood. One ride to Ayala, IT Park, SM, Parkmall, Banilad or Consolacion.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000201,"cebu","col","Комната",5000,None,
  "Комната по адресу 146 C. Padilla St., Себу — напротив школы Don Carlos Gothong. Кровать со шкафом, интернет и вода бесплатно, электричество по счётчику 18 ₱ за кВт·ч. Общие санузел, постирочная и кухонная мойка. Комендантского часа нет, гостей пускают, но не на ночь. На одного-двоих, месяц авансом и месяц депозита.",
  "https://www.facebook.com/marketplace/item/28239435619040678/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Room at 146 C. Padilla St., Cebu City — across from Don Carlos Gothong National High School. Bed frame and cabinet, free wifi and water, electricity submetered at PHP 18 per kWh. Shared bathroom, laundry area and kitchen sink. No curfew; visitors are allowed but cannot stay overnight. For one or two people; one month in advance and one month deposit.",
  details={"notice":"RU_P5K","noticeEn":"EN_P5K"}),
L(3000202,"cebu","tls","Студия",6500,None,
  "Студия в Булакао, Талисай, Себу — максимум на двоих. До Gaisano Tabunok и Robinsons South Town Mall пешком. Бесплатная парковка для мотоцикла и вода MCWD, во дворе фонари на солнечных батареях, на территории видеонаблюдение, ворота закрываются, комендантского часа нет.",
  "https://www.facebook.com/marketplace/item/1622801942576787/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Studio room in Bulacao, Talisay City, Cebu — two people maximum. Walking distance to Gaisano Tabunok and Robinsons South Town Mall. Free motorcycle parking and free MCWD water, solar lights in the yard, CCTV in the compound, a gated entrance and no curfew.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000203,"cebu","bnl","Комната",8000,None,
  "Комната на двоих в Sto. Niño, Банилад, Себу — полная меблировка, санузел общий. Рядом USC-TC, IT Park, Oakridge, Country Mall и UC Banilad. Месяц авансом и два месяца депозита.",
  "https://www.facebook.com/marketplace/item/1057798756659248/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Room for two in Sto. Niño, Banilad, Cebu — fully furnished, with a shared bathroom. Close to USC-TC, IT Park, Oakridge, Country Mall and UC Banilad. One month in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000204,"cebu","lab","Комната",6500,None,
  "Комната на улице Katipunan в Лабангоне, Себу — вдоль дороги, с кондиционером. Ориентир: пожарная часть Лабангона. Владелец сдаёт без детей и без гостей. Месяц авансом и два месяца депозита.",
  "https://www.facebook.com/marketplace/item/1085543573811050/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Room on Katipunan St., Labangon, Cebu — along the road, with air conditioning. Landmark: the Labangon fire station. The owner lets it with no children and no visitors. One month in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000205,"cebu","col","Студия",13000,None,
  "Студия в BLOQ Residences на Сикатуна-стрит, в центре Себу — сдаёт собственник напрямую. Частичная меблировка: кровать с матрасом, шкаф, кондиционер 1,5 л. с. Пешком: до церкви Sacred Heart 3–5 минут, до главного кампуса USC 5–10, до госпиталя Velez 5–10, до главного кампуса UC 15–20. Рядом Cebu Normal University, University of the Visayas и San Jose–Recoletos.",
  "https://www.facebook.com/marketplace/item/2030191750941103/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Studio at BLOQ Residences on Sikatuna Street, in the heart of Cebu City — let directly by the owner. Semi-furnished: bed and mattress, wardrobe, a 1.5 HP air conditioner. On foot: Sacred Heart Parish 3–5 minutes, the USC main campus 5–10, Velez General Hospital 5–10, the UC main campus 15–20. Cebu Normal University, the University of the Visayas and San Jose–Recoletos are all close.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000206,"cebu","mac","Квартира",12000,None,
  "1-спальная квартира без мебели в Mactan Oasis, Лапу-Лапу — из техники только кондиционер. Рядом Mactan Newtown.",
  "https://www.facebook.com/marketplace/item/1553663175908408/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Unfurnished one-bedroom unit inside Mactan Oasis, Lapu-Lapu — air conditioning is the only appliance. Close to Mactan Newtown.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000207,"cebu","gua","Квартира",20000,35,
  "2-спальная квартира 35 м² в Гуадалупе, Себу — частичная меблировка (шкаф и двухъярусная кровать), 1 санузел, стиральная машина, подготовка под оконный кондиционер, одно место на парковке. Можно с животными. До Puregold и Robinsons Supermarket пешком, рядом начальная и старшая школы Гуадалупе. Цена фиксированная. Договор от года, месяц авансом и два месяца депозита.",
  "https://www.facebook.com/marketplace/item/1622290002933965/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Two-bedroom flat, 35 m², in Guadalupe, Cebu City — semi-furnished with one closet and a double-decker bed, one bathroom, a washing machine, a window-aircon provision and one parking space. Pet-friendly. Walking distance to Puregold and Robinsons Supermarket, close to Guadalupe Elementary and High School. The price is fixed. A year minimum, one month in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000208,"cebu","man","Студия",21000,None,
  "Угловая студия с балконом в Casa Mira Mandaue, башня 4 — полная меблировка, взносы кондоминиума включены. Месяц авансом и два месяца депозита.",
  "https://www.facebook.com/marketplace/item/1634756804903710/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Corner studio with a balcony at Casa Mira Mandaue, Tower 4 — fully furnished, condo dues included. One month in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000209,"cebu","itp","Студия",21000,None,
  "Студия в Mivela Garden Residences, башня 2, четвёртый этаж, окнами на территорию — сразу за IT Park и Country Mall. Полная меблировка, взносы кондоминиума включены; интернет арендатор подключает сам, вода и электричество отдельно. На территории спортзал, взрослый и детский бассейны, открытая гостиная зона, кафе, детская площадка, сад, 7-Eleven у поста охраны, прачечная и станция очистки воды. До IT Park и делового района Ayala одна поездка, до Country Mall пешком. Договор от года, месяц авансом и два месяца депозита.",
  "https://www.facebook.com/marketplace/item/2287928388421626/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Furnished studio at Mivela Garden Residences, Tower 2, fourth floor, facing the amenities — directly behind IT Park and Country Mall. Condo dues are included; the tenant arranges their own wifi and pays water and electricity. On site: gym, lap pool and kids' pool, outdoor lounge, café, playground, garden, a 7-Eleven beside the guardhouse, a laundry and a water refilling station. One ride to IT Park and to the Ayala business park, walking distance to Country Mall. A year minimum, one month in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000210,"cebu","itp","Квартира",30000,None,
  "1-спальная квартира на 29-м этаже в Avida Towers Riala, башня 3, Cebu IT Park — полная меблировка. Сдаёт брокерская контора.",
  "https://www.facebook.com/marketplace/item/1603854287989050/","вчера",1,source="fbmarketplace",cur="PHP",
  descEn="One-bedroom condo on the 29th floor of Avida Towers Riala Tower 3, Cebu IT Park — fully furnished. Let through a brokerage.",
  details={"notice":"RU_D","noticeEn":"EN_D"}),
L(3000211,"cebu","tis","Дом",40000,135,
  "Дом 135 м² на участке 77 м² в Тисе, Себу — за Gaisano Tisa. 3 спальни, 3 санузла, гостиная, кухня со встроенной мебелью, постирочная, гараж на две машины. В хозяйской спальне сплит-кондиционер, в её ванной горячая и холодная вода, во всех комнатах встроенные шкафы, есть водяной насос. Свободен с 15 сентября 2026 года. Договор от года, месяц авансом и месяц депозита, вода и электричество отдельно, 12 чеков вперёд. С животными нельзя, агентов просят не обращаться.",
  "https://www.facebook.com/marketplace/item/1072983918648374/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="House of 135 m² on a 77 m² lot in Tisa, Cebu City — behind Gaisano Tisa. Three bedrooms, three bathrooms, a living room, a kitchen with cabinetry, a laundry area and a two-car garage. Split-type air conditioning in the master bedroom, a hot-and-cold shower in its bathroom, built-in cabinetry in every room and a water pump. Available from 15 September 2026. A year minimum, one month in advance and one month deposit, water and electricity billed separately, twelve postdated cheques required. No pets; agents are asked not to enquire.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000212,"manila","prq","Комната",3500,None,
  "Комната с местами на человека по адресу 1533 Opeña St. на углу Lt. Garcia, рядом с церковью Бакларан, Параньяке. Подходит и на короткий срок.",
  "https://www.facebook.com/marketplace/item/1039102132369686/","сегодня",0,source="fbmarketplace",cur="PHP",
  descEn="Room let by the bed at 1533 Opeña St., corner of Lt. Garcia, beside Baclaran Church, Parañaque. Short stays accepted.",
  details={"notice":"RU_D","noticeEn":"EN_D"}),
L(3000213,"manila","ort","Комната",5500,None,
  "Койко-место для мужчин в Urban Deca Pasig — вода, интернет и взносы кондоминиума включены, свой шкафчик, готовить можно. Квартира полностью меблирована.",
  "https://www.facebook.com/marketplace/item/1606414347809421/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Male bedspace at Urban Deca Pasig — water, internet and condo dues included, with your own locker, and cooking is allowed. The unit itself is fully furnished.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000214,"manila","mla","Комната",6000,None,
  "Комната по адресу 962 Paquita St., Сампалок, Манила — на одного или двоих. Электричество 18 ₱ за кВт·ч, вода 300 ₱ с человека. В комнате кондиционер, вентилятор, кровать с матрасом, бельё, подушка, одеяло, стол и стул. Санузел и мойка общие. Готовить можно только на электричестве, газ в здании запрещён. Парковки нет, гостей и животных нельзя, комендантского часа нет. Только на долгий срок. Пешком до UST, FEU, UE и PRC.",
  "https://www.facebook.com/marketplace/item/1549328066943947/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Room at 962 Paquita St., Sampaloc, Manila — for one or two. Electricity at PHP 18 per kWh, water at PHP 300 per head. The room comes with air conditioning, a fan, a bed with foam, bedsheet, pillow and blanket, a table and a chair. Shared bathroom and sink. Cooking is allowed on electricity only; gas is banned in the building. No parking, no visitors, no pets, no curfew. Long-term tenants only. Walking distance to UST, FEU, UE and the PRC.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000215,"manila","ort","Комната",6000,None,
  "Комната на 2–3 человек в посёлке Foundation of St. Joseph the Worker, Росарио, Пасиг — рядом с госпиталем Mission, на Ortigas Ave. Ext. у рынка Choice. После ремонта, первый этаж, свой счётчик электричества, гостей пускают. Удобно тем, кто работает в Bridgetowne, Пасиге и Ортигасе.",
  "https://www.facebook.com/marketplace/item/1483206597172525/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Room for two or three at Foundation of St. Joseph the Worker Village, Rosario, Pasig — beside Mission Hospital on Ortigas Ave. Ext., near Choice Market. Newly renovated, ground level, with its own electricity meter, and visitors are allowed. Convenient for anyone working in Bridgetowne, Pasig or Ortigas.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000216,"manila","alb","Комната",7000,None,
  "Комната в Алабанге, Мунтинлупа — электричество и вода включены, интернет есть. Рядом Starmall/VTX и транспортные терминалы.",
  "https://www.facebook.com/marketplace/item/1884950725819272/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Room in Alabang, Muntinlupa — electricity and water included, with wifi. Close to Starmall/VTX and the transport terminals.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000217,"manila","ort","Студия",10000,None,
  "Студия без отделки на первом этаже в Hampton Gardens Condominium, Майбунга, Пасиг — 10 000 ₱ плюс 1 700 ₱ взносов кондоминиума. Месяц авансом, два месяца депозита, 11 чеков вперёд. С животными нельзя.",
  "https://www.facebook.com/marketplace/item/1484902443437478/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Bare studio on the ground floor of Hampton Gardens Condominium, Maybunga, Pasig — PHP 10,000 plus PHP 1,700 condo dues. One month in advance, two months deposit, eleven postdated cheques. No pets.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000218,"manila","qzc","Квартира",10000,40,
  "1-спальная квартира около 40 м² в Ronald's Green Apartment, Palmera St. 26, посёлок Villa Florencia, Талипапа, Новаличес, Кесон-Сити. Свободны первый, третий и четвёртый этажи: первый — 11 000 ₱, третий и четвёртый — по 10 000 ₱. Подключение интернета +1 000 ₱, доступны PLDT Fiber и Converge. Парковка платная: 2 700 ₱ под навесом, 1 700 ₱ без. Пешком до шоссе Кирино (Сауйо) и Mindanao Ave. (Талипапа), рядом пункт оплаты NLEX Mindanao и посёлок Kingspoint. Ориентир: баскетбольная площадка Villa Florencia, напротив KM Apartment.",
  "https://www.facebook.com/marketplace/item/1514063430528440/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="One-bedroom flat of about 40 m² at Ronald's Green Apartment, #26 Palmera St., Villa Florencia Subdivision, Talipapa, Novaliches, Quezon City. The 1st, 3rd and 4th floors are free: the 1st is PHP 11,000, the 3rd and 4th PHP 10,000 each. Internet-ready for another PHP 1,000, with PLDT Fiber and Converge both available. Parking is paid: PHP 2,700 with a roof, PHP 1,700 without. Walking distance to Quirino Highway (Sauyo) and Mindanao Ave. (Talipapa), close to the NLEX Mindanao toll plaza and Kingspoint Subdivision. Landmark: the Villa Florencia basketball court, opposite KM Apartment.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000219,"manila","qzc","Квартира",15000,None,
  "2-спальная квартира в кондоминиуме Amaia Skies Cubao, Кесон-Сити — частичная меблировка, два кондиционера, холодильник, взносы кондоминиума включены. До трёх человек. Рядом SM Cubao, школы Samson и STI. Свободна с октября 2026 года.",
  "https://www.facebook.com/marketplace/item/1593879352323068/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Two-bedroom condo at Amaia Skies Cubao, Quezon City — semi-furnished, two air conditioners, a fridge, condo dues included. Up to three people. Close to SM Cubao, Samson College and STI. Available from October 2026.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000220,"manila","qzc","Квартира",14000,None,
  "1-спальная квартира без отделки в Mezza 1, башня 2, на Gregorio Araneta Ave., Кесон-Сити — кондиционер есть, взносы включены. Рядом CCP, FEU, PUP и SM Centerpoint. Месяц авансом, два месяца депозита, 11 чеков вперёд или банковский перевод. Осмотр по записи.",
  "https://www.facebook.com/marketplace/item/1115228477832266/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Bare one-bedroom unit at Mezza 1 Tower 2, Gregorio Araneta Ave., Quezon City — air conditioning included, dues included. Close to the CCP, FEU, PUP and SM Centerpoint. One month in advance, two months deposit, eleven postdated cheques or a bank transfer. Viewing by appointment.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000221,"manila","mak","Студия",17000,None,
  "Студия с полной меблировкой в Belton Place, Макати. Два месяца депозита и месяц авансом.",
  "https://www.facebook.com/marketplace/item/1811035316891087/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Fully furnished studio at Belton Place, Makati City. Two months security deposit and one month in advance.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000222,"manila","mla","Студия",17000,None,
  "Студия без отделки на 12-м этаже в Victoria de Manila 2, вдоль Taft Avenue, Малате, Манила — напротив университетов PWU и PCU. Рядом станция LRT Pedro Gil, госпиталь UP-PGH, университет St. Paul и Robinsons Manila. Взносы кондоминиума включены, договор от года.",
  "https://www.facebook.com/marketplace/item/953300444486858/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Bare studio on the 12th floor of Victoria de Manila 2, along Taft Avenue, Malate, Manila — in front of PWU and PCU. Close to LRT Pedro Gil station, UP-PGH, St Paul University and Robinsons Manila. Dues included, a year minimum.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000223,"manila","alb","Студия",17000,21,
  "Студия 21 м² с балконом на 19-м этаже башни 1 в Cityland One Premier Alabang — полная меблировка, 1 санузел, интернет бесплатно. Можно с одной небольшой собакой. Рядом Molito и San Beda Alabang. Свободна с 22 сентября 2026 года. Взносы и интернет входят в цену, торг уместен. Два месяца депозита, месяц авансом, оплата переводом, договор от года. Только напрямую, без посредников.",
  "https://www.facebook.com/marketplace/item/1077430741419951/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Studio of 21 m² with a balcony on the 19th floor of Tower 1, Cityland One Premier Alabang — fully furnished, one bathroom, free internet. One small-breed dog allowed. Close to Molito and San Beda Alabang. Available from 22 September 2026. Dues and internet are included in the price, which is negotiable. Two months deposit, one month in advance, payment by bank transfer, a year minimum. Direct clients only.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000224,"manila","psy","Студия",21000,30,
  "Студия 30 м² без мебели в Quantum Residences, башня Aqua, на Taft Avenue, барангай 49, Пасай — взносы товарищества включены. Два месяца депозита, месяц авансом, чеки вперёд, договор от года.",
  "https://www.facebook.com/marketplace/item/2240131736843410/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Unfurnished studio of 30 m² at Quantum Residences (Tower Aqua), Taft Ave., Barangay 49, Pasay City — association dues included. Two months deposit, one month in advance, postdated cheques, a year minimum.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000225,"manila","psy","Студия",28000,22,
  "Новая студия 22 м² с полной меблировкой в Avida Towers Prime Taft, Пасай. Владелец сдаёт только одному человеку или паре и отдельно оговаривает, что иностранцам не сдаёт.",
  "https://www.facebook.com/marketplace/item/1066728742988257/","30 дней назад",30,source="fbmarketplace",cur="PHP",
  descEn="Brand-new fully furnished studio of 22 m² at Avida Towers Prime Taft, Pasay City. The owner lets it to a single person or a couple only, and states outright that they do not let to foreigners.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
'''

NEW_SRC = (NEW_SRC
           .replace("RU_P125", P125_RU).replace("EN_P125", P125_EN)
           .replace("RU_P5K", P5K_RU).replace("EN_P5K", P5K_EN)
           .replace("RU_B5", B5_RU).replace("EN_B5", B5_EN)
           .replace("RU_D", D_RU).replace("EN_D", D_EN)
           .replace("RU_N", N_RU).replace("EN_N", N_EN))

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
