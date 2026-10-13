# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 15 строк, 2026-10-13.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * phongtrocanhonhadanang/1504029685223348 -- da-nang/ns, 6,500,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * phongtrocanhonhadanang/1501932988766351 -- da-nang/ah, 18,000,000 VND: улица Tô Hiến Thành: 4 из 4 отрезков в ah; пост: Son Tra
  * chothuecanhodanang43/1763917225264586 -- da-nang/cl2, 6,500,000 VND: улица Nguyễn Nhàn: 7 из 7 отрезков в cl2; пост: Cam Le
  * canhochothuedanangtot/2243209039640088 -- da-nang/ah, 11,000,000 VND: улица Đông Kinh Nghĩa Thục: 3 из 3 отрезков в ah; пост: Son Tra
  * canhochothuedanangtot/2254261675201491 -- da-nang/ns, 9,500,000 VND: прежний район Ngu Hanh Son весь вошёл в этот; улица Lê Quang Đạo: 3 из 3 отрезков в ns; пост: Ngu Hanh Son
  * v3homechothuenhahaiphong10/1996726040963709 -- hai-phong/lch, 7,000,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1802247057760684 -- ho-chi-minh/ak, 18,000,000 VND: район назван в адресе поста
  * 715451165293916/3462990163873322 -- manila/qzc, 60,000 PHP: район назван в адресе поста
  * chothue79/4642245916044929 -- nha-trang/ttr, 16,500,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2740913799674228 -- nha-trang/btr, 12,500,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1950686778960423 -- nha-trang/ph, 20,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1996062091089558 -- nha-trang/btr, 18,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1996167737745660 -- nha-trang/btr, 8,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1995396747822759 -- nha-trang/tl, 3,500,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1994398034589297 -- nha-trang/pl, 40,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (263):
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
  * 1847166082950711 -- тот же текст уже заведён: id 3002153
  * 1841760790157907 -- район не определяется по адресу «APARTMENT FOR RENT‼️»
  * 1841846580149328 -- в тексте есть и другая цена того же порядка: 33,111 против 60,000
  * 2146901265943135 -- район не определяется по адресу «TISA Labangon»
  * 2144283599538235 -- район не определяется по адресу «Mc Arthur Blvd»
  * 2113780859255176 -- рассрочка
  * 2146731842626744 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2116301972336398 -- в тексте есть и другая цена того же порядка: 7,833 против 18,000
  * 2129515557681706 -- тот же текст уже заведён: id 3002154
  * 2096872770945985 -- в посте несколько разных цен: 1,500, 13,000
  * 2115687289064533 -- район не определяется по адресу «Ready for viewing na❗»
  * 2144359749530620 -- район не определяется по адресу «P. Rodriguez St»
  * 2378291642990251 -- в посте несколько разных цен: 700,000, 15,000,000
  * 2386526018833480 -- район не определяется по адресу «Pham Hong Thai Street»
  * 2384843945668354 -- в посте несколько разных цен: 4,900,000, 5,400,000
  * 2384306445722104 -- район не определяется по адресу «LUXURY GARDEN VILLA FOR RENT»
  * 2159490707996179 -- это поиск жилья, а не предложение
  * 2069351513676766 -- уже на сайте: id 3002131
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2116570508954866 -- нет ни одной скачанной фотографии
  * 2134554663823117 -- нет ни одной скачанной фотографии
  * 2125924031352847 -- это поиск жилья, а не предложение
  * 2076569656288285 -- тот же текст уже заведён: id 3001872
  * 1664297761505615 -- район не определяется: «HOUSE FOR RENT, PHAM VAN DONG, SON TRA»
  * 1661791371756254 -- уже на сайте: id 3002132
  * 1628212845114107 -- тот же текст уже заведён: id 3002155
  * 1659646015304123 -- в тексте есть и другая цена того же порядка: 20,000,000 против 17,000,000
  * 1666707517931306 -- район не определяется: «CẦN CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ TẠI PHAN TỨ, ĐÀ NẴNG, PRIME LOCATION»
  * 1665003991434992 -- район не определяется: «APARTMENT FOR RENT IN THE PANOMA, MODERN AND LUXURIOUS LIVING SPACE, Map: maps.app.goo.gl/HBFupZspJxEKccnNA»
  * 1664686684800056 -- в посте несколько разных цен: 10,000,000, 12,000,000
  * 1637986504136741 -- район не определяется: «FOR RENT, 2-BEDROOM APARTMENT, MIA CENTER POINT»
  * 1666075467994511 -- район не определяется: «LUXURY SUN PONTE DUPLEX, 2BR, CITY VIEW»
  * 1666079001327491 -- район не определяется: «CHO THUÊ CĂN HỘ 2PN, MỸ ĐA TÂY 10, ĐÀ NẴNG»
  * 1412255507784905 -- уже на сайте: id 3002133
  * 1412121027798353 -- уже на сайте: id 3002134
  * 1411580267852429 -- уже на сайте: id 3002135
  * 1408665141477275 -- район не определяется: «STUDIO DANG VU HY, SON TRA 🏡, Dang Vu Hy»
  * 1411679851175804 -- в посте несколько разных цен: 500,000, 1,000,000, 7,000,000
  * 1410519097958546 -- район не определяется: «Separate bedroom, spacious living room, 🌊 APARTMENT FOR RENT»
  * 1370508071959649 -- район не определяется: «1-BEDROOM APARTMENT, HAI CHAU DISTRICT ✨, Le Thanh Nghi Street»
  * 1410333301310459 -- в посте несколько разных цен: 500,000, 1,000,000, 7,000,000
  * 1411656687844787 -- уже на сайте: id 3002136
  * 1409594331384356 -- район не определяется: «Dien Bien Phu Street (inside the Co.opmart Supermarket complex)., Property Highlights:, 🏢 LUXURY 1BR PENTHOUSE FOR RENT»
  * 2373490586822621 -- район не определяется: «💐 House for rent at K249/59 on Ha Huy Tap Street»
  * 2377178749787138 -- район не определяется: «HOUSE FOR RENT, HAI CHAU, DA NANG»
  * 2380358606135819 -- в посте несколько разных цен: 12,500,000, 13,500,000
  * 2373459913492355 -- район не определяется: «Da Nang beach area, approx. 100m from the beach, 3-BEDROOM HOUSE FOR RENT»
  * 2372487700256243 -- район не определяется: «3-BEDROOM HOUSE FOR RENT NEAR TAN THANH, CAM HOI BEACH, HOI AN»
  * 2375989359906077 -- район не определяется: «Prime location in the city center, 3 bedrooms, 2 bathrooms»
  * 2376514049853608 -- район не определяется: «Blooming Tower, Da Nang, Blooming Tower listing / 3 bedroom for rent»
  * 2376577839847229 -- тот же текст уже заведён: id 3002156
  * 2376837889821224 -- тот же текст уже заведён: id 3002157
  * 2384324425739237 -- тип жилья в тексте не назван
  * 2996352904092120 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT, MAI THUC LAN, Mai Thuc Lan Street»
  * 2996230964104314 -- тот же текст уже заведён: id 3002133
  * 2996288740765203 -- тот же текст уже заведён: id 3002158
  * 1583014733578036 -- район не определяется: «HOUSE FOR RENT, HAI CHAU, DA NANG»
  * 1578900223989487 -- в посте несколько разных цен: 15,000,000, 20,000,000
  * 1583463256866517 -- это поиск жилья, а не предложение
  * 1589847419561434 -- в посте несколько разных цен: 6,000,000, 8,000,000
  * 1503255625300754 -- в посте несколько разных цен: 6,500,000, 8,000,000
  * 1498498109109839 -- тип жилья в тексте не назван
  * 1504524831840500 -- в посте несколько разных цен: 5,000,000, 7,000,000
  * 1504097528549897 -- похоже на уже заведённое: id 1024175
  * 1504312168528433 -- тип жилья в тексте не назван
  * 1763839361939039 -- район не определяется: «✨ 1-BEDROOM APARTMENT FOR RENT, DIEN BIEN PHU, THANH KHE ✨🏡»
  * 1761626628826979 -- тип жилья в тексте не назван
  * 1762111078778534 -- нет ни одной скачанной фотографии
  * 2254230648537927 -- район не определяется: «For rent - 1-bedroom apartment at Nguyễn Huy Chương street, Sơn Trà Area, quiet place»
  * 2242107353083590 -- в посте несколько разных цен: 11,000,000, 13,000,000
  * 2245283689432623 -- район не определяется: «COZY STUDIO APARTMENT FOR RENT, 47 Nguyen Van Thoai Street, Da Nang»
  * 2244914949469497 -- улица Hà Kỳ Ngộ идёт через несколько районов (ah 1, st 1)
  * 2244984502795875 -- район не определяется: «✨ 1-BEDROOM APARTMENT, DUY TÂN ✨🏡, Duy Tân»
  * 2241207099840282 -- район не определяется: «Hiyori Garden Tower, Vo Van Kiet Street., ✨ PRESTIGIOUS 2-BEDROOM APARTMENT FOR RENT AT HIYORI GARDEN TOWER ✨»
  * 2254302605197398 -- район не определяется: «Huu Trac Street, Son Tra, Da Nang»
  * 3831769426978952 -- район не определяется по адресу «FULLY FURNISHED HOUSE FOR RENT»
  * 3829227160566512 -- уже на сайте: id 3002137
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
  * 2244337472845976 -- в посте несколько разных цен: 2,800,000, 3,300,000
  * 2275943409685382 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2251798492099874 -- помещение под бизнес или здание целиком, а не жильё
  * 2273544739925249 -- район не определяется по адресу «670 Đường Kim Giang ( Show room Vinfast )»; прецедент расколот: «Kim Giang»: hm 15, tx 5
  * 1082384288117917 -- тот же текст уже заведён: id 3001892
  * 1105631969126482 -- в посте несколько разных цен: 4,000,000, 6,000,000
  * 3885449368262838 -- тип жилья в тексте не назван
  * 29006310478980348 -- уже на сайте: id 3002138
  * 28441247912153277 -- нет ни одной скачанной фотографии
  * 29153180070960054 -- район не определяется по адресу «T2780 Cho thuê nhà mặt đường Văn Cao»
  * 29090459853898743 -- район не определяется по адресу «T2923 - Cho Thuê Biệt Thự Vinhomes Marina»
  * 29153134900964571 -- район не определяется по адресу «T1698 Cho thuê căn góc xẻ khe hoàng huy mall - Aeo»
  * 28959217347022995 -- район не определяется по адресу «🇻🇳 │ VINHOMES MARINA»
  * 28514993158112085 -- уже на сайте: id 3002139
  * 28660128650265201 -- район не определяется по адресу «the fourth floor»
  * 2029001354402844 -- район не определяется по адресу «T0796 Cho Thuê Nhà 193 Văn Cao»
  * 2003720763597570 -- район не определяется по адресу «T2922»
  * 2029712914331688 -- район не определяется по адресу «T2869 Cho thuê nhà nguyên căn Làng Việt Kiều Quốc »
  * 2028002394502740 -- тип жилья в тексте не назван
  * 2030770530892593 -- в посте несколько разных цен: 5,000,000, 6,500,000, 7,000,000
  * 2030712077565105 -- в посте несколько разных цен: 5,000,000, 6,500,000
  * 4537388423178980 -- район не определяется по адресу «HH422 Cho Thuê Chung Cư Hoàng Huy Commerce - Lotus»; прецедент расколот: «Lotus»: совпало только в ссылках строк lch -- это реклама, а не место
  * 4542386652679157 -- район не определяется по адресу «T3028»
  * 4541219612795861 -- район не определяется по адресу «T3028»
  * 4539788699605619 -- тип жилья в тексте не назван
  * 1879291176722938 -- в посте несколько разных цен: 5,200,000, 5,500,000, 5,700,000, 6,000,000, 6,700,000, 7,000,000
  * 1853134039338652 -- район не определяется по адресу «English below ⬇️»
  * 1874570790528310 -- в посте несколько разных цен: 5,000,000, 20,000,000
  * 1876575393661183 -- тип жилья в тексте не назван
  * 1857337518918304 -- уже на сайте: id 3002140
  * 1882187833099939 -- район не определяется по адресу «KO NGẬP LỤT»
  * 1882312279754161 -- в посте несколько разных цен: 12,000,000, 15,000,000, 16,000,000, 18,000,000, 21,000,000
  * 1801592087826181 -- уже на сайте: id 3002141
  * 1977095910033497 -- уже на сайте: id 3002142
  * 1990213192055102 -- район не определяется по адресу «NGUYEN VAN THUONG»
  * 1965348697874885 -- нет ни одной скачанной фотографии
  * 1990298222046599 -- уже на сайте: id 3002143
  * 1976252013451220 -- нет ни одной скачанной фотографии
  * 1989145782161843 -- район не определяется по адресу «Nguyen Cuu Van Street»
  * 1987669072309514 -- в посте несколько разных цен: 12,500,000, 14,000,000, 15,500,000, 26,000,000
  * 1983180809425007 -- тип жилья в тексте не назван
  * 1975807876828967 -- уже на сайте: id 3002144
  * 1975221100220978 -- район не определяется по адресу «Tran Quoc Thao Street»
  * 1991213958621692 -- в посте несколько разных цен: 14,000,000, 15,000,000
  * 1991210031955418 -- район не определяется по адресу «NGUYEN VAN THUONG»
  * 1978282599914828 -- в посте несколько разных цен: 6,000,000, 30,000,000
  * 1991248958618192 -- район не определяется по адресу «Nguyen Cuu Van Street»
  * 1992028011873620 -- цены в посте нет
  * 1991873401889081 -- район не определяется по адресу «Nguyễn Thị Định»
  * 1727772868781463 -- район не определяется по адресу «✨ COZY 1-BEDROOM APARTMENT FOR RENT IN HOI AN ✨🏡»
  * 1726429615582455 -- район не определяется по адресу «NEW VILLA FOR RENT IN AN MY»
  * 1727995195425897 -- район не определяется по адресу «🌿 Lovely 2-Bedroom Apartment for Rent in Hoi An 🏡»
  * 1727996932092390 -- район не определяется по адресу «Cute»
  * 1725652522326831 -- район не определяется по адресу «✨ YOUR OWN LITTLE SPACE!»
  * 1722717845953632 -- тип жилья в тексте не назван
  * 2035901133754936 -- район не определяется по адресу «- Near Thanh Nam Bridge»
  * 2033694973975552 -- район не определяется по адресу «🌾NEW 03 BRS VILLA FOR RENT IN RICEFIELD AN MY»
  * 2035947327083650 -- район не определяется по адресу «Cozy private apartment in a convenient location»
  * 2035293953815654 -- район не определяется по адресу «Cute»
  * 2033287777349605 -- район не определяется по адресу «Cozy private apartment in a convenient location»
  * 2079042302738675 -- район не определяется по адресу «I have a apartment for rent»
  * 2011801119498271 -- в посте несколько разных цен: 4,000,000, 5,000,000
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
  * 1815814552971228 -- продажа в рассрочку, а не аренда
  * 1817342422818441 -- район не определяется по адресу «For Rent ❗️❗️❗️»
  * 1820275605858456 -- район не определяется по адресу «Sto. Niño Village»
  * 1818350246050992 -- район не определяется по адресу «Apartment Unit !!!»
  * 1816990479520302 -- в посте несколько разных цен: 10,000, 11,000, 14,000, 15,000, 17,000, 18,000, 20,000
  * 1819793725906644 -- район не определяется по адресу «13K»
  * 1802711964281487 -- тип жилья в тексте не назван
  * 1732557494630268 -- район не определяется по адресу «Highlights**»
  * 3464179180421087 -- район не определяется по адресу «Connected to GMA-7 Mrt kamuning stations»
  * 3459205674251771 -- тот же текст уже заведён: id 3001987
  * 3457102384462100 -- это поиск жилья, а не предложение
  * 3447452425427096 -- район не определяется по адресу «Minutes to BGC & McKinley Hill»
  * 3463790320459973 -- цена 1,793 PHP вне разумных пределов
  * 1131806955959859 -- тот же текст уже заведён: id 3002159
  * 1129954529478435 -- тот же текст уже заведён: id 3002160
  * 1131392772667944 -- район не определяется по адресу «fully furnished with a private washing machine»
  * 1130887592718462 -- район не определяется по адресу «FOR RENT»
  * 1130797719394116 -- район не определяется по адресу «City center»
  * 1131337062673515 -- тот же текст уже заведён: id 3002161
  * 1131815232625698 -- похоже на уже заведённое: id 1022210
  * 1131344162672805 -- район не определяется по адресу «South Nha Trang»
  * 2087066102127491 -- в посте несколько разных цен: 500,000, 11,500,000
  * 2088427291991372 -- тот же текст уже заведён: id 3002162
  * 2088750848625683 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2087031058797662 -- в посте несколько разных цен: 500,000, 11,500,000
  * 2077475579753210 -- район не определяется по адресу «An Bình Tân»
  * 2088476468653121 -- тот же текст уже заведён: id 3002163
  * 2087513952082706 -- похоже на уже заведённое: id 1020205
  * 2088888421945259 -- помещение под бизнес или здание целиком, а не жильё
  * 4625802281022626 -- район не определяется по адресу «Tran Quy Cap Street»
  * 4626748320928022 -- похоже на уже заведённое: id 3002031
  * 4641042536165267 -- тот же текст уже заведён: id 3002164
  * 2729567317475543 -- район не определяется по адресу «fully furnished»
  * 2680936839005258 -- район не определяется по адресу «Street No. 27»
  * 2740859206346354 -- район не определяется по адресу «Biet Thu - Nha Trang»
  * 2727443507687924 -- район не определяется по адресу «Prime location near the city center»
  * 2726822094416732 -- район не определяется по адресу «Prime location: Directly opposite a park»
  * 2715479758884299 -- это поиск жилья, а не предложение
  * 2732940233804918 -- похоже на уже заведённое: id 3001994
  * 2736509383448003 -- район не определяется по адресу «STUDIO APARTMENT WITH REAR BALCONY FOR RENT»
  * 1977293056299795 -- нет ни одной скачанной фотографии
  * 1993736697988764 -- в посте несколько разных цен: 500,000, 9,000,000
  * 1993429948019439 -- в посте несколько разных цен: 500,000, 13,500,000, 14,500,000
  * 1899280460767722 -- район не определяется по адресу «ROOM FOR RENT»
  * 1995486781147089 -- похоже на уже заведённое: id new:thuecanhotronhatrang/1996062091089558
  * 1989335031762264 -- тип жилья в тексте не назван
  * 2359140247953318 -- тип жилья в тексте не назван
  * 2380371035830239 -- район не определяется по адресу «CHO THUÊ VILLA 3 PHÒNG NGỦ»
  * 2367700887097254 -- тот же текст уже заведён: id 3002165
  * 2373450553188954 -- район не определяется по адресу «CHO THUÊ CĂN HỘ THEO THÁNG»
  * 2297494690784541 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2369506903583319 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2616359608784694 -- тип жилья в тексте не назван
  * 2615310538889601 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2604061680014487 -- район не определяется по адресу «CHO THUÊ CĂN HỘ THEO THÁNG»
  * 2588243598262962 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2612174042536584 -- район не определяется по адресу «Meyhomes Phu Quoc»
  * 2599789720441683 -- тот же текст уже заведён: id 3002165
  * 5574690879422216 -- район не определяется по адресу «⭐️ Cho Thuê Căn Hộ ALTARA RESIDENCE»
  * 5573872579504046 -- район не определяется по адресу «Cho Thuê Căn Hộ ALTARA RESIDENCE»
  * 5569137533310884 -- тип жилья в тексте не назван
  * 3300621106815649 -- нет ни одной скачанной фотографии
  * 3278586459019114 -- нет ни одной скачанной фотографии
  * 3277316822479411 -- нет ни одной скачанной фотографии
  * 3282055582005535 -- нет ни одной скачанной фотографии
  * 3280507732160320 -- нет ни одной скачанной фотографии
  * 3273225212888572 -- район не определяется по адресу «Khu đô thị An Phú Thịnh»
  * 1491781806099221 -- район не определяется по адресу «Studio apartment for rent»
  * 1490821026195299 -- район не определяется по адресу «Mini Apartment for Rent»
  * 1493667805910621 -- район не определяется по адресу «💢LUXURY PENTHOUSE FOR RENT WITH 360-DEGREE OCEAN V»
  * 1493613745916027 -- район не определяется по адресу «🏢 Mini Apartment for Rent»
  * 1492688929341842 -- район не определяется по адресу «Apartment for rent at GoldSea Vung Tau»
  * 1480625103881558 -- район не определяется по адресу «🍀🍀🍀LOVELY HOUSE FOR RENT IN VUNG TAU - CITY CENTER»
  * 1492880149322720 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ MỚI»
"""
from listing_lock import insert_listings

IDS = [3002166, 3002167, 3002168, 3002169, 3002170, 3002171, 3002172, 3002173, 3002174, 3002175, 3002176, 3002177, 3002178, 3002179, 3002180]

NEW_SRC = r'''
L(3002166,"da-nang","ns","Студия",6500000,30,
  "Студия, 30 м², Tran khanh Du 44, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1504029685223348/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="Studio, 30 m², Tran khanh Du 44, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1504029685223348/01.webp"], "am": ["w", "k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002167,"da-nang","ah","Квартира",18000000,None,
  "1-спальная квартира, Tô Hiến Thành, An Hải.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1501932988766351/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="1-bedroom flat, Tô Hiến Thành, An Hải.",
  details={"photos": ["assets/fb_photos/1501932988766351/01.webp", "assets/fb_photos/1501932988766351/02.webp", "assets/fb_photos/1501932988766351/03.webp", "assets/fb_photos/1501932988766351/04.webp", "assets/fb_photos/1501932988766351/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3002168,"da-nang","cl2","Квартира",6500000,None,
  "1-спальная квартира, Nguyễn Nhàn, Cẩm Lệ.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1763917225264586/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="1-bedroom flat, Nguyễn Nhàn, Cẩm Lệ.",
  details={"photos": ["assets/fb_photos/1763917225264586/01.webp", "assets/fb_photos/1763917225264586/02.webp", "assets/fb_photos/1763917225264586/03.webp", "assets/fb_photos/1763917225264586/04.webp", "assets/fb_photos/1763917225264586/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3002169,"da-nang","ah","Квартира",11000000,None,
  "1-спальная квартира, Đông Kinh Nghĩa Thục, An Hải.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2243209039640088/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="1-bedroom flat, Đông Kinh Nghĩa Thục, An Hải.",
  details={"photos": ["assets/fb_photos/2243209039640088/01.webp", "assets/fb_photos/2243209039640088/02.webp", "assets/fb_photos/2243209039640088/03.webp", "assets/fb_photos/2243209039640088/04.webp", "assets/fb_photos/2243209039640088/05.webp"], "am": ["pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3002170,"da-nang","ns","Квартира",9500000,None,
  "1-спальная квартира, Lê Quang Đạo, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2254261675201491/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="1-bedroom flat, Lê Quang Đạo, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2254261675201491/01.webp", "assets/fb_photos/2254261675201491/02.webp", "assets/fb_photos/2254261675201491/03.webp", "assets/fb_photos/2254261675201491/04.webp", "assets/fb_photos/2254261675201491/05.webp"], "fl": 3, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3002171,"hai-phong","lch","Квартира",7000000,40,
  "1-спальная квартира, 40 м², Lê Chân — 1 санузел.",
  "https://www.facebook.com/groups/v3homechothuenhahaiphong10/posts/1996726040963709/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="1-bedroom flat, 40 m², Lê Chân — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1996726040963709/01.webp", "assets/fb_photos/1996726040963709/02.webp", "assets/fb_photos/1996726040963709/03.webp", "assets/fb_photos/1996726040963709/04.webp", "assets/fb_photos/1996726040963709/05.webp"], "am": ["k", "lift", "gym"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002172,"ho-chi-minh","ak","Квартира",18000000,40,
  "1-спальная квартира, 40 м², An Khánh.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1802247057760684/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="1-bedroom flat, 40 m², An Khánh.",
  details={"photos": ["assets/fb_photos/1802247057760684/01.webp", "assets/fb_photos/1802247057760684/02.webp", "assets/fb_photos/1802247057760684/03.webp", "assets/fb_photos/1802247057760684/04.webp", "assets/fb_photos/1802247057760684/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002173,"manila","qzc","Дом",60000,190,
  "Дом, 190 м², Quezon City — 3 санузла.",
  "https://www.facebook.com/groups/715451165293916/posts/3462990163873322/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-13",
  descEn="House, 190 m², Quezon City — 3 bathrooms.",
  details={"photos": ["assets/fb_photos/3462990163873322/01.webp", "assets/fb_photos/3462990163873322/02.webp", "assets/fb_photos/3462990163873322/03.webp", "assets/fb_photos/3462990163873322/04.webp", "assets/fb_photos/3462990163873322/05.webp"], "am": ["pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002174,"nha-trang","ttr","Квартира",16500000,None,
  "2-спальная квартира, Tây Nha Trang.",
  "https://www.facebook.com/groups/chothue79/posts/4642245916044929/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="2-bedroom flat, Tây Nha Trang.",
  details={"photos": ["assets/fb_photos/4642245916044929/01.webp", "assets/fb_photos/4642245916044929/02.webp", "assets/fb_photos/4642245916044929/03.webp", "assets/fb_photos/4642245916044929/04.webp", "assets/fb_photos/4642245916044929/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002175,"nha-trang","btr","Дом",12500000,80,
  "2-спальный дом, 80 м², Bắc Nha Trang — 1 санузел.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2740913799674228/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="2-bedroom house, 80 m², Bắc Nha Trang — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2740913799674228/01.webp", "assets/fb_photos/2740913799674228/02.webp", "assets/fb_photos/2740913799674228/03.webp", "assets/fb_photos/2740913799674228/04.webp", "assets/fb_photos/2740913799674228/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002176,"nha-trang","ph","Квартира",20000000,91,
  "3-спальная квартира, 91 м², Phước Hải — 2 санузла.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1950686778960423/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="3-bedroom flat, 91 m², Phước Hải — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1950686778960423/01.webp", "assets/fb_photos/1950686778960423/02.webp", "assets/fb_photos/1950686778960423/03.webp", "assets/fb_photos/1950686778960423/04.webp", "assets/fb_photos/1950686778960423/05.webp"], "am": ["k", "pool", "gym"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002177,"nha-trang","btr","Дом",18000000,130,
  "1-спальный дом, 130 м², Bắc Nha Trang — 2 санузла.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1996062091089558/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="1-bedroom house, 130 m², Bắc Nha Trang — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1996062091089558/01.webp", "assets/fb_photos/1996062091089558/02.webp", "assets/fb_photos/1996062091089558/03.webp", "assets/fb_photos/1996062091089558/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002178,"nha-trang","btr","Квартира",8000000,50,
  "Квартира, 50 м², Bắc Nha Trang.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1996167737745660/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="Flat, 50 m², Bắc Nha Trang.",
  details={"photos": ["assets/fb_photos/1996167737745660/01.webp", "assets/fb_photos/1996167737745660/02.webp", "assets/fb_photos/1996167737745660/03.webp", "assets/fb_photos/1996167737745660/04.webp", "assets/fb_photos/1996167737745660/05.webp"], "am": ["w", "b", "win", "lift"], "fl": 4, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002179,"nha-trang","tl","Студия",3500000,20,
  "Студия, 20 м², Tân Lập.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1995396747822759/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="Studio, 20 m², Tân Lập.",
  details={"photos": ["assets/fb_photos/1995396747822759/01.webp", "assets/fb_photos/1995396747822759/02.webp", "assets/fb_photos/1995396747822759/03.webp", "assets/fb_photos/1995396747822759/04.webp", "assets/fb_photos/1995396747822759/05.webp"], "am": ["ws", "k"], "fl": 4, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3002180,"nha-trang","pl","Дом",40000000,75,
  "4-спальный дом, 75 м², Phước Long — 5 санузлов.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1994398034589297/","сегодня",0,source="fbgroup",postedOn="2026-10-13",
  descEn="4-bedroom house, 75 m², Phước Long — 5 bathrooms.",
  details={"photos": ["assets/fb_photos/1994398034589297/01.webp", "assets/fb_photos/1994398034589297/02.webp", "assets/fb_photos/1994398034589297/03.webp", "assets/fb_photos/1994398034589297/04.webp", "assets/fb_photos/1994398034589297/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
