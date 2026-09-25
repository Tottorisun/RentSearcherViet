# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 9 строк, 2026-09-25.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 994303254903669/1831961487804504 -- cebu/bnl, 25,000 PHP: район назван в адресе поста
  * 652674525365824/2129515557681706 -- cebu/mab, 12,000 PHP: район назван в адресе поста
  * canhochungcudanang/2976792129381531 -- da-nang/hx, 10,000,000 VND: район назван в посте; улица Cồn Dầu 25: 1 из 1 отрезков в hx
  * chothuechungcuminihanoigiare/937482665588999 -- ha-noi/hm, 5,200,000 VND: район назван в адресе поста; «Thinh Liet»: 2 строк сайта, все в hm
  * 807531664242245/1466927818302623 -- hue/acu, 15,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1978201452875622 -- nha-trang/ph, 11,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1970693793626388 -- nha-trang/ph, 13,000,000 VND: район назван в адресе поста
  * thuecanhotronhatrang/1978862859476148 -- nha-trang/btr, 15,000,000 VND: район назван в адресе поста
  * 1172766863380743/2091252198198867 -- nha-trang/ph2, 8,500,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (225):
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
  * 3091345824530955 -- уже на сайте: id 3001270
  * 3089574081374796 -- тот же текст уже заведён: id 3001116
  * 1788624765783391 -- уже на сайте: id 3001271
  * 3090424441289760 -- в посте несколько разных цен: 3,000, 22,000
  * 3084842838514587 -- уже на сайте: id 3001272
  * 28646959921607710 -- тот же текст уже заведён: id 3001116
  * 28643114135325622 -- район не определяется по адресу «Vertex Central Archbishop Reyes Cebu City»
  * 28663251676645201 -- район не определяется по адресу «Room for rent in Subangdaku»
  * 28659385793698456 -- похоже на уже заведённое: id 3000864
  * 28648114874825548 -- в посте несколько разных цен: 31,000, 33,000
  * 1828615444805775 -- район не определяется по адресу «Avida Towers Cebu»
  * 1831468591187127 -- район не определяется по адресу «Cardinal Rosales Ave»
  * 1829954228005230 -- район не определяется по адресу «HOUSE FOR RENT IN AJOYA»
  * 1830943177906335 -- в тексте есть и другая цена того же порядка: 3,625 против 5,000
  * 1829677238032929 -- в посте несколько разных цен: 12,000, 18,000
  * 1831943547806298 -- район не определяется по адресу «ROOM FOR RENT (LADIES ONLY)»
  * 1826420871691899 -- в посте несколько разных цен: 18,000, 25,000
  * 1825901171743869 -- в тексте есть и другая цена того же порядка: 13,430 против 16,500
  * 1821535598847093 -- в тексте есть и другая цена того же порядка: 15,000 против 17,000
  * 1828052141528772 -- в посте несколько разных цен: 4,500, 80,000
  * 2130933830873212 -- это поиск жилья, а не предложение
  * 2130824454217483 -- район не определяется по адресу «ROOM FOR RENT - ₱4»
  * 2130706907562571 -- район не определяется по адресу «ROOM FOR RENT»
  * 2131553427477919 -- в посте несколько разных цен: 7,000, 7,500
  * 2127422497891012 -- район не определяется по адресу «UBCA 2 QUIOT PARDO CEBU CITY»
  * 2363088937843855 -- тип жилья в тексте не назван
  * 2368644720621610 -- район не определяется по адресу «HOUSE FOR RENT»
  * 2359711461514936 -- уже на сайте: id 3001273
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
  * 2076569656288285 -- уже на сайте: id 3001274
  * 2069351513676766 -- уже на сайте: id 3001275
  * 2363124944525852 -- район не определяется: «Alley connecting to 382 Tran Cao Van, 🍄Mini house for rent near Nguyen Tat Thanh beach - Thanh Khe»
  * 2362788734559473 -- похоже на уже заведённое: id 3001250
  * 2362549944583352 -- район не определяется: «Hiyori Tower, Đà Nẵng, 🏢 HIYORI TOWER»
  * 2362747857896894 -- тот же текст уже заведён: id 3001298
  * 2360398424798504 -- тот же текст уже заведён: id 3001299
  * 2361758191329194 -- похоже на уже заведённое: id 1010471
  * 2357231405115206 -- нет ни одной скачанной фотографии
  * 2361077668063913 -- район не определяется: «a densely populated area with convenient transportation, administrative offices, schools»
  * 2353501535488193 -- это поиск жилья, а не предложение
  * 2352331512271862 -- район не определяется: «- Two bed room ( 03 bed in two bed room ), - 200m walking to the an bang beach., TWO BEDROOM HOUSE FOR RENT AN BANG - HOI AN»
  * 1641666327102092 -- тип жилья в тексте не назван
  * 1644387356829989 -- тот же текст уже заведён: id 3001300
  * 1648116186457106 -- тот же текст уже заведён: id 3001301
  * 1648000753135316 -- район не определяется: «APARTMENT FOR RENT IN THE HIYORI GARDEN, FULLY FURNISHED, Private space»
  * 1646998733235518 -- район не определяется: «CHO THUÊ 2PN, MIA CENTER POINT, TẦNG 12»
  * 1648024443132947 -- тип жилья в тексте не назван
  * 1647772936491431 -- район не определяется: «4-Bedroom House for Rent in Central Da Nang 🌿, Prime location near Dragon Bridge & Han River, Entire house with spacious living areas»
  * 1394751396201983 -- тот же текст уже заведён: id 3001302
  * 1394116689598787 -- район не определяется: «BRAND-NEW STUDIO APARTMENT, SON TRA, DA NANG»
  * 1394422612901528 -- тот же текст уже заведён: id 3001303
  * 2977831269277617 -- район не определяется: «Fully Furnished Apartment in Da Nang City Center, Nguyen Chi Thanh St., Hai Chau District»
  * 2977208469339897 -- район не определяется: «1 Bedroom Apartment, 🏠1 Bedroom Apartment»
  * 1422244359333620 -- в тексте есть и другая цена того же порядка: 21,641 против 40,000
  * 1421461599411896 -- тип жилья в тексте не назван
  * 1423197052571684 -- уже на сайте: id 3001281
  * 4620975714826245 -- продажа
  * 4617681065155710 -- тип жилья в тексте не назван
  * 4620107064913110 -- район не определяется по адресу «House for rent‼️»
  * 4614646732125810 -- нет ни одной скачанной фотографии
  * 4614813985442418 -- нет ни одной скачанной фотографии
  * 4611225949134555 -- в тексте есть и другая цена того же порядка: 21,641 против 40,000
  * 2231309210775257 -- район не определяется по адресу «HOUSE FEATURES»
  * 2243700639536114 -- в посте несколько разных цен: 15,000, 22,000
  * 2240689496503895 -- тип жилья в тексте не назван
  * 2243314172908094 -- посуточно
  * 2238082586764586 -- рассрочка
  * 28516260041309277 -- тип жилья в тексте не назван
  * 28960082756927001 -- тип жилья в тексте не назван
  * 29240192592249348 -- помещение под бизнес или здание целиком, а не жильё
  * 28822141150721163 -- помещение под бизнес или здание целиком, а не жильё
  * 959510036719595 -- тот же текст уже заведён: id 3001304
  * 957601213577144 -- в посте несколько разных цен: 4,000,000, 6,000,000
  * 979833631353902 -- нет ни одной скачанной фотографии
  * 968845495786049 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 955745937096005 -- тип жилья в тексте не назван
  * 946525864684679 -- тип жилья в тексте не назван
  * 3859299804211128 -- район не определяется по адресу «[EN BELOW] 10»
  * 2011943879441925 -- тот же текст уже заведён: id 3001305
  * 2010562192913427 -- район не определяется по адресу «T2964 Cho Thuê Nhà Vinhomes Marina»
  * 2012014749434838 -- район не определяется по адресу «T2760 Cho Thuê Nhà Nguyên Căn - 193 Văn Cao ( oto »
  * 2012053172764329 -- район не определяется по адресу «CHO THUÊ CĂN HỘ LÊ HỒNG PHONG - T0656»
  * 2012882546014725 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 2011122146190765 -- район не определяется по адресу «Cho thuê căn hộ Penthouse 1 ngủ tách bếp to rộng t»
  * 2012021282767518 -- тот же текст уже заведён: id 3001306
  * 1865296498122406 -- похоже на уже заведённое: id 3001056
  * 1865385504780172 -- тот же текст уже заведён: id 3001307
  * 1865425554776167 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1858166655502057 -- тип жилья в тексте не назван
  * 1865336211451768 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 1864470381538351 -- тот же текст уже заведён: id 3001308
  * 1864402611545128 -- тот же текст уже заведён: id 3001309
  * 1858110785507644 -- похоже на уже заведённое: id 1006401
  * 1970185144057907 -- тот же текст уже заведён: id 3001310
  * 1970059524070469 -- район не определяется по адресу «Đinh Tiên Hoàng»
  * 1969270227482732 -- район не определяется по адресу «De Tham Street»
  * 1969292950813793 -- район не определяется по адресу «Pham Viet Chanh»
  * 1962341911508897 -- район не определяется по адресу «🌿 CHO THUÊ CĂN HỘ 2PN VIEW LANDMARK 81»; прецедент расколот: «VIEW LANDMARK 81»: ak 1
  * 1969269510816137 -- район не определяется по адресу «Nguyễn Bỉnh Khiêm»
  * 1969749244101497 -- тот же текст уже заведён: id 3001311
  * 1969006190842469 -- район не определяется по адресу «Tân Cảng»
  * 1969003407509414 -- цены в посте нет
  * 1706860460872704 -- район не определяется по адресу «2-Bedroom Fully Furnished House»
  * 1705644377660979 -- район не определяется по адресу «2-BEDROOM HOUSE FOR RENT»
  * 1704894227735994 -- район не определяется по адресу «HOUSE FOR RENT»
  * 1709427257282691 -- район не определяется по адресу «Cozy private apartment in a convenient location»
  * 1708764027349014 -- район не определяется по адресу «✨ COZY 1-BEDROOM APARTMENT FOR RENT IN HOI AN ✨🏡»
  * 2019489318729451 -- в посте несколько разных цен: 4,000,000, 5,000,000
  * 2017747158903667 -- район не определяется по адресу «A Beautiful Home in the Heart of Hoi An»
  * 2018607792150937 -- район не определяется по адресу «a quiet neighborhood»
  * 2017928622218854 -- район не определяется по адресу «✨ COZY 1-BEDROOM APARTMENT FOR RENT IN HOI AN ✨🏡»
  * 1287853898988310 -- в тексте есть и другая цена того же порядка: 4,568,736 против 4,000,000
  * 1464410321887706 -- тот же текст уже заведён: id 3001312
  * 1507435977585140 -- в посте несколько разных цен: 500,000, 600,000
  * 1506528094342595 -- тип жилья в тексте не назван
  * 1499726755022729 -- в посте несколько разных цен: 500,000, 600,000
  * 1799903581228992 -- в тексте есть и другая цена того же порядка: 36,000 против 30,000
  * 1797050891514261 -- в посте несколько разных цен: 12,000, 13,000, 14,000, 15,000, 17,000, 18,000, 20,000
  * 1797444981474852 -- тот же текст уже заведён: id 3001313
  * 1799249514627732 -- район не определяется по адресу «Apartment Unit !!!»
  * 1798453601373990 -- в посте несколько разных цен: 13,000, 14,000, 15,000, 17,000, 18,000, 20,000
  * 1801283101091040 -- в посте несколько разных цен: 16,000, 18,000, 25,000
  * 3443833065789032 -- район не определяется по адресу «Urban Deca Homes Ortigas»
  * 3436429663196039 -- район не определяется по адресу «PET FRIENDLY. VIEWING THIS SATURDAY! (SEPT19)»
  * 3837694026371144 -- район не определяется по адресу «2 bedrooms»; прецедент расколот: «LVCC»: lt 1
  * 3842813092525904 -- тот же текст уже заведён: id 3001314
  * 3843295509144329 -- тот же текст уже заведён: id 3001315
  * 3842934655847081 -- район не определяется по адресу «South Nha Trang»
  * 3842838922523321 -- тот же текст уже заведён: id 3001316
  * 3841899312617282 -- тот же текст уже заведён: id 3001317
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
  * 1974105989951835 -- тип жилья в тексте не назван
  * 1968186313877136 -- это поиск жилья, а не предложение
  * 1978364799525954 -- похоже на уже заведённое: id 3001282
  * 1979076319454802 -- район не определяется по адресу «Phước Tiến - Trung tâm thành phố»
  * 1968292877199813 -- район не определяется по адресу «Cho Thuê Nhà đường Thích Quảng Đức»
  * 1968092573886510 -- тот же текст уже заведён: id 3001235
  * 4726702167575852 -- это поиск жилья, а не предложение
  * 4728819124030823 -- район не определяется по адресу «Mini villa for rent near the city center»
  * 4728751454037590 -- район не определяется по адресу «South Nha Trang»
  * 4724156191163783 -- это поиск жилья, а не предложение
  * 4727773037468765 -- район не определяется по адресу «South Nha Trang»
  * 4727422960837106 -- район не определяется по адресу «NT RENT»
  * 2092360064754747 -- район не определяется по адресу «side a modern urban area»
  * 2090555578268529 -- в посте несколько разных цен: 530,000, 20,000,000
  * 2090509091606511 -- район не определяется по адресу «Nha Trang Ward»
  * 2369506903583319 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2367700887097254 -- тот же текст уже заведён: id 3001198
  * 2358276808039662 -- в посте несколько разных цен: 10,000,000, 18,000,000
  * 2599789720441683 -- тот же текст уже заведён: id 3001198
  * 2586447371775918 -- помещение под бизнес или здание целиком, а не жильё
  * 2599927840427871 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2588243598262962 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2592618517825470 -- район не определяется по адресу «✨ Brand-new villa»
  * 2582748732145782 -- тип жилья в тексте не назван
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
  * 3255575561303994 -- район не определяется по адресу «Apartment for rent near the beach - opposite Merma»
  * 3246119772249573 -- район не определяется по адресу «VILLA FOR RENT»
  * 3252616481599902 -- район не определяется по адресу «CHO THUÊ NHÀ PHAN CHU TRINH»; прецедент расколот: «CHU TRINH»: совпало только в ссылках строк vtp -- это реклама, а не место
  * 3254576238070593 -- в тексте есть и другая цена того же порядка: 4,013,527 против 7,000,000
  * 3213120192216198 -- район не определяется по адресу «Chính chủ cần cho thuê căn hộ 1 phòng ngủ»; прецедент расколот: «Xô Viết Nghệ Tĩnh»: vtp 1; «Viết Nghệ Tĩnh»: vtp 1
  * 3236985219829695 -- район не определяется по адресу «CHO THUÊ CĂN HỘ KHU PHỐ TÂY»; прецедент расколот: «PHAN CHU TRINH»: совпало только в ссылках строк vtp -- это реклама, а не место
  * 3203441086517442 -- район не определяется по адресу «CHO THUÊ CĂN HỘ 1 PHÒNG NGỦ»
  * 1478438467433555 -- район не определяется по адресу «Apartment for rent near the beach - opposite Merma»
"""
from listing_lock import insert_listings

IDS = [3001361, 3001362, 3001363, 3001364, 3001365, 3001366, 3001367, 3001368, 3001369]

NEW_SRC = r'''
L(3001361,"cebu","bnl","Квартира",25000,None,
  "2-спальная квартира, Banilad.",
  "https://www.facebook.com/groups/994303254903669/posts/1831961487804504/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-25",
  descEn="2-bedroom flat, Banilad.",
  details={"photos": ["assets/fb_photos/1831961487804504/01.webp", "assets/fb_photos/1831961487804504/02.webp", "assets/fb_photos/1831961487804504/03.webp", "assets/fb_photos/1831961487804504/04.webp", "assets/fb_photos/1831961487804504/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001362,"cebu","mab","Квартира",12000,32,
  "1-спальная квартира, 32 м², Mabolo.",
  "https://www.facebook.com/groups/652674525365824/posts/2129515557681706/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-25",
  descEn="1-bedroom flat, 32 m², Mabolo.",
  details={"photos": ["assets/fb_photos/2129515557681706/01.webp", "assets/fb_photos/2129515557681706/02.webp", "assets/fb_photos/2129515557681706/03.webp", "assets/fb_photos/2129515557681706/04.webp", "assets/fb_photos/2129515557681706/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001363,"da-nang","hx","Квартира",10000000,None,
  "1-спальная квартира, Cồn Dầu 25, Hòa Xuân.",
  "https://www.facebook.com/groups/canhochungcudanang/posts/2976792129381531/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="1-bedroom flat, Cồn Dầu 25, Hòa Xuân.",
  details={"photos": ["assets/fb_photos/2976792129381531/01.webp", "assets/fb_photos/2976792129381531/02.webp", "assets/fb_photos/2976792129381531/03.webp", "assets/fb_photos/2976792129381531/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001364,"ha-noi","hm","Квартира",5200000,None,
  "1-спальная квартира, Thinh Liet, Hoàng Mai.",
  "https://www.facebook.com/groups/chothuechungcuminihanoigiare/posts/937482665588999/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="1-bedroom flat, Thinh Liet, Hoàng Mai.",
  details={"photos": ["assets/fb_photos/937482665588999/01.webp", "assets/fb_photos/937482665588999/02.webp", "assets/fb_photos/937482665588999/03.webp", "assets/fb_photos/937482665588999/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001365,"hue","acu","Дом",15000000,81,
  "Дом, 81 м², An Cựu — 4 санузла.",
  "https://www.facebook.com/groups/807531664242245/posts/1466927818302623/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="House, 81 m², An Cựu — 4 bathrooms.",
  details={"photos": ["assets/fb_photos/1466927818302623/01.webp", "assets/fb_photos/1466927818302623/02.webp", "assets/fb_photos/1466927818302623/03.webp", "assets/fb_photos/1466927818302623/04.webp", "assets/fb_photos/1466927818302623/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001366,"nha-trang","ph","Квартира",11000000,65,
  "Квартира, 65 м², Bùi Thiện Ngộ, Phước Hải.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1978201452875622/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Flat, 65 m², Bùi Thiện Ngộ, Phước Hải.",
  details={"photos": ["assets/fb_photos/1978201452875622/01.webp", "assets/fb_photos/1978201452875622/02.webp", "assets/fb_photos/1978201452875622/03.webp", "assets/fb_photos/1978201452875622/04.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001367,"nha-trang","ph","Квартира",13000000,45,
  "Квартира, 45 м², Phước Hải.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1970693793626388/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Flat, 45 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/1970693793626388/01.webp", "assets/fb_photos/1970693793626388/02.webp", "assets/fb_photos/1970693793626388/03.webp", "assets/fb_photos/1970693793626388/04.webp", "assets/fb_photos/1970693793626388/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001368,"nha-trang","btr","Квартира",15000000,38,
  "Квартира, 38 м², Bắc Nha Trang.",
  "https://www.facebook.com/groups/thuecanhotronhatrang/posts/1978862859476148/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Flat, 38 m², Bắc Nha Trang.",
  details={"photos": ["assets/fb_photos/1978862859476148/01.webp", "assets/fb_photos/1978862859476148/02.webp", "assets/fb_photos/1978862859476148/03.webp", "assets/fb_photos/1978862859476148/04.webp", "assets/fb_photos/1978862859476148/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001369,"nha-trang","ph2","Квартира",8500000,30,
  "Квартира, 30 м², Phước Hòa.",
  "https://www.facebook.com/groups/1172766863380743/posts/2091252198198867/","сегодня",0,source="fbgroup",postedOn="2026-09-25",
  descEn="Flat, 30 m², Phước Hòa.",
  details={"photos": ["assets/fb_photos/2091252198198867/01.webp", "assets/fb_photos/2091252198198867/02.webp", "assets/fb_photos/2091252198198867/03.webp", "assets/fb_photos/2091252198198867/04.webp", "assets/fb_photos/2091252198198867/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
