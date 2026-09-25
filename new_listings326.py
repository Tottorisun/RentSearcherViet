# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 14 строк, 2026-09-25.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * chothuecanhodanang43/1744479857208323 -- da-nang/ns, 9,000,000 VND: район назван в посте; прежний район Ngu Hanh Son весь вошёл в этот; улица Khuê Mỹ Đông 7: 2 из 2 отрезков в ns; пост: Ngu Hanh Son
  * canhochothuedanangtot/2225157728111886 -- da-nang/ns, 6,500,000 VND: район назван в посте; улица Khuê Mỹ Đông 4: 1 из 1 отрезков в ns
  * canhochothuedanangtot/2231195800841412 -- da-nang/ns, 8,000,000 VND: район назван в посте
  * canhochothuedanangtot/2222420721718920 -- da-nang/st, 6,000,000 VND: улица Tân Thái 4: 1 из 1 отрезков в st; пост: Son Tra
  * canhochothuedanangtot/2224525978175061 -- da-nang/ns, 6,000,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * canhochothuedanangtot/2224106144883711 -- da-nang/ns, 12,000,000 VND: улица Lê Văn Hiến: 45 из 45 отрезков в ns
  * 416308689716559/1855203405827073 -- ha-noi/cg, 6,500,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1971187117291043 -- ho-chi-minh/bth, 17,500,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1971301710612917 -- ho-chi-minh/ak, 35,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1971188420624246 -- ho-chi-minh/ak, 21,000,000 VND: район назван в адресе поста
  * khachsanvillahomestaynhatrang/1107933228347232 -- nha-trang/ph, 8,000,000 VND: район назван в адресе поста
  * 849441571863086/3844324975708049 -- nha-trang/ph, 10,000,000 VND: район назван в адресе поста
  * 849441571863086/3844259259047954 -- nha-trang/ph2, 12,000,000 VND: район назван в адресе поста
  * 849441571863086/3844452962361917 -- nha-trang/ph2, 12,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (276):
  * 2672374729880903 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 2671323069986069 -- район не определяется по адресу «one of Buôn Ma Thuột's most secure and pristine ur»
  * 2168691324070411 -- район не определяется по адресу «one of Buôn Ma Thuột's most secure and pristine ur»
  * 2170210010585209 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 2182552376017639 -- это поиск жилья, а не предложение
  * 2185082292431314 -- нет ни одной скачанной фотографии
  * 4534963593485999 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 4535108773471481 -- район не определяется по адресу «Chủ gửi»
  * 4524078787907813 -- район не определяется по адресу «GIÁ THUÊ : 2.7 TRIỆU»
  * 4547172472265111 -- тот же текст уже заведён: id 3001175
  * 4523929227922769 -- район не определяется по адресу «Chủ gửi - GIÁ THUÊ : 2.7 TRIỆU»
  * 4578192675829757 -- район не определяется по адресу «🥨🫜🍒 CĂN HỘ CAO CẤP MỚI XÂY KDC AN KHÁNH FULL NỘI T»
  * 4576672325981792 -- район не определяется по адресу «🛍️🎀 PHÒNG FULL NỘI THẤT CÓ BAN CÔNG ĐƯỜNG HOÀNG QU»
  * 4576541529328205 -- район не определяется по адресу «🥟🍤 PHÒNG TRỌ ĐƯỜNG NGUYỄN TRÃI - GẦN VINCOM HÙNG V»
  * 4575984912717200 -- район не определяется по адресу «1/10 trống phòng!»
  * 4569297596719265 -- тип жилья в тексте не назван
  * 2145727852997245 -- район не определяется по адресу «Chủ gửi»
  * 2145579633012067 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 2136097713960259 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NGUYỄN VĂN LI»
  * 2182373332666030 -- район не определяется по адресу «1/10 trống!»
  * 2178278159742214 -- район не определяется по адресу «☸️🏚️📫MINIHOUSE CAO CẤP FULL NỘI THẤT - RỘNG 40M2 M»
  * 2181919569378073 -- район не определяется по адресу «🏚️⚖️🧿MINIHOUSE ĐƯỜNG 30/4 FULL NỘI THẤT - GẦN ĐHCT»
  * 2174816730088357 -- тип жилья в тексте не назван
  * 2129210777982286 -- район не определяется по адресу «CHO THUÊ CĂN HỘ TRUNG TÂM CẦN THƠ»
  * 1828615444805775 -- район не определяется по адресу «Avida Towers Cebu»
  * 1831468591187127 -- район не определяется по адресу «Cardinal Rosales Ave»
  * 1829954228005230 -- район не определяется по адресу «HOUSE FOR RENT IN AJOYA»
  * 1830943177906335 -- в тексте есть и другая цена того же порядка: 3,625 против 5,000
  * 1829677238032929 -- в посте несколько разных цен: 12,000, 18,000
  * 1831961487804504 -- тот же текст уже заведён: id 3001361
  * 1831943547806298 -- район не определяется по адресу «ROOM FOR RENT (LADIES ONLY)»
  * 1826420871691899 -- в посте несколько разных цен: 18,000, 25,000
  * 1825901171743869 -- в тексте есть и другая цена того же порядка: 13,430 против 16,500
  * 1821535598847093 -- в тексте есть и другая цена того же порядка: 15,000 против 17,000
  * 1828052141528772 -- в посте несколько разных цен: 4,500, 80,000
  * 2130933830873212 -- это поиск жилья, а не предложение
  * 2130824454217483 -- район не определяется по адресу «ROOM FOR RENT - ₱4»
  * 2130706907562571 -- район не определяется по адресу «ROOM FOR RENT»
  * 2129515557681706 -- тот же текст уже заведён: id 3001362
  * 2131553427477919 -- в посте несколько разных цен: 7,000, 7,500
  * 2127422497891012 -- район не определяется по адресу «UBCA 2 QUIOT PARDO CEBU CITY»
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
  * 2363124944525852 -- район не определяется: «Alley connecting to 382 Tran Cao Van, 🍄Mini house for rent near Nguyen Tat Thanh beach - Thanh Khe»
  * 2362788734559473 -- похоже на уже заведённое: id 3001250
  * 2362549944583352 -- район не определяется: «Hiyori Tower, Đà Nẵng, 🏢 HIYORI TOWER»
  * 2362747857896894 -- уже на сайте: id 3001298
  * 2360398424798504 -- уже на сайте: id 3001299
  * 2361758191329194 -- нет ни одной скачанной фотографии
  * 2357231405115206 -- нет ни одной скачанной фотографии
  * 2361077668063913 -- район не определяется: «a densely populated area with convenient transportation, administrative offices, schools»
  * 2353501535488193 -- это поиск жилья, а не предложение
  * 2352331512271862 -- район не определяется: «- Two bed room ( 03 bed in two bed room ), - 200m walking to the an bang beach., TWO BEDROOM HOUSE FOR RENT AN BANG - HOI AN»
  * 1641666327102092 -- тип жилья в тексте не назван
  * 1644387356829989 -- уже на сайте: id 3001300
  * 1648116186457106 -- уже на сайте: id 3001301
  * 1648000753135316 -- район не определяется: «APARTMENT FOR RENT IN THE HIYORI GARDEN, FULLY FURNISHED, Private space»
  * 1646998733235518 -- район не определяется: «CHO THUÊ 2PN, MIA CENTER POINT, TẦNG 12»
  * 1648024443132947 -- тип жилья в тексте не назван
  * 1647772936491431 -- район не определяется: «4-Bedroom House for Rent in Central Da Nang 🌿, Prime location near Dragon Bridge & Han River, Entire house with spacious living areas»
  * 1394751396201983 -- уже на сайте: id 3001302
  * 1394116689598787 -- район не определяется: «BRAND-NEW STUDIO APARTMENT, SON TRA, DA NANG»
  * 1394422612901528 -- уже на сайте: id 3001303
  * 2976792129381531 -- тот же текст уже заведён: id 3001363
  * 2977831269277617 -- район не определяется: «Fully Furnished Apartment in Da Nang City Center, Nguyen Chi Thanh St., Hai Chau District»
  * 2977208469339897 -- район не определяется: «1 Bedroom Apartment, 🏠1 Bedroom Apartment»
  * 1744394567216852 -- тип жилья в тексте не назван
  * 1743758793947096 -- похоже на уже заведённое: id 3001248
  * 1744684593854516 -- тип жилья в тексте не назван
  * 1744021827254126 -- в посте несколько разных цен: 5,500,000, 8,000,000
  * 1744488090540833 -- в посте несколько разных цен: 5,500,000, 8,000,000
  * 1744691540520488 -- похоже на уже заведённое: id 1011649
  * 1743860820603560 -- район не определяется: «1 Bedroom Apartment, 🏠1 Bedroom Apartment»
  * 1744407767215532 -- улица Lý Đạo Thành идёт через несколько районов (ah 1, вне 1), а пост называет только прежний район Son Tra
  * 1741320454190930 -- район не определяется: «🌟 BEAUTIFUL 1-BEDROOM APARTMENT, SON TRA, DA NANG»
  * 2231605974133728 -- улица Phạm Vấn идёт через несколько районов (ah 1, st 1), а пост называет только прежний район Son Tra
  * 2222237321737260 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000, 14,000,000
  * 2221117548515904 -- это поиск жилья, а не предложение
  * 2231309210775257 -- район не определяется по адресу «HOUSE FEATURES»
  * 2243700639536114 -- в посте несколько разных цен: 15,000, 22,000
  * 2240689496503895 -- тип жилья в тексте не назван
  * 2243314172908094 -- посуточно
  * 2238082586764586 -- рассрочка
  * 28516260041309277 -- тип жилья в тексте не назван
  * 28960082756927001 -- тип жилья в тексте не назван
  * 29240192592249348 -- помещение под бизнес или здание целиком, а не жильё
  * 28822141150721163 -- помещение под бизнес или здание целиком, а не жильё
  * 959510036719595 -- уже на сайте: id 3001304
  * 957601213577144 -- в посте несколько разных цен: 4,000,000, 6,000,000
  * 937482665588999 -- тот же текст уже заведён: id 3001364
  * 979833631353902 -- нет ни одной скачанной фотографии
  * 968845495786049 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 955745937096005 -- тип жилья в тексте не назван
  * 946525864684679 -- тип жилья в тексте не назван
  * 3816572018498693 -- тип жилья в тексте не назван
  * 3816499511839277 -- помещение под бизнес или здание целиком, а не жильё
  * 3816620251827203 -- тип жилья в тексте не назван
  * 3805749332914295 -- тип жилья в тексте не назван
  * 3813589265463635 -- помещение под бизнес или здание целиком, а не жильё
  * 3805800382909190 -- помещение под бизнес или здание целиком, а не жильё
  * 3803565069799388 -- тип жилья в тексте не назван
  * 1852873992726681 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 2 ngủ ngõ 53 Nguyễn »
  * 1839186734095407 -- тип жилья в тексте не назван
  * 1818287229518691 -- тип жилья в тексте не назван
  * 1798998168114264 -- тип жилья в тексте не назван
  * 3859299804211128 -- район не определяется по адресу «[EN BELOW] 10»
  * 2011943879441925 -- уже на сайте: id 3001305
  * 2010562192913427 -- район не определяется по адресу «T2964 Cho Thuê Nhà Vinhomes Marina»; прецедент расколот: «Vinhomes Marina»: совпало только в ссылках строк anb2 -- это реклама, а не место
  * 2012014749434838 -- район не определяется по адресу «T2760 Cho Thuê Nhà Nguyên Căn - 193 Văn Cao ( oto »
  * 2012053172764329 -- район не определяется по адресу «CHO THUÊ CĂN HỘ LÊ HỒNG PHONG - T0656»
  * 2012882546014725 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 2011122146190765 -- район не определяется по адресу «Cho thuê căn hộ Penthouse 1 ngủ tách bếp to rộng t»
  * 2012021282767518 -- уже на сайте: id 3001306
  * 1335188708645599 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 1336074805223656 -- район не определяется по адресу «Vị trí gần Trung tâm thành phố»
  * 28879476114997119 -- район не определяется по адресу «T2734 Cho thuê chung cư Sentosa Sky Park»; прецедент расколот: «Sentosa Sky Park»: lch 1
  * 28923761580568572 -- район не определяется по адресу «HH403 Cho thuê căn hộ Chung Cư Hoàng Huy Commerce »; прецедент расколот: «Commerce»: совпало только в ссылках строк lch -- это реклама, а не место
  * 28923763360568394 -- район не определяется по адресу «HH414 Cho thuê chung cư Hoàng Huy Commerce - Camel»
  * 28921927237418673 -- район не определяется по адресу «T0131 CHO THUÊ CĂN HỘ VINHOMES MARINA - PHÒNG 501»; прецедент расколот: «VINHOMES MARINA»: совпало только в ссылках строк anb2 -- это реклама, а не место
  * 28893993746878689 -- район не определяется по адресу «🇻🇳🇻🇳🇻🇳 VINHOMES MARINA»; прецедент расколот: «🇻🇳🇻🇳🇻🇳 VINHOMES MARINA»: совпало только в ссылках строк anb2 -- это реклама, а не место
  * 1865296498122406 -- похоже на уже заведённое: id 3001056
  * 1865385504780172 -- уже на сайте: id 3001307
  * 1865425554776167 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1858166655502057 -- тип жилья в тексте не назван
  * 1865336211451768 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1864470381538351 -- уже на сайте: id 3001308
  * 1864402611545128 -- уже на сайте: id 3001309
  * 1858110785507644 -- похоже на уже заведённое: id 1006401
  * 1970185144057907 -- уже на сайте: id 3001310
  * 1970059524070469 -- район не определяется по адресу «Đinh Tiên Hoàng»
  * 1969270227482732 -- район не определяется по адресу «De Tham Street»
  * 1969292950813793 -- район не определяется по адресу «Pham Viet Chanh»
  * 1962341911508897 -- район не определяется по адресу «🌿 CHO THUÊ CĂN HỘ 2PN VIEW LANDMARK 81»
  * 1969269510816137 -- район не определяется по адресу «Nguyễn Bỉnh Khiêm»
  * 1969749244101497 -- уже на сайте: id 3001311
  * 1969006190842469 -- район не определяется по адресу «Tân Cảng»
  * 1969003407509414 -- цены в посте нет
  * 1971113763965045 -- в посте несколько разных цен: 13,000,000, 14,000,000
  * 1971303350612753 -- цены в посте нет
  * 1970229000720188 -- район не определяется по адресу «Apartment Details»
  * 1971450930597995 -- в посте несколько разных цен: 6,000,000, 30,000,000
  * 1971199917289763 -- район не определяется по адресу «Phạm Ngọc Thạch Street»
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
  * 1287853898988310 -- в тексте есть и другая цена того же порядка: 4,568,736 против 4,000,000
  * 1464410321887706 -- уже на сайте: id 3001312
  * 1466927818302623 -- тот же текст уже заведён: id 3001365
  * 1507435977585140 -- в посте несколько разных цен: 500,000, 600,000
  * 1506528094342595 -- тип жилья в тексте не назван
  * 1499726755022729 -- в посте несколько разных цен: 500,000, 600,000
  * 1799903581228992 -- в тексте есть и другая цена того же порядка: 36,000 против 30,000
  * 1797050891514261 -- в посте несколько разных цен: 12,000, 13,000, 14,000, 15,000, 17,000, 18,000, 20,000
  * 1797444981474852 -- уже на сайте: id 3001313
  * 1799249514627732 -- район не определяется по адресу «Apartment Unit !!!»
  * 1798453601373990 -- в посте несколько разных цен: 13,000, 14,000, 15,000, 17,000, 18,000, 20,000
  * 1801283101091040 -- в посте несколько разных цен: 16,000, 18,000, 25,000
  * 3443833065789032 -- район не определяется по адресу «Urban Deca Homes Ortigas»
  * 3436429663196039 -- район не определяется по адресу «PET FRIENDLY. VIEWING THIS SATURDAY! (SEPT19)»
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
  * 3837694026371144 -- район не определяется по адресу «2 bedrooms»; прецедент расколот: «LVCC»: lt 1
  * 3842813092525904 -- уже на сайте: id 3001314
  * 3843295509144329 -- уже на сайте: id 3001315
  * 3842934655847081 -- район не определяется по адресу «South Nha Trang»
  * 3842838922523321 -- уже на сайте: id 3001316
  * 3841899312617282 -- уже на сайте: id 3001317
  * 3838846259589254 -- в посте несколько разных цен: 14,500,000, 15,500,000
  * 3839121829561697 -- тот же текст уже заведён: id 3001235
  * 4615612555374932 -- нет ни одной скачанной фотографии
  * 4620269678242553 -- район не определяется по адресу «NT RENT»
  * 4619187528350768 -- в посте несколько разных цен: 500,000, 12,500,000
  * 4619729971629857 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4620125994923588 -- это поиск жилья, а не предложение
  * 4618707241732130 -- нет ни одной скачанной фотографии
  * 4617186755217512 -- это поиск жилья, а не предложение
  * 4618866955049492 -- это поиск жилья, а не предложение
  * 4614602318809289 -- это поиск жилья, а не предложение
  * 2718801841885424 -- район не определяется по адресу «Available now»
  * 2714520092313599 -- в посте несколько разных цен: 1,000,000, 10,000,000
  * 2719033868528888 -- тот же текст уже заведён: id 3001224
  * 1974105989951835 -- тип жилья в тексте не назван
  * 1978201452875622 -- тот же текст уже заведён: id 3001366
  * 1968186313877136 -- это поиск жилья, а не предложение
  * 1970693793626388 -- тот же текст уже заведён: id 3001367
  * 1978364799525954 -- похоже на уже заведённое: id 3001282
  * 1979076319454802 -- район не определяется по адресу «Phước Tiến - Trung tâm thành phố»
  * 1978862859476148 -- тот же текст уже заведён: id 3001368
  * 1968292877199813 -- район не определяется по адресу «Cho Thuê Nhà đường Thích Quảng Đức»
  * 1968092573886510 -- тот же текст уже заведён: id 3001235
  * 4726702167575852 -- это поиск жилья, а не предложение
  * 4728819124030823 -- район не определяется по адресу «Mini villa for rent near the city center»
  * 4728751454037590 -- район не определяется по адресу «South Nha Trang»
  * 4724156191163783 -- это поиск жилья, а не предложение
  * 4727773037468765 -- район не определяется по адресу «South Nha Trang»
  * 4727422960837106 -- район не определяется по адресу «NT RENT»
  * 2091252198198867 -- тот же текст уже заведён: id 3001369
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
  * 1115284050945483 -- в посте несколько разных цен: 1,000,000, 20,000,000, 22,000,000
  * 2071886053645496 -- район не определяется по адресу «Mini villa for rent near the city center»
  * 2072146586952776 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2072125566954878 -- район не определяется по адресу «Cao Văn Bé - Nha Trang»
  * 2072331850267583 -- район не определяется по адресу «CHO THUÊ STUDIO - GIÁ YÊU THƯƠNG»
  * 2072286320272136 -- район не определяется по адресу «**Khanh Hoa»
  * 2069346347232800 -- это поиск жилья, а не предложение
  * 3844105802396633 -- район не определяется по адресу «South Nha Trang»
  * 2369506903583319 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2367700887097254 -- тот же текст уже заведён: id 3001198
  * 2358276808039662 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 2599789720441683 -- тот же текст уже заведён: id 3001198
  * 2586447371775918 -- помещение под бизнес или здание целиком, а не жильё
  * 2599927840427871 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2588243598262962 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2592618517825470 -- район не определяется по адресу «✨ Brand-new villa»
  * 2582748732145782 -- тип жилья в тексте не назван
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

IDS = [3001405, 3001406, 3001407, 3001408, 3001409, 3001410, 3001411, 3001412, 3001413, 3001414, 3001415, 3001416, 3001417, 3001418]

NEW_SRC = r'''
L(3001405,"da-nang","ns","Квартира",9000000,None,
  "Квартира, Khuê Mỹ Đông 7, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1744479857208323/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Flat, Khuê Mỹ Đông 7, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1744479857208323/01.webp", "assets/fb_photos/1744479857208323/02.webp", "assets/fb_photos/1744479857208323/03.webp", "assets/fb_photos/1744479857208323/04.webp", "assets/fb_photos/1744479857208323/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001406,"da-nang","ns","Дом",6500000,None,
  "1-спальный дом, Khuê Mỹ Đông 4, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2225157728111886/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="1-bedroom house, Khuê Mỹ Đông 4, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2225157728111886/01.webp", "assets/fb_photos/2225157728111886/02.webp", "assets/fb_photos/2225157728111886/03.webp", "assets/fb_photos/2225157728111886/04.webp", "assets/fb_photos/2225157728111886/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001407,"da-nang","ns","Студия",8000000,None,
  "Студия, For Rent - Brand new studio apartment at Xuân Quỳnh, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2231195800841412/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Studio, For Rent - Brand new studio apartment at Xuân Quỳnh, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2231195800841412/01.webp", "assets/fb_photos/2231195800841412/02.webp", "assets/fb_photos/2231195800841412/03.webp", "assets/fb_photos/2231195800841412/04.webp", "assets/fb_photos/2231195800841412/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001408,"da-nang","st","Студия",6000000,None,
  "Студия, Tân Thái 4, Sơn Trà.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2222420721718920/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Studio, Tân Thái 4, Sơn Trà.",
  details={"photos": ["assets/fb_photos/2222420721718920/01.webp", "assets/fb_photos/2222420721718920/02.webp", "assets/fb_photos/2222420721718920/03.webp", "assets/fb_photos/2222420721718920/04.webp", "assets/fb_photos/2222420721718920/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001409,"da-nang","ns","Квартира",6000000,41,
  "Квартира, 41 м², PS Apartment - Phía sau đường Huỳnh Lắm, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2224525978175061/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Flat, 41 m², PS Apartment - Phía sau đường Huỳnh Lắm, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2224525978175061/01.webp", "assets/fb_photos/2224525978175061/02.webp", "assets/fb_photos/2224525978175061/03.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001410,"da-nang","ns","Квартира",12000000,None,
  "1-спальная квартира, Lê Văn Hiến, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2224106144883711/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="1-bedroom flat, Lê Văn Hiến, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2224106144883711/01.webp", "assets/fb_photos/2224106144883711/02.webp", "assets/fb_photos/2224106144883711/03.webp", "assets/fb_photos/2224106144883711/04.webp", "assets/fb_photos/2224106144883711/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001411,"ha-noi","cg","Квартира",6500000,45,
  "Квартира, 45 м², Cầu Giấy.",
  "https://www.facebook.com/groups/416308689716559/posts/1855203405827073/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Flat, 45 m², Cầu Giấy.",
  details={"photos": ["assets/fb_photos/1855203405827073/01.webp", "assets/fb_photos/1855203405827073/02.webp", "assets/fb_photos/1855203405827073/03.webp", "assets/fb_photos/1855203405827073/04.webp", "assets/fb_photos/1855203405827073/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001412,"ho-chi-minh","bth","Студия",17500000,100,
  "Студия, 100 м², Bến Thành.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1971187117291043/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Studio, 100 m², Bến Thành.",
  details={"photos": ["assets/fb_photos/1971187117291043/01.webp", "assets/fb_photos/1971187117291043/02.webp", "assets/fb_photos/1971187117291043/03.webp", "assets/fb_photos/1971187117291043/04.webp", "assets/fb_photos/1971187117291043/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001413,"ho-chi-minh","ak","Квартира",35000000,120,
  "3-спальная квартира, 120 м², An Khánh — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1971301710612917/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="3-bedroom flat, 120 m², An Khánh — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1971301710612917/01.webp", "assets/fb_photos/1971301710612917/02.webp", "assets/fb_photos/1971301710612917/03.webp", "assets/fb_photos/1971301710612917/04.webp", "assets/fb_photos/1971301710612917/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001414,"ho-chi-minh","ak","Квартира",21000000,90,
  "2-спальная квартира, 90 м², An Khánh — 1 санузел.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1971188420624246/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="2-bedroom flat, 90 m², An Khánh — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1971188420624246/01.webp", "assets/fb_photos/1971188420624246/02.webp", "assets/fb_photos/1971188420624246/03.webp", "assets/fb_photos/1971188420624246/04.webp", "assets/fb_photos/1971188420624246/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001415,"nha-trang","ph","Квартира",8000000,40,
  "1-спальная квартира, 40 м², Phước Hải.",
  "https://www.facebook.com/groups/khachsanvillahomestaynhatrang/posts/1107933228347232/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="1-bedroom flat, 40 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/1107933228347232/01.webp", "assets/fb_photos/1107933228347232/02.webp", "assets/fb_photos/1107933228347232/03.webp", "assets/fb_photos/1107933228347232/04.webp", "assets/fb_photos/1107933228347232/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001416,"nha-trang","ph","Квартира",10000000,40,
  "1-спальная квартира, 40 м², Phước Hải.",
  "https://www.facebook.com/groups/849441571863086/posts/3844324975708049/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="1-bedroom flat, 40 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/3844324975708049/01.webp", "assets/fb_photos/3844324975708049/02.webp", "assets/fb_photos/3844324975708049/03.webp", "assets/fb_photos/3844324975708049/04.webp", "assets/fb_photos/3844324975708049/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001417,"nha-trang","ph2","Квартира",12000000,40,
  "1-спальная квартира, 40 м², Phước Hòa.",
  "https://www.facebook.com/groups/849441571863086/posts/3844259259047954/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="1-bedroom flat, 40 m², Phước Hòa.",
  details={"photos": ["assets/fb_photos/3844259259047954/01.webp", "assets/fb_photos/3844259259047954/02.webp", "assets/fb_photos/3844259259047954/03.webp", "assets/fb_photos/3844259259047954/04.webp", "assets/fb_photos/3844259259047954/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001418,"nha-trang","ph2","Квартира",12000000,32,
  "Квартира, 32 м², Phước Hòa.",
  "https://www.facebook.com/groups/849441571863086/posts/3844452962361917/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Flat, 32 m², Phước Hòa.",
  details={"photos": ["assets/fb_photos/3844452962361917/01.webp", "assets/fb_photos/3844452962361917/02.webp", "assets/fb_photos/3844452962361917/03.webp", "assets/fb_photos/3844452962361917/04.webp", "assets/fb_photos/3844452962361917/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
