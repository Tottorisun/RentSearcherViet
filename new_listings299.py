# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 14 строк, 2026-09-23.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * phongtrocanhonhadanang/1478759971083653 -- da-nang/ah, 10,500,000 VND: район назван в посте
  * 203559903815711/2362473794590967 -- da-nang/ah, 13,000,000 VND: улица Nguyễn Xuân Khoát: 1 из 1 отрезков в ah
  * 203559903815711/2361433224695024 -- da-nang/ns, 10,500,000 VND: район назван в посте; улица An Thượng 12: 1 из 1 отрезков в ns
  * 728946289449167/1392918653051924 -- da-nang/hx, 5,500,000 VND: район назван в посте
  * 728946289449167/1391899156487207 -- da-nang/ns, 11,000,000 VND: район назван в посте
  * 728946289449167/1390298049980651 -- da-nang/ns, 12,500,000 VND: улица Tuy Lý Vương: 1 из 1 отрезков в ns
  * 728946289449167/1390869649923491 -- da-nang/ns, 6,500,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * 728946289449167/1391905603153229 -- da-nang/hx, 10,000,000 VND: район назван в посте
  * 728946289449167/1393001116377011 -- da-nang/cl2, 5,500,000 VND: улица Bùi Kỷ: 1 из 1 отрезков в cl2
  * 728946289449167/1393007243043065 -- da-nang/hx, 5,500,000 VND: район назван в посте; улица Đình Văn Chấp: 1 из 1 отрезков в hx
  * canhochungcudanang/2971851666542244 -- da-nang/ns, 20,000,000 VND: район назван в посте
  * canhochungcudanang/2975759296151481 -- da-nang/ns, 19,000,000 VND: район назван в посте
  * 1454201286459382/1570039781542198 -- da-nang/hx, 9,000,000 VND: район назван в посте
  * 1454201286459382/1569948948217948 -- da-nang/ns, 15,000,000 VND: район назван в посте; прежний район Ngu Hanh Son весь вошёл в этот

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (119):
  * 3474885602689740 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 3111524002383926 -- это поиск жилья, а не предложение
  * 3086171178252542 -- район не определяется по адресу «Studio siêu đẹp»
  * 2730478847155112 -- помещение под бизнес или здание целиком, а не жильё
  * 3489735917871375 -- это поиск жилья, а не предложение
  * 38776853001913132 -- уже на сайте: id 3001175
  * 39444546815143744 -- район не определяется по адресу «✨💫⚡️ CĂN NHÀ NHỎ RỘNG 40M2 KDC NAM LONG - GẦN BẾN »
  * 39444140438517715 -- район не определяется по адресу «🎊💫⚡️ PHÒNG TRỌ RỘNG 30M2 FULL NỘI THẤT - GIÁ 2.8 T»
  * 39420389250892834 -- тип жилья в тексте не назван
  * 1757290509336915 -- цена 650,000 VND вне разумных пределов
  * 1725575419175091 -- тип жилья в тексте не назван
  * 1725714562494510 -- район не определяется по адресу «Chủ gửi»
  * 1715148420217791 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NGUYỄN VĂN LI»
  * 1763376668728299 -- район не определяется по адресу «💒PHÒNG TRỌ RỘNG 32M2 - GỒM 1 TRỆT - 1 GÁC LỮNG VÀ »
  * 1761348792264420 -- район не определяется по адресу «🏩MINIHOUSE CAO CẤP FULL NỘI THẤT - RỘNG 40M2 MỚI -»
  * 1763329685399664 -- район не определяется по адресу «💒 PHÒNG TRỌ CÓ MÁY LẠNH RỘNG 25M2 GIÁP KDC NAM LON»
  * 1758617719204194 -- тип жилья в тексте не назван
  * 1763351818730784 -- тип жилья в тексте не назван
  * 1763832052016094 -- район не определяется по адресу «Coc 1 tháng»
  * 2226225068005152 -- район не определяется: «**PET-FRIENDLY 1BR FOR RENT, PANOMA, DA NANG** 🐾»
  * 2224400174854308 -- уже на сайте: id 3001176
  * 2221117548515904 -- это поиск жилья, а не предложение
  * 2227385361222456 -- район не определяется: «For rent - Studio apartment in the Sun Cosmo Residence, convenient area, Đà Nẵng City»
  * 2222237321737260 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000, 14,000,000
  * 2221611245133201 -- в посте несколько разных цен: 7,500,000, 8,000,000
  * 1476237824669201 -- в посте несколько разных цен: 8,000,000, 9,000,000
  * 1479585951001055 -- район не определяется: «CHO THUÊ NHÀ NGUYÊN CĂN 2PN kiệt 1xx NGUYỄN CHÍ THANH✨ Phường Hải Châu - Ngay trung tâm TP, đường Bạch Đằng, Trần Phú»
  * 1477203231239327 -- район не определяется: «Brand-new house for rent: 4 floors, 4 bedrooms, 6 bathrooms»
  * 1484065793886404 -- в посте несколько разных цен: 6,500,000, 7,000,000
  * 1483216707304646 -- в посте несколько разных цен: 4,200,000, 5,000,000
  * 1483981000561550 -- район не определяется: «1-BEDROOM, APARTMENT FOR RENT, SON TRA»
  * 1479325781027072 -- похоже на уже заведённое: id 1005952
  * 1480365884256395 -- тот же текст уже заведён: id 3001176
  * 2362511374587209 -- район не определяется: «STUDIO APARTMENT FOR RENT, NGUYEN VAN THOAI, Great location»
  * 2361586498013030 -- район не определяется: «BRAND NEW FULLY FURNISHED APARTMENT FOR RENT, HEAVY RAINY SEASON DISCOUNT!, Pho Duc Chinh Street»
  * 2361758191329194 -- похоже на уже заведённое: id 1010471
  * 2362626871242326 -- в посте несколько разных цен: 14,000,000, 15,000,000
  * 2360470918124588 -- цена 500,000 VND вне разумных пределов
  * 2362086147963065 -- район не определяется: «1-BEDROOM APARTMENT, CITY VIEW, Ha Ky Ngo Street»
  * 2357231405115206 -- нет ни одной скачанной фотографии
  * 2356307925207554 -- это поиск жилья, а не предложение
  * 1643178526950872 -- в посте несколько разных цен: 25,000,000, 27,000,000
  * 1646783353257056 -- в посте несколько разных цен: 10,000,000, 14,000,000
  * 1646819573253434 -- район не определяется: «FOR RENT, 2-BEDROOM APARTMENT, MIA PLAZA»
  * 1642237443711647 -- район не определяется: «🐋, VILLA 3 PHÒNG NGỦ 300M², SƠN TRÀ»
  * 1389904863353303 -- район не определяется: «CHO THUÊ PHÒNG P302, TRƯƠNG CÔNG HY, ĐÀ NẴNG»
  * 1393199799690476 -- в посте несколько разных цен: 4,000,000, 4,700,000
  * 1392816816395441 -- район не определяется: «1-BEDROOM APARTMENT, MOUNTAIN VIEW & GREAT VALUE, Dung Si Thanh Khe»
  * 1388166273527162 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000
  * 1570066731539503 -- в посте несколько разных цен: 25,000,000, 27,000,000, 29,000,000
  * 1559442292601947 -- район не определяется: «Da Nang, Hai Chau District, **92m² 2-bedroom Apartment in Da Nang»
  * 28879476114997119 -- район не определяется по адресу «T2734 Cho thuê chung cư Sentosa Sky Park»
  * 28787335770877821 -- район не определяется по адресу «T0451 Cho thuê Chung Cư Hoàng Huy Lạch Tray HH3 - »
  * 28714148764863189 -- район не определяется по адресу «🇻🇳 │ LÊ HỒNG PHONG»
  * 28810423058569092 -- район не определяется по адресу «T2960»
  * 28842684592009605 -- район не определяется по адресу «🇻🇳🇻🇳🇻🇳 VINHOMES MARINA»
  * 28878209611790436 -- район не определяется по адресу «🇻🇳 │ WATERFRONT CẦU RÀO»
  * 4514430372141452 -- это поиск жилья, а не предложение
  * 4518467168404439 -- район не определяется по адресу «Cho thuê căn hộ Penthouse 1 ngủ tách bếp to rộng t»
  * 28812159955062069 -- район не определяется по адресу «T0451 Cho thuê Chung Cư Hoàng Huy Lạch Tray HH3 - »
  * 28814728371471894 -- район не определяется по адресу «HH415 CHUNG CƯ HOÀNG HUY COMMERCE»
  * 28752123871065678 -- район не определяется по адресу «HH140 Hoàng Huy Commerce - Camellia Tìm khách Thuê»
  * 4518708065047016 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 1739874880555153 -- уже на сайте: id 3001177
  * 1708277650381543 -- район не определяется по адресу «CHO THUÊ STUDIO CAO CẤP»
  * 1701057297770245 -- в посте несколько разных цен: 3,600,000, 3,700,000, 3,800,000
  * 1637646127444696 -- район не определяется по адресу «Không gian sống hiện đại»
  * 1550648672811109 -- уже на сайте: id 3001178
  * 1251745672701412 -- в посте несколько разных цен: 4,000,000, 4,500,000, 4,800,000
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
  * 2592618517825470 -- район не определяется по адресу «✨ Brand-new villa»
  * 2591654944588494 -- помещение под бизнес или здание целиком, а не жильё
  * 2582748732145782 -- тип жилья в тексте не назван
  * 2596310307456291 -- район не определяется по адресу «🏡🏡🏡🏡🏡🏡🏡🏡🏡🏡🏡»
  * 1756168655595818 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1764181028127914 -- адрес называет несколько районов: ath, dto
  * 2597218400698815 -- уже на сайте: id 3001198
  * 2593687434385245 -- помещение под бизнес или здание целиком, а не жильё
  * 2586447371775918 -- помещение под бизнес или здание целиком, а не жильё
  * 1767333351146015 -- тот же текст уже заведён: id 3001198
"""
from listing_lock import insert_listings

IDS = [3001237, 3001238, 3001239, 3001240, 3001241, 3001242, 3001243, 3001244, 3001245, 3001246, 3001247, 3001248, 3001249, 3001250]

NEW_SRC = r'''
L(3001237,"da-nang","ah","Квартира",10500000,None,
  "Квартира, **APARTMENT AVAILABLE, An Hải.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1478759971083653/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, **APARTMENT AVAILABLE, An Hải.",
  details={"photos": ["assets/fb_photos/1478759971083653/01.webp", "assets/fb_photos/1478759971083653/02.webp", "assets/fb_photos/1478759971083653/03.webp", "assets/fb_photos/1478759971083653/04.webp", "assets/fb_photos/1478759971083653/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001238,"da-nang","ah","Квартира",13000000,None,
  "1-спальная квартира, Nguyễn Xuân Khoát, An Hải.",
  "https://www.facebook.com/groups/203559903815711/posts/2362473794590967/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="1-bedroom flat, Nguyễn Xuân Khoát, An Hải.",
  details={"photos": ["assets/fb_photos/2362473794590967/01.webp", "assets/fb_photos/2362473794590967/02.webp", "assets/fb_photos/2362473794590967/03.webp", "assets/fb_photos/2362473794590967/04.webp", "assets/fb_photos/2362473794590967/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001239,"da-nang","ns","Квартира",10500000,None,
  "1-спальная квартира, An Thượng 12, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/203559903815711/posts/2361433224695024/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="1-bedroom flat, An Thượng 12, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2361433224695024/01.webp", "assets/fb_photos/2361433224695024/02.webp", "assets/fb_photos/2361433224695024/03.webp", "assets/fb_photos/2361433224695024/04.webp", "assets/fb_photos/2361433224695024/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001240,"da-nang","hx","Студия",5500000,None,
  "Студия, BRAND-NEW STUDIO, Hòa Xuân.",
  "https://www.facebook.com/groups/728946289449167/posts/1392918653051924/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Studio, BRAND-NEW STUDIO, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1392918653051924/01.webp", "assets/fb_photos/1392918653051924/02.webp", "assets/fb_photos/1392918653051924/03.webp", "assets/fb_photos/1392918653051924/04.webp", "assets/fb_photos/1392918653051924/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001241,"da-nang","ns","Квартира",11000000,None,
  "Квартира, Quiet, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/728946289449167/posts/1391899156487207/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, Quiet, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1391899156487207/01.webp", "assets/fb_photos/1391899156487207/02.webp", "assets/fb_photos/1391899156487207/03.webp", "assets/fb_photos/1391899156487207/04.webp", "assets/fb_photos/1391899156487207/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001242,"da-nang","ns","Квартира",12500000,None,
  "2-спальная квартира, Tuy Lý Vương, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/728946289449167/posts/1390298049980651/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="2-bedroom flat, Tuy Lý Vương, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1390298049980651/01.webp", "assets/fb_photos/1390298049980651/02.webp", "assets/fb_photos/1390298049980651/03.webp", "assets/fb_photos/1390298049980651/04.webp", "assets/fb_photos/1390298049980651/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001243,"da-nang","ns","Квартира",6500000,None,
  "Квартира, Căn hộ full nội thất, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/728946289449167/posts/1390869649923491/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, Căn hộ full nội thất, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1390869649923491/01.webp", "assets/fb_photos/1390869649923491/02.webp", "assets/fb_photos/1390869649923491/03.webp", "assets/fb_photos/1390869649923491/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001244,"da-nang","hx","Квартира",10000000,None,
  "1-спальная квартира, ✨ 1-BEDROOM APARTMENT, Hòa Xuân.",
  "https://www.facebook.com/groups/728946289449167/posts/1391905603153229/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="1-bedroom flat, ✨ 1-BEDROOM APARTMENT, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1391905603153229/01.webp", "assets/fb_photos/1391905603153229/02.webp", "assets/fb_photos/1391905603153229/03.webp", "assets/fb_photos/1391905603153229/04.webp", "assets/fb_photos/1391905603153229/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001245,"da-nang","cl2","Студия",5500000,None,
  "Студия, Bùi Kỷ, Cẩm Lệ.",
  "https://www.facebook.com/groups/728946289449167/posts/1393001116377011/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Studio, Bùi Kỷ, Cẩm Lệ.",
  details={"photos": ["assets/fb_photos/1393001116377011/01.webp", "assets/fb_photos/1393001116377011/02.webp", "assets/fb_photos/1393001116377011/03.webp", "assets/fb_photos/1393001116377011/04.webp", "assets/fb_photos/1393001116377011/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001246,"da-nang","hx","Студия",5500000,None,
  "Студия, Đình Văn Chấp, Hòa Xuân.",
  "https://www.facebook.com/groups/728946289449167/posts/1393007243043065/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Studio, Đình Văn Chấp, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1393007243043065/01.webp", "assets/fb_photos/1393007243043065/02.webp", "assets/fb_photos/1393007243043065/03.webp", "assets/fb_photos/1393007243043065/04.webp", "assets/fb_photos/1393007243043065/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001247,"da-nang","ns","Квартира",20000000,None,
  "2-спальная квартира, APARTMENT FOR RENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2971851666542244/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="2-bedroom flat, APARTMENT FOR RENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2971851666542244/01.webp", "assets/fb_photos/2971851666542244/02.webp", "assets/fb_photos/2971851666542244/03.webp", "assets/fb_photos/2971851666542244/04.webp", "assets/fb_photos/2971851666542244/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001248,"da-nang","ns","Квартира",19000000,None,
  "2-спальная квартира, FOR RENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2975759296151481/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="2-bedroom flat, FOR RENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2975759296151481/01.webp", "assets/fb_photos/2975759296151481/02.webp", "assets/fb_photos/2975759296151481/03.webp", "assets/fb_photos/2975759296151481/04.webp", "assets/fb_photos/2975759296151481/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001249,"da-nang","hx","Квартира",9000000,None,
  "1-спальная квартира, ✨ BRAND NEW, Hòa Xuân.",
  "https://www.facebook.com/groups/1454201286459382/posts/1570039781542198/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="1-bedroom flat, ✨ BRAND NEW, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1570039781542198/01.webp", "assets/fb_photos/1570039781542198/02.webp", "assets/fb_photos/1570039781542198/03.webp", "assets/fb_photos/1570039781542198/04.webp", "assets/fb_photos/1570039781542198/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001250,"da-nang","ns","Квартира",15000000,None,
  "2-спальная квартира, APARTMENT FOR RENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/1454201286459382/posts/1569948948217948/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="2-bedroom flat, APARTMENT FOR RENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1569948948217948/01.webp", "assets/fb_photos/1569948948217948/02.webp", "assets/fb_photos/1569948948217948/03.webp", "assets/fb_photos/1569948948217948/04.webp", "assets/fb_photos/1569948948217948/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
