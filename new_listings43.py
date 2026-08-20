# -*- coding: utf-8 -*-
# Ежедневная проверка ДАНАНГА (только этот город из 7 "остальных") — 20 авг 2026 — 44 новых
# объявления (ID 1002-1045), все Chợ Tốt.
#
# ИСТОЧНИК: Chợ Tốt gateway API, region_v2=3017 (весь город), категории 1010 (căn hộ) и 1020
# (nhà ở), offset 0/20 каждая — 80 уникальных объявлений сырых. Категория 1060 (phòng trọ)
# сегодня вернула 0 объявлений по городу — как и в прошлых прогонах, похоже на временный сбой
# источника, не ошибка запроса.
#
# ДЕДУП: из 80 сырых 8 оказались буквальными URL-дублями уже существующих записей (проверено
# grep по list_id в rebuild_final.py) — все 8 добавлены вчерашним прогоном (commit с ID 902-920).
# Из оставшихся 72 запрошена детальная страница ad-listing/<id> каждого (кроме одного явного
# физического дубля 134216364 — тот же ЖК Mường Thanh Luxury/этаж/площадь/цена, что и уже
# принятый вчера 134184287, пропущен без детального запроса).
#
# ЧЕСТНЫЙ daysAgo (ловушка "đẩy tin"): для каждого объявления сравнены list_time и orig_list_time
# из детального ответа API. Подтверждён паттерн из прошлых прогонов: когда orig_list_time
# ОТСУТСТВУЕТ в ответе — объявление НИ РАЗУ не перевыкладывалось, list_time и есть настоящая дата
# (все такие в этом прогоне оказались свежими, 0-6.5 часов назад). Когда orig_list_time
# ПРИСУТСТВУЕТ — это перевыкладка, и он всегда оказывается СТАРШЕ list_time на существенный
# отрезок (от 0.24 до 15 дней в найденных случаях) — такие объявления взяты по orig_list_time,
# и почти все с задержкой >1 дня отклонены как несвежие (18 штук: 133966072, 132783002,
# 134003422, 134162288, 133840490, 134238152, 134094046, 134227770, 134175114, 133687396,
# 133429715, 134214458, 134226329, 134170378, 133276505, 133821430, 134174325, 134229534).
# Два объявления с orig_list_time, но малой задержкой (134253015: 0.28 дня, 134246817: 0.45 дня)
# оставлены как действительно свежие.
#
# ФИЛЬТР ПО ТИПУ ОБЪЯВЛЕНИЯ (CRITICAL RULES — не фабриковать, не публиковать явно коммерческие
# объекты вместо жилья): отклонены как преимущественно коммерческие/не подходящие под формат
# проекта: 134259622 (135 млн ₫/мес, кафе/ресторан на углу — "phù hợp kinh doanh nhà hàng"),
# 134256873 (50 млн ₫/мес вилла, явно позиционируется под кафе/ресторан "thích hợp mở cafe sân
# vườn, nhà hàng"), 134255372 (300 млн ₫/мес "cho thuê mặt bằng" — чисто коммерческая площадь),
# 134255126 (110 млн ₫/мес — сдача целого здания на 10 квартир + торговая площадь, не единичный
# юнит), 134254921 (160 млн ₫/мес — сдача целой гостиницы-апартаментов на 48 номеров). Также
# отклонён 134258924 (Тạ Mỹ Duật, 3PN/2WC, 26 млн ₫) как вероятный дубль-перевыкладка того же
# физического дома другим агентом почти сразу после принятого 134260965 (тот же адрес/цена/
# планировка, отличие только в площади 90 vs 100 м² — похоже на опечатку, а не другой объект).
# Также отклонён минимально информативный 134254623 (только "2pn 1wc, ~50m2, цена по звонку" без
# уточнения дома/улицы сверх "Minh Mạng") — недостаточно конкретики для уверенной верификации.
#
# ЦЕНОВЫЕ РАСХОЖДЕНИЯ (честно отмечены в details.notice ниже, а не проигнорированы):
# 134258586 и 134257990 — Chợ Tốt указывает диапазон цены по этажам, использована нижняя граница
# (структурное поле price совпадает с нижней границей). 134253562 — поле price (32 млн ₫,
# совпадает с заголовком объявления) расходится с текстом описания (35 млн ₫, похоже на
# скопированный из другого объявления кусок шаблона) — использовано структурное поле/заголовок.
#
# ГЕОГРАФИЯ: ward_name_v3 (новые укрупнённые районы) в Дананге сопоставляется с районами проекта
# практически 1:1 по названию (ns/ah/st/hc/hcg/tk/cl2/hx/hk/lc), кроме одного случая — ЖК The Ori
# Garden числится в ward_name_v3 «Hải Vân», которого нет в списке районов проекта; по прецеденту
# вчерашнего прогона (L907, тот же ЖК) отнесён к ближайшему — lc (Liên Chiểu).
#
# BATDONGSAN: `nha-dat-cho-thue-tp-da-nang` — 403 при первой попытке и повторно после паузы с
# более полными заголовками (Accept-Language/Referer) — источник недоступен в этом прогоне.
# FACEBOOK: не проверялся — ожидаемо недоступен в этом headless-окружении (login wall/400),
# время не тратилось согласно инструкции промпт-файла.
NEW_SRC = r'''
L(1002,"da-nang","ah","Дом",26000000,100,
  "Дом целиком (3 спальни, 2 с/у) на ул. Tạ Mỹ Duật, квартал Khu Phố Hàn, An Hải. Чистый, подходит для семьи или группы.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134260965.htm","сегодня",0,source="chotot",
  details={"contact":"Nhựt Lê"}),

L(1003,"da-nang","ns","Квартира",7500000,45,
  "Дуплекс-квартира (1 спальня, 1 с/у) на ул. Lê Văn Hiến. Собственный сад на первом этаже (корпус B), своя стиральная машина, фильтр для воды, животные разрешены.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134260771.htm","сегодня",0,source="chotot",
  details={"contact":"Huy ho"}),

L(1004,"da-nang","ah","Дом",25000000,70,
  "Дом целиком (2 этажа, 3 спальни, 2 с/у), переулок Kiệt 02 Lâm Hoành (от Võ Văn Kiệt вглубь 50 м), P. Phước Mỹ, рядом пляж Mỹ Khê. Полная меблировка, принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134260398.htm","сегодня",0,source="chotot",
  details={"contact":"A Minh"}),

L(1005,"da-nang","ns","Дом",16000000,100,
  "Дом с садом (3 спальни, 3 с/у) фасадом на ул. Nguyễn Đình Chiểu, КДТ Nam Việt Á, P. Khuê Mỹ. Полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134260263.htm","сегодня",0,source="chotot",
  details={"contact":"A Phước"}),

L(1006,"da-nang","ns","Дом",25000000,100,
  "Дом-шопхаус (3 этажа, 4 спальни, 4 с/у) в комплексе Shophouse FPT. Задний двор, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134259736.htm","сегодня",0,source="chotot",
  details={"deposit":"2 месяца (оплата за 3)","contact":"Diep Nguyen"}),

L(1007,"da-nang","ah","Дом",18000000,65,
  "Дом целиком (3 этажа, ширина 6 м, 3 спальни, 2 с/у), Khu An Trung, рядом мост Trần Thị Lý и ЖК Monarchy. Первый этаж свободной планировки — подходит и под офис/шоурум (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/132401067.htm","сегодня",0,source="chotot",
  details={"contact":"Xuân Kỳ"}),

L(1008,"da-nang","ns","Квартира",12000000,50,
  "2-спальная квартира (1 с/у) на ул. Nguyễn Lữ, Khuê Mỹ, КДТ Nam Việt Á, рядом мост Tiên Sơn. Полная меблировка, балкон, своя стиральная машина.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134259223.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","contact":"HAVILAND HOUSE"}),

L(1009,"da-nang","hcg","Студия",11000000,40,
  "Студия (новое строительство, 100%) с балконом на ул. Hoa Sơn 7, рядом ТЦ Lotte, Hải Châu. Своя стиральная и сушильная машина. Доступны этажи 3 и 4, цена по объявлению 11-13 млн ₫ — указана нижняя граница.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134258765.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","notice":"диапазон цены по этажам 11-13 млн ₫ — использована нижняя граница (совпадает со структурным полем цены)","contact":"HAVILAND HOUSE"}),

L(1010,"da-nang","ns","Квартира",10000000,40,
  "1-спальная квартира (в тексте объявления указано 45 м², по данным площадки — 40 м²) с балконом, ул. An Thượng 17, рядом пляж. Этаж 2, можно въезжать сразу, еженедельная уборка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134258787.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","contact":"HAVILAND HOUSE"}),

L(1011,"da-nang","cl2","Дом",15000000,125,
  "Дом целиком (3 этажа, 4 спальни, 3 с/у) фасадом на ул. 48 Nguyễn Nhàn, напротив больницы Cẩm Lệ. Терраса, место для сушки белья.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134258860.htm","сегодня",0,source="chotot",
  details={"deposit":"6 месяцев","contact":"Thái Văn Bình"}),

L(1012,"da-nang","hcg","Студия",7400000,30,
  "Студия (комн. 301) на ул. Nguyễn Văn Linh 302, 5 минут пешком до аэропорта, рядом парк 29/3. Полная меблировка, лифт, бесплатная стирка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134258803.htm","сегодня",0,source="chotot",
  details={"contact":"Quyên Quyên"}),

L(1013,"da-nang","ns","Квартира",10500000,45,
  "1-спальная квартира с балконом на ул. Nguyễn Lữ, Khuê Mỹ. Своя стиральная машина, лифт, еженедельная уборка. Доступны этажи 3-5, цена по объявлению 10,5-12 млн ₫ — указана нижняя граница.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134258633.htm","сегодня",0,source="chotot",
  details={"notice":"диапазон цены по этажам 10,5-12 млн ₫ — использована нижняя граница","contact":"HAVILAND HOUSE ĐÀ NẴNG"}),

L(1014,"da-nang","ns","Студия",10000000,40,
  "Студия на ул. Tôn Thất Thiệp. Своя прачечная, водоочиститель, wifi. Этаж 2 (10 млн ₫, готова сейчас) или этаж 4 (11,5 млн ₫, скоро освободится) — в цене указан этаж 2.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134258586.htm","сегодня",0,source="chotot",
  details={"notice":"два варианта по этажам — использована цена этажа 2 (10 млн ₫)","contact":"HAVILAND HOUSE ĐÀ NẴNG"}),

L(1015,"da-nang","ns","Квартира",7000000,45,
  "1-спальная квартира на ул. Lê Quang Đạo 133, 5 минут пешком до моря. Балкон, своя стиральная машина, лифт, электронный замок. Цена варьируется по этажу (1/3/6) от 7 до 10,5 млн ₫ — указана нижняя граница.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134257990.htm","сегодня",0,source="chotot",
  details={"notice":"диапазон цены по этажам 7-10,5 млн ₫ — использована нижняя граница","contact":"1W05.Lê Phan Cẩm Ly"}),

L(1016,"da-nang","ns","Дом",40000000,100,
  "Дом целиком (4 этажа, 5 спален, 6 с/у, полезная площадь 400 м²) фасадом на ул. Khuê Mỹ Đông 7, рядом ул. Hồ Xuân Hương и пляж Mỹ Khê, район с высокой концентрацией иностранцев. Премиальная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134257545.htm","сегодня",0,source="chotot",
  details={"contact":"A Phong"}),

L(1017,"da-nang","ns","Дом",30000000,125,
  "Дом целиком (3 этажа, 6 спален, 6 с/у) на ул. Đoàn Khuê, КДТ Nam Việt Á. Двор для авто, меблирован, подходит и под офис/для проживания. Для вьетнамцев 30 млн ₫/мес, для иностранцев — 40 млн ₫/мес.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134257509.htm","сегодня",0,source="chotot",
  details={"notice":"цена для иностранных арендаторов выше (40 млн ₫) — указана базовая цена для местных (30 млн ₫)","contact":"Mr.Tú"}),

L(1018,"da-nang","hx","Дом",11000000,100,
  "Дом целиком (3 этажа, 3 спальни, 3 с/у) на ул. Phù Đổng, Hòa Xuân. Полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134257231.htm","сегодня",0,source="chotot",
  details={"contact":"Thuỷ DT"}),

L(1019,"da-nang","ns","Дом",35000000,70,
  "Дом целиком (3 этажа, 4 спальни, 3 с/у), квартал An Thượng, рядом множество удобств. Без мебели, только кондиционеры — подходит и для проживания, и под офис (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134257191.htm","сегодня",0,source="chotot",
  details={"contact":"Mr.Tú"}),

L(1020,"da-nang","ns","Дом",17000000,100,
  "Дом целиком (3 этажа, 4 спальни) фасадом на ул. Tùng Thiện Vương, КДТ Nam Việt Á. Приоритет долгосрочной аренде.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134257141.htm","сегодня",0,source="chotot",
  details={"contact":"Mr.Thắng"}),

L(1021,"da-nang","cl2","Дом",23000000,120,
  "Дом целиком (3 этажа, 4 спальни, 4 с/у) фасадом на ул. Trịnh Đình Thảo, Khuê Trung, рядом ул. Nguyễn Hữu Thọ. Просторный двор для авто, подходит и под офис/учебный центр (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134256971.htm","сегодня",0,source="chotot",
  details={"contact":"BÌNH CAPITAL"}),

L(1022,"da-nang","tk","Квартира",10000000,45,
  "2-спальная квартира (1 с/у) на ул. Phan Thanh, рядом университет Duy Tân. Полная меблировка, лифт, принимают иностранцев, животные не разрешены. Контракт от 6 месяцев.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134256882.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","contact":"Minh Kiệt Haviland"}),

L(1023,"da-nang","ns","Студия",5500000,20,
  "Компактная квартира (20 м²) с балконом на ул. An Thượng 37, рядом университет экономики, рынок Bắc Mỹ An, пляж Mỹ Khê. ТВ, холодильник, кондиционер, кухонная утварь.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134256438.htm","сегодня",0,source="chotot",
  details={"contact":"Hòa"}),

L(1024,"da-nang","ns","Квартира",6300000,40,
  "Квартира (40 м²) с балконом на ул. Chế Lan Viên 08, рядом университет экономики, рынок Bắc Mỹ An, пляж Mỹ Khê. Полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134256378.htm","сегодня",0,source="chotot",
  details={"contact":"Hòa"}),

L(1025,"da-nang","hk","Студия",8500000,40,
  "Студия с просторным балконом на ул. Hòa Phú 30, Hòa Khánh. Своя стиральная и сушильная машина, свободна сейчас.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134256189.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Thanh Kiệt"}),

L(1026,"da-nang","hx","Дом",25000000,100,
  "Дом целиком (3 этажа, сквозной, новое строительство) на ул. 10м5 Lê Quảng Chí, Hòa Xuân. Подходит и для проживания, и под бизнес/офис (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134256080.htm","сегодня",0,source="chotot",
  details={"contact":"mr AN"}),

L(1027,"da-nang","ah","Дом",20000000,66,
  "Дом новой постройки (2 этажа, 2 спальни, 3 с/у) на ул. Tạ Mỹ Duật, рядом пляж Mỹ Khê. 3 кондиционера, стиралка, ТВ, холодильник, водонагреватель. Первый этаж уже оборудован под кафе (барная стойка, мебель) — подходит и для совмещённого проживания с бизнесом.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134255960.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Anh Tuyền"}),

L(1028,"da-nang","hx","Дом",12000000,100,
  "Дом целиком (2 этажа, 3 спальни) на ул. Hoàng Hiệp, Hòa Xuân. Двор для авто, базовая меблировка, подходит и под офис (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134255879.htm","сегодня",0,source="chotot",
  details={"contact":"Quyên Lê"}),

L(1029,"da-nang","st","Дом",130000000,300,
  "Вилла премиум-класса (3 этажа, 6 спален, у каждой свой с/у) рядом мостом Thuận Phước, ул. Phan Bá Vành. Бассейн, лифт, karaoke, сауна, терраса для BBQ, элитный закрытый квартал.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134255725.htm","сегодня",0,source="chotot",
  details={"contact":"Ruby Ho (Toan Huy Hoang Realty)"}),

L(1030,"da-nang","hx","Дом",15000000,100,
  "Дом целиком (3 этажа, немного смещённой планировки, 3 спальни, 3 с/у) фасадом на ул. Hoàng Đình Ái, рядом рынок Hòa Xuân. Комната для алтаря, место для сушки белья, двор для авто, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134255706.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Dự"}),

L(1031,"da-nang","ah","Дом",70000000,250,
  "Вилла в комплексе Euro Village 1 (3 этажа, 4 спальни, у каждой свой с/у). Премиальная меблировка, много зелени, охраняемый квартал.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134255692.htm","сегодня",0,source="chotot",
  details={"contact":"Ruby Ho (Toan Huy Hoang Realty)"}),

L(1032,"da-nang","ah","Квартира",50000000,94,
  "1-спальная квартира 94 м² в комплексе Wyndham Soleil Ánh Dương, ~50 м от пляжа Phạm Văn Đồng. Вид на море и гору Sơn Trà, премиальная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134255320.htm","сегодня",0,source="chotot",
  details={"contact":"Chanh Phạm"}),

L(1033,"da-nang","ah","Студия",6500000,35,
  "Студия/1-спальная на ул. Trần Hưng Đạo, P. An Hải Tây, рядом мост Dragon Bridge, ночной рынок Sơn Trà и набережная реки Хан. Полная меблировка, лифт, охраняемая парковка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134255065.htm","сегодня",0,source="chotot",
  details={"contact":"Apartment Đà Nẵng"}),

L(1034,"da-nang","ah","Дом",26000000,76,
  "Дом целиком (3 этажа, 3 спальни, 2 с/у) на ул. Tạ Mỹ Duật, An Hải Bắc, рядом Phạm Văn Đồng. Полная меблировка, рядом пляж.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134255017.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Quân Land"}),

L(1035,"da-nang","ah","Дом",23000000,150,
  "Дом целиком (4 спальни, 3 с/у) в квартале Phúc Lộc Viên, ул. Ngô Quyền.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134254990.htm","сегодня",0,source="chotot",
  details={"contact":"Nhựt Lê"}),

L(1036,"da-nang","st","Квартира",24000000,50,
  "2-спальная квартира на высоком этаже комплекса Golden Bay, вид на реку. Премиальная меблировка, свободна сейчас.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134254924.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц (оплата за 3)","contact":"Nguyễn Công Chinh"}),

L(1037,"da-nang","ah","Дом",30000000,90,
  "Дом в переулке для авто (3 этажа, 5 спален, 3 с/у, полезная площадь 270 м²) на ул. Nguyễn Văn Thoại, рядом пляж Mỹ Khê. Чистый; в объявлении также предлагается под спа/нейл-салон/хостел (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134254920.htm","сегодня",0,source="chotot",
  details={"contact":"Hải (NCC)"}),

L(1038,"da-nang","ns","Дом",25000000,300,
  "Дом с большим садом (2 спальни, 2 с/у) на ул. Bình Kỳ, Hòa Quý, рядом мост Khuê Đông. Пруд с карпами кои, тихий район.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134254862.htm","сегодня",0,source="chotot",
  details={"contact":"Hải"}),

L(1039,"da-nang","st","Квартира",14000000,70,
  "2-спальная квартира (2 с/у) на ул. Mân Quang 9, рядом супермаркет Coopmart Sơn Trà. Бассейн на 1 этаже, терраса с мангалом, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134254820.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Diêm"}),

L(1040,"da-nang","ns","Квартира",20000000,50,
  "2-спальная квартира на ул. Khuê Mỹ Đông 15 (в объявлении также фигурирует Khuê Mỹ Đông 14). Полная меблировка, животные разрешены.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134254543.htm","сегодня",0,source="chotot",
  details={"contact":"Huy ho"}),

L(1041,"da-nang","lc","Квартира",5500000,56,
  "2-спальная квартира (2 с/у) в ЖК The Ori Garden, Hòa Hiệp Nam. Район по ward_name_v3 — «Hải Vân» (не входит в список районов проекта явно, нанесена на ближайший — Liên Chiểu, по прецеденту L907). Цена не включает сервис-сбор. В том же объявлении также предлагается 3-спальная квартира за 7,5 млн ₫ — не добавлена отдельно (нет данных о площади).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/133562284.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц (оплата за 3)","contact":"Hồ sỹ ánh"}),

L(1042,"da-nang","hcg","Квартира",14000000,72,
  "2-спальная квартира (2 с/у) 72 м² на ул. Nguyễn Hữu Thọ, рядом центр и аэропорт. Полная меблировка, животные разрешены, свободна сейчас.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134253638.htm","сегодня",0,source="chotot",
  details={"contact":"Kiều Oanh"}),

L(1043,"da-nang","ns","Квартира",32000000,70,
  "2-спальная квартира (2 с/у) 70 м² в ЖК Panoma, ул. Trần Thị Lý, рядом мост Dragon Bridge и пляж Mỹ Khê. Бассейн, спортзал, ресепшен, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134253562.htm","сегодня",0,source="chotot",
  details={"notice":"структурное поле цены и заголовок объявления указывают 32 млн ₫, но в тексте описания фигурирует 35 млн ₫ (похоже на кусок шаблона от другого юнита) — использована цена из заголовка/структурного поля","contact":"Kiều Oanh"}),

L(1044,"da-nang","ns","Квартира",9000000,45,
  "Квартира на ул. Lê Văn Hưu, Ngũ Hành Sơn. Своя стиральная машина, wifi, лифт, замок по отпечатку пальца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134253015.htm","сегодня",0,source="chotot",
  details={"contact":"Khánh Linh"}),

L(1045,"da-nang","ns","Квартира",9500000,60,
  "2-спальная квартира (2 с/у) 60 м² на ул. Hói Kiểng 27, вид на реку. Полная меблировка, кондиционер, холодильник, свой паркинг для авто — подходит для 3-4 человек.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134246817.htm","сегодня",0,source="chotot",
  details={"contact":"Trường Giang"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted daily check (Da Nang only) 20 aug 2026: 44 listings written (all chotot); "
      "batdongsan blocked (403 twice), facebook not attempted (expected fail)")
