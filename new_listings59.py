# -*- coding: utf-8 -*-

NEW_SRC = '''
L(1399,"ho-chi-minh","bq","Студия",6500000,45,
  "Студия в доме Tiến Lân Apartment, ул. Bình Quới, Bình Quới (Thanh Đa) — 45м², 1 спальня, окно, тихо, лифт, водонагреватель на солнечных батареях, спортзал, прачечная, фильтр воды, Wi-Fi, рядом Landmark 81 и Thảo Điền.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-binh-thanh-tp-ho-chi-minh/134315847.htm","сегодня",1,source="chotot",
  details={"notice":"в карточке указана цена 6,5 млн ₫/мес, но в тексте объявления также встречается «Studio B301 – 9 млн ₫/мес» (похоже на описание другого юнита в этом же доме) — указана официальная цена карточки объявления.","contact":"Tiến Lân Apartment","photos":["https://cdn.chotot.com/Cup0UHpcDo9Z7icxMay4Bw4jcJ1nld2WdLIU53JPyu8/preset:view/plain/94abd55b9c203154e137de2432530493-2998925054659872455.jpg","https://cdn.chotot.com/v29YZ83BiIHrEhwA3lbUGeC5h6VXuZEce7oH056X5YQ/preset:view/plain/8b884704b1610372887ac76a8132dda4-2998925054830522615.jpg"]}),

L(1400,"ho-chi-minh","th","Квартира",12000000,65,
  "2-спальная квартира (1 с/у), 65м², ЖК M-One Nam Sài Gòn, ул. Bế Văn Cấm, Tân Hưng (Q7) — полная меблировка, залог 24 млн ₫, реальные фото без прикрас.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134307339.htm","1 день назад",1,source="chotot",
  details={"contact":"Võ Tấn Hùng","photos":["https://cdn.chotot.com/h3VM2XPJDJ6tbEurfkopMHAKEGrb1TuWvoAycnRViRs/preset:view/plain/98e70b299bd9eff00864c791020e0297-2998866615736697427.jpg","https://cdn.chotot.com/MbjiV1w1oOpUEf49ikPqlrcQgHsYQJF3fYhea9S2NZc/preset:view/plain/652398621fdcda8df4fc599a3cb890d0-2998866615802000938.jpg"]}),

L(1401,"ho-chi-minh","ak","Студия",8800000,35,
  "Студия/1-спальная квартира индивидуальной планировки, 35м², ул. Trần Não, An Khánh (Thảo Điền/An Phú) — в квартале вилл, много зелени, полная меблировка, вход по отпечатку пальца, свободный график, рядом мост через Sài Gòn и туннель Thủ Thiêm. Залог 8,8 млн ₫.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thu-duc-tp-ho-chi-minh/131731670.htm","2 дня назад",2,source="chotot",
  details={"contact":"Quỳnh Như HiFriendz","photos":["https://cdn.chotot.com/vNd4tcGQgaDX7qc7bYipB2o6292jjlnzW2UimWrzO5U/preset:view/plain/615348a095cb7a4ba7bdfab8587dda1a-2979264075986461222.jpg","https://cdn.chotot.com/gFIABRA-lQbsm0npQVnqpTabGbN4UT7qHRvYp2TnUWo/preset:view/plain/0872b2e832da34a3239aa7e5c58c71ad-2979264076607283750.jpg"]}),

L(1402,"ho-chi-minh","th","Дом",15000000,60,
  "Дом целиком в переулке 118, ул. Nguyễn Thị Thập, Tân Hưng (Q7) — участок 4x15м (60м²), 1 этаж + 2 этажа, 2 спальни, 3 с/у, новый ремонт, полная меблировка. Рядом перекрёсток Nguyễn Văn Linh, университет Marketing, Lotte Mart, рынок Tân Mỹ (~100м), КПЗ Tân Thuận, выставочный центр Phú Mỹ Hưng. Цена договорная для добросовестных арендаторов.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-thi-thap-phuong-tan-hung-14-59/heart-heart-cho-can-hem-118-ep-moi-full-noi-that-pr46204765","4 дня назад",4,source="batdongsan",
  details={"notice":"дата размещения по данным страницы объявления (Ngày đăng): 20.08.2026 — как и на других объявлениях Batdongsan, это может быть датой обновления/переразмещения, а не гарантированно первой публикацией. Цена 15 млн ₫ подтверждена дважды — в карточке выдачи и в блоке «Khoảng giá» на странице объявления.","contact":"Ngọc Trang","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/20/20260820095356-2f5a_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/20/20260820095356-f27f_wm.jpg"]}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content

new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
assert new_content != content
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", NEW_SRC.count("L("), "listings")
