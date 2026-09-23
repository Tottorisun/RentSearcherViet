# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 16 строк, 2026-09-23.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 849441571863086/3841464279327452 -- nha-trang/btr, 18,500,000 VND: район назван в адресе поста
  * 849441571863086/3841247709349109 -- nha-trang/vt, 15,000,000 VND: район назван в адресе поста
  * 849441571863086/3841439605996586 -- nha-trang/lt, 11,000,000 VND: район назван в адресе поста
  * 849441571863086/3840556076084939 -- nha-trang/ph, 12,000,000 VND: район назван в адресе поста
  * 849441571863086/3839108232896390 -- nha-trang/lt, 10,000,000 VND: район назван в адресе поста
  * chothue79/4615520195384168 -- nha-trang/vn, 14,500,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2714566965642245 -- nha-trang/vp, 25,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2714405582325050 -- nha-trang/vp, 23,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2712131079219167 -- nha-trang/btr, 24,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2715436048888670 -- nha-trang/btr, 11,500,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1950686778960423 -- nha-trang/ph, 20,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1976374273058340 -- nha-trang/btr, 15,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1977194386309662 -- nha-trang/lt, 15,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1976650559697378 -- nha-trang/ph, 12,500,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1976587589703675 -- nha-trang/ntr, 25,000,000 VND: «Thích Quảng Đức»: 2 строк сайта, все в ntr
  * 2253829621529798/4717511835161552 -- nha-trang/tl, 28,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (77):
  * 3474885602689740 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 3111524002383926 -- это поиск жилья, а не предложение
  * 3086171178252542 -- район не определяется по адресу «Studio siêu đẹp»
  * 2730478847155112 -- помещение под бизнес или здание целиком, а не жильё
  * 3489735917871375 -- это поиск жилья, а не предложение
  * 38776853001913132 -- уже на сайте: id 3001175
  * 39444546815143744 -- район не определяется по адресу «✨💫⚡️ CĂN NHÀ NHỎ RỘNG 40M2 KDC NAM LONG - GẦN BẾN »; прецедент расколот: «FPT»: ltu 1, anb 1
  * 39444140438517715 -- район не определяется по адресу «🎊💫⚡️ PHÒNG TRỌ RỘNG 30M2 FULL NỘI THẤT - GIÁ 2.8 T»
  * 39420389250892834 -- тип жилья в тексте не назван
  * 1757290509336915 -- цена 650,000 VND вне разумных пределов
  * 1725575419175091 -- тип жилья в тексте не назван
  * 1725714562494510 -- район не определяется по адресу «Chủ gửi»
  * 1715148420217791 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NGUYỄN VĂN LI»
  * 1763376668728299 -- район не определяется по адресу «💒PHÒNG TRỌ RỘNG 32M2 - GỒM 1 TRỆT - 1 GÁC LỮNG VÀ »
  * 1761348792264420 -- район не определяется по адресу «🏩MINIHOUSE CAO CẤP FULL NỘI THẤT - RỘNG 40M2 MỚI -»
  * 1763329685399664 -- район не определяется по адресу «💒 PHÒNG TRỌ CÓ MÁY LẠNH RỘNG 25M2 GIÁP KDC NAM LON»; прецедент расколот: «FPT»: ltu 1, anb 1
  * 1758617719204194 -- тип жилья в тексте не назван
  * 1763351818730784 -- тип жилья в тексте не назван
  * 1763832052016094 -- район не определяется по адресу «Coc 1 tháng»
  * 2226225068005152 -- район не определяется: «**PET-FRIENDLY 1BR FOR RENT, PANOMA, DA NANG** 🐾»
  * 2224400174854308 -- уже на сайте: id 3001176
  * 2221117548515904 -- это поиск жилья, а не предложение
  * 2227385361222456 -- район не определяется: «For rent - Studio apartment in the Sun Cosmo Residence, convenient area, Đà Nẵng City»
  * 2222237321737260 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000, 14,000,000
  * 2221611245133201 -- в посте несколько разных цен: 7,500,000, 8,000,000
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
  * 3837694026371144 -- район не определяется по адресу «2 bedrooms»; прецедент расколот: «LVCC»: lt 1
  * 3841518345988712 -- район не определяется по адресу «fully furnished with a private washing machine»
  * 3840038072803406 -- район не определяется по адресу «APARTMENT FOR RENT»; прецедент расколот: «CT6»: ttr 1
  * 3838846259589254 -- в посте несколько разных цен: 14,500,000, 15,500,000
  * 4615612555374932 -- район не определяется по адресу «Muong Thanh 04 Tran Phu»
  * 4619753401627514 -- район не определяется по адресу «Tran Phu - Nha Trang»
  * 4619187528350768 -- в посте несколько разных цен: 500,000, 12,500,000
  * 4617186755217512 -- это поиск жилья, а не предложение
  * 4618707241732130 -- нет ни одной скачанной фотографии
  * 4611904355745752 -- нет ни одной скачанной фотографии
  * 4618733135062874 -- это поиск жилья, а не предложение
  * 2713243959107879 -- адрес называет несколько районов: btr, vh
  * 2714520092313599 -- в посте несколько разных цен: 1,000,000, 10,000,000
  * 2717514738680801 -- район не определяется по адресу «fully furnished with a private washing machine»
  * 2716907985408143 -- в посте несколько разных цен: 11,500,000, 12,500,000
  * 2716165988815676 -- район не определяется по адресу «NT RENT»
  * 1974105989951835 -- тип жилья в тексте не назван
  * 1972456823450085 -- район не определяется по адресу «CHO THUÊ CHUNG CƯ HƯNG PHÚ»
  * 1975747079787726 -- в тексте есть и другая цена того же порядка: 85,845,478 против 68,000,000
  * 1973536030008831 -- тип жилья в тексте не назван
  * 1968092573886510 -- тот же текст уже заведён: id new:thuecanhotronhatrang/1976587589703675
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

IDS = [3001221, 3001222, 3001223, 3001224, 3001225, 3001226, 3001227, 3001228, 3001229, 3001230, 3001231, 3001232, 3001233, 3001234, 3001235, 3001236]

NEW_SRC = r'''
L(3001221,"nha-trang","btr","Квартира",18500000,45,
  "Квартира, 45 м², Bắc Nha Trang.",
  "https://www.facebook.com/groups/849441571863086/posts/3841464279327452/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, 45 m², Bắc Nha Trang.",
  details={"photos": ["assets/fb_photos/3841464279327452/01.webp", "assets/fb_photos/3841464279327452/02.webp", "assets/fb_photos/3841464279327452/03.webp", "assets/fb_photos/3841464279327452/04.webp", "assets/fb_photos/3841464279327452/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001222,"nha-trang","vt","Квартира",15000000,60,
  "2-спальная квартира, 60 м², Vĩnh Trường.",
  "https://www.facebook.com/groups/849441571863086/posts/3841247709349109/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="2-bedroom flat, 60 m², Vĩnh Trường.",
  details={"photos": ["assets/fb_photos/3841247709349109/01.webp", "assets/fb_photos/3841247709349109/02.webp", "assets/fb_photos/3841247709349109/03.webp", "assets/fb_photos/3841247709349109/04.webp", "assets/fb_photos/3841247709349109/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001223,"nha-trang","lt","Квартира",11000000,35,
  "Квартира, 35 м², Lộc Thọ.",
  "https://www.facebook.com/groups/849441571863086/posts/3841439605996586/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, 35 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/3841439605996586/01.webp", "assets/fb_photos/3841439605996586/02.webp", "assets/fb_photos/3841439605996586/03.webp", "assets/fb_photos/3841439605996586/04.webp", "assets/fb_photos/3841439605996586/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001224,"nha-trang","ph","Квартира",12000000,45,
  "1-спальная квартира, 45 м², Phước Hải.",
  "https://www.facebook.com/groups/849441571863086/posts/3840556076084939/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="1-bedroom flat, 45 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/3840556076084939/01.webp", "assets/fb_photos/3840556076084939/02.webp", "assets/fb_photos/3840556076084939/03.webp", "assets/fb_photos/3840556076084939/04.webp", "assets/fb_photos/3840556076084939/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001225,"nha-trang","lt","Квартира",10000000,30,
  "Квартира, 30 м², Lộc Thọ.",
  "https://www.facebook.com/groups/849441571863086/posts/3839108232896390/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, 30 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/3839108232896390/01.webp", "assets/fb_photos/3839108232896390/02.webp", "assets/fb_photos/3839108232896390/03.webp", "assets/fb_photos/3839108232896390/04.webp", "assets/fb_photos/3839108232896390/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001226,"nha-trang","vn","Квартира",14500000,None,
  "1-спальная квартира, Vĩnh Nguyên.",
  "https://www.facebook.com/groups/chothue79/posts/4615520195384168/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="1-bedroom flat, Vĩnh Nguyên.",
  details={"photos": ["assets/fb_photos/4615520195384168/01.webp", "assets/fb_photos/4615520195384168/02.webp", "assets/fb_photos/4615520195384168/03.webp", "assets/fb_photos/4615520195384168/04.webp", "assets/fb_photos/4615520195384168/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001227,"nha-trang","vp","Квартира",25000000,None,
  "Квартира, Vĩnh Phước — 1 санузел.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2714566965642245/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, Vĩnh Phước — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2714566965642245/01.webp", "assets/fb_photos/2714566965642245/02.webp", "assets/fb_photos/2714566965642245/03.webp", "assets/fb_photos/2714566965642245/04.webp", "assets/fb_photos/2714566965642245/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001228,"nha-trang","vp","Квартира",23000000,None,
  "3-спальная квартира, Vĩnh Phước — 2 санузла.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2714405582325050/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="3-bedroom flat, Vĩnh Phước — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/2714405582325050/01.webp", "assets/fb_photos/2714405582325050/02.webp", "assets/fb_photos/2714405582325050/03.webp", "assets/fb_photos/2714405582325050/04.webp", "assets/fb_photos/2714405582325050/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001229,"nha-trang","btr","Квартира",24000000,60,
  "Квартира, 60 м², Bắc Nha Trang — 1 санузел.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2712131079219167/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, 60 m², Bắc Nha Trang — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2712131079219167/01.webp", "assets/fb_photos/2712131079219167/02.webp", "assets/fb_photos/2712131079219167/03.webp", "assets/fb_photos/2712131079219167/04.webp", "assets/fb_photos/2712131079219167/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001230,"nha-trang","btr","Квартира",11500000,None,
  "1-спальная квартира, Bắc Nha Trang.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2715436048888670/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="1-bedroom flat, Bắc Nha Trang.",
  details={"photos": ["assets/fb_photos/2715436048888670/01.webp", "assets/fb_photos/2715436048888670/02.webp", "assets/fb_photos/2715436048888670/03.webp", "assets/fb_photos/2715436048888670/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001231,"nha-trang","ph","Квартира",20000000,91,
  "3-спальная квартира, 91 м², Phước Hải — 2 санузла.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1950686778960423/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="3-bedroom flat, 91 m², Phước Hải — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1950686778960423/01.webp", "assets/fb_photos/1950686778960423/02.webp", "assets/fb_photos/1950686778960423/03.webp", "assets/fb_photos/1950686778960423/04.webp", "assets/fb_photos/1950686778960423/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001232,"nha-trang","btr","Квартира",15000000,55,
  "2-спальная квартира, 55 м², Bắc Nha Trang — 2 санузла.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1976374273058340/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="2-bedroom flat, 55 m², Bắc Nha Trang — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1976374273058340/01.webp", "assets/fb_photos/1976374273058340/02.webp", "assets/fb_photos/1976374273058340/03.webp", "assets/fb_photos/1976374273058340/04.webp", "assets/fb_photos/1976374273058340/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001233,"nha-trang","lt","Квартира",15000000,35,
  "Квартира, 35 м², Lộc Thọ.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1977194386309662/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, 35 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/1977194386309662/01.webp", "assets/fb_photos/1977194386309662/02.webp", "assets/fb_photos/1977194386309662/03.webp", "assets/fb_photos/1977194386309662/04.webp", "assets/fb_photos/1977194386309662/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001234,"nha-trang","ph","Квартира",12500000,40,
  "Квартира, 40 м², Phước Hải.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1976650559697378/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="Flat, 40 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/1976650559697378/01.webp", "assets/fb_photos/1976650559697378/02.webp", "assets/fb_photos/1976650559697378/03.webp", "assets/fb_photos/1976650559697378/04.webp", "assets/fb_photos/1976650559697378/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001235,"nha-trang","ntr","Дом",25000000,80,
  "Дом, 80 м², Thích Quảng Đức, Nam Nha Trang.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1976587589703675/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="House, 80 m², Thích Quảng Đức, Nam Nha Trang.",
  details={"photos": ["assets/fb_photos/1976587589703675/01.webp", "assets/fb_photos/1976587589703675/02.webp", "assets/fb_photos/1976587589703675/03.webp", "assets/fb_photos/1976587589703675/04.webp", "assets/fb_photos/1976587589703675/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001236,"nha-trang","tl","Квартира",28000000,90,
  "2-спальная квартира, 90 м², Tân Lập — 2 санузла.",
  "https://www.facebook.com/groups/2253829621529798/posts/4717511835161552/","сегодня",0,source="fbgroup",postedOn="2026-09-23",
  descEn="2-bedroom flat, 90 m², Tân Lập — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/4717511835161552/01.webp", "assets/fb_photos/4717511835161552/02.webp", "assets/fb_photos/4717511835161552/03.webp", "assets/fb_photos/4717511835161552/04.webp", "assets/fb_photos/4717511835161552/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
