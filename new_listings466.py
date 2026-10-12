# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 13 строк, 2026-10-12.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 994303254903669/1847166082950711 -- cebu/lah, 10,000 PHP: район назван в адресе поста
  * 652674525365824/2129515557681706 -- cebu/mab, 12,000 PHP: район назван в адресе поста
  * 476056366996433/1628212845114107 -- da-nang/ns, 22,000,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * 203559903815711/2376577839847229 -- da-nang/ns, 9,500,000 VND: район назван в посте
  * 203559903815711/2376837889821224 -- da-nang/hcg, 10,500,000 VND: улица Phan Thành Tài: 5 из 5 отрезков в hcg; пост: Hai Chau
  * canhochungcudanang/2996288740765203 -- da-nang/ns, 16,500,000 VND: прежний район Ngu Hanh Son весь вошёл в этот; улица Mỹ Đa Tây 9: 2 из 2 отрезков в ns; пост: Ngu Hanh Son
  * khachsanvillahomestaynhatrang/1131806955959859 -- nha-trang/ph, 12,000,000 VND: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1129954529478435 -- nha-trang/pl, 12,500,000 VND: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1131337062673515 -- nha-trang/ntr, 9,500,000 VND: район назван в адресе поста
  * chothuecanhogiarenhatrang/2088427291991372 -- nha-trang/ttr, 16,500,000 VND: район назван в адресе поста
  * chothuecanhogiarenhatrang/2088476468653121 -- nha-trang/lt, 17,000,000 VND: район назван в адресе поста
  * chothue79/4641042536165267 -- nha-trang/btr, 10,500,000 VND: район назван в адресе поста
  * 833750970492261/2367700887097254 -- phu-quoc/ddg, 30,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (167):
  * 2671323069986069 -- район не определяется по адресу «one of Buôn Ma Thuột's most secure and pristine ur»
  * 2168691324070411 -- район не определяется по адресу «one of Buôn Ma Thuột's most secure and pristine ur»
  * 2185082292431314 -- нет ни одной скачанной фотографии
  * 4535108773471481 -- район не определяется по адресу «Chủ gửi»
  * 4534963593485999 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 4524078787907813 -- район не определяется по адресу «GIÁ THUÊ : 2.7 TRIỆU»
  * 4523929227922769 -- район не определяется по адресу «Chủ gửi - GIÁ THUÊ : 2.7 TRIỆU»
  * 4583088438673514 -- район не определяется по адресу «CĂN HỘ CAO CẤP KDC THỚI NHỰT FULL NỘI THẤT GẦN ĐH »
  * 4578192675829757 -- район не определяется по адресу «🥨🫜🍒 CĂN HỘ CAO CẤP MỚI XÂY KDC AN KHÁNH FULL NỘI T»
  * 4576672325981792 -- район не определяется по адресу «🛍️🎀 PHÒNG FULL NỘI THẤT CÓ BAN CÔNG ĐƯỜNG HOÀNG QU»; прецедент расколот: «ĐHYD»: tanc 1
  * 4585402665108758 -- тип жилья в тексте не назван
  * 2145727852997245 -- район не определяется по адресу «Chủ gửi»
  * 2145579633012067 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 2136097713960259 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NGUYỄN VĂN LI»
  * 2178278159742214 -- район не определяется по адресу «☸️🏚️📫MINIHOUSE CAO CẤP FULL NỘI THẤT - RỘNG 40M2 M»
  * 2200583187511711 -- район не определяется по адресу «Căn hộ có phòng ngủ»
  * 2174816730088357 -- тип жилья в тексте не назван
  * 2129210777982286 -- район не определяется по адресу «CHO THUÊ CĂN HỘ TRUNG TÂM CẦN THƠ»
  * 1844291109904875 -- район не определяется по адресу «Bldg 7»
  * 1848636742803645 -- адрес называет несколько районов: bnl, man
  * 1847115122955807 -- район не определяется по адресу «For rent: 20K»
  * 1846159399718046 -- район не определяется по адресу «For rent❗️👍»
  * 1841760790157907 -- район не определяется по адресу «APARTMENT FOR RENT‼️»
  * 1841846580149328 -- в тексте есть и другая цена того же порядка: 33,111 против 60,000
  * 2146901265943135 -- район не определяется по адресу «TISA Labangon»
  * 2144283599538235 -- район не определяется по адресу «Mc Arthur Blvd»
  * 2113780859255176 -- рассрочка
  * 2146731842626744 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2116301972336398 -- в тексте есть и другая цена того же порядка: 7,833 против 18,000
  * 2096872770945985 -- в посте несколько разных цен: 1,500, 13,000
  * 2115687289064533 -- район не определяется по адресу «Ready for viewing na❗»
  * 2144359749530620 -- район не определяется по адресу «P. Rodriguez St»
  * 2378291642990251 -- в посте несколько разных цен: 700,000, 15,000,000
  * 2386526018833480 -- район не определяется по адресу «Pham Hong Thai Street»
  * 2384843945668354 -- в посте несколько разных цен: 4,900,000, 5,400,000
  * 2384306445722104 -- район не определяется по адресу «LUXURY GARDEN VILLA FOR RENT»
  * 2159490707996179 -- это поиск жилья, а не предложение
  * 2069351513676766 -- тот же текст уже заведён: id 3002131
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2116570508954866 -- нет ни одной скачанной фотографии
  * 2134554663823117 -- нет ни одной скачанной фотографии
  * 2125924031352847 -- это поиск жилья, а не предложение
  * 2076569656288285 -- тот же текст уже заведён: id 3001872
  * 1664297761505615 -- район не определяется: «HOUSE FOR RENT, PHAM VAN DONG, SON TRA»
  * 1661791371756254 -- тот же текст уже заведён: id 3002132
  * 1659646015304123 -- в тексте есть и другая цена того же порядка: 20,000,000 против 17,000,000
  * 1666707517931306 -- район не определяется: «CẦN CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ TẠI PHAN TỨ, ĐÀ NẴNG, PRIME LOCATION»
  * 1665003991434992 -- район не определяется: «APARTMENT FOR RENT IN THE PANOMA, MODERN AND LUXURIOUS LIVING SPACE, Map: maps.app.goo.gl/HBFupZspJxEKccnNA»
  * 1664686684800056 -- в посте несколько разных цен: 10,000,000, 12,000,000
  * 1637986504136741 -- район не определяется: «FOR RENT, 2-BEDROOM APARTMENT, MIA CENTER POINT»
  * 1666075467994511 -- район не определяется: «LUXURY SUN PONTE DUPLEX, 2BR, CITY VIEW»
  * 1666079001327491 -- район не определяется: «CHO THUÊ CĂN HỘ 2PN, MỸ ĐA TÂY 10, ĐÀ NẴNG»
  * 1412255507784905 -- тот же текст уже заведён: id 3002133
  * 1412121027798353 -- тот же текст уже заведён: id 3002134
  * 1411580267852429 -- тот же текст уже заведён: id 3002135
  * 1408665141477275 -- район не определяется: «STUDIO DANG VU HY, SON TRA 🏡, Dang Vu Hy»
  * 1411679851175804 -- в посте несколько разных цен: 500,000, 1,000,000, 7,000,000
  * 1410519097958546 -- район не определяется: «Separate bedroom, spacious living room, 🌊 APARTMENT FOR RENT»
  * 1370508071959649 -- район не определяется: «1-BEDROOM APARTMENT, HAI CHAU DISTRICT ✨, Le Thanh Nghi Street»
  * 1410333301310459 -- в посте несколько разных цен: 500,000, 1,000,000, 7,000,000
  * 1411656687844787 -- тот же текст уже заведён: id 3002136
  * 1409594331384356 -- район не определяется: «Dien Bien Phu Street (inside the Co.opmart Supermarket complex)., Property Highlights:, 🏢 LUXURY 1BR PENTHOUSE FOR RENT»
  * 2373490586822621 -- район не определяется: «💐 House for rent at K249/59 on Ha Huy Tap Street»
  * 2377178749787138 -- район не определяется: «HOUSE FOR RENT, HAI CHAU, DA NANG»
  * 2380358606135819 -- в посте несколько разных цен: 12,500,000, 13,500,000
  * 2373459913492355 -- район не определяется: «Da Nang beach area, approx. 100m from the beach, 3-BEDROOM HOUSE FOR RENT»
  * 2372487700256243 -- район не определяется: «3-BEDROOM HOUSE FOR RENT NEAR TAN THANH, CAM HOI BEACH, HOI AN»
  * 2375989359906077 -- район не определяется: «Prime location in the city center, 3 bedrooms, 2 bathrooms»
  * 2376514049853608 -- район не определяется: «Blooming Tower, Da Nang, Blooming Tower listing / 3 bedroom for rent»
  * 2384324425739237 -- тип жилья в тексте не назван
  * 2996352904092120 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT, MAI THUC LAN, Mai Thuc Lan Street»
  * 2996230964104314 -- тот же текст уже заведён: id 3002133
  * 1583014733578036 -- район не определяется: «HOUSE FOR RENT, HAI CHAU, DA NANG»
  * 1578900223989487 -- в посте несколько разных цен: 15,000,000, 20,000,000
  * 1583463256866517 -- это поиск жилья, а не предложение
  * 1589847419561434 -- в посте несколько разных цен: 6,000,000, 8,000,000
  * 3831769426978952 -- район не определяется по адресу «FULLY FURNISHED HOUSE FOR RENT»
  * 3829227160566512 -- тот же текст уже заведён: id 3002137
  * 3836096546546240 -- тип жилья в тексте не назван
  * 3839766172845944 -- тип жилья в тексте не назван
  * 3834265520062676 -- тип жилья в тексте не назван
  * 3837161476439747 -- тип жилья в тексте не назван
  * 3839770359512192 -- тип жилья в тексте не назван
  * 3833174136838481 -- помещение под бизнес или здание целиком, а не жильё
  * 3835597253262836 -- помещение под бизнес или здание целиком, а не жильё
  * 3821479454674616 -- помещение под бизнес или здание целиком, а не жильё
  * 1798998168114264 -- тип жилья в тексте не назван
  * 1839186734095407 -- тип жилья в тексте не назван
  * 1818287229518691 -- тип жилья в тексте не назван
  * 3885449368262838 -- тип жилья в тексте не назван
  * 29006310478980348 -- тот же текст уже заведён: id 3002138
  * 28441247912153277 -- нет ни одной скачанной фотографии
  * 29153180070960054 -- район не определяется по адресу «T2780 Cho thuê nhà mặt đường Văn Cao»
  * 29090459853898743 -- район не определяется по адресу «T2923 - Cho Thuê Biệt Thự Vinhomes Marina»
  * 29153134900964571 -- район не определяется по адресу «T1698 Cho thuê căn góc xẻ khe hoàng huy mall - Aeo»
  * 28959217347022995 -- район не определяется по адресу «🇻🇳 │ VINHOMES MARINA»
  * 28514993158112085 -- тот же текст уже заведён: id 3002139
  * 28660128650265201 -- район не определяется по адресу «the fourth floor»
  * 1879291176722938 -- в посте несколько разных цен: 5,200,000, 5,500,000, 5,700,000, 6,000,000, 6,700,000, 7,000,000
  * 1853134039338652 -- район не определяется по адресу «English below ⬇️»
  * 1874570790528310 -- в посте несколько разных цен: 5,000,000, 20,000,000
  * 1876575393661183 -- тип жилья в тексте не назван
  * 1857337518918304 -- тот же текст уже заведён: id 3002140
  * 1882187833099939 -- район не определяется по адресу «KO NGẬP LỤT»
  * 1882312279754161 -- в посте несколько разных цен: 12,000,000, 15,000,000, 16,000,000, 18,000,000, 21,000,000
  * 1801592087826181 -- тот же текст уже заведён: id 3002141
  * 1977095910033497 -- тот же текст уже заведён: id 3002142
  * 1990213192055102 -- район не определяется по адресу «NGUYEN VAN THUONG»
  * 1965348697874885 -- нет ни одной скачанной фотографии
  * 1990298222046599 -- тот же текст уже заведён: id 3002143
  * 1976252013451220 -- нет ни одной скачанной фотографии
  * 1989145782161843 -- район не определяется по адресу «Nguyen Cuu Van Street»
  * 1987669072309514 -- в посте несколько разных цен: 12,500,000, 14,000,000, 15,500,000, 26,000,000
  * 1983180809425007 -- тип жилья в тексте не назван
  * 1975807876828967 -- тот же текст уже заведён: id 3002144
  * 1975221100220978 -- район не определяется по адресу «Tran Quoc Thao Street»
  * 1287853898988310 -- в тексте есть и другая цена того же порядка: 4,568,736 против 4,000,000
  * 1457057169289688 -- район не определяется по адресу «Vị trí thuận tiện»
  * 1407858374209568 -- район не определяется по адресу «Vị trí trung tâm»; прецедент расколот: «The Manor»: vyd 1
  * 1467684398226965 -- похоже на уже заведённое: id 3001985
  * 1507435977585140 -- в посте несколько разных цен: 500,000, 600,000
  * 1506528094342595 -- тип жилья в тексте не назван
  * 28983258057976292 -- тип жилья в тексте не назван
  * 28982722708029827 -- район не определяется по адресу «Lot 2»
  * 28953046350997463 -- в тексте есть и другая цена того же порядка: 7,796 против 20,500
  * 28970083059293792 -- в тексте есть и другая цена того же порядка: 5,510 против 15,000
  * 28899773106324788 -- район не определяется по адресу «2BR APARTMENT FOR RENT 🏠»
  * 28911494098486022 -- район не определяется по адресу «1022 Solis Street»
  * 2426403604767946 -- район не определяется по адресу «Pacific Skyloft»
  * 2407388686669438 -- цена 2,350 PHP вне разумных пределов
  * 2390246748383632 -- район не определяется по адресу «FOR RENT - 1BR-APARMENT UNIT IN SAMPALOC MANILA.»
  * 2419370192137954 -- район не определяется по адресу «000/Month pdc required»
  * 2422350878506552 -- в посте несколько разных цен: 33,000, 35,000
  * 1131392772667944 -- район не определяется по адресу «fully furnished with a private washing machine»
  * 1130887592718462 -- район не определяется по адресу «FOR RENT»
  * 1130797719394116 -- район не определяется по адресу «City center»
  * 1131815232625698 -- похоже на уже заведённое: id 1021734
  * 1131344162672805 -- район не определяется по адресу «South Nha Trang»
  * 2087066102127491 -- в посте несколько разных цен: 500,000, 11,500,000
  * 2088750848625683 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2087031058797662 -- в посте несколько разных цен: 500,000, 11,500,000
  * 2077475579753210 -- район не определяется по адресу «An Bình Tân»
  * 2087513952082706 -- похоже на уже заведённое: id 1020205
  * 2088888421945259 -- помещение под бизнес или здание целиком, а не жильё
  * 4625802281022626 -- район не определяется по адресу «Tran Quy Cap Street»
  * 4642245916044929 -- похоже на уже заведённое: id new:chothuecanhogiarenhatrang/2088427291991372
  * 4626748320928022 -- похоже на уже заведённое: id 3002031
  * 2359140247953318 -- тип жилья в тексте не назван
  * 2380371035830239 -- район не определяется по адресу «CHO THUÊ VILLA 3 PHÒNG NGỦ»
  * 2373450553188954 -- район не определяется по адресу «CHO THUÊ CĂN HỘ THEO THÁNG»
  * 2297494690784541 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2369506903583319 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2616359608784694 -- тип жилья в тексте не назван
  * 2615310538889601 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2604061680014487 -- район не определяется по адресу «CHO THUÊ CĂN HỘ THEO THÁNG»
  * 2588243598262962 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2612174042536584 -- район не определяется по адресу «Meyhomes Phu Quoc»
  * 2599789720441683 -- тот же текст уже заведён: id new:833750970492261/2367700887097254
  * 5574690879422216 -- район не определяется по адресу «⭐️ Cho Thuê Căn Hộ ALTARA RESIDENCE»; прецедент расколот: «TRẦN HƯNG ĐẠO 🌆🌆🌆»: qn 1
  * 5573872579504046 -- район не определяется по адресу «Cho Thuê Căn Hộ ALTARA RESIDENCE»; прецедент расколот: «TRẦN HƯNG ĐẠO»: qn 1
  * 5569137533310884 -- тип жилья в тексте не назван
  * 3300621106815649 -- нет ни одной скачанной фотографии
  * 3278586459019114 -- нет ни одной скачанной фотографии
  * 3277316822479411 -- нет ни одной скачанной фотографии
  * 3282055582005535 -- нет ни одной скачанной фотографии
  * 3280507732160320 -- нет ни одной скачанной фотографии
  * 3273225212888572 -- район не определяется по адресу «Khu đô thị An Phú Thịnh»
"""
from listing_lock import insert_listings

IDS = [3002153, 3002154, 3002155, 3002156, 3002157, 3002158, 3002159, 3002160, 3002161, 3002162, 3002163, 3002164, 3002165]

NEW_SRC = r'''
L(3002153,"cebu","lah","Квартира",10000,15,
  "Квартира, 15 м², Lahug.",
  "https://www.facebook.com/groups/994303254903669/posts/1847166082950711/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-12",
  descEn="Flat, 15 m², Lahug.",
  details={"photos": ["assets/fb_photos/1847166082950711/01.webp", "assets/fb_photos/1847166082950711/02.webp", "assets/fb_photos/1847166082950711/03.webp", "assets/fb_photos/1847166082950711/04.webp", "assets/fb_photos/1847166082950711/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002154,"cebu","mab","Квартира",12000,32,
  "1-спальная квартира, 32 м², Mabolo.",
  "https://www.facebook.com/groups/652674525365824/posts/2129515557681706/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-12",
  descEn="1-bedroom flat, 32 m², Mabolo.",
  details={"photos": ["assets/fb_photos/2129515557681706/01.webp", "assets/fb_photos/2129515557681706/02.webp", "assets/fb_photos/2129515557681706/03.webp", "assets/fb_photos/2129515557681706/04.webp", "assets/fb_photos/2129515557681706/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002155,"da-nang","ns","Дом",22000000,100,
  "3-спальный дом, 100 м², - House for rent, Ngũ Hành Sơn — 3 санузла.",
  "https://www.facebook.com/groups/476056366996433/posts/1628212845114107/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="3-bedroom house, 100 m², - House for rent, Ngũ Hành Sơn — 3 bathrooms.",
  details={"photos": ["assets/fb_photos/1628212845114107/01.webp", "assets/fb_photos/1628212845114107/02.webp", "assets/fb_photos/1628212845114107/03.webp", "assets/fb_photos/1628212845114107/04.webp", "assets/fb_photos/1628212845114107/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002156,"da-nang","ns","Квартира",9500000,None,
  "1-спальная квартира, BEDROOM APARTMENT FOR RENT IN MY AN, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/203559903815711/posts/2376577839847229/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="1-bedroom flat, BEDROOM APARTMENT FOR RENT IN MY AN, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2376577839847229/01.webp", "assets/fb_photos/2376577839847229/02.webp", "assets/fb_photos/2376577839847229/03.webp", "assets/fb_photos/2376577839847229/04.webp", "assets/fb_photos/2376577839847229/05.webp"], "am": ["w", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002157,"da-nang","hcg","Студия",10500000,None,
  "Студия, Phan Thành Tài, Hòa Cường.",
  "https://www.facebook.com/groups/203559903815711/posts/2376837889821224/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="Studio, Phan Thành Tài, Hòa Cường.",
  details={"photos": ["assets/fb_photos/2376837889821224/01.webp", "assets/fb_photos/2376837889821224/02.webp", "assets/fb_photos/2376837889821224/03.webp", "assets/fb_photos/2376837889821224/04.webp", "assets/fb_photos/2376837889821224/05.webp"], "am": ["w"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3002158,"da-nang","ns","Квартира",16500000,None,
  "Квартира, Mỹ Đa Tây 9, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2996288740765203/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="Flat, Mỹ Đa Tây 9, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2996288740765203/01.webp", "assets/fb_photos/2996288740765203/02.webp", "assets/fb_photos/2996288740765203/03.webp", "assets/fb_photos/2996288740765203/04.webp", "assets/fb_photos/2996288740765203/05.webp"], "am": ["w", "k", "b"], "fl": 5, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3002159,"nha-trang","ph","Квартира",12000000,55,
  "2-спальная квартира, 55 м², Phước Hải.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1131806955959859/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="2-bedroom flat, 55 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/1131806955959859/01.webp", "assets/fb_photos/1131806955959859/02.webp", "assets/fb_photos/1131806955959859/03.webp", "assets/fb_photos/1131806955959859/04.webp", "assets/fb_photos/1131806955959859/05.webp"], "am": ["w", "b", "win"], "fl": 2, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002160,"nha-trang","pl","Квартира",12500000,30,
  "Квартира, 30 м², Phước Long.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1129954529478435/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="Flat, 30 m², Phước Long.",
  details={"photos": ["assets/fb_photos/1129954529478435/01.webp", "assets/fb_photos/1129954529478435/02.webp", "assets/fb_photos/1129954529478435/03.webp", "assets/fb_photos/1129954529478435/04.webp", "assets/fb_photos/1129954529478435/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002161,"nha-trang","ntr","Квартира",9500000,28,
  "Квартира, 28 м², Nam Nha Trang — 1 санузел.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1131337062673515/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="Flat, 28 m², Nam Nha Trang — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1131337062673515/01.webp", "assets/fb_photos/1131337062673515/02.webp", "assets/fb_photos/1131337062673515/03.webp", "assets/fb_photos/1131337062673515/04.webp", "assets/fb_photos/1131337062673515/05.webp"], "am": ["w", "k", "b"], "fl": 2, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002162,"nha-trang","ttr","Квартира",16500000,60,
  "2-спальная квартира, 60 м², Tây Nha Trang.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2088427291991372/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="2-bedroom flat, 60 m², Tây Nha Trang.",
  details={"photos": ["assets/fb_photos/2088427291991372/01.webp", "assets/fb_photos/2088427291991372/02.webp", "assets/fb_photos/2088427291991372/03.webp", "assets/fb_photos/2088427291991372/04.webp"], "am": ["w"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002163,"nha-trang","lt","Квартира",17000000,None,
  "1-спальная квартира, Lộc Thọ.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2088476468653121/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="1-bedroom flat, Lộc Thọ.",
  details={"photos": ["assets/fb_photos/2088476468653121/01.webp", "assets/fb_photos/2088476468653121/02.webp", "assets/fb_photos/2088476468653121/03.webp", "assets/fb_photos/2088476468653121/04.webp", "assets/fb_photos/2088476468653121/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002164,"nha-trang","btr","Квартира",10500000,None,
  "2-спальная квартира, Bắc Nha Trang — 2 санузла.",
  "https://www.facebook.com/groups/chothue79/posts/4641042536165267/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="2-bedroom flat, Bắc Nha Trang — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/4641042536165267/01.webp", "assets/fb_photos/4641042536165267/02.webp", "assets/fb_photos/4641042536165267/03.webp", "assets/fb_photos/4641042536165267/04.webp", "assets/fb_photos/4641042536165267/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002165,"phu-quoc","ddg","Дом",30000000,None,
  "5-спальный дом, Dương Đông.",
  "https://www.facebook.com/groups/833750970492261/posts/2367700887097254/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="5-bedroom house, Dương Đông.",
  details={"photos": ["assets/fb_photos/2367700887097254/01.webp", "assets/fb_photos/2367700887097254/02.webp", "assets/fb_photos/2367700887097254/03.webp", "assets/fb_photos/2367700887097254/04.webp", "assets/fb_photos/2367700887097254/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
