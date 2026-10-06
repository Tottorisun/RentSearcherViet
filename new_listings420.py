# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 30 строк, 2026-10-06.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 563896434149922/2383302612209286 -- cebu/man, 18,000 PHP: район назван в адресе поста
  * 563896434149922/2369556196917261 -- cebu/tls, 15,000 PHP: район назван в адресе поста
  * 476056366996433/1658807542054637 -- da-nang/ns, 12,000,000 VND: «2-BEDROOM APARTMENT FOR RENT»: 3 строк сайта, все в ns
  * canhochungcudanang/2989131598147584 -- da-nang/hx, 7,000,000 VND: район назван в посте; улица Mẹ Thứ: 4 из 5 отрезков в hx; пост: Cam Le
  * canhochungcudanang/2987224998338244 -- da-nang/hk, 5,000,000 VND: улица Hồ Tùng Mậu: 8 из 8 отрезков в hk
  * canhochungcudanang/2987349481659129 -- da-nang/ns, 8,000,000 VND: район назван в посте; прежний район Ngu Hanh Son весь вошёл в этот; «1-BEDROOM APARTMENT FOR RENT»: 3 строк сайта, все в ns
  * canhochungcudanang/2988003308260413 -- da-nang/ah, 21,000,000 VND: улица Đỗ Anh Hàn: 2 из 2 отрезков в ah; пост: Son Tra
  * 1454201286459382/1580457130500463 -- da-nang/ns, 45,000,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * 1454201286459382/1581925173686992 -- da-nang/ns, 35,000,000 VND: «FOR RENT»: 4 строк сайта, все в ns
  * phongtrocanhonhadanang/1496918042601179 -- da-nang/ns, 16,000,000 VND: район назван в посте; «1-BEDROOM APARTMENT FOR RENT ✨»: 3 строк сайта, все в ns
  * phongtrocanhonhadanang/1495161229443527 -- da-nang/ah, 4,500,000 VND: улица Nguyễn Công Trứ: 5 из 5 отрезков в ah; пост: Son Tra
  * chothuecanhodanang43/1756559932666982 -- da-nang/ns, 11,000,000 VND: «1-Bedroom Apartment for Rent»: 3 строк сайта, все в ns
  * canhochothuedanangtot/2236476216980037 -- da-nang/ns, 12,000,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * canhochothuedanangtot/2221665295127796 -- da-nang/ns, 5,600,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * canhochothuedanangtot/2203496343611358 -- da-nang/ah, 10,000,000 VND: улица Hoàng Bích Sơn: 1 из 1 отрезков в ah; пост: Son Tra
  * canhochothuedanangtot/2245630299397962 -- da-nang/hx, 9,500,000 VND: район назван в посте; улица Cồn Dầu 25: 1 из 1 отрезков в hx
  * canhochothuedanangtot/2245612022733123 -- da-nang/ns, 8,500,000 VND: район назван в посте; прежний район Ngu Hanh Son весь вошёл в этот
  * canhochothuedanangtot/2245603999400592 -- da-nang/ah, 12,000,000 VND: район назван в посте; улица Võ Nghĩa: 1 из 1 отрезков в ah; пост: Son Tra
  * 807531664242245/1464410321887706 -- hue/acu, 15,000,000 VND: район назван в адресе поста
  * 715451165293916/3454038931435112 -- manila/prq, 13,000 PHP: «Parañaque»: 2 строк сайта, все в prq
  * 715451165293916/3454507284721610 -- manila/mdl, 70,000 PHP: район назван в адресе поста
  * 715451165293916/3443070299198642 -- manila/mdl, 22,000 PHP: район назван в адресе поста
  * chothuecanhogiarenhatrang/2060280514806050 -- nha-trang/tl, 15,000,000 VND: район назван в адресе поста
  * chothue79/4587623478173840 -- nha-trang/vp, 13,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2714566965642245 -- nha-trang/vp, 25,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2726864874412454 -- nha-trang/tl, 10,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2732262370539371 -- nha-trang/pl, 7,000,000 VND: район назван в адресе поста
  * nhatrang.apartment.and.house/2731973180568290 -- nha-trang/vp, 13,500,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1978201452875622 -- nha-trang/ph, 11,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1954919618537139 -- nha-trang/tl, 7,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (210):
  * 3474885602689740 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»
  * 3489735917871375 -- это поиск жилья, а не предложение
  * 3501758010002499 -- район не определяется по адресу «Nest5 Home»
  * 3466498576861776 -- район не определяется по адресу «Cho thuê nhà hẻm 102 Nguyễn Tất Thành»
  * 3121633828039610 -- район не определяется по адресу «☘️☘️ CHO THUÊ CHUNG CƯ HOÀNG ANH GIA LAI»
  * 2984311105105217 -- в посте несколько разных цен: 5,500,000, 6,000,000
  * 3111524002383926 -- это поиск жилья, а не предложение
  * 3086171178252542 -- район не определяется по адресу «Studio siêu đẹp»; прецедент расколот: «Eco City»: tanb 1
  * 3017264535143207 -- в посте несколько разных цен: 7,000,000, 7,500,000
  * 3059192510950409 -- тип жилья в тексте не назван
  * 4534963593485999 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 4535108773471481 -- район не определяется по адресу «Chủ gửi»
  * 4524078787907813 -- район не определяется по адресу «GIÁ THUÊ : 2.7 TRIỆU»
  * 4523929227922769 -- район не определяется по адресу «Chủ gửi - GIÁ THUÊ : 2.7 TRIỆU»
  * 4583088438673514 -- район не определяется по адресу «CĂN HỘ CAO CẤP KDC THỚI NHỰT FULL NỘI THẤT GẦN ĐH »
  * 4578192675829757 -- район не определяется по адресу «🥨🫜🍒 CĂN HỘ CAO CẤP MỚI XÂY KDC AN KHÁNH FULL NỘI T»
  * 4576672325981792 -- район не определяется по адресу «🛍️🎀 PHÒNG FULL NỘI THẤT CÓ BAN CÔNG ĐƯỜNG HOÀNG QU»; прецедент расколот: «ĐHCT»: tanc 1
  * 4585402665108758 -- тип жилья в тексте не назван
  * 2145630893006941 -- район не определяется по адресу «Chủ gửi»
  * 2145579633012067 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 2136097713960259 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NGUYỄN VĂN LI»
  * 2178278159742214 -- район не определяется по адресу «☸️🏚️📫MINIHOUSE CAO CẤP FULL NỘI THẤT - RỘNG 40M2 M»
  * 2192629371640426 -- район не определяется по адресу «🔮📭🌼CĂN MẶT TIỀN HẺM CÓ PHÒNG NGỦ RIÊNG ĐƯỜNG PHẠM »; прецедент расколот: «PHẠM NGŨ LÃO»: tanc 2, nki 1, anb 1
  * 2174816730088357 -- тип жилья в тексте не назван
  * 2129210777982286 -- район не определяется по адресу «CHO THUÊ CĂN HỘ TRUNG TÂM CẦN THƠ»
  * 2367341113805436 -- в посте несколько разных цен: 3,000, 4,500
  * 2397743264098554 -- в посте несколько разных цен: 9,000, 10,000
  * 2379455639260650 -- тип жилья в тексте не назван
  * 2384258058780408 -- район не определяется по адресу «ROOM FOR RENT: FEMALE ONLY 4K»
  * 2397178127488401 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2397460614126819 -- в посте несколько разных цен: 12,000, 18,000
  * 2371615766711304 -- в тексте есть и другая цена того же порядка: 7,833 против 18,000
  * 2392936531245894 -- в посте несколько разных цен: 9,000, 10,000
  * 2391426354730245 -- район не определяется по адресу «ROOM FOR RENT (FEMALE ONLY)»
  * 2384022142137333 -- район не определяется по адресу «EL ORLANDO VILLAGE»
  * 2348011072701363 -- район не определяется по адресу «Basak San Nicolas»
  * 4521497431443289 -- район не определяется по адресу «Bulacao Luyo Prince Warehouse»
  * 4568165530109812 -- в посте несколько разных цен: 12,000, 18,000
  * 4562745847318447 -- продажа
  * 4568197823439916 -- район не определяется по адресу «Basak San Nicolas»
  * 4555728451353520 -- тип жилья в тексте не назван
  * 4549148565344842 -- тип жилья в тексте не назван
  * 1628212845114107 -- похоже на уже заведённое: id 3001720
  * 1655398372395554 -- тот же текст уже заведён: id 3001884
  * 1589097499025642 -- тот же текст уже заведён: id 3001885
  * 1642026050399453 -- похоже на уже заведённое: id 3001604
  * 1650857336182991 -- район не определяется: «Vị trí thuận tiện, Làng Đại học, Phan Châu Trinh»
  * 1657385775530147 -- район не определяется: «Đường Hóa Sơn 4, Đà Nẵng, 3 phòng ngủ»; без диакритики это разные улицы: Hóa Sơn 4, Hỏa Sơn 4
  * 1651352766133448 -- тот же текст уже заведён: id 3001886
  * 1405547428455713 -- тот же текст уже заведён: id 3001887
  * 1405203591823430 -- тот же текст уже заведён: id 3001888
  * 1403955818614874 -- в посте несколько разных цен: 500,000, 4,200,000, 4,600,000, 5,000,000
  * 1404956358514820 -- район не определяется: «CẬP NHẬT CĂN HỘ TRỐNG, 03/10, Căn 402»
  * 1396653956011727 -- в посте несколько разных цен: 11,500,000, 13,500,000, 14,000,000
  * 1391899156487207 -- тот же текст уже заведён: id 3001889
  * 1400114168999039 -- это поиск жилья, а не предложение
  * 2374408800064133 -- тот же текст уже заведён: id 3001876
  * 2366385470866466 -- район не определяется: «🇻🇳2BR VILLA FOR RENT, SON TRA, DA NANG»
  * 2373490586822621 -- нет ни одной скачанной фотографии
  * 2368431490661864 -- район не определяется: «** 51 Tran Bach Dang, Da Nang, surrounded by restaurants»
  * 2372056313632715 -- тот же текст уже заведён: id 3001890
  * 2985124201881657 -- тот же текст уже заведён: id 3001873
  * 2977953042598773 -- район не определяется: «chung cư HAGL - 72 Hàm Nghi, HAGL Apartment - 72 Hàm Nghi, the city center»
  * 1578555537357289 -- тот же текст уже заведён: id 3001874
  * 1541482734397903 -- район не определяется: «Da Nang, 🏢 2 BEDROOM APARTMENT FOR RENT IN DA NANG 🌊»
  * 1571298261416350 -- это поиск жилья, а не предложение
  * 1579325383946971 -- нет ни одной скачанной фотографии
  * 1577195244159985 -- тип жилья в тексте не назван
  * 1496426262650357 -- в посте несколько разных цен: 7,000,000, 9,500,000
  * 1497339675892349 -- район не определяется: «the 4th floor, features a spacious balcony and a lovely view., An Nhơn 4 Street»
  * 1753307146325594 -- тот же текст уже заведён: id 3001878
  * 1749995506656758 -- улица Trưng Nữ Vương идёт через несколько районов (hcg 13, hc 6), а пост называет только прежний район Hai Chau
  * 1754680382854937 -- похоже на уже заведённое: id new:canhochungcudanang/2987349481659129
  * 1756431676013141 -- в посте несколько разных цен: 12,000,000, 13,500,000
  * 1756564899333152 -- цены в посте нет
  * 1756559822666993 -- район не определяется: «2-BEDROOM VILLA, HOI AN, Hoi An»
  * 2241901533104172 -- район не определяется: «FOR RENT: STUDIO 402, 85 HOANG BICH SON, DA NANG»
  * 2245610196066639 -- тот же текст уже заведён: id new:chothuecanhodanang43/1756559932666982
  * 2245607846066874 -- источники назвали разные районы: street=ns, ward=hx
  * 2329906251181055 -- район не определяется: «**HOUSE FOR RENT, 3 BEDROOMS, THANH KHÊ»
  * 2362667247904955 -- район не определяется: «2-BEDROOM HOUSE FOR RENT, CAM CHAU, HOI AN»
  * 2263786434234413 -- тип жилья в тексте не назван
  * 2244337472845976 -- в посте несколько разных цен: 2,800,000, 3,300,000
  * 2239733899973000 -- в посте несколько разных цен: 6,000,000, 6,300,000, 7,000,000, 8,000,000, 8,500,000, 9,000,000, 10,000,000, 11,000,000, 13,000,000, 18,000,000
  * 2230450230901367 -- тот же текст уже заведён: id 3001892
  * 2275943409685382 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2274703299809393 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2273544739925249 -- район не определяется по адресу «670 Đường Kim Giang ( Show room Vinfast )»; прецедент расколот: «Kim Giang»: hm 20, tx 4, hd 1
  * 1105631969126482 -- в посте несколько разных цен: 4,000,000, 6,000,000
  * 1084120737944272 -- тот же текст уже заведён: id 3001892
  * 1084124464610566 -- тот же текст уже заведён: id 3001893
  * 1293381509492986 -- район не определяется по адресу «Cho thuê căn hộ»
  * 4465741240343699 -- район не определяется по адресу «Cho thuê căn hộ»
  * 4533730846878071 -- район не определяется по адресу «K295. C.H.O T.H.U.Ê toà khách sạn căn hộ tại Văn C»
  * 4532395727011583 -- в посте несколько разных цен: 5,000,000, 6,500,000
  * 1874570790528310 -- в посте несколько разных цен: 5,000,000, 20,000,000
  * 1853134039338652 -- район не определяется по адресу «English below ⬇️»
  * 1865296498122406 -- тот же текст уже заведён: id 3001894
  * 1876023027049753 -- тип жилья в тексте не назван
  * 1858110785507644 -- тот же текст уже заведён: id 3001895
  * 1876575393661183 -- тип жилья в тексте не назван
  * 1975221100220978 -- район не определяется по адресу «Tran Quoc Thao Street»
  * 1982733252803096 -- район не определяется по адресу «HOT DEAL»
  * 1967788500964238 -- тот же текст уже заведён: id 3001896
  * 1962032718206483 -- в посте несколько разных цен: 6,000,000, 30,000,000
  * 1970229000720188 -- район не определяется по адресу «Apartment Details»
  * 1973529393723482 -- в посте несколько разных цен: 6,000,000, 30,000,000
  * 1980795949663493 -- район не определяется по адресу «**CHO THUÊ STAR HILL»
  * 1965348697874885 -- район не определяется по адресу «Nguyễn Bỉnh Khiêm»
  * 1977206003355821 -- тип жилья в тексте не назван
  * 2000628700620098 -- тип жилья в тексте не назван
  * 2001579740524994 -- район не определяется по адресу «Trảng Kèo 8»
  * 1977822679567367 -- район не определяется по адресу «BEACH LIFE IN HOI AN»
  * 2001539610529007 -- район не определяется по адресу «CHO THUÊ NHÀ GẦN PHỐ CỔ HỘI AN»
  * 1997355244280777 -- посуточно
  * 2000122124004089 -- в тексте есть и другая цена того же порядка: 38,334,700 против 18,000,000
  * 2027169491294767 -- район не определяется по адресу «Entire house for rent on Dinh Tien Hoang Street»
  * 2021506941861022 -- район не определяется по адресу «3-BEDROOM VILLA FOR RENT»
  * 2028982294446820 -- район не определяется по адресу «✨ YOUR OWN LITTLE SPACE!»
  * 2028195524525497 -- район не определяется по адресу «Cute»
  * 2020537728624610 -- район не определяется по адресу «a non-flooding area»
  * 2027618511249865 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 1998953254116391 -- район не определяется по адресу «Nhà 98m²»
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
  * 2029738977704485 -- район не определяется по адресу «Cozy private apartment in a convenient location»
  * 2009406873071029 -- район не определяется по адресу «2-BEDROOM GROUND-FLOOR APARTMENT FOR RENT»
  * 2026529394692110 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 1993632857981764 -- нет ни одной скачанной фотографии
  * 1287853898988310 -- в тексте есть и другая цена того же порядка: 4,568,736 против 4,000,000
  * 1407858374209568 -- район не определяется по адресу «Vị trí trung tâm»
  * 1466927818302623 -- похоже на уже заведённое: id new:807531664242245/1464410321887706
  * 1506528094342595 -- тип жилья в тексте не назван
  * 1507435977585140 -- в посте несколько разных цен: 500,000, 600,000
  * 1499726755022729 -- в посте несколько разных цен: 500,000, 600,000
  * 3452057211633284 -- район не определяется по адресу «Manila Residences Tower 2»
  * 3436429663196039 -- район не определяется по адресу «PET FRIENDLY. VIEWING THIS SATURDAY! (SEPT19)»
  * 3453659481473057 -- район не определяется по адресу «UNIT FEATURES:»
  * 3447452425427096 -- район не определяется по адресу «Minutes to BGC & McKinley Hill»
  * 3448430621995943 -- нет ни одной скачанной фотографии
  * 3447877042051301 -- тип жилья в тексте не назван
  * 2032166500794472 -- в посте несколько разных цен: 10,000, 12,500, 15,500
  * 2035107657167023 -- в посте несколько разных цен: 4,000, 4,500, 5,000
  * 2032143240796798 -- в посте несколько разных цен: 14,000, 15,000
  * 2035162927161496 -- тип жилья в тексте не назван
  * 2025675264776929 -- в посте несколько разных цен: 5,000, 6,000, 8,000, 9,000, 10,000, 12,000
  * 2022434191767703 -- нет ни одной скачанной фотографии
  * 2038684243476031 -- район не определяется по адресу «1022 Solis Street»
  * 2011944009483388 -- тип жилья в тексте не назван
  * 2032171387460650 -- район не определяется по адресу «Urban Deca homes»
  * 1097636699376885 -- район не определяется по адресу «📞📞 Contact +84901717411 via WhatsApp»
  * 1124229146717640 -- в посте несколько разных цен: 500,000, 18,500,000
  * 2080195716147863 -- похоже на уже заведённое: id 2000929
  * 2076181956549239 -- район не определяется по адресу «** Khanh Hoa»
  * 2074055276761907 -- район не определяется по адресу «**Khanh Hoa»
  * 2081008036066631 -- это поиск жилья, а не предложение
  * 4626748320928022 -- похоже на уже заведённое: id 2000946
  * 4628240987445422 -- район не определяется по адресу «1-BEDROOM APARTMENT FOR RENT ~ AIRY»
  * 4615612555374932 -- район не определяется по адресу «Muong Thanh 04 Tran Phu»
  * 4630547377214783 -- район не определяется по адресу «Brand-new apartment in the south of the city ~ Pet»
  * 4615648422038012 -- район не определяется по адресу «LUXURY 3-BEDROOM APARTMENT FOR RENT»; прецедент расколот: «GOLDCOAST»: nt 1
  * 4614743152128539 -- район не определяется по адресу «NT RENT»
  * 2645301635902112 -- в посте несколько разных цен: 700,000, 6,000,000, 8,000,000
  * 2720128521752756 -- район не определяется по адресу «CHO THUÊ STUDIO - GIÁ YÊU THƯƠNG»
  * 2731964543902487 -- район не определяется по адресу «South Nha Trang»
  * 2727443507687924 -- район не определяется по адресу «Prime location near the city center»
  * 2705811429851132 -- в посте несколько разных цен: 880,000, 40,000,000
  * 1989335031762264 -- тип жилья в тексте не назван
  * 1945533369475764 -- в посте несколько разных цен: 3,000,000, 3,500,000
  * 1981279022567865 -- район не определяется по адресу «Central location»
  * 1976587589703675 -- район не определяется по адресу «LVCC 🍃 Cho Thuê Nhà đường Thích Quảng Đức»; прецедент расколот: «LVCC»: nt 1
  * 1984318178930616 -- район не определяется по адресу «Tổng diện tích sàn: 195m²»
  * 1980800452615722 -- район не определяется по адресу «CHO THUÊ NHÀ 3 TẦNG»
  * 3840038072803406 -- район не определяется по адресу «APARTMENT FOR RENT»
  * 3849844405156106 -- в посте несколько разных цен: 500,000, 7,000,000
  * 3856254821181731 -- в посте несколько разных цен: 1,000,000, 14,000,000
  * 4742360189343383 -- район не определяется по адресу «fully furnished»
  * 2253829621529798/4743749845871084 -- лимит прогона (30) выбран
  * 2253829621529798/4743707395875329 -- лимит прогона (30) выбран
  * 4743699732542762 -- похоже на уже заведённое: id new:nhatrang.apartment.and.house/2732262370539371
  * 4743696429209759 -- адрес называет несколько районов: btr, vh
  * 4743690755876993 -- район не определяется по адресу «--lvcc--»; прецедент расколот: «lvcc»: nt 1
  * 2103428090314611 -- район не определяется по адресу «Central Nha Trang»
  * 2103086887015398 -- в посте несколько разных цен: 500,000, 18,000,000
  * 2102610263729727 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1172766863380743/2101944567129630 -- лимит прогона (30) выбран
  * 2103658440291576 -- адрес называет несколько районов: btr, vh
  * 2103634340293986 -- район не определяется по адресу «Ly Nam De»
  * 1172766863380743/2103628353627918 -- лимит прогона (30) выбран
  * 4623890491213805 -- район не определяется по адресу «Central location»
  * chothue79/4635199233416264 -- лимит прогона (30) выбран
  * 4633229313613256 -- район не определяется по адресу «1-BEDROOM APARTMENT»
  * 1763318494880834 -- район не определяется по адресу «CHO THUÊ VILLA PALM GARDEN»
  * 472474987298531/1715808856298465 -- лимит прогона (30) выбран
  * 1769689764243707 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2579623245791664 -- район не определяется по адресу «the prestigious Meyhomes community»
  * 2604061680014487 -- район не определяется по адресу «CHO THUÊ CĂN HỘ THEO THÁNG»
  * 2588243598262962 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * congdongphuquocnew/2599789720441683 -- лимит прогона (30) выбран
  * 2592618517825470 -- район не определяется по адресу «✨ Brand-new villa»
  * 1482580230352712 -- район не определяется по адресу «💥💥💥HOUSE FOR RENT💥💥💥»
  * 1480625103881558 -- район не определяется по адресу «🍀🍀🍀LOVELY HOUSE FOR RENT IN VUNG TAU - CITY CENTER»
"""
from listing_lock import insert_listings

IDS = [3001967, 3001968, 3001969, 3001970, 3001971, 3001972, 3001973, 3001974, 3001975, 3001976, 3001977, 3001978, 3001979, 3001980, 3001981, 3001982, 3001983, 3001984, 3001985, 3001986, 3001987, 3001988, 3001989, 3001990, 3001991, 3001992, 3001993, 3001994, 3001995, 3001996]

NEW_SRC = r'''
L(3001967,"cebu","man","Квартира",18000,36,
  "2-спальная квартира, 36 м², Mandaue.",
  "https://www.facebook.com/groups/563896434149922/posts/2383302612209286/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-06",
  descEn="2-bedroom flat, 36 m², Mandaue.",
  details={"photos": ["assets/fb_photos/2383302612209286/01.webp", "assets/fb_photos/2383302612209286/02.webp", "assets/fb_photos/2383302612209286/03.webp", "assets/fb_photos/2383302612209286/04.webp", "assets/fb_photos/2383302612209286/05.webp"], "am": ["k", "b", "win"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001968,"cebu","tls","Квартира",15000,None,
  "1-спальная квартира, Talisay.",
  "https://www.facebook.com/groups/563896434149922/posts/2369556196917261/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-06",
  descEn="1-bedroom flat, Talisay.",
  details={"photos": ["assets/fb_photos/2369556196917261/01.webp", "assets/fb_photos/2369556196917261/02.webp", "assets/fb_photos/2369556196917261/03.webp", "assets/fb_photos/2369556196917261/04.webp", "assets/fb_photos/2369556196917261/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001969,"da-nang","ns","Квартира",12000000,None,
  "2-спальная квартира, APARTMENT FOR RENT, Ngũ Hành Sơn — 2 санузла.",
  "https://www.facebook.com/groups/476056366996433/posts/1658807542054637/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="2-bedroom flat, APARTMENT FOR RENT, Ngũ Hành Sơn — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1658807542054637/01.webp", "assets/fb_photos/1658807542054637/02.webp", "assets/fb_photos/1658807542054637/03.webp", "assets/fb_photos/1658807542054637/04.webp"], "am": ["pool"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001970,"da-nang","hx","Квартира",7000000,None,
  "1-спальная квартира, Mẹ Thứ, Hòa Xuân.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2989131598147584/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, Mẹ Thứ, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/2989131598147584/01.webp", "assets/fb_photos/2989131598147584/02.webp", "assets/fb_photos/2989131598147584/03.webp", "assets/fb_photos/2989131598147584/04.webp", "assets/fb_photos/2989131598147584/05.webp"], "am": ["win", "lift"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001971,"da-nang","hk","Квартира",5000000,None,
  "1-спальная квартира, Hồ Tùng Mậu, Hòa Khánh.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2987224998338244/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, Hồ Tùng Mậu, Hòa Khánh.",
  details={"photos": ["assets/fb_photos/2987224998338244/01.webp", "assets/fb_photos/2987224998338244/02.webp", "assets/fb_photos/2987224998338244/03.webp", "assets/fb_photos/2987224998338244/04.webp", "assets/fb_photos/2987224998338244/05.webp"], "fl": 5, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001972,"da-nang","ns","Квартира",8000000,None,
  "1-спальная квартира, APARTMENT FOR RENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2987349481659129/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, APARTMENT FOR RENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2987349481659129/01.webp", "assets/fb_photos/2987349481659129/02.webp", "assets/fb_photos/2987349481659129/03.webp", "assets/fb_photos/2987349481659129/04.webp", "assets/fb_photos/2987349481659129/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001973,"da-nang","ah","Квартира",21000000,None,
  "2-спальная квартира, Đỗ Anh Hàn, An Hải.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2988003308260413/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="2-bedroom flat, Đỗ Anh Hàn, An Hải.",
  details={"photos": ["assets/fb_photos/2988003308260413/01.webp", "assets/fb_photos/2988003308260413/02.webp", "assets/fb_photos/2988003308260413/03.webp", "assets/fb_photos/2988003308260413/04.webp", "assets/fb_photos/2988003308260413/05.webp"], "am": ["w", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001974,"da-nang","ns","Дом",45000000,100,
  "4-спальный дом, 100 м², quiet, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/1454201286459382/posts/1580457130500463/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="4-bedroom house, 100 m², quiet, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1580457130500463/01.webp", "assets/fb_photos/1580457130500463/02.webp", "assets/fb_photos/1580457130500463/03.webp", "assets/fb_photos/1580457130500463/04.webp", "assets/fb_photos/1580457130500463/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001975,"da-nang","ns","Квартира",35000000,114,
  "2-спальная квартира, 114 м², FOR RENT, Ngũ Hành Sơn — 2 санузла.",
  "https://www.facebook.com/groups/1454201286459382/posts/1581925173686992/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="2-bedroom flat, 114 m², FOR RENT, Ngũ Hành Sơn — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1581925173686992/01.webp", "assets/fb_photos/1581925173686992/02.webp", "assets/fb_photos/1581925173686992/03.webp", "assets/fb_photos/1581925173686992/04.webp", "assets/fb_photos/1581925173686992/05.webp"], "am": ["pool", "gym"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001976,"da-nang","ns","Квартира",16000000,None,
  "1-спальная квартира, APARTMENT FOR RENT ✨, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1496918042601179/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, APARTMENT FOR RENT ✨, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1496918042601179/01.webp", "assets/fb_photos/1496918042601179/02.webp", "assets/fb_photos/1496918042601179/03.webp", "assets/fb_photos/1496918042601179/04.webp", "assets/fb_photos/1496918042601179/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001977,"da-nang","ah","Студия",4500000,None,
  "Студия, Nguyễn Công Trứ, An Hải.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1495161229443527/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="Studio, Nguyễn Công Trứ, An Hải.",
  details={"photos": ["assets/fb_photos/1495161229443527/01.webp", "assets/fb_photos/1495161229443527/02.webp", "assets/fb_photos/1495161229443527/03.webp", "assets/fb_photos/1495161229443527/04.webp", "assets/fb_photos/1495161229443527/05.webp"], "am": ["w", "k", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001978,"da-nang","ns","Квартира",11000000,None,
  "1-спальная квартира, Apartment for Rent, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1756559932666982/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, Apartment for Rent, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1756559932666982/01.webp", "assets/fb_photos/1756559932666982/02.webp", "assets/fb_photos/1756559932666982/03.webp", "assets/fb_photos/1756559932666982/04.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001979,"da-nang","ns","Квартира",12000000,None,
  "1-спальная квартира, **Chung cư Mường Thanh, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2236476216980037/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, **Chung cư Mường Thanh, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2236476216980037/01.webp", "assets/fb_photos/2236476216980037/02.webp", "assets/fb_photos/2236476216980037/03.webp", "assets/fb_photos/2236476216980037/04.webp", "assets/fb_photos/2236476216980037/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001980,"da-nang","ns","Квартира",5600000,None,
  "Квартира, FULLY FURNISHED APARTMENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2221665295127796/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="Flat, FULLY FURNISHED APARTMENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2221665295127796/01.webp", "assets/fb_photos/2221665295127796/02.webp", "assets/fb_photos/2221665295127796/03.webp", "assets/fb_photos/2221665295127796/04.webp", "assets/fb_photos/2221665295127796/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001981,"da-nang","ah","Квартира",10000000,None,
  "1-спальная квартира, Hoàng Bích Sơn, An Hải.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2203496343611358/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, Hoàng Bích Sơn, An Hải.",
  details={"photos": ["assets/fb_photos/2203496343611358/01.webp", "assets/fb_photos/2203496343611358/02.webp", "assets/fb_photos/2203496343611358/03.webp", "assets/fb_photos/2203496343611358/04.webp", "assets/fb_photos/2203496343611358/05.webp"], "am": ["w", "b", "win"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001982,"da-nang","hx","Квартира",9500000,None,
  "1-спальная квартира, Cồn Dầu 25, Hòa Xuân.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2245630299397962/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, Cồn Dầu 25, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/2245630299397962/01.webp", "assets/fb_photos/2245630299397962/02.webp", "assets/fb_photos/2245630299397962/03.webp", "assets/fb_photos/2245630299397962/04.webp"], "am": ["w", "b", "pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001983,"da-nang","ns","Квартира",8500000,None,
  "1-спальная квартира, FULLY FURNISHED APARTMENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2245612022733123/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, FULLY FURNISHED APARTMENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2245612022733123/01.webp", "assets/fb_photos/2245612022733123/02.webp", "assets/fb_photos/2245612022733123/03.webp", "assets/fb_photos/2245612022733123/04.webp", "assets/fb_photos/2245612022733123/05.webp"], "am": ["w", "k", "b", "lift"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001984,"da-nang","ah","Квартира",12000000,40,
  "1-спальная квартира, 40 м², Võ Nghĩa, An Hải.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2245603999400592/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, 40 m², Võ Nghĩa, An Hải.",
  details={"photos": ["assets/fb_photos/2245603999400592/01.webp", "assets/fb_photos/2245603999400592/02.webp", "assets/fb_photos/2245603999400592/03.webp", "assets/fb_photos/2245603999400592/04.webp", "assets/fb_photos/2245603999400592/05.webp"], "am": ["pool", "gym"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001985,"hue","acu","Дом",15000000,81,
  "Дом, 81 м², An Cựu.",
  "https://www.facebook.com/groups/807531664242245/posts/1464410321887706/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="House, 81 m², An Cựu.",
  details={"photos": ["assets/fb_photos/1464410321887706/01.webp", "assets/fb_photos/1464410321887706/02.webp", "assets/fb_photos/1464410321887706/03.webp", "assets/fb_photos/1464410321887706/04.webp", "assets/fb_photos/1464410321887706/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001986,"manila","prq","Студия",13000,None,
  "Студия, Parañaque, Parañaque / BF Homes.",
  "https://www.facebook.com/groups/715451165293916/posts/3454038931435112/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-06",
  descEn="Studio, Parañaque, Parañaque / BF Homes.",
  details={"photos": ["assets/fb_photos/3454038931435112/01.webp", "assets/fb_photos/3454038931435112/02.webp", "assets/fb_photos/3454038931435112/03.webp", "assets/fb_photos/3454038931435112/04.webp", "assets/fb_photos/3454038931435112/05.webp"], "am": ["w", "pool", "gym", "pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001987,"manila","mdl","Квартира",70000,80,
  "2-спальная квартира, 80 м², Mandaluyong — 2 санузла.",
  "https://www.facebook.com/groups/715451165293916/posts/3454507284721610/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-06",
  descEn="2-bedroom flat, 80 m², Mandaluyong — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/3454507284721610/01.webp", "assets/fb_photos/3454507284721610/02.webp", "assets/fb_photos/3454507284721610/03.webp", "assets/fb_photos/3454507284721610/04.webp", "assets/fb_photos/3454507284721610/05.webp"], "am": ["b", "pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001988,"manila","mdl","Квартира",22000,None,
  "1-спальная квартира, Mandaluyong.",
  "https://www.facebook.com/groups/715451165293916/posts/3443070299198642/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-06",
  descEn="1-bedroom flat, Mandaluyong.",
  details={"photos": ["assets/fb_photos/3443070299198642/01.webp", "assets/fb_photos/3443070299198642/02.webp", "assets/fb_photos/3443070299198642/03.webp", "assets/fb_photos/3443070299198642/04.webp", "assets/fb_photos/3443070299198642/05.webp"], "am": ["k", "b", "pool", "gym", "pet"], "fl": 8, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001989,"nha-trang","tl","Квартира",15000000,62,
  "2-спальная квартира, 62 м², Tân Lập — 2 санузла.",
  "https://www.facebook.com/groups/chothuecanhogiarenhatrang/posts/2060280514806050/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="2-bedroom flat, 62 m², Tân Lập — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/2060280514806050/01.webp", "assets/fb_photos/2060280514806050/02.webp", "assets/fb_photos/2060280514806050/03.webp", "assets/fb_photos/2060280514806050/04.webp", "assets/fb_photos/2060280514806050/05.webp"], "flHigh": 1, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001990,"nha-trang","vp","Квартира",13000000,None,
  "2-спальная квартира, Vĩnh Phước.",
  "https://www.facebook.com/groups/chothue79/posts/4587623478173840/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="2-bedroom flat, Vĩnh Phước.",
  details={"photos": ["assets/fb_photos/4587623478173840/01.webp", "assets/fb_photos/4587623478173840/02.webp", "assets/fb_photos/4587623478173840/03.webp", "assets/fb_photos/4587623478173840/04.webp", "assets/fb_photos/4587623478173840/05.webp"], "am": ["win", "gym", "pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001991,"nha-trang","vp","Квартира",25000000,None,
  "Квартира, Vĩnh Phước — 1 санузел.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2714566965642245/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="Flat, Vĩnh Phước — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2714566965642245/01.webp", "assets/fb_photos/2714566965642245/02.webp", "assets/fb_photos/2714566965642245/03.webp", "assets/fb_photos/2714566965642245/04.webp", "assets/fb_photos/2714566965642245/05.webp"], "am": ["w", "k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001992,"nha-trang","tl","Квартира",10000000,None,
  "1-спальная квартира, Tân Lập.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2726864874412454/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, Tân Lập.",
  details={"photos": ["assets/fb_photos/2726864874412454/01.webp", "assets/fb_photos/2726864874412454/02.webp", "assets/fb_photos/2726864874412454/03.webp", "assets/fb_photos/2726864874412454/04.webp", "assets/fb_photos/2726864874412454/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001993,"nha-trang","pl","Квартира",7000000,35,
  "1-спальная квартира, 35 м², Phước Long.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2732262370539371/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, 35 m², Phước Long.",
  details={"photos": ["assets/fb_photos/2732262370539371/01.webp", "assets/fb_photos/2732262370539371/02.webp", "assets/fb_photos/2732262370539371/03.webp", "assets/fb_photos/2732262370539371/04.webp", "assets/fb_photos/2732262370539371/05.webp"], "am": ["w", "b", "win"], "fl": 2, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001994,"nha-trang","vp","Квартира",13500000,None,
  "1-спальная квартира, Vĩnh Phước.",
  "https://www.facebook.com/groups/nhatrang.apartment.and.house/posts/2731973180568290/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="1-bedroom flat, Vĩnh Phước.",
  details={"photos": ["assets/fb_photos/2731973180568290/01.webp", "assets/fb_photos/2731973180568290/02.webp", "assets/fb_photos/2731973180568290/03.webp", "assets/fb_photos/2731973180568290/04.webp", "assets/fb_photos/2731973180568290/05.webp"], "am": ["b", "win", "pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001995,"nha-trang","ph","Квартира",11000000,65,
  "Квартира, 65 м², Bùi Thiện Ngộ, Phước Hải.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1978201452875622/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="Flat, 65 m², Bùi Thiện Ngộ, Phước Hải.",
  details={"photos": ["assets/fb_photos/1978201452875622/01.webp", "assets/fb_photos/1978201452875622/02.webp", "assets/fb_photos/1978201452875622/03.webp", "assets/fb_photos/1978201452875622/04.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001996,"nha-trang","tl","Квартира",7000000,30,
  "Квартира, 30 м², Tân Lập.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1954919618537139/","сегодня",0,source="fbgroup",postedOn="2026-10-06",
  descEn="Flat, 30 m², Tân Lập.",
  details={"photos": ["assets/fb_photos/1954919618537139/01.webp", "assets/fb_photos/1954919618537139/02.webp", "assets/fb_photos/1954919618537139/03.webp", "assets/fb_photos/1954919618537139/04.webp", "assets/fb_photos/1954919618537139/05.webp"], "am": ["w", "win", "lift"], "fl": 6, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
