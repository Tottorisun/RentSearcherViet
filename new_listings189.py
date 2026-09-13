# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 9 строк, 2026-09-13.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * nhatrocantho/38776853001913132 -- can-tho/crg, 8,000,000 VND: район назван в адресе поста
  * 563896434149922/2373197543219793 -- cebu/cap, 35,000 PHP: район назван в адресе поста
  * 1735327053393688/4529600670632965 -- cebu/prd, 15,000 PHP: район назван в адресе поста
  * 211616406116962/2069351513676766 -- da-lat/xh, 2,800,000 VND: улица Lương Thế Vinh: 4 из 4 отрезков в xh
  * chothuenhataihaiphong/4507882599462896 -- hai-phong/lch, 7,000,000 VND: район назван в адресе поста
  * chothuenhataihaiphong/4507342216183601 -- hai-phong/lch, 6,500,000 VND: район назван в адресе поста
  * phongtrosvhue/1739874880555153 -- hue/vyd, 8,500,000 VND: район назван в адресе поста
  * phongtrosvhue/1550648672811109 -- hue/vyd, 3,700,000 VND: район назван в адресе поста
  * chothuecanhogiarenhatrang/2060280514806050 -- nha-trang/tl, 15,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (145):
  * 3474885602689740 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 3489735917871375 -- это поиск жилья, а не предложение
  * 3111524002383926 -- это поиск жилья, а не предложение
  * 2984311105105217 -- в посте несколько разных цен: 5,500,000, 6,000,000
  * 39126175940314168 -- район не определяется по адресу «🏩 MINIHOUSE LUXURY FULL NỘI THẤT ĐƯỜNG VÕ VĂN KIỆT»; прецедент расколот: «KIỆT»: ckh 3, ltu 1, crg 1, anb 1
  * 39164774486454313 -- район не определяется по адресу «MINIHOUSE LUXURY FULL NỘI THẤT ĐƯỜNG VÕ VĂN KIỆT -»; прецедент расколот: «KIỆT»: ckh 3, ltu 1, crg 1, anb 1
  * 38629798796618554 -- тип жилья в тексте не назван
  * 37988563517408755 -- тип жилья в тексте не назван
  * 38206461175618987 -- тип жилья в тексте не назван
  * 1725575419175091 -- тип жилья в тексте не назван
  * 1725714562494510 -- тип жилья в тексте не назван
  * 1725537895845510 -- тип жилья в тексте не назван
  * 1715148420217791 -- тип жилья в тексте не назван
  * 1737136038019029 -- район не определяется по адресу «♥️Ưu đãi giảm 300k tháng đầu tiên!»
  * 1753359733063326 -- продажа
  * 1753319426400690 -- район не определяется по адресу «♥️Ưu đãi 3 tháng đầu giảm 200k/tháng!»
  * 1753370626395570 -- уже на сайте: id 3000545
  * 1753257533073546 -- уже на сайте: id 3000546
  * 1744926680573298 -- тип жилья в тексте не назван
  * 1730244832041483 -- тип жилья в тексте не назван
  * 1669709601428340 -- уже на сайте: id 3000547
  * 2370556600150554 -- район не определяется по адресу «OPEN FOR VIEWING NOW❗️❗️😍»
  * 2371615766711304 -- в тексте есть и другая цена того же порядка: 7,833 против 18,000
  * 2370267693512778 -- район не определяется по адресу «🔥 FOR RENT APARTMENT IN AS FORTUNA LAST UNIT LEFT »
  * 2351777795361768 -- уже на сайте: id 2000614
  * 2372027243336823 -- уже на сайте: id 3000548
  * 4541720556087643 -- продажа
  * 4508302629429436 -- продажа
  * 4521497431443289 -- район не определяется по адресу «Bulacao Luyo Prince Warehouse»
  * 2366453963894151 -- в тексте есть и другая цена того же порядка: 2,500 против 3,000
  * 2371025860103628 -- район не определяется по адресу «Ready for viewing na❗»
  * 2369999990206215 -- тот же текст уже заведён: id 3000578
  * 2125924031352847 -- нет ни одной скачанной фотографии
  * 2124332511511999 -- тип жилья в тексте не назван
  * 2103298020282115 -- тип жилья в тексте не назван
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 2076569656288285 -- район не определяется по адресу «Nguyễn An Ninh»
  * 3738232963000471 -- тип жилья в тексте не назван
  * 3654240948066340 -- тип жилья в тексте не назван
  * 3743941329096301 -- тип жилья в тексте не назван
  * 3672523882904713 -- район не определяется по адресу «Nguyễn An Ninh»
  * 2211213676172958 -- уже на сайте: id 2000615
  * 2204094880218171 -- в посте несколько разных цен: 15,000,000, 23,000,000
  * 2207673073193685 -- в посте несколько разных цен: 11,000,000, 11,500,000
  * 4607702726153544 -- район не определяется по адресу «🔑 FURNISHED UNIT FOR RENT»
  * 4540691986187952 -- уже на сайте: id 3000549
  * 2220626071843571 -- нет ни одной скачанной фотографии
  * 2227834604456051 -- уже на сайте: id 3000550
  * 2199887580584087 -- тот же текст уже заведён: id 3000549
  * 2205044503401728 -- уже на сайте: id 3000551
  * 2229008354338676 -- район не определяется по адресу «YOUR NEXT HOME: NEW 3BR HOUSE FOR RENT»
  * 2184459758793536 -- нет ни одной скачанной фотографии
  * 2244337472845976 -- тип жилья в тексте не назван
  * 2267652187181171 -- продажа
  * 2275943409685382 -- уже на сайте: id 3000558
  * 2274703299809393 -- тот же текст уже заведён: id 3000559
  * 2273544739925249 -- тип жилья в тексте не назван
  * 2267841370495586 -- тип жилья в тексте не назван
  * 2251798492099874 -- тип жилья в тексте не назван
  * 1084119331277746 -- уже на сайте: id 3000560
  * 29173961498872458 -- район не определяется по адресу «Vị trí thuận tiện»
  * 28659579656977314 -- тот же текст уже заведён: id 3000560
  * 29164770296458245 -- тот же текст уже заведён: id 3000558
  * 29148358604766081 -- тот же текст уже заведён: id 3000559
  * 28960082756927001 -- тип жилья в тексте не назван
  * 29101311996137409 -- тип жилья в тексте не назван
  * 28471445119124103 -- тип жилья в тексте не назван
  * 1085668984456114 -- тип жилья в тексте не назван
  * 28678125855132147 -- район не определяется по адресу «T2302 Cho thuê nhà Thiên Lôi»
  * 28714148764863189 -- район не определяется по адресу «🇻🇳 │ LÊ HỒNG PHONG»
  * 4504818996435923 -- район не определяется по адресу «Vị trí gần Trung tâm thành phố»
  * 4508075062776983 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 1845768123408577 -- район не определяется по адресу «English below ⬇️»
  * 1851095799542476 -- тот же текст уже заведён: id 2000616
  * 1847508349901221 -- нет ни одной скачанной фотографии
  * 1855181912467198 -- район не определяется по адресу «Ton Duc Thang»; прецедент расколот: «80m²»: btr 2, th 1, tm 1, ak 1
  * 1956614132081675 -- район не определяется по адресу «Nguyen Huu Canh Street»
  * 1956339032109185 -- район не определяется по адресу «ORCHARD PARKVIEW»; прецедент расколот: «83M²»: ak 1; «22M»: ak 1
  * 1956617238748031 -- уже на сайте: id 3000561
  * 1954711942271894 -- цены в посте нет
  * 1955781068831648 -- район не определяется по адресу «Trường Sa»
  * 1896571768085912 -- уже на сайте: id 3000562
  * 1785204119222678 -- в посте несколько разных цен: 500,000, 12,000,000
  * 1933826464360442 -- уже на сайте: id 3000563
  * 1957269865349435 -- цены в посте нет
  * 1956780812065007 -- район не определяется по адресу «Thang Long Street»
  * 1948466112896477 -- в посте несколько разных цен: 6,000,000, 30,000,000
  * 1957270682016020 -- похоже на уже заведённое: id 1000761
  * 1956968145379607 -- в посте несколько разных цен: 1,500,000, 18,000,000
  * 2008451673166549 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 1993632857981764 -- нет ни одной скачанной фотографии
  * 1698562345035849 -- район не определяется по адресу «Căn hộ 1 phòng ngủ có ban công»; прецедент расколот: «Street»: ha 1
  * 2008854763126240 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 1693044982254252 -- в тексте есть и другая цена того же порядка: 7,500,000 против 15,000,000
  * 1947495812624862 -- район не определяется по адресу «STUDIO FULL NỘI THẤT»
  * 1978625339511909 -- уже на сайте: id 3000552
  * 1997802540927522 -- район не определяется по адресу «đường Tố Hữu»
  * 1950365399004570 -- похоже на уже заведённое: id 3000552
  * 1699463947929580 -- уже на сайте: id 3000553
  * 1708277650381543 -- район не определяется по адресу «CHO THUÊ STUDIO CAO CẤP»
  * 1701057297770245 -- тип жилья в тексте не назван
  * 1637646127444696 -- район не определяется по адресу «Không gian sống hiện đại»
  * 1251745672701412 -- в посте несколько разных цен: 4,000,000, 4,500,000, 4,800,000
  * 2571419586635461 -- похоже на уже заведённое: id 3000257
  * 2573848076392612 -- уже на сайте: id 3000554
  * 2571853679925385 -- район не определяется по адресу «Looking for your own home or an extra property for»
  * 2390246748383632 -- нет ни одной скачанной фотографии
  * 2395927144482259 -- нет ни одной скачанной фотографии
  * 2395848701156770 -- район не определяется по адресу «Fully Furnished 1 Bedroom Condo Unit For Rent - Un»
  * 2488180458292708 -- тот же текст уже заведён: id 3000579
  * 2580908829019870 -- в посте несколько разных цен: 10,000, 15,000
  * 2394379184637055 -- в тексте есть и другая цена того же порядка: 6,000, 6,500 против 15,000
  * 2395247541216886 -- ищут соседа, а не сдают
  * 2396059584469015 -- нет ни одной скачанной фотографии
  * 2060438324790269 -- район не определяется по адресу «Pham Ngoc Thach Street - Nha Trang»
  * 2031470527687049 -- район не определяется по адресу «Prime central location»
  * 2054398412060927 -- это поиск жилья, а не предложение
  * 2057440031756765 -- нет ни одной скачанной фотографии
  * 2058852521615516 -- нет ни одной скачанной фотографии
  * 2579623245791664 -- район не определяется по адресу «the prestigious Meyhomes community»
  * 2586447371775918 -- помещение под бизнес или здание целиком, а не жильё
  * 1756168655595818 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1755470302332320 -- уже на сайте: id 3000555
  * 1757293212150029 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 2588230074930981 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 3273225212888572 -- район не определяется по адресу «Khu đô thị An Phú Thịnh»
  * 2126105611361434 -- в посте несколько разных цен: 10,000,000, 13,000,000
  * 2119050485400280 -- это поиск жилья, а не предложение
  * 2126688371303158 -- район не определяется по адресу «Khu đô thị An Phú Thịnh»
  * 3255608651316895 -- район не определяется по адресу «Ngay Đại học FPT»
  * 2113640639274598 -- нет ни одной скачанной фотографии
  * 2106615719977090 -- нет ни одной скачанной фотографии
  * 1445448987399170 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»
  * 1463642598913142 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 1461245469152855 -- район не определяется по адресу «APARTMENT FOR RENT»
  * 3213120192216198 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»
  * 3236985219829695 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 3236874719840745 -- помещение под бизнес или здание целиком, а не жильё
  * 3203441086517442 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ»
  * 3232506143610936 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 3230379787156905 -- район не определяется по адресу «36/.. lương văn can»
  * 3214918155369735 -- в посте несколько разных цен: 3,500,000, 4,200,000
  * 3170988256429392 -- район не определяется по адресу «gồm 1 phòng ngủ»
  * 3161796947348523 -- район не определяется по адресу «**CHO THUÊ CĂN HỘ MINI ĐƯỜNG THỐNG NHẤT»
  * 1452094226734646 -- район не определяется по адресу «✅Cho thuê nhà phố - Dạng biệt thự mini đường Ngô Đ»
"""
from listing_lock import insert_listings

IDS = [3000602, 3000603, 3000604, 3000605, 3000606, 3000607, 3000608, 3000609, 3000610]

NEW_SRC = r'''
L(3000602,"can-tho","crg","Квартира",8000000,None,
  "1-спальная квартира, Cái Răng.",
  "https://www.facebook.com/groups/nhatrocantho/posts/38776853001913132/","сегодня",0,source="fbgroup",
  descEn="1-bedroom flat, Cái Răng.",
  details={"photos": ["assets/fb_photos/38776853001913132/01.webp", "assets/fb_photos/38776853001913132/02.webp", "assets/fb_photos/38776853001913132/03.webp", "assets/fb_photos/38776853001913132/04.webp", "assets/fb_photos/38776853001913132/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000603,"cebu","cap","Квартира",35000,42,
  "1-спальная квартира, 42 м², Capitol Site.",
  "https://www.facebook.com/groups/563896434149922/posts/2373197543219793/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="1-bedroom flat, 42 m², Capitol Site.",
  details={"photos": ["assets/fb_photos/2373197543219793/01.webp", "assets/fb_photos/2373197543219793/02.webp", "assets/fb_photos/2373197543219793/03.webp", "assets/fb_photos/2373197543219793/04.webp", "assets/fb_photos/2373197543219793/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000604,"cebu","prd","Квартира",15000,None,
  "3-спальная квартира, Пардо.",
  "https://www.facebook.com/groups/1735327053393688/posts/4529600670632965/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="3-bedroom flat, Пардо.",
  details={"photos": ["assets/fb_photos/4529600670632965/01.webp", "assets/fb_photos/4529600670632965/02.webp", "assets/fb_photos/4529600670632965/03.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000605,"da-lat","xh","Комната",2800000,None,
  "Комната, Lương Thế Vinh, Xuân Hương - Đà Lạt.",
  "https://www.facebook.com/groups/211616406116962/posts/2069351513676766/","сегодня",0,source="fbgroup",
  descEn="Room, Lương Thế Vinh, Xuân Hương - Đà Lạt.",
  details={"photos": ["assets/fb_photos/2069351513676766/01.webp", "assets/fb_photos/2069351513676766/02.webp", "assets/fb_photos/2069351513676766/03.webp", "assets/fb_photos/2069351513676766/04.webp", "assets/fb_photos/2069351513676766/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3000606,"hai-phong","lch","Квартира",7000000,40,
  "1-спальная квартира, 40 м², Lê Chân — 1 санузел.",
  "https://www.facebook.com/groups/chothuenhataihaiphong/posts/4507882599462896/","сегодня",0,source="fbgroup",
  descEn="1-bedroom flat, 40 m², Lê Chân — 1 bathroom.",
  details={"photos": ["assets/fb_photos/4507882599462896/01.webp", "assets/fb_photos/4507882599462896/02.webp", "assets/fb_photos/4507882599462896/03.webp", "assets/fb_photos/4507882599462896/04.webp", "assets/fb_photos/4507882599462896/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000607,"hai-phong","lch","Квартира",6500000,30,
  "1-спальная квартира, 30 м², Lê Chân — 1 санузел.",
  "https://www.facebook.com/groups/chothuenhataihaiphong/posts/4507342216183601/","сегодня",0,source="fbgroup",
  descEn="1-bedroom flat, 30 m², Lê Chân — 1 bathroom.",
  details={"photos": ["assets/fb_photos/4507342216183601/01.webp", "assets/fb_photos/4507342216183601/02.webp", "assets/fb_photos/4507342216183601/03.webp", "assets/fb_photos/4507342216183601/04.webp", "assets/fb_photos/4507342216183601/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000608,"hue","vyd","Квартира",8500000,64,
  "2-спальная квартира, 64 м², Vỹ Dạ — 2 санузла.",
  "https://www.facebook.com/groups/phongtrosvhue/posts/1739874880555153/","сегодня",0,source="fbgroup",
  descEn="2-bedroom flat, 64 m², Vỹ Dạ — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1739874880555153/01.webp", "assets/fb_photos/1739874880555153/02.webp", "assets/fb_photos/1739874880555153/03.webp", "assets/fb_photos/1739874880555153/04.webp", "assets/fb_photos/1739874880555153/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000609,"hue","vyd","Квартира",3700000,53,
  "Квартира, 53 м², Vỹ Dạ — 1 санузел.",
  "https://www.facebook.com/groups/phongtrosvhue/posts/1550648672811109/","сегодня",0,source="fbgroup",
  descEn="Flat, 53 m², Vỹ Dạ — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1550648672811109/01.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000610,"nha-trang","tl","Квартира",15000000,62,
  "2-спальная квартира, 62 м², Tân Lập — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2060280514806050/","сегодня",0,source="fbgroup",
  descEn="2-bedroom flat, 62 m², Tân Lập — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/2060280514806050/01.webp", "assets/fb_photos/2060280514806050/02.webp", "assets/fb_photos/2060280514806050/03.webp", "assets/fb_photos/2060280514806050/04.webp", "assets/fb_photos/2060280514806050/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
