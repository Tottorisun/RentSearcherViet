# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 7 строк, 2026-09-18.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 1735327053393688/4546074128985619 -- cebu/man, 30,000 PHP: район назван в адресе поста
  * 153191128587086/2236609860245192 -- dumaguete/val, 28,000 PHP: район назван в адресе поста
  * 153191128587086/2236602116912633 -- dumaguete/bcg, 20,000 PHP: район назван в адресе поста
  * 153191128587086/2236869286885916 -- dumaguete/val, 40,000 PHP: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1860026475316075 -- ho-chi-minh/ak, 9,000,000 VND: район назван в адресе поста
  * 224805677963542/2585600158550737 -- manila/mdl, 23,000 PHP: район назван в адресе поста
  * 224805677963542/2583538828756870 -- manila/mdl, 22,000 PHP: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (104):
  * 3474885602689740 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 3489735917871375 -- это поиск жилья, а не предложение
  * 3111524002383926 -- это поиск жилья, а не предложение
  * 3086171178252542 -- район не определяется по адресу «Studio siêu đẹp»
  * 2730478847155112 -- помещение под бизнес или здание целиком, а не жильё
  * 39290383267226767 -- район не определяется по адресу «1/10 nhận phòng!»
  * 39313842264880867 -- в посте несколько разных цен: 2,600,000, 2,700,000
  * 39289709790627448 -- район не определяется по адресу «10/10 có phòng»
  * 38629798796618554 -- тип жилья в тексте не назван
  * 1757290509336915 -- цена 650,000 VND вне разумных пределов
  * 1725575419175091 -- тип жилья в тексте не назван
  * 1725714562494510 -- район не определяется по адресу «Chủ gửi»
  * 1725537895845510 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 1715148420217791 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NGUYỄN VĂN LI»
  * 1755508766181756 -- район не определяется по адресу «💒 PHÒNG TRỌ CÓ GÁC & BAN CÔNG KDC PHÚ AN - ĐỐI DIỆ»
  * 1755688602830439 -- в посте несколько разных цен: 2,600,000, 2,700,000
  * 1757674389298527 -- тип жилья в тексте не назван
  * 1757701769295789 -- тип жилья в тексте не назван
  * 39320797987518628 -- район не определяется по адресу «🎀💞🐟 PHÒNG TRỆT MỚI XÂY RỘNG 30M2 - ĐƯỜNG VÕ VĂN KI»
  * 1756319306100702 -- район не определяется по адресу «🏩 MINIHOUSE CAO CẤP FULL NỘI THẤT KẾ BÊN FPT»
  * 1758617719204194 -- тип жилья в тексте не назван
  * 2379456289260585 -- тип жилья в тексте не назван
  * 2379457085927172 -- тип жилья в тексте не назван
  * 2379509992588548 -- в посте несколько разных цен: 2,500, 5,000
  * 2377868909419323 -- район не определяется по адресу «FOR RENT: SEMI-FURNISHED 1-BEDROOM APARTMENT»
  * 2371615766711304 -- в тексте есть и другая цена того же порядка: 7,833 против 18,000
  * 2377927736080107 -- в посте несколько разных цен: 12,000, 17,000
  * 2376287629577451 -- в тексте есть и другая цена того же порядка: 7,833 против 16,000
  * 2377389776133903 -- в посте несколько разных цен: 18,000, 20,000, 26,000
  * 4543273292599036 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4541720556087643 -- продажа
  * 2125924031352847 -- нет ни одной скачанной фотографии
  * 2134554663823117 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 3752397751583992 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 3753978761425891 -- район не определяется по адресу «/ Location:** C6 Mạc Đĩnh Chi»
  * 3738232963000471 -- помещение под бизнес или здание целиком, а не жильё
  * 3672523882904713 -- тот же текст уже заведён: id 3000757
  * 4611225949134555 -- в тексте есть и другая цена того же порядка: 21,641 против 40,000
  * 4613476128909537 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4610204959236654 -- в посте несколько разных цен: 15,000, 22,000
  * 2238082586764586 -- рассрочка
  * 1858166655502057 -- тип жилья в тексте не назван
  * 1860020188650037 -- район не определяется по адресу «2 Ton Duc Thang»
  * 1858420938809962 -- похоже на уже заведённое: id 1002385
  * 1858110785507644 -- похоже на уже заведённое: id 1003984
  * 1958911608518594 -- район не определяется по адресу «APARTMENT HIGHLIGHTS»
  * 1962341911508897 -- район не определяется по адресу «🌿 CHO THUÊ CĂN HỘ 2PN VIEW LANDMARK 81»
  * 1960769064999515 -- район не определяется по адресу «Tạ Quang Bửu»; прецедент расколот: «🔥 HOT DEAL»: ak 1
  * 1962218594854562 -- район не определяется по адресу «Nguyễn Bỉnh Khiêm»; прецедент расколот: «🔥 HOT DEAL»: ak 1
  * 1962226554853766 -- район не определяется по адресу «Tran Khac Chan»
  * 2011716992840017 -- район не определяется по адресу «👉👉Cần cho thuê nhà mới full nội thất 2 phòng ngủ 1»
  * 2010975296247520 -- район не определяется по адресу «ENTIRE HOUSE FOR RENT»
  * 2010891479589235 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 1703111911247559 -- район не определяется по адресу «1-BEDROOM APARTMENT FOR RENT»
  * 2012595552752161 -- район не определяется по адресу «👉👉Cần cho thuê nhà mới full nội thất 2 phòng ngủ 1»
  * 2008953266449723 -- тип жилья в тексте не назван
  * 2011801119498271 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 1985882385452871 -- тот же текст уже заведён: id 3000552
  * 1997802540927522 -- район не определяется по адресу «đường Tố Hữu»
  * 1708277650381543 -- район не определяется по адресу «CHO THUÊ STUDIO CAO CẤP»
  * 1701057297770245 -- в посте несколько разных цен: 3,600,000, 3,700,000, 3,800,000
  * 1637646127444696 -- район не определяется по адресу «Không gian sống hiện đại»
  * 1251745672701412 -- в посте несколько разных цен: 4,000,000, 4,500,000, 4,800,000
  * 2583972028713550 -- тип жилья в тексте не назван
  * 2580076449103108 -- в тексте есть и другая цена того же порядка: 18,500 против 15,700
  * 2581711695606250 -- продажа
  * 2585147178596035 -- продажа
  * 2584471455330274 -- район не определяется по адресу «Benefits:»
  * 2585556971888389 -- тип жилья в тексте не назван
  * 2586048311839255 -- тип жилья в тексте не назван
  * 2404261026982204 -- в посте несколько разных цен: 6,000, 9,000, 14,000
  * 2404310366977270 -- район не определяется по адресу «Napico Manggahan Pasig City»
  * 2403826127025694 -- тип жилья в тексте не назван
  * 2401137383961235 -- район не определяется по адресу «Fully Furnished 1 Bedroom Condo Unit For Rent - Un»
  * 2586447371775918 -- помещение под бизнес или здание целиком, а не жильё
  * 2591654944588494 -- помещение под бизнес или здание целиком, а не жильё
  * 2582748732145782 -- тип жилья в тексте не назван
  * 2585080565245932 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 1756168655595818 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1757293212150029 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 2592618517825470 -- район не определяется по адресу «✨ Brand-new villa»
  * 3280507732160320 -- район не определяется по адресу «Ngay Đại học FPT»
  * 3278586459019114 -- район не определяется по адресу «CHO THUÊ CHUNG CƯ PHÚ TÀI CENTRAL LIFE (HOÀNG VĂN »
  * 3277316822479411 -- район не определяется по адресу «Le Duc Tho Street»
  * 3281095278768232 -- в посте несколько разных цен: 12,000,000, 20,000,000
  * 3278700075674419 -- район не определяется по адресу «Le Duc Tho Street»
  * 3280432182167875 -- в посте несколько разных цен: 840,000, 11,000,000
  * 3273225212888572 -- район не определяется по адресу «Khu đô thị An Phú Thịnh»
  * 2131353820836613 -- район не определяется по адресу «💥CHO THUÊ CĂN HỘ PHÚ TÀI RESIDENCE QUY NHƠN 💥»
  * 2119050485400280 -- это поиск жилья, а не предложение
  * 1469609108316491 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 1445448987399170 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»; прецедент расколот: «Xô Viết Nghệ Tĩnh»: vtp 1
  * 1463642598913142 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 3246119772249573 -- район не определяется по адресу «VILLA FOR RENT»
  * 3213120192216198 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»; прецедент расколот: «Xô Viết Nghệ Tĩnh»: vtp 1
  * 3236985219829695 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 3236874719840745 -- помещение под бизнес или здание целиком, а не жильё
  * 3232506143610936 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 3203441086517442 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ»
  * 3170988256429392 -- район не определяется по адресу «gồm 1 phòng ngủ»
  * 3161796947348523 -- район не определяется по адресу «**CHO THUÊ CĂN HỘ MINI ĐƯỜNG THỐNG NHẤT»
  * 3244620785732805 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
"""
from listing_lock import insert_listings

IDS = [3000864, 3000865, 3000866, 3000867, 3000868, 3000869, 3000870]

NEW_SRC = r'''
L(3000864,"cebu","man","Дом",30000,None,
  "4-спальный дом, Mandaue.",
  "https://www.facebook.com/groups/1735327053393688/posts/4546074128985619/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-18",
  descEn="4-bedroom house, Mandaue.",
  details={"photos": ["assets/fb_photos/4546074128985619/01.webp", "assets/fb_photos/4546074128985619/02.webp", "assets/fb_photos/4546074128985619/03.webp", "assets/fb_photos/4546074128985619/04.webp", "assets/fb_photos/4546074128985619/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000865,"dumaguete","val","Дом",28000,None,
  "2-спальный дом, Valencia — 1 санузел.",
  "https://www.facebook.com/groups/153191128587086/posts/2236609860245192/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-18",
  descEn="2-bedroom house, Valencia — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2236609860245192/01.webp", "assets/fb_photos/2236609860245192/02.webp", "assets/fb_photos/2236609860245192/03.webp", "assets/fb_photos/2236609860245192/04.webp", "assets/fb_photos/2236609860245192/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000866,"dumaguete","bcg","Дом",20000,None,
  "2-спальный дом, Bacong.",
  "https://www.facebook.com/groups/153191128587086/posts/2236602116912633/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-18",
  descEn="2-bedroom house, Bacong.",
  details={"photos": ["assets/fb_photos/2236602116912633/01.webp", "assets/fb_photos/2236602116912633/02.webp", "assets/fb_photos/2236602116912633/03.webp", "assets/fb_photos/2236602116912633/04.webp", "assets/fb_photos/2236602116912633/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000867,"dumaguete","val","Дом",40000,175,
  "Дом, 175 м², Valencia.",
  "https://www.facebook.com/groups/153191128587086/posts/2236869286885916/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-18",
  descEn="House, 175 m², Valencia.",
  details={"photos": ["assets/fb_photos/2236869286885916/01.webp", "assets/fb_photos/2236869286885916/02.webp", "assets/fb_photos/2236869286885916/03.webp", "assets/fb_photos/2236869286885916/04.webp", "assets/fb_photos/2236869286885916/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000868,"ho-chi-minh","ak","Студия",9000000,35,
  "Студия, 35 м², An Khánh.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1860026475316075/","сегодня",0,source="fbgroup",postedOn="2026-09-18",
  descEn="Studio, 35 m², An Khánh.",
  details={"photos": ["assets/fb_photos/1860026475316075/01.webp", "assets/fb_photos/1860026475316075/02.webp", "assets/fb_photos/1860026475316075/03.webp", "assets/fb_photos/1860026475316075/04.webp", "assets/fb_photos/1860026475316075/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000869,"manila","mdl","Квартира",23000,45,
  "2-спальная квартира, 45 м², Mandaluyong.",
  "https://www.facebook.com/groups/224805677963542/posts/2585600158550737/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-18",
  descEn="2-bedroom flat, 45 m², Mandaluyong.",
  details={"photos": ["assets/fb_photos/2585600158550737/01.webp", "assets/fb_photos/2585600158550737/02.webp", "assets/fb_photos/2585600158550737/03.webp", "assets/fb_photos/2585600158550737/04.webp", "assets/fb_photos/2585600158550737/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000870,"manila","mdl","Квартира",22000,30,
  "2-спальная квартира, 30 м², Mandaluyong.",
  "https://www.facebook.com/groups/224805677963542/posts/2583538828756870/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-18",
  descEn="2-bedroom flat, 30 m², Mandaluyong.",
  details={"photos": ["assets/fb_photos/2583538828756870/01.webp", "assets/fb_photos/2583538828756870/02.webp", "assets/fb_photos/2583538828756870/03.webp", "assets/fb_photos/2583538828756870/04.webp", "assets/fb_photos/2583538828756870/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
