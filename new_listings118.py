# -*- coding: utf-8 -*-
"""Первый настоящий заход по Facebook Marketplace, 4 сентября 2026.

Процедура -- facebook_check_prompt.txt. Заход шёл через залогиненный Chrome
владельца, лента Хошимина, сортировка по свежести, фильтр "не старше 7 дней",
радиус 30 км, включён переключатель "только от частных лиц"
(его URL-параметр -- isC2CListingOnly=1).

Из 14 объявлений ленты годными оказались 2, оба в Тхаодьене. Отсеяны:
3 продажи в разделе аренды (5,5 и 5,45 млрд ₫), покраска домов, несколько
объявлений без цены в тексте или без площади. Ещё одно ценное -- 3-спальная
квартира 108 м² в ЖК Ascentia (Phú Mỹ Hưng, 40 млн ₫/мес,
facebook.com/marketplace/item/890080047457513/) -- НЕ добавлено: у объявлений
формата "Rentals" Facebook не показывает возраст вообще, и подставлять
выдуманное число в поле даты было бы враньём в главном поле этого сайта.

Фотографий нет ни у одного: ссылки Facebook подписаны и живут ~4 дня.
Значит, эти строки не попадут в телеграм-хаб (--min-photos 3) и живут
только на сайте.
"""
from listing_lock import insert_listings

IDS = [1000386, 1000387]

NEW_SRC = '''
L(1000386,"ho-chi-minh","ak","Студия",13500000,38,
  "Сервисная студия 38 м² на улице 64, Тхаодьен (An Khánh) — интернет и уборка включены в стоимость, заселение сразу. Просмотр по договорённости с менеджером.",
  "https://www.facebook.com/marketplace/item/2620808191683838/","7 дней назад",7,source="fbmarketplace",
  descEn="Serviced studio, 38 m², on Street 64, Thảo Điền (An Khánh) — internet and cleaning included in the rent, available now. Viewings by arrangement with the manager.",
  details={"notice": "Цена взята из текста объявления (13,5 млн ₫/мес): в поле цены Facebook стоит «₫13,500» — площадка обрезает суммы, доверять её полю цены нельзя. Район в карточке Facebook указан как Тхудык, адрес в тексте — Тхаодьен. Facebook не публикует дату размещения. Объявление найдено 4 сентября 2026 в ленте с фильтром «не старше 7 дней», поэтому 7 дней — это верхняя граница возраста, а не дата публикации. Фотографий нет: ссылки на изображения Facebook подписаны и действуют около четырёх дней, сохранять их бессмысленно — смотрите фото по ссылке на объявление.", "noticeEn": "The price is taken from the ad text (13.5 million ₫/month): Facebook's own price field shows ₫13,500 — the platform mangles amounts and its price field cannot be trusted. Facebook files the ad under Thủ Đức while the address in the text is Thảo Điền. Facebook publishes no posting date. This ad was found on 4 September 2026 in a feed filtered to the last 7 days, so 7 days is an upper bound on its age, not a publication date. No photos: Facebook image URLs are signed and last about four days, so storing them is pointless — see the photos on the listing itself."}),
L(1000387,"ho-chi-minh","ak","Квартира",14000000,40,
  "1-спальная квартира 40 м² (1 санузел) рядом с улицей Xuân Thủy, Тхаодьен (An Khánh) — в стоимость включены быстрый интернет, парковка, регулярная уборка и эксплуатационный сбор. Состояние — как новое.",
  "https://www.facebook.com/marketplace/item/946687877778613/","7 дней назад",7,source="fbmarketplace",
  descEn="1-bedroom apartment, 40 m² (1 bathroom), near Xuân Thủy St, Thảo Điền (An Khánh) — high-speed internet, parking, regular cleaning and the management fee are all included in the rent. Condition: like new.",
  details={"notice": "Цена взята из заголовка и текста объявления (14 млн ₫/мес): в поле цены Facebook стоит «₫1,400,000», в десять раз меньше. Район в карточке Facebook указан как Кв. 3, адрес в тексте — Тхаодьен. Facebook не публикует дату размещения. Объявление найдено 4 сентября 2026 в ленте с фильтром «не старше 7 дней», поэтому 7 дней — это верхняя граница возраста, а не дата публикации. Фотографий нет: ссылки на изображения Facebook подписаны и действуют около четырёх дней, сохранять их бессмысленно — смотрите фото по ссылке на объявление.", "noticeEn": "The price is taken from the ad's title and body (14 million ₫/month): Facebook's price field says ₫1,400,000, ten times too little. Facebook files the ad under District 3 while the address in the text is Thảo Điền. Facebook publishes no posting date. This ad was found on 4 September 2026 in a feed filtered to the last 7 days, so 7 days is an upper bound on its age, not a publication date. No photos: Facebook image URLs are signed and last about four days, so storing them is pointless — see the photos on the listing itself."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
