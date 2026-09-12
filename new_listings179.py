# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 6 строк, 2026-09-12.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * nhatrogiarenhat/2275943409685382 -- ha-noi/tyh, 6,000,000 VND: район назван в адресе поста
  * nhatrogiarenhat/2274703299809393 -- ha-noi/tyh, 6,000,000 VND: район назван в адресе поста
  * chungcuminigiarehanoii/1084119331277746 -- ha-noi/bd, 11,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1956617238748031 -- ho-chi-minh/ak, 24,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1896571768085912 -- ho-chi-minh/ak, 15,200,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1933826464360442 -- ho-chi-minh/ak, 14,500,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (20):
  * 2244337472845976 -- тип жилья в тексте не назван
  * 2267652187181171 -- продажа
  * 2273544739925249 -- тип жилья в тексте не назван
  * 2267841370495586 -- тип жилья в тексте не назван
  * 2251798492099874 -- тип жилья в тексте не назван
  * 29173961498872458 -- район не определяется по адресу «Vị trí thuận tiện»
  * 28659579656977314 -- тот же текст уже заведён: id new:chungcuminigiarehanoii/1084119331277746
  * 29164770296458245 -- тот же текст уже заведён: id new:nhatrogiarenhat/2275943409685382
  * 29148358604766081 -- тот же текст уже заведён: id new:nhatrogiarenhat/2274703299809393
  * 28960082756927001 -- тип жилья в тексте не назван
  * 29101311996137409 -- тип жилья в тексте не назван
  * 28471445119124103 -- тип жилья в тексте не назван
  * 1845768123408577 -- район не определяется по адресу «English below ⬇️»
  * 1851095799542476 -- тот же текст уже заведён: id 2000616
  * 1847508349901221 -- район не определяется по адресу «Nguyen Huu Canh Street»; прецедент расколот: «OPEN VIEW»: tm 1
  * 1956614132081675 -- район не определяется по адресу «Nguyen Huu Canh Street»
  * 1956339032109185 -- район не определяется по адресу «ORCHARD PARKVIEW»; прецедент расколот: «83M²»: ak 1; «22M»: ak 1
  * 1954711942271894 -- цены в посте нет
  * 1955781068831648 -- район не определяется по адресу «Trường Sa»; прецедент расколот: «50m²»: tm 2, ak 2, btr 1, th 1, bth 1; «Bright»: th 4, tm 4, ak 3, btr 2, kh 1
  * 1785204119222678 -- в посте несколько разных цен: 500,000, 12,000,000
"""
from listing_lock import insert_listings

IDS = [3000558, 3000559, 3000560, 3000561, 3000562, 3000563]

NEW_SRC = r'''
L(3000558,"ha-noi","tyh","Студия",6000000,None,
  "Студия, Tây Hồ.",
  "https://www.facebook.com/groups/nhatrogiarenhat/posts/2275943409685382/","сегодня",0,source="fbgroup",
  descEn="Studio, Tây Hồ.",
  details={"photos": ["assets/fb_photos/2275943409685382/01.webp", "assets/fb_photos/2275943409685382/02.webp", "assets/fb_photos/2275943409685382/03.webp", "assets/fb_photos/2275943409685382/04.webp", "assets/fb_photos/2275943409685382/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000559,"ha-noi","tyh","Студия",6000000,None,
  "Студия, Tây Hồ.",
  "https://www.facebook.com/groups/nhatrogiarenhat/posts/2274703299809393/","сегодня",0,source="fbgroup",
  descEn="Studio, Tây Hồ.",
  details={"photos": ["assets/fb_photos/2274703299809393/01.webp", "assets/fb_photos/2274703299809393/02.webp", "assets/fb_photos/2274703299809393/03.webp", "assets/fb_photos/2274703299809393/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000560,"ha-noi","bd","Квартира",11000000,45,
  "1-спальная квартира, 45 м², Ba Đình — 1 санузел.",
  "https://www.facebook.com/groups/chungcuminigiarehanoii/posts/1084119331277746/","сегодня",0,source="fbgroup",
  descEn="1-bedroom flat, 45 m², Ba Đình — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1084119331277746/01.webp", "assets/fb_photos/1084119331277746/02.webp", "assets/fb_photos/1084119331277746/03.webp", "assets/fb_photos/1084119331277746/04.webp", "assets/fb_photos/1084119331277746/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000561,"ho-chi-minh","ak","Квартира",24000000,90,
  "2-спальная квартира, 90 м², An Khánh — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1956617238748031/","сегодня",0,source="fbgroup",
  descEn="2-bedroom flat, 90 m², An Khánh — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1956617238748031/01.webp", "assets/fb_photos/1956617238748031/02.webp", "assets/fb_photos/1956617238748031/03.webp", "assets/fb_photos/1956617238748031/04.webp", "assets/fb_photos/1956617238748031/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000562,"ho-chi-minh","ak","Квартира",15200000,60,
  "1-спальная квартира, 60 м², An Khánh.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1896571768085912/","сегодня",0,source="fbgroup",
  descEn="1-bedroom flat, 60 m², An Khánh.",
  details={"photos": ["assets/fb_photos/1896571768085912/01.webp", "assets/fb_photos/1896571768085912/02.webp", "assets/fb_photos/1896571768085912/03.webp", "assets/fb_photos/1896571768085912/04.webp", "assets/fb_photos/1896571768085912/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000563,"ho-chi-minh","ak","Квартира",14500000,None,
  "1-спальная квартира, An Khánh.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1933826464360442/","сегодня",0,source="fbgroup",
  descEn="1-bedroom flat, An Khánh.",
  details={"photos": ["assets/fb_photos/1933826464360442/01.webp", "assets/fb_photos/1933826464360442/02.webp", "assets/fb_photos/1933826464360442/03.webp", "assets/fb_photos/1933826464360442/04.webp", "assets/fb_photos/1933826464360442/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
