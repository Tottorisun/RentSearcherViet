# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 30 строк, 2026-10-05.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * rentcebu/28255246164174142 -- cebu/man, 35,000 PHP: район назван в адресе поста
  * cebu.tambayan.2/28677928168537286 -- cebu/tls, 28,000 PHP: район назван в адресе поста
  * phongtrodalat/3672523882904713 -- da-lat/cl, 15,000,000 VND: район назван в адресе поста
  * canhochungcudanang/2985124201881657 -- da-nang/ns, 9,000,000 VND: район назван в посте
  * 1454201286459382/1578555537357289 -- da-nang/ah, 10,000,000 VND: район назван в посте; улица Lê Ninh: 1 из 1 отрезков в ah
  * 203559903815711/2375416663296680 -- da-nang/ns, 7,000,000 VND: улица Trương Văn Hiến: 1 из 1 отрезков в ns
  * 203559903815711/2374408800064133 -- da-nang/ns, 9,000,000 VND: район назван в посте
  * 203559903815711/2374477963390550 -- da-nang/ns, 11,000,000 VND: район назван в посте
  * chothuecanhodanang43/1753307146325594 -- da-nang/ah, 21,000,000 VND: улица Phước Trường 3: 1 из 1 отрезков в ah
  * chothuecanhodanang43/1752796116376697 -- da-nang/ns, 8,500,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * canhochothuedanangtot/2243290389631953 -- da-nang/ah, 9,000,000 VND: район назван в посте
  * canhochothuedanangtot/2243119016315757 -- da-nang/ah, 12,000,000 VND: улица An Đồn 6: 1 из 1 отрезков в ah; пост: Son Tra
  * phongtrocanhonhadanang/1491835269776123 -- da-nang/ah, 6,500,000 VND: район назван в посте
  * phongtrocanhonhadanang/1461522199474097 -- da-nang/ah, 11,000,000 VND: улица Lý Thánh Tông: 1 из 1 отрезков в ah; пост: Son Tra
  * 476056366996433/1655398372395554 -- da-nang/hx, 15,000,000 VND: район назван в посте
  * 476056366996433/1589097499025642 -- da-nang/ah, 40,000,000 VND: улица Đặng Vũ Hỷ: 1 из 1 отрезков в ah; пост: Son Tra
  * 476056366996433/1651352766133448 -- da-nang/ah, 12,000,000 VND: улица Dương Đình Nghệ: 5 из 5 отрезков в ah
  * 728946289449167/1405547428455713 -- da-nang/hx, 6,000,000 VND: район назван в посте; улица Nguyễn Thị Sáu: 1 из 1 отрезков в hx
  * 728946289449167/1405203591823430 -- da-nang/ns, 7,500,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * 728946289449167/1391899156487207 -- da-nang/ns, 11,000,000 VND: район назван в посте
  * 203559903815711/2372056313632715 -- da-nang/ns, 14,000,000 VND: улица Trương Quang Được: 1 из 1 отрезков в ns
  * 153191128587086/2249949128911265 -- dumaguete/dau, 29,500 PHP: район назван в адресе поста
  * nhatrogiarenhat/2230450230901367 -- ha-noi/bd, 11,000,000 VND: район назван в адресе поста
  * chungcuminigiarehanoii/1084124464610566 -- ha-noi/hm, 5,200,000 VND: район назван в адресе поста; «Thinh Liet»: 3 строк сайта, все в hm
  * chungcumini.canhodichvu.phongtrotphcm/1865296498122406 -- ho-chi-minh/ak, 13,800,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1858110785507644 -- ho-chi-minh/ak, 13,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1967788500964238 -- ho-chi-minh/ak, 20,000,000 VND: район назван в адресе поста
  * phongtrochothuehue/2044199632954479 -- hue/acu, 2,900,000 VND: район назван в адресе поста
  * phongtrosvhue/1739874880555153 -- hue/vyd, 8,500,000 VND: район назван в адресе поста
  * phongtrosvhue/1550648672811109 -- hue/vyd, 3,700,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (211):
  * 3474885602689740 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»; прецедент расколот: «Đồng Sỹ Bình»: bmt 1
  * 3489735917871375 -- это поиск жилья, а не предложение
  * 3501758010002499 -- район не определяется по адресу «Nest5 Home»
  * 3466498576861776 -- район не определяется по адресу «Cho thuê nhà hẻm 102 Nguyễn Tất Thành»
  * 3121633828039610 -- район не определяется по адресу «☘️☘️ CHO THUÊ CHUNG CƯ HOÀNG ANH GIA LAI»
  * 2984311105105217 -- в посте несколько разных цен: 5,500,000, 6,000,000
  * 3111524002383926 -- это поиск жилья, а не предложение
  * 3086171178252542 -- район не определяется по адресу «Studio siêu đẹp»; прецедент расколот: «Eco City»: tanb 1
  * 3017264535143207 -- в посте несколько разных цен: 7,000,000, 7,500,000
  * 3059192510950409 -- тип жилья в тексте не назван
  * 1757290509336915 -- цена 650,000 VND вне разумных пределов
  * 1725575419175091 -- тип жилья в тексте не назван
  * 1777096620689637 -- район не определяется по адресу «🔮📭🌼CĂN MẶT TIỀN HẺM CÓ PHÒNG NGỦ RIÊNG ĐƯỜNG PHẠM »; прецедент расколот: «PHẠM NGŨ LÃO»: tanc 2, nki 1, anb 1
  * 1775069377559028 -- район не определяется по адресу «🏚️💠🍩CĂN MẶT TIỀN HẺM CÓ PHÒNG NGỦ RIÊNG ĐƯỜNG PHẠM»; прецедент расколот: «PHẠM NGŨ LÃO»: tanc 2, nki 1, anb 1
  * 1776196584112974 -- район не определяется по адресу «🍩📭🏵️CĂN MẶT TIỀN HẺM CÓ PHÒNG NGỦ RIÊNG ĐƯỜNG PHẠM»; прецедент расколот: «PHẠM NGŨ LÃO»: tanc 2, nki 1, anb 1
  * 1773617367704229 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1758617719204194 -- тип жилья в тексте не назван
  * 1772660991133200 -- тип жилья в тексте не назван
  * 1763351818730784 -- тип жилья в тексте не назван
  * 1757674389298527 -- тип жилья в тексте не назван
  * 28214337764931649 -- район не определяется по адресу «**Marco Polo»
  * 28252464834452275 -- адрес называет несколько районов: bnl, mac, man
  * 27857258347306261 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 28263068256725266 -- район не определяется по адресу «Kasambagan»
  * 28269659312732827 -- район не определяется по адресу «APARTMENT FOR RENT‼️»
  * 28239174759114616 -- в посте несколько разных цен: 12,000, 18,000
  * 27929073140124781 -- в тексте есть и другая цена того же порядка: 7,833 против 18,000
  * 28120444450987648 -- в посте несколько разных цен: 3,000, 22,000
  * 28189540407411385 -- тот же текст уже заведён: id 3001602
  * 28213649528333806 -- район не определяется по адресу «1 bedroom near gillesania review center Duterte St»
  * 28745578288438940 -- район не определяется по адресу «House for Rent in RIVA RIDGE SUBDIVISION LUPA TISA»
  * 28747923394871096 -- в тексте есть и другая цена того же порядка: 2,026 против 4,000
  * 28745577611772341 -- в тексте есть и другая цена того же порядка: 9,385 против 10,000
  * 28730941179902651 -- район не определяется по адресу «Apartment for RENT in PUNTA princesa»
  * 28723896340607135 -- продажа
  * 28735517596111676 -- цена 2,500 PHP вне разумных пределов
  * 2378291642990251 -- в посте несколько разных цен: 700,000, 15,000,000
  * 2380290386123710 -- район не определяется по адресу «/ Location:** Đường Mạc Đĩnh Chi»
  * 2379994232819992 -- это поиск жилья, а не предложение
  * 2380102169475865 -- в посте несколько разных цен: 700,000, 15,000,000
  * 2378011466351602 -- район не определяется по адресу «DALAT APARTMENT FOR RENT:»
  * 2380358586116890 -- район не определяется по адресу «1-BEDROOM APARTMENT FOR RENT»
  * 2125924031352847 -- это поиск жилья, а не предложение
  * 2134554663823117 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 2080210199257564 -- это поиск жилья, а не предложение
  * 3777462915744142 -- район не определяется по адресу «/ Location:** Đường Mạc Đĩnh Chi»
  * 3752397751583992 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 3586443918179377 -- район не определяется по адресу «✅ Apartment for Rent - 2 Bedrooms - Truong Van Hoa»
  * 3738232963000471 -- помещение под бизнес или здание целиком, а не жильё
  * 2071715403440377 -- нет ни одной скачанной фотографии
  * 2051576832120901 -- в посте несколько разных цен: 6,500,000, 7,500,000
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2977062496021161 -- район не определяется: «CHO THUÊ CĂN HỘ CAO CẤP HYORI, ĐÀ NẴNG, HYORI PREMIUM 2-BEDROOM APARTMENT FOR RENT»
  * 2987349481659129 -- похоже на уже заведённое: id 3001529
  * 2987875474939863 -- район не определяется: «APARTMENT FOR RENT, FULLY FURNISHED»
  * 2986897831704294 -- район не определяется: «1 Bedroom Apartment, 🏠1 Bedroom Apartment»
  * 1578965567316286 -- район не определяется: «WHOLE HOUSE FOR RENT, 3BR, 2BATH»
  * 1580606683818841 -- тип жилья в тексте не назван
  * 1580672763812233 -- район не определяется: «Usable area: 200m², # **LUXURY 4-STORY HOUSE FOR RENT, YEN BAI ALLEY»
  * 1581193333760176 -- это поиск жилья, а не предложение
  * 1571298261416350 -- это поиск жилья, а не предложение
  * 1580505813828928 -- это поиск жилья, а не предложение
  * 1578930237319819 -- в посте несколько разных цен: 15,000,000, 20,000,000
  * 2366385470866466 -- район не определяется: «🇻🇳2BR VILLA FOR RENT, SON TRA, DA NANG»
  * 2365039657667714 -- район не определяется: «2-BEDROOM HOUSE FOR RENT, DIEN BIEN PHU STREET, DA NANG»
  * 2373490586822621 -- район не определяется: «💐 House for rent at K249/59 on Ha Huy Tap Street»
  * 2371825186989161 -- в посте несколько разных цен: 1,000,000, 1,500,000, 6,500,000
  * 1754541842868791 -- район не определяется: «the 6th floor with a large, airy balcony and a beautiful view, Duong Tri Trach Street»
  * 1754486922874283 -- район не определяется: «1-BEDROOM APARTMENT FOR RENT, LE LO, 🏡 1-BEDROOM APARTMENT FOR RENT»
  * 1754423429547299 -- похоже на уже заведённое: id 1016854
  * 1753717879617854 -- похоже на уже заведённое: id 1021530
  * 1754467719542870 -- в посте несколько разных цен: 12,000,000, 13,000,000
  * 1753404436315865 -- улица Đinh Đạt лежит вне районов сайта (вне 1)
  * 2241901533104172 -- район не определяется: «FOR RENT: STUDIO 402, 85 HOANG BICH SON, DA NANG»
  * 2214431699184489 -- район не определяется: «LUXURY PRIVATE HOUSE FOR RENT, DA NANG, EACH UNIT FEATURES:»
  * 2242107353083590 -- в посте несколько разных цен: 11,000,000, 13,000,000
  * 2226528471308145 -- тип жилья в тексте не назван
  * 2241967123097613 -- район не определяется: «1-BEDROOM APARTMENT FOR RENT, NGUYEN XUAN KHOAT, Nguyen Xuan Khoat»
  * 1495856392707344 -- в посте несколько разных цен: 12,000,000, 14,000,000
  * 1495505776075739 -- район не определяется: «the 6th floor with a large, airy balcony and a beautiful view, Duong Tri Trach Street»
  * 1496368979322752 -- цена 500,000 VND вне разумных пределов
  * 1628212845114107 -- похоже на уже заведённое: id 3001720
  * 1642026050399453 -- район не определяется: «FOR RENT, 2-BEDROOM APARTMENT, MIA CENTER POINT»
  * 1658807542054637 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT, 2 BATHROOMS, MIA PLAZA»
  * 1650857336182991 -- район не определяется: «Vị trí thuận tiện, Làng Đại học, Phan Châu Trinh»
  * 1657385775530147 -- район не определяется: «Đường Hóa Sơn 4, Đà Nẵng, 3 phòng ngủ»; без диакритики это разные улицы: Hóa Sơn 4, Hỏa Sơn 4
  * 1403955818614874 -- в посте несколько разных цен: 500,000, 4,200,000, 4,600,000, 5,000,000
  * 1404956358514820 -- район не определяется: «CẬP NHẬT CĂN HỘ TRỐNG, 03/10, Căn 402»
  * 1396653956011727 -- в посте несколько разных цен: 11,500,000, 13,500,000, 14,000,000
  * 1400114168999039 -- это поиск жилья, а не предложение
  * 2368431490661864 -- район не определяется: «** 51 Tran Bach Dang, Da Nang, surrounded by restaurants»
  * 2252555391983972 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2248106355762209 -- район не определяется по адресу «HOUSE FOR RENT»
  * 2249715358934642 -- тип жилья в тексте не назван
  * 2240689496503895 -- тип жилья в тексте не назван
  * 2246076275965217 -- нет ни одной скачанной фотографии
  * 2263786434234413 -- тип жилья в тексте не назван
  * 2244337472845976 -- в посте несколько разных цен: 2,800,000, 3,300,000
  * 2239733899973000 -- в посте несколько разных цен: 6,000,000, 6,300,000, 7,000,000, 8,000,000, 8,500,000, 9,000,000, 10,000,000, 11,000,000, 13,000,000, 18,000,000
  * 2275943409685382 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2274703299809393 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2273544739925249 -- район не определяется по адресу «670 Đường Kim Giang ( Show room Vinfast )»; прецедент расколот: «Kim Giang»: hm 20, tx 4
  * 1105631969126482 -- в посте несколько разных цен: 4,000,000, 6,000,000
  * 1084120737944272 -- тот же текст уже заведён: id new:nhatrogiarenhat/2230450230901367
  * 1293381509492986 -- район не определяется по адресу «Cho thuê căn hộ»
  * 4465741240343699 -- район не определяется по адресу «Cho thuê căn hộ»
  * 4533730846878071 -- район не определяется по адресу «K295. C.H.O T.H.U.Ê toà khách sạn căn hộ tại Văn C»
  * 4532395727011583 -- в посте несколько разных цен: 5,000,000, 6,500,000
  * 1874570790528310 -- в посте несколько разных цен: 5,000,000, 20,000,000
  * 1853134039338652 -- район не определяется по адресу «English below ⬇️»
  * 1876023027049753 -- тип жилья в тексте не назван
  * 1876575393661183 -- тип жилья в тексте не назван
  * 1975221100220978 -- район не определяется по адресу «Tran Quoc Thao Street»
  * 1982733252803096 -- район не определяется по адресу «HOT DEAL»
  * 1962032718206483 -- в посте несколько разных цен: 6,000,000, 30,000,000
  * 1970229000720188 -- район не определяется по адресу «Apartment Details»
  * 1973529393723482 -- в посте несколько разных цен: 6,000,000, 30,000,000
  * 1980795949663493 -- район не определяется по адресу «**CHO THUÊ STAR HILL»
  * 1965348697874885 -- район не определяется по адресу «Nguyễn Bỉnh Khiêm»
  * 1977206003355821 -- тип жилья в тексте не назван
  * 1947495812624862 -- район не определяется по адресу «STUDIO FULL NỘI THẤT»
  * 2040218203352622 -- район не определяется по адресу «CHO THUÊ PHÒNG DÀI HẠN»
  * 1997802540927522 -- район не определяется по адресу «đường Tố Hữu»
  * 1680724936470148 -- тип жилья в тексте не назван
  * 1692451368630838 -- тип жилья в тексте не назван
  * 1691615248714450 -- в посте несколько разных цен: 6,000,000, 8,000,000
  * 1708277650381543 -- район не определяется по адресу «CHO THUÊ STUDIO CAO CẤP»
  * 1761093448433296 -- район не определяется по адресу «PHÒNG STUDIO TẦNG 3»
  * 1637646127444696 -- район не определяется по адресу «Không gian sống hiện đại»
  * 1251745672701412 -- в посте несколько разных цен: 4,000,000, 4,500,000, 4,800,000
  * 3452057211633284 -- район не определяется по адресу «Manila Residences Tower 2»
  * 715451165293916/3454038931435112 -- лимит прогона (30) выбран
  * 3436429663196039 -- район не определяется по адресу «PET FRIENDLY. VIEWING THIS SATURDAY! (SEPT19)»
  * 3453659481473057 -- район не определяется по адресу «UNIT FEATURES:»
  * 3447452425427096 -- район не определяется по адресу «Minutes to BGC & McKinley Hill»
  * 3448430621995943 -- нет ни одной скачанной фотографии
  * 715451165293916/3454507284721610 -- лимит прогона (30) выбран
  * 3447877042051301 -- тип жилья в тексте не назван
  * 715451165293916/3443070299198642 -- лимит прогона (30) выбран
  * 2032166500794472 -- в посте несколько разных цен: 10,000, 12,500, 15,500
  * 2035107657167023 -- в посте несколько разных цен: 4,000, 4,500, 5,000
  * 2032143240796798 -- в посте несколько разных цен: 14,000, 15,000
  * 2035162927161496 -- тип жилья в тексте не назван
  * 2025675264776929 -- в посте несколько разных цен: 5,000, 6,000, 8,000, 9,000, 10,000, 12,000
  * 2022434191767703 -- нет ни одной скачанной фотографии
  * 2038684243476031 -- район не определяется по адресу «1022 Solis Street»
  * 2011944009483388 -- тип жилья в тексте не назван
  * 2032171387460650 -- район не определяется по адресу «Urban Deca homes»
  * 2727443507687924 -- район не определяется по адресу «Prime location near the city center»
  * 2729452834153658 -- район не определяется по адресу «Ton Dan Street»
  * 2728103040955304 -- район не определяется по адресу «Brand-new apartment in the south of the city ~ Pet»
  * nhatrang.apartment.and.house/2729540080811600 -- лимит прогона (30) выбран
  * 2727115907720684 -- район не определяется по адресу «Nguyen Thien Thuat»; прецедент расколот: «Nguyen Thien Thuat»: tl 1, lt 1
  * 1945533369475764 -- в посте несколько разных цен: 3,000,000, 3,500,000
  * 1983758185653282 -- район не определяется по адресу «CHO THUÊ NHÀ MỚI XÂY»
  * 1977293056299795 -- нет ни одной скачанной фотографии
  * thuecanhotronhatrang/1984854042210363 -- лимит прогона (30) выбран
  * 1986878398674594 -- район не определяется по адресу «LVCC 🌿 Cho Thuê Nhà đường Thích Quảng Đức»
  * 1980800452615722 -- район не определяется по адресу «CHO THUÊ NHÀ 3 TẦNG»
  * 4626748320928022 -- похоже на уже заведённое: id 2000946
  * 4628240987445422 -- район не определяется по адресу «1-BEDROOM APARTMENT FOR RENT ~ AIRY»
  * 4632898333646354 -- район не определяется по адресу «D’qua apartment for rent»
  * 4630547377214783 -- район не определяется по адресу «Brand-new apartment in the south of the city ~ Pet»
  * 4741640429415359 -- в посте несколько разных цен: 500,000, 18,500,000
  * 4741223349457067 -- в посте несколько разных цен: 500,000, 13,500,000
  * 2253829621529798/4737023933210342 -- лимит прогона (30) выбран
  * 4741637449415657 -- район не определяется по адресу «An Bình Tân»
  * 2253829621529798/4740940036152065 -- лимит прогона (30) выбран
  * 2100846437239443 -- район не определяется по адресу «South Nha Trang»
  * 1172766863380743/2100851360572284 -- лимит прогона (30) выбран
  * 2096498764340877 -- уже на сайте: id 3001730
  * 2101751040482316 -- в посте несколько разных цен: 500,000, 13,500,000
  * 2097731520884268 -- район не определяется по адресу «the heart of Nha Trang»
  * 1172766863380743/2101944567129630 -- лимит прогона (30) выбран
  * 2100822863908467 -- район не определяется по адресу «FOR RENT»
  * 1172766863380743/2099712060686214 -- лимит прогона (30) выбран
  * 3852850711522142 -- район не определяется по адресу «South Nha Trang»
  * 3856943337779546 -- район не определяется по адресу «Southern Nha Trang»
  * 3854107721396441 -- в посте несколько разных цен: 500,000, 13,000,000, 13,500,000
  * 3848252325315314 -- тот же текст уже заведён: id 3001618
  * 3857260247747855 -- в посте несколько разных цен: 500,000, 13,000,000
  * 1097636699376885 -- район не определяется по адресу «📞📞 Contact +84901717411 via WhatsApp»
  * 1124229146717640 -- в посте несколько разных цен: 500,000, 18,500,000
  * 2080195716147863 -- похоже на уже заведённое: id 2000909
  * 2076181956549239 -- район не определяется по адресу «** Khanh Hoa»
  * chothuecanhogiarenhatrang/2060280514806050 -- лимит прогона (30) выбран
  * 2074055276761907 -- район не определяется по адресу «**Khanh Hoa»
  * 2081008036066631 -- это поиск жилья, а не предложение
  * 4615612555374932 -- район не определяется по адресу «Muong Thanh 04 Tran Phu»
  * chothue79/4587623478173840 -- лимит прогона (30) выбран
  * 4615648422038012 -- район не определяется по адресу «LUXURY 3-BEDROOM APARTMENT FOR RENT»
  * 4614743152128539 -- район не определяется по адресу «NT RENT»
  * 1763318494880834 -- район не определяется по адресу «CHO THUÊ VILLA PALM GARDEN»
  * 472474987298531/1715808856298465 -- лимит прогона (30) выбран
  * 1769689764243707 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2579623245791664 -- район не определяется по адресу «the prestigious Meyhomes community»
  * 2604061680014487 -- район не определяется по адресу «CHO THUÊ CĂN HỘ THEO THÁNG»
  * 2588243598262962 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * congdongphuquocnew/2599789720441683 -- лимит прогона (30) выбран
  * 2592618517825470 -- район не определяется по адресу «✨ Brand-new villa»
  * 5560433464181291 -- район не определяется по адресу «✅✅✅ Cho Thuê Căn Hộ ALTARA RESIDENCE»
  * 5560371154187522 -- район не определяется по адресу «studio layout featuring 2 beds»
  * 3288882517989508 -- район не определяется по адресу «studio layout featuring 2 beds»
  * 3278586459019114 -- район не определяется по адресу «Studio»
  * 3292703214274105 -- район не определяется по адресу «**CHO THUÊ CĂN HỘ PHÚ TÀI CENTRALLIFE»
  * 2148291142476214 -- район не определяется по адресу «44 Vo Thi Yen»
  * 2148699985768663 -- район не определяется по адресу «studio layout featuring 2 beds»
  * 2149027355735926 -- район не определяется по адресу «Cho Thuê Căn Hộ ALTARA RESIDENCE»
  * 2148781312427197 -- в посте несколько разных цен: 7,500,000, 10,000,000
  * 2131116177527044 -- район не определяется по адресу «Vina2 Panorama Quy Nhon»
"""
from listing_lock import insert_listings

IDS = [3001870, 3001871, 3001872, 3001873, 3001874, 3001875, 3001876, 3001877, 3001878, 3001879, 3001880, 3001881, 3001882, 3001883, 3001884, 3001885, 3001886, 3001887, 3001888, 3001889, 3001890, 3001891, 3001892, 3001893, 3001894, 3001895, 3001896, 3001897, 3001898, 3001899]

NEW_SRC = r'''
L(3001870,"cebu","man","Дом",35000,None,
  "3-спальный дом, Mandaue.",
  "https://www.facebook.com/groups/rentcebu/posts/28255246164174142/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-05",
  descEn="3-bedroom house, Mandaue.",
  details={"photos": ["assets/fb_photos/28255246164174142/01.webp", "assets/fb_photos/28255246164174142/02.webp", "assets/fb_photos/28255246164174142/03.webp", "assets/fb_photos/28255246164174142/04.webp", "assets/fb_photos/28255246164174142/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001871,"cebu","tls","Квартира",28000,None,
  "4-спальная квартира, Talisay — 3 санузла.",
  "https://www.facebook.com/groups/cebu.tambayan.2/posts/28677928168537286/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-05",
  descEn="4-bedroom flat, Talisay — 3 bathrooms.",
  details={"photos": ["assets/fb_photos/28677928168537286/01.webp", "assets/fb_photos/28677928168537286/02.webp", "assets/fb_photos/28677928168537286/03.webp", "assets/fb_photos/28677928168537286/04.webp", "assets/fb_photos/28677928168537286/05.webp"], "am": ["k"], "fl": 2, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001872,"da-lat","cl","Квартира",15000000,55,
  "Квартира, 55 м², Cam Ly - Đà Lạt — 1 санузел.",
  "https://www.facebook.com/groups/phongtrodalat/posts/3672523882904713/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Flat, 55 m², Cam Ly - Đà Lạt — 1 bathroom.",
  details={"photos": ["assets/fb_photos/3672523882904713/01.webp", "assets/fb_photos/3672523882904713/02.webp", "assets/fb_photos/3672523882904713/03.webp", "assets/fb_photos/3672523882904713/04.webp", "assets/fb_photos/3672523882904713/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001873,"da-nang","ns","Студия",9000000,None,
  "Студия, Located: Do Ba st - in the heart of An Thuong, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2985124201881657/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Studio, Located: Do Ba st - in the heart of An Thuong, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2985124201881657/01.webp", "assets/fb_photos/2985124201881657/02.webp", "assets/fb_photos/2985124201881657/03.webp", "assets/fb_photos/2985124201881657/04.webp", "assets/fb_photos/2985124201881657/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001874,"da-nang","ah","Студия",10000000,40,
  "Студия, 40 м², Lê Ninh, An Hải.",
  "https://www.facebook.com/groups/1454201286459382/posts/1578555537357289/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Studio, 40 m², Lê Ninh, An Hải.",
  details={"photos": ["assets/fb_photos/1578555537357289/01.webp", "assets/fb_photos/1578555537357289/02.webp", "assets/fb_photos/1578555537357289/03.webp", "assets/fb_photos/1578555537357289/04.webp", "assets/fb_photos/1578555537357289/05.webp"], "am": ["b", "lift", "gym"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001875,"da-nang","ns","Квартира",7000000,None,
  "1-спальная квартира, Trương Văn Hiến, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/203559903815711/posts/2375416663296680/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, Trương Văn Hiến, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2375416663296680/01.webp", "assets/fb_photos/2375416663296680/02.webp", "assets/fb_photos/2375416663296680/03.webp", "assets/fb_photos/2375416663296680/04.webp", "assets/fb_photos/2375416663296680/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001876,"da-nang","ns","Квартира",9000000,None,
  "2-спальная квартира, D**uong Thi Xuan Quy, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/203559903815711/posts/2374408800064133/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="2-bedroom flat, D**uong Thi Xuan Quy, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2374408800064133/01.webp", "assets/fb_photos/2374408800064133/02.webp", "assets/fb_photos/2374408800064133/03.webp", "assets/fb_photos/2374408800064133/04.webp", "assets/fb_photos/2374408800064133/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001877,"da-nang","ns","Квартира",11000000,None,
  "1-спальная квартира, BEDROOM APARTMENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/203559903815711/posts/2374477963390550/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, BEDROOM APARTMENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2374477963390550/01.webp", "assets/fb_photos/2374477963390550/02.webp", "assets/fb_photos/2374477963390550/03.webp", "assets/fb_photos/2374477963390550/04.webp", "assets/fb_photos/2374477963390550/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001878,"da-nang","ah","Квартира",21000000,None,
  "1-спальная квартира, Phước Trường 3, An Hải.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1753307146325594/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, Phước Trường 3, An Hải.",
  details={"photos": ["assets/fb_photos/1753307146325594/01.webp", "assets/fb_photos/1753307146325594/02.webp", "assets/fb_photos/1753307146325594/03.webp", "assets/fb_photos/1753307146325594/04.webp", "assets/fb_photos/1753307146325594/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001879,"da-nang","ns","Студия",8500000,None,
  "Студия, ✨ STUDIO APARTMENT FOR RENT, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/chothuecanhodanang43/posts/1752796116376697/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Studio, ✨ STUDIO APARTMENT FOR RENT, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1752796116376697/01.webp", "assets/fb_photos/1752796116376697/02.webp", "assets/fb_photos/1752796116376697/03.webp", "assets/fb_photos/1752796116376697/04.webp", "assets/fb_photos/1752796116376697/05.webp"], "am": ["w", "k", "b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001880,"da-nang","ah","Квартира",9000000,None,
  "Квартира, **APARTMENT FOR RENT, An Hải.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2243290389631953/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Flat, **APARTMENT FOR RENT, An Hải.",
  details={"photos": ["assets/fb_photos/2243290389631953/01.webp", "assets/fb_photos/2243290389631953/02.webp", "assets/fb_photos/2243290389631953/03.webp", "assets/fb_photos/2243290389631953/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001881,"da-nang","ah","Квартира",12000000,None,
  "1-спальная квартира, An Đồn 6, An Hải.",
  "https://www.facebook.com/groups/canhochothuedanangtot/posts/2243119016315757/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, An Đồn 6, An Hải.",
  details={"photos": ["assets/fb_photos/2243119016315757/01.webp", "assets/fb_photos/2243119016315757/02.webp", "assets/fb_photos/2243119016315757/03.webp", "assets/fb_photos/2243119016315757/04.webp", "assets/fb_photos/2243119016315757/05.webp"], "am": ["w", "b", "pool", "pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001882,"da-nang","ah","Студия",6500000,35,
  "Студия, 35 м², 🔴 FULLY FURNISHED STUDIO APARTMENT FOR RENT, An Hải.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1491835269776123/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Studio, 35 m², 🔴 FULLY FURNISHED STUDIO APARTMENT FOR RENT, An Hải.",
  details={"photos": ["assets/fb_photos/1491835269776123/01.webp", "assets/fb_photos/1491835269776123/02.webp", "assets/fb_photos/1491835269776123/03.webp", "assets/fb_photos/1491835269776123/04.webp", "assets/fb_photos/1491835269776123/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001883,"da-nang","ah","Студия",11000000,None,
  "Студия, Lý Thánh Tông, An Hải.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1461522199474097/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Studio, Lý Thánh Tông, An Hải.",
  details={"photos": ["assets/fb_photos/1461522199474097/01.webp", "assets/fb_photos/1461522199474097/02.webp", "assets/fb_photos/1461522199474097/03.webp", "assets/fb_photos/1461522199474097/04.webp", "assets/fb_photos/1461522199474097/05.webp"], "am": ["w", "k", "pet"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001884,"da-nang","hx","Дом",15000000,None,
  "4-спальный дом, NHÀ 2 TẦNG, Hòa Xuân.",
  "https://www.facebook.com/groups/476056366996433/posts/1655398372395554/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="4-bedroom house, NHÀ 2 TẦNG, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1655398372395554/01.webp", "assets/fb_photos/1655398372395554/02.webp", "assets/fb_photos/1655398372395554/03.webp", "assets/fb_photos/1655398372395554/04.webp", "assets/fb_photos/1655398372395554/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001885,"da-nang","ah","Дом",40000000,None,
  "4-спальный дом, Đặng Vũ Hỷ, An Hải.",
  "https://www.facebook.com/groups/476056366996433/posts/1589097499025642/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="4-bedroom house, Đặng Vũ Hỷ, An Hải.",
  details={"photos": ["assets/fb_photos/1589097499025642/01.webp", "assets/fb_photos/1589097499025642/02.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001886,"da-nang","ah","Квартира",12000000,None,
  "1-спальная квартира, Dương Đình Nghệ, An Hải.",
  "https://www.facebook.com/groups/476056366996433/posts/1651352766133448/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, Dương Đình Nghệ, An Hải.",
  details={"photos": ["assets/fb_photos/1651352766133448/01.webp", "assets/fb_photos/1651352766133448/02.webp", "assets/fb_photos/1651352766133448/03.webp", "assets/fb_photos/1651352766133448/04.webp", "assets/fb_photos/1651352766133448/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001887,"da-nang","hx","Студия",6000000,None,
  "Студия, Nguyễn Thị Sáu, Hòa Xuân.",
  "https://www.facebook.com/groups/728946289449167/posts/1405547428455713/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Studio, Nguyễn Thị Sáu, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1405547428455713/01.webp", "assets/fb_photos/1405547428455713/02.webp", "assets/fb_photos/1405547428455713/03.webp", "assets/fb_photos/1405547428455713/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001888,"da-nang","ns","Квартира",7500000,None,
  "1-спальная квартира, Căn hộ 1PN, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/728946289449167/posts/1405203591823430/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, Căn hộ 1PN, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1405203591823430/01.webp", "assets/fb_photos/1405203591823430/02.webp", "assets/fb_photos/1405203591823430/03.webp", "assets/fb_photos/1405203591823430/04.webp", "assets/fb_photos/1405203591823430/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001889,"da-nang","ns","Квартира",11000000,None,
  "Квартира, Quiet, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/728946289449167/posts/1391899156487207/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Flat, Quiet, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1391899156487207/01.webp", "assets/fb_photos/1391899156487207/02.webp", "assets/fb_photos/1391899156487207/03.webp", "assets/fb_photos/1391899156487207/04.webp", "assets/fb_photos/1391899156487207/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001890,"da-nang","ns","Квартира",14000000,None,
  "2-спальная квартира, Trương Quang Được, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/203559903815711/posts/2372056313632715/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="2-bedroom flat, Trương Quang Được, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2372056313632715/01.webp", "assets/fb_photos/2372056313632715/02.webp", "assets/fb_photos/2372056313632715/03.webp", "assets/fb_photos/2372056313632715/04.webp", "assets/fb_photos/2372056313632715/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001891,"dumaguete","dau","Квартира",29500,None,
  "1-спальная квартира, Dauin — 1 санузел.",
  "https://www.facebook.com/groups/153191128587086/posts/2249949128911265/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-10-05",
  descEn="1-bedroom flat, Dauin — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2249949128911265/01.webp", "assets/fb_photos/2249949128911265/02.webp", "assets/fb_photos/2249949128911265/03.webp", "assets/fb_photos/2249949128911265/04.webp", "assets/fb_photos/2249949128911265/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001892,"ha-noi","bd","Квартира",11000000,45,
  "1-спальная квартира, 45 м², Ba Đình — 1 санузел.",
  "https://www.facebook.com/groups/nhatrogiarenhat/posts/2230450230901367/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, 45 m², Ba Đình — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2230450230901367/01.webp", "assets/fb_photos/2230450230901367/02.webp", "assets/fb_photos/2230450230901367/03.webp", "assets/fb_photos/2230450230901367/04.webp", "assets/fb_photos/2230450230901367/05.webp"], "am": ["w", "win", "lift"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001893,"ha-noi","hm","Квартира",5200000,None,
  "1-спальная квартира, Thinh Liet, Hoàng Mai.",
  "https://www.facebook.com/groups/chungcuminigiarehanoii/posts/1084124464610566/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, Thinh Liet, Hoàng Mai.",
  details={"photos": ["assets/fb_photos/1084124464610566/01.webp", "assets/fb_photos/1084124464610566/02.webp", "assets/fb_photos/1084124464610566/03.webp", "assets/fb_photos/1084124464610566/04.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001894,"ho-chi-minh","ak","Квартира",13800000,None,
  "1-спальная квартира, An Khánh.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1865296498122406/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, An Khánh.",
  details={"photos": ["assets/fb_photos/1865296498122406/01.webp", "assets/fb_photos/1865296498122406/02.webp", "assets/fb_photos/1865296498122406/03.webp", "assets/fb_photos/1865296498122406/04.webp", "assets/fb_photos/1865296498122406/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001895,"ho-chi-minh","ak","Квартира",13000000,None,
  "1-спальная квартира, An Khánh — 1 санузел.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1858110785507644/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, An Khánh — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1858110785507644/01.webp", "assets/fb_photos/1858110785507644/02.webp", "assets/fb_photos/1858110785507644/03.webp", "assets/fb_photos/1858110785507644/04.webp", "assets/fb_photos/1858110785507644/05.webp"], "am": ["b"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001896,"ho-chi-minh","ak","Квартира",20000000,None,
  "1-спальная квартира, An Khánh.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1967788500964238/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="1-bedroom flat, An Khánh.",
  details={"photos": ["assets/fb_photos/1967788500964238/01.webp", "assets/fb_photos/1967788500964238/02.webp", "assets/fb_photos/1967788500964238/03.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001897,"hue","acu","Студия",2900000,None,
  "Студия, Hồ Đắc Di, An Cựu.",
  "https://www.facebook.com/groups/phongtrochothuehue/posts/2044199632954479/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Studio, Hồ Đắc Di, An Cựu.",
  details={"photos": ["assets/fb_photos/2044199632954479/01.webp", "assets/fb_photos/2044199632954479/02.webp", "assets/fb_photos/2044199632954479/03.webp", "assets/fb_photos/2044199632954479/04.webp", "assets/fb_photos/2044199632954479/05.webp"], "am": ["ws", "k", "win"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001898,"hue","vyd","Квартира",8500000,64,
  "2-спальная квартира, 64 м², Vỹ Dạ — 2 санузла.",
  "https://www.facebook.com/groups/phongtrosvhue/posts/1739874880555153/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="2-bedroom flat, 64 m², Vỹ Dạ — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1739874880555153/01.webp", "assets/fb_photos/1739874880555153/02.webp", "assets/fb_photos/1739874880555153/03.webp", "assets/fb_photos/1739874880555153/04.webp", "assets/fb_photos/1739874880555153/05.webp"], "fl": 12, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001899,"hue","vyd","Квартира",3700000,53,
  "Квартира, 53 м², Vỹ Dạ — 1 санузел.",
  "https://www.facebook.com/groups/phongtrosvhue/posts/1550648672811109/","сегодня",0,source="fbgroup",postedOn="2026-10-05",
  descEn="Flat, 53 m², Vỹ Dạ — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1550648672811109/01.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
