# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 13 строк, 2026-09-26.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * rentcebu/28129154990116594 -- cebu/bnl, 15,000 PHP: район назван в адресе поста
  * cebu.tambayan.2/28648204168176353 -- cebu/tlm, 17,000 PHP: район назван в адресе поста
  * 728946289449167/1395964762747313 -- da-nang/ah, 9,500,000 VND: район назван в посте
  * 728946289449167/1395720109438445 -- da-nang/cl2, 6,000,000 VND: улица Bàu Tràm Trung: 1 из 1 отрезков в cl2
  * 728946289449167/1395740982769691 -- da-nang/ns, 5,500,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * phongtrocanhonhadanang/1486233807002936 -- da-nang/ns, 12,000,000 VND: район назван в посте
  * phongtrocanhonhadanang/1487160270243623 -- da-nang/ns, 14,000,000 VND: прежний район Ngu Hanh Son весь вошёл в этот; улица Trương Quang Được: 1 из 1 отрезков в ns; пост: Ngu Hanh Son
  * phongtrocanhonhadanang/1487162310243419 -- da-nang/ns, 10,000,000 VND: район назван в посте; прежний район Ngu Hanh Son весь вошёл в этот; улица An Thượng 32: 1 из 1 отрезков в ns; пост: Ngu Hanh Son
  * phongtrocanhonhadanang/1486327023660281 -- da-nang/ns, 10,000,000 VND: район назван в посте; улица Nguyễn Đình Chiểu: 4 из 4 отрезков в ns
  * chothue79/4623191777950343 -- nha-trang/vn, 14,000,000 VND: район назван в адресе поста
  * chothue79/4622251358044385 -- nha-trang/ph2, 12,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2719655501800058 -- nha-trang/lt, 14,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2720674205031521 -- nha-trang/ph, 14,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (257):
  * 2672374729880903 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 2671323069986069 -- район не определяется по адресу «one of Buôn Ma Thuột's most secure and pristine ur»
  * 2168691324070411 -- район не определяется по адресу «one of Buôn Ma Thuột's most secure and pristine ur»
  * 2170210010585209 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 2182552376017639 -- это поиск жилья, а не предложение
  * 2185082292431314 -- нет ни одной скачанной фотографии
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
  * 1828615444805775 -- район не определяется по адресу «Avida Towers Cebu»
  * 1831468591187127 -- район не определяется по адресу «Cardinal Rosales Ave»
  * 1829954228005230 -- район не определяется по адресу «HOUSE FOR RENT IN AJOYA»
  * 1830943177906335 -- в тексте есть и другая цена того же порядка: 3,625 против 5,000
  * 1829677238032929 -- в посте несколько разных цен: 12,000, 18,000
  * 1831961487804504 -- уже на сайте: id 3001361
  * 1831943547806298 -- район не определяется по адресу «ROOM FOR RENT (LADIES ONLY)»
  * 1826420871691899 -- в посте несколько разных цен: 18,000, 25,000
  * 1825901171743869 -- в тексте есть и другая цена того же порядка: 13,430 против 16,500
  * 1821535598847093 -- в тексте есть и другая цена того же порядка: 15,000 против 17,000
  * 1828052141528772 -- в посте несколько разных цен: 4,500, 80,000
  * 2130933830873212 -- это поиск жилья, а не предложение
  * 2130824454217483 -- район не определяется по адресу «ROOM FOR RENT - ₱4»
  * 2130706907562571 -- район не определяется по адресу «ROOM FOR RENT»
  * 2129515557681706 -- уже на сайте: id 3001362
  * 2131553427477919 -- в посте несколько разных цен: 7,000, 7,500
  * 2127422497891012 -- район не определяется по адресу «UBCA 2 QUIOT PARDO CEBU CITY»
  * 28168081102890649 -- район не определяется по адресу «Galleria Residences Tower 2»
  * 28154568060908620 -- район не определяется по адресу «FOR RENT»
  * 28147798434918916 -- район не определяется по адресу «ROOM FOR RENT»
  * 28166579659707460 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 28153984027633690 -- в посте несколько разных цен: 13,000, 15,000
  * 28142531495445610 -- в тексте есть и другая цена того же порядка: 3,625 против 5,000
  * 28085902431108517 -- продажа
  * 28609811225348981 -- ищут соседа, а не сдают
  * 28623363410660429 -- в посте несколько разных цен: 3,000, 15,000
  * 28582610778069026 -- тот же текст уже заведён: id 3001116
  * 28596429580020479 -- район не определяется по адресу «SEMI- FURNISHED HOUSE FOR RENT‼️ UP AND DOWN - LAB»
  * 28647135941616509 -- район не определяется по адресу «New Apartment for rent ♥️»
  * 28428011576862281 -- район не определяется по адресу «‼️House for rent in cabancalan»
  * 28558508677145903 -- район не определяется по адресу «APARTMENT FOR RENT»
  * 28635157646147672 -- район не определяется по адресу «ROOM FOR RENT (LADIES ONLY)»
  * 3766046853552415 -- это поиск жилья, а не предложение
  * 3762964507193983 -- район не определяется по адресу «/ Location:** Đường Mạc Đĩnh Chi»
  * 3752397751583992 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 3672523882904713 -- тот же текст уже заведён: id 3001274
  * 3670595533097548 -- нет ни одной скачанной фотографии
  * 3669518326538602 -- нет ни одной скачанной фотографии
  * 2125924031352847 -- это поиск жилья, а не предложение
  * 2134554663823117 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 2080210199257564 -- это поиск жилья, а не предложение
  * 2976792129381531 -- уже на сайте: id 3001363
  * 2977831269277617 -- район не определяется: «Fully Furnished Apartment in Da Nang City Center, Nguyen Chi Thanh St., Hai Chau District»
  * 2977208469339897 -- район не определяется: «1 Bedroom Apartment, 🏠1 Bedroom Apartment»
  * 1744394567216852 -- тип жилья в тексте не назван
  * 1743758793947096 -- похоже на уже заведённое: id 3001248
  * 1744684593854516 -- тип жилья в тексте не назван
  * 1744021827254126 -- в посте несколько разных цен: 5,500,000, 8,000,000
  * 1744488090540833 -- в посте несколько разных цен: 5,500,000, 8,000,000
  * 1744479857208323 -- тот же текст уже заведён: id 3001405
  * 1744691540520488 -- похоже на уже заведённое: id 1011649
  * 1743860820603560 -- район не определяется: «1 Bedroom Apartment, 🏠1 Bedroom Apartment»
  * 1744407767215532 -- улица Lý Đạo Thành идёт через несколько районов (ah 1, вне 1), а пост называет только прежний район Son Tra
  * 1741320454190930 -- район не определяется: «🌟 BEAUTIFUL 1-BEDROOM APARTMENT, SON TRA, DA NANG»
  * 2225157728111886 -- тот же текст уже заведён: id 3001406
  * 2231605974133728 -- улица Phạm Vấn идёт через несколько районов (ah 1, st 1), а пост называет только прежний район Son Tra
  * 2231195800841412 -- тот же текст уже заведён: id 3001407
  * 2222420721718920 -- тот же текст уже заведён: id 3001408
  * 2222237321737260 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000, 14,000,000
  * 2224525978175061 -- тот же текст уже заведён: id 3001409
  * 2221117548515904 -- это поиск жилья, а не предложение
  * 2224106144883711 -- тот же текст уже заведён: id 3001410
  * 2363124944525852 -- район не определяется: «Alley connecting to 382 Tran Cao Van, 🍄Mini house for rent near Nguyen Tat Thanh beach - Thanh Khe»
  * 2362788734559473 -- похоже на уже заведённое: id 3001250
  * 1648727443062647 -- район не определяется: «CHO THUÊ NHÀ 3 TẦNG, MẶT TIỀN TRƯNG NỮ VƯƠNG, ĐÀ NẴNG»
  * 1643178526950872 -- в посте несколько разных цен: 25,000,000, 27,000,000
  * 1389904863353303 -- район не определяется: «CHO THUÊ PHÒNG P302, TRƯƠNG CÔNG HY, ĐÀ NẴNG»
  * 1394116689598787 -- район не определяется: «BRAND-NEW STUDIO APARTMENT, SON TRA, DA NANG»
  * 1388166273527162 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000
  * 1487114080248242 -- район не определяется: «🌷CHÍNH CHỦ CHO THUÊ CĂN HỘ NEW 100% - PHAN HUỲNH ĐIỂU»
  * 1476237824669201 -- в посте несколько разных цен: 8,000,000, 9,000,000
  * 1485169163776067 -- район не определяется: «1-BEDROOM, APARTMENT FOR RENT, SON TRA»
  * 1485327343760249 -- похоже на уже заведённое: id 1011635
  * 1486318753661108 -- район не определяется: «FULLY FURNISHED 1- BEDROOM APARTMENT, SON TRA, FLEXIBLE LEASE TERMS»
  * 1486578613635122 -- район ns не входит в прежний район Son Tra из поста
  * 2231309210775257 -- район не определяется по адресу «HOUSE FEATURES»
  * 2243700639536114 -- в посте несколько разных цен: 15,000, 22,000
  * 2240689496503895 -- тип жилья в тексте не назван
  * 2243314172908094 -- посуточно
  * 2238082586764586 -- рассрочка
  * 3816572018498693 -- тип жилья в тексте не назван
  * 3816499511839277 -- помещение под бизнес или здание целиком, а не жильё
  * 3816620251827203 -- тип жилья в тексте не назван
  * 3805749332914295 -- тип жилья в тексте не назван
  * 3813589265463635 -- помещение под бизнес или здание целиком, а не жильё
  * 3805800382909190 -- помещение под бизнес или здание целиком, а не жильё
  * 3803565069799388 -- тип жилья в тексте не назван
  * 1852873992726681 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 2 ngủ ngõ 53 Nguyễn »
  * 1855203405827073 -- тот же текст уже заведён: id 3001411
  * 1839186734095407 -- тип жилья в тексте не назван
  * 1818287229518691 -- тип жилья в тексте не назван
  * 1798998168114264 -- тип жилья в тексте не назван
  * 1335188708645599 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 1336074805223656 -- район не определяется по адресу «Vị trí gần Trung tâm thành phố»
  * 28879476114997119 -- район не определяется по адресу «T2734 Cho thuê chung cư Sentosa Sky Park»
  * 28923761580568572 -- район не определяется по адресу «HH403 Cho thuê căn hộ Chung Cư Hoàng Huy Commerce »
  * 28923763360568394 -- район не определяется по адресу «HH414 Cho thuê chung cư Hoàng Huy Commerce - Camel»
  * 28921927237418673 -- район не определяется по адресу «T0131 CHO THUÊ CĂN HỘ VINHOMES MARINA - PHÒNG 501»
  * 28893993746878689 -- район не определяется по адресу «🇻🇳🇻🇳🇻🇳 VINHOMES MARINA»
  * 1865296498122406 -- похоже на уже заведённое: id 3001056
  * 1858166655502057 -- тип жилья в тексте не назван
  * 1865425554776167 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1858110785507644 -- похоже на уже заведённое: id 1006401
  * 1971187117291043 -- тот же текст уже заведён: id 3001412
  * 1971113763965045 -- в посте несколько разных цен: 13,000,000, 14,000,000
  * 1971303350612753 -- цены в посте нет
  * 1969270227482732 -- район не определяется по адресу «De Tham Street»
  * 1970229000720188 -- район не определяется по адресу «Apartment Details»
  * 1971450930597995 -- в посте несколько разных цен: 6,000,000, 30,000,000
  * 1971301710612917 -- тот же текст уже заведён: id 3001413
  * 1971199917289763 -- район не определяется по адресу «Phạm Ngọc Thạch Street»
  * 1971188420624246 -- тот же текст уже заведён: id 3001414
  * 1971189337290821 -- цены в посте нет
  * 1971161343960287 -- район не определяется по адресу «Đề Thám»
  * 1706860460872704 -- район не определяется по адресу «2-Bedroom Fully Furnished House»
  * 1705644377660979 -- район не определяется по адресу «2-BEDROOM HOUSE FOR RENT»
  * 1704894227735994 -- район не определяется по адресу «HOUSE FOR RENT»
  * 1709427257282691 -- район не определяется по адресу «Cozy private apartment in a convenient location»
  * 1708764027349014 -- район не определяется по адресу «✨ COZY 1-BEDROOM APARTMENT FOR RENT IN HOI AN ✨🏡»
  * 2019489318729451 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 2017747158903667 -- нет ни одной скачанной фотографии
  * 2018607792150937 -- район не определяется по адресу «a quiet neighborhood»
  * 2017928622218854 -- нет ни одной скачанной фотографии
  * 1692451368630838 -- тип жилья в тексте не назван
  * 1708277650381543 -- район не определяется по адресу «CHO THUÊ STUDIO CAO CẤP»
  * 1701057297770245 -- в посте несколько разных цен: 3,600,000, 3,700,000, 3,800,000
  * 1637646127444696 -- район не определяется по адресу «Không gian sống hiện đại»
  * 1251745672701412 -- в посте несколько разных цен: 4,000,000, 4,500,000, 4,800,000
  * 2029606884383767 -- район не определяется по адресу «‼️For Rent‼️»
  * 2029646411046481 -- продажа в рассрочку, а не аренда
  * 2028222764522179 -- тип жилья в тексте не назван
  * 2025675264776929 -- в посте несколько разных цен: 5,000, 6,000, 8,000, 9,000, 10,000, 12,000
  * 2011944009483388 -- тип жилья в тексте не назван
  * 4422888704707669 -- район не определяется по адресу «SPACIOUS 2-BEDROOM APARTMENT FOR RENT»
  * 4423508661312340 -- район не определяется по адресу «‼️For Rent‼️»
  * 4423595861303620 -- район не определяется по адресу «AVIDA TOWERS SUCAT located in front of SM City Suc»
  * 4416200248709848 -- район не определяется по адресу «1584 J Fajardo st. sampaloc manila.»
  * 4422233138106559 -- тип жилья в тексте не назван
  * 4420961321567074 -- район не определяется по адресу «Napico Manggahan Pasig City»
  * 4418049975191542 -- район не определяется по адресу «Furnished Studio for Rent»
  * 4416633901999816 -- тот же текст уже заведён: id 3001120
  * 4423344427995430 -- в посте несколько разных цен: 12,000, 12,500
  * 4421905988139274 -- район не определяется по адресу «along C5»
  * 4423033101359896 -- тип жилья в тексте не назван
  * 4421181384878401 -- похоже на уже заведённое: id 3000869
  * 1974105989951835 -- тип жилья в тексте не назван
  * 1978201452875622 -- уже на сайте: id 3001366
  * 1968186313877136 -- это поиск жилья, а не предложение
  * 1970693793626388 -- уже на сайте: id 3001367
  * 1978364799525954 -- похоже на уже заведённое: id 3001282
  * 1979076319454802 -- район не определяется по адресу «Phước Tiến - Trung tâm thành phố»
  * 1978862859476148 -- уже на сайте: id 3001368
  * 1968292877199813 -- район не определяется по адресу «Cho Thuê Nhà đường Thích Quảng Đức»
  * 1968092573886510 -- тот же текст уже заведён: id 3001235
  * 4726702167575852 -- это поиск жилья, а не предложение
  * 4728819124030823 -- район не определяется по адресу «Mini villa for rent near the city center»
  * 4728751454037590 -- район не определяется по адресу «South Nha Trang»
  * 4724156191163783 -- это поиск жилья, а не предложение
  * 4727773037468765 -- район не определяется по адресу «South Nha Trang»
  * 4727422960837106 -- район не определяется по адресу «NT RENT»
  * 2091252198198867 -- уже на сайте: id 3001369
  * 2092360064754747 -- район не определяется по адресу «side a modern urban area»
  * 2090555578268529 -- в посте несколько разных цен: 530,000, 20,000,000
  * 2090509091606511 -- нет ни одной скачанной фотографии
  * 1114854120988476 -- район не определяется по адресу «4th floor with airy windows»
  * 1114003031073585 -- район не определяется по адресу «South Nha Trang»
  * 1115153104291911 -- в посте несколько разных цен: 660,000, 700,000, 1,000,000, 15,000,000
  * 1114744844332737 -- район не определяется по адресу «South Nha Trang»
  * 1114413457699209 -- в посте несколько разных цен: 500,000, 14,000,000
  * 1111413477999207 -- район не определяется по адресу «South Nha Trang»
  * 1113365664470655 -- в посте несколько разных цен: 20,000,000, 25,000,000
  * 1107933228347232 -- тот же текст уже заведён: id 3001415
  * 1115284050945483 -- в посте несколько разных цен: 1,000,000, 20,000,000, 22,000,000
  * 2071886053645496 -- район не определяется по адресу «Mini villa for rent near the city center»
  * 2072146586952776 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2072125566954878 -- район не определяется по адресу «Cao Văn Bé - Nha Trang»
  * 2072331850267583 -- район не определяется по адресу «CHO THUÊ STUDIO - GIÁ YÊU THƯƠNG»
  * 2072286320272136 -- район не определяется по адресу «**Khanh Hoa»
  * 2069346347232800 -- это поиск жилья, а не предложение
  * 3844105802396633 -- район не определяется по адресу «South Nha Trang»
  * 3837694026371144 -- район не определяется по адресу «2 bedrooms»; прецедент расколот: «LVCC»: lt 1
  * 3844324975708049 -- тот же текст уже заведён: id 3001416
  * 3844259259047954 -- тот же текст уже заведён: id 3001417
  * 3844452962361917 -- тот же текст уже заведён: id 3001418
  * 4619187528350768 -- в посте несколько разных цен: 500,000, 12,500,000
  * 4620269678242553 -- район не определяется по адресу «NT RENT»
  * 4623182901284564 -- район не определяется по адресу «1 separate bedroom»
  * 4615612555374932 -- район не определяется по адресу «Muong Thanh 04 Tran Phu»
  * 4617186755217512 -- это поиск жилья, а не предложение
  * 4618707241732130 -- нет ни одной скачанной фотографии
  * 4615648422038012 -- район не определяется по адресу «LUXURY 3-BEDROOM APARTMENT FOR RENT»; прецедент расколот: «GOLDCOAST»: совпало только в ссылках строк lt -- это реклама, а не место
  * 4611904355745752 -- нет ни одной скачанной фотографии
  * 2712281229204152 -- район не определяется по адресу «136m²/floor - 5m wide with parking space»
  * 2714520092313599 -- в посте несколько разных цен: 1,000,000, 10,000,000
  * 2720806041685004 -- район не определяется по адресу «City center»
  * 2719901165108825 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2720297438402531 -- в тексте есть и другая цена того же порядка: 8,580,887 против 25,000,000
  * 2720750971690511 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2720321525066789 -- район не определяется по адресу «NT RENT»
  * 2720776721687936 -- район не определяется по адресу «40m² - Balcony available»
  * 2369506903583319 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2367700887097254 -- тот же текст уже заведён: id 3001198
  * 2358276808039662 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 2599789720441683 -- тот же текст уже заведён: id 3001198
  * 2586447371775918 -- помещение под бизнес или здание целиком, а не жильё
  * 2599927840427871 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2588243598262962 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2592618517825470 -- район не определяется по адресу «✨ Brand-new villa»
  * 2582748732145782 -- тип жилья в тексте не назван
  * 1763318494880834 -- район не определяется по адресу «CHO THUÊ VILLA PALM GARDEN»
  * 1769689764243707 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1768081234404560 -- тот же текст уже заведён: id 3001198
  * 1764181028127914 -- адрес называет несколько районов: ath, dto
  * 1756168655595818 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2585080565245932 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 2136536980318297 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 2134695860502409 -- район не определяется по адресу «studio layout featuring 2 beds»
  * 2133240870647908 -- это поиск жилья, а не предложение
  * 2138432310128764 -- район не определяется по адресу «🎉🎉Cho thuê căn hộ Phú Tài Residence»
  * 3281767222034371 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 3288974787980281 -- район не определяется по адресу «⭐️ Cho Thuê Căn Hộ ALTARA RESIDENCE»; прецедент расколот: «TRẦN HƯNG ĐẠO 🌟🌟🌟»: совпало только в ссылках строк qn -- это реклама, а не место
  * 3280507732160320 -- район не определяется по адресу «Ngay Đại học FPT»
  * 3288882517989508 -- район не определяется по адресу «studio layout featuring 2 beds»
  * 3278586459019114 -- район не определяется по адресу «Studio»
  * 3255575561303994 -- район не определяется по адресу «Apartment for rent near the beach - opposite Merma»
  * 3246119772249573 -- район не определяется по адресу «VILLA FOR RENT»
  * 3252616481599902 -- район не определяется по адресу «CHO THUÊ NHÀ PHAN CHU TRINH»
  * 3254576238070593 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 3213120192216198 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»; прецедент расколот: «Xô Viết Nghệ Tĩnh»: vtp 1; «Viết Nghệ Tĩnh»: vtp 1
  * 3236985219829695 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»
  * 3203441086517442 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ»
  * 1474799354464133 -- район не определяется по адресу «Direct owner service»
  * 1478438467433555 -- район не определяется по адресу «Apartment for rent near the beach - opposite Merma»
  * 1476872604256808 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 1477067380903997 -- в посте несколько разных цен: 9,000,000, 13,000,000, 18,000,000
"""
from listing_lock import insert_listings

IDS = [3001449, 3001450, 3001451, 3001452, 3001453, 3001454, 3001455, 3001456, 3001457, 3001458, 3001459, 3001460, 3001461]

NEW_SRC = r'''
L(3001449,"cebu","bnl","Квартира",15000,30,
  "2-спальная квартира, 30 м², Banilad.",
  "https://www.facebook.com/groups/rentcebu/posts/28129154990116594/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-26",
  descEn="2-bedroom flat, 30 m², Banilad.",
  details={"photos": ["assets/fb_photos/28129154990116594/01.webp", "assets/fb_photos/28129154990116594/02.webp", "assets/fb_photos/28129154990116594/03.webp", "assets/fb_photos/28129154990116594/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001450,"cebu","tlm","Дом",17000,None,
  "2-спальный дом, Talamban.",
  "https://www.facebook.com/groups/cebu.tambayan.2/posts/28648204168176353/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-26",
  descEn="2-bedroom house, Talamban.",
  details={"photos": ["assets/fb_photos/28648204168176353/01.webp", "assets/fb_photos/28648204168176353/02.webp", "assets/fb_photos/28648204168176353/03.webp", "assets/fb_photos/28648204168176353/04.webp", "assets/fb_photos/28648204168176353/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001451,"da-nang","ah","Квартира",9500000,None,
  "Квартира, Convenient location, An Hải.",
  "https://www.facebook.com/groups/728946289449167/posts/1395964762747313/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="Flat, Convenient location, An Hải.",
  details={"photos": ["assets/fb_photos/1395964762747313/01.webp", "assets/fb_photos/1395964762747313/02.webp", "assets/fb_photos/1395964762747313/03.webp", "assets/fb_photos/1395964762747313/04.webp", "assets/fb_photos/1395964762747313/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001452,"da-nang","cl2","Студия",6000000,None,
  "Студия, Bàu Tràm Trung, Cẩm Lệ.",
  "https://www.facebook.com/groups/728946289449167/posts/1395720109438445/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="Studio, Bàu Tràm Trung, Cẩm Lệ.",
  details={"photos": ["assets/fb_photos/1395720109438445/01.webp", "assets/fb_photos/1395720109438445/02.webp", "assets/fb_photos/1395720109438445/03.webp", "assets/fb_photos/1395720109438445/04.webp", "assets/fb_photos/1395720109438445/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001453,"da-nang","ns","Квартира",5500000,None,
  "Квартира, Căn hộ full nội thất, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/728946289449167/posts/1395740982769691/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="Flat, Căn hộ full nội thất, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1395740982769691/01.webp", "assets/fb_photos/1395740982769691/02.webp", "assets/fb_photos/1395740982769691/03.webp", "assets/fb_photos/1395740982769691/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001454,"da-nang","ns","Квартира",12000000,None,
  "1-спальная квартира, Khue My Dong 7 Street., Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1486233807002936/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="1-bedroom flat, Khue My Dong 7 Street., Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1486233807002936/01.webp", "assets/fb_photos/1486233807002936/02.webp", "assets/fb_photos/1486233807002936/03.webp", "assets/fb_photos/1486233807002936/04.webp", "assets/fb_photos/1486233807002936/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001455,"da-nang","ns","Квартира",14000000,None,
  "2-спальная квартира, Trương Quang Được, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1487160270243623/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="2-bedroom flat, Trương Quang Được, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1487160270243623/01.webp", "assets/fb_photos/1487160270243623/02.webp", "assets/fb_photos/1487160270243623/03.webp", "assets/fb_photos/1487160270243623/04.webp", "assets/fb_photos/1487160270243623/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001456,"da-nang","ns","Квартира",10000000,None,
  "1-спальная квартира, An Thượng 32, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1487162310243419/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="1-bedroom flat, An Thượng 32, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1487162310243419/01.webp", "assets/fb_photos/1487162310243419/02.webp", "assets/fb_photos/1487162310243419/03.webp", "assets/fb_photos/1487162310243419/04.webp", "assets/fb_photos/1487162310243419/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001457,"da-nang","ns","Квартира",10000000,None,
  "2-спальная квартира, Nguyễn Đình Chiểu, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1486327023660281/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="2-bedroom flat, Nguyễn Đình Chiểu, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1486327023660281/01.webp", "assets/fb_photos/1486327023660281/02.webp", "assets/fb_photos/1486327023660281/03.webp", "assets/fb_photos/1486327023660281/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001458,"nha-trang","vn","Квартира",14000000,None,
  "1-спальная квартира, Vĩnh Nguyên.",
  "https://www.facebook.com/groups/chothue79/posts/4623191777950343/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="1-bedroom flat, Vĩnh Nguyên.",
  details={"photos": ["assets/fb_photos/4623191777950343/01.webp", "assets/fb_photos/4623191777950343/02.webp", "assets/fb_photos/4623191777950343/03.webp", "assets/fb_photos/4623191777950343/04.webp", "assets/fb_photos/4623191777950343/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001459,"nha-trang","ph2","Квартира",12000000,32,
  "Квартира, 32 м², Phước Hòa.",
  "https://www.facebook.com/groups/chothue79/posts/4622251358044385/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="Flat, 32 m², Phước Hòa.",
  details={"photos": ["assets/fb_photos/4622251358044385/01.webp", "assets/fb_photos/4622251358044385/02.webp", "assets/fb_photos/4622251358044385/03.webp", "assets/fb_photos/4622251358044385/04.webp", "assets/fb_photos/4622251358044385/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001460,"nha-trang","lt","Квартира",14000000,None,
  "Квартира, Lộc Thọ — 1 санузел.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2719655501800058/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="Flat, Lộc Thọ — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2719655501800058/01.webp", "assets/fb_photos/2719655501800058/02.webp", "assets/fb_photos/2719655501800058/03.webp", "assets/fb_photos/2719655501800058/04.webp", "assets/fb_photos/2719655501800058/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001461,"nha-trang","ph","Квартира",14000000,40,
  "1-спальная квартира, 40 м², Phước Hải.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2720674205031521/","сегодня",0,source="fbgroup",postedOn="2026-09-26",
  descEn="1-bedroom flat, 40 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/2720674205031521/01.webp", "assets/fb_photos/2720674205031521/02.webp", "assets/fb_photos/2720674205031521/03.webp", "assets/fb_photos/2720674205031521/04.webp", "assets/fb_photos/2720674205031521/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
