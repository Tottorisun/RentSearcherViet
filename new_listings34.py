# -*- coding: utf-8 -*-
# Ежедневная проверка ОСТАЛЬНЫХ 7 городов (не HCMC) — 19 авг 2026 — 53 новых объявления
# (ID 875-928, минус дубль 877 — см. ниже): Нячанг 13, Далат 13, Дананг 19 (17 Chợ Tốt +
# 2 Batdongsan), Вунгтау 5, Куинён 3.
# Хойан и Фантьет/Муйне — за сегодня СУХО на обоих источниках (все объявления Chợ Tốt старше 5 дней,
# Batdongsan не дал ни одной карточки выше потолка ID) — это ожидаемо, не форсировалось.
#
# ВАЖНАЯ ТЕХНИЧЕСКАЯ ПОПРАВКА (исправлен баг из вчерашнего HCMC-прогона): поле ward_name_v3 в JSON
# гейтвея Chợ Tốt отдаётся в СМЕШАННОЙ юникод-нормализации (NFC/NFD вперемешку). Везде ниже оба
# операнда сравнения (ward_name_v3 и справочные названия районов) пропущены через
# unicodedata.normalize("NFC", ...) перед сравнением — без этого часть совпадений тихо пропадает.
#
# ГЕОГРАФИЯ НЯЧАНГА: у Chợ Tốt ward_name_v3 в Нячанге даёт только 4 УКРУПНЁННЫХ новых района
# (Nha Trang/Bắc/Nam/Tây Nha Trang), тогда как список районов проекта — это 12 СТАРЫХ районов.
# Однозначное сопоставление невозможно по одному ward_name_v3 — использовалось только явное
# упоминание старого района/улицы/комплекса в тексте объявления (Vĩnh Phước, Vĩnh Hải, Vĩnh Hoà→vh
# по прецеденту L23/L64, Phước Hải/Hà Quang→ph по прецеденту L313/L369/L370, Mỹ Gia/Vĩnh Thái→vt
# по прецеденту L318, Vĩnh Điềm Trung/Vĩnh Hiệp→ps по прецеденту L297/L303/L316/L321, Panorama→lt
# по прецеденту L7/L24/L352/L356/L357, ЖК Mường Thanh 04 Trần Phú→lt по прецеденту L322,
# Mường Thanh Viễn Triều→vp по прецеденту L30, Hoàng Quân→vh по прецеденту L300). Кандидаты без
# однозначной привязки (например "трung tâm thành phố" без улицы, KĐT Thái Hưng без старого
# района) НЕ добавлялись, чтобы не рисковать неверным районом.
#
# ДУБЛИКАТЫ: Chợ Tốt 134216364 (Mường Thanh Luxury Đà Nẵng, тот же этаж/площадь/цена/вид, что и
# принятый 134184287) — не добавлен, тот же физический объект от другого агента. Chợ Tốt 134234582
# (Lapaz Tower, тот же адрес/площадь/цена, что и принятый 134235191) — аналогично не добавлен.
#
# BATDONGSAN: потолок ID = 46202495 (зафиксирован сегодняшним HCMC-прогоном, commit 5c12ad7,
# ~15:57) — применён как консервативный (заведомо не старее) порог для всех 7 городов. Проверены
# все URL из промпт-файла (Нячанг/Далат/Дананг/Вунгтау/Куинён/Хойан/Фантьет) — 403 только на
# phuong-xuan-truong-da-lat (снят после одного повтора). Выше потолка нашлось только 2 карточки,
# обе в Дананге (Ngũ Hành Sơn) — цена подтверждена дважды (карточка выдачи + поле "Khoảng giá" на
# странице объявления).
#
# FACEBOOK: не проверялся отдельно в этом прогоне — время потрачено на полное покрытие Chợ Tốt +
# Batdongsan по всем 7 городам (см. ниже общий итог: ~180 объявлений Chợ Tốt разобрано, 52 принято).
#
# ПОПРАВКА К ПРОМПТ-ФАЙЛУ: раздел NHA TRANG подразумевает, что ward_name_v3 будет содержать старые
# 12 названий — на практике Chợ Tốt даёт только 4 укрупнённых новых макрорайона (см. выше), из-за
# чего прямое сопоставление ward_name_v3→district key для Нячанга невозможно без чтения текста
# объявления. Стоит уточнить промпт явно.
NEW_SRC = r'''
L(875,"nha-trang","lt","Студия",14000000,45,
  "Меблированная студия A1402 (вид на город) в комплексе Panorama на набережной Trần Phú. Балкон, есть кухня.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134236286.htm","сегодня",0,source="chotot",
  details={"amenities":"бесплатный бассейн и спортзал (6 этаж)","policy":"животные не принимаются","contact":"Hà Lương IT"}),

L(876,"nha-trang","lt","Квартира",27000000,70,
  "2-спальная квартира (2 с/у) на 12 этаже башни Nam в комплексе Gold Coast, набережная Trần Phú.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134235652.htm","сегодня",0,source="chotot",
  details={"deposit":"2 месяца (оплата за 1)","contact":"Hà Lương IT"}),

# L(877, id=132796382, ЖК Mường Thanh Khánh Hòa) УДАЛЁН после шага 7 (проверка на дубли URL по
# финальному LISTINGS-массиву): тот же URL уже существовал как L(68) (добавлен в далёком прошлом
# батче, район "vt2"/Vạn Thạnh, другое описание "Xương Huân"). Первоначальная проверка на дубли
# перед вставкой (grep по буквальным "nhatot.com/...") пропустила это совпадение, потому что L(68)
# использует конкатенацию N+"/thue-..." — URL без литеральной подстроки "nhatot.com" в самой строке.
# Итоговый список ниже — уже БЕЗ этого дубля (53 объявления вместо изначальных 54).

L(878,"nha-trang","vp","Квартира",10000000,65,
  "2-спальная квартира (2 с/у) в комплексе Mường Thanh Viễn Triều, 03 Phạm Văn Đồng, Vĩnh Phước — напротив пляжа Hòn Chồng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134235623.htm","сегодня",0,source="chotot",
  details={"amenities":"бассейн и спортзал в комплексе, ТЦ на 1 этаже, рядом больница и школа (50 м), рынок Vĩnh Hải (500 м)","notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Nguyễn Tuấn Đại"}),

L(879,"nha-trang","vh","Квартира",9000000,60,
  "2-спальная квартира (2 с/у), этаж 4, башня A1, ЖК Hoàng Quân, Бắc Нячанг. До моря 800 м.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134226591.htm","сегодня",0,source="chotot",
  details={"deposit":"2 месяца (оплата за 1)","contact":"Hà Lương IT"}),

L(880,"nha-trang","vh","Дом",20000000,110,
  "Дом целиком, новый ремонт, район Vĩnh Hoà (старое название, ближайший район проекта — Vĩnh Hải), 1 этаж + мезонин. 3 спальни, 2 с/у.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134215272.htm","вчера",1,source="chotot",
  details={"deposit":"2 месяца (оплата за 2)","electricity":"по гостарифу","water":"по гостарифу","contract":"от 1 года","contact":"Phương GoHome"}),

L(881,"nha-trang","vh","Дом",15000000,100,
  "Дом целиком (угловой участок), район Vĩnh Hải, городской квартал (KĐT), 3 этажа, 4 спальни, 2 с/у, гараж, крыша-терраса. 500 м до рынка Vĩnh Hải.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134187565.htm","2 дня назад",2,source="chotot",
  details={"deposit":"3 месяца (оплата за 3)","electricity":"по гостарифу","water":"по гостарифу","contract":"более 1 года","notice":"общепит не разрешён","contact":"Phương GoHome"}),

L(882,"nha-trang","pl","Квартира",10000000,65,
  "Угловая 2-спальная квартира (2 с/у) с балконом, ЖК CT4 Hud, ул. 28, КДТ Phước Long.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134184961.htm","2 дня назад",2,source="chotot",
  details={"deposit":"2 месяца (оплата за 2)","contact":"Hà Lương IT"}),

L(883,"nha-trang","ph","Квартира",10000000,67,
  "2-спальная квартира (2 с/у) в ЖК CT2 VCN Phước Hải. 3 кондиционера, 2 ТВ, водонагреватель, электроплита, стиралка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134206429.htm","вчера",1,source="chotot",
  details={"notice":"цена не включает сервис-сбор, электричество/воду, wifi и прочие расходы по управлению"}),

L(884,"nha-trang","ph","Дом",22000000,100,
  "Дом целиком, КДТ Hà Quang 1. 1 этаж + 3 надстройки, 4 спальни, 5 с/у, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134208448.htm","вчера",1,source="chotot",
  details={"deposit":"2 месяца (оплата за 1)","contact":"Hà Lương IT"}),

L(885,"nha-trang","vt","Дом",26000000,100,
  "Дом целиком, новое строительство, КДТ Mỹ Gia (старый район — Vĩnh Thái, по прецеденту проекта ближайший район — Vĩnh Trường). 3 этажа + техэтаж, 3 спальни, 4 с/у, двор.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/133827595.htm","вчера",1,source="chotot",
  details={"deposit":"2 месяца (оплата за 2)","electricity":"по гостарифу","water":"по гостарифу","contract":"1-3 года"}),

L(886,"nha-trang","ps","Дом",22000000,102,
  "Дом-магазин (1 этаж свободной планировки под бизнес + 2 этажа жилых комнат), район Vĩnh Hiệp рядом с супермаркетом GO! (район близок к Vĩnh Điềm Trung, по прецеденту проекта — Phương Sài). Терраса на крыше.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134187463.htm","2 дня назад",2,source="chotot",
  details={"deposit":"4 месяца (оплата за 3)","contract":"от 2 лет","notice":"первый этаж пустой под коммерцию, 2-3 этажи — жилые комнаты","contact":"Phương GoHome"}),

L(887,"nha-trang","ph2","Дом",25000000,58,
  "Дом-магазин на оживлённой ул. Nguyễn Thị Minh Khai, район Phước Hòa, рядом с «русским кварталом». 1 этаж + 2 надстройки, первый этаж свободный под бизнес, 4 комнаты, 3 с/у.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134187349.htm","2 дня назад",2,source="chotot",
  details={"deposit":"2 месяца (оплата за 3)","electricity":"по гостарифу","water":"по гостарифу","amenities":"4 кондиционера, 2 водонагревателя","notice":"первый этаж пустой под коммерцию","contact":"Phương GoHome"}),

L(888,"nha-trang","vn","Дом",20000000,100,
  "Дом целиком, квартал Tô Hiệu, ЖК Mipeco, район Vĩnh Nguyên. 4 этажа, 5 спален, 6 с/у. До моря 500 м. Можно заселяться сразу.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134191590.htm","2 дня назад",2,source="chotot",
  details={"deposit":"2 месяца (оплата за 2)","notice":"подходит и для проживания, и под небольшой офис (вторично)","contact":"Hà Văn Trạch"}),

L(889,"da-lat","lv","Квартира",6000000,40,
  "2-спальная квартира (мебель) на ул. Mê Linh, район Lâm Viên (старое — Phường 9), 7 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134187126.htm","2 дня назад",2,source="chotot",
  details={"electricity":"5 000 ₫/кВт·ч","water":"15 000 ₫/м³","deposit":"1 месяц","contract":"от 6 месяцев","contact":"Hương Lê"}),

L(890,"da-lat","lv","Студия",4500000,20,
  "Студия с балконом на ул. Trần Quang Khải, район Lâm Viên (старое — Phường 8), электричество/вода включены.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134186245.htm","2 дня назад",2,source="chotot",
  details={"deposit":"1 месяц","contract":"6-12 месяцев","amenities":"общая стиральная машина, кухня на террасе","contact":"Hương Lê"}),

L(891,"da-lat","xh","Студия",5200000,50,
  "Студия с видом на ул. Ngô Thì Sỹ, район Xuân Hương (старое — Phường 4), 5 мин до рынка Đà Lạt и озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134185628.htm","2 дня назад",2,source="chotot",
  details={"electricity":"2 600 ₫/кВт·ч","water":"16 000 ₫/м³","deposit":"1 месяц","contract":"3-6-12 месяцев","contact":"Hương Lê"}),

L(892,"da-lat","lv","Квартира",9000000,60,
  "1-спальная квартира с балконом на ул. Phan Chu Trinh, район Lâm Viên (старое — Phường 9), полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134181161.htm","3 дня назад",3,source="chotot",
  details={"electricity":"4 000 ₫/кВт·ч","water":"25 000 ₫/м³","deposit":"1 месяц","contract":"6-12 месяцев","contact":"Hương Lê"}),

L(893,"da-lat","cl","Квартира",15000000,60,
  "2-спальная квартира с балконом и видом, район Cam Ly (старое — Phường 6), рядом школа Lam Sơn, 2,5 км до ночного рынка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134181134.htm","3 дня назад",3,source="chotot",
  details={"electricity":"5 000 ₫/кВт·ч","water":"100 000 ₫/чел.","deposit":"1 месяц","contract":"6-12 месяцев","amenities":"кафе и коворкинг на первом/верхнем этаже здания","contact":"Hương Lê"}),

L(894,"da-lat","lv","Студия",5500000,40,
  "Студия на ул. Phan Chu Trinh, район Lâm Viên (старое — Phường 9), полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134181114.htm","3 дня назад",3,source="chotot",
  details={"electricity":"4 000 ₫/кВт·ч","water":"25 000 ₫/м³","deposit":"1 месяц","contract":"6-12 месяцев","contact":"Hương Lê"}),

L(895,"da-lat","cl","Дом",20000000,72,
  "Дом целиком напрямую от собственника, ул. Phan Đình Giót, район Cam Ly, 50 м до рынка. 1 этаж + 3 надстройки, 6 спален (у каждой свой с/у), комната для алтаря. Без мебели.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134232785.htm","сегодня",0,source="chotot",
  details={"deposit":"3 месяца (оплата за 3)","contract":"от 2 лет","contact":"Phạm Tăng Thắng (собственник)"}),

L(896,"da-lat","xh","Дом",12000000,54,
  "Дом целиком на ул. Cổ Loa (д.5), район Xuân Hương. 3 спальни, 3 с/у, гостиная, кухня, базовая меблировка.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134200385.htm","2 дня назад",2,source="chotot",
  details={"contact":"Ngọc Uyên"}),

L(897,"da-lat","xh","Дом",13000000,30,
  "Дом целиком в переулке за пекарней Bon Bon, угол Phan Đình Phùng/Nguyễn Lương Bằng, район Xuân Hương, 1,7 км до ночного рынка. 1 этаж + 2 надстройки с мезонином, 4 спальни, 4 с/у.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134213711.htm","вчера",1,source="chotot",
  details={"contact":"A Tèo"}),

L(898,"da-lat","xt","Дом",4000000,50,
  "Дом целиком, новое строительство, квартал Trại Mát, район Xuân Trường. Основная площадь 35-37 м² + антресоль 18 м². Свой двор, заезд для мотобайка. Заселение возможно с начала сентября.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134208763.htm","вчера",1,source="chotot",
  details={"deposit":"2 месяца","contact":"Trần Nguyễn"}),

L(899,"da-lat","xh","Дом",6000000,80,
  "Дом целиком (2 спальни, 2 с/у) на ул. Khe Sanh, район Xuân Hương (старое — Phường 10), 3 мин до озера Xuân Hương, рядом больница Hoàn Mỹ.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134199776.htm","2 дня назад",2,source="chotot",
  details={"electricity":"3 500 ₫/кВт·ч","water":"25 000 ₫/м³","deposit":"2 месяца (оплата за 1)","contract":"6 месяцев","contact":"Hương Lê"}),

L(900,"da-lat","lv","Дом",7000000,70,
  "Дом целиком (2 спальни, 1 с/у) на ул. Đinh Công Tráng, район Lâm Viên (старое — Phường 7), рядом школа Lam Sơn, 7 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134186697.htm","2 дня назад",2,source="chotot",
  details={"electricity":"4 000 ₫/кВт·ч","water":"25 000 ₫/м³","deposit":"10 млн ₫","contract":"от 2 лет","contact":"Hương Lê"}),

L(901,"da-lat","xt","Дом",4300000,55,
  "Дом целиком (1 спальня + мезонин), район Xuân Trường, 10 мин до озера Xuân Hương, рядом храм Linh Phước. Без мебели, свой двор.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134185872.htm","2 дня назад",2,source="chotot",
  details={"electricity":"по гостарифу","water":"по гостарифу","deposit":"2 месяца (оплата за 1)","contract":"от 1 года","contact":"Hương Lê"}),

L(902,"da-nang","ns","Студия",8000000,30,
  "Меблированная студия, ул. Hải Triều, район Ngũ Hành Sơn. Бассейн и спортзал в комплексе, еженедельная уборка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134236635.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","contact":"Mr Thịnh"}),

L(903,"da-nang","ah","Студия",17000000,29,
  "Студия на среднем этаже с видом на город и море, район An Hải. Полностью новая меблировка. Год без сервис-сбора.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134236553.htm","сегодня",0,source="chotot",
  details={"contact":"агентство «Thuê Nhà Đẹp Căn Hộ Cao Cấp Đà Nẵng»"}),

L(904,"da-nang","ns","Квартира",17000000,60,
  "Квартира на фасаде квартала An Thượng, район Ngũ Hành Sơn, с балконом. Разрешены животные, принимают иностранцев.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134236493.htm","сегодня",0,source="chotot",
  details={"contact":"Nhuận Oanh"}),

L(905,"da-nang","ah","Квартира",6500000,25,
  "1-спальная квартира, новая меблировка, своя стиральная машина, ул. Lương Thế Vinh (за Mỹ Khê 7, рядом Võ Văn Kiệt), район An Hải.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134236486.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении указан диапазон 6,5-7,5 млн ₫/мес — использована нижняя граница","contact":"Ms Nhu"}),

L(906,"da-nang","ns","Квартира",26500000,65,
  "2-спальная квартира (2 с/у) напрямую от собственника, этаж 20 (кв. 2034), ЖК Mường Thanh Luxury, район Ngũ Hành Sơn. 50 м до пляжа, вид на море с балкона.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134184287.htm","2 дня назад",2,source="chotot",
  details={"amenities":"Netflix и wifi 500 Мбит/с бесплатно, электронный замок (отпечаток/карта/пароль), подземный паркинг, охрана 24/7","contact":"+84 866 791 931 (собственник)"}),

L(907,"da-nang","lc","Квартира",7000000,56,
  "Угловая 2-спальная квартира на 19 этаже, вид на море и озеро Bàu Tràm, ЖК The Ori Garden. Район по ward_name_v3 — «Hải Vân» (не входит в список районов проекта явно; нанесена на ближайший — Liên Chiểu).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/132606104.htm","сегодня",0,source="chotot",
  details={"amenities":"2 кондиционера, ТВ, холодильник, стиралка","contract":"1 год","notice":"цена не включает сервис-сбор; контакт скрыт продавцом (номер замаскирован ***)"}),

L(908,"da-nang","hk","Квартира",9000000,40,
  "1-спальная квартира, ул. Nguyễn Tất Thành, район Hòa Khánh. В нескольких шагах от одноимённого пляжа, вид на море.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134235627.htm","сегодня",0,source="chotot",
  details={"amenities":"своя стиральная машина"}),

L(909,"da-nang","ah","Квартира",12500000,35,
  "1-спальная квартира, новое строительство (2026), этаж 6, рядом Vincom Plaza, район An Hải. Балкон, вид в сторону моря.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134235555.htm","сегодня",0,source="chotot",
  details={"electricity":"3 800 ₫/кВт·ч","water":"100 000 ₫/чел.","deposit":"1 месяц","amenities":"Smart TV, стиралка, диван, СВЧ, бесплатный wifi, уборка 1 раз/нед., прописка для иностранцев","policy":"животные и курение в помещении запрещены"}),

L(910,"da-nang","hc","Квартира",15000000,94,
  "2-спальная квартира (2 с/у) в ЖК Lapaz Tower, район Hải Châu, центр города. Кондиционер, стиралка, кровать, ТВ, диван.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134235191.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц (оплата за 3)"}),

L(911,"da-nang","hc","Квартира",11000000,75,
  "2-спальная квартира (2 с/у) с балконом, отдельная кухня и прачечная, ул. 07 Nguyễn Trãi, район Hải Châu. Рядом мост Dragon Bridge и ул. Nguyễn Văn Linh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134206247.htm","вчера",1,source="chotot",
  details={}),

L(912,"da-nang","ns","Дом",35000000,90,
  "Дом целиком напрямую от собственника, ул. Lê Văn Tâm, район Ngũ Hành Sơn (рядом Crowne Plaza, пляж Sơn Thủy). 3 этажа, 5 спален, 5 с/у, авто во дворе.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134236460.htm","сегодня",0,source="chotot",
  details={"contact":"Mr.Tú (собственник)"}),

L(913,"da-nang","st","Дом",14000000,90,
  "Дом целиком напрямую от собственника, переулок Phan Bá Phiến, район Sơn Trà. 3 этажа, 3 спальни, 2 с/у, 100 м до моря, рядом крупные отели и рыбные рынки.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/133570105.htm","2 дня назад",2,source="chotot",
  details={"notice":"подходит и для проживания, и под онлайн-бизнес (вторично)","contact":"Zalo (номер замаскирован ***)"}),

L(914,"da-nang","tk","Дом",22000000,50,
  "Дом целиком (2 этажа, полная меблировка), переулок с заездом для авто, ул. Nguyễn Văn Linh, район Thanh Khê. 2 спальни, 3 с/у, 1 км до моста Dragon Bridge.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134179368.htm","3 дня назад",3,source="chotot",
  details={}),

L(915,"da-nang","cl2","Дом",15000000,100,
  "Дом целиком, 3 этажа, ул. Cống Quỳnh, рядом с эстакадой Hòa Cẩm, район Cẩm Lệ. 3 спальни, 3 с/у, место для авто.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134235822.htm","сегодня",0,source="chotot",
  details={}),

L(916,"da-nang","ns","Дом",22000000,100,
  "Дом целиком, 2 этажа, ул. Mộc Sơn 2, район Ngũ Hành Sơn, рядом пляж Non Nước. 3 спальни, 3 с/у, двор для авто, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134235765.htm","сегодня",0,source="chotot",
  details={"notice":"контакт скрыт продавцом (номер замаскирован ***)"}),

L(917,"da-nang","tk","Дом",20000000,60,
  "Дом целиком, фасад ул. Thuận An (рядом Thái Thị Bôi и рынок), центр города, район Thanh Khê. 3 спальни, 4 с/у, полная меблировка, авто во дворе. Принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134216512.htm","вчера",1,source="chotot",
  details={"contact":"Nhuận Oanh"}),

L(918,"da-nang","ns","Дом",120000000,325,
  "Вилла с бассейном и садом, ул. Chế Lan Viên, район Ngũ Hành Sơn, рядом квартал An Thượng и море. 2 этажа, 5 спален, 6 с/у, полная премиальная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134235959.htm","сегодня",0,source="chotot",
  details={"notice":"позиционируется для семей/иностранных специалистов, дублируется описание на английском","contact":"Toan House"}),

L(919,"da-nang","ns","Дом",35000000,100,
  "Дом целиком, 3 этажа, ул. Phạm Hữu Kính, Mỹ An, район Ngũ Hành Sơn, рядом река Хан. 4 спальни.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-pham-huu-kinh_1-phuong-ngu-hanh-son-tp-da-nang/cho-3-tang-4pn-uong-kinh-my-an-gan-song-han-pr46202569","проверено 19 авг",0,source="batdongsan",
  details={"contact":"Ms Quyên","notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления (prNNNNNNNN) — выше потолка, зафиксированного сегодняшним HCMC-прогоном (46202495). Цена подтверждена дважды: в карточке поиска и на странице объявления (поле «Khoảng giá»)."}),

L(920,"da-nang","ns","Дом",40000000,100,
  "Дом целиком, новый ремонт, 3 этажа, квартал Nam Việt Á, район Ngũ Hành Sơn. 4 спальни, 5 с/у, балкон и терраса на крыше, полная современная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-doan-khue-1-phuong-ngu-hanh-son-tp-da-nang/cho-moi-ep-4pn-khu-nam-viet-a-full-noi-that-hien-ai-pr46202528","проверено 19 авг",0,source="batdongsan",
  details={"contact":"Ms Quyên","notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления — выше потолка 46202495. Цена подтверждена дважды (карточка + «Khoảng giá»). Для гостей из Китая владелец указывает повышенную ставку 45 млн ₫ — в качестве цены взята стандартная (40 млн ₫)."}),

L(921,"vung-tau","vtp","Квартира",10000000,74,
  "2-спальная квартира (2 с/у) в ЖК Goldsea, вид на море, ~50 м до пляжа Thùy Vân, район Vũng Tàu (центр).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134210077.htm","вчера",1,source="chotot",
  details={"notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Thiết Lê"}),

L(922,"vung-tau","rd","Квартира",16000000,91,
  "3-спальная квартира (2 с/у), новая меблировка (100%), ЖК Vũng Tàu Center Point, район Rạch Dừa.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134189479.htm","2 дня назад",2,source="chotot",
  details={"amenities":"бесплатное обслуживание дома и бассейн","contact":"Như Quỳnh"}),

L(923,"vung-tau","vtp","Квартира",8000000,74,
  "2-спальная квартира (2 с/у) в ЖК Melody, район Vũng Tàu (центр), прямой вид на море. Базовая меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134189418.htm","2 дня назад",2,source="chotot",
  details={"contract":"1 год","policy":"животные не принимаются","contact":"Như Quỳnh"}),

L(924,"vung-tau","rd","Дом",14000000,115,
  "Дом целиком на фасаде ул. Lê Quang Định, район Rạch Dừa. 1 этаж + 2 надстройки, 4 спальни, задний двор.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-vung-tau-ba-ria-vung-tau/133865836.htm","2 дня назад",2,source="chotot",
  details={"notice":"подходит и для проживания, и под офис/репетиторство (вторично)","contact":"Mr Mạnh"}),

L(925,"vung-tau","vtp","Квартира",9000000,92,
  "Квартира ~50 м от моря, район Vũng Tàu (центр).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134168519.htm","3 дня назад",3,source="chotot",
  details={"notice":"также предлагается посуточная аренда — приоритет отдаётся долгосрочным арендаторам","contact":"Loi Nguyen Văn"}),

L(926,"quy-nhon","qn","Квартира",8500000,58,
  "Угловая 2-спальная квартира на высоком этаже с видом на море, ЖК TMS Quy Nhơn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-qui-nhon-binh-dinh/134226216.htm","сегодня",0,source="chotot",
  details={"notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Vũ Thành Long"}),

L(927,"quy-nhon","qn","Квартира",13000000,96,
  "3-спальная квартира с видом на залив, новая меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-qui-nhon-binh-dinh/134166973.htm","3 дня назад",3,source="chotot",
  details={"notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Vũ Thành Long"}),

L(928,"quy-nhon","qn","Дом",3200000,40,
  "Дом с мезонином в переулке от ул. Nguyễn Huệ, рядом с провинциальной больницей, рынком и Университетом Куинён. Несколько шагов до моря.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-qui-nhon-binh-dinh/134220484.htm","вчера",1,source="chotot",
  details={"contact":"Chị Quỳnh"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted daily check (other 7 cities) 19 aug 2026: 54 listings written (52 chotot, 2 batdongsan); "
      "1 duplicate (id 877, dup of pre-existing L(68) URL) removed post-insertion after step-7 URL check -> 53 net new")
