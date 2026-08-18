# -*- coding: utf-8 -*-
# Ежедневная проверка HCMC 18 авг 2026 — 67 действительно новых объявлений (ID 750-816),
# опубликованных 15-18 авг 2026 (daysAgo 0-3).
#
# Источники: Chợ Tốt / Nhà Tốt (53) и Batdongsan.com.vn (14).
# Facebook Marketplace и группы Facebook сегодня недоступны (curl -> HTTP 400, WebFetch -> логин-стена),
# поэтому оттуда не добавлено ничего.
#
# ВАЖНО о датах: и Chợ Tốt, и Batdongsan «поднимают» (đẩy tin) старые объявления, из-за чего
# видимая дата обновляется, а объявление на деле старое. Для Chợ Tốt daysAgo считается по
# orig_list_time (реальная дата создания) из публичного gateway-API, а не по list_time.
# Batdongsan оригинальную дату не публикует вообще, поэтому оттуда взяты только объявления,
# у которых сам ID записи (prNNNNNNNN) свежий, а цена подтверждена дважды — в карточке выдачи
# и на странице объявления; у каждого такого объявления стоит соответствующая пометка.
#
# ВАЖНО о районах (укрупнение округов 2025 г.): новый Phường Bến Thành включает бывшие
# Phạm Ngũ Lão / Nguyễn Thái Bình / Cầu Ông Lãnh, а новый Phường Tân Hưng — бывшие
# Tân Quy / Tân Kiểng / Tân Phong. Ключи tm/th/bth проставлены по официальному новому
# названию района (ward_name_v3), а реальный подрайон назван в описании — как в батче 26.
NEW_SRC = r'''
L(750,"ho-chi-minh","ak","Дом",30000000,250,
  "Дом 2 этажа, 2 спальни/3 с/у, гостиная и кухня, мини-двор. Ул. Quốc Hương, центр Thảo Điền. Тихая охраняемая улица, рядом парк и супермаркет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133314010.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(751,"ho-chi-minh","ak","Дом",35000000,350,
  "Угловой дом на 2 фасада, гараж + 2 этажа, 4 спальни/5 с/у. Ул. Nguyễn Văn Hưởng, Thảo Điền. Улица 10 м, подходит под жильё или офис.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133314052.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(752,"ho-chi-minh","ak","Дом",100000000,120,
  "Вилла с бассейном и лифтом, 5 спален/7 с/у, цоколь + антресоль + 2 этажа. Ул. số 12, Trần Não, An Khánh (бывш. Quận 2). Полностью меблирована.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134174858.htm","2 дня назад",2,source="chotot",
  details={"contact":"Tony BĐS","notice":"⚠ 120 м² — это площадь застройки (7x17 м), общая площадь по этажам больше. Цена 100 млн ₫ указана без налога."}),

L(753,"ho-chi-minh","ak","Квартира",9000000,40,
  "1-спальная квартира с отдельной кухней, балкон, своя стиральная машина. Рядом с Tropic Garden, ул. Quốc Hương, Thảo Điền.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133727326.htm","3 дня назад",3,source="chotot",
  details={"contact":"Thiện HIFRIENDZ"}),

L(754,"ho-chi-minh","bth","Квартира",8000000,40,
  "1-спальная квартира 40 м² с балконом и своей стиральной машиной, ул. Nguyễn Thị Minh Khai, Q1. Пешком до университетов (KHXH&NV, Y Dược), рядом Hồ Con Rùa и собор Нотр-Дам.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/133035984.htm","сегодня",0,source="chotot",
  details={"contact":"Chiêu Minh Vĩ"}),

L(755,"ho-chi-minh","bth","Квартира",30000000,150,
  "3 спальни/2 с/у, полностью меблирована, 4-й этаж. 74 Lý Tự Trọng, Phường Bến Thành — прямо у рынка Bến Thành.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/133703704.htm","сегодня",0,source="chotot",
  details={"contact":"Duy Nguyễn","notice":"⚠ в поле площади указано 150 м², в тексте — 100 м² собственно квартиры плюс терраса, всего около 200 м². Уточняйте у продавца."}),

L(756,"ho-chi-minh","bth","Дом",14000000,27,
  "Дом в переулке с автомобильным заездом, 3x9 м: цоколь + 2 этажа + терраса, 2 спальни с кондиционерами, 3 с/у, солнечный водонагреватель. Ул. Calmette, Phường Bến Thành, у моста Calmette.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134195294.htm","вчера",1,source="chotot",
  details={"contact":"Phương","notice":"⚠ в поле цены стоит 14 млн ₫, в тексте объявления — «14,5 млн ₫, ещё торг». Использована цена из поля; ориентируйтесь на 14-14,5 млн."}),

L(757,"ho-chi-minh","bth","Квартира",8000000,45,
  "1-спальная квартира 45 м² с большим балконом, полная меблировка, вход по отпечатку пальца, лифт, круглосуточная охрана. Ул. Nguyễn Thái Bình (новый Phường Bến Thành), пешком до рынка Bến Thành и ул. Nguyễn Huệ.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134192560.htm","вчера",1,source="chotot",
  details={"contact":"Trần Hưng"}),

L(758,"ho-chi-minh","bth","Дом",15000000,24,
  "Дом целиком, 3x8 м (Г-образный), цоколь + 2 этажа + терраса, 2 спальни, 4 с/у, кондиционеры в каждой комнате, солнечный водонагреватель. Переулок с автозаездом, ул. Calmette.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134174699.htm","2 дня назад",2,source="chotot",
  details={"contact":"Thuy Vi","notice":"залог 2 месяца. Тот же дом продвигают ещё два агента отдельными объявлениями — при обзвоне возможны повторы."}),

L(759,"ho-chi-minh","bth","Дом",7500000,15,
  "Дом на 2 фасада в переулке, цоколь + 1 этаж, 2 спальни, балкон, свежий ремонт, есть кондиционер, водонагреватель, кровать и шкаф. Пер. 265 Phạm Ngũ Lão (новый Phường Bến Thành), у парка 23/9 и ул. Bùi Viện.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134172340.htm","2 дня назад",2,source="chotot",
  details={"contact":"Dang Lam Son","notice":"⚠ в поле площади 15 м², в тексте — 30 м² общей площади (цоколь + этаж)."}),

L(760,"ho-chi-minh","bth","Дом",9000000,27,
  "Дом целиком без мебели, 3x9 м, цоколь + 1 этаж, 2 спальни, 1 с/у + душевая. Электричество и вода по государственному тарифу. Пер. 120 Trần Hưng Đạo, 5 минут пешком до Bùi Viện.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134166853.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trần Minh","notice":"цена «9 млн, торг»."}),

L(761,"ho-chi-minh","bth","Дом",7500000,27,
  "Дом целиком без мебели, 2,5x7 м, цоколь + 1 этаж, 2 спальни, 1 с/у. Электричество и вода по государственному тарифу. Пер. 217 Đề Thám (новый Phường Bến Thành), 2 минуты до Bùi Viện.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/133546031.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trần Minh"}),

L(762,"ho-chi-minh","bth","Дом",12000000,48,
  "Полностью отремонтированный дом от собственника, 4 уровня: цоколь + 2 этажа + терраса, 2 спальни. Пер. Đỗ Quang Đẩu / 12 Bùi Viện, ~30 м от главной улицы, рядом пешеходная Nguyễn Huệ.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/133509519.htm","3 дня назад",3,source="chotot",
  details={"contact":"Thiện Tâm"}),

L(763,"ho-chi-minh","btr","Дом",40000000,410,
  "Дом с гаражом, цоколь + 3 этажа, 4 большие спальни, 5 с/у. Ул. số 57, Bình Trưng, рядом река и парк, улица 10 м.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133295504.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(764,"ho-chi-minh","btr","Дом",55000000,420,
  "Вилла с гаражом и двором, цоколь + 3 этажа, 5 спален, 5 с/у, ориентация юго-восток. Ул. Đỗ Pháp Thuận, Bình Trưng.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133220885.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(765,"ho-chi-minh","btr","Дом",35000000,410,
  "Дом целиком 8x20 м, гараж + цоколь + 3 этажа, 5 спален, 5 с/у. Bình Trưng Tây, рядом с Đảo Kim Cương (Diamond Island). Собственник предпочитает договор на 2-5 лет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133295237.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(766,"ho-chi-minh","btr","Дом",35000000,400,
  "Дом с гаражом, цоколь + 3 этажа, 5 больших спален, 5 с/у. Ул. Lương Định Của, Bình Trưng, рядом парк и супермаркет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133309816.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(767,"ho-chi-minh","btr","Дом",40000000,390,
  "Вилла с гаражом и двором, цоколь + 3 этажа, 5 спален, 5 с/у, юго-восток. Ул. Nguyễn Hoàng, Bình Trưng.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133179629.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(768,"ho-chi-minh","btr","Дом",33000000,100,
  "Таунхаус в Lakeview City с видом на озеро, 5x20 м, площадь застройки 262 м², полностью меблирован премиум-мебелью. Ул. Song Hành, рядом Đỗ Xuân Hợp, Mai Chí Thọ и The Global City.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134208435.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng, Mana Homes","notice":"⚠ в поле площади 100 м² (участок), в тексте — 262 м² застройки."}),

L(769,"ho-chi-minh","btr","Дом",50000000,95,
  "Новый таунхаус в The Global City, 5x19 м, полезная площадь 400 м², цоколь + 4 этажа, лифт, кондиционеры, мебель на верхнем этаже. Ул. Đỗ Xuân Hợp.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/130746503.htm","сегодня",0,source="chotot",
  details={"contact":"Mr. Kha","notice":"⚠ в поле площади 95 м² (участок), в тексте — 400 м² полезной. У агента есть и другие дома в The Global City, 45-120 млн ₫."}),

L(770,"ho-chi-minh","btr","Квартира",18500000,98,
  "3-спальная квартира 98 м² в Cantavil An Phú, высокий этаж, хороший вид, полностью меблирована, заезд сразу. Ул. Thái Thuận, район An Phú An Khánh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/132957410.htm","сегодня",0,source="chotot",
  details={"contact":"Hằng"}),

L(771,"ho-chi-minh","btr","Дом",32000000,265,
  "Таунхаус в закрытом комплексе Lakeview City, 5x20 м, цоколь + 3 этажа, 5 спален, 6 с/у, полная меблировка. Бассейн, спортзал, кафе и ТЦ в радиусе 200 м, экопарк 3,6 га.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134159448.htm","3 дня назад",3,source="chotot",
  details={"contact":"Võ Hữu Nhân","notice":"залог 2 месяца."}),

L(772,"ho-chi-minh","th","Дом",8000000,25,
  "Небольшой дом целиком, 2 спальни, 2 с/у. Ул. Số 27, бывший Phường Tân Quy (новый Tân Hưng). Широкий переулок с автозаездом, без подтоплений.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134208795.htm","сегодня",0,source="chotot",
  details={"contact":"Việt Tiến"}),

L(773,"ho-chi-minh","th","Дом",35000000,120,
  "Дом на первой линии 6x20 м, цоколь + 3 этажа, 5 спален (3 с мебелью), 6 с/у, двор спереди и сзади, терраса. Бывший Phường Tân Quy, несколько минут до Lotte Mart, SC VivoCity и Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134208458.htm","сегодня",0,source="chotot",
  details={"contact":"Gia Gia","notice":"собственник разрешает жильё в сочетании с работой, но запрещает переоборудование под сервисные апартаменты (CHDV)."}),

L(774,"ho-chi-minh","th","Дом",30000000,80,
  "Дом на первой линии ул. Phan Huy Thực, 4x20 м, цоколь + 2 этажа, 4 спальни, 4 с/у. Оживлённый жилой квартал со всей инфраструктурой.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134208354.htm","сегодня",0,source="chotot",
  details={"contact":"Quốc Đạt"}),

L(775,"ho-chi-minh","th","Дом",10000000,44,
  "Дом целиком 4x11 м, 1 этаж, 2 спальни, 1 с/у, базовая мебель. Пер. 1041 Trần Xuân Soạn, Phường Tân Hưng. Рядом мост Him Lam, Lotte Mart, университеты Tôn Đức Thắng и RMIT.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134208072.htm","сегодня",0,source="chotot",
  details={"contact":"Anh Quan"}),

L(776,"ho-chi-minh","th","Квартира",17000000,76,
  "2-спальная квартира 76 м², 2 с/у, полная меблировка, ЖК Sunrise City, ул. Nguyễn Hữu Thọ.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/131393439.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Quốc Thịnh","notice":"у того же агента в Sunrise City есть и другие варианты (106 м² 2 спальни — 18 млн, 99 м² Central — 20 млн)."}),

L(777,"ho-chi-minh","th","Дом",6500000,44,
  "Дом в переулке, 3,8x13 м, цоколь с антресолью, 3 спальни, 1 с/у. Ул. Trần Xuân Soạn, Phường Tân Hưng. Мотобайковый переулок, счётчики по основному тарифу, свободен.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134207211.htm","сегодня",0,source="chotot",
  details={"contact":"Vinh","notice":"залог 1 месяц."}),

L(778,"ho-chi-minh","th","Дом",8000000,48,
  "Дом целиком 4x12 м, цоколь + этаж, 2 спальни, 2 с/у. Переулок 2 м (только мотобайки), ул. Lê Văn Lương, Phường Tân Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134206954.htm","сегодня",0,source="chotot",
  details={"contact":"Vinh","notice":"⚠ только под жильё, коммерческая деятельность запрещена; собственник просит небольшую семью. Залог 1 месяц + 1 месяц вперёд."}),

L(779,"ho-chi-minh","th","Студия",6000000,28,
  "Студия с большим балконом на зелень, деревянный пол, полная премиум-меблировка (ТВ, кондиционер, большой холодильник, обеденный стол, своя кухня). Вилловый квартал Dragon Parc 2, охрана 24/7, ул. Nguyễn Hữu Thọ.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134205789.htm","сегодня",0,source="chotot",
  details={"contact":"Quốc Thắng Nguyễn"}),

L(780,"ho-chi-minh","th","Дом",38000000,89,
  "Дом целиком от собственника: 46 Mai Văn Vĩnh, Phường Tân Hưng, 50 м от перекрёстка с Nguyễn Thị Thập, оживлённый район рядом со школами, супермаркетом и рынком.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/127890819.htm","сегодня",0,source="chotot",
  details={"contact":"Thảo Thanh (собственник)","notice":"в одном объявлении сдаются два разных дома — второй по адресу 1172/12 Huỳnh Tấn Phát, Phường Tân Mỹ (4x18 м, цоколь + 2 этажа + терраса, 5 спален). Цена 38 млн ₫ относится к объекту на Mai Văn Vĩnh."}),

L(781,"ho-chi-minh","th","Дом",19000000,120,
  "Дом-вилла 8x15 м, цоколь + 1 этаж, 4 спальни, 2 с/у, гостиная, кухня, двор под машину. Пер. 1041 Trần Xuân Soạn, Phường Tân Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133904642.htm","сегодня",0,source="chotot",
  details={"contact":"LHP"}),

L(782,"ho-chi-minh","th","Дом",10000000,44,
  "Дом целиком 4x11 м, цоколь + этаж, 2 спальни, 1 с/у. Мебель: 2 кондиционера, стиральная машина, холодильник, водонагреватель, фильтр для воды, кухонный гарнитур. Пер. Trần Xuân Soạn рядом с Him Lam.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134200854.htm","вчера",1,source="chotot",
  details={"contact":"Gia Gia"}),

L(783,"ho-chi-minh","th","Дом",12000000,72,
  "Дом 4x18 м, цоколь + 1 этаж, 3 спальни, 2 с/у, гостиная, кухня, двор под машину. Ул. Trần Xuân Soạn, Phường Tân Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133808666.htm","вчера",1,source="chotot",
  details={"contact":"LHP"}),

L(784,"ho-chi-minh","th","Дом",10000000,30,
  "Новый дом целиком 3x10 м, цоколь + 1 этаж, 2 спальни, 2 с/у, 2 новых кондиционера, просторная кухня. Пер. 108 Lê Văn Lương, выход к мосту Kênh Tẻ — 5 минут до Quận 4.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134200113.htm","вчера",1,source="chotot",
  details={"contact":"Mec Nguyễn","notice":"⚠ домашние животные запрещены. Электричество и вода по государственному тарифу, оплата помесячно с залогом за месяц."}),

L(785,"ho-chi-minh","th","Студия",4500000,35,
  "Передача аренды дома целиком с антресолью, полная меблировка (кондиционер, холодильник, стиральная машина, большой шкаф, газовая плита). Крытый двор под сушку белья и 3-4 мотобайка. Пер. 791 Trần Xuân Soạn.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134199483.htm","вчера",1,source="chotot",
  details={"contact":"Anh Đức","notice":"заезд возможен с начала сентября 2026. 2 км до университетов Tài chính-Marketing и Tôn Đức Thắng."}),

L(786,"ho-chi-minh","th","Дом",15000000,110,
  "Одноэтажный дом на первой линии, 5x22 м, 2 спальни, 2 с/у, 2 кондиционера. Ул. số Lâm Văn Bền, бывший Phường Tân Quy.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134197944.htm","вчера",1,source="chotot",
  details={"contact":"Lê Vân BĐS","notice":"этажей нет — только цоколь."}),

L(787,"ho-chi-minh","th","Квартира",12000000,63,
  "2-спальная квартира 63 м², 1 с/у, с мебелью, ЖК M-One Nam Sài Gòn, бывший Phường Tân Kiểng. Бассейн, спортзал, спа, супермаркет, BBQ, парк вдоль реки.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/132046796.htm","вчера",1,source="chotot",
  details={"contact":"Hữu Nhân","notice":"у агента в этом ЖК есть и другие квартиры."}),

L(788,"ho-chi-minh","th","Дом",9700000,35,
  "Новый дом целиком, 2 спальни, полная новая меблировка, рассчитан на 2-4 человек. Ул. Trần Xuân Soạn, Phường Tân Hưng. Рядом Quận 1 и 4, университеты TĐT и RMIT.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133812034.htm","вчера",1,source="chotot",
  details={"contact":"Hang Pham","notice":"можно с животными и электробайком, цена обсуждается."}),

L(789,"ho-chi-minh","th","Студия",4500000,35,
  "Дуплекс-студия с балконом и полной меблировкой, большое окно. Ул. Nguyễn Thị Thập, напротив университета Tôn Đức Thắng, рядом UFM, NTTU, RMIT и Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134196108.htm","вчера",1,source="chotot",
  details={"contact":"Nhật Thiên","notice":"⚠ цена «от»: в объявлении диапазон 4,5-6 млн ₫ в зависимости от комнаты, ориентировано на студентов, в том числе подселение."}),

L(790,"ho-chi-minh","th","Дом",130000000,300,
  "Вилла Nam Thông I, 300 м², цоколь + 3 этажа, 5 спален, бассейн, премиум-мебель, 2 фасада. Напротив Канадской международной школы, Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134192547.htm","вчера",1,source="chotot",
  details={"contact":"Thảo","notice":"верхний ценовой сегмент — для ориентира по рынку вилл Phú Mỹ Hưng."}),

L(791,"ho-chi-minh","th","Дом",12000000,40,
  "Дом 8x6 м, цоколь + 3 этажа, 3 спальни (по одной на этаж), 4 с/у, большие балконы. Широкий переулок, ул. Lê Văn Lương, Tân Hưng. 200 м до университета Tôn Đức Thắng, 100 м до Lotte.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134192034.htm","вчера",1,source="chotot",
  details={"contact":"Phạm Tăng","notice":"цена обсуждается."}),

L(792,"ho-chi-minh","th","Студия",7000000,25,
  "Новая сервисная студия: окно, отдельный балкон, полная новая меблировка (кровать, шкаф, кондиционер, холодильник, рабочий стол, водонагреватель), своя кухня и с/у, wi-fi, камеры 24/7. Ул. Số 36, Phường Tân Hưng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133510216.htm","вчера",1,source="chotot",
  details={"contact":"Duy Tân","notice":"в здании несколько типов комнат по разным ценам — 7 млн ₫ относится к описанному варианту."}),

L(793,"ho-chi-minh","th","Студия",6000000,40,
  "Двухуровневый дуплекс с балконом, полная премиум-меблировка, оборудованная кухня, свободный режим входа. Ул. Số 37, Phường Tân Hưng. Несколько минут до Lotte Mart, SC VivoCity, TDTU, RMIT, UFM и Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133741374.htm","вчера",1,source="chotot",
  details={"contact":"Nhật Thiên Airways Unitegroup"}),

L(794,"ho-chi-minh","th","Студия",5500000,40,
  "Квартира-студия с отдельным балконом, полная меблировка, современный ремонт. Ул. Nguyễn Thị Thập, Tân Hưng — рядом TDTU, Lotte Mart, NTTU, удобный выезд в Quận 1, 4, 8 и Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134189415.htm","вчера",1,source="chotot",
  details={"contact":"Nguyễn Hữu Quyết"}),

L(795,"ho-chi-minh","th","Дом",25000000,150,
  "Цокольный этаж виллы с отдельным входом, 7,5x20 м, готовые комнаты с кондиционерами, двор спереди и сзади, свободная парковка у дома. Квартал Him Lam, Tân Hưng, напротив парка.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134187797.htm","вчера",1,source="chotot",
  details={"contact":"Nguyễn Hoàng Minh Sơn, S Home","notice":"сдаётся только цокольный этаж виллы, не дом целиком."}),

L(796,"ho-chi-minh","th","Дом",15000000,100,
  "Цокольный этаж виллы 5x20 м в квартале Him Lam Tân Hưng, напротив парка, двор спереди и сзади, свободная парковка. Заезд сразу.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134187999.htm","вчера",1,source="chotot",
  details={"contact":"Nguyễn Hoàng Minh Sơn, S Home","notice":"сдаётся только цокольный этаж виллы. ⚠ в заголовке 5x18 м, в тексте 5x20 м (100 м²)."}),

L(797,"ho-chi-minh","th","Студия",5800000,40,
  "Дуплекс с полной меблировкой и собственной стиральной машиной, просторно и приватно, на 1-2 человек. Ул. Trần Xuân Soạn, Quận 7. Рядом TDTU, RMIT, UFM.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134175843.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nhật Thiên Airways Unitegroup"}),

L(798,"ho-chi-minh","th","Студия",5500000,43,
  "Квартира с антресолью и дизайнерским ремонтом, деревянный пол, своя стиральная машина, большой холодильник, кондиционер, шкаф, обеденная зона, просторная кухня. Ул. Trần Xuân Soạn у мостов Rạch Ông и Him Lam.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134175552.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phong Nguyễn","notice":"в здании есть комнаты от 5 до 8 млн ₫ — 5,5 млн относится к описанной."}),

L(799,"ho-chi-minh","th","Студия",5400000,27,
  "Квартира с высокой антресолью на 3 человек, 2 больших панорамных окна, кондиционер, шкаф, отдельная кухонная зона, свой с/у. Есть лифт, камеры 24/7, вход по отпечатку, свободный режим, без подселения к хозяевам. Ул. Lê Văn Lương у рынка Tân Quy и Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134174630.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phong Nguyễn"}),

L(800,"ho-chi-minh","th","Студия",6000000,40,
  "Мини-квартира в жилом квартале Kim Sơn напротив университетов TĐT и RMIT (пешком). Полная современная меблировка, свободный режим, камеры 24/7, вход по отпечатку, лифт, пожарная система, парковка, общая стирально-сушильная зона, скоростной интернет и кабельное.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134172290.htm","2 дня назад",2,source="chotot",
  details={"contact":"агент «Hà cho thuê căn hộ mini Quận 7»"}),

L(801,"ho-chi-minh","th","Квартира",15000000,71,
  "Угловая 2-спальная квартира 71 м² с собственным садом-террасой 12 м², 3-й этаж, вид на VivoCity. ЖК Sky Garden 1, ул. Phạm Văn Nghị. Мебель: 3 новых кондиционера, кровать, новый холодильник, полностью оборудованная кухня.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133245543.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phạm Hồng Đức","notice":"цена включает эксплуатационный сбор и интернет. Ограничение: до 4 человек, без кошек и собак. Рядом больницы FV и Tâm Đức, парк Hồ Bán Nguyệt."}),

L(802,"ho-chi-minh","th","Студия",5000000,35,
  "Сервисная студия с балконом и отдельной кухней, полная меблировка, свежая уборка, заезд сразу. Ул. Mai Văn Vĩnh, центр Quận 7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134165695.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trịnh Hữu Nghị","notice":"при заезде в текущем месяце собственник обещает скидку 2 млн ₫."}),

L(803,"ho-chi-minh","tm","Квартира",22000000,82,
  "2-спальная квартира 82 м² в The Infiniti at Riviera Point, ул. Huỳnh Tấn Phát, бывший Phường Tân Phú (новый Tân Mỹ). Агент позиционирует как «2 спальни по цене однушки».",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-huynh-tan-phat-phuong-tan-phu-19-the-infiniti-riviera-point/cho-nhanh-2pn-gia-re-chi-bang-1pn-tro-xem-nha-24-7-pr46188496","2 дня назад",2,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «2 дня» это её собственная отметка. Цена 22 млн ₫ подтверждена дважды: в карточке выдачи и в блоке параметров объявления."}),

L(804,"ho-chi-minh","bth","Комната",4600000,20,
  "Студенческая комната 20 м² с окном, полностью оборудована. Ул. Phạm Ngũ Lão (новый Phường Bến Thành), рядом с улицей Bùi Viện, самый центр Q1.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-pham-ngu-lao-phuong-pham-ngu-lao-1-53/trong-sinh-vien-20m2-cua-so-full-tien-nghi-gia-chi-4x-ngay-trung-tam-gan-pho-bui-vien-q1-pr46194018","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 4,6 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(805,"ho-chi-minh","bth","Дом",10000000,21,
  "Дом 21 м², 2 этажа, ул. Lê Thị Riêng, Phường Bến Thành.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-thi-rieng-phuong-ben-thanh-53/cho-21m-2-tang-10-trieu-thang-pr46193043","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 10 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Описание у объявления очень краткое."}),

L(806,"ho-chi-minh","bth","Дом",20000000,36,
  "Дом 36 м², 4 этажа, ул. Tôn Thất Tùng (новый Phường Bến Thành).",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ton-that-tung-phuong-pham-ngu-lao-1-53/cho-36m-4-tang-20-trieu-thang-pr46192981","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 20 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Описание у объявления очень краткое."}),

L(807,"ho-chi-minh","bth","Дом",23000000,60,
  "Дом 60 м², 1 этаж, ул. Nguyễn Du, Phường Bến Thành.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-du-phuong-ben-thanh-53/cho-60m-1-tang-23-trieu-thang-pr46192828","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 23 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Описание у объявления очень краткое."}),

L(808,"ho-chi-minh","bth","Дом",18000000,36,
  "Дом 36 м², 1 этаж, ул. Thủ Khoa Huân, Phường Bến Thành — рядом с рынком Bến Thành.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-thu-khoa-huan-phuong-ben-thanh-53/cho-36m-1-tang-18-trieu-thang-pr46192816","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 18 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Описание у объявления очень краткое."}),

L(809,"ho-chi-minh","bth","Студия",6500000,45,
  "Студия с балконом 45 м², ул. Bùi Thị Xuân (новый Phường Bến Thành), самый центр Quận 1.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-bui-thi-xuan-phuong-pham-ngu-lao-1-53/studio-ban-cong-ngay-trung-tam-quan-1-pr46183646","3 дня назад",3,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «3 дня» это её собственная отметка. Цена 6,5 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(810,"ho-chi-minh","th","Дом",10000000,34,
  "Дом целиком в квартале Him Lam, 2 этажа, 2 комнаты, 34 м². Ул. Trần Xuân Soạn, Phường Tân Hưng.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-tran-xuan-soan-phuong-tan-hung-14-59/cho-nguyen-can-kdc-himlam-2-tang-2-phong-34m2-10tr-thang-pr46191418","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 10 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(811,"ho-chi-minh","th","Комната",5700000,30,
  "Комната 30 м² в доме 70 по ул. Nguyễn Văn Quỳ, бывший Phường Tân Kiểng (новый Tân Hưng). Свежий ремонт, много удобств поблизости.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-van-quy-phuong-tan-kieng-59/cho-70-5-7-trieu-30-m2-ep-nhieu-tien-ich-pr46190981","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 5,7 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(812,"ho-chi-minh","th","Комната",6000000,35,
  "Комната 35 м² с полной меблировкой, ул. Số 2, квартал Kim Sơn, бывший Phường Tân Phong (новый Tân Hưng). Напротив университета Tôn Đức Thắng и академии Cảnh sát Nhân dân.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-so-2-phuong-tan-phong-9-khu-dan-cu-kim-son/cho-full-noi-that-35m-oi-dien-h-ton-uc-thang-canh-sat-nhan-quan-7-pr46189179","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 6 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(813,"ho-chi-minh","th","Комната",5800000,30,
  "Комната типа «master» 30 м² в ЖК Hoàng Anh Gia Lai 3, ул. Nguyễn Hữu Thọ, Phường Tân Hưng. Рядом университеты TDTU, UFM, RMIT.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-huu-tho-phuong-tan-hung-14-59/uu-tien-cho-sv-master-trong-chung-cu-hagl3-gan-h-tdtu-ufm-rmit-pr46184693","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 5,8 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Объявление ориентировано на студентов (подселение в квартире)."}),

L(814,"ho-chi-minh","th","Комната",4700000,20,
  "Комната 20 м², ул. 9A, Phường Tân Hưng. Рядом университеты Tôn Đức Thắng, RMIT и педагогический.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-9a-phuong-tan-hung-14-59/cho-gan-h-t-tu-rmit-su-pham-pr46184329","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 4,7 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(815,"ho-chi-minh","th","Комната",4500000,20,
  "Комната 20 м² в ЖК Hồng Lĩnh, ул. 9A, Phường Tân Hưng. Рядом TDTU, RMIT и педагогический университет.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-9a-phuong-tan-hung-14-59/uu-tien-cho-sv-trong-chung-cu-hong-linh-gan-h-tdtu-rmit-h-su-pham-pr46184234","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 4,5 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Объявление ориентировано на студентов (подселение)."}),

L(816,"ho-chi-minh","th","Дом",12000000,80,
  "Дом целиком 80 м², 2 спальни, 2 с/у, просторный, свежий ремонт. Район Lotte Mart, ул. Trần Xuân Soạn, Phường Tân Hưng.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-tran-xuan-soan-phuong-tan-hung-14-59/cho-nguyen-can-khu-vuc-lotte-mart-2pn-2wc-cuc-ki-rong-rai-ep-moi-lam-pr46169030","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 12 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted daily check 18 aug 2026 (67 listings: 53 chotot + 14 batdongsan)")
