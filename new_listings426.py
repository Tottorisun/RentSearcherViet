# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 24 строки, 2026-10-07.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 993673090964916/3106336639698540 -- cebu/gua, 25,000 PHP: район назван в адресе поста
  * 993673090964916/3106366376362233 -- cebu/mab, 23,000 PHP: район назван в адресе поста
  * 993673090964916/3106122276386643 -- cebu/tlm, 18,000 PHP: район назван в адресе поста
  * 993673090964916/3105063616492509 -- cebu/man, 17,000 PHP: район назван в адресе поста
  * 3914645581932487/28849022008068166 -- cebu/gua, 18,000 PHP: район назван в адресе поста
  * 3914645581932487/28836130679357299 -- cebu/man, 15,000 PHP: район назван в адресе поста
  * 476056366996433/1656261375642587 -- da-nang/hcg, 12,000,000 VND: «Đường Hóa Sơn 4»: 2 строк сайта, все в hcg
  * 476056366996433/1655589649043093 -- da-nang/ah, 6,000,000 VND: улица Phước Trường 3: 1 из 1 отрезков в ah; пост: Son Tra
  * 728946289449167/1405859971757792 -- da-nang/hcg, 7,000,000 VND: район назван в посте
  * 728946289449167/1407479641595825 -- da-nang/hx, 6,000,000 VND: район назван в посте
  * phongtrocanhonhadanang/1497921535834163 -- da-nang/ah, 12,000,000 VND: район назван в посте
  * 153191128587086/2242577632981748 -- dumaguete/btg, 15,000 PHP: район назван в адресе поста
  * 807531664242245/1466927818302623 -- hue/acu, 15,000,000 VND: район назван в адресе поста
  * phongtrosvhue/1676192456923396 -- hue/acu, 5,000,000 VND: район назван в адресе поста
  * phongtrosvhue/1699463947929580 -- hue/vyd, 6,000,000 VND: район назван в адресе поста
  * 2253829621529798/4743707395875329 -- nha-trang/ph, 14,000,000 VND: район назван в адресе поста
  * 1172766863380743/2103628353627918 -- nha-trang/lt, 8,000,000 VND: район назван в адресе поста
  * chothue79/4635199233416264 -- nha-trang/ph, 17,000,000 VND: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1117203214086900 -- nha-trang/btr, 23,000,000 VND: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1125804183226803 -- nha-trang/pl, 25,000,000 VND: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1125809883226233 -- nha-trang/pl, 25,000,000 VND: район назван в адресе поста
  * chothuecanhogiarenhatrang/2082963112537790 -- nha-trang/btr, 15,000,000 VND: район назван в адресе поста
  * chothuecanhogiarenhatrang/2083377932496308 -- nha-trang/vp, 23,000,000 VND: район назван в адресе поста
  * 849441571863086/3857113297762550 -- nha-trang/lt, 15,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (179):
  * 4534963593485999 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 4535108773471481 -- район не определяется по адресу «Chủ gửi»
  * 4524078787907813 -- район не определяется по адресу «GIÁ THUÊ : 2.7 TRIỆU»
  * 4523929227922769 -- район не определяется по адресу «Chủ gửi - GIÁ THUÊ : 2.7 TRIỆU»
  * 4583088438673514 -- район не определяется по адресу «CĂN HỘ CAO CẤP KDC THỚI NHỰT FULL NỘI THẤT GẦN ĐH »
  * 4578192675829757 -- район не определяется по адресу «🥨🫜🍒 CĂN HỘ CAO CẤP MỚI XÂY KDC AN KHÁNH FULL NỘI T»
  * 4576672325981792 -- район не определяется по адресу «🛍️🎀 PHÒNG FULL NỘI THẤT CÓ BAN CÔNG ĐƯỜNG HOÀNG QU»; прецедент расколот: «QUỐC VIỆT»: anb 4, tanc 2, crg 1
  * 4585402665108758 -- тип жилья в тексте не назван
  * 2145630893006941 -- район не определяется по адресу «Chủ gửi»
  * 2145579633012067 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 2136097713960259 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NGUYỄN VĂN LI»
  * 2178278159742214 -- район не определяется по адресу «☸️🏚️📫MINIHOUSE CAO CẤP FULL NỘI THẤT - RỘNG 40M2 M»
  * 2192629371640426 -- район не определяется по адресу «🔮📭🌼CĂN MẶT TIỀN HẺM CÓ PHÒNG NGỦ RIÊNG ĐƯỜNG PHẠM »; прецедент расколот: «PHẠM NGŨ LÃO»: tanc 2, nki 1, anb 1
  * 2174816730088357 -- тип жилья в тексте не назван
  * 2129210777982286 -- район не определяется по адресу «CHO THUÊ CĂN HỘ TRUNG TÂM CẦN THƠ»
  * 1757290509336915 -- цена 650,000 VND вне разумных пределов
  * 1737136038019029 -- район не определяется по адресу «♥️Ưu đãi giảm 300k tháng đầu tiên!»
  * 1777096620689637 -- район не определяется по адресу «🔮📭🌼CĂN MẶT TIỀN HẺM CÓ PHÒNG NGỦ RIÊNG ĐƯỜNG PHẠM »; прецедент расколот: «PHẠM NGŨ LÃO»: tanc 2, nki 1, anb 1
  * 1773617367704229 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1761416928924273 -- район не определяется по адресу «🏩 CĂN NHÀ NHỎ RỘNG»
  * 1765803441818955 -- район не определяется по адресу «Cọc 1 tháng»
  * 1772660991133200 -- тип жилья в тексте не назван
  * 1744926680573298 -- тип жилья в тексте не назван
  * 1758617719204194 -- тип жилья в тексте не назван
  * 1763351818730784 -- тип жилья в тексте не назван
  * 2367341113805436 -- в посте несколько разных цен: 3,000, 4,500
  * 2397743264098554 -- в посте несколько разных цен: 9,000, 10,000
  * 2379455639260650 -- тип жилья в тексте не назван
  * 2384258058780408 -- район не определяется по адресу «ROOM FOR RENT: FEMALE ONLY 4K»
  * 2397178127488401 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2397460614126819 -- в посте несколько разных цен: 12,000, 18,000
  * 2371615766711304 -- в тексте есть и другая цена того же порядка: 7,833 против 18,000
  * 2392936531245894 -- в посте несколько разных цен: 9,000, 10,000
  * 2383302612209286 -- тот же текст уже заведён: id 3001967
  * 2391426354730245 -- район не определяется по адресу «ROOM FOR RENT (FEMALE ONLY)»
  * 2384022142137333 -- район не определяется по адресу «EL ORLANDO VILLAGE»
  * 2348011072701363 -- район не определяется по адресу «Basak San Nicolas»
  * 2369556196917261 -- тот же текст уже заведён: id 3001968
  * 4521497431443289 -- район не определяется по адресу «Bulacao Luyo Prince Warehouse»
  * 4568165530109812 -- в посте несколько разных цен: 12,000, 18,000
  * 4562745847318447 -- продажа
  * 4568197823439916 -- район не определяется по адресу «Basak San Nicolas»
  * 4555728451353520 -- тип жилья в тексте не назван
  * 4549148565344842 -- тип жилья в тексте не назван
  * 3105028929829311 -- район не определяется по адресу «Single Detached Fully Furnished 4- Bedroom House F»
  * 3107152942950243 -- район не определяется по адресу «Salinas Drive»
  * 3104421416556729 -- в посте несколько разных цен: 17,000, 22,000, 25,000
  * 3099825480349656 -- продажа
  * 3094642354201302 -- в посте несколько разных цен: 12,000, 17,000
  * 28770564795913888 -- район не определяется по адресу «FOR RENT!»
  * 28826433170327050 -- цена 1,500 PHP вне разумных пределов
  * 28840217038948663 -- в посте несколько разных цен: 2,000, 12,500
  * 28824521897184844 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2348011072701363 -- район не определяется по адресу «Basak San Nicolas»
  * 28778227495147618 -- в посте несколько разных цен: 11,000, 13,000
  * 28565420743094962 -- район не определяется по адресу «New Apartment for rent ♥️»
  * 28646959921607710 -- тот же текст уже заведён: id 3001967
  * 28808298728807161 -- в тексте есть и другая цена того же порядка: 9,538 против 25,000
  * 1753307146325594 -- уже на сайте: id 3001878
  * 1749995506656758 -- улица Trưng Nữ Vương идёт через несколько районов (hcg 13, hc 6), а пост называет только прежний район Hai Chau
  * 1754680382854937 -- район не определяется: «✨ APARTMENT FOR RENT, FPT ✨🏡, FPT Urban Area»
  * 1756431676013141 -- в посте несколько разных цен: 12,000,000, 13,500,000
  * 1756564899333152 -- цены в посте нет
  * 1756559822666993 -- район не определяется: «2-BEDROOM VILLA, HOI AN, Hoi An»
  * 1756559932666982 -- тот же текст уже заведён: id 3001978
  * 2236476216980037 -- тот же текст уже заведён: id 3001979
  * 2221665295127796 -- тот же текст уже заведён: id 3001980
  * 2241901533104172 -- нет ни одной скачанной фотографии
  * 2203496343611358 -- тот же текст уже заведён: id 3001981
  * 2245630299397962 -- тот же текст уже заведён: id 3001982
  * 2245612022733123 -- тот же текст уже заведён: id 3001983
  * 2245610196066639 -- тот же текст уже заведён: id 3001978
  * 2245607846066874 -- источники назвали разные районы: street=ns, ward=hx
  * 2245603999400592 -- тот же текст уже заведён: id 3001984
  * 2366385470866466 -- нет ни одной скачанной фотографии
  * 2373490586822621 -- нет ни одной скачанной фотографии
  * 2329906251181055 -- район не определяется: «**HOUSE FOR RENT, 3 BEDROOMS, THANH KHÊ»
  * 2362667247904955 -- район не определяется: «2-BEDROOM HOUSE FOR RENT, CAM CHAU, HOI AN»
  * 1659646015304123 -- в тексте есть и другая цена того же порядка: 20,000,000 против 17,000,000
  * 1628212845114107 -- похоже на уже заведённое: id 3001720
  * 1660837205185004 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT, 2 BATHROOMS, MIA PLAZA»
  * 1659747985293926 -- район не определяется: «FOR RENT: 2-BEDROOM APARTMENT, 2 BATHROOMS, MIA PLAZA DA NANG»
  * 1658654802069911 -- похоже на уже заведённое: id 1021549
  * 1642026050399453 -- район не определяется: «FOR RENT, 2-BEDROOM APARTMENT, MIA CENTER POINT»
  * 1405656428444813 -- тип жилья в тексте не назван
  * 1406929351650854 -- район не определяется: «APARTMENT NEAR NGUYEN TAT THANH BEACH, ONLY 9M ✨, Da Nang»
  * 1407471778263278 -- район не определяется: «👉Cho thuê nhà mặt tiền 5m5 gần Chu huy mân, có sân rộng»
  * 1400114168999039 -- это поиск жилья, а не предложение
  * 1407456994931423 -- район не определяется: «**Great location near My Khe Beach, Brand new 100%**, **45m²»
  * 1404956358514820 -- район не определяется: «CẬP NHẬT CĂN HỘ TRỐNG, 03/10, Căn 402»
  * 1498819502411033 -- район не определяется: «APARTMENT FOR RENT, AN THUONG 33, An Thuong 33»
  * 1496426262650357 -- в посте несколько разных цен: 7,000,000, 9,500,000
  * 1489359883356995 -- район не определяется: «MINI VILLA FOR RENT, PHAN KHOANG, Phan Khoang»
  * 2252555391983972 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2249715358934642 -- тип жилья в тексте не назван
  * 2240689496503895 -- тип жилья в тексте не назван
  * 2246076275965217 -- район не определяется по адресу «Taclobo»
  * 1686463159579101 -- район не определяется по адресу «HOUSE FOR RENT NEAR HOI AN ANCIENT TOWN»
  * 1720996282792455 -- район не определяется по адресу «🌿 Lovely 2-Bedroom Apartment for Rent in Hoi An 🏡»
  * 1659093615649389 -- район не определяется по адресу «NEW 2-BEDROOM HOUSE FOR LONG-TERM RENTAL»
  * 1720720756153341 -- район не определяется по адресу «✨ YOUR OWN LITTLE SPACE!»
  * 1705616164330467 -- район не определяется по адресу «A 1-bedroom apartment featuring a stunning view of»
  * 1719895296235887 -- район не определяется по адресу «Cute»
  * 1709427257282691 -- район не определяется по адресу «Cozy private apartment in a convenient location»
  * 1710230713869012 -- в посте несколько разных цен: 12,000,000, 18,000,000
  * 1708764027349014 -- район не определяется по адресу «✨ COZY 1-BEDROOM APARTMENT FOR RENT IN HOI AN ✨🏡»
  * 1705644377660979 -- район не определяется по адресу «2-BEDROOM HOUSE FOR RENT»
  * 2027169491294767 -- район не определяется по адресу «Entire house for rent on Dinh Tien Hoang Street»
  * 2021506941861022 -- район не определяется по адресу «3-BEDROOM VILLA FOR RENT»
  * 2028982294446820 -- район не определяется по адресу «✨ YOUR OWN LITTLE SPACE!»
  * 2029738977704485 -- район не определяется по адресу «Cozy private apartment in a convenient location»
  * 2009406873071029 -- район не определяется по адресу «2-BEDROOM GROUND-FLOOR APARTMENT FOR RENT»
  * 2026529394692110 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 1993632857981764 -- нет ни одной скачанной фотографии
  * 2001579740524994 -- район не определяется по адресу «Trảng Kèo 8»
  * 2000628700620098 -- тип жилья в тексте не назван
  * 2004057603610541 -- район не определяется по адресу «HOI AN PRIVATE VILLA FOR RENT»
  * 2004286143587687 -- в посте несколько разных цен: 7,000,000, 8,000,000
  * 2001539610529007 -- район не определяется по адресу «CHO THUÊ NHÀ GẦN PHỐ CỔ HỘI AN»
  * 2000122124004089 -- в тексте есть и другая цена того же порядка: 38,334,700 против 18,000,000
  * 1997355244280777 -- посуточно
  * 2029917844353265 -- нет ни одной скачанной фотографии
  * 1998953254116391 -- район не определяется по адресу «Nhà 98m²»
  * 1287853898988310 -- в тексте есть и другая цена того же порядка: 4,568,736 против 4,000,000
  * 1464410321887706 -- тот же текст уже заведён: id 3001985
  * 1407858374209568 -- район не определяется по адресу «Vị trí trung tâm»
  * 1506528094342595 -- тип жилья в тексте не назван
  * 1507435977585140 -- в посте несколько разных цен: 500,000, 600,000
  * 1499726755022729 -- в посте несколько разных цен: 500,000, 600,000
  * 2040218203352622 -- район не определяется по адресу «CHO THUÊ PHÒNG DÀI HẠN»
  * 1997802540927522 -- район не определяется по адресу «đường Tố Hữu»
  * 1680724936470148 -- тип жилья в тексте не назван
  * 1692451368630838 -- тип жилья в тексте не назван
  * 1708277650381543 -- район не определяется по адресу «CHO THUÊ STUDIO CAO CẤP»
  * 1762934068249234 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1762881568254484 -- район не определяется по адресу «EcoGarden»
  * 1761093448433296 -- район не определяется по адресу «PHÒNG STUDIO TẦNG 3»
  * 1637646127444696 -- район не определяется по адресу «Không gian sống hiện đại»
  * 4742360189343383 -- район не определяется по адресу «fully furnished»
  * 4743749845871084 -- источники назвали разные районы: precedent=ntr, ward=ph
  * 4743699732542762 -- похоже на уже заведённое: id 2001056
  * 4743696429209759 -- адрес называет несколько районов: btr, vh
  * 4743690755876993 -- район не определяется по адресу «--lvcc--»; прецедент расколот: «lvcc»: nt 1
  * 2103428090314611 -- район не определяется по адресу «Central Nha Trang»
  * 2103086887015398 -- в посте несколько разных цен: 500,000, 18,000,000
  * 2102610263729727 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2101944567129630 -- нет ни одной скачанной фотографии
  * 2103658440291576 -- адрес называет несколько районов: btr, vh
  * 2103634340293986 -- район не определяется по адресу «Ly Nam De»
  * 4626748320928022 -- похоже на уже заведённое: id 2000946
  * 4628240987445422 -- район не определяется по адресу «1-BEDROOM APARTMENT FOR RENT ~ AIRY»
  * 4623890491213805 -- район не определяется по адресу «Central location»
  * 4615612555374932 -- район не определяется по адресу «Muong Thanh 04 Tran Phu»
  * 4630547377214783 -- нет ни одной скачанной фотографии
  * 4633229313613256 -- район не определяется по адресу «1-BEDROOM APARTMENT»
  * 1097636699376885 -- район не определяется по адресу «📞📞 Contact +84901717411 via WhatsApp»
  * 1126061896534365 -- тип жилья в тексте не назван
  * 1125979989875889 -- в посте несколько разных цен: 1,000,000, 14,500,000
  * 1126019979871890 -- район не определяется по адресу «Khanh Hoa»
  * 2083319469168821 -- район не определяется по адресу «Ha Quang 2»
  * 2082870602547041 -- похоже на уже заведённое: id 2001056
  * 2076181956549239 -- район не определяется по адресу «** Khanh Hoa»
  * 2060280514806050 -- тот же текст уже заведён: id 3001989
  * 2071238320376936 -- район не определяется по адресу «**Khanh Hoa»
  * 2083494715817963 -- район не определяется по адресу «Tòa CT5»
  * 3860022427471637 -- район не определяется по адресу «Southern Nha Trang»
  * 3856331891174024 -- в посте несколько разных цен: 500,000, 13,000,000, 13,500,000
  * 3860056857468194 -- район не определяется по адресу «City center»
  * 3856943337779546 -- район не определяется по адресу «Southern Nha Trang»
  * 1482580230352712 -- район не определяется по адресу «💥💥💥HOUSE FOR RENT💥💥💥»
  * 1480625103881558 -- район не определяется по адресу «🍀🍀🍀LOVELY HOUSE FOR RENT IN VUNG TAU - CITY CENTER»
  * 3246119772249573 -- район не определяется по адресу «VILLA FOR RENT»
  * 3255575561303994 -- район не определяется по адресу «Apartment for rent near the beach - opposite Merma»
  * 3213120192216198 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»
  * 3257536201107930 -- помещение под бизнес или здание целиком, а не жильё
  * 3232506143610936 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 3236985219829695 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 3203441086517442 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ»
  * 1483417786935623 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
"""
from listing_lock import insert_listings

IDS = [3002016, 3002017, 3002018, 3002019, 3002020, 3002021, 3002022, 3002023, 3002024, 3002025, 3002026, 3002027, 3002028, 3002029, 3002030, 3002031, 3002032, 3002033, 3002034, 3002035, 3002036, 3002037, 3002038, 3002039]

NEW_SRC = r'''
L(3002016,"cebu","gua","Квартира",25000,None,
  "2-спальная квартира, Guadalupe.",
  "https://www.facebook.com/groups/993673090964916/posts/3106336639698540/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-07",
  descEn="2-bedroom flat, Guadalupe.",
  details={"photos": ["assets/fb_photos/3106336639698540/01.webp", "assets/fb_photos/3106336639698540/02.webp", "assets/fb_photos/3106336639698540/03.webp", "assets/fb_photos/3106336639698540/04.webp", "assets/fb_photos/3106336639698540/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002017,"cebu","mab","Квартира",23000,None,
  "2-спальная квартира, Mabolo.",
  "https://www.facebook.com/groups/993673090964916/posts/3106366376362233/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-07",
  descEn="2-bedroom flat, Mabolo.",
  details={"photos": ["assets/fb_photos/3106366376362233/01.webp", "assets/fb_photos/3106366376362233/02.webp", "assets/fb_photos/3106366376362233/03.webp", "assets/fb_photos/3106366376362233/04.webp", "assets/fb_photos/3106366376362233/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002018,"cebu","tlm","Дом",18000,None,
  "2-спальный дом, Talamban.",
  "https://www.facebook.com/groups/993673090964916/posts/3106122276386643/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-07",
  descEn="2-bedroom house, Talamban.",
  details={"photos": ["assets/fb_photos/3106122276386643/01.webp", "assets/fb_photos/3106122276386643/02.webp", "assets/fb_photos/3106122276386643/03.webp", "assets/fb_photos/3106122276386643/04.webp", "assets/fb_photos/3106122276386643/05.webp"], "am": ["pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002019,"cebu","man","Квартира",17000,None,
  "2-спальная квартира, Mandaue.",
  "https://www.facebook.com/groups/993673090964916/posts/3105063616492509/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-07",
  descEn="2-bedroom flat, Mandaue.",
  details={"photos": ["assets/fb_photos/3105063616492509/01.webp", "assets/fb_photos/3105063616492509/02.webp", "assets/fb_photos/3105063616492509/03.webp", "assets/fb_photos/3105063616492509/04.webp", "assets/fb_photos/3105063616492509/05.webp"], "am": ["b"], "fl": 3, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002020,"cebu","gua","Квартира",18000,None,
  "1-спальная квартира, Guadalupe.",
  "https://www.facebook.com/groups/3914645581932487/posts/28849022008068166/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-07",
  descEn="1-bedroom flat, Guadalupe.",
  details={"photos": ["assets/fb_photos/28849022008068166/01.webp", "assets/fb_photos/28849022008068166/02.webp", "assets/fb_photos/28849022008068166/03.webp", "assets/fb_photos/28849022008068166/04.webp", "assets/fb_photos/28849022008068166/05.webp"], "am": ["lift", "pool"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002021,"cebu","man","Квартира",15000,25,
  "1-спальная квартира, 25 м², Mandaue.",
  "https://www.facebook.com/groups/3914645581932487/posts/28836130679357299/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-07",
  descEn="1-bedroom flat, 25 m², Mandaue.",
  details={"photos": ["assets/fb_photos/28836130679357299/01.webp", "assets/fb_photos/28836130679357299/02.webp", "assets/fb_photos/28836130679357299/03.webp", "assets/fb_photos/28836130679357299/04.webp", "assets/fb_photos/28836130679357299/05.webp"], "am": ["k", "pool", "gym"], "fl": 4, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002022,"da-nang","hcg","Дом",12000000,None,
  "3-спальный дом, Hóa Sơn 4, Hòa Cường.",
  "https://www.facebook.com/groups/476056366996433/posts/1656261375642587/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="3-bedroom house, Hóa Sơn 4, Hòa Cường.",
  details={"photos": ["assets/fb_photos/1656261375642587/01.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3002023,"da-nang","ah","Комната",6000000,None,
  "Комната, Phước Trường 3, An Hải.",
  "https://www.facebook.com/groups/476056366996433/posts/1655589649043093/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="Room, Phước Trường 3, An Hải.",
  details={"photos": ["assets/fb_photos/1655589649043093/01.webp", "assets/fb_photos/1655589649043093/02.webp", "assets/fb_photos/1655589649043093/03.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3002024,"da-nang","hcg","Квартира",7000000,None,
  "Квартира, BRAND-NEW APARTMENT, Hòa Cường.",
  "https://www.facebook.com/groups/728946289449167/posts/1405859971757792/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="Flat, BRAND-NEW APARTMENT, Hòa Cường.",
  details={"photos": ["assets/fb_photos/1405859971757792/01.webp", "assets/fb_photos/1405859971757792/02.webp", "assets/fb_photos/1405859971757792/03.webp", "assets/fb_photos/1405859971757792/04.webp", "assets/fb_photos/1405859971757792/05.webp"], "am": ["w", "k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002025,"da-nang","hx","Квартира",6000000,None,
  "Квартира, ✨ 1 PHÒNG NGỦ FULL NỘI THẤT, Hòa Xuân.",
  "https://www.facebook.com/groups/728946289449167/posts/1407479641595825/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="Flat, ✨ 1 PHÒNG NGỦ FULL NỘI THẤT, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1407479641595825/01.webp", "assets/fb_photos/1407479641595825/02.webp", "assets/fb_photos/1407479641595825/03.webp", "assets/fb_photos/1407479641595825/04.webp", "assets/fb_photos/1407479641595825/05.webp"], "am": ["w", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002026,"da-nang","ah","Дом",12000000,100,
  "2-спальный дом, 100 м², CHO THUÊ NHÀ NGUYÊN CĂN, An Hải — 1 санузел.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1497921535834163/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="2-bedroom house, 100 m², CHO THUÊ NHÀ NGUYÊN CĂN, An Hải — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1497921535834163/01.webp", "assets/fb_photos/1497921535834163/02.webp"], "am": ["k", "pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002027,"dumaguete","btg","Дом",15000,None,
  "2-спальный дом, Batinguel.",
  "https://www.facebook.com/groups/153191128587086/posts/2242577632981748/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-07",
  descEn="2-bedroom house, Batinguel.",
  details={"photos": ["assets/fb_photos/2242577632981748/01.webp", "assets/fb_photos/2242577632981748/02.webp", "assets/fb_photos/2242577632981748/03.webp", "assets/fb_photos/2242577632981748/04.webp", "assets/fb_photos/2242577632981748/05.webp"], "am": ["k", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002028,"hue","acu","Дом",15000000,81,
  "Дом, 81 м², An Cựu — 4 санузла.",
  "https://www.facebook.com/groups/807531664242245/posts/1466927818302623/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="House, 81 m², An Cựu — 4 bathrooms.",
  details={"photos": ["assets/fb_photos/1466927818302623/01.webp", "assets/fb_photos/1466927818302623/02.webp", "assets/fb_photos/1466927818302623/03.webp", "assets/fb_photos/1466927818302623/04.webp", "assets/fb_photos/1466927818302623/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002029,"hue","acu","Студия",5000000,32,
  "Студия, 32 м², An Cựu.",
  "https://www.facebook.com/groups/phongtrosvhue/posts/1676192456923396/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="Studio, 32 m², An Cựu.",
  details={"photos": ["assets/fb_photos/1676192456923396/01.webp", "assets/fb_photos/1676192456923396/02.webp", "assets/fb_photos/1676192456923396/03.webp", "assets/fb_photos/1676192456923396/04.webp", "assets/fb_photos/1676192456923396/05.webp"], "am": ["w", "k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002030,"hue","vyd","Студия",6000000,40,
  "Студия, 40 м², Vỹ Dạ.",
  "https://www.facebook.com/groups/phongtrosvhue/posts/1699463947929580/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="Studio, 40 m², Vỹ Dạ.",
  details={"photos": ["assets/fb_photos/1699463947929580/01.webp", "assets/fb_photos/1699463947929580/02.webp", "assets/fb_photos/1699463947929580/03.webp", "assets/fb_photos/1699463947929580/04.webp", "assets/fb_photos/1699463947929580/05.webp"], "am": ["w", "k", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002031,"nha-trang","ph","Квартира",14000000,80,
  "1-спальная квартира, 80 м², Phước Hải.",
  "https://www.facebook.com/groups/2253829621529798/posts/4743707395875329/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="1-bedroom flat, 80 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/4743707395875329/01.webp", "assets/fb_photos/4743707395875329/02.webp", "assets/fb_photos/4743707395875329/03.webp", "assets/fb_photos/4743707395875329/04.webp", "assets/fb_photos/4743707395875329/05.webp"], "am": ["w", "b", "lift"], "fl": 4, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002032,"nha-trang","lt","Студия",8000000,40,
  "Студия, 40 м², Lộc Thọ — 1 санузел.",
  "https://www.facebook.com/groups/1172766863380743/posts/2103628353627918/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="Studio, 40 m², Lộc Thọ — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2103628353627918/01.webp", "assets/fb_photos/2103628353627918/02.webp", "assets/fb_photos/2103628353627918/03.webp", "assets/fb_photos/2103628353627918/04.webp"], "am": ["w", "k", "lift"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002033,"nha-trang","ph","Квартира",17000000,70,
  "1-спальная квартира, 70 м², Phước Hải.",
  "https://www.facebook.com/groups/chothue79/posts/4635199233416264/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="1-bedroom flat, 70 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/4635199233416264/01.webp", "assets/fb_photos/4635199233416264/02.webp", "assets/fb_photos/4635199233416264/03.webp", "assets/fb_photos/4635199233416264/04.webp", "assets/fb_photos/4635199233416264/05.webp"], "am": ["w", "b", "lift", "gym"], "fl": 1, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002034,"nha-trang","btr","Квартира",23000000,100,
  "2-спальная квартира, 100 м², Bắc Nha Trang — 1 санузел.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1117203214086900/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="2-bedroom flat, 100 m², Bắc Nha Trang — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1117203214086900/01.webp", "assets/fb_photos/1117203214086900/02.webp", "assets/fb_photos/1117203214086900/03.webp", "assets/fb_photos/1117203214086900/04.webp", "assets/fb_photos/1117203214086900/05.webp"], "am": ["k", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002035,"nha-trang","pl","Дом",25000000,None,
  "5-спальный дом, Phước Long — 4 санузла.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1125804183226803/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="5-bedroom house, Phước Long — 4 bathrooms.",
  details={"photos": ["assets/fb_photos/1125804183226803/01.webp", "assets/fb_photos/1125804183226803/02.webp", "assets/fb_photos/1125804183226803/03.webp", "assets/fb_photos/1125804183226803/04.webp", "assets/fb_photos/1125804183226803/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002036,"nha-trang","pl","Дом",25000000,300,
  "4-спальный дом, 300 м², Phước Long — 4 санузла.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1125809883226233/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="4-bedroom house, 300 m², Phước Long — 4 bathrooms.",
  details={"photos": ["assets/fb_photos/1125809883226233/01.webp", "assets/fb_photos/1125809883226233/02.webp", "assets/fb_photos/1125809883226233/03.webp", "assets/fb_photos/1125809883226233/04.webp", "assets/fb_photos/1125809883226233/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002037,"nha-trang","btr","Дом",15000000,60,
  "2-спальный дом, 60 м², Bắc Nha Trang — 1 санузел.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2082963112537790/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="2-bedroom house, 60 m², Bắc Nha Trang — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2082963112537790/01.webp", "assets/fb_photos/2082963112537790/02.webp", "assets/fb_photos/2082963112537790/03.webp", "assets/fb_photos/2082963112537790/04.webp", "assets/fb_photos/2082963112537790/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002038,"nha-trang","vp","Квартира",23000000,75,
  "2-спальная квартира, 75 м², Vĩnh Phước — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2083377932496308/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="2-bedroom flat, 75 m², Vĩnh Phước — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/2083377932496308/01.webp", "assets/fb_photos/2083377932496308/02.webp", "assets/fb_photos/2083377932496308/03.webp", "assets/fb_photos/2083377932496308/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002039,"nha-trang","lt","Квартира",15000000,35,
  "Квартира, 35 м², Lộc Thọ.",
  "https://www.facebook.com/groups/849441571863086/posts/3857113297762550/","сегодня",0,source="fbgroup",postedOn="2026-10-07",
  descEn="Flat, 35 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/3857113297762550/01.webp", "assets/fb_photos/3857113297762550/02.webp", "assets/fb_photos/3857113297762550/03.webp", "assets/fb_photos/3857113297762550/04.webp", "assets/fb_photos/3857113297762550/05.webp"], "am": ["w", "b", "lift"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
