# -*- coding: utf-8 -*-

NEW_SRC = '''
L(1370,"ho-chi-minh","bth","Студия",5900000,35,
  "Студия с большим окном на ул. Lý Tự Trọng, Bến Thành (Q1), у рынка Chợ Bến Thành — полная меблировка, вход по отпечатку пальца, фасад улицы, парковка у дома.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134320741.htm","сегодня",0,source="chotot",
  details={"contact":"Đỗ Toán HiFriendz","photos":["https://cdn.chotot.com/MpbROuCgFMCwpwA4waQW9f8pFAhXpaiW9NjwKYfLtZk/preset:view/plain/cbb03fe2079879f3ef9bd0d673756e7d-2998993294404438924.jpg","https://cdn.chotot.com/FfJU18mKBn-1khpazLTHSHcUer1h-3zmjUT_NqsZG-E/preset:view/plain/0c7f24c8a8253d8bde903535f4ee5f3e-2998993294741370597.jpg"]}),

L(1371,"ho-chi-minh","bth","Дом",15000000,23,
  "Дом целиком в переулке ул. Phạm Ngũ Lão, Bến Thành (Q1) — участок 3,5x8м (23м²), 1 этаж + 2 этажа + терраса, 2 спальни, 3 с/у, новый ремонт, полная меблировка, рядом Q5/Q3/Q10.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/133740133.htm","1 день назад",1,source="chotot",
  details={"contact":"Thế Hạo","photos":["https://cdn.chotot.com/wQemd8HJZjMI5QCRF4QZZyni9zUdQpZ_kOZ5UBw8-yA/preset:view/plain/bdb5049da526dcdfa7f0dba5f1a34d39-2994571543749393139.jpg","https://cdn.chotot.com/aaduArNRKTbE0gccTqkaVladkEav-D4G3GyxAk6xAfE/preset:view/plain/84d02bf177855616918aa67903c480f4-2994571543691580272.jpg"]}),

L(1372,"ho-chi-minh","kh","Студия",14000000,35,
  "Студия в ЖК Millennium, Khánh Hội (Q4) — 35м², полная меблировка, несколько минут до Q1, бассейн, спортзал, охрана 24/7, паркинг.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134315424.htm","1 день назад",1,source="chotot",
  details={"contact":"Lâm Hậu","photos":["https://cdn.chotot.com/emjL4tfo5Cwqtf-r3g2nuiW-qi-IleiGzi8VKFtPQtw/preset:view/plain/be180766b4444428ae70075b2c116005-2998920837819326684.jpg","https://cdn.chotot.com/jIr9i4Z7Pit7GorzONgp3An_8K2tApJ3UTGH0roFHeY/preset:view/plain/a2eff0e30c127d894dfb72848b3b5935-2998920839233081922.jpg"]}),

L(1373,"ho-chi-minh","kh","Дом",11000000,22,
  "Дом целиком на ул. Đoàn Văn Bơ, Khánh Hội (Q4) — участок 3,2x7м (22м²), 2 спальни, 3 с/у, свободен с 16 августа.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134322631.htm","сегодня",0,source="chotot",
  details={"contact":"Huy Nguyễn","photos":["https://cdn.chotot.com/svwQBATcN88dZweUDfqJWCzf_0_hvq4isnEg_rzNpMc/preset:view/plain/d07e88c37987d7fb9877159f5a20d1c6-2998999544571317132.jpg","https://cdn.chotot.com/HYE88k_xFuS4kOOe4CDblLzDmoxboXZLhu1MswK4yZI/preset:view/plain/7fef4e8992a089f77fd985bf3bef2074-2998999544717223955.jpg"]}),

L(1374,"ho-chi-minh","kh","Дом",13000000,35,
  "Дом целиком, Khánh Hội (Q4) — участок 3,3x10м (35м²), 1 этаж + 2 этажа + терраса, 3 спальни, 2 с/у, полная меблировка (3 кондиционера, стиральная машина), рядом Q1.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134320990.htm","сегодня",0,source="chotot",
  details={"contact":"Đông Thiên","photos":["https://cdn.chotot.com/uIWHW92gZg_uwAKOtFsOG0fu0wVcfzOsKcXb1sGA3Fk/preset:view/plain/59b03344f88515694f72d90b415b4c3f-2998994151044696972.jpg","https://cdn.chotot.com/1edpOnV2sCa8jxgnQzp4IlNoA8DNklGa1vxakqwNyd4/preset:view/plain/d85417fab9a87285fab6fb6114b6ded3-2998994150921867343.jpg"]}),

L(1375,"ho-chi-minh","kh","Комната",3000000,22,
  "Комната-мансарда с окном и отдельным двориком, Khánh Hội (Q4) — 22м², без мебели, электричество 5 тыс ₫/кВт, вода 100 тыс ₫/чел.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134311370.htm","1 день назад",1,source="chotot",
  details={"contact":"Vy","photos":["https://cdn.chotot.com/uP0EOEwK95qJYemMWjEda4Dw864caLjXnWPL9yZ3d1g/preset:view/plain/45d5b28425039c1371fa26c87cc57d26-2998889384092623068.jpg","https://cdn.chotot.com/ZHxRRkmOK9PIZQ5YFfsgsyhfjs2tm0hQLge1HG1YM_s/preset:view/plain/4a36c39abd243560e5f0e04d554f17df-2998889384523368274.jpg"]}),

L(1376,"ho-chi-minh","kh","Дом",11000000,24,
  "Дом целиком, Khánh Hội (Q4) — участок 3x8м (24м²), 1 этаж + мезонин + 1 этаж + терраса, 2 спальни, 3 с/у, рядом рынок Xóm Chiếu, мост Khánh Hội, университеты Luật и Nguyễn Tất Thành.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134307060.htm","1 день назад",1,source="chotot",
  details={"contact":"Đặng Trung Hậu","photos":["https://cdn.chotot.com/iSTpeA0FqoXGq8JNspHjBHRB-7XP7nWaVYBo43S5c6Y/preset:view/plain/7e1d40f2d66f06832350f03fa0066d3d-2998864718030809371.jpg","https://cdn.chotot.com/GIA0wl0E2n4DY776z-ebxJZ_L6SK3oGM_6k5_1eowqw/preset:view/plain/cd8b8dc5f3d51125a1654359f29216a0-2998864718112421418.jpg"]}),

L(1377,"ho-chi-minh","tm","Квартира",11500000,92,
  "3-спальная квартира (2 с/у), 92м², угловая с видом на реку, ЖК Era Town Đức Khải, Tân Mỹ (Q7) — полная меблировка, бассейн, спортзал, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134323259.htm","сегодня",0,source="chotot",
  details={"contact":"Loc Phan","photos":["https://cdn.chotot.com/hokfUKMelYZwy4DhDaX77tOVCtXhAYJRJJlpwBKGj2A/preset:view/plain/e2f8318608cd3f38d01b9b855143cc03-2999001894875913990.jpg","https://cdn.chotot.com/HqeKjmOWXfndzmmmNcLPaOKUEB7ecMNBzmEHeBZL9V0/preset:view/plain/07a5019d9bd80d2dd149422af1bdec93-2999001895432957383.jpg"]}),

L(1378,"ho-chi-minh","th","Студия",5400000,30,
  "Просторная студия с балконом, 30м², ул. Lê Văn Lương, Tân Hưng (Q7) — полная меблировка, лифт, паркинг, рядом TDTU/Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133239075.htm","сегодня",0,source="chotot",
  details={"contact":"Nhân Bùi","photos":["https://cdn.chotot.com/mYeo1bvEcHRufro2K1QYhSnje6rzI-wqzpXzoOwQJRE/preset:view/plain/b6fd16b78fd2da4cb179592246098133-2990759507291738271.jpg","https://cdn.chotot.com/hGeHfnZAjbDjQ25aTmNyh86wdpac0eUvd2AKa0PcDbM/preset:view/plain/5455db6a66c882ae816e35d37fac986d-2990759507350378830.jpg"]}),

L(1379,"ho-chi-minh","th","Студия",6000000,35,
  "Студия, напротив RMIT/TDTU/Lotte Mart/SC VivoCity, Tân Hưng (Q7) — полная меблировка (Smart TV, кондиционер, холодильник), можно с животными, депозит 1 месяц, охрана и камеры 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134309572.htm","1 день назад",1,source="chotot",
  details={"notice":"цена варьируется по типу окна: 6 млн (обычное окно) / 7,6 млн (с балконом)","contact":"Nguyễn Từ (CHDV Q7)","photos":["https://cdn.chotot.com/k7wBOseF6Cs_UyXicwKgi-6agbcSpRAhYuv5sceCNZw/preset:view/plain/4e98e7fc8da185eab26faff9edb801e7-2998879570211173930.jpg","https://cdn.chotot.com/OZsTGOcLV7cUwQQogD_rvso0jM6bvAyP7wK5fV1IjYY/preset:view/plain/9604d3cdb2df7e1f59c53ea049293217-2998879569953436057.jpg"]}),

L(1380,"ho-chi-minh","tm","Дом",20000000,64,
  "Дом целиком (1 этаж + 3 этажа), переулок ул. Huỳnh Tấn Phát, Tân Mỹ (Q7) — участок 4x16м (64м²), 3 спальни, 3 с/у, полная меблировка, подходит и под небольшой офис/интернет-магазин.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134319649.htm","сегодня",0,source="chotot",
  details={"contact":"LHP","photos":["https://cdn.chotot.com/AVa7QXzbZVDS-ylqKwW8y_nhvZx65cK17IgIVERnat8/preset:view/plain/b98ba7653de06619b8e78534d75055ce-2998989206928565261.jpg","https://cdn.chotot.com/ownU6sRftwJ8UkijRth2SsSh4SUHzxKdp1dD6gncYNQ/preset:view/plain/fefe2a1440d27920b6821e0197691bbc-2998989206681547542.jpg"]}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content

new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
assert new_content != content
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", NEW_SRC.count("L("), "listings")
