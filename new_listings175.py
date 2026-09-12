# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 11 строк, 2026-09-12.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 674135380985772/1753370626395570 -- can-tho/hpu, 3,500,000 VND: район назван в адресе поста
  * 674135380985772/1753257533073546 -- can-tho/hpu, 3,500,000 VND: район назван в адресе поста
  * 674135380985772/1669709601428340 -- can-tho/nki, 2,800,000 VND: район назван в адресе поста
  * 563896434149922/2372027243336823 -- cebu/gua, 30,000 PHP: район назван в адресе поста
  * 1996683940588782/4540691986187952 -- dumaguete/bcg, 18,000 PHP: район назван в адресе поста
  * 153191128587086/2227834604456051 -- dumaguete/sib, 75,000 PHP: район назван в адресе поста
  * 153191128587086/2205044503401728 -- dumaguete/val, 26,000 PHP: район назван в адресе поста
  * phongtrochothuehue/1978625339511909 -- hue/acu, 2,800,000 VND: район назван в адресе поста
  * phongtrosvhue/1699463947929580 -- hue/vyd, 6,000,000 VND: район назван в адресе поста
  * 224805677963542/2573848076392612 -- manila/mak, 35,000 PHP: район назван в адресе поста
  * 472474987298531/1755470302332320 -- phu-quoc/ath, 5,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (129):
  * 3474885602689740 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 3489735917871375 -- это поиск жилья, а не предложение
  * 3111524002383926 -- это поиск жилья, а не предложение
  * 2984311105105217 -- в посте несколько разных цен: 5,500,000, 6,000,000
  * 38776853001913132 -- район не определяется по адресу «CHO THUÊ CĂN HỘ CARA RIVER PARK»
  * 39126175940314168 -- район не определяется по адресу «🏩 MINIHOUSE LUXURY FULL NỘI THẤT ĐƯỜNG VÕ VĂN KIỆT»; прецедент расколот: «KIỆT»: ckh 1, ltu 1, crg 1
  * 39164774486454313 -- район не определяется по адресу «MINIHOUSE LUXURY FULL NỘI THẤT ĐƯỜNG VÕ VĂN KIỆT -»; прецедент расколот: «KIỆT»: ckh 1, ltu 1, crg 1
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
  * 1744926680573298 -- тип жилья в тексте не назван
  * 1730244832041483 -- тип жилья в тексте не назван
  * 2368220717050809 -- район не определяется по адресу «Oprra Unit 1 Kalunasan Cebu City»
  * 2372909199915294 -- уже на сайте: id 3000527
  * 2371615766711304 -- в тексте есть и другая цена того же порядка: 7,833 против 18,000
  * 2369556196917261 -- уже на сайте: id 3000528
  * 2370296823509865 -- уже на сайте: id 3000529
  * 2351777795361768 -- уже на сайте: id 2000614
  * 4528691044057261 -- уже на сайте: id 3000239
  * 1808557076990144 -- уже на сайте: id 3000531
  * 2373197543219793 -- район не определяется по адресу «Baseline Residences»
  * 2370556600150554 -- район не определяется по адресу «OPEN FOR VIEWING NOW❗️❗️😍»
  * 2370267693512778 -- район не определяется по адресу «🔥 FOR RENT APARTMENT IN AS FORTUNA LAST UNIT LEFT »
  * 4541720556087643 -- продажа
  * 4529600670632965 -- район не определяется по адресу «Saint Jude acres Subd»; прецедент расколот: «Bulacao»: tls 1, prd 1
  * 4508302629429436 -- продажа
  * 4521497431443289 -- район не определяется по адресу «Bulacao Luyo Prince Warehouse»
  * 2125924031352847 -- нет ни одной скачанной фотографии
  * 2124332511511999 -- тип жилья в тексте не назван
  * 2069351513676766 -- район не определяется по адресу «Em còn 1 phòng cho thuê đường Lương Thế Vinh»
  * 2103298020282115 -- тип жилья в тексте не назван
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 2076569656288285 -- район не определяется по адресу «Nguyễn An Ninh»
  * 3738232963000471 -- тип жилья в тексте не назван
  * 3654240948066340 -- тип жилья в тексте не назван
  * 3743941329096301 -- тип жилья в тексте не назван
  * 3672523882904713 -- район не определяется по адресу «Nguyễn An Ninh»
  * 2203496343611358 -- уже на сайте: id 3000541
  * 2214424259185233 -- район не определяется: «Apartment Details, The Ponte, Da Nang»
  * 2211064666187859 -- уже на сайте: id 3000542
  * 2207115733249419 -- уже на сайте: id 3000543
  * 2204094880218171 -- в посте несколько разных цен: 15,000,000, 23,000,000
  * 2211213676172958 -- уже на сайте: id 2000615
  * 2207673073193685 -- в посте несколько разных цен: 11,000,000, 11,500,000
  * 4606474172943066 -- уже на сайте: id 3000462
  * 4606662779590872 -- район не определяется по адресу «the 2nd floor of Building C at G & B Navarro Apart»
  * 2231309210775257 -- уже на сайте: id 3000523
  * 2220626071843571 -- район не определяется по адресу «HOUSE FOR RENT - CANTIL-E»
  * 2225051174734394 -- уже на сайте: id 3000190
  * 2228726647700180 -- уже на сайте: id 3000525
  * 2223649681541210 -- уже на сайте: id 3000526
  * 2184459758793536 -- район не определяется по адресу «A Quiet refreshing Environment of Lower Cantil e(n»; прецедент расколот: «Diversion»: cdw 1
  * 2222417241664454 -- тип жилья в тексте не назван
  * 4607702726153544 -- район не определяется по адресу «🔑 FURNISHED UNIT FOR RENT»
  * 2199887580584087 -- тот же текст уже заведён: id new:1996683940588782/4540691986187952
  * 28678125855132147 -- район не определяется по адресу «T2302 Cho thuê nhà Thiên Lôi»
  * 28714148764863189 -- район не определяется по адресу «🇻🇳 │ LÊ HỒNG PHONG»
  * 4504818996435923 -- район не определяется по адресу «Vị trí gần Trung tâm thành phố»
  * 4508075062776983 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 4507882599462896 -- район не определяется по адресу «✨ Cho thuê căn hộ ở WaterFront City»
  * 4507342216183601 -- район не определяется по адресу «Cho thuê căn hộ tại KĐT WaterFront City»
  * 1847508349901221 -- район не определяется по адресу «Nguyen Huu Canh Street»
  * 1840738980578158 -- уже на сайте: id 3000534
  * 1846023873383002 -- район не определяется по адресу «Thach Thi Thanh»; прецедент расколот: «~50M²»: tm 2, ak 2, btr 1, th 1, bth 1
  * 1802133711105352 -- уже на сайте: id 3000535
  * 1802247057760684 -- уже на сайте: id 3000536
  * 1853708945947828 -- уже на сайте: id 3000537
  * 1801592087826181 -- уже на сайте: id 3000538
  * 1845768123408577 -- район не определяется по адресу «English below ⬇️»
  * 1851095799542476 -- тот же текст уже заведён: id 2000616
  * 1855181912467198 -- район не определяется по адресу «Ton Duc Thang»; прецедент расколот: «80m²»: btr 2, th 1, tm 1, ak 1
  * 2008451673166549 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 1993632857981764 -- нет ни одной скачанной фотографии
  * 1698562345035849 -- район не определяется по адресу «Căn hộ 1 phòng ngủ có ban công»; прецедент расколот: «Street»: ha 1
  * 1947495812624862 -- район не определяется по адресу «STUDIO FULL NỘI THẤT»
  * 1997802540927522 -- район не определяется по адресу «đường Tố Hữu»
  * 1950365399004570 -- похоже на уже заведённое: id new:phongtrochothuehue/1978625339511909
  * 1739874880555153 -- район не определяется по адресу «CHO THUÊ CĂN HỘ MANOR CROWN»; прецедент расколот: «TỐ HỮU»: acu 2, vyd 1
  * 1708277650381543 -- район не определяется по адресу «CHO THUÊ STUDIO CAO CẤP»
  * 1701057297770245 -- тип жилья в тексте не назван
  * 1550648672811109 -- район не определяется по адресу «CHO THUÊ GẤP CHUNG CƯ VICOLAND CÓ NỘI THẤT»
  * 1637646127444696 -- район не определяется по адресу «Không gian sống hiện đại»
  * 1251745672701412 -- в посте несколько разных цен: 4,000,000, 4,500,000, 4,800,000
  * 2576071049503648 -- продажа в рассрочку, а не аренда
  * 2575869156190504 -- уже на сайте: id 3000532
  * 2572896956487724 -- район не определяется по адресу «Condo Unit in Wilshire Plaza»
  * 2579759342468152 -- уже на сайте: id 3000533
  * 2390246748383632 -- район не определяется по адресу «FOR RENT - 1BR-APARMENT UNIT IN SAMPALOC MANILA.»
  * 2395927144482259 -- район не определяется по адресу «2-BEDROOM APARTMENT FOR RENT»
  * 2395247541216886 -- ищут соседа, а не сдают
  * 2571419586635461 -- похоже на уже заведённое: id 3000257
  * 2571853679925385 -- район не определяется по адресу «Looking for your own home or an extra property for»
  * 2395848701156770 -- район не определяется по адресу «Fully Furnished 1 Bedroom Condo Unit For Rent - Un»
  * 2055592715274830 -- район не определяется по адресу «Cu Chi - Nha Trang»
  * 2052488255585276 -- район не определяется по адресу «Enjoy a beautiful living space with a stunning sea»
  * 2053340292166739 -- уже на сайте: id 2000617
  * 2050739092426859 -- уже на сайте: id 3000539
  * 2058946284939473 -- уже на сайте: id 3000540
  * 2060438324790269 -- район не определяется по адресу «Pham Ngoc Thach Street - Nha Trang»
  * 2031470527687049 -- район не определяется по адресу «Prime central location»
  * 2060280514806050 -- район не определяется по адресу «Cho thuê căn hộ HUD Building Nguyễn thiện thuật nh»
  * 2054398412060927 -- это поиск жилья, а не предложение
  * 2579623245791664 -- район не определяется по адресу «the prestigious Meyhomes community»
  * 2586447371775918 -- тип жилья в тексте не назван
  * 1756168655595818 -- район не определяется по адресу «Marina Waterfront»
  * 1757293212150029 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 3273225212888572 -- район не определяется по адресу «Khu đô thị An Phú Thịnh»
  * 2126105611361434 -- в посте несколько разных цен: 10,000,000, 13,000,000
  * 2119050485400280 -- это поиск жилья, а не предложение
  * 2126688371303158 -- район не определяется по адресу «Khu đô thị An Phú Thịnh»
  * 1445448987399170 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»
  * 1463642598913142 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 1461245469152855 -- район не определяется по адресу «APARTMENT FOR RENT»
  * 3213120192216198 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»
  * 3236985219829695 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 3236874719840745 -- район не определяется по адресу «Vị trí độc tôn: Lô góc 2 mặt tiền đường Thi Sách»
  * 3203441086517442 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ»
  * 3232506143610936 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 3230379787156905 -- район не определяется по адресу «36/.. lương văn can»
  * 3214918155369735 -- в посте несколько разных цен: 3,500,000, 4,200,000
  * 3170988256429392 -- район не определяется по адресу «gồm 1 phòng ngủ»
  * 3161796947348523 -- район не определяется по адресу «**CHO THUÊ CĂN HỘ MINI ĐƯỜNG THỐNG NHẤT»
"""
from listing_lock import insert_listings

IDS = [3000545, 3000546, 3000547, 3000548, 3000549, 3000550, 3000551, 3000552, 3000553, 3000554, 3000555]

NEW_SRC = r'''
L(3000545,"can-tho","hpu","Студия",3500000,None,
  "Студия, Hưng Phú.",
  "https://www.facebook.com/groups/674135380985772/posts/1753370626395570/","сегодня",0,source="fbgroup",
  descEn="Studio, Hưng Phú.",
  details={"photos": ["assets/fb_photos/1753370626395570/01.webp", "assets/fb_photos/1753370626395570/02.webp", "assets/fb_photos/1753370626395570/03.webp", "assets/fb_photos/1753370626395570/04.webp", "assets/fb_photos/1753370626395570/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000546,"can-tho","hpu","Комната",3500000,None,
  "Комната, Hưng Phú.",
  "https://www.facebook.com/groups/674135380985772/posts/1753257533073546/","сегодня",0,source="fbgroup",
  descEn="Room, Hưng Phú.",
  details={"photos": ["assets/fb_photos/1753257533073546/01.webp", "assets/fb_photos/1753257533073546/02.webp", "assets/fb_photos/1753257533073546/03.webp", "assets/fb_photos/1753257533073546/04.webp", "assets/fb_photos/1753257533073546/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000547,"can-tho","nki","Комната",2800000,25,
  "Комната, 25 м², Ninh Kiều.",
  "https://www.facebook.com/groups/674135380985772/posts/1669709601428340/","сегодня",0,source="fbgroup",
  descEn="Room, 25 m², Ninh Kiều.",
  details={"photos": ["assets/fb_photos/1669709601428340/01.webp", "assets/fb_photos/1669709601428340/02.webp", "assets/fb_photos/1669709601428340/03.webp", "assets/fb_photos/1669709601428340/04.webp", "assets/fb_photos/1669709601428340/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000548,"cebu","gua","Квартира",30000,34,
  "1-спальная квартира, 34 м², Guadalupe.",
  "https://www.facebook.com/groups/563896434149922/posts/2372027243336823/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="1-bedroom flat, 34 m², Guadalupe.",
  details={"photos": ["assets/fb_photos/2372027243336823/01.webp", "assets/fb_photos/2372027243336823/02.webp", "assets/fb_photos/2372027243336823/03.webp", "assets/fb_photos/2372027243336823/04.webp", "assets/fb_photos/2372027243336823/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000549,"dumaguete","bcg","Квартира",18000,None,
  "Квартира, Bacong.",
  "https://www.facebook.com/groups/1996683940588782/posts/4540691986187952/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Flat, Bacong.",
  details={"photos": ["assets/fb_photos/4540691986187952/01.webp", "assets/fb_photos/4540691986187952/02.webp", "assets/fb_photos/4540691986187952/03.webp", "assets/fb_photos/4540691986187952/04.webp", "assets/fb_photos/4540691986187952/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000550,"dumaguete","sib","Дом",75000,None,
  "3-спальный дом, Sibulan.",
  "https://www.facebook.com/groups/153191128587086/posts/2227834604456051/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="3-bedroom house, Sibulan.",
  details={"photos": ["assets/fb_photos/2227834604456051/01.webp", "assets/fb_photos/2227834604456051/02.webp", "assets/fb_photos/2227834604456051/03.webp", "assets/fb_photos/2227834604456051/04.webp", "assets/fb_photos/2227834604456051/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000551,"dumaguete","val","Квартира",26000,None,
  "1-спальная квартира, Valencia — 1 санузел.",
  "https://www.facebook.com/groups/153191128587086/posts/2205044503401728/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="1-bedroom flat, Valencia — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2205044503401728/01.webp", "assets/fb_photos/2205044503401728/02.webp", "assets/fb_photos/2205044503401728/03.webp", "assets/fb_photos/2205044503401728/04.webp", "assets/fb_photos/2205044503401728/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000552,"hue","acu","Студия",2800000,None,
  "Студия, Hồ Đắc Di, An Cựu.",
  "https://www.facebook.com/groups/phongtrochothuehue/posts/1978625339511909/","сегодня",0,source="fbgroup",
  descEn="Studio, Hồ Đắc Di, An Cựu.",
  details={"photos": ["assets/fb_photos/1978625339511909/01.webp", "assets/fb_photos/1978625339511909/02.webp", "assets/fb_photos/1978625339511909/03.webp", "assets/fb_photos/1978625339511909/04.webp", "assets/fb_photos/1978625339511909/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000553,"hue","vyd","Студия",6000000,40,
  "Студия, 40 м², Vỹ Dạ.",
  "https://www.facebook.com/groups/phongtrosvhue/posts/1699463947929580/","сегодня",0,source="fbgroup",
  descEn="Studio, 40 m², Vỹ Dạ.",
  details={"photos": ["assets/fb_photos/1699463947929580/01.webp", "assets/fb_photos/1699463947929580/02.webp", "assets/fb_photos/1699463947929580/03.webp", "assets/fb_photos/1699463947929580/04.webp", "assets/fb_photos/1699463947929580/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000554,"manila","mak","Квартира",35000,59,
  "1-спальная квартира, 59 м², Makati.",
  "https://www.facebook.com/groups/224805677963542/posts/2573848076392612/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="1-bedroom flat, 59 m², Makati.",
  details={"photos": ["assets/fb_photos/2573848076392612/01.webp", "assets/fb_photos/2573848076392612/02.webp", "assets/fb_photos/2573848076392612/03.webp", "assets/fb_photos/2573848076392612/04.webp", "assets/fb_photos/2573848076392612/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000555,"phu-quoc","ath","Студия",5000000,None,
  "Студия, An Thới.",
  "https://www.facebook.com/groups/472474987298531/posts/1755470302332320/","сегодня",0,source="fbgroup",
  descEn="Studio, An Thới.",
  details={"photos": ["assets/fb_photos/1755470302332320/01.webp", "assets/fb_photos/1755470302332320/02.webp", "assets/fb_photos/1755470302332320/03.webp", "assets/fb_photos/1755470302332320/04.webp", "assets/fb_photos/1755470302332320/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
