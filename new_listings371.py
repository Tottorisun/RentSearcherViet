# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 18 строк, 2026-09-29.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * chothuecanhodanang43/1749070003415975 -- da-nang/ns, 15,000,000 VND: район назван в посте
  * chothuecanhodanang43/1747683616887947 -- da-nang/ns, 15,000,000 VND: район назван в посте; прежний район Ngu Hanh Son весь вошёл в этот
  * chothuecanhodanang43/1749470933375882 -- da-nang/ns, 18,000,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * canhochothuedanangtot/2236401146987544 -- da-nang/hx, 12,000,000 VND: район назван в посте
  * canhochothuedanangtot/2234640973830228 -- da-nang/ah, 10,000,000 VND: район назван в посте
  * canhochothuedanangtot/2229042801056712 -- da-nang/hk, 13,000,000 VND: улица Ngô Thì Nhậm: 11 из 12 отрезков в hk; пост: Lien Chieu
  * chungcumini.canhodichvu.phongtrotphcm/1871302410855148 -- ho-chi-minh/ak, 12,000,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1870376907614365 -- ho-chi-minh/ak, 24,000,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1870306850954704 -- ho-chi-minh/ak, 17,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1976354320107656 -- ho-chi-minh/ak, 42,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1975807876828967 -- ho-chi-minh/ak, 50,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1976356766774078 -- ho-chi-minh/ak, 45,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1974837923592629 -- ho-chi-minh/bth, 16,000,000 VND: район назван в адресе поста
  * 299437881275577/1802022997683717 -- manila/qzc, 25,000 PHP: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1118167457323809 -- nha-trang/pl, 25,000,000 VND: район назван в адресе поста
  * chothuecanhogiarenhatrang/2074267146740720 -- nha-trang/pl, 13,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1982808442414923 -- nha-trang/ntr, 5,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1983785945650506 -- nha-trang/ntr, 15,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (99):
  * 3766046853552415 -- это поиск жилья, а не предложение
  * 3762964507193983 -- район не определяется по адресу «/ Location:** Đường Mạc Đĩnh Chi»
  * 3752397751583992 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 3751083238382110 -- район не определяется по адресу «/ Location:** C6 Mạc Đĩnh Chi»
  * 3672523882904713 -- тот же текст уже заведён: id 3001274
  * 3669518326538602 -- нет ни одной скачанной фотографии
  * 3586443918179377 -- район не определяется по адресу «✅ Apartment for Rent - 2 Bedrooms - Truong Van Hoa»
  * 2125924031352847 -- это поиск жилья, а не предложение
  * 2134554663823117 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 2096068041005113 -- тип жилья в тексте не назван
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 2080210199257564 -- это поиск жилья, а не предложение
  * 1749174926738816 -- район не определяется: «MINI VILLA FOR RENT, PHAN KHOANG, Phan Khoang»
  * 1749179183405057 -- район не определяется: «BRAND-NEW 4-BEDROOM HOUSE FOR RENT, TRAN CAO VAN, DA NANG»
  * 1749294170060225 -- в посте несколько разных цен: 18,000,000, 20,000,000
  * 1748788876777421 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT, NAI NAM, HAI CHAU»
  * 1749196030070039 -- похоже на уже заведённое: id 1014099
  * 1749377270051915 -- район не определяется: «1 Bedroom Apartment, 🏠1 Bedroom Apartment»
  * 1746986366957672 -- в посте несколько разных цен: 9,000,000, 11,000,000
  * 2234141570546835 -- в посте несколько разных цен: 15,000,000, 17,000,000
  * 2228142007813458 -- район не определяется: «Panoma 1, Đà Nẵng, Panoma 1»
  * 2208355459792113 -- район не определяется: «CĂN HỘ 2PN, 2-BEDROOM APARTMENT, Biển 1»
  * 2366385470866466 -- район не определяется: «🇻🇳2BR VILLA FOR RENT, SON TRA, DA NANG»
  * 2364890091016004 -- район не определяется: «Newly built house available for rent»
  * 2362788734559473 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT, AN THUONG 14, An Thuong 14»
  * 2363015744536772 -- район не определяется: «HOUSE FOR RENT ON NGUYEN TRI PHUONG STREET, HAI CHAU, 🏠 HOUSE FOR RENT ON NGUYEN TRI PHUONG STREET»
  * 3821605077995387 -- тип жилья в тексте не назван
  * 3819441944878367 -- тип жилья в тексте не назван
  * 3821479454674616 -- помещение под бизнес или здание целиком, а не жильё
  * 3805749332914295 -- тип жилья в тексте не назван
  * 1839186734095407 -- тип жилья в тексте не назван
  * 1798998168114264 -- тип жилья в тексте не назван
  * 1818287229518691 -- тип жилья в тексте не назван
  * 2003720763597570 -- район не определяется по адресу «T2922»
  * 2014739465829033 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 2016652748971038 -- район не определяется по адресу «T2986 Cho Thuê Nhà Văn Cao»
  * 2017140412255605 -- район не определяется по адресу «T2983»; прецедент расколот: «LẠCH TRAY»: совпало только в ссылках строк gvi -- это реклама, а не место
  * 2018000975502882 -- район не определяется по адресу «Võ Nguyên Giáp»
  * 2017684395534540 -- район не определяется по адресу «Cho thuê căn hộ Penthouse 1 ngủ tách bếp to rộng t»; прецедент расколот: «WaterFront»: совпало только в ссылках строк anb2 -- это реклама, а не место
  * 28981446664800063 -- район не определяется по адресу «Cho Thuê Chung Cư Sentosa Sky Park»; прецедент расколот: «Sentosa Sky Park»: совпало только в ссылках строк lch -- это реклама, а не место
  * 28948373588107371 -- район не определяется по адресу «HH422 Cho Thuê Chung Cư Hoàng Huy Commerce - Lotus»
  * 28987445850866811 -- район не определяется по адресу «T0108 Cho Thuê Căn hộ Vinhomes Marina»
  * 28981472958130767 -- район не определяется по адресу «T2734 Cho thuê chung cư Sentosa Sky Park»; прецедент расколот: «Sentosa Sky Park»: совпало только в ссылках строк lch -- это реклама, а не место
  * 28959217347022995 -- район не определяется по адресу «🇻🇳 │ VINHOMES MARINA»
  * 1853134039338652 -- район не определяется по адресу «English below ⬇️»
  * 1865296498122406 -- похоже на уже заведённое: id 1011268
  * 1976283110114777 -- район не определяется по адресу «RARE PENTHOUSE»
  * 1975996423476779 -- в посте несколько разных цен: 500,000, 13,000,000
  * 1975226316887123 -- район не определяется по адресу «Tân Cảng»
  * 2416297615778545 -- район не определяется по адресу «Available 1 Unit for Rent - Metrica St. Sampaloc M»
  * 2409421553132818 -- в посте несколько разных цен: 10,000, 12,000
  * 2415051862569787 -- в тексте есть и другая цена того же порядка: 7,796 против 20,500
  * 2390246748383632 -- район не определяется по адресу «FOR RENT - 1BR-APARMENT UNIT IN SAMPALOC MANILA.»
  * 2415501675858139 -- район не определяется по адресу «APARTMENT FOR RENT»
  * 2414173732657600 -- в посте несколько разных цен: 15,000, 20,000
  * 1802711964281487 -- тип жилья в тексте не назван
  * 1797050891514261 -- в посте несколько разных цен: 12,000, 13,000, 14,000, 15,000, 17,000, 18,000, 20,000
  * 1798992321320118 -- район не определяется по адресу «- Taft Avenue Manila 15Floor»
  * 1797047358181281 -- тот же текст уже заведён: id 3001120
  * 1801921144360569 -- в посте несколько разных цен: 7,000, 17,000
  * 1118269267313628 -- район не определяется по адресу «An Bình Tân»
  * 1118307227309832 -- район не определяется по адресу «Convenient location in a lively residential area»
  * 1118327047307850 -- в посте несколько разных цен: 500,000, 17,000,000
  * 1118327377307817 -- район не определяется по адресу «Panorama Nha Trang»
  * 1118331140640774 -- район не определяется по адресу «Southern Nha Trang»
  * 1117854047355150 -- район не определяется по адресу «Apartment for rent - 1 bedroom»
  * 1117203214086900 -- тот же текст уже заведён: id 3001619
  * 1118277630646125 -- тип жилья в тексте не назван
  * 1117994190674469 -- в посте несколько разных цен: 700,000, 15,500,000
  * 2066052177562217 -- похоже на уже заведённое: id 2000908
  * 2075154193318682 -- похоже на уже заведённое: id 3001125
  * 2074927750007993 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2069346347232800 -- это поиск жилья, а не предложение
  * 2073049100195858 -- район не определяется по адресу «CHO THUÊ NHÀ 3 TẦNG»
  * 2075165209984247 -- район не определяется по адресу «Vinh Diem Trung»
  * 4625597054376482 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4620125994923588 -- это поиск жилья, а не предложение
  * 4615612555374932 -- район не определяется по адресу «Muong Thanh 04 Tran Phu»
  * 2718900588542216 -- в посте несколько разных цен: 1,000,000, 18,000,000
  * 2724499167982358 -- район не определяется по адресу «Great location:»
  * 2725069237925351 -- район не определяется по адресу «BRAND-NEW HOUSE FOR RENT»
  * 2724867841278824 -- район не определяется по адресу «City center»
  * 2722002958231979 -- тот же текст уже заведён: id 3001614
  * 2721785808253694 -- нет ни одной скачанной фотографии
  * 2725075927924682 -- район не определяется по адресу «NT RENT»
  * 1981279022567865 -- район не определяется по адресу «Central location»
  * 1983758185653282 -- район не определяется по адресу «CHO THUÊ NHÀ MỚI XÂY»
  * 1980921325936968 -- это поиск жилья, а не предложение
  * 1981650005864100 -- тот же текст уже заведён: id 3001614
  * 3848235645316982 -- район не определяется по адресу «Convenient residential area with plenty of ameniti»
  * 3848866261920587 -- район не определяется по адресу «Convenient location in a lively residential area»
  * 3847311922076021 -- в посте несколько разных цен: 2,000,000, 9,000,000
  * 3849699658503914 -- район не определяется по адресу «Southern Nha Trang»
  * 3850417528432127 -- похоже на уже заведённое: id 3001535
  * 3850156065124940 -- адрес называет несколько районов: btr, vh
  * 3850029455137601 -- в посте несколько разных цен: 9,500,000, 10,000,000
  * 2136536980318297 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 2143930936245568 -- район не определяется по адресу «⭐️⭐️ CHO THUÊ CĂN HỘ ALTARA RESIDENCE»
"""
from listing_lock import insert_listings

IDS = [3001688, 3001689, 3001690, 3001691, 3001692, 3001693, 3001694, 3001695, 3001696, 3001697, 3001698, 3001699, 3001700, 3001701, 3001702, 3001703, 3001704, 3001705]

NEW_SRC = r'''
L(3001688,"da-nang","ns","Квартира",15000000,None,
  "1-спальная квартира, My An Stress, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1749070003415975/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="1-bedroom flat, My An Stress, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1749070003415975/01.webp", "assets/fb_photos/1749070003415975/02.webp", "assets/fb_photos/1749070003415975/03.webp", "assets/fb_photos/1749070003415975/04.webp", "assets/fb_photos/1749070003415975/05.webp"], "am": ["lift"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001689,"da-nang","ns","Квартира",15000000,None,
  "1-спальная квартира, Cozy 1-Bedroom Apartment for Rent, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1747683616887947/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="1-bedroom flat, Cozy 1-Bedroom Apartment for Rent, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1747683616887947/01.webp", "assets/fb_photos/1747683616887947/02.webp", "assets/fb_photos/1747683616887947/03.webp", "assets/fb_photos/1747683616887947/04.webp", "assets/fb_photos/1747683616887947/05.webp"], "fl": 2, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001690,"da-nang","ns","Квартира",18000000,None,
  "2-спальная квартира, 🌴🐚 2BR APARTMENT NEAR THE BEACH, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1749470933375882/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="2-bedroom flat, 🌴🐚 2BR APARTMENT NEAR THE BEACH, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1749470933375882/01.webp", "assets/fb_photos/1749470933375882/02.webp", "assets/fb_photos/1749470933375882/03.webp", "assets/fb_photos/1749470933375882/04.webp", "assets/fb_photos/1749470933375882/05.webp"], "am": ["w", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001691,"da-nang","hx","Студия",12000000,None,
  "Студия, ✨ MODERN STUDIO APARTMENT, Hòa Xuân.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2236401146987544/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="Studio, ✨ MODERN STUDIO APARTMENT, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/2236401146987544/01.webp", "assets/fb_photos/2236401146987544/02.webp", "assets/fb_photos/2236401146987544/03.webp", "assets/fb_photos/2236401146987544/04.webp", "assets/fb_photos/2236401146987544/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001692,"da-nang","ah","Квартира",10000000,None,
  "1-спальная квартира, APARTMENT, An Hải.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2234640973830228/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="1-bedroom flat, APARTMENT, An Hải.",
  details={"photos": ["assets/fb_photos/2234640973830228/01.webp", "assets/fb_photos/2234640973830228/02.webp", "assets/fb_photos/2234640973830228/03.webp", "assets/fb_photos/2234640973830228/04.webp", "assets/fb_photos/2234640973830228/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001693,"da-nang","hk","Квартира",13000000,63,
  "2-спальная квартира, 63 м², Ngô Thì Nhậm, Hòa Khánh — 2 санузла.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2229042801056712/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="2-bedroom flat, 63 m², Ngô Thì Nhậm, Hòa Khánh — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/2229042801056712/01.webp", "assets/fb_photos/2229042801056712/02.webp", "assets/fb_photos/2229042801056712/03.webp", "assets/fb_photos/2229042801056712/04.webp", "assets/fb_photos/2229042801056712/05.webp"], "am": ["pool"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001694,"ho-chi-minh","ak","Студия",12000000,40,
  "Студия, 40 м², An Khánh.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1871302410855148/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="Studio, 40 m², An Khánh.",
  details={"photos": ["assets/fb_photos/1871302410855148/01.webp", "assets/fb_photos/1871302410855148/02.webp", "assets/fb_photos/1871302410855148/03.webp", "assets/fb_photos/1871302410855148/04.webp", "assets/fb_photos/1871302410855148/05.webp"], "am": ["pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001695,"ho-chi-minh","ak","Студия",24000000,None,
  "Студия, An Khánh — 2 санузла.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1870376907614365/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="Studio, An Khánh — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1870376907614365/01.webp", "assets/fb_photos/1870376907614365/02.webp", "assets/fb_photos/1870376907614365/03.webp", "assets/fb_photos/1870376907614365/04.webp", "assets/fb_photos/1870376907614365/05.webp"], "am": ["k", "win", "pool", "gym"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001696,"ho-chi-minh","ak","Квартира",17000000,45,
  "1-спальная квартира, 45 м², An Khánh — 1 санузел.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1870306850954704/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="1-bedroom flat, 45 m², An Khánh — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1870306850954704/01.webp", "assets/fb_photos/1870306850954704/02.webp", "assets/fb_photos/1870306850954704/03.webp", "assets/fb_photos/1870306850954704/04.webp", "assets/fb_photos/1870306850954704/05.webp"], "am": ["k", "win"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001697,"ho-chi-minh","ak","Квартира",42000000,99,
  "3-спальная квартира, 99 м², An Khánh — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1976354320107656/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="3-bedroom flat, 99 m², An Khánh — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1976354320107656/01.webp", "assets/fb_photos/1976354320107656/02.webp", "assets/fb_photos/1976354320107656/03.webp", "assets/fb_photos/1976354320107656/04.webp", "assets/fb_photos/1976354320107656/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001698,"ho-chi-minh","ak","Квартира",50000000,145,
  "2-спальная квартира, 145 м², An Khánh — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1975807876828967/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="2-bedroom flat, 145 m², An Khánh — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1975807876828967/01.webp", "assets/fb_photos/1975807876828967/02.webp", "assets/fb_photos/1975807876828967/03.webp", "assets/fb_photos/1975807876828967/04.webp", "assets/fb_photos/1975807876828967/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001699,"ho-chi-minh","ak","Квартира",45000000,130,
  "3-спальная квартира, 130 м², An Khánh — 3 санузла.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1976356766774078/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="3-bedroom flat, 130 m², An Khánh — 3 bathrooms.",
  details={"photos": ["assets/fb_photos/1976356766774078/01.webp", "assets/fb_photos/1976356766774078/02.webp", "assets/fb_photos/1976356766774078/03.webp", "assets/fb_photos/1976356766774078/04.webp", "assets/fb_photos/1976356766774078/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001700,"ho-chi-minh","bth","Квартира",16000000,60,
  "1-спальная квартира, 60 м², Bến Thành.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1974837923592629/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="1-bedroom flat, 60 m², Bến Thành.",
  details={"photos": ["assets/fb_photos/1974837923592629/01.webp", "assets/fb_photos/1974837923592629/02.webp", "assets/fb_photos/1974837923592629/03.webp", "assets/fb_photos/1974837923592629/04.webp", "assets/fb_photos/1974837923592629/05.webp"], "am": ["k", "lift"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001701,"manila","qzc","Квартира",25000,42,
  "2-спальная квартира, 42 м², Quezon City.",
  "https://www.facebook.com/groups/299437881275577/posts/1802022997683717/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-29",
  descEn="2-bedroom flat, 42 m², Quezon City.",
  details={"photos": ["assets/fb_photos/1802022997683717/01.webp", "assets/fb_photos/1802022997683717/02.webp", "assets/fb_photos/1802022997683717/03.webp", "assets/fb_photos/1802022997683717/04.webp", "assets/fb_photos/1802022997683717/05.webp"], "am": ["k", "pool", "gym", "pet"], "fl": 12, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001702,"nha-trang","pl","Квартира",25000000,94,
  "3-спальная квартира, 94 м², Phước Long — 2 санузла.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1118167457323809/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="3-bedroom flat, 94 m², Phước Long — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1118167457323809/01.webp", "assets/fb_photos/1118167457323809/02.webp", "assets/fb_photos/1118167457323809/03.webp", "assets/fb_photos/1118167457323809/04.webp", "assets/fb_photos/1118167457323809/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001703,"nha-trang","pl","Квартира",13000000,45,
  "1-спальная квартира, 45 м², Phước Long.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2074267146740720/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="1-bedroom flat, 45 m², Phước Long.",
  details={"photos": ["assets/fb_photos/2074267146740720/01.webp", "assets/fb_photos/2074267146740720/02.webp", "assets/fb_photos/2074267146740720/03.webp", "assets/fb_photos/2074267146740720/04.webp", "assets/fb_photos/2074267146740720/05.webp"], "am": ["w", "b", "win", "lift"], "fl": 4, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001704,"nha-trang","ntr","Квартира",5000000,None,
  "Квартира, T9 An Bình Tân, Nam Nha Trang.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1982808442414923/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="Flat, T9 An Bình Tân, Nam Nha Trang.",
  details={"photos": ["assets/fb_photos/1982808442414923/01.webp", "assets/fb_photos/1982808442414923/02.webp", "assets/fb_photos/1982808442414923/03.webp", "assets/fb_photos/1982808442414923/04.webp", "assets/fb_photos/1982808442414923/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001705,"nha-trang","ntr","Дом",15000000,100,
  "5-спальный дом, 100 м², Nam Nha Trang — 3 санузла.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1983785945650506/","сегодня",0,source="fbgroup",postedOn="2026-09-29",
  descEn="5-bedroom house, 100 m², Nam Nha Trang — 3 bathrooms.",
  details={"photos": ["assets/fb_photos/1983785945650506/01.webp", "assets/fb_photos/1983785945650506/02.webp", "assets/fb_photos/1983785945650506/03.webp", "assets/fb_photos/1983785945650506/04.webp", "assets/fb_photos/1983785945650506/05.webp"], "am": ["w", "k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
