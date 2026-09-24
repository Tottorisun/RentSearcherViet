# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 14 строк, 2026-09-24.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 993673090964916/3091345824530955 -- cebu/lah, 25,000 PHP: район назван в адресе поста
  * 993673090964916/1788624765783391 -- cebu/tls, 17,000 PHP: район назван в адресе поста
  * 993673090964916/3084842838514587 -- cebu/man, 35,000 PHP: район назван в адресе поста
  * 975470559939040/2359711461514936 -- da-lat/cl, 15,000,000 VND: район назван в адресе поста
  * 211616406116962/2076569656288285 -- da-lat/cl, 15,000,000 VND: район назван в адресе поста
  * 211616406116962/2069351513676766 -- da-lat/xh, 2,800,000 VND: район назван в адресе поста; улица Lương Thế Vinh: 4 из 4 отрезков в xh
  * chothuecanhodanang43/1742573107398998 -- da-nang/ns, 9,000,000 VND: прежний район Ngu Hanh Son весь вошёл в этот; «Son Thuy Street»: 5 строк сайта, все в ns
  * chothuecanhodanang43/1739962917660017 -- da-nang/hcg, 13,000,000 VND: улица Lê Thanh Nghị: 18 из 18 отрезков в hcg; пост: Hai Chau
  * chothuecanhodanang43/1742875017368807 -- da-nang/ah, 8,000,000 VND: улица Lê Hữu Trác: 3 из 3 отрезков в ah
  * chothuecanhodanang43/1742275864095389 -- da-nang/st, 8,500,000 VND: «Vu Ngoc Nha Street»: 2 строк сайта, все в st
  * canhochothuedanangtot/2214802225814103 -- da-nang/ns, 23,400,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * 346330203591713/1423197052571684 -- dumaguete/btg, 15,000 PHP: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1113334617807093 -- nha-trang/lt, 12,000,000 VND: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1113152374491984 -- nha-trang/btr, 12,500,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (161):
  * 3089574081374796 -- тот же текст уже заведён: id 3001116
  * 3090424441289760 -- в посте несколько разных цен: 3,000, 22,000
  * 28646959921607710 -- тот же текст уже заведён: id 3001116
  * 28643114135325622 -- район не определяется по адресу «Vertex Central Archbishop Reyes Cebu City»
  * 28663251676645201 -- район не определяется по адресу «Room for rent in Subangdaku»
  * 28659385793698456 -- похоже на уже заведённое: id 3000864
  * 28648114874825548 -- в посте несколько разных цен: 31,000, 33,000
  * 2363088937843855 -- тип жилья в тексте не назван
  * 2368644720621610 -- район не определяется по адресу «HOUSE FOR RENT»
  * 2367064320779650 -- район не определяется по адресу «LUXURY BRAND-NEW HOUSE FOR RENT»
  * 2366316614187754 -- район не определяется по адресу «Panorama Apartment for Rent»
  * 2367397907412958 -- это поиск жилья, а не предложение
  * 2368197180666364 -- район не определяется по адресу «BRAND NEW 1BR APARTMENT»
  * 2125924031352847 -- это поиск жилья, а не предложение
  * 2134554663823117 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 2096068041005113 -- тип жилья в тексте не назван
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2103298020282115 -- в тексте есть и другая цена того же порядка: 953,303, 7,201,681 против 2,500,000
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 1476237824669201 -- в посте несколько разных цен: 8,000,000, 9,000,000
  * 1479585951001055 -- район не определяется: «CHO THUÊ NHÀ NGUYÊN CĂN 2PN kiệt 1xx NGUYỄN CHÍ THANH✨ Phường Hải Châu - Ngay trung tâm TP, đường Bạch Đằng, Trần Phú»
  * 1477203231239327 -- район не определяется: «Brand-new house for rent: 4 floors, 4 bedrooms, 6 bathrooms»
  * 1484065793886404 -- в посте несколько разных цен: 6,500,000, 7,000,000
  * 1483216707304646 -- в посте несколько разных цен: 4,200,000, 5,000,000
  * 1483981000561550 -- район не определяется: «1-BEDROOM, APARTMENT FOR RENT, SON TRA»
  * 1478759971083653 -- тот же текст уже заведён: id 3001237
  * 1479325781027072 -- похоже на уже заведённое: id 1005952
  * 1480365884256395 -- тот же текст уже заведён: id 3001176
  * 2362511374587209 -- район не определяется: «STUDIO APARTMENT FOR RENT, NGUYEN VAN THOAI, Great location»
  * 2361586498013030 -- район не определяется: «BRAND NEW FULLY FURNISHED APARTMENT FOR RENT, HEAVY RAINY SEASON DISCOUNT!, Pho Duc Chinh Street»
  * 2362473794590967 -- тот же текст уже заведён: id 3001238
  * 2361758191329194 -- похоже на уже заведённое: id 1010471
  * 2362626871242326 -- в посте несколько разных цен: 14,000,000, 15,000,000
  * 2360470918124588 -- цена 500,000 VND вне разумных пределов
  * 2362086147963065 -- район не определяется: «1-BEDROOM APARTMENT, CITY VIEW, Ha Ky Ngo Street»
  * 2361433224695024 -- тот же текст уже заведён: id 3001239
  * 2357231405115206 -- нет ни одной скачанной фотографии
  * 2356307925207554 -- это поиск жилья, а не предложение
  * 1643178526950872 -- в посте несколько разных цен: 25,000,000, 27,000,000
  * 1646783353257056 -- в посте несколько разных цен: 10,000,000, 14,000,000
  * 1646819573253434 -- район не определяется: «FOR RENT, 2-BEDROOM APARTMENT, MIA PLAZA»
  * 1642237443711647 -- район не определяется: «🐋, VILLA 3 PHÒNG NGỦ 300M², SƠN TRÀ»
  * 1392918653051924 -- тот же текст уже заведён: id 3001240
  * 1391899156487207 -- тот же текст уже заведён: id 3001241
  * 1390298049980651 -- тот же текст уже заведён: id 3001242
  * 1390869649923491 -- тот же текст уже заведён: id 3001243
  * 1389904863353303 -- район не определяется: «CHO THUÊ PHÒNG P302, TRƯƠNG CÔNG HY, ĐÀ NẴNG»
  * 1393199799690476 -- в посте несколько разных цен: 4,000,000, 4,700,000
  * 1391905603153229 -- тот же текст уже заведён: id 3001244
  * 1393001116377011 -- тот же текст уже заведён: id 3001245
  * 1393007243043065 -- тот же текст уже заведён: id 3001246
  * 1392816816395441 -- район не определяется: «1-BEDROOM APARTMENT, MOUNTAIN VIEW & GREAT VALUE, Dung Si Thanh Khe»
  * 1388166273527162 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000
  * 2971851666542244 -- тот же текст уже заведён: id 3001247
  * 2975759296151481 -- тот же текст уже заведён: id 3001248
  * 1570066731539503 -- в посте несколько разных цен: 25,000,000, 27,000,000, 29,000,000
  * 1559442292601947 -- район не определяется: «Da Nang, Hai Chau District, **92m² 2-bedroom Apartment in Da Nang»
  * 1570039781542198 -- тот же текст уже заведён: id 3001249
  * 1569948948217948 -- тот же текст уже заведён: id 3001250
  * 1742357717420537 -- тот же текст уже заведён: id 3001248
  * 1742797127376596 -- район не определяется: «HOUSE FOR RENT ON NGUYEN TRI PHUONG STREET, HAI CHAU, 🏠 HOUSE FOR RENT ON NGUYEN TRI PHUONG STREET»
  * 1742576090732033 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT, AN THUONG 14, An Thuong 14»
  * 1740963570893285 -- похоже на уже заведённое: id 1005932
  * 2227385361222456 -- район не определяется: «For rent - Studio apartment in the Sun Cosmo Residence, convenient area, Đà Nẵng City»
  * 2229530991007893 -- источники назвали разные районы: district=ns, street=ah
  * 2226225068005152 -- район не определяется: «**PET-FRIENDLY 1BR FOR RENT, PANOMA, DA NANG** 🐾»
  * 2222237321737260 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000, 14,000,000
  * 2226704014623924 -- похоже на уже заведённое: id 1010627
  * 2223506231610369 -- в посте несколько разных цен: 6,000,000, 9,000,000
  * 2221117548515904 -- это поиск жилья, а не предложение
  * 2221611245133201 -- в посте несколько разных цен: 7,500,000, 8,000,000
  * 2220636861897306 -- тип жилья в тексте не назван
  * 1422244359333620 -- в тексте есть и другая цена того же порядка: 21,641 против 40,000
  * 1421461599411896 -- тип жилья в тексте не назван
  * 4620975714826245 -- продажа
  * 4617681065155710 -- тип жилья в тексте не назван
  * 4620107064913110 -- район не определяется по адресу «House for rent‼️»
  * 4614646732125810 -- район не определяется по адресу «Crossing Bogo»
  * 4614813985442418 -- район не определяется по адресу «Mangnao Dumaguete City»
  * 4611225949134555 -- в тексте есть и другая цена того же порядка: 21,641 против 40,000
  * 1987516638597971 -- район не определяется по адресу «Trảng Kèo 8»
  * 1992234034792898 -- район не определяется по адресу «Move-in ready»
  * 1977822679567367 -- район не определяется по адресу «BEACH LIFE IN HOI AN»
  * 1984906532192315 -- в посте несколько разных цен: 4,500,000, 5,000,000
  * 1984287965587505 -- нет ни одной скачанной фотографии
  * 1992280878121547 -- район не определяется по адресу «Spacious 3-Bedroom House for Long-Term Rent Near H»
  * 2017947155550334 -- район не определяется по адресу «PRIVATE 4-BEDROOM CORNER VILLA»
  * 2017928622218854 -- район не определяется по адресу «✨ COZY 1-BEDROOM APARTMENT FOR RENT IN HOI AN ✨🏡»
  * 2017747158903667 -- район не определяется по адресу «A Beautiful Home in the Heart of Hoi An»
  * 2017532202258496 -- район не определяется по адресу «1-Bedroom Apartment»
  * 2014292692582447 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 2010975296247520 -- район не определяется по адресу «ENTIRE HOUSE FOR RENT»
  * 3841464279327452 -- тот же текст уже заведён: id 3001221
  * 3837694026371144 -- район не определяется по адресу «2 bedrooms»; прецедент расколот: «LVCC»: lt 1
  * 3841247709349109 -- тот же текст уже заведён: id 3001222
  * 3841439605996586 -- тот же текст уже заведён: id 3001223
  * 3841518345988712 -- район не определяется по адресу «fully furnished with a private washing machine»
  * 3840556076084939 -- тот же текст уже заведён: id 3001224
  * 3840038072803406 -- район не определяется по адресу «APARTMENT FOR RENT»; прецедент расколот: «CT6»: ttr 1
  * 3839108232896390 -- тот же текст уже заведён: id 3001225
  * 3838846259589254 -- в посте несколько разных цен: 14,500,000, 15,500,000
  * 4615612555374932 -- район не определяется по адресу «Muong Thanh 04 Tran Phu»
  * 4615520195384168 -- тот же текст уже заведён: id 3001226
  * 4619753401627514 -- район не определяется по адресу «Tran Phu - Nha Trang»
  * 4619187528350768 -- в посте несколько разных цен: 500,000, 12,500,000
  * 4617186755217512 -- это поиск жилья, а не предложение
  * 4618707241732130 -- нет ни одной скачанной фотографии
  * 4611904355745752 -- нет ни одной скачанной фотографии
  * 4618733135062874 -- это поиск жилья, а не предложение
  * 2713243959107879 -- адрес называет несколько районов: btr, vh
  * 2714520092313599 -- в посте несколько разных цен: 1,000,000, 10,000,000
  * 2717514738680801 -- район не определяется по адресу «fully furnished with a private washing machine»
  * 2714566965642245 -- тот же текст уже заведён: id 3001227
  * 2716907985408143 -- в посте несколько разных цен: 11,500,000, 12,500,000
  * 2716165988815676 -- район не определяется по адресу «NT RENT»
  * 2714405582325050 -- тот же текст уже заведён: id 3001228
  * 2712131079219167 -- тот же текст уже заведён: id 3001229
  * 2715436048888670 -- тот же текст уже заведён: id 3001230
  * 1974105989951835 -- тип жилья в тексте не назван
  * 1950686778960423 -- тот же текст уже заведён: id 3001231
  * 1976374273058340 -- тот же текст уже заведён: id 3001232
  * 1972456823450085 -- район не определяется по адресу «CHO THUÊ CHUNG CƯ HƯNG PHÚ»
  * 1975747079787726 -- в тексте есть и другая цена того же порядка: 85,845,478 против 68,000,000
  * 1977194386309662 -- тот же текст уже заведён: id 3001233
  * 1976650559697378 -- тот же текст уже заведён: id 3001234
  * 1976587589703675 -- тот же текст уже заведён: id 3001235
  * 1973536030008831 -- тип жилья в тексте не назван
  * 1968092573886510 -- тот же текст уже заведён: id 3001235
  * 4717511835161552 -- тот же текст уже заведён: id 3001236
  * 4721597574752978 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4724156191163783 -- это поиск жилья, а не предложение
  * 4725782844334451 -- это поиск жилья, а не предложение
  * 2090509091606511 -- район не определяется по адресу «Nha Trang Ward»
  * 2090555578268529 -- в посте несколько разных цен: 530,000, 20,000,000
  * 2088878168436270 -- тот же текст уже заведён: id 3001235
  * 1113468417793713 -- район не определяется по адресу «Bustling residential area near the city center»
  * 1109977311476157 -- район не определяется по адресу «South Nha Trang»
  * 1113375201136368 -- район не определяется по адресу «NT RENT»
  * 1113530237787531 -- район не определяется по адресу «**Khanh Hoa»
  * 1113365664470655 -- в посте несколько разных цен: 20,000,000, 25,000,000
  * 2070505000450268 -- в посте несколько разных цен: 700,000, 21,000,000
  * 2070589390441829 -- район не определяется по адресу «**Khanh Hoa»
  * 2070057083828393 -- район не определяется по адресу «**Khanh Hoa»
  * 2069346347232800 -- это поиск жилья, а не предложение
  * 2068493540651414 -- тот же текст уже заведён: id 3001235
  * 5545581265666511 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 5549054955319142 -- район не определяется по адресу «# **Cho thuê căn hộ Altara Residences Quy Nhơn - 2»
  * 3285077928369967 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 3280507732160320 -- район не определяется по адресу «Ngay Đại học FPT»
  * 3278586459019114 -- район не определяется по адресу «Studio»
  * 1737704797293837 -- район не определяется по адресу «Direct owner service»
  * 1735000710897579 -- район не определяется по адресу «2 bedrooms»
  * 1738431463887837 -- район не определяется по адресу «Apartment for rent at Binh Gia Resident»
  * 1736754977388819 -- район не определяется по адресу «172 Hoang Hoa Tham Street»
  * 27948705921436408 -- в посте несколько разных цен: 6,000,000, 6,500,000
  * 1674135736984077 -- район не определяется по адресу «Thông tin căn hộ:»
  * 1712195156511468 -- район не определяется по адресу «🏢 Apartment for Rent - Fully Furnished - Ward 8»
  * 1474799354464133 -- район не определяется по адресу «Direct owner service»
  * 1472289898048412 -- это поиск жилья, а не предложение
  * 1476872604256808 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 1477067380903997 -- в посте несколько разных цен: 9,000,000, 13,000,000, 18,000,000
"""
from listing_lock import insert_listings

IDS = [3001270, 3001271, 3001272, 3001273, 3001274, 3001275, 3001276, 3001277, 3001278, 3001279, 3001280, 3001281, 3001282, 3001283]

NEW_SRC = r'''
L(3001270,"cebu","lah","Дом",25000,None,
  "1-спальный дом, Lahug.",
  "https://www.facebook.com/groups/993673090964916/posts/3091345824530955/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-24",
  descEn="1-bedroom house, Lahug.",
  details={"photos": ["assets/fb_photos/3091345824530955/01.webp", "assets/fb_photos/3091345824530955/02.webp", "assets/fb_photos/3091345824530955/03.webp", "assets/fb_photos/3091345824530955/04.webp", "assets/fb_photos/3091345824530955/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001271,"cebu","tls","Квартира",17000,None,
  "3-спальная квартира, Talisay.",
  "https://www.facebook.com/groups/993673090964916/posts/1788624765783391/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-24",
  descEn="3-bedroom flat, Talisay.",
  details={"photos": ["assets/fb_photos/1788624765783391/01.webp", "assets/fb_photos/1788624765783391/02.webp", "assets/fb_photos/1788624765783391/03.webp", "assets/fb_photos/1788624765783391/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001272,"cebu","man","Дом",35000,None,
  "1-спальный дом, Mandaue.",
  "https://www.facebook.com/groups/993673090964916/posts/3084842838514587/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-24",
  descEn="1-bedroom house, Mandaue.",
  details={"photos": ["assets/fb_photos/3084842838514587/01.webp", "assets/fb_photos/3084842838514587/02.webp", "assets/fb_photos/3084842838514587/03.webp", "assets/fb_photos/3084842838514587/04.webp", "assets/fb_photos/3084842838514587/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001273,"da-lat","cl","Квартира",15000000,None,
  "Квартира, Cam Ly - Đà Lạt — 1 санузел.",
  "https://www.facebook.com/groups/975470559939040/posts/2359711461514936/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Flat, Cam Ly - Đà Lạt — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2359711461514936/01.webp", "assets/fb_photos/2359711461514936/02.webp", "assets/fb_photos/2359711461514936/03.webp", "assets/fb_photos/2359711461514936/04.webp", "assets/fb_photos/2359711461514936/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001274,"da-lat","cl","Квартира",15000000,55,
  "Квартира, 55 м², Cam Ly - Đà Lạt — 1 санузел.",
  "https://www.facebook.com/groups/211616406116962/posts/2076569656288285/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Flat, 55 m², Cam Ly - Đà Lạt — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2076569656288285/01.webp", "assets/fb_photos/2076569656288285/02.webp", "assets/fb_photos/2076569656288285/03.webp", "assets/fb_photos/2076569656288285/04.webp", "assets/fb_photos/2076569656288285/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001275,"da-lat","xh","Комната",2800000,None,
  "Комната, Lương Thế Vinh, Xuân Hương - Đà Lạt.",
  "https://www.facebook.com/groups/211616406116962/posts/2069351513676766/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Room, Lương Thế Vinh, Xuân Hương - Đà Lạt.",
  details={"photos": ["assets/fb_photos/2069351513676766/01.webp", "assets/fb_photos/2069351513676766/02.webp", "assets/fb_photos/2069351513676766/03.webp", "assets/fb_photos/2069351513676766/04.webp", "assets/fb_photos/2069351513676766/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001276,"da-nang","ns","Квартира",9000000,None,
  "Квартира, Son Thuy, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1742573107398998/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Flat, Son Thuy, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1742573107398998/01.webp", "assets/fb_photos/1742573107398998/02.webp", "assets/fb_photos/1742573107398998/03.webp", "assets/fb_photos/1742573107398998/04.webp", "assets/fb_photos/1742573107398998/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001277,"da-nang","hcg","Квартира",13000000,None,
  "1-спальная квартира, Lê Thanh Nghị, Hòa Cường.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1739962917660017/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="1-bedroom flat, Lê Thanh Nghị, Hòa Cường.",
  details={"photos": ["assets/fb_photos/1739962917660017/01.webp", "assets/fb_photos/1739962917660017/02.webp", "assets/fb_photos/1739962917660017/03.webp", "assets/fb_photos/1739962917660017/04.webp", "assets/fb_photos/1739962917660017/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001278,"da-nang","ah","Квартира",8000000,None,
  "1-спальная квартира, Lê Hữu Trác, An Hải.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1742875017368807/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="1-bedroom flat, Lê Hữu Trác, An Hải.",
  details={"photos": ["assets/fb_photos/1742875017368807/01.webp", "assets/fb_photos/1742875017368807/02.webp", "assets/fb_photos/1742875017368807/03.webp", "assets/fb_photos/1742875017368807/04.webp", "assets/fb_photos/1742875017368807/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001279,"da-nang","st","Квартира",8500000,None,
  "1-спальная квартира, Vu Ngoc Nha, Sơn Trà.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1742275864095389/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="1-bedroom flat, Vu Ngoc Nha, Sơn Trà.",
  details={"photos": ["assets/fb_photos/1742275864095389/01.webp", "assets/fb_photos/1742275864095389/02.webp", "assets/fb_photos/1742275864095389/03.webp", "assets/fb_photos/1742275864095389/04.webp", "assets/fb_photos/1742275864095389/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001280,"da-nang","ns","Квартира",23400000,None,
  "2-спальная квартира, PREMIUM BRAND-NEW 2BR, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2214802225814103/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="2-bedroom flat, PREMIUM BRAND-NEW 2BR, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2214802225814103/01.webp", "assets/fb_photos/2214802225814103/02.webp", "assets/fb_photos/2214802225814103/03.webp", "assets/fb_photos/2214802225814103/04.webp", "assets/fb_photos/2214802225814103/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001281,"dumaguete","btg","Дом",15000,None,
  "2-спальный дом, Batinguel.",
  "https://www.facebook.com/groups/346330203591713/posts/1423197052571684/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-24",
  descEn="2-bedroom house, Batinguel.",
  details={"photos": ["assets/fb_photos/1423197052571684/01.webp", "assets/fb_photos/1423197052571684/02.webp", "assets/fb_photos/1423197052571684/03.webp", "assets/fb_photos/1423197052571684/04.webp", "assets/fb_photos/1423197052571684/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001282,"nha-trang","lt","Квартира",12000000,80,
  "2-спальная квартира, 80 м², Lộc Thọ.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1113334617807093/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="2-bedroom flat, 80 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/1113334617807093/01.webp", "assets/fb_photos/1113334617807093/02.webp", "assets/fb_photos/1113334617807093/03.webp", "assets/fb_photos/1113334617807093/04.webp", "assets/fb_photos/1113334617807093/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001283,"nha-trang","btr","Квартира",12500000,35,
  "Квартира, 35 м², Bắc Nha Trang.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1113152374491984/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Flat, 35 m², Bắc Nha Trang.",
  details={"photos": ["assets/fb_photos/1113152374491984/01.webp", "assets/fb_photos/1113152374491984/02.webp", "assets/fb_photos/1113152374491984/03.webp", "assets/fb_photos/1113152374491984/04.webp", "assets/fb_photos/1113152374491984/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
