# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 4 строки, 2026-09-12.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 563896434149922/2351777795361768 -- cebu/tis, 12,000 PHP: «TISA»: 3 строк сайта, все в tis
  * canhochothuedanangtot/2211213676172958 -- da-nang/ns, 13,000,000 VND: район назван в посте; прежний район Ngu Hanh Son весь вошёл в этот
  * chungcumini.canhodichvu.phongtrotphcm/1851095799542476 -- ho-chi-minh/tm, 5,000,000 VND: «Full Nội Thất»: 4 строк сайта, все в tm
  * chothuecanhogiarenhatrang/2053340292166739 -- nha-trang/lt, 8,500,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (63):
  * 2368220717050809 -- район не определяется по адресу «Oprra Unit 1 Kalunasan Cebu City»
  * 2372909199915294 -- уже на сайте: id 3000527
  * 2371615766711304 -- район не определяется по адресу «**2-BEDROOM TISA»
  * 2369556196917261 -- уже на сайте: id 3000528
  * 2370296823509865 -- уже на сайте: id 3000529
  * 4528691044057261 -- уже на сайте: id 3000239
  * 1808557076990144 -- уже на сайте: id 3000531
  * 2373197543219793 -- район не определяется по адресу «Baseline Residences»
  * 2370556600150554 -- район не определяется по адресу «OPEN FOR VIEWING NOW❗️❗️😍»
  * 2370267693512778 -- район не определяется по адресу «🔥 FOR RENT APARTMENT IN AS FORTUNA LAST UNIT LEFT »
  * 2372027243336823 -- район не определяется по адресу «FOR RENT Brandnew 1 Bedroom with Parking at Casa M»; прецедент расколот: «Casa Mira Towers»: lab 1
  * 4541720556087643 -- продажа
  * 4529600670632965 -- район не определяется по адресу «Saint Jude acres Subd»; прецедент расколот: «Bulacao»: tls 1, prd 1
  * 4508302629429436 -- продажа
  * 4521497431443289 -- район не определяется по адресу «Bulacao Luyo Prince Warehouse»
  * 2203496343611358 -- уже на сайте: id 3000541
  * 2214424259185233 -- район не определяется: «Apartment Details, The Ponte, Da Nang»
  * 2211064666187859 -- уже на сайте: id 3000542
  * 2207115733249419 -- уже на сайте: id 3000543
  * 2204094880218171 -- в посте несколько разных цен: 15,000,000, 23,000,000
  * 2207673073193685 -- в посте несколько разных цен: 11,000,000, 11,500,000
  * 4606474172943066 -- уже на сайте: id 3000462
  * 4606662779590872 -- район не определяется по адресу «the 2nd floor of Building C at G & B Navarro Apart»
  * 2231309210775257 -- уже на сайте: id 3000523
  * 2220626071843571 -- район не определяется по адресу «HOUSE FOR RENT - CANTIL-E»
  * 2225051174734394 -- уже на сайте: id 3000190
  * 2228726647700180 -- уже на сайте: id 3000525
  * 2223649681541210 -- уже на сайте: id 3000526
  * 2184459758793536 -- район не определяется по адресу «A Quiet refreshing Environment of Lower Cantil e(n»
  * 2222417241664454 -- тип жилья в тексте не назван
  * 4607702726153544 -- район не определяется по адресу «🔑 FURNISHED UNIT FOR RENT»
  * 4540691986187952 -- район не определяется по адресу «martisan»
  * 2227834604456051 -- район не определяется по адресу «FULLY FURNISHED HOUSE FOR RENT»
  * 2199887580584087 -- район не определяется по адресу «martisan»
  * 2205044503401728 -- район не определяется по адресу «Liptong Valencia.»
  * 1847508349901221 -- район не определяется по адресу «Nguyen Huu Canh Street»
  * 1840738980578158 -- уже на сайте: id 3000534
  * 1846023873383002 -- район не определяется по адресу «Thach Thi Thanh»; прецедент расколот: «Central»: bth 8, ak 8, th 6, kh 1, bq 1; «MODERN»: ak 5, btr 4, tm 3, th 3, kh 1
  * 1802133711105352 -- уже на сайте: id 3000535
  * 1802247057760684 -- уже на сайте: id 3000536
  * 1853708945947828 -- уже на сайте: id 3000537
  * 1801592087826181 -- уже на сайте: id 3000538
  * 1845768123408577 -- район не определяется по адресу «English below ⬇️»
  * 1855181912467198 -- район не определяется по адресу «Ton Duc Thang»; прецедент расколот: «✨ 2BR»: ak 1, btr 1; «80m²»: btr 2, th 1, tm 1, ak 1
  * 2576071049503648 -- продажа в рассрочку, а не аренда
  * 2575869156190504 -- уже на сайте: id 3000532
  * 2572896956487724 -- район не определяется по адресу «Condo Unit in Wilshire Plaza»
  * 2579759342468152 -- уже на сайте: id 3000533
  * 2390246748383632 -- район не определяется по адресу «FOR RENT - 1BR-APARMENT UNIT IN SAMPALOC MANILA.»
  * 2395927144482259 -- район не определяется по адресу «2-BEDROOM APARTMENT FOR RENT»
  * 2395247541216886 -- ищут соседа, а не сдают
  * 2571419586635461 -- район не определяется по адресу «* 21 Apo St.»; прецедент расколот: «Marcos Compound»: qzc 1; «Brgy. Pasong Tamo»: qzc 1
  * 2573848076392612 -- район не определяется по адресу «FOR LEASE»; прецедент расколот: «Valero»: mak 1
  * 2571853679925385 -- район не определяется по адресу «Looking for your own home or an extra property for»
  * 2395848701156770 -- район не определяется по адресу «Fully Furnished 1 Bedroom Condo Unit For Rent - Un»
  * 2055592715274830 -- район не определяется по адресу «Cu Chi - Nha Trang»; прецедент расколот: «Chi»: tl 1, vh 1
  * 2052488255585276 -- район не определяется по адресу «Enjoy a beautiful living space with a stunning sea»
  * 2050739092426859 -- уже на сайте: id 3000539
  * 2058946284939473 -- уже на сайте: id 3000540
  * 2060438324790269 -- район не определяется по адресу «Pham Ngoc Thach Street - Nha Trang»
  * 2031470527687049 -- район не определяется по адресу «Prime central location»
  * 2060280514806050 -- район не определяется по адресу «Cho thuê căn hộ HUD Building Nguyễn thiện thuật nh»
  * 2054398412060927 -- это поиск жилья, а не предложение
"""
from listing_lock import insert_listings

IDS = [2000614, 2000615, 2000616, 2000617]

NEW_SRC = r'''
L(2000614,"cebu","tis","Студия",12000,None,
  "Студия, TISA, Тиса.",
  "https://www.facebook.com/groups/563896434149922/posts/2351777795361768/","сегодня",0,source="fbgroup",cur="PHP",
  descEn="Studio, TISA, Тиса.",
  details={"photos": ["assets/fb_photos/2351777795361768/01.webp", "assets/fb_photos/2351777795361768/02.webp", "assets/fb_photos/2351777795361768/03.webp", "assets/fb_photos/2351777795361768/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(2000615,"da-nang","ns","Студия",13000000,None,
  "Студия, An Thuong 3 - My An - Ngu Hanh Son - Studio Balcony, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2211213676172958/","сегодня",0,source="fbgroup",
  descEn="Studio, An Thuong 3 - My An - Ngu Hanh Son - Studio Balcony, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2211213676172958/01.webp", "assets/fb_photos/2211213676172958/02.webp", "assets/fb_photos/2211213676172958/03.webp", "assets/fb_photos/2211213676172958/04.webp", "assets/fb_photos/2211213676172958/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(2000616,"ho-chi-minh","tm","Квартира",5000000,None,
  "1-спальная квартира, Full Nội Thất, Tân Mỹ.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1851095799542476/","сегодня",0,source="fbgroup",
  descEn="1-bedroom flat, Full Nội Thất, Tân Mỹ.",
  details={"photos": ["assets/fb_photos/1851095799542476/01.webp", "assets/fb_photos/1851095799542476/02.webp", "assets/fb_photos/1851095799542476/03.webp", "assets/fb_photos/1851095799542476/04.webp", "assets/fb_photos/1851095799542476/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(2000617,"nha-trang","lt","Студия",8500000,35,
  "Студия, 35 м², Lộc Thọ.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2053340292166739/","сегодня",0,source="fbgroup",
  descEn="Studio, 35 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/2053340292166739/01.webp", "assets/fb_photos/2053340292166739/02.webp", "assets/fb_photos/2053340292166739/03.webp", "assets/fb_photos/2053340292166739/04.webp", "assets/fb_photos/2053340292166739/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
