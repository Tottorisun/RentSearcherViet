# -*- coding: utf-8 -*-
"""Группы Facebook по Вьетнаму: Тхао Дьен, 8 сентября 2026, 5 объявлений.

Первые вьетнамские строки из групп. До сегодняшнего дня Вьетнам на сайте (1510
объявлений) держался на Chợ Tốt и Batdongsan, из Facebook там было ровно два
объявления и ни одного из групп -- при том что владелец состоит в девяти
вьетнамских группах.

ПОЧЕМУ ИМЕННО ТХАО ДЬЕН. Хошимин на сайте -- это не весь город, а семь районов,
совпадающих с зоной личного поиска владельца. Поэтому и в группах искали не
«аренду вообще», а по названиям этих районов: Thảo Điền, An Phú, Phú Mỹ Hưng,
Thanh Đa. Старые названия ложатся на новые ключи так (сверено по описаниям уже
заведённых строк): Тхао Дьен и Ан Фу -> ak (Phường An Khánh), Ан Фу -> btr
(Bình Trưng), Фу Ми Хынг -> tm и th, Тхань Да -> bq.

ЧЕМ ВЬЕТНАМСКИЕ ГРУППЫ ОТЛИЧАЮТСЯ ОТ ФИЛИППИНСКИХ. Шума заметно больше: половина
выдачи -- продажа (bán), посуточная сдача и сервисные апартаменты, которых сайт
не берёт. Зато нашлась коммерция в том самом Тхао Дьене, которой в Chợ Tốt по
этому району почти нет: витрина на Xuân Thủy, офисное здание и дом под офис.

Одно объявление отброшено, хотя адрес и описание хорошие: 1PN на 1 Đường số 64,
Тхао Дьен -- в посте нет цены вообще, а без неё строка не сравнима и выпадает из
фильтра бюджета.

ЦЕНА В ДОЛЛАРАХ. У дома на 10x11 м цена объявлена в USD, и она так и заведена:
cur="USD". Валюта уже поддержана -- есть в rates.json и в CUR_SYM, а в строке
пересчёта своя валюта не дублируется. Пересчитывать в донги значило бы выдумать
курс за владельца.

ДАТЫ нет, как и у филиппинских групп: источник fbgroup освобождён от чистки по
возрасту, daysAgo=0 и подпись «сегодня» означают «сегодня проверено». Все пять
открыты по прямой ссылке и подтверждены живыми.
"""
from listing_lock import insert_listings

IDS = [1000575, 1000576, 1000577, 1000578, 1000579]

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
L(1000575,"ho-chi-minh","ak","Квартира",25000000,110,
  "1-спальный пентхаус 110 м² рядом с улицей Суантхюи, Тхао Дьен — полная меблировка, свободен сразу. В стоимость входят уборка раз в неделю, парковка и быстрый интернет. В центре Тхао Дьена: международные школы, супермаркеты и кафе рядом.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1806478077337582/","сегодня",0,source="fbgroup",
  descEn="One-bedroom penthouse of 110 m² near Xuân Thủy street, Thảo Điền — fully furnished and available now. Weekly cleaning, parking and high-speed internet are included in the rent. In the heart of Thảo Điền, with international schools, supermarkets and cafés nearby.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(1000576,"ho-chi-minh","ak","Студия",13000000,None,
  "Студия в новом доме Aura Living на улице 60, Тхао Дьен — 17 студий, балкон, полная меблировка. В доме лифт, спортзал, сад и питьевая вода из-под крана. Цена указана как начальная: 13 000 000 ₫, конкретная зависит от юнита.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1850976909554365/","сегодня",0,source="fbgroup",
  descEn="Studio at Aura Living, a new building on Street 60, Thảo Điền — 17 studios, each with a balcony and fully furnished. The building has a lift, a gym, a garden and filtered drinking water on tap. The price is quoted as a starting figure of ₫13,000,000; the exact rent depends on the unit.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(1000577,"ho-chi-minh","ak","Торговая площадь",160000000,150,
  "Помещение с витриной на первой линии улицы Суантхюи, Тхао Дьен — пятно 10 на 15 м, первый этаж плюс один. Оживлённая центральная улица района, много иностранцев, помещение хорошо заметно с дороги. Под ресторан, кофейню, шоурум, спа или магазин.",
  "https://www.facebook.com/groups/2439677179643705/posts/4644169972527737/","сегодня",0,source="fbgroup",
  descEn="Shopfront premises on the Xuân Thủy frontage in Thảo Điền — a 10 by 15 m footprint over a ground floor plus one. A busy central street of the district with a large foreign community and high visibility from the road. Suited to a restaurant, café, showroom, spa or shop.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(1000578,"ho-chi-minh","ak","Офис",70000000,70,
  "Помещение под офис в Тхао Дьене — пятно 3,5 на 20 м, первый этаж плюс три. Подойдёт под офис, шоурум, спа или магазин. Депозит за три месяца, оплата помесячно.",
  "https://www.facebook.com/groups/2439677179643705/posts/4680245392253528/","сегодня",0,source="fbgroup",
  descEn="Office premises in Thảo Điền — a 3.5 by 20 m footprint over a ground floor plus three. Suited to an office, showroom, spa or shop. Three months' deposit, paid monthly.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
L(1000579,"ho-chi-minh","ak","Офис",3300,110,
  "Дом под офис в Тхао Дьене — пятно 10 на 11 м, первый этаж плюс два, помещение пустое, заезжать можно сразу. Тихий жилой квартал с удобным подъездом на машине. Владелец предлагает под офис компании, шоурум или студию — то есть под дело, которому не нужна витрина на людной улице.",
  "https://www.facebook.com/groups/2439677179643705/posts/4625048791106522/","сегодня",0,source="fbgroup",cur="USD",
  descEn="House let as office space in Thảo Điền — a 10 by 11 m footprint over a ground floor plus two, empty and ready to occupy. A quiet residential block with easy car access. The owner offers it for a company office, a showroom or a studio: a business that does not need a busy street frontage.",
  details={"notice":"RU_N","noticeEn":"EN_N"}),
'''

NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
