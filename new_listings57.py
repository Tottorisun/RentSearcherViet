# -*- coding: utf-8 -*-

NEW_SRC = '''
L(1399,"da-lat","xh","Квартира",6500000,30,
  "Меблированная 1-спальная квартира с балконом, ул. Phan Đình Phùng, Xuân Hương — гостиная, спальня, с/у, полная меблировка (холодильник, ТВ, водонагреватель), рядом Nam Á Bank, Winmart, Bách Hóa Xanh, ~3 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134314653.htm","сегодня",0,source="chotot",
  details={"contact":"Hương Lê","photos":["https://cdn.chotot.com/ESnEI6Jq26IxNKVpq2ejtvrhI6CeYO5KkJ3_p7qu7v0/preset:view/plain/8b198a637d3b6ae7a2ff580ca341494d-2998914273611287258.jpg"]}),

L(1400,"da-lat","lv","Квартира",11500000,80,
  "2-спальная квартира с балконом, ул. Trần Quang Khải, Lâm Viên — 1 с/у, вид на долину, полная меблировка (холодильник, ТВ, стиральная машина), общий двор, ~5 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134314528.htm","сегодня",0,source="chotot",
  details={"contact":"Hương Lê","photos":["https://cdn.chotot.com/EpqELwuK-pP9k2lqOsLYxiuxDJMjohK1RlslsHxBBYw/preset:view/plain/81c755c702078eb42ff396deb7d7280b-2998913502304002268.jpg"]}),

L(1401,"da-lat","lv","Квартира",3500000,45,
  "1-спальная квартира с антресолью, ул. Mê Linh, Lâm Viên — базовая меблировка (кровать, водонагреватель, кухонная зона), рядом Bách Hóa Xanh, рынок, спортзал, ~10 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134314396.htm","сегодня",0,source="chotot",
  details={"notice":"меблировка базовая (в структурном поле объявления отмечено «Nhà trống», но в тексте указана базовая мебель)","contact":"Hương Lê","photos":["https://cdn.chotot.com/taMX-k3aNI3SVVHDNI_0Gxc108GosStl1j_gEEgQoiQ/preset:view/plain/e01f5e49d6652b0437cb7cebaabe2141-2998912618945596300.jpg"]}),

L(1402,"da-lat","lv","Квартира",7500000,45,
  "1-спальная квартира, ул. Trương Văn Hoàn, Lâm Viên — полная меблировка (холодильник, стиральная машина, ТВ, диван), ~5 мин до озера Than Thở.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134311932.htm","сегодня",0,source="chotot",
  details={"notice":"цена зависит от этажа — 7,5 млн (3-й этаж) или 8 млн (1-й этаж)","contact":"Hương Lê","photos":["https://cdn.chotot.com/D4UMJFzK0t5OPXWwuGyI8j15UMR_1iyKGwqvSJdjR0s/preset:view/plain/66705e049a964ecd6c33c7ca4e33aeca-2998892933897336332.jpg"]}),

L(1403,"da-lat","lv","Квартира",8000000,50,
  "2-спальная квартира в ЖК Yersin, Lâm Viên — новая полная меблировка, лифт, тихий охраняемый район, 600 м до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134311179.htm","сегодня",0,source="chotot",
  details={"notice":"цена 8 млн — при контракте от 3 лет; при контракте на 1-2 года цена другая (не указана в объявлении); депозит 2 месяца, оплата за 1","contact":"Minh Anh","photos":["https://cdn.chotot.com/ppJ-3Qgcn6HiUWd3Q0UoK16Lxl2j3AHwj9iDD2welWY/preset:view/plain/3aa33e63c1dbf6c0d196168e17570de9-2998888351407623052.jpg"]}),

L(1404,"da-lat","lv","Квартира",9000000,60,
  "2-спальная квартира с полной меблировкой, ул. Nguyễn Đình Chiểu, Lâm Viên — «заезжай с чемоданом», депозит 1 месяц.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133600009.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trần Thị Bích Thuỳ","photos":["https://cdn.chotot.com/93A-xa6ShB_fcCn4ZlnmIoXlExUDWMRXQ9U44Nyf1wo/preset:view/plain/2aec2c3908bd144cdd832a312f75e6c9-2993511507454289101.jpg"]}),

L(1405,"da-lat","cl","Дом",21000000,72,
  "Дом целиком на ул. Lê Thánh Tôn, Cam Ly — 1 этаж + 3 надстройки, участок 288м², 4 спальни/5 с/у, кухня, комната для алтаря, сдаётся пустым (без мебели), рядом рынок, школы, больница, АЗС.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134268166.htm","3 дня назад",3,source="chotot",
  details={"notice":"пригоден под небольшой бизнес (кафе, офис, гостевой дом), но не под общепит/бар","contact":"Thanh Thủy","photos":["https://cdn.chotot.com/4NpKlo7WEsYhwMo_3SL5l9pZoRtjatEhfEe0thpTjFI/preset:view/plain/db99c4e55e9e9b23afb218a1f5506074-2998559063886219149.jpg"]}),

L(1406,"phan-thiet","mn","Студия",5000000,32,
  "Студия с видом на море в жилом комплексе Apec Mandala, Mũi Né — 32м², в стоимость входят управление домом и WiFi. Аренда от 6 месяцев до 1 года.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-apec-mandala-wyndham-binh-thuan-phuong-mui-ne-tinh-lam-dong/cho-view-bien-32m-gia-5-trieu-thang-bao-phi-quan-ly-wifi-pr46210314","3 дня назад",3,source="batdongsan",
  details={"contact":"Hoàng My","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/21/20260821111923-4fa4_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/21/20260821111927-6315_wm.jpg"]}),

L(1407,"quy-nhon","qnn","Квартира",6000000,46,
  "1-спальная квартира с полной меблировкой (кондиционер, кровать, холодильник), FLC SeaTower, ул. An Dương Vương, Quy Nhơn Nam; минимальный срок аренды 1 год.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-flc-seatower-phuong-quy-nhon-nam-tinh-gia-lai/cho-ch-1pn-46m2-an-duong-vuong-nguyen-van-500k-em-pr45577797","вчера",1,source="batdongsan",
  details={"contact":"Ngô Minh Hiếu","photos":["https://file4.batdongsan.com.vn/crop/600x315/2025/12/04/20251204084249-11ff_wm.jpg"]}),

L(1408,"quy-nhon","qnn","Квартира",None,108,
  "3-спальная квартира в FLC SeaTower, ул. An Dương Vương, Quy Nhơn Nam, вмещает 8-12 человек, полная меблировка; минимальный срок 6 месяцев.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-flc-seatower-phuong-quy-nhon-nam-tinh-gia-lai/cho-3pn-an-duong-vuong-1-5-trieu-vnd-em-108m2-pr45577841","вчера",1,source="batdongsan",
  details={"notice":"цена по запросу — карточка и детальная страница показывают «Thỏa thuận», в тексте только посуточная ставка (1,5 млн/ночь), помесячная цена не указана","contact":"Ngô Minh Hiếu","photos":["https://file4.batdongsan.com.vn/crop/600x315/2025/12/04/20251204062036-f001_wm.jpg"]}),

L(1409,"quy-nhon","qnn","Студия",6500000,46,
  "Студия в FLC SeaTower, ул. Võ Thị Yến 44, Quy Nhơn Nam — 200 м до моря, меблирована.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-flc-seatower-phuong-quy-nhon-nam-tinh-gia-lai/cho-tot-1pn-45m2-cach-bien-200m-pr46208672","3 дня назад",3,source="batdongsan",
  details={"contact":"Tùng Quy Nhơn Safehome","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/20/20260820232929-8d4c_wm.jpg"]}),

L(1410,"quy-nhon","qn","Квартира",8000000,65,
  "Угловая 2-спальная квартира (2 с/у), Altara Residences, 76 Trần Hưng Đạo, Quy Nhơn — высокий этаж, вид на море, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-altara-residences-phuong-quy-nhon-tinh-gia-lai/cho-residence-1pn-2pn-2wc-2pn-goc-tang-trung-cao-view-bien-full-nt-pr45172456","сегодня",0,source="batdongsan",
  details={"contact":"Mỹ Linh","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/07/20260807142931-622e_wm.jpg"]}),

L(1411,"quy-nhon","qn","Квартира",8000000,65,
  "2-спальная квартира (2 с/у), Phú Tài Residence, ул. Lê Đức Thọ, Quy Nhơn — большой балкон, бассейн на 3 этаже, зал, 5 мин до пляжа Xuân Diệu.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phu-tai-residence-phuong-quy-nhon-tinh-gia-lai/cho-cc-cao-cap-2-phong-ngu-full-nt-7tr-th-view-bien-mat-pr43127816","3 дня назад",3,source="batdongsan",
  details={"contact":"Minh Dũng Land","photos":["https://file4.batdongsan.com.vn/crop/600x315/2025/05/31/20250531084558-b82f_wm.jpg"]}),

L(1412,"quy-nhon","qn","Квартира",8500000,65,
  "Угловая 2-спальная квартира (2 с/у), Altara Residences, ул. Trần Hưng Đạo, этаж 41 — вид на море, полная меблировка, документы готовы.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-altara-residences-phuong-quy-nhon-tinh-gia-lai/cho-residence-6-5tr-7-5tr-th-2pn-2wc-tang-trung-cao-view-bien-pr42954925","3 дня назад",3,source="batdongsan",
  details={"contact":"Minh Dũng Land","photos":["https://file4.batdongsan.com.vn/crop/600x315/2025/03/06/20250306104506-923b_wm.jpg"]}),

L(1413,"quy-nhon","qn","Квартира",8500000,65,
  "2-спальная квартира (2 с/у), Altara Residences, 76 Trần Hưng Đạo — 300 м до моря, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-altara-residences-phuong-quy-nhon-tinh-gia-lai/cho-tot-2pn-65m2-cach-bien-200m-pr46208542","3 дня назад",3,source="batdongsan",
  details={"notice":"похожа на другую квартиру в этом же доме (тот же метраж и близкая цена), но другой контакт/агент — возможна параллельная продажа одного юнита разными брокерами; не объединено из-за отсутствия точного совпадения номера квартиры","contact":"Tùng Quy Nhơn Safehome","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/20/20260820222205-643c_wm.jpg"]}),

L(1414,"quy-nhon","qn","Студия",None,47,
  "Студия в TMS Luxury Hotel & Residences, 28 ул. Nguyễn Huệ — 50 м до моря, вид на город/лагуну Thị Nại, доступ к ресторану, скайбару, бассейну.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-tms-luxury-hotel-residences-phuong-quy-nhon-tinh-gia-lai/cho-pull-man-ngan-han-va-dai-han-lien-he-pr39050214","3 дня назад",3,source="batdongsan",
  details={"notice":"цена по запросу («Thỏa thuận», меняется от срока аренды)","contact":"Nguyễn Lê Nhã Phương","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/03/14/20260314085524-e9c8_wm.jpg"]}),

L(1415,"quy-nhon","qnd","Квартира",3500000,64,
  "Квартира в ЖК Ecolife Riverside, ул. Điện Biên Phủ, Quy Nhơn Đông — полная меблировка, доступны разные планировки у того же продавца.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-ecolife-riverside-phuong-quy-nhon-dong-tinh-gia-lai/cho-chi-tu-3-6-trieu-nha-moi-pr36709073","3 дня назад",3,source="batdongsan",
  details={"contact":"Ngô Minh Hoàn","photos":["https://file4.batdongsan.com.vn/crop/600x315/2023/03/12/20230312143222-8769_wm.jpg"]}),

L(1416,"vung-tau","vtp","Квартира",8000000,30,
  "Меблированная квартира (телевизор, холодильник, кондиционер, стиральная машина, кухня), ул. Hoàng Văn Hòe (C19), Vũng Tàu — ~800 м до пляжа Bãi Sau, ~10 мин на машине до рынка Vũng Tàu.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134313813.htm","сегодня",0,source="chotot",
  details={"contact":"Mùi Phan Thị","photos":["https://cdn.chotot.com/wFg1YuMuCXFl1tAiPgfRLyhkV-wj5MNuAeTT1rYtnhw/preset:view/plain/77623251fc8ef018a29cf9ed4f24d1ec-2998906905357398425.jpg"]}),

L(1417,"vung-tau","rd","Дом",7500000,150,
  "Дом на первой линии по ул. Ba Tháng Hai (3/2), №28, Rạch Dừa — вид на море, рядом парк Sun World Vũng Tàu (салюты), 2 спальни/1 с/у, подходит под жильё или небольшой бизнес.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-vung-tau-ba-ria-vung-tau/134315419.htm","сегодня",0,source="chotot",
  details={"contact":"Phuong Chi","photos":["https://cdn.chotot.com/ZsNz-n2OuSeqhHE_evVFIdfX-70tVYYLgBc5wCOQtJ8/preset:view/plain/9712f1bcd071d09dce838da421d2e99e-2998916394546276371.jpg"]}),

L(1418,"vung-tau","vtp","Дом",12000000,100,
  "Дом 1 этаж + 3 этажа (5×20м), 4 спальни/5 с/у, тихий тупиковый переулок для авто, ул. Lê Lợi, Vũng Tàu — рядом рынок и школа, подходит под семью, офис или онлайн-бизнес.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-loi-1-phuong-vung-tau-tp-ho-chi-minh/cho-ep-1-tret-3-lau-hem-o-to-uong-gia-12tr-thang-pr46213330","2 дня назад",2,source="batdongsan",
  details={"notice":"точной даты публикации сайт не даёт, оценено по дате загрузки фото на CDN (22 авг)","contact":"Nguyễn Ngọc Long","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/22/20260822085447-acd7_wm.jpg"]}),

L(1419,"vung-tau","vtp","Квартира",20000000,80,
  "Квартира в ЖК The Sóng, ул. Thi Sách, Vũng Tàu — 2 спальни/2 с/у, вид на море и башню Tam Thắng, мебель почти новая (99%), только долгосрочная аренда.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-pho-thi-sach-the-song/cho-o-lau-dai-80m2-2pn-2wc-view-truc-dien-bien-va-thap-tam-thang-pr46210093","3 дня назад",3,source="batdongsan",
  details={"notice":"точной даты публикации сайт не даёт, оценено по дате загрузки фото на CDN (21 авг)","contact":"phạm anh phương","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/21/20260821104912-7afe_wm.jpg"]}),

L(1420,"da-nang","ah","Квартира",8500000,50,
  "1-спальная квартира с 2 кондиционерами и своей стиральной машиной на ул. Trần Đình Đàn, An Hải — лифт, паркинг, 300 м до пляжа Phạm Văn Đồng, можно с животными.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134322571.htm","сегодня",0,source="chotot",
  details={"contact":"Thái An","photos":["https://cdn.chotot.com/56PzBNpWBiOtzsEwNBoif7HOR1yBOTHG4pZ9N2lYrD4/preset:view/plain/79f1d192c999d222aa49ba3e6599cf4e-2998999543594553423.jpg"]}),

L(1421,"da-nang","ah","Квартира",17500000,82,
  "2-спальная квартира в ЖК Monarchy (An Trung 2), An Hải — полная меблировка, бассейн, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134321049.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Thị Minh Thư"}),

L(1422,"da-nang","ah","Квартира",8000000,40,
  "1-спальная меблированная квартира на ул. Tô Hiến Thành, An Hải — принимают иностранцев и краткосрочную аренду от 1 месяца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134320946.htm","сегодня",0,source="chotot",
  details={"contact":"Ha for rent APT"}),

L(1423,"da-nang","ah","Квартира",10000000,40,
  "Пентхаус с полной меблировкой на ул. Phạm Tu, An Hải — рядом пляж, животные не разрешены.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134320232.htm","сегодня",0,source="chotot",
  details={"contact":"MrNam Căn Hộ Giá Tốt Đà Nẵng"}),

L(1424,"da-nang","ah","Дом",40000000,210,
  "Дом в закрытом комплексе Euro Village у моста Trần Thị Lý на реке Hàn, An Hải — участок 100м², 4 спальни, охрана 24/7, 1,5 км до моря.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/133708643.htm","сегодня",0,source="chotot",
  details={"contact":"hồ ngọc minh"}),

L(1425,"da-nang","ah","Дом",22000000,75,
  "Дом на 3 спальни (полная меблировка) на ул. Nguyễn Công Trứ, An Hải — тихий переулок, умный замок, Smart TV, 10 мин пешком до моря.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134323156.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Đức Minh Tuấn"}),

L(1426,"da-nang","ah","Дом",18000000,90,
  "3-этажный дом (4 спальни/2 с/у) на ул. Hồ Nghinh, An Hải, рядом с пляжем — без мебели, подходит для жилья и бизнеса.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134322143.htm","сегодня",0,source="chotot",
  details={"contact":"Trân Duy Hải"}),

L(1427,"da-nang","ah","Дом",220000000,155,
  "Здание (8 этажей) с 18 квартирами (студии 25-30м², 1-спальные 30-35м², пентхаус 90м²) + коммерческое помещение у пляжа, р-н Hồ Nghinh, An Hải.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134321307.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"MR HUY"}),

L(1428,"da-nang","ah","Дом",110000000,100,
  "Здание (5 этажей) на 10 квартир (5 студий + 5 1-спальных) на ул. Nguyễn Xuân Khoát, An Hải — антресоль под бизнес.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134321176.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"MR HUY"}),

L(1429,"da-nang","ak","Квартира",5000000,40,
  "1-спальная меблированная квартира на ул. Bùi Tấn Diên, An Khê, рядом с автовокзалом — свободна с 30 августа.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134321478.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Thanh Phong"}),

L(1430,"da-nang","ak","Дом",27000000,100,
  "Дом (3 этажа) с 4 спальнями/4 с/у, полная меблировка, ул. Cần Giuộc, An Khê — ширина фасада 7,5 м.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134307159.htm","сегодня",0,source="chotot",
  details={"contact":"Nhuận Oanh"}),

L(1431,"da-nang","cl2","Квартира",5800000,45,
  "Новая 1-спальная квартира на 4 этаже с балконом на ул. Bình Hòa 15, Cẩm Lệ, рядом университет Đông Á.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134322315.htm","сегодня",0,source="chotot",
  details={"contact":"Apartment Đà Nẵng"}),

L(1432,"da-nang","cl2","Квартира",4400000,40,
  "1-спальная квартира на ул. Bàu Gia Thượng 1, Cẩm Lệ — центр района, 500 м до рынка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134320547.htm","сегодня",0,source="chotot",
  details={"contact":"Đỗ Đăng Khôi"}),

L(1433,"da-nang","cl2","Дом",16000000,280,
  "4-этажный дом (70м²/этаж) с 4 спальнями на ул. Nguyễn Nhàn 100, Cẩm Lệ, напротив больницы Cẩm Lệ, рядом УК района.",
  "https://batdongsan.com.vn/cho-thue-nha-mat-pho-duong-nguyen-nhan_1-phuong-cam-le-tp-da-nang/cho-4-tang-4pn-16-trieu-thuong-luong-tien-100-nhan-uong-10-5m-pr46219871","сегодня",0,source="batdongsan",
  details={"notice":"цена по договорённости («thương lượng»); похожий дом на этой же улице уже есть в базе (48 Nguyễn Nhàn, 125м², 3 этажа), но параметры заметно отличаются (280м² vs 125м², 4 этажа vs 3, №100 vs №48) — не объединено","contact":"Mr.Phúc"}),

L(1434,"da-nang","hx","Студия",5000000,30,
  "Меблированная студия у моста Hòa Xuân, ул. Cồn Dầu 15, Hòa Xuân — своя стиральная машина, терраса на крыше.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/133965392.htm","сегодня",0,source="chotot",
  details={"contact":"CĂN HỘ LKA HOÀ XUÂN"}),

L(1435,"da-nang","hx","Квартира",10000000,85,
  "2-спальная квартира на ул. Vũ Thành Năm, Hòa Xuân — базовая меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134320313.htm","сегодня",0,source="chotot",
  details={"contact":"Công Bình"}),

L(1436,"da-nang","hx","Дом",18000000,100,
  "3-спальный дом (2 этажа, 3 кондиционера), фасад 10,5 м, ул. Mai Chí Thọ, Hòa Xuân.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134322444.htm","сегодня",0,source="chotot",
  details={"contact":"DAVICO LAND"}),

L(1437,"da-nang","hx","Дом",25000000,100,
  "Новый сквозной дом (3 этажа) на ул. Lê Quảng Chí, Hòa Xuân.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134322306.htm","сегодня",0,source="chotot",
  details={"contact":"Mr AN"}),

L(1438,"da-nang","hx","Дом",18000000,100,
  "Новый дом (3 этажа, 3 спальни) на ул. Diên Hồng, Hòa Xuân, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134322068.htm","сегодня",0,source="chotot",
  details={"contact":"Mr AN"}),

L(1439,"da-nang","hx","Дом",23000000,100,
  "Дом (3 этажа, 3 спальни/3 с/у) с полной меблировкой, ул. Mai Chí Thọ (10,5 м), Hòa Xuân.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134322015.htm","сегодня",0,source="chotot",
  details={"contact":"Mr AN"}),

L(1440,"da-nang","hx","Дом",8000000,100,
  "Одноэтажный дом (2 спальни/2 с/у) на ул. Khương Hữu Dụng, Hòa Xuân — кондиционер, парковка на 7 мест, рядом рынок Hòa Xuân.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134254135.htm","3 дня назад",3,source="chotot",
  details={"contact":"Thuỷ DT"}),

L(1441,"da-nang","lc","Квартира",9000000,55,
  "1-спальная меблированная квартира на ул. Nguyễn Lương Bằng 173, Liên Chiểu, рядом университет Bách Khoa — отдельная стирка/сушка, бесплатная уборка раз в месяц.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/107137945.htm","2 дня назад",2,source="chotot",
  details={"contact":"Van Dong Nguyen"}),

L(1442,"da-nang","lc","Квартира",10500000,60,
  "2-спальная квартира, тот же дом на ул. Nguyễn Lương Bằng 173, Liên Chiểu — другая планировка, тот же агент.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/127121957.htm","2 дня назад",2,source="chotot",
  details={"contact":"Van Dong Nguyen"}),

L(1443,"da-nang","lc","Квартира",30000000,97,
  "3-спальная квартира в ЖК MIA Center Point, ул. Ngô Thì Nhậm, Liên Chiểu — полная меблировка, готова к заезду.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mia-center-point-phuong-lien-chieu-tp-da-nang/cho-3-phong-ngu-gia-30-trieu-a-nang-pr46218726","сегодня",0,source="batdongsan",
  details={"notice":"в базе уже есть меньшие юниты этого же ЖК (63-67м², 2 спальни) — этот 97м²/3-спальный явно другой юнит, не дубль","contact":"Nguyễn Lê Vương"}),

L(1444,"da-nang","ns","Квартира",7500000,40,
  "1-спальная квартира, ул. Nguyễn Lữ (Khu Nam Việt Á), Ngũ Hành Sơn, рядом река Hàn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134323185.htm","сегодня",0,source="chotot",
  details={"contact":"Hiền Nguyễn"}),

L(1445,"da-nang","ns","Квартира",32000000,70,
  "2-спальная квартира в ЖК Panoma, ул. Trần Thị Lý, Ngũ Hành Sơn — бассейн, спортзал, охрана 24/7, рядом мост Trần Thị Lý и пляж Mỹ Khê.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134322599.htm","сегодня",0,source="chotot",
  details={"contact":"Kiều Oanh"}),

L(1446,"da-nang","ns","Квартира",32000000,70,
  "Квартира в том же ЖК Panoma, ул. Trần Thị Lý, Ngũ Hành Sơn — параллельное объявление другого агента.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134322008.htm","сегодня",0,source="chotot",
  details={"notice":"параметры идентичны соседнему объявлению этого же ЖК (Panoma, 2 спальни, 70м², 32 млн) — возможно, тот же физический юнит через другого посредника; оставлено отдельно, т.к. номер квартиры не указан ни там, ни там","contact":"My Trần"}),

L(1447,"da-nang","ns","Квартира",20000000,50,
  "1-спальная премиум-квартира, ЖК Panoma 2, ул. Phạm Hữu Kính, Ngũ Hành Sơn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134321580.htm","сегодня",0,source="chotot",
  details={"contact":"Thanh Trung Haviland"}),

L(1448,"da-nang","ns","Студия",6100000,30,
  "Тихая студия на 4 этаже, кв. 405, ул. Đa Mặn 5, Ngũ Hành Sơn, рядом университет Kinh tế — общая прачечная и терраса; принимают иностранцев (кроме Китая/Индии), без животных/детей.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134321203.htm","сегодня",0,source="chotot",
  details={"contact":"Viết Đức Trần"}),

L(1449,"da-nang","ns","Квартира",14000000,30,
  "1-спальная квартира на ул. Lê Quang Đạo, Ngũ Hành Sơn, рядом пляж Mỹ Khê и Phố Tây An Thượng — можно с животными, есть уборка, wifi.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134321165.htm","сегодня",0,source="chotot",
  details={"contact":"Mr Khanh Haviland"}),

L(1450,"da-nang","ns","Квартира",9900000,48,
  "1-спальная квартира, кв. 202, ул. Đa Mặn 5, Ngũ Hành Sơn — большие окна и балкон, рядом университет Kinh tế.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134320885.htm","сегодня",0,source="chotot",
  details={"contact":"Viết Đức Trần"}),

L(1451,"da-nang","ns","Квартира",18000000,65,
  "2-спальная квартира со 100% новой мебелью, 2 балкона, ул. Trần Quốc Vượng, Khu đô thị FPT, Ngũ Hành Sơn — рядом школа Singapore, река и море.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/132930327.htm","сегодня",0,source="chotot",
  details={"contact":"Hiền Nguyễn"}),

L(1452,"da-nang","ns","Квартира",8500000,50,
  "1-спальная квартира на ул. An Thượng 15, Ngũ Hành Sơn — можно с животными, уборка раз в 2 недели, рядом пляж Mỹ Khê.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134320787.htm","сегодня",0,source="chotot",
  details={"contact":"HAVILAND HOUSE"}),

L(1453,"da-nang","ns","Квартира",5500000,50,
  "1-спальная квартира на ул. Nguyễn Đình Chiểu, Ngũ Hành Sơn, рядом больница на 600 коек и рынок Khuê Mỹ — кондиционер Daikin, стиральная машина Electrolux.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134313622.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Nhật Tân"}),

L(1454,"da-nang","ns","Квартира",5800000,45,
  "1-спальная квартира (кухня отдельно), ул. Nguyễn Xiển 94, Ngũ Hành Sơn, рядом Minh Mạng/Lê Văn Hiến/больница/море — принимают чистых кошек/собак.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134313527.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Nhật Tân"}),

L(1455,"da-nang","ns","Студия",9500000,40,
  "Новая меблированная студия на 5 этаже с балконом и ТВ, ул. Thủy Sơn 4, кв. P501, Ngũ Hành Sơn — въезд с 30 августа.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134319928.htm","сегодня",0,source="chotot",
  details={"contact":"Huy ho"}),

L(1456,"da-nang","ns","Дом",35000000,102,
  "Меблированный дом (3 этажа, 3 спальни/2 с/у) на ул. Khuê Mỹ Đông, Ngũ Hành Sơn — без животных, не сдаётся гражданам Китая.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134323198.htm","сегодня",0,source="chotot",
  details={"contact":"MR HUY"}),

L(1457,"da-nang","ns","Дом",25000000,78,
  "Меблированный дом (2 этажа, 4 спальни/3 с/у) на ул. Mỹ Đa Đông 8, Ngũ Hành Sơn, рядом рынок Bắc Mỹ An.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134323068.htm","сегодня",0,source="chotot",
  details={"contact":"MR HUY"}),

L(1458,"da-nang","ns","Дом",25000000,90,
  "Дом (3 этажа, 3 спальни/3 с/у) с полной меблировкой, пер. Đa Phước 2 (фасад Nam Việt Á), Ngũ Hành Sơn — принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322934.htm","сегодня",0,source="chotot",
  details={"contact":"Anh Nữ"}),

L(1459,"da-nang","ns","Дом",7500000,60,
  "Дом целиком (1 спальня) в тихом переулке для авто, ул. Chế Lan Viên, Ngũ Hành Sơn — 5 мин пешком до пляжа Mỹ Khê.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322459.htm","сегодня",0,source="chotot",
  details={"contact":"Bích Tuyền"}),

L(1460,"da-nang","ns","Дом",70000000,275,
  "Вилла (5 спален/6 с/у) с бассейном, большой двор, ул. Đặng Đoàn Bằng (Sơn Thuỷ), Ngũ Hành Sơn, рядом Minh Mạng.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322244.htm","сегодня",0,source="chotot",
  details={"contact":"MR HUY"}),

L(1461,"da-nang","ns","Дом",250000000,380,
  "Здание (5 этажей, 17 юнитов: 8 квартир + 9 номеров) с бассейном и лифтом, 150 м до пляжа Mỹ Khê, Ngũ Hành Sơn.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322142.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"MR HUY"}),

L(1462,"da-nang","ns","Дом",100000000,100,
  "Вилла (3 этажа, 5 спален) с бассейном, сауной, джакузи, р-н An Thượng, Ngũ Hành Sơn — новая меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322036.htm","сегодня",0,source="chotot",
  details={"contact":"MR HUY"}),

L(1463,"da-nang","ns","Дом",100000000,100,
  "Здание (6 этажей, 8 юнитов) с лифтом и пожарной сигнализацией, р-н Mỹ An, Ngũ Hành Sơn, рядом ул. Chương Dương.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134321793.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"MR HUY"}),

L(1464,"da-nang","ns","Дом",19000000,100,
  "Дом (2 этажа, 2 спальни/2 с/у) с полной меблировкой, р-н Khu FPT (Hoà Hải), Ngũ Hành Sơn — свободен с 3 сентября.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134321692.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng na"}),

L(1465,"da-nang","ns","Дом",22000000,80,
  "Дом (3 этажа, 5 спален/3 с/у + помещение под бизнес) на ул. Ngũ Hành Sơn, рядом университет Kinh tế Đà Nẵng.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/133957612.htm","сегодня",0,source="chotot",
  details={"contact":"Hiền Nguyễn"}),

L(1466,"da-nang","ns","Дом",120000000,300,
  "Вилла (5 спален/6 с/у) с большим бассейном и садом, ул. Chế Lan Viên, Ngũ Hành Sơn — 500 м до Phố Tây An Thượng.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134287364.htm","2 дня назад",2,source="chotot",
  details={"contact":"NGUYỄN NGỌC SƠN"}),

L(1467,"da-nang","ns","Квартира",11000000,68,
  "2-спальная/2 с/у квартира в ЖК FPT Plaza 2, Ngũ Hành Sơn — полная меблировка, стирально-сушильная машина, бассейн, рядом супермаркет, принимают иностранцев.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-fpt-plaza-2-phuong-ngu-hanh-son-tp-da-nang/chinh-chu-cho-2pn-gia-11-tr-o-ngay-nhan-khach-nuoc-ngoai-pr45753847","3 дня назад",3,source="batdongsan",
  details={"notice":"фото объявления датированы 18 мая 2026 — есть риск, что объявление неактуально/висит давно, стоит проверить при обращении"}),

L(1468,"da-nang","ns","Квартира",15000000,45,
  "Меблированная мини-квартира (стиральная/сушильная машина, кондиционер) на ул. Nguyễn Văn Thoại, Ngũ Hành Sơn, рядом пляж Mỹ Khê, река Hàn, Vincom.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-nguyen-van-thoai-phuong-ngu-hanh-son-tp-da-nang/cho-nhanh-full-noi-that-ay-u-may-giat-say-ieu-hoa-dien-tich-rong-pr46059746","3 дня назад",3,source="batdongsan",
  details={"notice":"фото объявления от 17 июля 2026 — тоже риск неактуальности","contact":"Tấn Sự"}),

L(1469,"da-nang","st","Студия",10000000,37,
  "Студия на высоком этаже гостиничного стандарта в ЖК Golden Bay, ул. 01 Lê Văn Duyệt, Sơn Trà — бассейн, спортзал, минимаркет в здании.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/127786776.htm","сегодня",0,source="chotot",
  details={"contact":"hồ ngọc minh"}),

L(1470,"da-nang","st","Квартира",16000000,76,
  "2-спальная квартира с видом на море, полная меблировка, дом Sơn Trà Ocean View (ул. Ngô Quyền 95), Sơn Trà.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134320825.htm","сегодня",0,source="chotot",
  details={"contact":"MAI CHI LAND"}),

L(1471,"da-nang","st","Квартира",14000000,76,
  "Квартира в том же доме Sơn Trà Ocean View (ул. Ngô Quyền 95), Sơn Trà — другой этаж/юнит.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134319761.htm","сегодня",0,source="chotot",
  details={"contact":"MAI CHI LAND"}),

L(1472,"da-nang","st","Дом",25000000,110,
  "Дом (2 спальни/1 с/у) с двором перед домом, ул. Trương Định (р-н Mân Thái), Sơn Trà, рядом пляж.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134314963.htm","сегодня",0,source="chotot",
  details={"contact":"Phạm Cát"}),

L(1473,"da-nang","st","Дом",30000000,100,
  "Дом (3 этажа, 5 спален, санузел в каждой) с новой противопожарной системой, подходит под хостел/homestay, принимают иностранцев (ул. Chu Huy Mân, Mân Thái, Sơn Trà).",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134322982.htm","сегодня",0,source="chotot",
  details={"contact":"Phạm Cát"}),

L(1474,"da-nang","st","Дом",35000000,360,
  "Дом (участок 180м², 2 этажа, 3 спальни/3 с/у) с премиум-меблировкой, ул. Trần Sâm, Sơn Trà, рядом залив Đà Nẵng и мост Thuận Phước — принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134321706.htm","сегодня",0,source="chotot",
  details={"contact":"Nga Lê"}),

L(1475,"da-nang","tk","Квартира",15000000,117,
  "Просторная 3-спальная квартира на высоком этаже, ЖК Hoàng Anh Gia Lai (ул. Hàm Nghi 72), Thanh Khê, рядом аэропорт и центр.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134322160.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Tuấn"}),

L(1476,"da-nang","tk","Дом",160000000,148,
  "Здание (9 этажей, 48 квартир) с видом на море, ул. Nguyễn Tất Thành, Thanh Khê.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134323123.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"Mr AN"}),

L(1477,"da-nang","tk","Дом",27000000,150,
  "Дом (3 этажа, 65м²/этаж, 3 спальни/4 с/у) с премиум-меблировкой, пер. Huỳnh Ngọc Huệ, Thanh Khê, 2 км до аэропорта — принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134322046.htm","сегодня",0,source="chotot",
  details={"contact":"Trung BĐS Dòng Tiền Đà Nẵng"}),

L(1478,"da-nang","tk","Дом",35000000,78,
  "Мини-вилла (3 этажа, 3 спальни/3 с/у) с крытым бассейном, отдельный кабинет, балкон 360°, угловой участок, 100 м до моря, ул. Yên Khê 2, Thanh Khê.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134288699.htm","2 дня назад",2,source="chotot",
  details={"contact":"Được Phan"}),

L(1479,"da-nang","tk","Квартира",None,94,
  "2-спальная квартира ЖК HAGL Lake View Residence (ул. Hàm Nghi 72), Thanh Khê — бассейн, спортзал, детская площадка, рядом ТЦ GO!, адм. центр, мост Rồng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-hoang-anh-gia-lai-lake-view-residence-phuong-thanh-khe-tp-da-nang/cho-dt-93-8m-4-mat-tien-ngay-trung-tam-a-nang-pr46203271","2 дня назад",2,source="batdongsan",
  details={"notice":"цена по запросу — цифры нет ни на карточке («Giá thỏa thuận»), ни в тексте","contact":"Ms Dung"}),

L(1480,"da-nang","hk","Дом",18000000,100,
  "Дом (3 этажа, 4 спальни/4 с/у) с полной меблировкой, ул. Tú Quỳ (р-н Hòa Minh), Hòa Khánh, фасад 7,5 м — приоритет семьям/компаниям.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-tu-quy-phuong-hoa-khanh-tp-da-nang/cho-3-tang-full-noi-that-18-trieu-1-thang-pr46219445","сегодня",0,source="batdongsan",
  details={"contact":"Xuân Cảm"}),

L(1481,"da-nang","hcg","Дом",150000000,200,
  "Угловой дом (5 этажей, 15 квартир) с 2 фасадами, рядом Lotte Mart и река Hàn, ул. Thăng Long, Hòa Cường.",
  "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134322392.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"Mr Zco"}),

L(1482,"da-nang","hcg","Дом",30000000,78,
  "Сквозной дом (4,5×17м, 3 этажа) на торговой ул. Lê Duẩn, Hòa Cường.",
  "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134321079.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Đức Lộc"}),

L(1483,"da-nang","hcg","Квартира",6500000,25,
  "1-спальная квартира на ул. Lưu Quý Kỳ, Hòa Cường (рядом Helio/Sunwheel) — максимум 1-2 человека, животные и иностранцы не принимаются.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/133168205.htm","вчера",1,source="chotot",
  details={"contact":"Thuỷ DT"}),

L(1484,"da-nang","hcg","Квартира",6000000,40,
  "1-спальная квартира с современной техникой (смарт-ТВ, холодильник, индукционная плита), ул. Núi Thành 187, Hòa Cường.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-nui-thanh-phuong-hoa-cuong-tp-da-nang/cho-187-quan-hai-chau-a-gia-chi-6-tr-thang-lh-pr46107388","3 дня назад",3,source="batdongsan",
  details={"notice":"⚠ фото объявления датированы 22.10.2018 — сильное подозрение на просроченное/неактуальное объявление, проверить перед контактом","contact":"Võ Văn Hoàng"}),

L(1485,"da-nang","hcg","Квартира",25000000,76,
  "Угловая 2-спальная квартира на 10 этаже ЖК The Vista Residence (ул. Xô Viết Nghệ Tĩnh 40A), Hòa Cường — вид на фейерверк/реку Hàn/мост Rồng, рядом больница Vinmec, университеты.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-vista-residence-da-nang-phuong-hoa-cuong-tp-da-nang/cho-goc-2pn-a-view-toa-tang-10-dt-76m2-view-phao-song-han-downtown-pr46219360","сегодня",0,source="batdongsan",
  details={"notice":"точная цена встретилась только на карточке поиска, не в тексте объявления — рекомендуется уточнить"}),

L(1486,"da-nang","hc","Квартира",22000000,70,
  "2-спальная квартира в ЖК Sam Towers (ул. Như Nguyệt), Hải Châu — полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134321769.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng Trưởng"}),

L(1487,"da-nang","hc","Квартира",25000000,131,
  "3-спальная квартира в ЖК Đà Nẵng Plaza (Thạch Thang), Hải Châu — вид на реку Hàn, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/133251940.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Thị Lanh"}),

L(1488,"da-nang","hc","Квартира",8000000,40,
  "1-спальная квартира в 10-этажном доме на ул. Nguyễn Thị Minh Khai 142, Hải Châu — охрана 24/7, приём почты на ресепшн.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134291462.htm","вчера",1,source="chotot",
  details={"contact":"Văn Hiệu Nguyễn"}),

L(1489,"nha-trang","lt","Студия",17000000,45,
  "Студия Mường Thanh Luxury, 60 Trần Phú, Lộc Thọ — рядом с центральной площадью, полностью меблирована, залог 2 месяца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134322776.htm","сегодня",0,source="chotot",
  details={"contact":"Văn Hoà","photos":["https://cdn.chotot.com/bYIPSYH7E1JCo6C9_F2wZGjy3jaHoaFLp_zANhf40TM/preset:view/plain/30bc6020f4b262b64be0ec5a9b2526a1-2999000449694634975.jpg"]}),

L(1490,"nha-trang","vp","Квартира",20000000,72,
  "2-спальная угловая квартира с балконом, ул. Phạm Văn Đồng, Vĩnh Phước — премиальная мебель, управление 700 тыс/мес, wifi 275 тыс.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134313119.htm","сегодня",0,source="chotot",
  details={"contact":"Runa Vu","photos":["https://cdn.chotot.com/Kw3MrWsBVQkzCleUkyjZjKNBI9QVNlsuHOyE_mibhlU/preset:view/plain/e33c87efb38153b287c738a45d92b477-2998900976936962956.jpg"],"alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-muong-thanh-vien-trieu-phuong-bac-nha-trang-tinh-khanh-hoa/2-phong-ngu-2-toilet-co-ban-cong-goc-thoang-cung-noi-that-cao-cap-pr46217898"}]}),

L(1491,"nha-trang","vt2","Квартира",14000000,68,
  "2-спальная квартира Mường Thanh Khánh Hòa у моста Trần Phú (старый район Xương Huân), Vạn Thạnh — управление и проживание 700 тыс.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134319931.htm","сегодня",0,source="chotot",
  details={"contact":"Văn Hoà","photos":["https://cdn.chotot.com/Qb3tojOm9pnWytfyQAaBrkV6U4E1e6v_aODfgILnsbA/preset:view/plain/d65224358a330be90cf631b103073343-2998990481354597389.jpg"]}),

L(1492,"nha-trang","lt","Студия",5500000,22,
  "Небольшая студия, 132 Hùng Vương, Lộc Thọ — рядом с морем, в районе «Phố Tây», безопасный район.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134298187.htm","вчера",1,source="chotot",
  details={"contact":"Vũ Duy","photos":["https://cdn.chotot.com/6UBlaFBggtDzXIAm0PpjAQJ9_vHWxnRq-vSWznkUKOQ/preset:view/plain/82cf59d689a9717c096ed599999bf6ce-2998911947193928588.jpg"]}),

L(1493,"nha-trang","pl","Квартира",9000000,88,
  "3-спальная квартира, ЖК CCU-01, Phước Long — вид на реку, высокий этаж.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134314646.htm","сегодня",0,source="chotot",
  details={"notice":"без мебели («không nội thất»), депозит 1 платёж×2","contact":"Hà Lương IT","photos":["https://cdn.chotot.com/sSDCb5_refGJ6Da1xh7OcuREHWU2uiTW0JiPrX4RFdw/preset:view/plain/194aa54b88e315f8e295b3a08408b02a-2998914286732674898.jpg"]}),

L(1494,"nha-trang","ps","Квартира",8000000,60,
  "2-спальная квартира CT5, ЖК Vĩnh Điềm Trung (старый район Vĩnh Hiệp), Phương Sài — полностью меблирована, депозит 2×2, контракт на 1 год.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134314620.htm","сегодня",0,source="chotot",
  details={"contact":"Hà Lương IT","photos":["https://cdn.chotot.com/wVilie-7rqHqH5HuZ2oyj0Zi6s8B55omeV_NKKAuctE/preset:view/plain/64676d190c9a0ec9f49f9e543b4c7ce1-2998914026342274582.jpg"]}),

L(1495,"nha-trang","lt","Студия",21000000,68,
  "Люкс-студия 5*, The Costa Nha Trang, 32-34 Trần Phú, Lộc Thọ — King-кровать, бассейн-инфинити, спортзал, частный пляж, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133495451.htm","сегодня",0,source="chotot",
  details={"contact":"Runa Vu","photos":["https://cdn.chotot.com/E-OtjHsqeDoIt3hq2iZJLHzpaUa8QMWtkHqlpMICe5M/preset:view/plain/10a032b7f1fa482732ebaf3214306838-2992715781090394167.jpg"],"alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-the-costa-nha-trang-phuong-nha-trang-tinh-khanh-hoa/cho-cc-30-trieu-vnd-68-m2-gia-sieu-hoi-uy-tin-pr46040104"}]}),

L(1496,"nha-trang","vp","Квартира",24000000,75,
  "2-спальная квартира с видом прямо на море (Hòn Chồng), ул. Phạm Văn Đồng, Vĩnh Phước — высокий этаж, депозит 2×1.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134313247.htm","сегодня",0,source="chotot",
  details={"contact":"Runa Vu","photos":["https://cdn.chotot.com/nNlTgBjBgbWV0naQyih1x4F4lQaPMd6JP8LPEOeu1CA/preset:view/plain/b2472b9c5dd6b5db9998a5ef343fd254-2998901700360636242.jpg"],"alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-muong-thanh-vien-trieu-phuong-bac-nha-trang-tinh-khanh-hoa/2-phong-ngu-2-toilet-view-truc-dien-bien-co-ban-cong-tang-cao-cuc-chill-pr46217907"}]}),

L(1497,"nha-trang","pl","Квартира",14000000,67,
  "2-спальная квартира CCU-01, Phước Long — новая мебель «как новая», высокий этаж, балкон.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134283852.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phan Thị Lan","photos":["https://cdn.chotot.com/bRXnkLQ-PM429s8u_m5GV4eJEtx6bW_qbIsg2KTPZ4s/preset:view/plain/43ed694f6ad24376fc9d38f9161031e2-2998680383627237643.jpg"],"alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-chung-cu-ccu-01-phuoc-long-phuong-nam-nha-trang-tinh-khanh-hoa/cho-full-noi-that-moi-pr46216867"},{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-khu-do-thi-moi-phuoc-long-phuong-nam-nha-trang-tinh-khanh-hoa/cho-ccu01-hud-pl-dt-67m2-2pn-2wc-full-nt-gia-14tr-thg-lh-thanh-pr46213594"}]}),

L(1498,"nha-trang","vt","Дом",45000000,130,
  "Дом (6 спален/6 с/у), КГТ Mỹ Gia (пакет 5), ул. Phùng Hưng (старый район Vĩnh Thái), Vĩnh Trường — 3 этажа, полная качественная мебель.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134314524.htm","сегодня",0,source="chotot",
  details={"contact":"Hà Lương IT","photos":["https://cdn.chotot.com/urtb7uvaGw4IKy1-m0n3Cc2qQ77KFGBZI-ICzHkhqEE/preset:view/plain/c3ac2843bfcb99b24d83e0299789a6cf-2998913470869818252.jpg"]}),

L(1499,"nha-trang","pl","Дом",8000000,200,
  "Дом целиком, фасад ул. Nguyễn Tất Thành, Phước Long — в 200 м от круговой Lê Hồng Phong, 1 этаж+мансарда (5×20м, 100м²/этаж), 3 спальни, 2 с/у, световой колодец, безопасный район без затоплений.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134305793.htm","вчера",1,source="chotot",
  details={"contact":"Phuong","photos":["https://cdn.chotot.com/OF2z67CAmaofmyJ4pOXJ36fN3ZoxrHzAvoQd0YRHqso/preset:view/plain/728183d849b164ab923d347886918a88-2998858850089651084.jpg"]}),

L(1500,"nha-trang","vt","Дом",26000000,100,
  "Дом (3 спальни), КГТ Mỹ Gia (пакет 7), ул. Phùng Hưng, напротив футбольного поля — 3 этажа, полная мебель, свободный первый этаж.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134291250.htm","вчера",1,source="chotot",
  details={"contact":"Phan Thị Lan","photos":["https://cdn.chotot.com/3jtGEHTlMOnrF5bBMkZXqoxmzy0oQ-_d3em5Tv14fnc/preset:view/plain/0b406069d8c8b910c7d612a30f378cc4-2998723603996299106.jpg"]}),

L(1501,"nha-trang","pl","Дом",18000000,173,
  "Дом-фасад ул. Bửu Đoá, Phước Long (6,5×26,6 м), у рынка Bửu Đoá — разрешён свободный бизнес, депозит 2×3.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134280252.htm","2 дня назад",2,source="chotot",
  details={"contact":"Hà Văn Trạch","photos":["https://cdn.chotot.com/aRSXTawenRUKR1wAHQNWt1sAwbhaIznXA1TnsyEw7hU/preset:view/plain/f76d33f3347fe07137fdcba0ad5a8404-2998614614026537046.jpg"]}),

L(1502,"nha-trang","vt","Дом",18000000,200,
  "Вилла (гостиная+3 спальни+4 с/у), КГТ Mỹ Gia (пакет 2), ул. Phùng Hưng, напротив парка — фасад 10 м, 1 этаж+2 уровня, базовая мебель.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134276763.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phan Thị Lan","photos":["https://cdn.chotot.com/2d2WwbqcHqyedYhTw1RciHlUyhCdPvKwWKHtDp7IPdk/preset:view/plain/9cbc588bdd274bb464f7cb71c4144ef1-2998769803284918681.jpg"]}),

L(1503,"nha-trang","vt","Дом",25000000,100,
  "Дом (3 спальни/4 с/у), КГТ Mỹ Gia (пакет 8) / The Capella, ул. Võ Nguyên Giáp (18 м, широкий тротуар) — полная мебель, умное электричество, кондиционер в потолке, бассейн, охрана 24/7.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134276554.htm","2 дня назад",2,source="chotot",
  details={"notice":"в структурном поле площадки указан старый район Vĩnh Hiệp, но текст и проект (Mỹ Gia) явно указывают на Vĩnh Thái — район определён по тексту","contact":"Phan Thị Lan","photos":["https://cdn.chotot.com/O5QRVpywlp8WA00yo3SwfVCQaPZwyoNbL0o7sPPtdps/preset:view/plain/2fe7b4626f31406e840e72b4f940a7a2-2998595039860087923.jpg"]}),

L(1504,"nha-trang","ph","Дом",45000000,450,
  "Коммерческий дом (4 этажа с лифтом), ул. Thích Quảng Đức, Phước Hải — участок 126м², 2 комнаты на этаже со своим с/у, кондиционеры, пожарная сигнализация, тротуар 3 м.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134275397.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nguyễn Trần Duy Phước","photos":["https://cdn.chotot.com/8PTNPsVnAXuvEugFhZt5gHWph362RTAfKa0djKlLPzk/preset:view/plain/987e06e08220be96b7660fe044dc8566-2998590684166048652.jpg"]}),

L(1505,"nha-trang","vt","Дом",18000000,120,
  "Новый хоумстей (2 спальни), ул. Phong Châu, район Vĩnh Thái (запад), рядом с проектом Sun Group — участок 70м², антресоль, ориентация север.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134274673.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phương GoHome","photos":["https://cdn.chotot.com/892d_hsu7fT9j86Sdf7BHPy0cgfwkvXPlEqjiyb4r5A/preset:view/plain/e6d7197a1aaa5e2371cc69f0d5c2f221-2998588565536394124.jpg"]}),

L(1506,"nha-trang","lt","Квартира",300000000,362,
  "VIP-квартира (4 спальни/4 с/у) на 17 этаже, The Costa Nha Trang, вид на восток — консьерж 24/7, уборка, частный пляж-клуб, спортзал, бассейн.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-the-costa-nha-trang-phuong-nha-trang-tinh-khanh-hoa/cho-vip-4-phong-ngu-trang-pr46218257","сегодня",0,source="batdongsan",
  details={"notice":"⚠ очень высокая цена — люкс-пентхаус, стоит перепроверить актуальность при обращении","contact":"Lê Hữu Khánh"}),

L(1507,"nha-trang","vp","Квартира",None,83,
  "2-спальная квартира, ЖК Scenia Bay, Vĩnh Phước (Bắc Nha Trang) — бассейн-инфинити, сад, детская комната; агент сдаёт несколько типов юнитов.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-scenia-bay-nha-trang-phuong-bac-nha-trang-tinh-khanh-hoa/chuyen-cho-va-van-hanh-gom-studio-1pn-1pn-2pn-2pn-pr46217862","вчера",1,source="batdongsan",
  details={"notice":"цена по запросу","contact":"Nguyễn Thị Hồng"}),

L(1508,"nha-trang","vp","Квартира",None,45,
  "1-спальная квартира, Scenia Bay, 25-26 Phạm Văn Đồng, Vĩnh Phước — свободна с 3 сентября, бассейн-инфинити на 31 этаже, детская комната.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-scenia-bay-nha-trang-phuong-bac-nha-trang-tinh-khanh-hoa/cho-1pn-ay-u-noi-that-1-bedroom-for-rent-pr46217796","вчера",1,source="batdongsan",
  details={"notice":"цена по запросу","contact":"Nguyễn Thị Hồng"}),

L(1509,"nha-trang","vp","Квартира",14000000,94,
  "2-спальная квартира, ЖК Sông Đà Nha Trang, Vĩnh Phước — полная мебель, рядом рынок/школа/супермаркет.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-bai-duong-phuong-bac-nha-trang-tinh-khanh-hoa/cho-song-a-uong-cach-bien-hon-chong-100m-pr46216577","вчера",1,source="batdongsan",
  details={"notice":"точная улица в объявлении не указана, район определён приблизительно по кластеру похожих Bắc Nha Trang объявлений — стоит уточнить"}),

L(1510,"nha-trang","vp","Квартира",9500000,70,
  "2-спальная квартира, Mường Thanh Viễn Triều, район Hòn Chồng, ул. Phạm Văn Đồng, Vĩnh Phước — полная мебель, лифт, охрана, парковка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-muong-thanh-vien-trieu-phuong-bac-nha-trang-tinh-khanh-hoa/cho-gia-chi-tu-9-thang-2-pn-2wc-uc-pr46216424","вчера",1,source="batdongsan",
  details={}),

L(1511,"nha-trang","pl","Квартира",11000000,67,
  "2-спальная квартира CCU-01, Phước Long — новая, полная мебель, балкон юго-восток.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-chung-cu-ccu-01-phuoc-long-phuong-nam-nha-trang-tinh-khanh-hoa/cho-2-pn-2vs-full-noi-that-gia-11-trieu-thang-pr46214858","2 дня назад",2,source="batdongsan",
  details={"contact":"Nguyễn Minh Sâm"}),

L(1512,"nha-trang","lt","Дом",30000000,221,
  "Дом под бизнес с двором, ул. Nguyễn Thiện Thuật, Lộc Thọ (переулок квартала «Phố Tây», фасад 6,6 м) — 1 этаж: двор+открытая площадка+3 спальни+кухня+4 с/у, без мебели, контракт до 5 лет.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-nguyen-thien-thuat-phuong-nha-trang-tinh-khanh-hoa/cho-o-kinh-doanh-san-vuon-221m2-ngang-6-6m-hem-khu-tay-pr46214598","2 дня назад",2,source="batdongsan",
  details={"contact":"Phương Gohome"}),

L(1513,"nha-trang","vt","Дом",20000000,100,
  "Дом (4 спальни/3 с/у), КГТ Mỹ Gia (пакет 3), Vĩnh Thái — 5×20 м, 3 этажа, базовая мебель (кондиционер+кухня); полная меблировка доступна за 22 млн.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-khu-do-thi-my-gia-phuong-nam-nha-trang-tinh-khanh-hoa/cho-4-phong-ngu-o-goi-3-20-trieu-thang-pr46214556","2 дня назад",2,source="batdongsan",
  details={"contact":"Phương Gohome"}),

L(1514,"nha-trang","vn","Дом",140000000,100,
  "Целое здание из 18 комнат (6 этажей + подвал), ул. Tô Hiếu, Vĩnh Nguyên — каждая комната 25-30м² с полной мебелью (кровать, ТВ, холодильник, стиральная/сушильная машина, своя кухня и водонагреватель).",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-to-hieu-phuong-nha-trang-tinh-khanh-hoa/cho-toa-can-ho-18-phong-moi-xay-sieu-ep-co-thang-may-pccc-ay-u-pr46214523","2 дня назад",2,source="batdongsan",
  details={"notice":"сдаётся целое здание, не отдельная комната — цена указана за весь объект","contact":"Phương Gohome"}),

L(1515,"nha-trang","vp","Дом",30000000,154,
  "Новый дом целиком (4 спальни/2 с/у/2 гостиных/2 кухни), Vĩnh Phước, фасад 5 м — у центра/рынка/школы, полная новая мебель.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ngo-den-phuong-bac-nha-trang-tinh-khanh-hoa/moi-xay-full-noi-that-4-phong-ngu-co-san-phia-trang-pr46211264","3 дня назад",3,source="batdongsan",
  details={"contact":"Phương Gohome"}),

L(1516,"nha-trang","ps","Дом",12000000,279.5,
  "Дом с садом, ул. Vĩnh Châu (старый район Vĩnh Hiệp), Phương Sài — рядом ресторан Hoàng Lan/дамба, 200 м от ул. 23/10, сад с прудом с рыбками, 2 этажа, 2 спальни/2 с/у, комната для алтаря, терраса, базовая мебель.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-vinh-chau-phuong-tay-nha-trang-tinh-khanh-hoa/cho-hiep-gan-hang-hoang-lan-ap-nuoc-pr46210704","3 дня назад",3,source="batdongsan",
  details={"contact":"Hồ Quang Minh"}),

L(1517,"nha-trang","vp","Дом",7500000,64,
  "Дом (1 этаж+2 уровня), район Hòn Sện, рядом с ул. Phạm Văn Đồng и морем — 3 спальни/2 с/у, аккуратный, много света.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-bac-nha-trang-tinh-khanh-hoa/cho-hon-sen-1-tret-2-lau-noi-that-ep-gia-7-5-trieu-pr46208909","3 дня назад",3,source="batdongsan",
  details={"notice":"точный район приблизительный (в объявлении нет старого названия района) — стоит уточнить"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content

new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
assert new_content != content
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", NEW_SRC.count("L("), "listings")
