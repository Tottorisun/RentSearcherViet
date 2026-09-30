# -*- coding: utf-8 -*-
"""Facebook, заведение по постам групп: 13 строк, 2026-09-30.

Партию собрал ingest_facebook.py -- без модели в контуре. Заведены только посты,
у которых разобрался тип, ровно одна цена и есть фотографии, а район доказан:
назван в адресной строке, определён по улице (отрезки из OpenStreetMap в
границах районов карты) или по названию, которое на сайте уже стоит в одном
районе не меньше чем в двух строках. Даты у постов Facebook нет: возраст --
время с проверки, пост открыт по ссылке и подтверждён живым (об этом сказано в
оговорке каждой строки).

ЗАВЕДЕНО:
  * 994303254903669/1831364024530917 -- cebu/tlm, 15,000 PHP: район назван в адресе поста
  * 652674525365824/2134579390508656 -- cebu/tlm, 8,000 PHP: район назван в адресе поста
  * 476056366996433/1651973576071367 -- da-nang/ns, 20,000,000 VND: прежний район Ngu Hanh Son весь вошёл в этот
  * 728946289449167/1398710885806034 -- da-nang/hk, 4,800,000 VND: район назван в посте
  * phongtrocanhonhadanang/1491542419805408 -- da-nang/ns, 15,000,000 VND: район назван в посте; улица Mỹ An 19: 1 из 1 отрезков в ns
  * phongtrocanhonhadanang/1491410159818634 -- da-nang/ah, 8,000,000 VND: район назван в посте; улица Đỗ Xuân Hợp: 2 из 2 отрезков в ah; пост: Son Tra
  * 153191128587086/2247439485828896 -- dumaguete/sib, 17,000 PHP: район назван в адресе поста
  * 299437881275577/1797047358181281 -- manila/qzc, 23,000 PHP: район назван в адресе поста
  * 849441571863086/3850156065124940 -- nha-trang/vh, 10,000,000 VND: район назван в адресе поста
  * 2253829621529798/4735843886661680 -- nha-trang/tl, 21,000,000 VND: район назван в адресе поста
  * 2253829621529798/4735693780010024 -- nha-trang/ph, 12,000,000 VND: район назван в адресе поста
  * 1172766863380743/2096627637661323 -- nha-trang/tl, 35,000,000 VND: район назван в адресе поста
  * 1172766863380743/2096498764340877 -- nha-trang/ntr, 30,000,000 VND: район назван в адресе поста

РАЗОБРАНО, НО НЕ ЗАВЕДЕНО (176):
  * 2672374729880903 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»; прецедент расколот: «Đồng Sỹ Bình»: bmt 1
  * 2671323069986069 -- район не определяется по адресу «one of Buôn Ma Thuột's most secure and pristine ur»
  * 2475107316274313 -- район не определяется по адресу «Ywang Alley»
  * 2168691324070411 -- район не определяется по адресу «one of Buôn Ma Thuột's most secure and pristine ur»
  * 2170210010585209 -- район не определяется по адресу «🇻🇳🇻🇳 Cho Thuê Nhà Hẻm Đồng Sỹ Bình - Buôn Mê Thuột»; прецедент расколот: «Đồng Sỹ Bình»: bmt 1
  * 2182552376017639 -- это поиск жилья, а не предложение
  * 2185082292431314 -- нет ни одной скачанной фотографии
  * 4535108773471481 -- район не определяется по адресу «Chủ gửi»
  * 4534963593485999 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 4524078787907813 -- район не определяется по адресу «GIÁ THUÊ : 2.7 TRIỆU»
  * 4583088438673514 -- район не определяется по адресу «CĂN HỘ CAO CẤP KDC THỚI NHỰT FULL NỘI THẤT GẦN ĐH »
  * 4583743761941315 -- район не определяется по адресу «🎉🎐🪩 PHÒNG TRỌ MỚI XÂY ĐƯỜNG VÕ VĂN KIỆT - GẦN ĐỀN »
  * 4582452828737075 -- район не определяется по адресу «🎈🎁🛍️ CĂN NHÀ NHỎ RỘNG»
  * 4578192675829757 -- район не определяется по адресу «🥨🫜🍒 CĂN HỘ CAO CẤP MỚI XÂY KDC AN KHÁNH FULL NỘI T»
  * 4569297596719265 -- тип жилья в тексте не назван
  * 2145727852997245 -- район не определяется по адресу «Chủ gửi»
  * 2145579633012067 -- район не определяется по адресу «🌻CHO THUÊ TRỌ SAU LƯNG ĐHYD HẺM TỔ 4 NVL CÁCH TRẦN»
  * 2132985117604852 -- район не определяется по адресу «CHO THUÊ CĂN HỘ TRUNG TÂM CẦN THƠ»
  * 2187126685524028 -- район не определяется по адресу «📭MINIHOUSE MẶT TIỀN RIÊNG BIỆT - KDC 91B - GẦN ĐHC»
  * 2182373332666030 -- район не определяется по адресу «1/10 trống!»
  * 2186095045627192 -- район не определяется по адресу «MINIHOUSE MẶT TIỀN NGAY TRUNG TÂM - GẦN VINCOM HÙN»
  * 2186094652293898 -- район не определяется по адресу «🍤🍄‍🟫🥧 MINIHOUSE MẶT TIỀN NGAY TRUNG TÂM - GẦN VINC»
  * 2174816730088357 -- тип жилья в тексте не назван
  * 1833859894281330 -- в посте несколько разных цен: 25,000, 35,000
  * 1826883078312345 -- тип жилья в тексте не назван
  * 1837283613938958 -- район не определяется по адресу «6th Street Happy Valley V-rama»
  * 1821535598847093 -- в тексте есть и другая цена того же порядка: 15,000 против 17,000
  * 2136536676979594 -- район не определяется по адресу «READY FOR VIEWING AND MOVE-IN»
  * 2135424270424168 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 2130933830873212 -- это поиск жилья, а не предложение
  * 2134467310519864 -- в посте несколько разных цен: 3,200, 4,000, 5,500
  * 2130977997535462 -- в посте несколько разных цен: 2,000, 10,000, 16,000, 20,000
  * 3766046853552415 -- это поиск жилья, а не предложение
  * 3762964507193983 -- район не определяется по адресу «/ Location:** Đường Mạc Đĩnh Chi»
  * 3752397751583992 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 3751083238382110 -- район не определяется по адресу «/ Location:** C6 Mạc Đĩnh Chi»
  * 3672523882904713 -- тот же текст уже заведён: id 3001274
  * 3669518326538602 -- нет ни одной скачанной фотографии
  * 3586443918179377 -- район не определяется по адресу «✅ Apartment for Rent - 2 Bedrooms - Truong Van Hoa»
  * 2125924031352847 -- это поиск жилья, а не предложение
  * 2134554663823117 -- район не определяется по адресу «Khu tổ hợp nhà e còn trống căn hộ phong cách vinta»
  * 2096068041005113 -- тип жилья в тексте не назван
  * 2124332511511999 -- помещение под бизнес или здание целиком, а не жильё
  * 2116570508954866 -- район не определяется по адресу «Vị trí trung tâm»
  * 2080210199257564 -- это поиск жилья, а не предложение
  * 1749174926738816 -- район не определяется: «MINI VILLA FOR RENT, PHAN KHOANG, Phan Khoang»
  * 1749179183405057 -- район не определяется: «BRAND-NEW 4-BEDROOM HOUSE FOR RENT, TRAN CAO VAN, DA NANG»
  * 1749294170060225 -- в посте несколько разных цен: 18,000,000, 20,000,000
  * 1748788876777421 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT, NAI NAM, HAI CHAU»
  * 1749196030070039 -- похоже на уже заведённое: id 1014099
  * 1749070003415975 -- тот же текст уже заведён: id 3001688
  * 1749377270051915 -- район не определяется: «1 Bedroom Apartment, 🏠1 Bedroom Apartment»
  * 1747683616887947 -- тот же текст уже заведён: id 3001689
  * 1749470933375882 -- тот же текст уже заведён: id 3001690
  * 1746986366957672 -- в посте несколько разных цен: 9,000,000, 11,000,000
  * 2236401146987544 -- тот же текст уже заведён: id 3001691
  * 2234640973830228 -- тот же текст уже заведён: id 3001692
  * 2234141570546835 -- в посте несколько разных цен: 15,000,000, 17,000,000
  * 2228142007813458 -- район не определяется: «Panoma 1, Đà Nẵng, Panoma 1»
  * 2229042801056712 -- тот же текст уже заведён: id 3001693
  * 2208355459792113 -- район не определяется: «CĂN HỘ 2PN, 2-BEDROOM APARTMENT, Biển 1»
  * 2366385470866466 -- район не определяется: «🇻🇳2BR VILLA FOR RENT, SON TRA, DA NANG»
  * 2364890091016004 -- район не определяется: «Newly built house available for rent»
  * 2362788734559473 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT, AN THUONG 14, An Thuong 14»
  * 2363015744536772 -- район не определяется: «HOUSE FOR RENT ON NGUYEN TRI PHUONG STREET, HAI CHAU, 🏠 HOUSE FOR RENT ON NGUYEN TRI PHUONG STREET»
  * 1652531956015529 -- район не определяется: «Đường Hóa Sơn 4, Đà Nẵng, 3 phòng ngủ»; без диакритики это разные улицы: Hóa Sơn 4, Hỏa Sơn 4
  * 1654121815856543 -- в посте несколько разных цен: 30,000,000, 32,000,000
  * 1654328905835834 -- тот же текст уже заведён: id 3001604
  * 1650352909566767 -- в посте несколько разных цен: 28,000,000, 30,000,000, 32,000,000, 35,000,000
  * 1653438335924891 -- район не определяется: «APARTMENT FOR RENT IN THE PANOMA, FULLY FURNISHED, MODERN DESIGN»
  * 1651352766133448 -- похоже на уже заведённое: id 1012086
  * 1653547619247296 -- нет ни одной скачанной фотографии
  * 1400114168999039 -- это поиск жилья, а не предложение
  * 1400007885676334 -- в посте несколько разных цен: 6,500,000, 7,500,000
  * 1398750992468690 -- в посте несколько разных цен: 3,000,000, 4,000,000
  * 1396653956011727 -- в посте несколько разных цен: 11,500,000, 13,500,000, 14,000,000
  * 1397782809232175 -- похоже на уже заведённое: id 3001302
  * 1491594556466861 -- район не определяется: «2-BEDROOM APARTMENT FOR RENT ✨, Bach Dang Street, Da Nang»
  * 1489359883356995 -- район не определяется: «MINI VILLA FOR RENT, PHAN KHOANG, Phan Khoang»
  * 1490701373222846 -- район не определяется: «1-Bedroom Apartment for Rent, An Thuong 3, Da Nang»
  * 1491489309810719 -- похоже на уже заведённое: id 1015603
  * 2247810562458455 -- район не определяется по адресу «Purok Avocado»
  * 2248297409076437 -- тот же текст уже заведён: id 3001530
  * 2249014432338068 -- в тексте есть и другая цена того же порядка: 29,958 против 25,000
  * 2248487302390781 -- район не определяется по адресу «YOUR NEXT HOME: 3BR APARTMENT»
  * 2248969109009267 -- в тексте есть и другая цена того же порядка: 4,430 против 13,500
  * 2245615379344640 -- район не определяется по адресу «Purok Avocado»
  * 2246076275965217 -- район не определяется по адресу «Taclobo»
  * 3821605077995387 -- тип жилья в тексте не назван
  * 3819441944878367 -- тип жилья в тексте не назван
  * 3821479454674616 -- помещение под бизнес или здание целиком, а не жильё
  * 3805749332914295 -- тип жилья в тексте не назван
  * 1839186734095407 -- тип жилья в тексте не назван
  * 1798998168114264 -- тип жилья в тексте не назван
  * 1818287229518691 -- тип жилья в тексте не назван
  * 2003720763597570 -- район не определяется по адресу «T2922»
  * 2014739465829033 -- район не определяется по адресу «Cho thuê căn hộ tại Lê Hồng Phong gần ĐH Y Hải Phò»
  * 2016652748971038 -- район не определяется по адресу «T2986 Cho Thuê Nhà Văn Cao»
  * 2017140412255605 -- район не определяется по адресу «T2983»
  * 2018000975502882 -- район не определяется по адресу «Võ Nguyên Giáp»
  * 2017684395534540 -- район не определяется по адресу «Cho thuê căn hộ Penthouse 1 ngủ tách bếp to rộng t»
  * 28981446664800063 -- район не определяется по адресу «Cho Thuê Chung Cư Sentosa Sky Park»; прецедент расколот: «Sentosa Sky Park»: совпало только в ссылках строк lch -- это реклама, а не место
  * 28948373588107371 -- район не определяется по адресу «HH422 Cho Thuê Chung Cư Hoàng Huy Commerce - Lotus»
  * 28987445850866811 -- район не определяется по адресу «T0108 Cho Thuê Căn hộ Vinhomes Marina»
  * 28981472958130767 -- район не определяется по адресу «T2734 Cho thuê chung cư Sentosa Sky Park»; прецедент расколот: «Sentosa Sky Park»: совпало только в ссылках строк lch -- это реклама, а не место
  * 28959217347022995 -- район не определяется по адресу «🇻🇳 │ VINHOMES MARINA»
  * 1853134039338652 -- район не определяется по адресу «English below ⬇️»
  * 1871302410855148 -- тот же текст уже заведён: id 3001694
  * 1870376907614365 -- тот же текст уже заведён: id 3001695
  * 1865296498122406 -- похоже на уже заведённое: id 1011268
  * 1870306850954704 -- тот же текст уже заведён: id 3001696
  * 1976283110114777 -- район не определяется по адресу «RARE PENTHOUSE»
  * 1976354320107656 -- тот же текст уже заведён: id 3001697
  * 1975807876828967 -- тот же текст уже заведён: id 3001698
  * 1976356766774078 -- тот же текст уже заведён: id 3001699
  * 1975996423476779 -- в посте несколько разных цен: 500,000, 13,000,000
  * 1975226316887123 -- район не определяется по адресу «Tân Cảng»
  * 1974837923592629 -- тот же текст уже заведён: id 3001700
  * 1287853898988310 -- в тексте есть и другая цена того же порядка: 4,568,736 против 4,000,000
  * 1507435977585140 -- в посте несколько разных цен: 500,000, 600,000
  * 1506528094342595 -- тип жилья в тексте не назван
  * 1499726755022729 -- в посте несколько разных цен: 500,000, 600,000
  * 2416297615778545 -- район не определяется по адресу «Available 1 Unit for Rent - Metrica St. Sampaloc M»
  * 2409421553132818 -- в посте несколько разных цен: 10,000, 12,000
  * 2415051862569787 -- в тексте есть и другая цена того же порядка: 7,796 против 20,500
  * 2390246748383632 -- район не определяется по адресу «FOR RENT - 1BR-APARMENT UNIT IN SAMPALOC MANILA.»
  * 2415501675858139 -- район не определяется по адресу «APARTMENT FOR RENT»
  * 2414173732657600 -- в посте несколько разных цен: 15,000, 20,000
  * 1802711964281487 -- тип жилья в тексте не назван
  * 1797050891514261 -- в посте несколько разных цен: 12,000, 13,000, 14,000, 15,000, 17,000, 18,000, 20,000
  * 1798992321320118 -- район не определяется по адресу «- Taft Avenue Manila 15Floor»
  * 1801921144360569 -- в посте несколько разных цен: 7,000, 17,000
  * 1802022997683717 -- тот же текст уже заведён: id 3001701
  * 2718900588542216 -- в посте несколько разных цен: 1,000,000, 18,000,000
  * 2724499167982358 -- район не определяется по адресу «Great location:»
  * 2725069237925351 -- район не определяется по адресу «BRAND-NEW HOUSE FOR RENT»
  * 2724867841278824 -- район не определяется по адресу «City center»
  * 2722002958231979 -- тот же текст уже заведён: id 3001614
  * 2721785808253694 -- нет ни одной скачанной фотографии
  * 2725075927924682 -- район не определяется по адресу «NT RENT»
  * 1981279022567865 -- нет ни одной скачанной фотографии
  * 1983758185653282 -- район не определяется по адресу «CHO THUÊ NHÀ MỚI XÂY»
  * 1980921325936968 -- это поиск жилья, а не предложение
  * 1982808442414923 -- тот же текст уже заведён: id 3001704
  * 1983785945650506 -- тот же текст уже заведён: id 3001705
  * 1981650005864100 -- уже на сайте: id 3001614
  * 3848235645316982 -- район не определяется по адресу «Convenient residential area with plenty of ameniti»
  * 3848866261920587 -- район не определяется по адресу «Convenient location in a lively residential area»
  * 3847311922076021 -- в посте несколько разных цен: 2,000,000, 9,000,000
  * 3849699658503914 -- район не определяется по адресу «Southern Nha Trang»
  * 3850417528432127 -- похоже на уже заведённое: id 3001535
  * 3850029455137601 -- в посте несколько разных цен: 9,500,000, 10,000,000
  * 4733539370225465 -- в посте несколько разных цен: 500,000, 17,000,000
  * 4721597574752978 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4735484286697640 -- это поиск жилья, а не предложение
  * 4725486697697399 -- похоже на уже заведённое: id 3001224
  * 2097537324237021 -- район не определяется по адресу «🍀 FOR RENT»
  * 2097580597566027 -- район не определяется по адресу «FOR RENT»
  * 4628240987445422 -- район не определяется по адресу «1-BEDROOM APARTMENT FOR RENT ~ AIRY»
  * 4620125994923588 -- это поиск жилья, а не предложение
  * 4628105934125594 -- ни улицы, ни комплекса, ни площади, ни комнат -- карточка вышла бы «Студия, район» и ни о чём не говорила
  * 4618707241732130 -- нет ни одной скачанной фотографии
  * 4626748320928022 -- похоже на уже заведённое: id 3001461
  * 4617186755217512 -- это поиск жилья, а не предложение
  * 2369506903583319 -- район не определяется по адресу «CHÍNH CHỦ CHO THUÊ»
  * 2374436799756996 -- район не определяется по адресу «11 phòng»
  * 2366883067179036 -- тот же текст уже заведён: id 3001198
  * 2373450553188954 -- район не определяется по адресу «CHO THUÊ CĂN HỘ THEO THÁNG»
  * 2371536880046988 -- это поиск жилья, а не предложение
  * 2359140247953318 -- тип жилья в тексте не назван
  * 2599789720441683 -- тот же текст уже заведён: id 3001198
  * 2586447371775918 -- помещение под бизнес или здание целиком, а не жильё
  * 2602894183464570 -- район не определяется по адресу «Sunset Town ~7km»
  * 2604061680014487 -- район не определяется по адресу «CHO THUÊ CĂN HỘ THEO THÁNG»
  * 2136536980318297 -- район не определяется по адресу «Đường Lê Đức Thọ»
  * 2143930936245568 -- район не определяется по адресу «⭐️⭐️ CHO THUÊ CĂN HỘ ALTARA RESIDENCE»
"""
from listing_lock import insert_listings

IDS = [3001718, 3001719, 3001720, 3001721, 3001722, 3001723, 3001724, 3001725, 3001726, 3001727, 3001728, 3001729, 3001730]

NEW_SRC = r'''
L(3001718,"cebu","tlm","Дом",15000,None,
  "2-спальный дом, Talamban.",
  "https://www.facebook.com/groups/994303254903669/posts/1831364024530917/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-30",
  descEn="2-bedroom house, Talamban.",
  details={"photos": ["assets/fb_photos/1831364024530917/01.webp", "assets/fb_photos/1831364024530917/02.webp", "assets/fb_photos/1831364024530917/03.webp", "assets/fb_photos/1831364024530917/04.webp", "assets/fb_photos/1831364024530917/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001719,"cebu","tlm","Дом",8000,None,
  "1-спальный дом, Talamban.",
  "https://www.facebook.com/groups/652674525365824/posts/2134579390508656/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-30",
  descEn="1-bedroom house, Talamban.",
  details={"photos": ["assets/fb_photos/2134579390508656/01.webp", "assets/fb_photos/2134579390508656/02.webp", "assets/fb_photos/2134579390508656/03.webp", "assets/fb_photos/2134579390508656/04.webp", "assets/fb_photos/2134579390508656/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001720,"da-nang","ns","Дом",20000000,None,
  "3-спальный дом, House for rent on Kim Dong, Ngũ Hành Sơn — 3 санузла.",
  "https://www.facebook.com/groups/476056366996433/posts/1651973576071367/","сегодня",0,source="fbgroup",postedOn="2026-09-30",
  descEn="3-bedroom house, House for rent on Kim Dong, Ngũ Hành Sơn — 3 bathrooms.",
  details={"photos": ["assets/fb_photos/1651973576071367/01.webp", "assets/fb_photos/1651973576071367/02.webp", "assets/fb_photos/1651973576071367/03.webp", "assets/fb_photos/1651973576071367/04.webp", "assets/fb_photos/1651973576071367/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001721,"da-nang","hk","Студия",4800000,None,
  "Студия, ✨ STUDIO NAM CAO, Hòa Khánh.",
  "https://www.facebook.com/groups/728946289449167/posts/1398710885806034/","сегодня",0,source="fbgroup",postedOn="2026-09-30",
  descEn="Studio, ✨ STUDIO NAM CAO, Hòa Khánh.",
  details={"photos": ["assets/fb_photos/1398710885806034/01.webp", "assets/fb_photos/1398710885806034/02.webp", "assets/fb_photos/1398710885806034/03.webp", "assets/fb_photos/1398710885806034/04.webp", "assets/fb_photos/1398710885806034/05.webp"], "am": ["w", "win"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001722,"da-nang","ns","Квартира",15000000,None,
  "1-спальная квартира, Mỹ An 19, Ngũ Hành Sơn.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1491542419805408/","сегодня",0,source="fbgroup",postedOn="2026-09-30",
  descEn="1-bedroom flat, Mỹ An 19, Ngũ Hành Sơn.",
  details={"photos": ["assets/fb_photos/1491542419805408/01.webp", "assets/fb_photos/1491542419805408/02.webp", "assets/fb_photos/1491542419805408/03.webp", "assets/fb_photos/1491542419805408/04.webp", "assets/fb_photos/1491542419805408/05.webp"], "am": ["k"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
L(3001723,"da-nang","ah","Квартира",8000000,45,
  "1-спальная квартира, 45 м², Đỗ Xuân Hợp, An Hải.",
  "https://www.facebook.com/groups/phongtrocanhonhadanang/posts/1491410159818634/","сегодня",0,source="fbgroup",postedOn="2026-09-30",
  descEn="1-bedroom flat, 45 m², Đỗ Xuân Hợp, An Hải.",
  details={"photos": ["assets/fb_photos/1491410159818634/01.webp", "assets/fb_photos/1491410159818634/02.webp", "assets/fb_photos/1491410159818634/03.webp", "assets/fb_photos/1491410159818634/04.webp", "assets/fb_photos/1491410159818634/05.webp"], "am": ["w"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(3001724,"dumaguete","sib","Дом",17000,None,
  "3-спальный дом, Sibulan.",
  "https://www.facebook.com/groups/153191128587086/posts/2247439485828896/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-30",
  descEn="3-bedroom house, Sibulan.",
  details={"photos": ["assets/fb_photos/2247439485828896/01.webp", "assets/fb_photos/2247439485828896/02.webp", "assets/fb_photos/2247439485828896/03.webp", "assets/fb_photos/2247439485828896/04.webp", "assets/fb_photos/2247439485828896/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001725,"manila","qzc","Квартира",23000,40,
  "2-спальная квартира, 40 м², Quezon City.",
  "https://www.facebook.com/groups/299437881275577/posts/1797047358181281/","сегодня",0,source="fbgroup",cur="PHP",postedOn="2026-09-30",
  descEn="2-bedroom flat, 40 m², Quezon City.",
  details={"photos": ["assets/fb_photos/1797047358181281/01.webp", "assets/fb_photos/1797047358181281/02.webp", "assets/fb_photos/1797047358181281/03.webp", "assets/fb_photos/1797047358181281/04.webp", "assets/fb_photos/1797047358181281/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001726,"nha-trang","vh","Квартира",10000000,30,
  "Квартира, 30 м², Vĩnh Hải.",
  "https://www.facebook.com/groups/849441571863086/posts/3850156065124940/","сегодня",0,source="fbgroup",postedOn="2026-09-30",
  descEn="Flat, 30 m², Vĩnh Hải.",
  details={"photos": ["assets/fb_photos/3850156065124940/01.webp", "assets/fb_photos/3850156065124940/02.webp", "assets/fb_photos/3850156065124940/03.webp", "assets/fb_photos/3850156065124940/04.webp", "assets/fb_photos/3850156065124940/05.webp"], "am": ["w", "b", "lift", "pet"], "fl": 4, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001727,"nha-trang","tl","Квартира",21000000,60,
  "2-спальная квартира, 60 м², Nguyen Thien Thuat, Tân Lập — 2 санузла.",
  "https://www.facebook.com/groups/2253829621529798/posts/4735843886661680/","сегодня",0,source="fbgroup",postedOn="2026-09-30",
  descEn="2-bedroom flat, 60 m², Nguyen Thien Thuat, Tân Lập — 2 bathrooms.",
  details={"photos": ["assets/fb_photos/4735843886661680/01.webp", "assets/fb_photos/4735843886661680/02.webp", "assets/fb_photos/4735843886661680/03.webp", "assets/fb_photos/4735843886661680/04.webp", "assets/fb_photos/4735843886661680/05.webp"], "am": ["pet"], "flHigh": 1, "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001728,"nha-trang","ph","Квартира",12000000,50,
  "1-спальная квартира, 50 м², Phước Hải.",
  "https://www.facebook.com/groups/2253829621529798/posts/4735693780010024/","сегодня",0,source="fbgroup",postedOn="2026-09-30",
  descEn="1-bedroom flat, 50 m², Phước Hải.",
  details={"photos": ["assets/fb_photos/4735693780010024/01.webp", "assets/fb_photos/4735693780010024/02.webp", "assets/fb_photos/4735693780010024/03.webp", "assets/fb_photos/4735693780010024/04.webp", "assets/fb_photos/4735693780010024/05.webp"], "am": ["w", "lift"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001729,"nha-trang","tl","Дом",35000000,None,
  "4-спальный дом, Tân Lập — 4 санузла.",
  "https://www.facebook.com/groups/1172766863380743/posts/2096627637661323/","сегодня",0,source="fbgroup",postedOn="2026-09-30",
  descEn="4-bedroom house, Tân Lập — 4 bathrooms.",
  details={"photos": ["assets/fb_photos/2096627637661323/01.webp", "assets/fb_photos/2096627637661323/02.webp", "assets/fb_photos/2096627637661323/03.webp", "assets/fb_photos/2096627637661323/04.webp", "assets/fb_photos/2096627637661323/05.webp"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
L(3001730,"nha-trang","ntr","Дом",30000000,270,
  "3-спальный дом, 270 м², Nam Nha Trang.",
  "https://www.facebook.com/groups/1172766863380743/posts/2096498764340877/","сегодня",0,source="fbgroup",postedOn="2026-09-30",
  descEn="3-bedroom house, 270 m², Nam Nha Trang.",
  details={"photos": ["assets/fb_photos/2096498764340877/01.webp", "assets/fb_photos/2096498764340877/02.webp", "assets/fb_photos/2096498764340877/03.webp", "assets/fb_photos/2096498764340877/04.webp", "assets/fb_photos/2096498764340877/05.webp"], "am": ["lift"], "notice": "Источник — пост в группе Facebook. Точной даты размещения Facebook не отдаёт, поэтому возраст здесь — это время с проверки: программа открыла пост по ссылке и убедилась, что он жив. Описание собрано из полей поста — тип, спальни, площадь, адрес и цена; рекламный текст не пересказан. Фотографии взяты из самого поста и хранятся на этом сайте: ссылки Facebook на изображения подписаны и живут около четырёх дней. Цену и условия подтверждайте у автора объявления.", "noticeEn": "Source: a post in a Facebook group. Facebook publishes no posting date, so the age shown is the time since the check: the program opened the post and confirmed it is alive. The description was assembled from the post's fields — type, bedrooms, size, address and price; the marketing text is not retold. The photos come from the post itself and are stored on this site, because Facebook's own image links are signed and expire in about four days. Confirm the price and terms with the poster."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
