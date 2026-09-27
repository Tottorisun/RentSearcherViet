# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 14 строк, 2026-09-27.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 1451533241829065/4569058646743160 -- can-tho/nki, 5,500,000 VND: район назван в адресе поста
  * 1735327053393688/4552676971658668 -- cebu/man, 30,000 PHP: район назван в адресе поста
  * chothuecanhodanang43/1746041937052115 -- da-nang/ns, 12,000,000 VND: «1-BEDROOM APARTMENT FOR RENT»: 2 строк сайта, все в ns
  * chothuecanhodanang43/1746023073720668 -- da-nang/hx, 8,500,000 VND: район назван в посте
  * canhochothuedanangtot/2233882067239452 -- da-nang/ns, 14,000,000 VND: улица Bà Huyện Thanh Quan: 5 из 5 отрезков в ns
  * phongtrocanhonhadanang/1487288543564129 -- da-nang/ns, 8,000,000 VND: район назван в посте; «APARTMENT FOR RENT»: 2 строк сайта, все в ns
  * 153191128587086/2245260889380089 -- dumaguete/val, 28,000 PHP: район назван в адресе поста
  * 153191128587086/2246072355965609 -- dumaguete/jnb, 25,000 PHP: район назван в адресе поста
  * 849441571863086/3846906242116589 -- nha-trang/btr, 12,000,000 VND: район назван в адресе поста
  * 849441571863086/3845481628925717 -- nha-trang/lt, 8,000,000 VND: район назван в адресе поста
  * 849441571863086/3845510235589523 -- nha-trang/ph2, 11,000,000 VND: район назван в адресе поста
  * 849441571863086/3846286742178539 -- nha-trang/lt, 11,000,000 VND: район назван в адресе поста
  * 849441571863086/3845656285574918 -- nha-trang/pl, 6,000,000 VND: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1116057517534803 -- nha-trang/pl, 25,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (263):
  * 3474885602689740 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 3496639880514312 -- район не определяется по адресу «Giá chỉ 5»
  * 3501758010002499 -- район не определяется по адресу «Nest5 Home»
  * 3121633828039610 -- район не определяется по адресу «☘️☘️ CHO THUÊ CHUNG CƯ HOÀNG ANH GIA LAI»
  * 3111524002383926 -- это поиск жилья, а не предложение
  * 3086171178252542 -- район не определяется по адресу «Studio siêu đẹp»
  * 3059192510950409 -- тип жилья в тексте не назван
  * 3017264535143207 -- в посте несколько разных цен: 7,000,000, 7,500,000
  * 2730478847155112 -- помещение под бизнес или здание целиком, а не жильё
  * 1757290509336915 -- цена 650,000 VND вне разумных пределов
  * 1725575419175091 -- тип жилья в тексте не назван
  * 1725714562494510 -- район не определяется по адресу «Chủ gửi»
  * 1761788175553815 -- тип жилья в тексте не назван
  * 1763351818730784 -- тип жилья в тексте не назван
  * 4534963593485999 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 4535108773471481 -- район не определяется по адресу «Chủ gửi»
  * 4524078787907813 -- район не определяется по адресу «GIÁ THUÊ : 2.7 TRIỆU»
  * 4547172472265111 -- тот же текст уже заведён: id 3001175
  * 4578192675829757 -- район не определяется по адресу «🥨🫜🍒 CĂN HỘ CAO CẤP MỚI XÂY KDC AN KHÁNH FULL NỘI T»
  * 4576672325981792 -- район не определяется по адресу «🛍️🎀 PHÒNG FULL NỘI THẤT CÓ BAN CÔNG ĐƯỜNG HOÀNG QU»
  * 4569057556743269 -- в посте несколько разных цен: 4,850,000, 9,700,000
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
  * 28168081102890649 -- район не определяется по адресу «Galleria Residences Tower 2»
  * 28154568060908620 -- район не определяется по адресу «FOR RENT»
  * 28147798434918916 -- район не определяется по адресу «ROOM FOR RENT»
  * 28166579659707460 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 28153984027633690 -- в посте несколько разных цен: 13,000, 15,000
  * 28142531495445610 -- в тексте есть и другая цена того же порядка: 3,625 против 5,000
  * 28085902431108517 -- продажа
  * 28129154990116594 -- уже на сайте: id 3001449
  * 28609811225348981 -- ищут соседа, а не сдают
  * 28623363410660429 -- в посте несколько разных цен: 3,000, 15,000
  * 28582610778069026 -- тот же текст уже заведён: id 3001116
  * 28596429580020479 -- район не определяется по адресу «SEMI- FURNISHED HOUSE FOR RENT‼️ UP AND DOWN - LAB»
  * 28647135941616509 -- район не определяется по адресу «New Apartment for rent ♥️»
  * 28428011576862281 -- район не определяется по адресу «‼️House for rent in cabancalan»
  * 28558508677145903 -- район не определяется по адресу «APARTMENT FOR RENT»
  * 28635157646147672 -- район не определяется по адресу «ROOM FOR RENT (LADIES ONLY)»
  * 28648204168176353 -- уже на сайте: id 3001450
  * 2384022142137333 -- район не определяется по адресу «EL ORLANDO VILLAGE»
  * 2384258058780408 -- район не определяется по адресу «ROOM FOR RENT: FEMALE ONLY 4K»
  * 2388233741716173 -- район не определяется по адресу «New Apartment for rent ♥️»
  * 2386742698531944 -- это поиск жилья, а не предложение
  * 2386750458531168 -- район не определяется по адресу «ROOM FOR RENT (LADIES ONLY)»
  * 4555728451353520 -- тип жилья в тексте не назван
  * 4553647301561635 -- район не определяется по адресу «HOUSE FOR RENT ‼️ ALMIYA SUBDIVISION»
  * 4555775611348804 -- это поиск жилья, а не предложение
  * 4557081944551504 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4521497431443289 -- район не определяется по адресу «Bulacao Luyo Prince Warehouse»
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
  * 1648727443062647 -- район не определяется: «CHO THUÊ NHÀ 3 TẦNG, MẶT TIỀN TRƯNG NỮ VƯƠNG, ĐÀ NẴNG»
  * 1643178526950872 -- в посте несколько разных цен: 25,000,000, 27,000,000
  * 1395964762747313 -- уже на сайте: id 3001451
  * 1395720109438445 -- уже на сайте: id 3001452
  * 1395740982769691 -- уже на сайте: id 3001453
  * 1389904863353303 -- район не определяется: «CHO THUÊ PHÒNG P302, TRƯƠNG CÔNG HY, ĐÀ NẴNG»
  * 1394116689598787 -- нет ни одной скачанной фотографии
  * 1388166273527162 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000
  * 1487114080248242 -- район не определяется: «🌷CHÍNH CHỦ CHO THUÊ CĂN HỘ NEW 100% - PHAN HUỲNH ĐIỂU»
  * 1476237824669201 -- в посте несколько разных цен: 8,000,000, 9,000,000
  * 1485169163776067 -- район не определяется: «1-BEDROOM, APARTMENT FOR RENT, SON TRA»
  * 1486233807002936 -- уже на сайте: id 3001454
  * 1487160270243623 -- уже на сайте: id 3001455
  * 1487162310243419 -- уже на сайте: id 3001456
  * 1485327343760249 -- похоже на уже заведённое: id 1011635
  * 1486318753661108 -- район не определяется: «FULLY FURNISHED 1- BEDROOM APARTMENT, SON TRA, FLEXIBLE LEASE TERMS»
  * 1486578613635122 -- район ns не входит в прежний район Son Tra из поста
  * 1486327023660281 -- уже на сайте: id 3001457
  * 2977953042598773 -- район не определяется: «chung cư HAGL - 72 Hàm Nghi, HAGL Apartment - 72 Hàm Nghi, the city center»
  * 2979465262447551 -- район не определяется: «**STUDIO APARTMENT FOR RENT, MAN THAI, SON TRA»
  * 2979444759116268 -- район не определяется: «**1-BEDROOM APARTMENT FOR RENT, SON TRA, DA NANG**»
  * 2979429565784454 -- в посте несколько разных цен: 15,000,000, 17,000,000
  * 2977062496021161 -- район не определяется: «CHO THUÊ CĂN HỘ CAO CẤP HYORI, ĐÀ NẴNG, HYORI PREMIUM 2-BEDROOM APARTMENT FOR RENT»
  * 2977992425928168 -- район не определяется: «1-Bedroom Apartment in Son Tra Area, Ha Ky Ngo Street, just 3 minutes from the beach...»
  * 1573221624557347 -- в посте несколько разных цен: 750,000, 15,000,000
  * 1573499174529592 -- район не определяется: «**STUDIO APARTMENT FOR RENT, MAN THAI, SON TRA»
  * 1573443281201848 -- район не определяется: «Son Tra District, Da Nang, 1-BEDROOM APARTMENT FOR RENT IN SON TRA DISTRICT»
  * 1566696508543192 -- район не определяется: «Looking for an apartment in the FPT area, Da Nang, Tìm thuê căn hộ tại khu vực FPT»
  * 1570473774832132 -- это поиск жилья, а не предложение
  * 1571298261416350 -- это поиск жилья, а не предложение
  * 1572175604661949 -- это поиск жилья, а не предложение
  * 1573289111217265 -- тот же текст уже заведён: id 3001491
  * 1568526158360227 -- это поиск жилья, а не предложение
  * 1559381239274719 -- это поиск жилья, а не предложение
  * 1567479671798209 -- цены в посте нет
  * 2352783798893300 -- тот же текст уже заведён: id 3001492
  * 2353178895520457 -- в посте несколько разных цен: 10,000,000, 11,500,000, 12,500,000, 14,000,000
  * 2352213162283697 -- тип жилья в тексте не назван
  * 1746627713660204 -- в посте несколько разных цен: 11,500,000, 13,500,000, 14,000,000
  * 1746240140365628 -- источники назвали разные районы: precedent=ns, ward=hx
  * 1745873907068918 -- в посте несколько разных цен: 6,500,000, 369,745,619
  * 1746080637048245 -- район не определяется: «Hoa Son (Quiet, peaceful & ultra-serene neighborhood), 🌊 BRAND NEW ULTRA-LUXURY 1-BEDROOM APARTMENT FOR RENT»
  * 2226949671266025 -- район не определяется: «Apartment Highlights:, Prime Location, Lý Đạo Thành Street:»
  * 2229982960962696 -- улица Xô Viết Nghệ Tĩnh идёт через несколько районов (hcg 24, cl2 17), а пост называет только прежний район Hai Chau
  * 2230754917552167 -- улица Nguyễn Chánh идёт через несколько районов (lc 13, hk 5), а пост называет только прежний район Lien Chieu
  * 2232654177362241 -- район не определяется: «BRAND-NEW 1-BEDROOM APARTMENT FOR RENT, AN THUONG, An Thuong area»
  * 2232022014092124 -- нет ни одной скачанной фотографии
  * 2230071360953856 -- тип жилья в тексте не назван
  * 2229842037643455 -- в посте несколько разных цен: 8,000,000, 12,000,000, 14,000,000, 15,000,000
  * 2231605974133728 -- улица Phạm Vấn идёт через несколько районов (ah 1, st 1), а пост называет только прежний район Son Tra
  * 1477203231239327 -- район не определяется: «Brand-new house for rent: 4 floors, 4 bedrooms, 6 bathrooms»
  * 1488120813480902 -- в посте несколько разных цен: 11,000,000, 14,000,000
  * 2246160629290115 -- район не определяется по адресу «May I ask permission to post Admin.»
  * 2244714546101390 -- район не определяется по адресу «House for rent with swimming pool»
  * 2246076275965217 -- район не определяется по адресу «Taclobo»
  * 2231309210775257 -- район не определяется по адресу «HOUSE FEATURES»
  * 2245287132710798 -- в посте несколько разных цен: 15,000, 22,000
  * 2240689496503895 -- тип жилья в тексте не назван
  * 2288508075095582 -- нет ни одной скачанной фотографии
  * 2275943409685382 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2274703299809393 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2273544739925249 -- район не определяется по адресу «670 Đường Kim Giang ( Show room Vinfast )»
  * 2251798492099874 -- помещение под бизнес или здание целиком, а не жильё
  * 1105631969126482 -- в посте несколько разных цен: 4,000,000, 6,000,000
  * 1084124464610566 -- тот же текст уже заведён: id 3001364
  * 4523309137920242 -- район не определяется по адресу «HH426 Cho thuê chung cư Hoàng Huy commerce - Tòa L»
  * 4518708065047016 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 4522187834699039 -- район не определяется по адресу «Cho thuê căn hộ Penthouse 1 ngủ tách bếp to rộng t»
  * 4514430372141452 -- это поиск жилья, а не предложение
  * 3868029470004828 -- район не определяется по адресу «[EN BELOW] 10»
  * 1865296498122406 -- похоже на уже заведённое: id 3001056
  * 1863473498304706 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1858166655502057 -- тип жилья в тексте не назван
  * 1865425554776167 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1858110785507644 -- похоже на уже заведённое: id 1006401
  * 1957829645293457 -- тот же текст уже заведён: id 3001493
  * 1972539347155820 -- тип жилья в тексте не назван
  * 1972443553832066 -- в посте несколько разных цен: 6,000,000, 30,000,000
  * 1970229000720188 -- район не определяется по адресу «Apartment Details»
  * 1969269510816137 -- район не определяется по адресу «Nguyễn Bỉnh Khiêm»
  * 1972485960494492 -- тот же текст уже заведён: id 3001494
  * 1972486703827751 -- тот же текст уже заведён: id 3001495
  * 1987516638597971 -- район не определяется по адресу «Trảng Kèo 8»
  * 1984287965587505 -- нет ни одной скачанной фотографии
  * 1995042774512024 -- район не определяется по адресу «15tr/tháng hd dài hạn có tl»
  * 1982926145723687 -- в посте несколько разных цен: 4,500,000, 5,000,000
  * 2020629845282065 -- район не определяется по адресу «✨ Modern 1-Bedroom Apartment for Rent in Central H»
  * 2020348438643539 -- район не определяется по адресу «House details:»
  * 2006764370001946 -- район не определяется по адресу «HOUSE FOR RENT IN CAM THANH»
  * 2020257518652631 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 2020537728624610 -- район не определяется по адресу «a non-flooding area»
  * 1692451368630838 -- тип жилья в тексте не назван
  * 1708277650381543 -- район не определяется по адресу «CHO THUÊ STUDIO CAO CẤP»
  * 1701057297770245 -- в посте несколько разных цен: 3,600,000, 3,700,000, 3,800,000
  * 1637646127444696 -- район не определяется по адресу «Không gian sống hiện đại»
  * 1251745672701412 -- в посте несколько разных цен: 4,000,000, 4,500,000, 4,800,000
  * 1287853898988310 -- в тексте есть и другая цена того же порядка: 4,568,736 против 4,000,000
  * 1507435977585140 -- в посте несколько разных цен: 500,000, 600,000
  * 1506528094342595 -- тип жилья в тексте не назван
  * 1499726755022729 -- в посте несколько разных цен: 500,000, 600,000
  * 28743681078600659 -- тип жилья в тексте не назван
  * 28799717366330363 -- тот же текст уже заведён: id 3001497
  * 28803924852576281 -- в тексте есть и другая цена того же порядка: 8,838 против 12,000
  * 28802420006060099 -- тот же текст уже заведён: id 3001498
  * 28670036715965096 -- район не определяется по адресу «Tejeron St. cor. Pedro Gil St.»
  * 28789190557383044 -- рассрочка
  * 28394381120197325 -- район не определяется по адресу «PTPA»
  * 28787966574172109 -- тот же текст уже заведён: id 3001499
  * 2594623547648398 -- район не определяется по адресу «HOUSE & LOT FOR RENT»
  * 2588553684922051 -- тот же текст уже заведён: id 3001500
  * 2594674554309964 -- район не определяется по адресу «16»
  * 2592293024548117 -- тип жилья в тексте не назван
  * 2594278631016223 -- район не определяется по адресу «*** Fully Furnished unit for Rent ***»
  * 2594272364350183 -- тип жилья в тексте не назван
  * 2593006787810074 -- тип жилья в тексте не назван
  * 2594713960972690 -- тип жилья в тексте не назван
  * 2586424258468327 -- район не определяется по адресу «the 17th floor»; прецедент расколот: «Uptown»: bgc 1
  * 2591368297973923 -- район не определяется по адресу «Dominga St.»
  * 4623191777950343 -- уже на сайте: id 3001458
  * 4619187528350768 -- в посте несколько разных цен: 500,000, 12,500,000
  * 4620269678242553 -- нет ни одной скачанной фотографии
  * 4623182901284564 -- район не определяется по адресу «1 separate bedroom»
  * 4622251358044385 -- уже на сайте: id 3001459
  * 4615612555374932 -- район не определяется по адресу «Muong Thanh 04 Tran Phu»
  * 4617186755217512 -- это поиск жилья, а не предложение
  * 4618707241732130 -- нет ни одной скачанной фотографии
  * 4615648422038012 -- район не определяется по адресу «LUXURY 3-BEDROOM APARTMENT FOR RENT»; прецедент расколот: «GOLDCOAST»: lt 1
  * 4611904355745752 -- нет ни одной скачанной фотографии
  * 2712281229204152 -- район не определяется по адресу «136m²/floor - 5m wide with parking space»; прецедент расколот: «Mac Dinh Chi»: nt 1
  * 2714520092313599 -- в посте несколько разных цен: 1,000,000, 10,000,000
  * 2720806041685004 -- район не определяется по адресу «City center»
  * 2719901165108825 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2720297438402531 -- в тексте есть и другая цена того же порядка: 8,580,887 против 25,000,000
  * 2719655501800058 -- уже на сайте: id 3001460
  * 2720750971690511 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2720321525066789 -- район не определяется по адресу «NT RENT»
  * 2720674205031521 -- уже на сайте: id 3001461
  * 2720776721687936 -- район не определяется по адресу «40m² - Balcony available»
  * 1981099679252466 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1974105989951835 -- тип жилья в тексте не назван
  * 1980800452615722 -- район не определяется по адресу «CHO THUÊ NHÀ 3 TẦNG»
  * 1975747079787726 -- в тексте есть и другая цена того же порядка: 85,845,478 против 68,000,000
  * 1978364799525954 -- похоже на уже заведённое: id 3001282
  * 1979076319454802 -- район не определяется по адресу «Phước Tiến - Trung tâm thành phố»
  * 1968092573886510 -- тот же текст уже заведён: id 3001235
  * 1968292877199813 -- район не определяется по адресу «Cho Thuê Nhà đường Thích Quảng Đức»
  * 4730842770495125 -- в посте несколько разных цен: 500,000, 14,000,000
  * 4729178327328236 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4730811993831536 -- в посте несколько разных цен: 1,000,000, 18,000,000
  * 4730653110514091 -- район не определяется по адресу «Bustling residential area near the city center»
  * 4730550950524307 -- район не определяется по адресу «with airy windows»
  * 4727773037468765 -- район не определяется по адресу «South Nha Trang»
  * 4729295160649886 -- район не определяется по адресу «PARAMOUNT APARTMENT FOR RENT»
  * 2093336394657114 -- район не определяется по адресу «City center»
  * 2092650078059079 -- в посте несколько разных цен: 660,000, 700,000, 1,000,000, 15,000,000
  * 2092889218035165 -- в тексте есть и другая цена того же порядка: 8,580,887 против 25,000,000
  * 2092360064754747 -- район не определяется по адресу «side a modern urban area»
  * 2090555578268529 -- в посте несколько разных цен: 530,000, 20,000,000
  * 3837694026371144 -- район не определяется по адресу «2 bedrooms»
  * 3844860945654452 -- тот же текст уже заведён: id 3001416
  * 3846876995452847 -- район не определяется по адресу «3 tầng»
  * 3838846259589254 -- в посте несколько разных цен: 14,500,000, 15,500,000
  * 3845948588879021 -- район не определяется по адресу «Bustling residential area near the city center»
  * 1116292897511265 -- в посте несколько разных цен: 500,000, 14,000,000
  * 1116393200834568 -- район не определяется по адресу «NT RENT»
  * 1114003031073585 -- район не определяется по адресу «South Nha Trang»
  * 1116838927456662 -- район не определяется по адресу «**Khanh Hoa»
  * 1116293970844491 -- район не определяется по адресу «NT RENT»
  * 1116228750851013 -- район не определяется по адресу «**Khanh Hoa»
  * 2072146586952776 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2073488746818560 -- нет ни одной скачанной фотографии
  * 2057506045083497 -- в посте несколько разных цен: 15,500,000, 16,000,000
  * 1763318494880834 -- район не определяется по адресу «CHO THUÊ VILLA PALM GARDEN»
  * 1769689764243707 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1768081234404560 -- тот же текст уже заведён: id 3001198
  * 1764181028127914 -- адрес называет несколько районов: ath, dto
  * 1756168655595818 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2599789720441683 -- тот же текст уже заведён: id 3001198
  * 2599927840427871 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2586447371775918 -- помещение под бизнес или здание целиком, а не жильё
  * 2588243598262962 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2585080565245932 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 2592618517825470 -- район не определяется по адресу «✨ Brand-new villa»
  * 5551917961699508 -- район не определяется по адресу «2BR»
  * 5551876498370321 -- район не определяется по адресу «28 Nguyễn Huệ»
  * 5550361121855192 -- район не определяется по адресу «studio layout featuring 2 beds»
  * 5551753641715940 -- район не определяется по адресу «Vị trí trung tâm Quy Nhơn»
  * 5546593298898641 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 3288974787980281 -- район не определяется по адресу «⭐️ Cho Thuê Căn Hộ ALTARA RESIDENCE»
  * 3288882517989508 -- район не определяется по адресу «studio layout featuring 2 beds»
  * 3290024791208614 -- район не определяется по адресу «Vị trí trung tâm Quy Nhơn»
  * 3290133441197749 -- район не определяется по адресу «2BR»
  * 3285077928369967 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 1479503063993762 -- район не определяется по адресу «AIRIA VUNG TAU»
  * 1476872604256808 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
"""
from listing_lock import insert_listings

IDS = [3001524, 3001525, 3001526, 3001527, 3001528, 3001529, 3001530, 3001531, 3001532, 3001533, 3001534, 3001535, 3001536, 3001537]

NEW_SRC = r'''
L(3001524,"can-tho","nki","Студия",5500000,26,
  "Студия, 26 м², Ninh Kiều.",
  "https://www.facebook.com/groups/1451533241829065/posts/4569058646743160/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="Studio, 26 m², Ninh Kiều.",
  details={"photos": ["assets/fb_photos/4569058646743160/01.webp", "assets/fb_photos/4569058646743160/02.webp", "assets/fb_photos/4569058646743160/03.webp", "assets/fb_photos/4569058646743160/04.webp", "assets/fb_photos/4569058646743160/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001525,"cebu","man","Дом",30000,None,
  "4-спальный дом, Mandaue.",
  "https://www.facebook.com/groups/1735327053393688/posts/4552676971658668/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-27",
  descEn="4-bedroom house, Mandaue.",
  details={"photos": ["assets/fb_photos/4552676971658668/01.webp", "assets/fb_photos/4552676971658668/02.webp", "assets/fb_photos/4552676971658668/03.webp", "assets/fb_photos/4552676971658668/04.webp", "assets/fb_photos/4552676971658668/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001526,"da-nang","ns","Квартира",12000000,None,
  "1-спальная квартира, APARTMENT FOR RENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1746041937052115/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="1-bedroom flat, APARTMENT FOR RENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1746041937052115/01.webp", "assets/fb_photos/1746041937052115/02.webp", "assets/fb_photos/1746041937052115/03.webp", "assets/fb_photos/1746041937052115/04.webp", "assets/fb_photos/1746041937052115/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001527,"da-nang","hx","Студия",8500000,38,
  "Студия, 38 м², FULLY FURNISHED STUDIO APARTMENT FOR RENT, Hòa Xuân.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1746023073720668/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="Studio, 38 m², FULLY FURNISHED STUDIO APARTMENT FOR RENT, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1746023073720668/01.webp", "assets/fb_photos/1746023073720668/02.webp", "assets/fb_photos/1746023073720668/03.webp", "assets/fb_photos/1746023073720668/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001528,"da-nang","ns","Квартира",14000000,None,
  "Квартира, Bà Huyện Thanh Quan, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2233882067239452/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="Flat, Bà Huyện Thanh Quan, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2233882067239452/01.webp", "assets/fb_photos/2233882067239452/02.webp", "assets/fb_photos/2233882067239452/03.webp", "assets/fb_photos/2233882067239452/04.webp", "assets/fb_photos/2233882067239452/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001529,"da-nang","ns","Квартира",8000000,40,
  "Квартира, 40 м², APARTMENT FOR RENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1487288543564129/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="Flat, 40 m², APARTMENT FOR RENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1487288543564129/01.webp", "assets/fb_photos/1487288543564129/02.webp", "assets/fb_photos/1487288543564129/03.webp", "assets/fb_photos/1487288543564129/04.webp", "assets/fb_photos/1487288543564129/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001530,"dumaguete","val","Дом",28000,None,
  "2-спальный дом, Valencia — 1 санузел.",
  "https://www.facebook.com/groups/153191128587086/posts/2245260889380089/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-27",
  descEn="2-bedroom house, Valencia — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2245260889380089/01.webp", "assets/fb_photos/2245260889380089/02.webp", "assets/fb_photos/2245260889380089/03.webp", "assets/fb_photos/2245260889380089/04.webp", "assets/fb_photos/2245260889380089/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001531,"dumaguete","jnb","Дом",25000,None,
  "2-спальный дом, Junob — 1 санузел.",
  "https://www.facebook.com/groups/153191128587086/posts/2246072355965609/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-27",
  descEn="2-bedroom house, Junob — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2246072355965609/01.webp", "assets/fb_photos/2246072355965609/02.webp", "assets/fb_photos/2246072355965609/03.webp", "assets/fb_photos/2246072355965609/04.webp", "assets/fb_photos/2246072355965609/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001532,"nha-trang","btr","Квартира",12000000,32,
  "Квартира, 32 м², Bắc Nha Trang.",
  "https://www.facebook.com/groups/849441571863086/posts/3846906242116589/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="Flat, 32 m², Bắc Nha Trang.",
  details={"photos": ["assets/fb_photos/3846906242116589/01.webp", "assets/fb_photos/3846906242116589/02.webp", "assets/fb_photos/3846906242116589/03.webp", "assets/fb_photos/3846906242116589/04.webp", "assets/fb_photos/3846906242116589/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001533,"nha-trang","lt","Квартира",8000000,30,
  "Квартира, 30 м², Lộc Thọ.",
  "https://www.facebook.com/groups/849441571863086/posts/3845481628925717/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="Flat, 30 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/3845481628925717/01.webp", "assets/fb_photos/3845481628925717/02.webp", "assets/fb_photos/3845481628925717/03.webp", "assets/fb_photos/3845481628925717/04.webp", "assets/fb_photos/3845481628925717/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001534,"nha-trang","ph2","Квартира",11000000,30,
  "Квартира, 30 м², Phước Hòa.",
  "https://www.facebook.com/groups/849441571863086/posts/3845510235589523/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="Flat, 30 m², Phước Hòa.",
  details={"photos": ["assets/fb_photos/3845510235589523/01.webp", "assets/fb_photos/3845510235589523/02.webp", "assets/fb_photos/3845510235589523/03.webp", "assets/fb_photos/3845510235589523/04.webp", "assets/fb_photos/3845510235589523/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001535,"nha-trang","lt","Квартира",11000000,30,
  "Квартира, 30 м², Lộc Thọ.",
  "https://www.facebook.com/groups/849441571863086/posts/3846286742178539/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="Flat, 30 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/3846286742178539/01.webp", "assets/fb_photos/3846286742178539/02.webp", "assets/fb_photos/3846286742178539/03.webp", "assets/fb_photos/3846286742178539/04.webp", "assets/fb_photos/3846286742178539/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001536,"nha-trang","pl","Квартира",6000000,30,
  "1-спальная квартира, 30 м², Phước Long.",
  "https://www.facebook.com/groups/849441571863086/posts/3845656285574918/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="1-bedroom flat, 30 m², Phước Long.",
  details={"photos": ["assets/fb_photos/3845656285574918/01.webp", "assets/fb_photos/3845656285574918/02.webp", "assets/fb_photos/3845656285574918/03.webp", "assets/fb_photos/3845656285574918/04.webp", "assets/fb_photos/3845656285574918/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001537,"nha-trang","pl","Дом",25000000,None,
  "4-спальный дом, Phước Long — 5 санузлов.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1116057517534803/","сегодня",0,source="fbgroup",postedOn="2026-09-27",
  descEn="4-bedroom house, Phước Long — 5 bathrooms.",
  details={"photos": ["assets/fb_photos/1116057517534803/01.webp", "assets/fb_photos/1116057517534803/02.webp", "assets/fb_photos/1116057517534803/03.webp", "assets/fb_photos/1116057517534803/04.webp", "assets/fb_photos/1116057517534803/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
