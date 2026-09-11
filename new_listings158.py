# -*- coding: utf-8 -*-
"""Группы Facebook: первая строка, которую собрала сама программа, 11 сентября 2026.

До этого дня ночной прогон не собрал из групп ни одного поста: профиль программы
был не залогинен, а после входа прежний код листал ленту и вернул ноль. Кандидата
дал новый путь fb_collect.py -- поиск по группе и JSON из <script> -- на группе
HOUSE AND ROOMS FOR RENT DUMAGUETE: 13 постов, 2 прошли отбор.

РАЙОН -- ИЗ САМОГО ПОСТА: «Upper Batinguel Dumaguete City», у сайта есть btg.
Второй кандидат (G & B Navarro, Umbac Subdivision, Calindagan) не заведён:
района Calindagan на сайте нет, и прецедента тоже нет.

ТИП -- «Квартира», а не «Дом»: сдаётся только нижний этаж («Bottom part lang
(SILONG RA)») с двумя спальнями, кухней, санузлом и гостиной.

ФОТО -- ВЛОЖЕНИЯ САМОГО ПОСТА, скачанные программой и лежащие на сайте. Это первая
строка из группы с фото: у 65 прежних их нет, потому что ссылки Facebook живут
около четырёх дней. Сверено глазами: дом с жилым низом за белым забором и та же
комната «Before with gamit...», что в посте. Папка assets/fb_photos в .gitignore,
поэтому эта папка добавлена в git явно.
"""
from listing_lock import insert_listings

IDS = [3000462]

NEW_SRC = r'''
L(3000462,"dumaguete","btg","Квартира",6500,None,
  "Нижний этаж дома в Верхнем Батингеле, напротив главных ворот Katrina Homes phase 1 — 2 спальни, санузел, кухня и гостиная, место для парковки, свои счётчики на электричество и воду. Депозит за два месяца, осмотр в любое время по договорённости.",
  "https://www.facebook.com/groups/1996683940588782/posts/4606474172943066/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="The ground floor of a house in Upper Batinguel, opposite the main gate of Katrina Homes phase 1 — 2 bedrooms, a bathroom, a kitchen and a living room, a parking space, and separate electricity and water meters. Two months' deposit, viewing any time by arrangement.",
  details={"photos": ["assets/fb_photos/4606474172943066/01.webp", "assets/fb_photos/4606474172943066/02.webp", "assets/fb_photos/4606474172943066/03.webp", "assets/fb_photos/4606474172943066/04.webp", "assets/fb_photos/4606474172943066/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения группа не отдаёт: в данных страницы её нет, а видимые метки времени принадлежат комментариям. Указанный возраст — это время с проверки: 11 сентября 2026 объявление было открыто по ссылке и подтверждено живым. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цена в филиппинских песо, как в посте.", "noticeEn": "Source: a post in a Facebook group. The group gives no exact posting date — it is absent from the page data, and the visible timestamps belong to comments. The age shown is time since verification: on 11 September 2026 the listing was opened by its link and confirmed live. The photos come from the post itself and are stored on this site, because Facebook's image links are signed and expire in about four days. The price is in Philippine pesos, as in the post."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
