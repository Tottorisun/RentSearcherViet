# -*- coding: utf-8 -*-
"""Группы Facebook через личный Chrome владельца, 8 сентября 2026 (вечер).

Вход в отдельном профиле `_fb_profile/` протух, и fb_collect.py честно
отказался работать. Владелец сказал заходить через его Chrome — этот проход
сделан claude-in-chrome по методу из fb_groups_howto.md: поиск по группе,
разбор JSON из <script>, проверка каждого поста по прямой ссылке.

ИЗ ШЕСТНАДЦАТИ ОТОБРАННЫХ ДОШЛИ ВОСЕМЬ. Отсев по порядку:
  * ЧЕТЫРЕ уже на сайте (4592229514367532 Пиапи, 2227162764523235 Талай,
    2228480617724783 Аджонг, 2573076826469737 Мандалуйонг). Поиск по группе
    выдаёт их наравне с новыми, поэтому сверка по id обязательна ДО проверки
    живости: она сэкономила четыре загрузки страниц.
  * ТРИ СНЯТЫ, хотя поиск их выдаёт: 37717782854534617 (дом в Баниладе,
    Баконг), 122121963909168011 (квартира у Diversion Road, Баконг) и
    28698912193035115 — та самая студия DECA Homes на Тисе, которую
    fb_groups_howto.md записал снятой ещё вчера. Индекс поиска её всё ещё
    отдаёт. Вчерашняя оценка «один снятый из девяти» сегодня не подтвердилась:
    три из одиннадцати проверенных. Проверять ссылкой надо каждый пост.
  * ОДИН БЕЗ ЦЕНЫ: 4589625574627926 (Болокболок, Сибулан) — брокерский пост
    Filipino Homes с кодом объекта и без суммы.

ЧЕГО НЕ ВЗЯЛИ ОСОЗНАННО. Cantil-E (40 000 ₱), San Jose Extension (40 000 ₱),
Булакао, Бакаян, Лилоан и Яти — районов с такими ключами у нас нет, а
приписывать объявление к соседнему району наугад нельзя. Мандауэ «в закрытом
посёлке» без названия посёлка — адрес скрыт, такие не заводим.

ФОТОГРАФИЙ НЕТ по той же причине, что и в прошлых групповых партиях: ссылки
Facebook на изображения подписаны и живут около четырёх дней.
"""
from listing_lock import insert_listings

IDS = [3000252, 3000253, 3000254, 3000255, 3000256, 3000257, 3000258, 3000259]

N_RU = ("Источник — пост в группе Facebook. Точной даты размещения группа не отдаёт: в данных "
        "страницы её нет, а видимые метки времени принадлежат комментариям. Указанный возраст — "
        "это время с проверки: 8 сентября 2026 объявление было открыто по прямой ссылке и "
        "подтверждено живым. Фотографий нет: ссылки Facebook на изображения подписаны и живут "
        "около четырёх дней, смотрите фото по ссылке.")
N_EN = ("Source: a post in a Facebook group. The group gives no exact posting date — it is absent "
        "from the page data, and the visible timestamps belong to comments. The age shown is time "
        "since verification: on 8 September 2026 the post was opened at its permalink and confirmed "
        "live. No photos: Facebook image links are signed and last about four days, so see the "
        "photos on the post.")

NEW_SRC = r'''
L(3000252,"dumaguete","val","Квартира",25000,None,
  "Новая квартира в Валенсии, Негрос Ориенталь — 2 спальни с кондиционерами, 2 санузла с водонагревателями, полная меблировка. Стоит вдоль асфальтированной дороги, три минуты на машине до площади Валенсии.",
  "https://www.facebook.com/groups/153191128587086/posts/2227259157846929/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A brand-new flat in Valencia, Negros Oriental — 2 bedrooms with air conditioning, 2 bathrooms with water heaters, fully furnished. It stands along a paved road, a three-minute drive from Valencia plaza.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000253,"dumaguete","dar","Квартира",12000,None,
  "Квартира в Даро, Думагете — кровать с матрасом и подушками, шкафы, душ с горячей и холодной водой, парковка для машины и мотоцикла. Вода и электричество включены в плату. Рядом больницы ACE, NOPH и SUMC, университет NORSU и центр города. Свободны четыре одинаковые квартиры, владелец сдаёт в порядке обращения и ищет долгосрочных жильцов.",
  "https://www.facebook.com/groups/346330203591713/posts/1410386863852703/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A flat in Daro, Dumaguete — bed with foam and pillows, cabinets, hot and cold shower, parking for a car and a motorcycle. Water and electricity are included in the rent. ACE Hospital, NOPH and SUMC, NORSU university and downtown are all close by. Four identical units are free, let first come first served, and the owner is looking for long-term tenants.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000254,"dumaguete","cdy","Квартира",7000,None,
  "Квартира в Кандау-ай, Думагете — одна спальня с кроватью, санузел, стол со стульями и диван, частичная меблировка. Закрытый двор. Освобождается 25 сентября 2026 года. Месяц авансом и месяц депозита.",
  "https://www.facebook.com/groups/346330203591713/posts/1404520667772656/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A flat in Candau-ay, Dumaguete — one bedroom with a bed, a bathroom, table and chairs and a sofa, semi-furnished. Gated compound. Free from 25 September 2026. One month in advance and one month deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000255,"cebu","prd","Комната",4000,None,
  "Комната в Пардо, Себу — общий санузел, отдельный счётчик электричества, закрытая территория, парковка для мотоцикла, район не топит. Рядом USJR Basak, церковь и рынок Пардо. Свободна одна комната. Владелец просит соблюдать чистоту, не курить и не пить на территории и не приводить посторонних.",
  "https://www.facebook.com/groups/1735327053393688/posts/4534649576794741/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A room in Pardo, Cebu City — shared bathroom, its own electricity submeter, gated property, motorcycle parking, and the area does not flood. USJR Basak, Pardo Church and Pardo Market are nearby. One room is free. The owner asks tenants to keep the place clean, not to smoke or drink on the premises and not to bring unauthorised visitors.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000256,"cebu","gua","Квартира",12500,None,
  "Однокомнатная квартира в Гуадалупе, Себу — своя ванная, третий этаж, из мебели только кровать. Рассчитана на двоих, животных нельзя. Парковка есть, но оплачивается отдельно. Дом стоит вдоль главной дороги за воротами; пешком до медицинской школы MHAM, торгового центра One Pavilion и перекрёстка Банава, одна поездка до Капитолия, Фуэнте, Колона и Айялы. Месяц авансом и два месяца депозита, только долгий срок.",
  "https://www.facebook.com/groups/rentcebu/posts/27388937317471702/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A one-bedroom flat in Guadalupe, Cebu City — its own bathroom, third floor, a bedframe as the only furniture. Good for two people, no pets. Parking is available for a separate fee. The building is gated and stands along the main road; MHAM Medical School, One Pavilion Mall and Banawa Junction are within walking distance, and Capitol, Fuente, Colon and Ayala are one ride away. One month advance and two months deposit, long lease only.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000257,"manila","qzc","Квартира",10000,42,
  "Квартира 42 м² на ул. Апо, 21, Маркос Компаунд, барангай Пасонг Тамо (Пингкиан 2), Тандан Сора, Кесон-Сити — спальня, гостиная, кухня, столовая и санузел. Свои счётчики воды и электричества, закрытый двор с парковкой для мотоцикла, район не топит. Животных нельзя, вай-фай по желанию. Срок от года, свободна одна квартира.",
  "https://www.facebook.com/groups/224805677963542/posts/2566293860481367/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A 42 m² flat at 21 Apo St., Marcos Compound, Brgy. Pasong Tamo (Pingkian 2), Tandang Sora, Quezon City — bedroom, living room, kitchen, dining area and bathroom. Its own water and electricity meters, a gated compound with motorcycle parking, and the area does not flood. No pets; WiFi is optional. One-year minimum, one unit left.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000258,"manila","bgc","Квартира",350000,205,
  "Квартира 205 м² в Grand Hyatt Residences, южная башня, Бонифачо Глобал Сити — 3 спальни, полная меблировка, два парковочных места.",
  "https://www.facebook.com/groups/224805677963542/posts/2497734997337254/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A 205 m² flat in Grand Hyatt Residences, South Tower, Bonifacio Global City — 3 bedrooms, fully furnished, two parking slots.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000259,"manila","bgc","Квартира",170000,123,
  "Квартира 123 м² в Park Triangle Residences, Бонифачо Глобал Сити — 3 спальни, полная меблировка, комната для прислуги со своим санузлом и ещё два полных санузла, парковка. Дом только что сдан. Два месяца авансом и два депозита.",
  "https://www.facebook.com/groups/224805677963542/posts/2576446792799407/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="A 123 m² flat in Park Triangle Residences, Bonifacio Global City — 3 bedrooms, fully furnished, a maid's room with its own bathroom plus two full bathrooms, and parking. The building has just been turned over. Two months advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
