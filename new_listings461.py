# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 14 строк, 2026-10-12.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 211616406116962/2069351513676766 -- da-lat/xh, 2,800,000 VND: район назван в адресе поста; улица Lương Thế Vinh: 4 из 4 отрезков в xh
  * 476056366996433/1661791371756254 -- da-nang/lc, 25,000,000 VND: улица Nguyễn Chánh: 13 из 18 отрезков в lc
  * 728946289449167/1412255507784905 -- da-nang/hx, 9,500,000 VND: район назван в посте
  * 728946289449167/1412121027798353 -- da-nang/st, 13,000,000 VND: улица Trần Duy Chiến: 2 из 2 отрезков в st; пост: Son Tra
  * 728946289449167/1411580267852429 -- da-nang/hx, 6,000,000 VND: район назван в посте
  * 728946289449167/1411656687844787 -- da-nang/ns, 13,000,000 VND: район назван в посте; улица Khuê Mỹ Đông 7: 2 из 2 отрезков в ns
  * 2244023172420260/3829227160566512 -- ha-noi/dd, 32,000,000 VND: район назван в адресе поста
  * CHOTHUE.NHATRO.NHARIENG.HAIPHONG/29006310478980348 -- hai-phong/hbg, 45,000,000 VND: район назван в адресе поста
  * CHOTHUE.NHATRO.NHARIENG.HAIPHONG/28514993158112085 -- hai-phong/lch, 6,500,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1857337518918304 -- ho-chi-minh/ak, 13,000,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1801592087826181 -- ho-chi-minh/ak, 17,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1977095910033497 -- ho-chi-minh/ak, 19,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1990298222046599 -- ho-chi-minh/ak, 28,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1975807876828967 -- ho-chi-minh/ak, 50,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (77):
  * 2378291642990251 -- в посте несколько разных цен: 700,000, 15,000,000
  * 2386526018833480 -- район не определяется по адресу «Pham Hong Thai Street»
  * 2384843945668354 -- в посте несколько разных цен: 4,900,000, 5,400,000
  * 2384306445722104 -- район не определяется по адресу «LUXURY GARDEN VILLA FOR RENT»
  * 2159490707996179 -- это поиск жилья, а не предложение
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 2134554663823117 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»; прецедент расколот: «Triệu Việt Vương»: xh 1
  * 2125924031352847 -- это поиск жилья, а не предложение
  * 2076569656288285 -- тот же текст уже заведён: id 3001872
  * 1664297761505615 -- район не определяется: «HOUSE FOR RENT, PHAM VAN DONG, SON TRA»
  * 1628212845114107 -- похоже на уже заведённое: id 3001720
  * 1659646015304123 -- в тексте есть и другая цена того же порядка: 20,000,000 против 17,000,000
  * 1666707517931306 -- район не определяется: «CẦN CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ TẠI PHAN TỨ, ĐÀ NẴNG, PRIME LOCATION»
  * 1665003991434992 -- район не определяется: «APARTMENT FOR RENT IN THE PANOMA, MODERN AND LUXURIOUS LIVING SPACE, Map: maps.app.goo.gl/HBFupZspJxEKccnNA»
  * 1664686684800056 -- в посте несколько разных цен: 10,000,000, 12,000,000
  * 1637986504136741 -- район не определяется: «FOR RENT, 2-BEDROOM APARTMENT, MIA CENTER POINT»
  * 1666075467994511 -- район не определяется: «LUXURY SUN PONTE DUPLEX, 2BR, CITY VIEW»
  * 1666079001327491 -- район не определяется: «CHO THUÊ CĂN HỘ 2PN, MỸ ĐA TÂY 10, ĐÀ NẴNG»
  * 1408665141477275 -- район не определяется: «STUDIO DANG VU HY, SON TRA 🏡, Dang Vu Hy»
  * 1411679851175804 -- в посте несколько разных цен: 500,000, 1,000,000, 7,000,000
  * 1410519097958546 -- район не определяется: «Separate bedroom, spacious living room, 🌊 APARTMENT FOR RENT»
  * 1370508071959649 -- район не определяется: «1-BEDROOM APARTMENT, HAI CHAU DISTRICT ✨, Le Thanh Nghi Street»
  * 1410333301310459 -- в посте несколько разных цен: 500,000, 1,000,000, 7,000,000
  * 1409594331384356 -- район не определяется: «Dien Bien Phu Street (inside the Co.opmart Supermarket complex)., Property Highlights:, 🏢 LUXURY 1BR PENTHOUSE FOR RENT»
  * 3831769426978952 -- район не определяется по адресу «FULLY FURNISHED HOUSE FOR RENT»
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
  * 28441247912153277 -- район не определяется по адресу «T2862 Cho thuê nhà Trung Lực ( Gần Văn Cao - Lê Hồ»
  * 29153180070960054 -- район не определяется по адресу «T2780 Cho thuê nhà mặt đường Văn Cao»
  * 29090459853898743 -- район не определяется по адресу «T2923 - Cho Thuê Biệt Thự Vinhomes Marina»
  * 29153134900964571 -- район не определяется по адресу «T1698 Cho thuê căn góc xẻ khe hoàng huy mall - Aeo»
  * 28959217347022995 -- район не определяется по адресу «🇻🇳 │ VINHOMES MARINA»
  * 28660128650265201 -- район не определяется по адресу «the fourth floor»
  * 1879291176722938 -- в посте несколько разных цен: 5,200,000, 5,500,000, 5,700,000, 6,000,000, 6,700,000, 7,000,000
  * 1853134039338652 -- район не определяется по адресу «English below ⬇️»
  * 1874570790528310 -- в посте несколько разных цен: 5,000,000, 20,000,000
  * 1876575393661183 -- тип жилья в тексте не назван
  * 1882187833099939 -- район не определяется по адресу «KO NGẬP LỤT»
  * 1882312279754161 -- в посте несколько разных цен: 12,000,000, 15,000,000, 16,000,000, 18,000,000, 21,000,000
  * 1990213192055102 -- район не определяется по адресу «NGUYEN VAN THUONG»
  * 1965348697874885 -- район не определяется по адресу «Nguyễn Bỉnh Khiêm»; прецедент расколот: «🔥 HOT DEAL»: ak 1
  * 1976252013451220 -- район не определяется по адресу «102 Phan Huy Ích»
  * 1989145782161843 -- район не определяется по адресу «Nguyen Cuu Van Street»
  * 1987669072309514 -- в посте несколько разных цен: 12,500,000, 14,000,000, 15,500,000, 26,000,000
  * 1983180809425007 -- тип жилья в тексте не назван
  * 1975221100220978 -- район не определяется по адресу «Tran Quoc Thao Street»; прецедент расколот: «🔥 HOT DEAL»: ak 1
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
  * 5574690879422216 -- район не определяется по адресу «⭐️ Cho Thuê Căn Hộ ALTARA RESIDENCE»
  * 5573872579504046 -- район не определяется по адресу «Cho Thuê Căn Hộ ALTARA RESIDENCE»
  * 5569137533310884 -- тип жилья в тексте не назван
  * 3300621106815649 -- район не определяется по адресу «🔥🔥🔥Cho Thuê Căn Hộ ALTARA RESIDENCE»
  * 3278586459019114 -- район не определяется по адресу «Studio»
  * 3277316822479411 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 3282055582005535 -- район не определяется по адресу «KĐT An Phú Thịnh»
  * 3280507732160320 -- район не определяется по адресу «Ngay Đại học FPT»
  * 3273225212888572 -- район не определяется по адресу «Khu đô thị An Phú Thịnh»
"""
from listing_lock import insert_listings

IDS = [3002131, 3002132, 3002133, 3002134, 3002135, 3002136, 3002137, 3002138, 3002139, 3002140, 3002141, 3002142, 3002143, 3002144]

NEW_SRC = r'''
L(3002131,"da-lat","xh","Комната",2800000,None,
  "Комната, Lương Thế Vinh, Xuân Hương - Đà Lạt.",
  "https://www.facebook.com/groups/211616406116962/posts/2069351513676766/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="Room, Lương Thế Vinh, Xuân Hương - Đà Lạt.",
  details={"photos": ["assets/fb_photos/2069351513676766/01.webp", "assets/fb_photos/2069351513676766/02.webp", "assets/fb_photos/2069351513676766/03.webp", "assets/fb_photos/2069351513676766/04.webp", "assets/fb_photos/2069351513676766/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3002132,"da-nang","lc","Дом",25000000,None,
  "3-спальный дом, Nguyễn Chánh, Liên Chiểu — 4 санузла.",
  "https://www.facebook.com/groups/476056366996433/posts/1661791371756254/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="3-bedroom house, Nguyễn Chánh, Liên Chiểu — 4 bathrooms.",
  details={"photos": ["assets/fb_photos/1661791371756254/01.webp", "assets/fb_photos/1661791371756254/02.webp", "assets/fb_photos/1661791371756254/03.webp", "assets/fb_photos/1661791371756254/04.webp", "assets/fb_photos/1661791371756254/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3002133,"da-nang","hx","Квартира",9500000,None,
  "1-спальная квартира, ✨ 1-BEDROOM APARTMENT, Hòa Xuân.",
  "https://www.facebook.com/groups/728946289449167/posts/1412255507784905/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="1-bedroom flat, ✨ 1-BEDROOM APARTMENT, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1412255507784905/01.webp", "assets/fb_photos/1412255507784905/02.webp", "assets/fb_photos/1412255507784905/03.webp", "assets/fb_photos/1412255507784905/04.webp", "assets/fb_photos/1412255507784905/05.webp"], "am": ["b", "win"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002134,"da-nang","st","Студия",13000000,None,
  "Студия, Trần Duy Chiến, Sơn Trà.",
  "https://www.facebook.com/groups/728946289449167/posts/1412121027798353/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="Studio, Trần Duy Chiến, Sơn Trà.",
  details={"photos": ["assets/fb_photos/1412121027798353/01.webp", "assets/fb_photos/1412121027798353/02.webp", "assets/fb_photos/1412121027798353/03.webp", "assets/fb_photos/1412121027798353/04.webp", "assets/fb_photos/1412121027798353/05.webp"], "am": ["w", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3002135,"da-nang","hx","Квартира",6000000,None,
  "Квартира, ✨ 1 PHÒNG NGỦ FULL NỘI THẤT, Hòa Xuân.",
  "https://www.facebook.com/groups/728946289449167/posts/1411580267852429/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="Flat, ✨ 1 PHÒNG NGỦ FULL NỘI THẤT, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1411580267852429/01.webp", "assets/fb_photos/1411580267852429/02.webp", "assets/fb_photos/1411580267852429/03.webp", "assets/fb_photos/1411580267852429/04.webp", "assets/fb_photos/1411580267852429/05.webp"], "am": ["w", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002136,"da-nang","ns","Квартира",13000000,40,
  "1-спальная квартира, 40 м², Khuê Mỹ Đông 7, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/728946289449167/posts/1411656687844787/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="1-bedroom flat, 40 m², Khuê Mỹ Đông 7, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1411656687844787/01.webp", "assets/fb_photos/1411656687844787/02.webp", "assets/fb_photos/1411656687844787/03.webp", "assets/fb_photos/1411656687844787/04.webp", "assets/fb_photos/1411656687844787/05.webp"], "am": ["pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3002137,"ha-noi","dd","Квартира",32000000,170,
  "3-спальная квартира, 170 м², Đống Đa — 2 санузла.",
  "https://www.facebook.com/groups/2244023172420260/posts/3829227160566512/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="3-bedroom flat, 170 m², Đống Đa — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/3829227160566512/01.webp", "assets/fb_photos/3829227160566512/02.webp", "assets/fb_photos/3829227160566512/03.webp", "assets/fb_photos/3829227160566512/04.webp", "assets/fb_photos/3829227160566512/05.webp"], "am": ["w", "k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002138,"hai-phong","hbg","Дом",45000000,144,
  "Дом, 144 м², Hồng Bàng — 5 санузлов.",
  "https://www.facebook.com/groups/CHOTHUE.NHATRO.NHARIENG.HAIPHONG/posts/29006310478980348/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="House, 144 m², Hồng Bàng — 5 bathrooms.",
  details={"photos": ["assets/fb_photos/29006310478980348/01.webp", "assets/fb_photos/29006310478980348/02.webp", "assets/fb_photos/29006310478980348/03.webp", "assets/fb_photos/29006310478980348/04.webp", "assets/fb_photos/29006310478980348/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002139,"hai-phong","lch","Дом",6500000,65,
  "Дом, 65 м², Lê Chân.",
  "https://www.facebook.com/groups/CHOTHUE.NHATRO.NHARIENG.HAIPHONG/posts/28514993158112085/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="House, 65 m², Lê Chân.",
  details={"photos": ["assets/fb_photos/28514993158112085/01.webp", "assets/fb_photos/28514993158112085/02.webp", "assets/fb_photos/28514993158112085/03.webp", "assets/fb_photos/28514993158112085/04.webp", "assets/fb_photos/28514993158112085/05.webp"], "am": ["w", "k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002140,"ho-chi-minh","ak","Студия",13000000,45,
  "Студия, 45 м², An Khánh.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1857337518918304/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="Studio, 45 m², An Khánh.",
  details={"photos": ["assets/fb_photos/1857337518918304/01.webp", "assets/fb_photos/1857337518918304/02.webp", "assets/fb_photos/1857337518918304/03.webp", "assets/fb_photos/1857337518918304/04.webp", "assets/fb_photos/1857337518918304/05.webp"], "am": ["pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002141,"ho-chi-minh","ak","Квартира",17000000,50,
  "1-спальная квартира, 50 м², An Khánh — 1 санузел.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1801592087826181/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="1-bedroom flat, 50 m², An Khánh — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1801592087826181/01.webp", "assets/fb_photos/1801592087826181/02.webp", "assets/fb_photos/1801592087826181/03.webp", "assets/fb_photos/1801592087826181/04.webp", "assets/fb_photos/1801592087826181/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002142,"ho-chi-minh","ak","Квартира",19000000,None,
  "1-спальная квартира, An Khánh.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1977095910033497/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="1-bedroom flat, An Khánh.",
  details={"photos": ["assets/fb_photos/1977095910033497/01.webp", "assets/fb_photos/1977095910033497/02.webp", "assets/fb_photos/1977095910033497/03.webp", "assets/fb_photos/1977095910033497/04.webp", "assets/fb_photos/1977095910033497/05.webp"], "flHigh": 1, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002143,"ho-chi-minh","ak","Квартира",28000000,55,
  "1-спальная квартира, 55 м², An Khánh — 1 санузел.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1990298222046599/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="1-bedroom flat, 55 m², An Khánh — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1990298222046599/01.webp", "assets/fb_photos/1990298222046599/02.webp", "assets/fb_photos/1990298222046599/03.webp", "assets/fb_photos/1990298222046599/04.webp", "assets/fb_photos/1990298222046599/05.webp"], "am": ["pool", "gym"], "fl": 8, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002144,"ho-chi-minh","ak","Квартира",50000000,145,
  "2-спальная квартира, 145 м², An Khánh — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1975807876828967/","сегодня",0,source="fbgroup",postedOn="2026-10-12",
  descEn="2-bedroom flat, 145 m², An Khánh — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1975807876828967/01.webp", "assets/fb_photos/1975807876828967/02.webp", "assets/fb_photos/1975807876828967/03.webp", "assets/fb_photos/1975807876828967/04.webp", "assets/fb_photos/1975807876828967/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
