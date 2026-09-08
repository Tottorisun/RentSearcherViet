# -*- coding: utf-8 -*-
"""Группы Facebook, 8 сентября 2026 (вечер): Фу Ми Хынг, Тхао Дьен и Лапу-Лапу.

Партия маленькая намеренно. Из семи отобранных постов четыре дошли до сайта:
два оказались снятыми, один -- дублем уже заведённого объекта.

СНЯТЫЕ: 29125039997085730 (студия у школы San Nicolas, Себу) и
122239746800321537 (комната в Santo Niño Village, Банилад). Оба поиск по группе
продолжает выдавать. Счёт этой проверки за два дня: 2 снятых из 18 и 2 из 7.

ДУБЛЬ МЕЖДУ ИСТОЧНИКАМИ -- случай новый и важный. Пост 2369186530287561
(таунхаус в Capitol Site за 35 000 ₱, взносы и вайфай включены, 2 санузла,
2 спальни с балконом в главной, охрана круглосуточно, клубный дом и бассейн,
до четырёх человек) -- это ровно наш 3000174, заведённый из Marketplace.
Арендодатель выложил объявление и туда, и в группу; ссылки разные, объект один.
Дедупликация по URL такое не видит в принципе -- ловится только по тексту,
через check_repost.py. Значит между fbmarketplace и fbgroup дубли будут и
дальше, и проверять партию надо не только против своего источника.

ТХАНЬ ДА в группах не нашлось: поиск цепляет «Тхань» и выдаёт Биньтхань.
Район bq так и остался самым тонким на сайте.

ЕЩЁ ОДИН ДУБЛЬ, пойманный check_repost.py уже после отбора: квартира в
Sunshine Sky City (2 спальни, 70 м², 17 000 000 ₫). На сайте таких УЖЕ ДВЕ --
1000169 из Batdongsan и 1000571 из Chợ Tốt, обе с той же ценой, площадью и
числом комнат. Почти наверняка это одна и та же квартира, уже задвоенная между
порталами; третья копия сделала бы только хуже. Не заведена.

РАЙОНЫ ПО ПРЕЦЕДЕНТУ, а не по догадке. Sunshine -> tm (10 уже заведённых
строк), Nam Viên -> tm (1). Хынг Фыок и Кань Дой прецедента не имеют и потому
пропущены, хотя объявления там были: ключ tm или th для них выбирался бы
наугад.
"""
from listing_lock import insert_listings

IDS = [1000580, 1000582, 3000251]

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
L(1000580,"ho-chi-minh","ak","Офис",73000000,230,
  "Офисный этаж 230 м² на улице Нгуен Ван Хыонг, Тхао Дьен — второй этаж, помещение полностью свободно, планировка любая. В том же здании сдаются третий и четвёртый этажи по 270 м² за 85 000 000 ₫ каждый; этажи сдаются по отдельности. Подходит под офис, представительство компании, учебный центр или студию.",
  "https://www.facebook.com/groups/2439677179643705/posts/4712530212358379/","сегодня",0,source="fbgroup",
  descEn="Office floor of 230 m² on Nguyễn Văn Hưởng street, Thảo Điền — the second floor, completely empty and open to any layout. The same building offers the third and fourth floors at 270 m² for ₫85,000,000 each, and floors are let separately. Suits an office, a company base, a training centre or a studio.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(1000582,"ho-chi-minh","tm","Дом",60000000,126,
  "Вилла 126 м² (7 на 18 м) в квартале Нам Вьен, Фу Ми Хынг, Куан 7 — три этажа, 5 спален, 4 санузла, полная меблировка. Ориентирована на северо-запад.",
  "https://www.facebook.com/groups/2439677179643705/posts/4723442334600500/","сегодня",0,source="fbgroup",
  descEn="Villa of 126 m² (7 by 18 m) in the Nam Viên quarter of Phú Mỹ Hưng, District 7 — three floors, 5 bedrooms, 4 bathrooms, fully furnished, facing north-west.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(3000251,"cebu","mac","Комната",4500,None,
  "Комната в новом доме: Block 7, Quarry Road, Sewage, Пусок, Лапу-Лапу — 4 500 ₱ на двоих, 3 000 ₱ на одного. Вода фиксированная: 200 ₱ в месяц за комнату на одного и 300 ₱ на двоих. Месяц авансом и месяц депозита, минимальный срок 6 месяцев, бронь не принимают. Владелец сдаёт только женщинам и отдельно оговаривает: без студентов, без работающих в ночную смену, без детей и без животных.",
  "https://www.facebook.com/groups/563896434149922/posts/2367341113805436/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Room in a newly built house at Block 7, Quarry Road, Sewage, Pusok, Lapu-Lapu City — PHP 4,500 for two people, PHP 3,000 for one. Water is a fixed PHP 200 a month for single rooms and PHP 300 for doubles. One month in advance and one month deposit, six months minimum, and no reservations are held. The owner lets to women only and states plainly: no students, no night-shift workers, no children and no pets.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
