# -*- coding: utf-8 -*-
# Ho Chi Minh City refresh round 2 — batch 2/5: Chợ Tốt / Nhà Tốt (22 listings), IDs 672-693.
NEW_SRC = r'''
L(672,"ho-chi-minh","bth","Комната",7200000,36,
  "Комната с балконом, полная мебель, ул. Lê Lai, Bến Thành.",
  "https://www.nhatot.com/thue-phong-tro-quan-1-tp-ho-chi-minh/134195225.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"1 месяц (7,2 млн ₫)"}),

L(673,"ho-chi-minh","bth","Комната",4000000,30,
  "Недорогая комната, своя ванная, без совместного хозяина, ул. Nam Kỳ Khởi Nghĩa, Bến Thành.",
  "https://www.nhatot.com/thue-phong-tro-quan-1-tp-ho-chi-minh/134166268.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"1 месяц"}),

L(674,"ho-chi-minh","bth","Комната",6900000,40,
  "Комната с окном на крышу (планировка на 2 «спальни»), рядом университеты UEH и Sài Gòn, ул. Nguyễn Thị Minh Khai, Bến Thành.",
  "https://www.nhatot.com/thue-phong-tro-quan-1-tp-ho-chi-minh/134053139.htm","7 дней назад",7,source="chotot",
  details={"notice":"свет/вода/сервис отдельно, краткосрочная аренда +15% к цене. В поле «депозит» стоит явно техническое значение — не ориентируйтесь на него."}),

L(675,"ho-chi-minh","bth","Студия",6500000,40,
  "Студия с отдельной кухней и балконом, рядом Bùi Viện, разрешены животные, рядом несколько вузов. Ул. Bùi Thị Xuân, Bến Thành.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134070750.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(676,"ho-chi-minh","bth","Квартира",30000000,100,
  "3-спальная квартира, этаж 4, в 100 м от рынка Bến Thành, подходит под хоумстей. Ул. Lý Tự Trọng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/132650643.htm","3 дня назад",3,source="chotot",
  details={}),

L(677,"ho-chi-minh","bth","Квартира",10500000,60,
  "«Пентхаус» в центре Bến Thành, 1 спальня, премиум-мебель, весь этаж. Ул. Nguyễn Thị Minh Khai.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/132326663.htm","5 дней назад",5,source="chotot",
  details={"notice":"поле «депозит» показывает явно ошибочное значение (1 000 000 ₫ при такой аренде) — не ориентируйтесь на него."}),

L(678,"ho-chi-minh","kh","Комната",4200000,20,
  "Комната, рядом университет Nguyễn Tất Thành, ул. Đoàn Văn Bơ.",
  "https://www.nhatot.com/thue-phong-tro-quan-4-tp-ho-chi-minh/129051597.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"1 месяц","electricity":"3 700 ₫/кВт·ч","water":"100 000 ₫/чел.","fees":"сервис 100 000 ₫/комната"}),

L(679,"ho-chi-minh","kh","Студия",6500000,25,
  "Студия в 500 м от университета права (ĐH Luật), ул. Nguyễn Trường Tộ.",
  "https://www.nhatot.com/thue-phong-tro-quan-4-tp-ho-chi-minh/134193231.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"1 месяц"}),

L(680,"ho-chi-minh","kh","Комната",4800000,18,
  "Комната на Xóm Chiếu, бонус 500 тыс ₫ при переезде в сентябре.",
  "https://www.nhatot.com/thue-phong-tro-quan-4-tp-ho-chi-minh/134154570.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"⚠ это переуступка — текущий жилец съезжает из своего 6-месячного контракта, гарантия аренды только на ~3 месяца.","electricity":"4 000 ₫/кВт·ч","water":"100 000 ₫/чел.","fees":"интернет+лифт+мусор 150 000 ₫/комната"}),

L(681,"ho-chi-minh","kh","Студия",9000000,38,
  "Студия с видом на Q1, рядом мост Ông Lãnh, ул. Hoàng Diệu.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134143475.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"2 месяца (18 млн ₫)","fees":"сервис-сбор ~200 000 ₫/мес"}),

L(682,"ho-chi-minh","kh","Квартира",13000000,65,
  "2-спальная квартира (1 с/у) в ЖК H1, угловая, стиральная+сушильная машина, холодильник, ТВ, рядом университет права, рынок Xóm Chiếu, Bến Nhà Rồng. Ул. Hoàng Diệu.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134162206.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"2 месяца (26 млн ₫)","contract":"от 1 года, без комиссии агенту","notice":"текущий жилец съезжает в конце августа, заезд с сентября"}),

L(683,"ho-chi-minh","kh","Квартира",20000000,74,
  "2-спальная квартира (2 с/у) в Masteri Millennium, прямо напротив Q1. Ул. Bến Vân Đồn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134142975.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"⚠ несостыковка площади: в структурированном поле 74 м², в тексте описания «rộng 65m2» — уточняйте у автора."}),

L(684,"ho-chi-minh","kh","Квартира",10500000,57,
  "Угловая 1-спальная квартира, полная мебель, высокий этаж, ЖК H3. Ул. Hoàng Diệu.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134186401.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(685,"ho-chi-minh","th","Квартира",13000000,70,
  "2-спальная квартира от 70 м² в Sky Garden 3 (застройщик Phú Mỹ Hưng), рядом SC VivoCity. Ул. Phạm Văn Nghị.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134194871.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"это агентский прайс-лист по нескольким юнитам в комплексе, не конкретная квартира: 2PN 70-75м² = 13-16 млн, 3PN 85-100м² = 18-30 млн. Указана нижняя граница."}),

L(686,"ho-chi-minh","th","Студия",9000000,28,
  "Студия-офистель в Lavida Plus, напротив Vivo City, рядом RMIT и Tôn Đức Thắng. Ул. Nguyễn Văn Linh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134194791.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(687,"ho-chi-minh","th","Квартира",40000000,100,
  "2-спальная квартира с видом на реку в Riverpark Premier (застройщик Phú Mỹ Hưng), рядом международная школа SSIS. Ул. Nguyễn Đức Cảnh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/131979965.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"премиум-сегмент"}),

L(688,"ho-chi-minh","ak","Студия",7200000,35,
  "Просторная студия, 15 мин до Q1/Bình Thạnh, охрана, паркинг. Ул. Trần Não.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/132504325.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(689,"ho-chi-minh","ak","Комната",8000000,50,
  "Комната в квартире De Capella (2 спальни/2 с/у, 50 м² на двоих), своя ванная, тарифы по гостарифу, заезд с начала августа. Ул. Lương Định Của.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134124945.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"⚠ это подселение в комнату к текущему жильцу, а не аренда целой квартиры."}),

L(690,"ho-chi-minh","ak","Квартира",7000000,40,
  "1-спальная квартира с видом на Landmark 81, отдельная кухня. Ул. Số 38.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133932395.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(691,"ho-chi-minh","bq","Дом",12000000,160,
  "Дом целиком, 3 спальни, есть право собственности (сổ), 3 кондиционера. Ул. Bình Quới.",
  "https://www.nhatot.com/thue-nha-dat-quan-binh-thanh-tp-ho-chi-minh/133318523.htm","16 дней назад",16,source="chotot",
  details={}),

L(692,"ho-chi-minh","bq","Дом",3500000,42,
  "Домик в стиле хоумстей, 1 спальня, естественная вентиляция, без комиссии. Ул. Bình Quới.",
  "https://www.nhatot.com/thue-nha-dat-quan-binh-thanh-tp-ho-chi-minh/134165310.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(693,"ho-chi-minh","bq","Дом",7000000,65,
  "Дом с видом на канал/озеро, свой сад, напротив зоны отдыха KDL Bình Quới 1, подходит под шоурум. Ул. Bình Quới.",
  "https://www.nhatot.com/thue-nha-dat-quan-binh-thanh-tp-ho-chi-minh/133516531.htm","5 дней назад",5,source="chotot",
  details={}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted round-2 batch 2 (chotot)")
