# -*- coding: utf-8 -*-
"""Группы Facebook, второй заход: Себу и Манила, 8 сентября 2026, 16 объявлений.

Пройдено 6 групп из оставшихся 15 (Себу: 993673090964916, 3914645581932487,
cebu.tambayan.2; Манила: 224805677963542, 1319639041431566, 715451165293916).
Способ съёма -- fb_groups_howto.md.

ПРОВЕРКА ЖИВОСТИ ОКУПИЛАСЬ СРАЗУ. Из 18 отобранных постов ДВА оказались уже
снятыми, хотя поиск по группе продолжал их выдавать: студия DECA Homes на Тисе
(28698912193035115) и Sun Residences у Welcome Rotonda (1090263046770528).
То есть индекс поиска отстаёт от удалений примерно в одном случае из девяти, и
открывать каждый пост по прямой ссылке -- не формальность. Оба выброшены.

Ещё одна особенность выдачи: один и тот же пост приходит под двумя разными id
(сам пост и его репост в ту же группу) -- дом в Баниладе за 80 000, дом в
Мабало за 50 000, квартира в Rainbow Village и лофты по 15 000 пришли парами.
Съёмник теперь режет такие пары по первым 70 символам текста.

ДАТЫ нет, как и у первой партии: источник fbgroup заведён как источник без
даты рядом с dotproperty. daysAgo=0 и подпись «сегодня» означают «сегодня
проверено», о чём прямо сказано в оговорке каждой строки.

Отсеяно: посты без барангая, прайс-листы без адреса, «SOLD», rent-to-own
(это продажа), а также Лилоан, Кордова, Консоласьон и Норсагарай -- районов
под них на сайте нет.
"""
from listing_lock import insert_listings

IDS = list(range(3000233, 3000249))

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
L(3000233,"cebu","bnl","Дом",80000,300,
  "Дом 300 м² в Баниладе, Себу — полная меблировка, 5 спален, 3 санузла, комната для помощницы со своим туалетом, постирочная, летняя кухня, парковка на три машины, небольшой сад. С животными нельзя. Договор на год, два месяца авансом и два месяца депозита.",
  "https://www.facebook.com/groups/993673090964916/posts/28133317763001222/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="House of 300 m² in Banilad, Cebu — fully furnished, 5 bedrooms, 3 bathrooms, a maid's room with its own toilet, a laundry area, a dirty kitchen, parking for three cars and a small garden. No pets. A one-year contract, two months in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000234,"cebu","mab","Дом",50000,200,
  "Дом 200 м² в Мабало, Себу — частичная меблировка, 4 спальни, 4 санузла, летняя кухня, одно место на парковке. Можно с животными, допускается субаренда. Договор на год, месяц авансом и два месяца депозита, оплата чеками вперёд.",
  "https://www.facebook.com/groups/993673090964916/posts/28162290210103977/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="House of 200 m² in Mabolo, Cebu — semi-furnished, 4 bedrooms, 4 bathrooms, a dirty kitchen and one parking space. Pets allowed, and the owner is open to sublease. A one-year contract, one month in advance and two months deposit, paid by postdated cheques.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000235,"cebu","lah","Квартира",13000,None,
  "1-спальная квартира на улице La Guardia, Лахуг, Себу — рядом IT Park и Университет Южных Филиппин (USPF). В доме по этой же цене есть и студии.",
  "https://www.facebook.com/groups/993673090964916/posts/3059186767746861/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="One-bedroom flat on La Guardia Street, Lahug, Cebu — close to IT Park and the University of Southern Philippines. Studio units are available in the same building at the same price.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000236,"cebu","man","Квартира",20000,None,
  "2-спальная квартира в Urban Deca Homes Banilad на Hernan Cortes, Мандауэ — взносы кондоминиума и интернет включены, вода и электричество отдельно. Напротив делового центра Oakridge. Месяц авансом и два месяца депозита, условия обсуждаются.",
  "https://www.facebook.com/groups/993673090964916/posts/26528937373449746/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Two-bedroom condo at Urban Deca Homes Banilad on Hernan Cortes, Mandaue City — condo dues and wifi included, water and electricity billed separately. Across from Oakridge Business Park. One month in advance and two months deposit, negotiable.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000237,"cebu","prd","Дом",25000,None,
  "Новый дом-бунгало в St Jude, Булакао, Пардо, Себу — сдаётся впервые. 3 спальни, 2 санузла, участок 110 м², накопительный бак для воды, парковка. Рядом кампус UC Bulacao, рынок ACT и склад Prince. Договор на год, месяц авансом и два месяца депозита.",
  "https://www.facebook.com/groups/993673090964916/posts/3047745422224329/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Newly built bungalow in St Jude, Bulacao, Pardo, Cebu City — let for the first time. Three bedrooms, two bathrooms, a 110 m² plot, a water tank and parking. UC Bulacao, the ACT wet market and the Prince warehouse are all nearby. A one-year lease, one month in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000238,"cebu","lab","Студия",16500,None,
  "Студия с полной меблировкой в Casa Mira Towers Labangon, башня 2, пятый этаж — двуспальная кровать, кондиционер, полностью оборудованная кухня с холодильником, плитой и вытяжкой, обеденная зона, шкаф, свой санузел. В доме лифт и круглосуточная охрана. Месяц авансом и месяц депозита.",
  "https://www.facebook.com/groups/3914645581932487/posts/28412985171671854/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Fully furnished studio at Casa Mira Towers Labangon, Tower 2, fifth floor — double bed, air conditioning, a fully equipped kitchen with fridge, stove and range hood, a dining area, a wardrobe and a private bathroom. The building has a lift and 24-hour security. One month in advance and one month deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000239,"cebu","tlm","Дом",35000,160,
  "Двухэтажный дом 160 м² на участке 127 м² в посёлке Metropolis, Пит-ос, Себу — рядом международная школа CIS. Меблирован, 3 спальни, 3 санузла, комната для помощницы, гараж на две машины. Посёлок закрытый. Осмотр по записи. Два месяца авансом и два месяца депозита.",
  "https://www.facebook.com/groups/3914645581932487/posts/28357490797221292/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Two-storey house of 160 m² on a 127 m² plot in Metropolis Subdivision, Pit-os, Cebu — next to Cebu International School. Furnished, 3 bedrooms, 3 bathrooms, a maid's quarter and a two-car garage, inside a gated executive subdivision. Viewing by appointment. Two months in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000240,"cebu","lab","Студия",9000,12,
  "Студия 12 м² с частичной меблировкой в Victor Village, Tres de Abril, Лабангон, Себу — второй и третий этажи. Санузел, кондиционер, шкаф, тумба, кровать с матрасом. Рассчитана на двоих. Вода 300 ₱ с человека, электричество по отдельному счётчику. Парковки нет, за неё доплата.",
  "https://www.facebook.com/groups/3914645581932487/posts/28187313874238986/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Semi-furnished studio of 12 m² in Victor Village, Tres de Abril, Labangon, Cebu City — second and third floors. Toilet and bath, air conditioning, a closet, a cupboard and a bed with foam. Suits two people. Water is PHP 300 per head, electricity on a submeter. No parking; it costs extra.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000241,"cebu","mac","Дом",17000,None,
  "Двухкомнатный таунхаус с частичной меблировкой в BF Better Living Homes, вторая очередь, Судтунган, Лапу-Лапу — цена снижена с 20 000 и объявлена окончательной. Взносы товарищества, электричество и вода сверх аренды. Два месяца депозита и месяц авансом.",
  "https://www.facebook.com/groups/3914645581932487/posts/28131772863126421/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Semi-furnished two-bedroom townhouse at BF Better Living Homes Phase 2, Sudtungan, Lapu-Lapu City — reduced from 20,000 and stated as the final price. HOA dues, electricity and water are on top of the rent. Two months security deposit and one month in advance.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000242,"cebu","mab","Комната",9000,None,
  "Комната в Мабало, Себу — рядом с кондоминиумом The Persimmon. Свой санузел, кухня общая на четверых, мебели нет. Интернет бесплатно, двор за воротами. Свободна одна комната. Владелец просит писать, а не звонить.",
  "https://www.facebook.com/groups/cebu.tambayan.2/posts/28335456679451105/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Room in Mabolo, Cebu, beside The Persimmon condominium — own bathroom, kitchen shared between four, and the room itself is bare. Free wifi, gated. One room is free. The owner asks for messages rather than calls.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000243,"cebu","prd","Дом",12000,None,
  "Двухэтажный таунхаус с 2 спальнями в Villa San Pedro 2, Басак, Пардо, Себу — напротив главных ворот кампуса USJR в Басаке. До шести жильцов. В том же доме есть 2-спальные квартиры за 10 000 ₱ (до четырёх человек), 1-спальные за 7 000 ₱ (до двоих) и койко-места за 2 000 ₱ с человека.",
  "https://www.facebook.com/groups/cebu.tambayan.2/posts/28387576457572460/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Two-storey, two-bedroom townhouse at Villa San Pedro 2, Basak Pardo, Cebu City — opposite the main gate of the USJR Basak campus. Up to six occupants. The same property also offers two-bedroom units at PHP 10,000 (up to four), one-bedroom at PHP 7,000 (up to two) and bedspaces at PHP 2,000 per head.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000244,"cebu","prd","Квартира",9000,None,
  "Новая 2-спальная квартира (дверь 6) в Rainbow Village, Кинасанг-ан, Пардо, Себу — два санузла с душем, биде и раковиной с зеркалом, кухня со столешницами из гранита, готовить разрешено, гостиная с трёхрежимным светом. Готова к заселению.",
  "https://www.facebook.com/groups/cebu.tambayan.2/posts/1773592386974748/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Brand-new two-bedroom flat (Door 6) at Rainbow Village, Kinasang-an, Pardo, Cebu City — two bathrooms with shower, bidet and a sink with mirror, a kitchen with granite countertops where cooking is allowed, and a living room with tri-colour lighting. Ready to move into.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000245,"cebu","col","Комната",4500,None,
  "Комната на улице F. Villa, Т. Падилья, Себу — близко ко всему. Без животных и без детей. Месяц авансом и месяц депозита. Свободна одна комната со 2 сентября 2026 года.",
  "https://www.facebook.com/groups/cebu.tambayan.2/posts/28304257979237642/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Room on F. Villa Street, T. Padilla, Cebu City — close to everything. No pets and no children. One month in advance and one month deposit. One room free from 2 September 2026.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000246,"manila","mdl","Студия",12500,19,
  "Студия 19 м² в Pioneer Heights 1 на Pioneer Street, Мандалуйонг — рядом McDonald's на Пионер, телецентр Channel 5, недалеко BGC. Взносы товарищества 1 460 ₱ сверх аренды. С животными нельзя. Договор на год, два месяца депозита и месяц авансом, 11 чеков вперёд; от всех жильцов нужны государственные удостоверения личности.",
  "https://www.facebook.com/groups/224805677963542/posts/2573076826469737/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Studio of 19 m² at Pioneer Heights 1 on Pioneer Street, Mandaluyong City — near the Pioneer McDonald's and the Channel 5 TV station, with BGC not far. Association dues of PHP 1,460 are on top of the rent. No pets. A one-year term, two months deposit and one month in advance, eleven postdated cheques, and a government-issued ID from every tenant.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000247,"manila","bgc","Студия",14000,None,
  "Студия без отделки в Panglao Oasis на Levi B. Mariano Avenue, Тагиг — дом только что сдан. Взносы товарищества включены. В том же доме 2-спальные без отделки за 19 000 ₱ и с балконом за 21 000 ₱. Договор от года с продлением, месяц авансом и два месяца депозита.",
  "https://www.facebook.com/groups/1319639041431566/posts/27198951583073624/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Bare studio at Panglao Oasis on Levi B. Mariano Avenue, Taguig City — a newly turned-over building. Association dues included. The same building offers bare two-bedroom units at PHP 19,000 and two-bedroom with balcony at PHP 21,000. A renewable one-year minimum lease, one month in advance and two months deposit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000248,"manila","ort","Студия",27000,29,
  "Студия 29 м² с полной меблировкой в The Vantage at Kapitolyo от Rockwell Land, Пасиг — взносы товарищества включены. Пешком до Pioneer Center, Estancia Mall и Unimart в Capitol Commons. Рядом мост Kalayaan между BGC и Ортигасом, сам Ортигас и Мандалуйонг.",
  "https://www.facebook.com/groups/715451165293916/posts/3363268593845480/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Fully furnished studio of 29 m² at The Vantage at Kapitolyo by Rockwell Land, Pasig — association dues included. Walking distance to Pioneer Center, Estancia Mall and Unimart at Capitol Commons. Close to the Kalayaan BGC–Ortigas bridge, Ortigas itself and Mandaluyong.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
