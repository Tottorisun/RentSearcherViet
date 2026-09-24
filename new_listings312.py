# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 20 строк, 2026-09-24.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 203559903815711/2362747857896894 -- da-nang/st, 11,000,000 VND: улица Trần Sâm: 1 из 1 отрезков в st; пост: Son Tra
  * 203559903815711/2360398424798504 -- da-nang/ns, 7,500,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * 476056366996433/1644387356829989 -- da-nang/hx, 18,000,000 VND: район назван в посте
  * 476056366996433/1648116186457106 -- da-nang/ns, 12,000,000 VND: «FOR RENT»: 3 строк сайта, все в ns
  * 728946289449167/1394751396201983 -- da-nang/ah, 4,500,000 VND: улица Nguyễn Công Trứ: 5 из 5 отрезков в ah; пост: Son Tra
  * 728946289449167/1394422612901528 -- da-nang/hx, 6,800,000 VND: район назван в посте
  * chothuechungcuminihanoigiare/959510036719595 -- ha-noi/hm, 5,200,000 VND: район назван в адресе поста; «LINH DAM»: 2 строк сайта, все в hm
  * v3homechothuenhahaiphong10/2011943879441925 -- hai-phong/lch, 9,000,000 VND: район назван в адресе поста
  * v3homechothuenhahaiphong10/2012021282767518 -- hai-phong/lch, 6,500,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1865385504780172 -- ho-chi-minh/ak, 24,000,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1864470381538351 -- ho-chi-minh/ak, 12,500,000 VND: район назван в адресе поста
  * chungcumini.canhodichvu.phongtrotphcm/1864402611545128 -- ho-chi-minh/ak, 13,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1970185144057907 -- ho-chi-minh/ak, 36,000,000 VND: район назван в адресе поста
  * chothuecanhotphcm5starsgroup/1969749244101497 -- ho-chi-minh/ak, 21,000,000 VND: район назван в адресе поста
  * 807531664242245/1464410321887706 -- hue/acu, 15,000,000 VND: район назван в адресе поста
  * 299437881275577/1797444981474852 -- manila/qzc, 35,000 PHP: район назван в адресе поста
  * 849441571863086/3842813092525904 -- nha-trang/lt, 8,000,000 VND: район назван в адресе поста
  * 849441571863086/3843295509144329 -- nha-trang/ph, 25,000,000 VND: район назван в адресе поста
  * 849441571863086/3842838922523321 -- nha-trang/ph2, 10,000,000 VND: район назван в адресе поста
  * 849441571863086/3841899312617282 -- nha-trang/ph, 14,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (185):
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
  * 3091345824530955 -- тот же текст уже заведён: id 3001270
  * 3089574081374796 -- тот же текст уже заведён: id 3001116
  * 1788624765783391 -- тот же текст уже заведён: id 3001271
  * 3090424441289760 -- в посте несколько разных цен: 3,000, 22,000
  * 3084842838514587 -- тот же текст уже заведён: id 3001272
  * 28646959921607710 -- тот же текст уже заведён: id 3001116
  * 28643114135325622 -- район не определяется по адресу «Vertex Central Archbishop Reyes Cebu City»
  * 28663251676645201 -- район не определяется по адресу «Room for rent in Subangdaku»
  * 28659385793698456 -- похоже на уже заведённое: id 3000864
  * 28648114874825548 -- в посте несколько разных цен: 31,000, 33,000
  * 2363088937843855 -- тип жилья в тексте не назван
  * 2368644720621610 -- район не определяется по адресу «HOUSE FOR RENT»
  * 2359711461514936 -- тот же текст уже заведён: id 3001273
  * 2367064320779650 -- район не определяется по адресу «LUXURY BRAND-NEW HOUSE FOR RENT»
  * 2366316614187754 -- район не определяется по адресу «Panorama Apartment for Rent»
  * 2367397907412958 -- это поиск жилья, а не предложение
  * 2368197180666364 -- район не определяется по адресу «BRAND NEW 1BR APARTMENT»
  * 2125924031352847 -- это поиск жилья, а не предложение
  * 2134554663823117 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 2096068041005113 -- тип жилья в тексте не назван
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2103298020282115 -- в тексте есть и другая цена того же порядка: 953,303, 7,201,681 против 2,500,000
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 2076569656288285 -- тот же текст уже заведён: id 3001274
  * 2069351513676766 -- тот же текст уже заведён: id 3001275
  * 1742357717420537 -- тот же текст уже заведён: id 3001248
  * 1742797127376596 -- район не определяется: «HOUSE FOR RENT ON NGUYEN TRI PHUONG STREET, HAI CHAU, 🏠 HOUSE FOR RENT ON NGUYEN TRI PHUONG STREET»
  * 1742576090732033 -- похоже на уже заведённое: id 3001250
  * 1742573107398998 -- тот же текст уже заведён: id 3001276
  * 1740963570893285 -- похоже на уже заведённое: id 1005932
  * 1739962917660017 -- тот же текст уже заведён: id 3001277
  * 1742875017368807 -- тот же текст уже заведён: id 3001278
  * 1742275864095389 -- тот же текст уже заведён: id 3001279
  * 2227385361222456 -- нет ни одной скачанной фотографии
  * 2229530991007893 -- источники назвали разные районы: district=ns, street=ah
  * 2226225068005152 -- нет ни одной скачанной фотографии
  * 2222237321737260 -- в посте несколько разных цен: 7,500,000, 9,500,000, 10,000,000, 12,000,000, 14,000,000
  * 2226704014623924 -- похоже на уже заведённое: id 1010627
  * 2223506231610369 -- в посте несколько разных цен: 6,000,000, 9,000,000
  * 2221117548515904 -- это поиск жилья, а не предложение
  * 2214802225814103 -- тот же текст уже заведён: id 3001280
  * 2221611245133201 -- в посте несколько разных цен: 7,500,000, 8,000,000
  * 2220636861897306 -- тип жилья в тексте не назван
  * 1476237824669201 -- в посте несколько разных цен: 8,000,000, 9,000,000
  * 1479585951001055 -- район не определяется: «CHO THUÊ NHÀ NGUYÊN CĂN 2PN kiệt 1xx NGUYỄN CHÍ THANH✨ Phường Hải Châu - Ngay trung tâm TP, đường Bạch Đằng, Trần Phú»
  * 2363124944525852 -- район не определяется: «Alley connecting to 382 Tran Cao Van, 🍄Mini house for rent near Nguyen Tat Thanh beach - Thanh Khe»
  * 2362788734559473 -- похоже на уже заведённое: id 3001250
  * 2362549944583352 -- район не определяется: «Hiyori Tower, Đà Nẵng, 🏢 HIYORI TOWER»
  * 2361758191329194 -- похоже на уже заведённое: id 1010471
  * 2357231405115206 -- нет ни одной скачанной фотографии
  * 2361077668063913 -- район не определяется: «a densely populated area with convenient transportation, administrative offices, schools»
  * 2353501535488193 -- это поиск жилья, а не предложение
  * 2352331512271862 -- район не определяется: «- Two bed room ( 03 bed in two bed room ), - 200m walking to the an bang beach., TWO BEDROOM HOUSE FOR RENT AN BANG - HOI AN»
  * 1641666327102092 -- тип жилья в тексте не назван
  * 1648000753135316 -- район не определяется: «APARTMENT FOR RENT IN THE HIYORI GARDEN, FULLY FURNISHED, Private space»
  * 1646998733235518 -- район не определяется: «CHO THUÊ 2PN, MIA CENTER POINT, TẦNG 12»
  * 1648024443132947 -- тип жилья в тексте не назван
  * 1647772936491431 -- район не определяется: «4-Bedroom House for Rent in Central Da Nang 🌿, Prime location near Dragon Bridge & Han River, Entire house with spacious living areas»
  * 1394116689598787 -- район не определяется: «BRAND-NEW STUDIO APARTMENT, SON TRA, DA NANG»
  * 1422244359333620 -- в тексте есть и другая цена того же порядка: 21,641 против 40,000
  * 1421461599411896 -- тип жилья в тексте не назван
  * 1423197052571684 -- тот же текст уже заведён: id 3001281
  * 4620975714826245 -- продажа
  * 4617681065155710 -- тип жилья в тексте не назван
  * 4620107064913110 -- район не определяется по адресу «House for rent‼️»
  * 4614646732125810 -- нет ни одной скачанной фотографии
  * 4614813985442418 -- нет ни одной скачанной фотографии
  * 4611225949134555 -- в тексте есть и другая цена того же порядка: 21,641 против 40,000
  * 28516260041309277 -- тип жилья в тексте не назван
  * 28960082756927001 -- тип жилья в тексте не назван
  * 29240192592249348 -- помещение под бизнес или здание целиком, а не жильё
  * 28822141150721163 -- помещение под бизнес или здание целиком, а не жильё
  * 957601213577144 -- в посте несколько разных цен: 4,000,000, 6,000,000
  * 937482665588999 -- похоже на уже заведённое: id 1007748
  * 979833631353902 -- нет ни одной скачанной фотографии
  * 968845495786049 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 955745937096005 -- тип жилья в тексте не назван
  * 946525864684679 -- тип жилья в тексте не назван
  * 3859299804211128 -- район не определяется по адресу «[EN BELOW] 10»
  * 2010562192913427 -- район не определяется по адресу «T2964 Cho Thuê Nhà Vinhomes Marina»
  * 2012014749434838 -- район не определяется по адресу «T2760 Cho Thuê Nhà Nguyên Căn - 193 Văn Cao ( oto »
  * 2012053172764329 -- район не определяется по адресу «CHO THUÊ CĂN HỘ LÊ HỒNG PHONG - T0656»
  * 2012882546014725 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 2011122146190765 -- район не определяется по адресу «Cho thuê căn hộ Penthouse 1 ngủ tách bếp to rộng t»
  * 1865296498122406 -- похоже на уже заведённое: id 3001056
  * 1865425554776167 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1858166655502057 -- тип жилья в тексте не назван
  * 1865336211451768 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1858110785507644 -- похоже на уже заведённое: id 1006401
  * 1970059524070469 -- район не определяется по адресу «Đinh Tiên Hoàng»
  * 1969270227482732 -- район не определяется по адресу «De Tham Street»
  * 1969292950813793 -- район не определяется по адресу «Pham Viet Chanh»
  * 1962341911508897 -- район не определяется по адресу «🌿 CHO THUÊ CĂN HỘ 2PN VIEW LANDMARK 81»; прецедент расколот: «VIEW LANDMARK 81»: ak 1
  * 1969269510816137 -- район не определяется по адресу «Nguyễn Bỉnh Khiêm»
  * 1969006190842469 -- район не определяется по адресу «Tân Cảng»
  * 1969003407509414 -- цены в посте нет
  * 1987516638597971 -- район не определяется по адресу «Trảng Kèo 8»
  * 1992234034792898 -- район не определяется по адресу «Move-in ready»
  * 1977822679567367 -- район не определяется по адресу «BEACH LIFE IN HOI AN»
  * 1984906532192315 -- в посте несколько разных цен: 4,500,000, 5,000,000
  * 1984287965587505 -- нет ни одной скачанной фотографии
  * 1992280878121547 -- район не определяется по адресу «Spacious 3-Bedroom House for Long-Term Rent Near H»
  * 2017947155550334 -- район не определяется по адресу «PRIVATE 4-BEDROOM CORNER VILLA»
  * 2017928622218854 -- район не определяется по адресу «✨ COZY 1-BEDROOM APARTMENT FOR RENT IN HOI AN ✨🏡»
  * 2017747158903667 -- район не определяется по адресу «A Beautiful Home in the Heart of Hoi An»
  * 2017532202258496 -- район не определяется по адресу «1-Bedroom Apartment»
  * 2014292692582447 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 2010975296247520 -- район не определяется по адресу «ENTIRE HOUSE FOR RENT»
  * 1287853898988310 -- в тексте есть и другая цена того же порядка: 4,568,736 против 4,000,000
  * 1466927818302623 -- похоже на уже заведённое: id new:807531664242245/1464410321887706
  * 1507435977585140 -- в посте несколько разных цен: 500,000, 600,000
  * 1506528094342595 -- тип жилья в тексте не назван
  * 1499726755022729 -- в посте несколько разных цен: 500,000, 600,000
  * 1799903581228992 -- в тексте есть и другая цена того же порядка: 36,000 против 30,000
  * 1797050891514261 -- в посте несколько разных цен: 12,000, 13,000, 14,000, 15,000, 17,000, 18,000, 20,000
  * 1799249514627732 -- район не определяется по адресу «Apartment Unit !!!»
  * 1798453601373990 -- в посте несколько разных цен: 13,000, 14,000, 15,000, 17,000, 18,000, 20,000
  * 1801283101091040 -- в посте несколько разных цен: 16,000, 18,000, 25,000
  * 3443833065789032 -- район не определяется по адресу «Urban Deca Homes Ortigas»
  * 3436429663196039 -- район не определяется по адресу «PET FRIENDLY. VIEWING THIS SATURDAY! (SEPT19)»
  * 2090509091606511 -- район не определяется по адресу «Nha Trang Ward»
  * 2090555578268529 -- в посте несколько разных цен: 530,000, 20,000,000
  * 2088878168436270 -- тот же текст уже заведён: id 3001235
  * 1113468417793713 -- район не определяется по адресу «Bustling residential area near the city center»
  * 1113334617807093 -- тот же текст уже заведён: id 3001282
  * 1109977311476157 -- район не определяется по адресу «South Nha Trang»
  * 1113375201136368 -- район не определяется по адресу «NT RENT»
  * 1113530237787531 -- район не определяется по адресу «**Khanh Hoa»
  * 1113152374491984 -- тот же текст уже заведён: id 3001283
  * 1113365664470655 -- в посте несколько разных цен: 20,000,000, 25,000,000
  * 2070505000450268 -- в посте несколько разных цен: 700,000, 21,000,000
  * 2070589390441829 -- район не определяется по адресу «**Khanh Hoa»
  * 2070057083828393 -- район не определяется по адресу «**Khanh Hoa»
  * 2069346347232800 -- это поиск жилья, а не предложение
  * 2068493540651414 -- тот же текст уже заведён: id 3001235
  * 3837694026371144 -- район не определяется по адресу «2 bedrooms»; прецедент расколот: «LVCC»: lt 1
  * 3842934655847081 -- район не определяется по адресу «South Nha Trang»
  * 3838846259589254 -- в посте несколько разных цен: 14,500,000, 15,500,000
  * 3839121829561697 -- тот же текст уже заведён: id 3001235
  * 4615612555374932 -- район не определяется по адресу «Muong Thanh 04 Tran Phu»
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
  * 5545581265666511 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 5549054955319142 -- район не определяется по адресу «# **Cho thuê căn hộ Altara Residences Quy Nhơn - 2»
  * 3285077928369967 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 3280507732160320 -- район не определяется по адресу «Ngay Đại học FPT»
  * 3278586459019114 -- район не определяется по адресу «Studio»
  * 1737704797293837 -- район не определяется по адресу «Direct owner service»
  * 1735000710897579 -- район не определяется по адресу «2 bedrooms»
  * 1738431463887837 -- район не определяется по адресу «Apartment for rent at Binh Gia Resident»
  * 1736754977388819 -- район не определяется по адресу «172 Hoang Hoa Tham Street»
  * 27948705921436408 -- в посте несколько разных цен: 6,000,000, 6,500,000
  * 1674135736984077 -- район не определяется по адресу «Thông tin căn hộ:»
  * 1712195156511468 -- район не определяется по адресу «🏢 Apartment for Rent - Fully Furnished - Ward 8»
  * 1474799354464133 -- район не определяется по адресу «Direct owner service»
  * 1472289898048412 -- это поиск жилья, а не предложение
  * 1476872604256808 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 1477067380903997 -- в посте несколько разных цен: 9,000,000, 13,000,000, 18,000,000
"""
from listing_lock import insert_listings

IDS = [3001298, 3001299, 3001300, 3001301, 3001302, 3001303, 3001304, 3001305, 3001306, 3001307, 3001308, 3001309, 3001310, 3001311, 3001312, 3001313, 3001314, 3001315, 3001316, 3001317]

NEW_SRC = r'''
L(3001298,"da-nang","st","Квартира",11000000,None,
  "1-спальная квартира, Trần Sâm, Sơn Trà.",
  "https://www.facebook.com/groups/203559903815711/posts/2362747857896894/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="1-bedroom flat, Trần Sâm, Sơn Trà.",
  details={"photos": ["assets/fb_photos/2362747857896894/01.webp", "assets/fb_photos/2362747857896894/02.webp", "assets/fb_photos/2362747857896894/03.webp", "assets/fb_photos/2362747857896894/04.webp", "assets/fb_photos/2362747857896894/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001299,"da-nang","ns","Квартира",7500000,None,
  "Квартира, ✨✨ For rent New Apartment - Near FPT Plaza - Ngu Hanh Sơn, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/203559903815711/posts/2360398424798504/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Flat, ✨✨ For rent New Apartment - Near FPT Plaza - Ngu Hanh Sơn, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/2360398424798504/01.webp", "assets/fb_photos/2360398424798504/02.webp", "assets/fb_photos/2360398424798504/03.webp", "assets/fb_photos/2360398424798504/04.webp", "assets/fb_photos/2360398424798504/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001300,"da-nang","hx","Дом",18000000,None,
  "Дом, NHÀ 3 TẦNG, Hòa Xuân.",
  "https://www.facebook.com/groups/476056366996433/posts/1644387356829989/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="House, NHÀ 3 TẦNG, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1644387356829989/01.webp", "assets/fb_photos/1644387356829989/02.webp", "assets/fb_photos/1644387356829989/03.webp", "assets/fb_photos/1644387356829989/04.webp", "assets/fb_photos/1644387356829989/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001301,"da-nang","ns","Квартира",12000000,None,
  "2-спальная квартира, FOR RENT, Ngũ Hành Sơn — 2 санузла.",
  "https://www.facebook.com/groups/476056366996433/posts/1648116186457106/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="2-bedroom flat, FOR RENT, Ngũ Hành Sơn — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1648116186457106/01.webp", "assets/fb_photos/1648116186457106/02.webp", "assets/fb_photos/1648116186457106/03.webp", "assets/fb_photos/1648116186457106/04.webp", "assets/fb_photos/1648116186457106/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по жилому комплексу: все объявления сайта из этого комплекса стоят в этом районе.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the residential complex: every listing on the site from this complex is in this district."}),
L(3001302,"da-nang","ah","Студия",4500000,None,
  "Студия, Nguyễn Công Trứ, An Hải.",
  "https://www.facebook.com/groups/728946289449167/posts/1394751396201983/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Studio, Nguyễn Công Trứ, An Hải.",
  details={"photos": ["assets/fb_photos/1394751396201983/01.webp", "assets/fb_photos/1394751396201983/02.webp", "assets/fb_photos/1394751396201983/03.webp", "assets/fb_photos/1394751396201983/04.webp", "assets/fb_photos/1394751396201983/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001303,"da-nang","hx","Студия",6800000,None,
  "Студия, ✨ STUDIO ĐẸP, Hòa Xuân.",
  "https://www.facebook.com/groups/728946289449167/posts/1394422612901528/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Studio, ✨ STUDIO ĐẸP, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/1394422612901528/01.webp", "assets/fb_photos/1394422612901528/02.webp", "assets/fb_photos/1394422612901528/03.webp", "assets/fb_photos/1394422612901528/04.webp", "assets/fb_photos/1394422612901528/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001304,"ha-noi","hm","Студия",5200000,None,
  "Студия, LINH DAM, Hoàng Mai.",
  "https://www.facebook.com/groups/chothuechungcuminihanoigiare/posts/959510036719595/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Studio, LINH DAM, Hoàng Mai.",
  details={"photos": ["assets/fb_photos/959510036719595/01.webp", "assets/fb_photos/959510036719595/02.webp", "assets/fb_photos/959510036719595/03.webp", "assets/fb_photos/959510036719595/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001305,"hai-phong","lch","Квартира",9000000,40,
  "Квартира, 40 м², Lê Chân.",
  "https://www.facebook.com/groups/v3homechothuenhahaiphong10/posts/2011943879441925/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Flat, 40 m², Lê Chân.",
  details={"photos": ["assets/fb_photos/2011943879441925/01.webp", "assets/fb_photos/2011943879441925/02.webp", "assets/fb_photos/2011943879441925/03.webp", "assets/fb_photos/2011943879441925/04.webp", "assets/fb_photos/2011943879441925/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001306,"hai-phong","lch","Квартира",6500000,40,
  "1-спальная квартира, 40 м², Lê Chân — 1 санузел.",
  "https://www.facebook.com/groups/v3homechothuenhahaiphong10/posts/2012021282767518/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="1-bedroom flat, 40 m², Lê Chân — 1 bathroom.",
  details={"photos": ["assets/fb_photos/2012021282767518/01.webp", "assets/fb_photos/2012021282767518/02.webp", "assets/fb_photos/2012021282767518/03.webp", "assets/fb_photos/2012021282767518/04.webp", "assets/fb_photos/2012021282767518/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001307,"ho-chi-minh","ak","Квартира",24000000,101,
  "3-спальная квартира, 101 м², An Khánh — 2 санузла.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1865385504780172/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="3-bedroom flat, 101 m², An Khánh — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/1865385504780172/01.webp", "assets/fb_photos/1865385504780172/02.webp", "assets/fb_photos/1865385504780172/03.webp", "assets/fb_photos/1865385504780172/04.webp", "assets/fb_photos/1865385504780172/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001308,"ho-chi-minh","ak","Квартира",12500000,50,
  "1-спальная квартира, 50 м², An Khánh — 1 санузел.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1864470381538351/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="1-bedroom flat, 50 m², An Khánh — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1864470381538351/01.webp", "assets/fb_photos/1864470381538351/02.webp", "assets/fb_photos/1864470381538351/03.webp", "assets/fb_photos/1864470381538351/04.webp", "assets/fb_photos/1864470381538351/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001309,"ho-chi-minh","ak","Студия",13000000,30,
  "Студия, 30 м², An Khánh.",
  "https://www.facebook.com/groups/chungcumini.canhodichvu.phongtrotphcm/posts/1864402611545128/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Studio, 30 m², An Khánh.",
  details={"photos": ["assets/fb_photos/1864402611545128/01.webp", "assets/fb_photos/1864402611545128/02.webp", "assets/fb_photos/1864402611545128/03.webp", "assets/fb_photos/1864402611545128/04.webp", "assets/fb_photos/1864402611545128/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001310,"ho-chi-minh","ak","Квартира",36000000,None,
  "2-спальная квартира, An Khánh.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1970185144057907/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="2-bedroom flat, An Khánh.",
  details={"photos": ["assets/fb_photos/1970185144057907/01.webp", "assets/fb_photos/1970185144057907/02.webp", "assets/fb_photos/1970185144057907/03.webp", "assets/fb_photos/1970185144057907/04.webp", "assets/fb_photos/1970185144057907/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001311,"ho-chi-minh","ak","Квартира",21000000,85,
  "2-спальная квартира, 85 м², Nguyễn Văn Hưởng, An Khánh — 1 санузел.",
  "https://www.facebook.com/groups/chothuecanhotphcm5starsgroup/posts/1969749244101497/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="2-bedroom flat, 85 m², Nguyễn Văn Hưởng, An Khánh — 1 bathroom.",
  details={"photos": ["assets/fb_photos/1969749244101497/01.webp", "assets/fb_photos/1969749244101497/02.webp", "assets/fb_photos/1969749244101497/03.webp", "assets/fb_photos/1969749244101497/04.webp", "assets/fb_photos/1969749244101497/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001312,"hue","acu","Дом",15000000,81,
  "Дом, 81 м², An Cựu.",
  "https://www.facebook.com/groups/807531664242245/posts/1464410321887706/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="House, 81 m², An Cựu.",
  details={"photos": ["assets/fb_photos/1464410321887706/01.webp", "assets/fb_photos/1464410321887706/02.webp", "assets/fb_photos/1464410321887706/03.webp", "assets/fb_photos/1464410321887706/04.webp", "assets/fb_photos/1464410321887706/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001313,"manila","qzc","Квартира",35000,None,
  "2-спальная квартира, Quezon City.",
  "https://www.facebook.com/groups/299437881275577/posts/1797444981474852/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-24",
  descEn="2-bedroom flat, Quezon City.",
  details={"photos": ["assets/fb_photos/1797444981474852/01.webp", "assets/fb_photos/1797444981474852/02.webp", "assets/fb_photos/1797444981474852/03.webp", "assets/fb_photos/1797444981474852/04.webp", "assets/fb_photos/1797444981474852/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001314,"nha-trang","lt","Квартира",8000000,32,
  "Квартира, 32 м², Lộc Thọ.",
  "https://www.facebook.com/groups/849441571863086/posts/3842813092525904/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Flat, 32 m², Lộc Thọ.",
  details={"photos": ["assets/fb_photos/3842813092525904/01.webp", "assets/fb_photos/3842813092525904/02.webp", "assets/fb_photos/3842813092525904/03.webp", "assets/fb_photos/3842813092525904/04.webp", "assets/fb_photos/3842813092525904/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001315,"nha-trang","ph","Квартира",25000000,70,
  "2-спальная квартира, 70 м², Phước Hải — 2 санузла.",
  "https://www.facebook.com/groups/849441571863086/posts/3843295509144329/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="2-bedroom flat, 70 m², Phước Hải — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/3843295509144329/01.webp", "assets/fb_photos/3843295509144329/02.webp", "assets/fb_photos/3843295509144329/03.webp", "assets/fb_photos/3843295509144329/04.webp", "assets/fb_photos/3843295509144329/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001316,"nha-trang","ph2","Квартира",10000000,30,
  "Квартира, 30 м², Phước Hòa.",
  "https://www.facebook.com/groups/849441571863086/posts/3842838922523321/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Flat, 30 m², Phước Hòa.",
  details={"photos": ["assets/fb_photos/3842838922523321/01.webp", "assets/fb_photos/3842838922523321/02.webp", "assets/fb_photos/3842838922523321/03.webp", "assets/fb_photos/3842838922523321/04.webp", "assets/fb_photos/3842838922523321/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001317,"nha-trang","ph","Квартира",14000000,35,
  "Квартира, 35 м², Phước Hải.",
  "https://www.facebook.com/groups/849441571863086/posts/3841899312617282/","сегодня",0,source="fbgroup",postedOn="2026-09-24",
  descEn="Flat, 35 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/3841899312617282/01.webp", "assets/fb_photos/3841899312617282/02.webp", "assets/fb_photos/3841899312617282/03.webp", "assets/fb_photos/3841899312617282/04.webp", "assets/fb_photos/3841899312617282/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
