# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 18 строк, 2026-09-28.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 993673090964916/3096835193982018 -- cebu/mab, 23,000 PHP: район назван в адресе поста
  * 3914645581932487/28736619799308388 -- cebu/cap, 35,000 PHP: район назван в адресе поста
  * 476056366996433/1651454722789919 -- da-nang/ns, 14,000,000 VND: «2-BEDROOM APARTMENT FOR RENT»: 2 строк сайта, все в ns
  * canhochungcudanang/2981249928935751 -- da-nang/ns, 17,500,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * canhochungcudanang/2969867860073958 -- da-nang/ns, 15,200,000 VND: район назван в посте; улица An Thượng 22: 3 из 3 отрезков в ns
  * 1454201286459382/1574683517744491 -- da-nang/ns, 9,500,000 VND: «Apartment for Rent»: 2 строк сайта, все в ns
  * 1454201286459382/1574681351078041 -- da-nang/ns, 19,000,000 VND: улица Tuy Lý Vương: 1 из 1 отрезков в ns
  * phongtrocanhonhadanang/1488716350088015 -- da-nang/ah, 12,000,000 VND: улица Nguyễn Thiện Kế: 2 из 2 отрезков в ah; пост: Son Tra
  * phongtrosvhue/1676192456923396 -- hue/acu, 5,000,000 VND: район назван в адресе поста
  * chothue79/4622243491378505 -- nha-trang/vp, 15,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2722683684830573 -- nha-trang/ph, 18,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2719042408528034 -- nha-trang/ph, 15,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1981650005864100 -- nha-trang/ntr, 12,000,000 VND: район назван в адресе поста
  * 2253829621529798/4732237407022328 -- nha-trang/ph, 20,000,000 VND: район назван в адресе поста
  * 1172766863380743/2095436347780452 -- nha-trang/btr, 30,000,000 VND: район назван в адресе поста
  * 1172766863380743/2095448704445883 -- nha-trang/lt, 8,500,000 VND: район назван в адресе поста
  * 1172766863380743/2095404804450273 -- nha-trang/vh, 20,000,000 VND: район назван в адресе поста
  * 849441571863086/3847261448747735 -- nha-trang/btr, 23,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (222):
  * 4534963593485999 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 4535108773471481 -- район не определяется по адресу «Chủ gửi»
  * 4524078787907813 -- район не определяется по адресу «GIÁ THUÊ : 2.7 TRIỆU»
  * 4547172472265111 -- тот же текст уже заведён: id 3001175
  * 4578192675829757 -- район не определяется по адресу «🥨🫜🍒 CĂN HỘ CAO CẤP MỚI XÂY KDC AN KHÁNH FULL NỘI T»
  * 4576672325981792 -- район не определяется по адресу «🛍️🎀 PHÒNG FULL NỘI THẤT CÓ BAN CÔNG ĐƯỜNG HOÀNG QU»
  * 4569057556743269 -- в посте несколько разных цен: 4,850,000, 9,700,000
  * 4569058646743160 -- тот же текст уже заведён: id 3001524
  * 4569297596719265 -- тип жилья в тексте не назван
  * 2145727852997245 -- район не определяется по адресу «Chủ gửi»
  * 2145579633012067 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 2136097713960259 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NGUYỄN VĂN LI»
  * 2132985117604852 -- район не определяется по адресу «CHO THUÊ CĂN HỘ TRUNG TÂM CẦN THƠ»
  * 2184098422493521 -- район не определяется по адресу «🍩🥮🍪MINIHOUSE BAN CÔNG MỚI XÂY KDC ĐẠI NGÂN GẦN ĐHY»
  * 2184016365835060 -- район не определяется по адресу «🎋🌹🍁 PHÒNG TRỌ MỚI XÂY ĐƯỜNG TRẦN HOÀNG NA GẦN 30/4»
  * 2182373332666030 -- район не определяется по адресу «1/10 trống!»
  * 2178278159742214 -- район не определяется по адресу «☸️🏚️📫MINIHOUSE CAO CẤP FULL NỘI THẤT - RỘNG 40M2 M»
  * 2174816730088357 -- тип жилья в тексте не назван
  * 1757290509336915 -- цена 650,000 VND вне разумных пределов
  * 1725575419175091 -- тип жилья в тексте не назван
  * 1725714562494510 -- район не определяется по адресу «Chủ gửi»
  * 1770000914732541 -- район не определяется по адресу «MINIHOUSE MẶT TIỀN NGAY TRUNG TÂM - GẦN VINCOM HÙN»
  * 1767068018359164 -- район не определяется по адресу «🎁 Giảm 300k tháng đầu tiên»
  * 1764604961938803 -- район не определяется по адресу «🏵️🌺🧿MINIHOUSE 2 PHÒNG NGỦ GẦN KDC NGÂN THUẬN - LỘ »
  * 1758617719204194 -- тип жилья в тексте не назван
  * 1763351818730784 -- тип жилья в тексте не назван
  * 2384022142137333 -- район не определяется по адресу «EL ORLANDO VILLAGE»
  * 2384258058780408 -- район не определяется по адресу «ROOM FOR RENT: FEMALE ONLY 4K»
  * 2388233741716173 -- район не определяется по адресу «New Apartment for rent ♥️»
  * 2386742698531944 -- это поиск жилья, а не предложение
  * 2386750458531168 -- район не определяется по адресу «ROOM FOR RENT (LADIES ONLY)»
  * 4555728451353520 -- тип жилья в тексте не назван
  * 4553647301561635 -- район не определяется по адресу «HOUSE FOR RENT ‼️ ALMIYA SUBDIVISION»
  * 4555775611348804 -- это поиск жилья, а не предложение
  * 4557081944551504 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4552676971658668 -- тот же текст уже заведён: id 3001525
  * 4521497431443289 -- район не определяется по адресу «Bulacao Luyo Prince Warehouse»
  * 3094111684254369 -- район не определяется по адресу «FOR RENT 1BR condo‼️‼️‼️»
  * 3090285144637023 -- тип жилья в тексте не назван
  * 3097058120626392 -- район не определяется по адресу «General Maxilom Ave (Mango Ave)»
  * 3094642354201302 -- в посте несколько разных цен: 12,000, 17,000
  * 3093396874325850 -- нет ни одной скачанной фотографии
  * 3096194254046112 -- в посте несколько разных цен: 2,000, 28,000
  * 3089574081374796 -- тот же текст уже заведён: id 3001116
  * 3096120780720126 -- район не определяется по адресу «✨AVAILABLE FOR RENT 2 BEDROOM UNIT💥✨»
  * 28663251676645201 -- район не определяется по адресу «Room for rent in Subangdaku»
  * 28734003092903392 -- район не определяется по адресу «**UNBEATABLE ACCESSIBILITY**»
  * 28734514449518923 -- район не определяется по адресу «Solinea Tower 1»
  * 28735751689395199 -- район не определяется по адресу «Cebu Business Park»
  * 28687829347520767 -- в посте несколько разных цен: 3,000, 15,000
  * 28697961909840844 -- нет ни одной скачанной фотографии
  * 28703438985959803 -- нет ни одной скачанной фотографии
  * 28646959921607710 -- тот же текст уже заведён: id 3001116
  * 28687929330844102 -- район не определяется по адресу «HOUSE FOR RENT ‼️ ALMIYA SUBDIVISION»
  * 2363088937843855 -- тип жилья в тексте не назван
  * 2371245923694823 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 2 PHÒNG NGỦ»
  * 2371985340287548 -- район не определяется по адресу «HOUSE FOR RENT»
  * 2371572253662190 -- в посте несколько разных цен: 700,000, 15,000,000
  * 2372458173573598 -- помещение под бизнес или здание целиком, а не жильё
  * 2366316614187754 -- район не определяется по адресу «Panorama Apartment for Rent»
  * 2367064320779650 -- район не определяется по адресу «LUXURY BRAND-NEW HOUSE FOR RENT»
  * 2370956603723755 -- нет ни одной скачанной фотографии
  * 2367397907412958 -- это поиск жилья, а не предложение
  * 2370052703814145 -- район не определяется по адресу «1-BEDROOM APARTMENT AVAILABLE FOR LONG-TERM LEASE »
  * 1746041937052115 -- тот же текст уже заведён: id 3001526
  * 1746627713660204 -- в посте несколько разных цен: 11,500,000, 13,500,000, 14,000,000
  * 1746023073720668 -- тот же текст уже заведён: id 3001527
  * 1746240140365628 -- источники назвали разные районы: precedent=ns, ward=hx
  * 1745873907068918 -- в посте несколько разных цен: 6,500,000, 369,745,619
  * 1746080637048245 -- район не определяется: «Hoa Son (Quiet, peaceful & ultra-serene neighborhood), 🌊 BRAND NEW ULTRA-LUXURY 1-BEDROOM APARTMENT FOR RENT»
  * 2233882067239452 -- тот же текст уже заведён: id 3001528
  * 2226949671266025 -- район не определяется: «Apartment Highlights:, Prime Location, Lý Đạo Thành Street:»
  * 2229982960962696 -- улица Xô Viết Nghệ Tĩnh идёт через несколько районов (hcg 24, cl2 17), а пост называет только прежний район Hai Chau
  * 2230754917552167 -- улица Nguyễn Chánh идёт через несколько районов (lc 13, hk 5), а пост называет только прежний район Lien Chieu
  * 2232654177362241 -- район не определяется: «BRAND-NEW 1-BEDROOM APARTMENT FOR RENT, AN THUONG, An Thuong area»
  * 2232022014092124 -- нет ни одной скачанной фотографии
  * 2230071360953856 -- тип жилья в тексте не назван
  * 2229842037643455 -- в посте несколько разных цен: 8,000,000, 12,000,000, 14,000,000, 15,000,000
  * 2231605974133728 -- нет ни одной скачанной фотографии
  * 1477203231239327 -- район не определяется: «Brand-new house for rent: 4 floors, 4 bedrooms, 6 bathrooms»
  * 1487288543564129 -- тот же текст уже заведён: id 3001529
  * 1485169163776067 -- нет ни одной скачанной фотографии
  * 1488120813480902 -- в посте несколько разных цен: 11,000,000, 14,000,000
  * 1485327343760249 -- нет ни одной скачанной фотографии
  * 1650952562840135 -- район не определяется: «HOUSE FOR RENT, MAI CHI THO STREET, Mai Chi Tho»
  * 1643178526950872 -- в посте несколько разных цен: 25,000,000, 27,000,000
  * 1651210349481023 -- район не определяется: «APARTMENT FOR RENT IN THE PONTE, BEAUTIFUL DESIGN, FULLY FURNISHED»
  * 1651352766133448 -- похоже на уже заведённое: id 1012086
  * 1651443406124384 -- тип жилья в тексте не назван
  * 1396653956011727 -- в посте несколько разных цен: 11,500,000, 13,500,000, 14,000,000
  * 1397782809232175 -- похоже на уже заведённое: id 3001302
  * 1396804425996680 -- район не определяется: «Studio full nội thất, bếp riêng, Sơn Trà / Fully Furnished Studio with Private Kitchen»
  * 1397460295931093 -- район не определяется: «Vị trí thuận tiện, Làng Đại học, Phan Châu Trinh»
  * 2977953042598773 -- район не определяется: «chung cư HAGL - 72 Hàm Nghi, HAGL Apartment - 72 Hàm Nghi, the city center»
  * 2977062496021161 -- район не определяется: «CHO THUÊ CĂN HỘ CAO CẤP HYORI, ĐÀ NẴNG, HYORI PREMIUM 2-BEDROOM APARTMENT FOR RENT»
  * 1574972141048962 -- район не определяется: «🌾House located in alley 25 Ha Huy Tap, accessible by car.»
  * 1574191837793659 -- улица Phạm Vấn идёт через несколько районов (ah 1, st 1), а пост называет только прежний район Son Tra
  * 1575164074363102 -- район ns не входит в прежний район Son Tra из поста
  * 1575102691035907 -- в посте несколько разных цен: 6,500,000, 7,000,000
  * 1574998491046327 -- район не определяется: «Property details:, Flood-free area in Hoi An, WHOLE VILLA FOR RENT NEAR CUA DAI BRIDGE»
  * 1571298261416350 -- это поиск жилья, а не предложение
  * 1570473774832132 -- это поиск жилья, а не предложение
  * 1575192211026955 -- похоже на уже заведённое: id 2000856
  * 1565206808692162 -- нет ни одной скачанной фотографии
  * 1568526158360227 -- это поиск жилья, а не предложение
  * 1489359883356995 -- район не определяется: «MINI VILLA FOR RENT, PHAN KHOANG, Phan Khoang»
  * 1489334096692907 -- район не определяется: «FULLY FURNISHED STUDIO IN THE CITY CENTER, Vu Trong Phung, Hai Chau»
  * 1489342136692103 -- улица Trần Hưng Đạo идёт через несколько районов (ah 18, вне 11, st 4, ns 3), а пост называет только прежний район Son Tra
  * 2246160629290115 -- район не определяется по адресу «May I ask permission to post Admin.»
  * 2245260889380089 -- тот же текст уже заведён: id 3001530
  * 2246072355965609 -- тот же текст уже заведён: id 3001531
  * 2244714546101390 -- район не определяется по адресу «House for rent with swimming pool»
  * 2246076275965217 -- район не определяется по адресу «Taclobo»
  * 2231309210775257 -- район не определяется по адресу «HOUSE FEATURES»
  * 2245287132710798 -- в посте несколько разных цен: 15,000, 22,000
  * 2240689496503895 -- тип жилья в тексте не назван
  * 28516260041309277 -- тип жилья в тексте не назван
  * 28960082756927001 -- тип жилья в тексте не назван
  * 29240192592249348 -- помещение под бизнес или здание целиком, а не жильё
  * 28822141150721163 -- помещение под бизнес или здание целиком, а не жильё
  * 29101311996137409 -- тип жилья в тексте не назван
  * 957601213577144 -- в посте несколько разных цен: 4,000,000, 6,000,000
  * 968845495786049 -- нет ни одной скачанной фотографии
  * 955745937096005 -- тип жилья в тексте не назван
  * 938069275530338 -- нет ни одной скачанной фотографии
  * 1705644377660979 -- район не определяется по адресу «2-BEDROOM HOUSE FOR RENT»
  * 1712289126996504 -- район не определяется по адресу «Brand new house»
  * 1704894227735994 -- район не определяется по адресу «HOUSE FOR RENT»
  * 1711664937058923 -- район не определяется по адресу «✨ Modern 1-Bedroom Apartment for Rent in Central H»
  * 1709427257282691 -- район не определяется по адресу «Cozy private apartment in a convenient location»
  * 1710230713869012 -- в посте несколько разных цен: 12,000,000, 18,000,000
  * 1710709390487811 -- район не определяется по адресу «✨ COZY 1-BEDROOM APARTMENT FOR RENT IN HOI AN ✨🏡»
  * 2021506941861022 -- район не определяется по адресу «3-BEDROOM VILLA FOR RENT»
  * 2020348438643539 -- район не определяется по адресу «House details:»
  * 2021222221889494 -- район не определяется по адресу «Right by Cua Dai Bridge»
  * 2017947155550334 -- район не определяется по адресу «PRIVATE 4-BEDROOM CORNER VILLA»
  * 2020537728624610 -- район не определяется по адресу «a non-flooding area»
  * 2021296185215431 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 2022184211793295 -- район не определяется по адресу «Spacious 3-Bedroom House for Long-Term Rent Near H»
  * 1287853898988310 -- в тексте есть и другая цена того же порядка: 4,568,736 против 4,000,000
  * 1507435977585140 -- в посте несколько разных цен: 500,000, 600,000
  * 1506528094342595 -- тип жилья в тексте не назван
  * 1499726755022729 -- в посте несколько разных цен: 500,000, 600,000
  * 1947495812624862 -- район не определяется по адресу «STUDIO FULL NỘI THẤT»
  * 1997802540927522 -- район не определяется по адресу «đường Tố Hữu»
  * 1692451368630838 -- тип жилья в тексте не назван
  * 1708277650381543 -- район не определяется по адресу «CHO THUÊ STUDIO CAO CẤP»
  * 1637646127444696 -- район не определяется по адресу «Không gian sống hiện đại»
  * 1251745672701412 -- в посте несколько разных цен: 4,000,000, 4,500,000, 4,800,000
  * 3837694026371144 -- нет ни одной скачанной фотографии
  * 3844860945654452 -- тот же текст уже заведён: id 3001416
  * 3846876995452847 -- район не определяется по адресу «3 tầng»
  * 3846906242116589 -- тот же текст уже заведён: id 3001532
  * 3845481628925717 -- тот же текст уже заведён: id 3001533
  * 3845510235589523 -- тот же текст уже заведён: id 3001534
  * 3846286742178539 -- тот же текст уже заведён: id 3001535
  * 3838846259589254 -- в посте несколько разных цен: 14,500,000, 15,500,000
  * 3845656285574918 -- тот же текст уже заведён: id 3001536
  * 3845948588879021 -- район не определяется по адресу «Bustling residential area near the city center»
  * 1116292897511265 -- в посте несколько разных цен: 500,000, 14,000,000
  * 1116393200834568 -- район не определяется по адресу «NT RENT»
  * 1114003031073585 -- нет ни одной скачанной фотографии
  * 1116838927456662 -- район не определяется по адресу «**Khanh Hoa»
  * 1116293970844491 -- район не определяется по адресу «NT RENT»
  * 1116057517534803 -- тот же текст уже заведён: id 3001537
  * 1116228750851013 -- район не определяется по адресу «**Khanh Hoa»
  * 2072146586952776 -- нет ни одной скачанной фотографии
  * 2073488746818560 -- нет ни одной скачанной фотографии
  * 2057506045083497 -- в посте несколько разных цен: 15,500,000, 16,000,000
  * 4615612555374932 -- нет ни одной скачанной фотографии
  * 4620269678242553 -- район не определяется по адресу «NT RENT»
  * 4621972501405604 -- район не определяется по адресу «MODERN 1BEDROOM FOR RENT»
  * 4624372704498917 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4619187528350768 -- в посте несколько разных цен: 500,000, 12,500,000
  * 4617186755217512 -- это поиск жилья, а не предложение
  * 4596231547313033 -- в посте несколько разных цен: 9,000,000, 12,000,000
  * 4618707241732130 -- нет ни одной скачанной фотографии
  * 4611904355745752 -- нет ни одной скачанной фотографии
  * 2720297438402531 -- в тексте есть и другая цена того же порядка: 8,580,887 против 25,000,000
  * 2722352204863721 -- район не определяется по адресу «NT RENT»
  * 2722648204834121 -- район не определяется по адресу «Nguyen Dinh Chieu - Nha Trang»
  * 2722322491533359 -- район не определяется по адресу «NT RENT»
  * 2722573131508295 -- район не определяется по адресу «Southern Nha Trang»
  * 2712281229204152 -- нет ни одной скачанной фотографии
  * 1981279022567865 -- район не определяется по адресу «Central location»
  * 4721597574752978 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4732831413629594 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4732902920289110 -- район не определяется по адресу «FOR RENT»
  * 4732804100298992 -- район не определяется по адресу «FOR RENT»
  * 4733007783611957 -- район не определяется по адресу «** Khanh Hoa»
  * 4732861156959953 -- район не определяется по адресу «Convenient residential area with plenty of ameniti»
  * 2095417404449013 -- район не определяется по адресу «FOR RENT»
  * 2095354357788651 -- район не определяется по адресу «FOR RENT»
  * 2093336394657114 -- район не определяется по адресу «City center»
  * 2092650078059079 -- в посте несколько разных цен: 660,000, 700,000, 1,000,000, 15,000,000
  * 3848235645316982 -- район не определяется по адресу «Convenient residential area with plenty of ameniti»
  * 3846041548869725 -- тот же текст уже заведён: id 3001532
  * 3848237591983454 -- район не определяется по адресу «Convenient residential area with plenty of ameniti»
  * 3848297518644128 -- похоже на уже заведённое: id new:chothue79/4622243491378505
  * 3848199038653976 -- район не определяется по адресу «Southern Nha Trang»
  * 5551917961699508 -- район не определяется по адресу «2BR»
  * 5551876498370321 -- район не определяется по адресу «28 Nguyễn Huệ»
  * 5550361121855192 -- район не определяется по адресу «studio layout featuring 2 beds»
  * 5551753641715940 -- район не определяется по адресу «Vị trí trung tâm Quy Nhơn»
  * 5546593298898641 -- район не определяется по адресу «Đường Lê Đức Thọ»; прецедент расколот: «Le Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место; «Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место
  * 3288974787980281 -- нет ни одной скачанной фотографии
  * 3288882517989508 -- нет ни одной скачанной фотографии
  * 3290024791208614 -- район не определяется по адресу «Vị trí trung tâm Quy Nhơn»
  * 3290133441197749 -- район не определяется по адресу «2BR»
  * 3285077928369967 -- район не определяется по адресу «Đường Lê Đức Thọ»; прецедент расколот: «Le Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место; «Duc Tho»: совпало только в ссылках строк qn -- это реклама, а не место
  * 3255575561303994 -- район не определяется по адресу «Apartment for rent near the beach - opposite Merma»
  * 3257536201107930 -- помещение под бизнес или здание целиком, а не жильё
  * 3246119772249573 -- район не определяется по адресу «VILLA FOR RENT»
  * 3252616481599902 -- район не определяется по адресу «CHO THUÊ NHÀ PHAN CHU TRINH»
  * 3258417357686481 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 3213120192216198 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»
  * 3236985219829695 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 3203441086517442 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ»
  * 3170988256429392 -- район не определяется по адресу «gồm 1 phòng ngủ»
  * 3161796947348523 -- район не определяется по адресу «**CHO THUÊ CĂN HỘ MINI ĐƯỜNG THỐNG NHẤT»
  * 1479503063993762 -- район не определяется по адресу «AIRIA VUNG TAU»
  * 1480625103881558 -- район не определяется по адресу «🍀🍀🍀LOVELY HOUSE FOR RENT IN VUNG TAU - CITY CENTER»
"""
from listing_lock import insert_listings

IDS = [3001602, 3001603, 3001604, 3001605, 3001606, 3001607, 3001608, 3001609, 3001610, 3001611, 3001612, 3001613, 3001614, 3001615, 3001616, 3001617, 3001618, 3001619]

NEW_SRC = r'''
L(3001602,"cebu","mab","Квартира",23000,None,
  "2-спальная квартира, Mabolo.",
  "https://www.facebook.com/groups/993673090964916/posts/3096835193982018/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-28",
  descEn="2-bedroom flat, Mabolo.",
  details={"photos": ["assets/fb_photos/3096835193982018/01.webp", "assets/fb_photos/3096835193982018/02.webp", "assets/fb_photos/3096835193982018/03.webp", "assets/fb_photos/3096835193982018/04.webp", "assets/fb_photos/3096835193982018/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001603,"cebu","cap","Квартира",35000,None,
  "1-спальная квартира, Capitol Site.",
  "https://www.facebook.com/groups/3914645581932487/posts/28736619799308388/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-28",
  descEn="1-bedroom flat, Capitol Site.",
  details={"photos": ["assets/fb_photos/28736619799308388/01.webp", "assets/fb_photos/28736619799308388/02.webp", "assets/fb_photos/28736619799308388/03.webp", "assets/fb_photos/28736619799308388/04.webp", "assets/fb_photos/28736619799308388/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001604,"da-nang","ns","Квартира",14000000,None,
  "2-спальная квартира, APARTMENT FOR RENT, Ngũ Hành Sơn — 2 санузла.",
  "https://www.facebook.com/groups/476056366996433/posts/1651454722789919/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="2-bedroom flat, APARTMENT FOR RENT, Ngũ Hành Sơn — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1651454722789919/01.webp", "assets/fb_photos/1651454722789919/02.webp", "assets/fb_photos/1651454722789919/03.webp", "assets/fb_photos/1651454722789919/04.webp", "assets/fb_photos/1651454722789919/05.webp"], "am": ["pool"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001605,"da-nang","ns","Квартира",17500000,None,
  "1-спальная квартира, Prime Location: An Thuong 10, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2981249928935751/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="1-bedroom flat, Prime Location: An Thuong 10, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2981249928935751/01.webp", "assets/fb_photos/2981249928935751/02.webp", "assets/fb_photos/2981249928935751/03.webp", "assets/fb_photos/2981249928935751/04.webp", "assets/fb_photos/2981249928935751/05.webp"], "am": ["w", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001606,"da-nang","ns","Квартира",15200000,None,
  "1-спальная квартира, An Thượng 22, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2969867860073958/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="1-bedroom flat, An Thượng 22, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2969867860073958/01.webp", "assets/fb_photos/2969867860073958/02.webp", "assets/fb_photos/2969867860073958/03.webp", "assets/fb_photos/2969867860073958/04.webp", "assets/fb_photos/2969867860073958/05.webp"], "am": ["w", "k", "b"], "fl": 6, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001607,"da-nang","ns","Квартира",9500000,None,
  "Квартира, Apartment for Rent, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/1454201286459382/posts/1574683517744491/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="Flat, Apartment for Rent, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1574683517744491/01.webp", "assets/fb_photos/1574683517744491/02.webp", "assets/fb_photos/1574683517744491/03.webp", "assets/fb_photos/1574683517744491/04.webp", "assets/fb_photos/1574683517744491/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001608,"da-nang","ns","Квартира",19000000,None,
  "2-спальная квартира, Tuy Lý Vương, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/1454201286459382/posts/1574681351078041/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="2-bedroom flat, Tuy Lý Vương, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1574681351078041/01.webp", "assets/fb_photos/1574681351078041/02.webp", "assets/fb_photos/1574681351078041/03.webp", "assets/fb_photos/1574681351078041/04.webp", "assets/fb_photos/1574681351078041/05.webp"], "am": ["w"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001609,"da-nang","ah","Квартира",12000000,None,
  "Квартира, Nguyễn Thiện Kế, An Hải.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1488716350088015/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="Flat, Nguyễn Thiện Kế, An Hải.",
  details={"photos": ["assets/fb_photos/1488716350088015/01.webp", "assets/fb_photos/1488716350088015/02.webp", "assets/fb_photos/1488716350088015/03.webp", "assets/fb_photos/1488716350088015/04.webp", "assets/fb_photos/1488716350088015/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001610,"hue","acu","Студия",5000000,32,
  "Студия, 32 м², An Cựu.",
  "https://www.facebook.com/groups/phongtrosvhue/posts/1676192456923396/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="Studio, 32 m², An Cựu.",
  details={"photos": ["assets/fb_photos/1676192456923396/01.webp", "assets/fb_photos/1676192456923396/02.webp", "assets/fb_photos/1676192456923396/03.webp", "assets/fb_photos/1676192456923396/04.webp", "assets/fb_photos/1676192456923396/05.webp"], "am": ["w", "k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001611,"nha-trang","vp","Квартира",15000000,38,
  "Квартира, 38 м², Vĩnh Phước.",
  "https://www.facebook.com/groups/chothue79/posts/4622243491378505/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="Flat, 38 m², Vĩnh Phước.",
  details={"photos": ["assets/fb_photos/4622243491378505/01.webp", "assets/fb_photos/4622243491378505/02.webp", "assets/fb_photos/4622243491378505/03.webp", "assets/fb_photos/4622243491378505/04.webp", "assets/fb_photos/4622243491378505/05.webp"], "am": ["w", "b", "lift"], "fl": 3, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001612,"nha-trang","ph","Квартира",18000000,40,
  "1-спальная квартира, 40 м², Phước Hải.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2722683684830573/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="1-bedroom flat, 40 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/2722683684830573/01.webp", "assets/fb_photos/2722683684830573/02.webp", "assets/fb_photos/2722683684830573/03.webp", "assets/fb_photos/2722683684830573/04.webp", "assets/fb_photos/2722683684830573/05.webp"], "am": ["b"], "fl": 4, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001613,"nha-trang","ph","Квартира",15000000,40,
  "1-спальная квартира, 40 м², Phước Hải.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2719042408528034/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="1-bedroom flat, 40 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/2719042408528034/01.webp", "assets/fb_photos/2719042408528034/02.webp", "assets/fb_photos/2719042408528034/03.webp", "assets/fb_photos/2719042408528034/04.webp", "assets/fb_photos/2719042408528034/05.webp"], "am": ["w", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001614,"nha-trang","ntr","Студия",12000000,45,
  "Студия, 45 м², Nam Nha Trang — 1 санузел.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1981650005864100/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="Studio, 45 m², Nam Nha Trang — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1981650005864100/01.webp", "assets/fb_photos/1981650005864100/02.webp", "assets/fb_photos/1981650005864100/03.webp", "assets/fb_photos/1981650005864100/04.webp", "assets/fb_photos/1981650005864100/05.webp"], "am": ["k", "lift", "pool"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001615,"nha-trang","ph","Квартира",20000000,80,
  "3-спальная квартира, 80 м², Phước Hải — 2 санузла.",
  "https://www.facebook.com/groups/2253829621529798/posts/4732237407022328/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="3-bedroom flat, 80 m², Phước Hải — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/4732237407022328/01.webp", "assets/fb_photos/4732237407022328/02.webp", "assets/fb_photos/4732237407022328/03.webp", "assets/fb_photos/4732237407022328/04.webp", "assets/fb_photos/4732237407022328/05.webp"], "am": ["pool", "gym"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001616,"nha-trang","btr","Дом",30000000,200,
  "2-спальный дом, 200 м², Bắc Nha Trang — 1 санузел.",
  "https://www.facebook.com/groups/1172766863380743/posts/2095436347780452/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="2-bedroom house, 200 m², Bắc Nha Trang — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2095436347780452/01.webp", "assets/fb_photos/2095436347780452/02.webp", "assets/fb_photos/2095436347780452/03.webp", "assets/fb_photos/2095436347780452/04.webp", "assets/fb_photos/2095436347780452/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001617,"nha-trang","lt","Студия",8500000,25,
  "Студия, 25 м², Lộc Thọ.",
  "https://www.facebook.com/groups/1172766863380743/posts/2095448704445883/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="Studio, 25 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/2095448704445883/01.webp", "assets/fb_photos/2095448704445883/02.webp", "assets/fb_photos/2095448704445883/03.webp", "assets/fb_photos/2095448704445883/04.webp", "assets/fb_photos/2095448704445883/05.webp"], "am": ["w", "win", "lift"], "fl": 4, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001618,"nha-trang","vh","Дом",20000000,None,
  "3-спальный дом, Vĩnh Hải — 2 санузла.",
  "https://www.facebook.com/groups/1172766863380743/posts/2095404804450273/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="3-bedroom house, Vĩnh Hải — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/2095404804450273/01.webp", "assets/fb_photos/2095404804450273/02.webp", "assets/fb_photos/2095404804450273/03.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001619,"nha-trang","btr","Квартира",23000000,100,
  "2-спальная квартира, 100 м², Bắc Nha Trang — 1 санузел.",
  "https://www.facebook.com/groups/849441571863086/posts/3847261448747735/","сегодня",0,source="fbgroup",postedOn="2026-09-28",
  descEn="2-bedroom flat, 100 m², Bắc Nha Trang — 1 bathroom.",
  details={"photos": ["assets/fb_photos/3847261448747735/01.webp", "assets/fb_photos/3847261448747735/02.webp", "assets/fb_photos/3847261448747735/03.webp", "assets/fb_photos/3847261448747735/04.webp", "assets/fb_photos/3847261448747735/05.webp"], "am": ["k", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
