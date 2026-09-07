# -*- coding: utf-8 -*-
"""Первые объявления из ГРУПП Facebook, 7 сентября 2026: Думагете, 6 штук.

Группы владельца до сегодняшнего дня не были использованы вообще -- ноль строк.
Причина была техническая: лента группы виртуализована (в DOM висит одна-две
карточки), а текст постов приходит вперемешку с подставными строками, поэтому
обычное чтение страницы даёт мусор. Рабочий способ описан в fb_groups_howto.md;
коротко -- Facebook сам кладёт посты в JSON внутри <script>, а поиск по группе
(/groups/<id>/search/?q=...) отдаёт их в первой же загрузке, без прокрутки.

Качество текста здесь заметно выше, чем в Marketplace: в группах пишут люди и
пишут подробно -- с барангаем, ориентирами, условиями договора и тем, что входит
в цену. Все шесть открыты по прямой ссылке и подтверждены живыми.

ДАТА. Её здесь нет, и это честная оговорка, а не упущение. В payload поста даты
не оказалось, а метки времени на странице принадлежат вперемешку комментариям и
соседним постам: пять постов из трёх разных групп дали одну и ту же «дату»
5 сентября, чем себя и выдали. Поэтому daysAgo у этих строк означает не возраст
объявления, а время, прошедшее с проверки: 7 сентября 2026 каждый пост был
открыт и подтверждён живым. Подпись «сегодня» на карточке читается как «сегодня
проверено», и оговорка в каждой строке говорит это прямым текстом -- иначе
сборка справедливо ругается на расхождение подписи с daysAgo. Источник fbgroup освобождён от чистки по возрасту
(purge_old_listings.py), но не от проверки на живость.

ФОТО не сохраняются: ссылки Facebook на изображения подписаны и живут около
четырёх дней, поэтому в телеграм-хаб (порог 3 фото) эти строки не идут.

Отсеяно: объявления без барангая (только «Dumaguete City»), пара одинаковых
постов одного брокера, прайс-лист комплекса без адреса и посты со снятой
пометкой «Rented».
"""
from listing_lock import insert_listings

IDS = [3000227, 3000228, 3000229, 3000230, 3000231, 3000232]

N_RU = ("Источник — пост в группе Facebook. Точной даты размещения группа не отдаёт: в данных "
        "страницы её нет, а видимые метки времени принадлежат комментариям. Указанный возраст — "
        "это время с проверки: 7 сентября 2026 объявление было открыто по ссылке и подтверждено "
        "живым. Фотографий нет: ссылки Facebook на изображения подписаны и живут около четырёх "
        "дней, смотрите фото по ссылке.")
N_EN = ("Source: a post in a Facebook group. The group gives no exact posting date — it is absent "
        "from the page data, and the visible timestamps belong to comments. The age shown is time "
        "since verification: on 7 September 2026 the post was opened and confirmed live. No photos: "
        "Facebook image links are signed and last about four days, so see the photos on the post.")

NEW_SRC = r'''
L(3000227,"dumaguete","tly","Дом",35000,None,
  "Дом в Talay Bliss, Думагете — полная меблировка, 2 спальни с кондиционерами, санузел с горячей и холодной водой, кухонная мойка с горячей водой. Четыре камеры видеонаблюдения, подключён интернет PLDT, накопительный бак для воды, ухоженный участок. До Валенсии 5 минут, до Robinsons 10. Договор на год, месяц авансом и два месяца депозита. Сдаёт собственник, посредников просят не обращаться. Осмотр в любое время.",
  "https://www.facebook.com/groups/153191128587086/posts/2227162764523235/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="House in Talay Bliss, Dumaguete — fully furnished, 2 bedrooms with air conditioning, a bathroom with a hot-and-cold shower, and a kitchen sink with hot water. Four CCTV cameras, PLDT internet installed, a water tank and a well-kept garden. Five minutes to Valencia, ten to Robinsons. A one-year contract, one month in advance and two months deposit. Let by the owner directly; agents and brokers are asked not to enquire. Viewing at any time.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000228,"dumaguete","sib","Дом",75000,None,
  "Дом с полной меблировкой в Аджонге, Сибулан — 3 спальни, в каждой свой санузел и кондиционер, гостиная с кондиционером. Большой собственный бассейн, высокий забор, видеонаблюдение. Заезжать можно сразу. Месяц авансом и месяц депозита.",
  "https://www.facebook.com/groups/153191128587086/posts/2228480617724783/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Fully furnished house in Ajong, Sibulan — 3 bedrooms, each with its own bathroom and air conditioner, and an air-conditioned living room. A large private swimming pool, a high fence for privacy and CCTV. Ready to move into. One month in advance and one month deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000229,"dumaguete","dau","Дом",30000,None,
  "Дом в Дауине — до пляжа и курортов 10 минут пешком, до шоссе 5. Три спальни (в двух кондиционеры), санузел с горячей и холодной водой, кухня со столовой. Кровать королевского размера с матрасом, холодильник, духовка. Участок за воротами, просторный двор перед домом, гараж. Интернет и вода бесплатно, кроме питьевой; электричество по счётчику. Можно с животными.",
  "https://www.facebook.com/groups/153191128587086/posts/2227722881133890/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="House in Dauin — a ten-minute walk to the beach and the resorts, five minutes to the highway. Three bedrooms (two with air conditioning), one bathroom with a hot-and-cold shower, and a kitchen with a dining area. Queen-size bed with mattress, fridge and oven. Gated, with a generous front yard and a garage. Wifi and water are free apart from drinking water; electricity is on your own meter. Pets allowed.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000230,"dumaguete","bcg","Дом",27000,None,
  "Таунхаус (юнит 55) в Richwood Homes, Баконг — меблирован, 2 спальни с кондиционерами, санузел с горячим душем, гостиная с кондиционером. На территории бассейн, баскетбольная площадка и детская площадка. Цена за долгий срок, коммунальные сверх аренды; у владельца есть и краткосрочные тарифы, они зависят от числа жильцов и срока.",
  "https://www.facebook.com/groups/153191128587086/posts/2228897344349777/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Townhouse (unit 55) at Richwood Homes, Bacong — furnished, 2 bedrooms with air conditioning, a bathroom with a hot shower and an air-conditioned living area. The grounds have a swimming pool, a basketball court and a playground. This is the long-term rate, with utilities on top; the owner also offers short-term and daily rates that depend on the number of guests and the length of stay.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000231,"dumaguete","pia","Квартира",28000,None,
  "3-спальная квартира в Пиапи, Думагете — частичная меблировка, кондиционеры во всех спальнях, в хозяйской своя ванная и гардеробная. Центральный кондиционер в гостиной и столовой, 2,5 санузла, просторные гостиная и столовая, свой бак для воды, двухдверный холодильник, газовая плита с духовкой, навес для машины. До университета Силлиман, офисов, магазинов и кафе пешком. Договор от года, два месяца авансом и два месяца депозита.",
  "https://www.facebook.com/groups/1996683940588782/posts/4592229514367532/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Three-bedroom flat in Piapi, Dumaguete — semi-furnished, air conditioning in every bedroom, the master with an ensuite bathroom and a walk-in closet. Centralised air conditioning in the living and dining areas, 2.5 bathrooms, generous living and dining space, its own water tank, a two-door fridge, a gas range with oven and a carport. Silliman University, offices, shops and restaurants are all within walking distance. A year minimum, two months in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000232,"dumaguete","dar","Студия",10000,None,
  "Студия в Клэйтауне, Даро, Думагете — за заправкой Shell, рядом с центром. Пешком до Jollibee, McDonald's, школ и спортзала. Недалеко университет Силлиман, St. Paul, NORSU и NOHS. В доме несколько таких юнитов.",
  "https://www.facebook.com/groups/1996683940588782/posts/4602281100029040/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Studio in Claytown, Daro, Dumaguete — behind the Shell petrol station, close to downtown. Walking distance to Jollibee, McDonald's, schools and a gym. Silliman University, St Paul, NORSU and NOHS are all nearby. Several such units are available in the building.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
