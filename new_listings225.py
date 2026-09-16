# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 7 строк, 2026-09-16.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * CHOTHUE.NHATRO.NHARIENG.HAIPHONG/28801798442764887 -- hai-phong/lch, 6,500,000 VND: район назван в адресе поста
  * chothuenhataihaiphong/4512273855690437 -- hai-phong/lch, 6,000,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1858509245467798 -- ho-chi-minh/ak, 15,000,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1857337518918304 -- ho-chi-minh/ak, 13,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1960803818329373 -- ho-chi-minh/ak, 24,000,000 VND: район назван в адресе поста
  * 224805677963542/2584610558649697 -- manila/mla, 20,000 PHP: «MALATE»: 2 строк сайта, все в mla
  * chothuecanhogiarenhatrang/2063549741145794 -- nha-trang/ph, 25,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (97):
  * 2371615766711304 -- в тексте есть и другая цена того же порядка: 7,833 против 18,000
  * 2376926116180269 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2370985886774292 -- район не определяется по адресу «Ready for viewing na❗»
  * 2376287629577451 -- в тексте есть и другая цена того же порядка: 7,833 против 16,000
  * 2373856576487223 -- в посте несколько разных цен: 30,372, 350,000
  * 4543273292599036 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4477021965890836 -- нет ни одной скачанной фотографии
  * 4541720556087643 -- продажа
  * 2373354519870762 -- район не определяется по адресу «HOUSE FOR RENT ‼️ ALMIYA SUBDIVISION»
  * 4528691044057261 -- район не определяется по адресу «3BR HOUSE FOR RENT IN METROPOLIS SUBDIVISION NEAR »
  * 4521497431443289 -- район не определяется по адресу «Bulacao Luyo Prince Warehouse»
  * 2125924031352847 -- нет ни одной скачанной фотографии
  * 2134554663823117 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 2076569656288285 -- уже на сайте: id 3000757
  * 3752397751583992 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 3752100554947045 -- район не определяется по адресу «/ Location:** C6 Mạc Đĩnh Chi»
  * 3738232963000471 -- помещение под бизнес или здание целиком, а не жильё
  * 3672523882904713 -- тот же текст уже заведён: id 3000757
  * 2220561435238182 -- улица Phạm Vấn идёт через несколько районов (ah 1, st 1)
  * 2215626562398336 -- тип жилья в тексте не назван
  * 4610163709240779 -- район не определяется по адресу «Avilina Tinaypan Apartment»
  * 4610204959236654 -- в посте несколько разных цен: 15,000, 22,000
  * 2229008354338676 -- район не определяется по адресу «YOUR NEXT HOME: NEW 3BR HOUSE FOR RENT»
  * 2220626071843571 -- нет ни одной скачанной фотографии
  * 2234753327097512 -- нет ни одной скачанной фотографии
  * 4602196563370827 -- район не определяется по адресу «1-BEDROOM APARTMENT FOR RENT»
  * 4602042140052936 -- в тексте есть и другая цена того же порядка: 9,068 против 15,000
  * 2235589800347198 -- уже на сайте: id 3000758
  * 2263786434234413 -- тип жилья в тексте не назван
  * 2274703299809393 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2273544739925249 -- нет ни одной скачанной фотографии
  * 2267841370495586 -- тип жилья в тексте не назван
  * 2251798492099874 -- помещение под бизнес или здание целиком, а не жильё
  * 1082385114784501 -- тот же текст уже заведён: id 3000560
  * 28810423058569092 -- район не определяется по адресу «T2960»
  * 28778926491718749 -- район не определяется по адресу «𝗖𝗛𝗢 𝗧𝗛𝗨Ê 𝗦𝗧𝗨𝗗𝗜𝗢 𝗟Ê 𝗛Ồ𝗡𝗚 𝗣𝗛O𝗡𝗚 - 𝗧0656»
  * 28730305976580801 -- район не определяется по адресу «T2938 Cho thuê nhà Ngô Gia Tự - Văn Cao»
  * 28714148764863189 -- район не определяется по адресу «🇻🇳 │ LÊ HỒNG PHONG»
  * 28809707778640620 -- район не определяется по адресу «🇻🇳🇻🇳🇻🇳 VINHOMES MARINA»
  * 4512309235686899 -- похоже на уже заведённое: id 3000657
  * 4512293565688466 -- район не определяется по адресу «🇻🇳🇻🇳🇻🇳 VINHOMES MARINA»
  * 1858110785507644 -- похоже на уже заведённое: id 1003984
  * 1858166655502057 -- тип жилья в тексте не назван
  * 1858420938809962 -- похоже на уже заведённое: id 1002385
  * 1857315212253868 -- район не определяется по адресу «BRIGHT & SPACIOUS 1BR»
  * 1958911608518594 -- район не определяется по адресу «APARTMENT HIGHLIGHTS»
  * 1960331325043289 -- район не определяется по адресу «HOT DEAL»; прецедент расколот: «HOT DEAL»: ak 1; «NET»: ak 1
  * 1960769064999515 -- район не определяется по адресу «Tạ Quang Bửu»; прецедент расколот: «🔥 HOT DEAL»: ak 1
  * 1958843148525440 -- район не определяется по адресу «THE VISTA»
  * 1959719635104458 -- район не определяется по адресу «HOT DEAL»; прецедент расколот: «HOT DEAL»: ak 1
  * 2010891479589235 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 1993632857981764 -- нет ни одной скачанной фотографии
  * 2010975296247520 -- район не определяется по адресу «ENTIRE HOUSE FOR RENT»
  * 1700515498173867 -- в тексте есть и другая цена того же порядка: 7,500,000 против 15,000,000
  * 1694743462084404 -- район не определяется по адресу «3-Bedroom House for Rent»
  * 1697457151813035 -- в тексте есть и другая цена того же порядка: 7,500,000 против 15,000,000
  * 2323384675064867 -- район не определяется по адресу «House for rent in Cam Thanh»
  * 2583972028713550 -- тип жилья в тексте не назван
  * 2584636301980456 -- тип жилья в тексте не назван
  * 2581711695606250 -- продажа
  * 2584475118663241 -- продажа
  * 2584471455330274 -- район не определяется по адресу «Benefits:»
  * 2401583067250000 -- район не определяется по адресу «APARTMENT FOR RENT»
  * 2390246748383632 -- район не определяется по адресу «FOR RENT - 1BR-APARMENT UNIT IN SAMPALOC MANILA.»
  * 2401834793891494 -- район не определяется по адресу «Napico Manggahan Pasig City»
  * 2399902690751371 -- нет ни одной скачанной фотографии
  * 2401137383961235 -- район не определяется по адресу «Fully Furnished 1 Bedroom Condo Unit For Rent - Un»
  * 2063894454444656 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2062607131240055 -- район не определяется по адресу «Khanh Hoa»
  * 3277316822479411 -- район не определяется по адресу «Le Duc Tho Street»; прецедент расколот: «Le Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место; «Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место
  * 3276787252532368 -- тип жилья в тексте не назван
  * 3255608651316895 -- район не определяется по адресу «Ngay Đại học FPT»
  * 3273225212888572 -- район не определяется по адресу «Khu đô thị An Phú Thịnh»
  * 2126105611361434 -- в посте несколько разных цен: 10,000,000, 13,000,000
  * 2129626641009331 -- тип жилья в тексте не назван
  * 2130067840965211 -- район не определяется по адресу «Le Duc Tho Street»; прецедент расколот: «Le Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место; «Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место
  * 2130501094255219 -- район не определяется по адресу «44 Vo Thi Yen Street»
  * 2119050485400280 -- это поиск жилья, а не предложение
  * 3278586459019114 -- район не определяется по адресу «CHO THUÊ CHUNG CƯ PHÚ TÀI CENTRAL LIFE (HOÀNG VĂN »
  * 3278700075674419 -- район не определяется по адресу «Le Duc Tho Street»; прецедент расколот: «Le Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место; «Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место
  * 2131129990858996 -- район не определяется по адресу «CHO THUÊ CHUNG CƯ PHÚ TÀI CENTRAL LIFE (HOÀNG VĂN »
  * 2131353820836613 -- район не определяется по адресу «💥CHO THUÊ CĂN HỘ PHÚ TÀI RESIDENCE QUY NHƠN 💥»
  * 2131223370849658 -- район не определяется по адресу «Le Duc Tho Street»; прецедент расколот: «Le Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место; «Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место
  * 1445448987399170 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»; прецедент расколот: «Xô Viết Nghệ Tĩnh»: vtp 1; «Viết Nghệ Tĩnh»: vtp 1
  * 1463642598913142 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 1452094226734646 -- уже на сайте: id 3000759
  * 3213120192216198 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»; прецедент расколот: «Xô Viết Nghệ Tĩnh»: vtp 1; «Viết Nghệ Tĩnh»: vtp 1
  * 3236985219829695 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 3236874719840745 -- помещение под бизнес или здание целиком, а не жильё
  * 3203441086517442 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ»
  * 3232506143610936 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 3170988256429392 -- район не определяется по адресу «gồm 1 phòng ngủ»
  * 3161796947348523 -- район не определяется по адресу «**CHO THUÊ CĂN HỘ MINI ĐƯỜNG THỐNG NHẤT»
  * 1469609108316491 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 1446052310672171 -- район не определяется по адресу «Cho thuê Chung cư gold sea»
"""
from listing_lock import insert_listings

IDS = [3000810, 3000811, 3000812, 3000813, 3000814, 3000815, 3000816]

NEW_SRC = r'''
L(3000810,"hai-phong","lch","Квартира",6500000,35,
  "Квартира, 35 м², Lê Chân — 1 санузел.",
  "https://www.facebook.com/groups/CHOTHUE.NHATRO.NHARIENG.HAIPHONG/posts/28801798442764887/","сегодня",0,source="fbgroup",postedOn="2026-09-16",
  descEn="Flat, 35 m², Lê Chân — 1 bathroom.",
  details={"photos": ["assets/fb_photos/28801798442764887/01.webp", "assets/fb_photos/28801798442764887/02.webp", "assets/fb_photos/28801798442764887/03.webp", "assets/fb_photos/28801798442764887/04.webp", "assets/fb_photos/28801798442764887/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000811,"hai-phong","lch","Квартира",6000000,30,
  "1-спальная квартира, 30 м², Lê Chân — 1 санузел.",
  "https://www.facebook.com/groups/chothuenhataihaiphong/posts/4512273855690437/","сегодня",0,source="fbgroup",postedOn="2026-09-16",
  descEn="1-bedroom flat, 30 m², Lê Chân — 1 bathroom.",
  details={"photos": ["assets/fb_photos/4512273855690437/01.webp", "assets/fb_photos/4512273855690437/02.webp", "assets/fb_photos/4512273855690437/03.webp", "assets/fb_photos/4512273855690437/04.webp", "assets/fb_photos/4512273855690437/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000812,"ho-chi-minh","ak","Студия",15000000,45,
  "Студия, 45 м², An Khánh — 1 санузел.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1858509245467798/","сегодня",0,source="fbgroup",postedOn="2026-09-16",
  descEn="Studio, 45 m², An Khánh — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1858509245467798/01.webp", "assets/fb_photos/1858509245467798/02.webp", "assets/fb_photos/1858509245467798/03.webp", "assets/fb_photos/1858509245467798/04.webp", "assets/fb_photos/1858509245467798/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000813,"ho-chi-minh","ak","Студия",13000000,45,
  "Студия, 45 м², An Khánh.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1857337518918304/","сегодня",0,source="fbgroup",postedOn="2026-09-16",
  descEn="Studio, 45 m², An Khánh.",
  details={"photos": ["assets/fb_photos/1857337518918304/01.webp", "assets/fb_photos/1857337518918304/02.webp", "assets/fb_photos/1857337518918304/03.webp", "assets/fb_photos/1857337518918304/04.webp", "assets/fb_photos/1857337518918304/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000814,"ho-chi-minh","ak","Квартира",24000000,110,
  "3-спальная квартира, 110 м², An Khánh — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1960803818329373/","сегодня",0,source="fbgroup",postedOn="2026-09-16",
  descEn="3-bedroom flat, 110 m², An Khánh — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1960803818329373/01.webp", "assets/fb_photos/1960803818329373/02.webp", "assets/fb_photos/1960803818329373/03.webp", "assets/fb_photos/1960803818329373/04.webp", "assets/fb_photos/1960803818329373/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3000815,"manila","mla","Квартира",20000,42,
  "2-спальная квартира, 42 м², MALATE, Malate / Ermita — 1 санузел.",
  "https://www.facebook.com/groups/224805677963542/posts/2584610558649697/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-16",
  descEn="2-bedroom flat, 42 m², MALATE, Malate / Ermita — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2584610558649697/01.webp", "assets/fb_photos/2584610558649697/02.webp", "assets/fb_photos/2584610558649697/03.webp", "assets/fb_photos/2584610558649697/04.webp", "assets/fb_photos/2584610558649697/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3000816,"nha-trang","ph","Квартира",25000000,90,
  "2-спальная квартира, 90 м², Phước Hải — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2063549741145794/","сегодня",0,source="fbgroup",postedOn="2026-09-16",
  descEn="2-bedroom flat, 90 m², Phước Hải — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/2063549741145794/01.webp", "assets/fb_photos/2063549741145794/02.webp", "assets/fb_photos/2063549741145794/03.webp", "assets/fb_photos/2063549741145794/04.webp", "assets/fb_photos/2063549741145794/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
