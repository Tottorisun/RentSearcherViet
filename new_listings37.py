# -*- coding: utf-8 -*-
# Ежедневная проверка HCMC 19 авг 2026 (5-й прогон в тот же день, ~19:30, после 4-го прогона
# 18:08/коммита ada493d) — 10 новых объявлений (ID 939-948).
#
# Chợ Tốt: широкий срез по всем 5 районам (Q1/Q4/Q7/Bình Thạnh/Thủ Đức) x 3 категориям
# (căn hộ/nhà/phòng trọ), offset 0/20/40/60 на запрос (глубже, чем в прошлых прогонах) —
# 765 объявлений всего, 216 в целевых районах, 134 с честным orig_list_time <=3.5 дня (все
# ward_name_v3 сверены через unicodedata.normalize('NFC', ...) с обеих сторон). Из них 40 уже
# были в файле (добавлены прошлыми прогонами сегодня, проверено grep по URL/ID в
# rebuild_final.py). Из оставшихся 94 кандидатов детально проверено (текст объявления +
# повторная сверка цены на детальной странице ad-listing/<id>) 12 наиболее похожих на
# конкретные, непосреднические единичные объекты; приняты 10, отклонены 2:
#   - 133780209 ("Căn hộ M-One 2PN 2WC... 13 triệu") — при совпадающей цене в подписи, тело
#     объявления содержит явный "Giỏ hàng cho thuê căn hộ M-One" (прайс-лист на 5 разных типов
#     юнитов: Officetel/Duplex/2PN1WC/2PN2WC/3PN) — тот же посреднический паттерн, что и
#     отклонённые в прошлых прогонах "chuỗi"-объявления — отклонено.
#   - 134221706 ("KHAI TRƯƠNG CĂN HỘ QUẬN 1...") — рекламный пост компании "Unite Group" о
#     "получении удачи на открытии" (khai trương), без конкретного адреса/юнита/этажа —
#     промо-реклама услуги, а не объявление о конкретном объекте — отклонено.
# Из принятых 10: ward_name_v3 у ЖК De Capella (ID 944, An Khánh) отдельно перепроверен через
# геокодинг адреса 116 Lương Định Của — Nominatim подтверждает Phường An Khánh (это не тот
# случай, что Estella Heights/Palm Heights из прошлой заметки — те реально относятся к Bình
# Trưng). Для ID 939 (Lâm Văn Bền) обнаружен классический repush-трюк: витринная дата API
# "10 giờ trước" (list_time), но честный orig_list_time даёт ~49 часов (2 дня) — использован
# честный расчёт daysAgo=2, а не витринный.
#
# Batdongsan.com.vn: не проверялся отдельно в этом прогоне — весь бюджет проверки ушёл на
# глубокий срез Chợ Тốt (offset 0-60 x 15 комбинаций район/категория); в прошлом (4-м) прогоне
# сегодня в 18:08 apartment-страницы были доступны, но давали только посреднические
# "rổ hàng"/"chuỗi" объявления в целевых районах — маловероятно, что за ~1.5 часа появилось
# что-то новое и при этом непосредническое.
#
# Facebook Marketplace/группы: как обычно недоступен в headless-окружении (редирект на логин).
NEW_SRC = r'''
L(939,"ho-chi-minh","th","Дом",15000000,100,
  "Дом целиком (5×20-22м, 2 спальни, 2 с/у) на ул. Lâm Văn Bền, Tân Hưng, Q7. Подходит для жилья или под небольшой офис. Витринная дата API вводила в заблуждение (repush) — использован честный orig_list_time (~2 дня).",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134196586.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nguyễn Hoa"}),

L(940,"ho-chi-minh","tm","Квартира",14000000,65,
  "2-спальная квартира (2 с/у) в River Panorama, Tân Mỹ (Phú Mỹ Hưng), Q7. Средний этаж, светлый вид, полная меблировка, готова к заселению.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/131760231.htm","2 часа назад",0,source="chotot",
  details={"contact":"BDS Premium Sky (Minh Thành)"}),

L(941,"ho-chi-minh","tm","Дом",45000000,140,
  "Вилла в закрытом комплексе Green Star Hưng Lộc Phát рядом с Phú Mỹ Hưng, Tân Mỹ, Q7. Участок 7×20м (140м²), 1 этаж + 2 верхних, ориентация СЗ, документы HĐMB.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134238016.htm","2 часа назад",0,source="chotot",
  details={"contact":"Xuyến Liễu"}),

L(942,"ho-chi-minh","tm","Дом",12500000,48,
  "Дом целиком (1 этаж+1 этаж, 4×12м, 2 спальни, 3 с/у) в переулке ул. Nguyễn Thị Thập рядом с рынком Tân Mỹ, Q7. С мебелью, подходит под жильё или небольшой офис.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133909291.htm","10 часов назад",0,source="chotot",
  details={"contact":"LHP"}),

L(943,"ho-chi-minh","tm","Дом",7200000,25,
  "Дом целиком (1 этаж+1 этаж, гостиная, 2 спальни, с/у, кухня) в широком переулке для машины, 730 Huỳnh Tấn Phát, Tân Mỹ, Q7. Рядом супермаркет GO! (бывший Big C) и рынок. Приоритет длительной аренде.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134228666.htm","9 часов назад",0,source="chotot",
  details={"contact":"Tuấn Anh Land"}),

L(944,"ho-chi-minh","ak","Квартира",25000000,72,
  "2-спальная квартира (2 с/у, 71,6м²) в ЖК De Capella, 116 Lương Định Của, An Khánh (Thảo Điền), Thủ Đức. Полная меблировка. Ward подтверждён геокодингом адреса.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134233963.htm","5 часов назад",0,source="chotot",
  details={"contact":"Lê Thanh Trung"}),

L(945,"ho-chi-minh","ak","Квартира",16000000,75,
  "2-спальная квартира с дизайнерским ремонтом в Masteri Thảo Điền, An Khánh, Thủ Đức. Высокий этаж, вид на реку.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/126685241.htm","5 часов назад",0,source="chotot",
  details={"contact":"Phương Nhi"}),

L(946,"ho-chi-minh","kh","Квартира",17000000,77,
  "2-спальная квартира (самая большая 2BR-планировка в комплексе) в Millennium на ул. Bến Vân Đồn, Khánh Hội, Q4. Высокий этаж, вид на Bitexco.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/126278417.htm","5 часов назад",0,source="chotot",
  details={"contact":"Phương Nhi"}),

L(947,"ho-chi-minh","kh","Студия",5500000,35,
  "Студия с отдельной кухней (без запаха от соседей), своей стиральной машиной и большим окном, у моста Calmette (Bến Vân Đồn), Khánh Hội, Q4 — рядом Q1/Q3/Q10. Свободный график, без совместного проживания с хозяином. Цена за 1 чел. — 5,5 млн ₫, за 2 чел. — 7,5 млн ₫.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/132262424.htm","21 час назад",0,source="chotot",
  details={"contact":"Duy Khoa Neway","occupancy_price":"1 чел. — 5,5 млн ₫, 2 чел. — 7,5 млн ₫"}),

L(948,"ho-chi-minh","bth","Студия",6400000,30,
  "Студия с отдельной кухней на ул. Phạm Ngũ Lão, Bến Thành, Q1 (между Bùi Viện и парком 23/9), 5 минут пешком до метро Bến Thành.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134226838.htm","10 часов назад",0,source="chotot",
  details={"contact":"Huỳnh Kỳ Đức"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted daily HCMC check 19 aug 2026 (5th pass): 10 listings (chotot) across "
      "th/tm/ak/kh/bth; batdongsan not re-checked this pass (budget spent on deep chotot sweep); "
      "facebook inaccessible as usual")
