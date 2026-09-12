# -*- coding: utf-8 -*-
"""Chợ Tốt, автоматический сбор: 16 объявлений, 2026-09-12.

Партию собрал collect_chotot.py -- без модели в контуре. Район взят точным
совпадением ward_name_v3 с CITIES, описание собрано из полей объявления, а не
пересказом текста продавца, возраст не больше 10.0 дней по orig_list_time.

Объявления, район которых не совпал ни с одним нашим, пропущены, а не приписаны
к соседнему -- в этом и разница с тем, как это делала сессия.
"""
from listing_lock import insert_listings

IDS = [1002626, 1002627, 1002628, 1002629, 1002630, 1002631, 1002632, 1002633, 1002634, 1002635, 1002636, 1002637, 1002638, 1002639, 1002640, 1002641]

N_RU = "Описание собрано программой из полей объявления на Chợ Tốt — тип, комнаты, площадь, улица, район, удобства по ключевым словам. Рекламный текст продавца не пересказан, названия районов оставлены вьетнамскими. Подробности смотрите по ссылке."
N_EN = "This description was assembled by a program from the ad's own fields on Chợ Tốt — type, rooms, size, street, ward and amenities matched by keyword. The seller's marketing copy is not retold and ward names are left in Vietnamese. See the source for the rest."

NEW_SRC = r'''
L(1002626,"hai-phong","hbg","Дом",3000000,47,
  "3-спальный дом, 47 м², ул. Tôn Đức Thắng, Hồng Bàng, Хайфон — 2 санузла.",
  "https://www.nhatot.com/thue-nha-o-quan-hong-bang-hai-phong/134632358.htm","вчера",1,source="chotot",
  descEn="3-bedroom house, 47 m², Tôn Đức Thắng, Hồng Bàng, Hai Phong — 2 bathrooms.",
  details={"photos": ["https://cdn.chotot.com/5QCCczHZVpX9Aom5ScuYyzhDFn77nGu3tH2zbjqYGzk/preset:view/plain/3591ee7d0de9d4c91ca7236b359abe1c-3001618713686569582.jpg", "https://cdn.chotot.com/tUhpCItIa7yIaaSAEbHEhvt3svlywWCLCnEX1if9vlQ/preset:view/plain/7d2a78f3a6aac5cdaa4bdd48f1fcf361-3001618713199563240.jpg", "https://cdn.chotot.com/XwN60Ciky3Ex2S6lCfcNRsQdCBHJseos9ahqCevFr4w/preset:view/plain/313bda402e789f92fc4bf99c94a853e7-3001618717037038260.jpg", "https://cdn.chotot.com/RVfWqQlrB-NJs784IvvFrDOImN6_emPrIebtgCmnsWE/preset:view/plain/8123f955278a9f40e3339f8ec928dcd0-3001618717755292813.jpg", "https://cdn.chotot.com/tJ5x-eL3FWPKk2JYop6jagQUZprRhHljKJBQih00sms/preset:view/plain/c830e23b1bfbec2cefbcb2fb40ebfb9a-3001618719641170894.jpg", "https://cdn.chotot.com/k3Tuh52YRoOA8lf7uQbtbdH5N1WgW58AEeKPuswv16s/preset:view/plain/a9da66d5905d50647a7dfd4f8d4c1195-3001618720859208845.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002627,"hai-phong","gvi","Квартира",10000000,66,
  "2-спальная квартира, 66 м², ул. Cầu Đất, Gia Viên, Хайфон — 2 санузла.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngo-quyen-hai-phong/134617749.htm","вчера",1,source="chotot",
  descEn="2-bedroom flat, 66 m², Cầu Đất, Gia Viên, Hai Phong — 2 bathrooms.",
  details={"photos": ["https://cdn.chotot.com/46Nrbour_Zp6phM0wE-xFbT8DWqwmLL50IEjzbiExHY/preset:view/plain/4c673ff0788fbf33633f1218340254db-3001489164579645527.jpg", "https://cdn.chotot.com/K12xOtS5ateFUrNlg9mRtPvc_4SK8VrNqx7W81by3es/preset:view/plain/cfb173da91a8dfbfdc7c12ce6b1e7c96-3001489164643830672.jpg", "https://cdn.chotot.com/DFP0H9SxCQpntz5WXf0qGtpbD3NcgJz0Wihjrf5l_N0/preset:view/plain/103be820ea9829ff81e430f244730eba-3001489164674665140.jpg", "https://cdn.chotot.com/5q1-A7_UwtMVqCZLDfIs6JihNSBqTBs3Rzsk3eSv5X0/preset:view/plain/6501b941257d8f519f44fc809731c1bf-3001489164725439331.jpg", "https://cdn.chotot.com/Y3Th4TeV1frgdspFOXywvxNAjjp4LmQcUrnDoids51M/preset:view/plain/4caa46498f5dad5041781be13b628e85-3001489164904759684.jpg", "https://cdn.chotot.com/QaQMDf8AH4LA5ucJGuRgNSQkb_EoyiC2SVT3d8QvuwQ/preset:view/plain/15ff9dc14bcc5f617a5d4db8cd7b5029-3001489164816097496.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002628,"hai-phong","anb2","Квартира",6500000,40,
  "1-спальная квартира, 40 м², ул. Võ Nguyên Giáp, An Biên, Хайфон — 1 санузел, полная меблировка, лифт, парковка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-le-chan-hai-phong/134620186.htm","вчера",1,source="chotot",
  descEn="1-bedroom flat, 40 m², Võ Nguyên Giáp, An Biên, Hai Phong — 1 bathroom, fully furnished, lift, parking.",
  details={"photos": ["https://cdn.chotot.com/4wi3trW2ABs2JnxksFvHLIG9A_0O650krgnR-mLe_Ao/preset:view/plain/379c77c874e821eef06c8581b5ccb453-3001500154751586722.jpg", "https://cdn.chotot.com/dxJb2nk4ug7DLi5a5ZUqjZTFSnVE_8pub4tDOKQDous/preset:view/plain/0ddf728a048151d4f7b54b65aaa2cb77-3001500154616875700.jpg", "https://cdn.chotot.com/iAGnujL-NR-CHy-MT_3oVV1vQGPKndPBvHRuHMAyshE/preset:view/plain/60d63e034567bf16368e01c3260ebe24-3001500154655875288.jpg", "https://cdn.chotot.com/eFQUawAKJ3m3DAaFKjp9Q18lDBOho4cFukrxOTuxaV0/preset:view/plain/add9835057a7f91abf5e049e53a6f75a-3001500154567183203.jpg", "https://cdn.chotot.com/FHPX8Us8H-NnmJm7FaISbNf5RCFQ0-gCBWLLhhLN49g/preset:view/plain/faf2f878ab8bc13f9c01808b6b3d08ba-3001500154597488078.jpg", "https://cdn.chotot.com/jo6ocqd-iWNBRngc4L7-wHa12W0ZWJ3iNvrwEQKivGQ/preset:view/plain/36557cdc4ff171cf8c9f86c6ce1a217f-3001500182943887982.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002629,"hai-phong","anb2","Квартира",11000000,80,
  "2-спальная квартира, 80 м², ул. Võ Nguyên Giáp, An Biên, Хайфон — 1 санузел, полная меблировка, кондиционер, балкон, лифт.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-le-chan-hai-phong/134229221.htm","вчера",1,source="chotot",
  descEn="2-bedroom flat, 80 m², Võ Nguyên Giáp, An Biên, Hai Phong — 1 bathroom, fully furnished, air conditioning, balcony, lift.",
  details={"photos": ["https://cdn.chotot.com/gCjnfzEzLS8TCmuF7tSKjsyi1O9W377jhgyxvgcCbHo/preset:view/plain/f1cecc048797599cc96df08818d5f8f9-2998277202100089745.jpg", "https://cdn.chotot.com/IGmUMRlLW1XfLrNMO7lggrqE1qLUWWnhxN3feQy9yvo/preset:view/plain/64a74cdaec534c70f907d95d03ac00ce-2998277202349317235.jpg", "https://cdn.chotot.com/9Btos9EDIOPNSzKOrx7BbBAuN5fDHcY_LxapTK64Zn8/preset:view/plain/5fd7c57c0adb1c36c6f89d3bc2e7bce4-2998277202061236178.jpg", "https://cdn.chotot.com/VNPKc-1GUf2T-H1zJv1j6xW7fbId2piFkJehn2E-vDU/preset:view/plain/93f5db8075a1d210ca68e1875100434b-2998277202181538297.jpg", "https://cdn.chotot.com/J-k7YJNhL-sS7wplUkPqXbfSMkQjyl1is7lltI1GHhw/preset:view/plain/eb3e991f6976e870b43f0d571d4a6f4f-2998277202524504217.jpg", "https://cdn.chotot.com/0U8KDMGiMDAdN0_QICketwLsDWoUtiTGQpLGPHZV2Nk/preset:view/plain/7d54aec6b76ddb3a342b65d4a15ce9f2-2998277202306241905.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002630,"hai-phong","gvi","Квартира",12000000,56,
  "1-спальная квартира, 56 м², ул. Lê Hồng Phong, Gia Viên, Хайфон — 1 санузел, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngo-quyen-hai-phong/134609047.htm","2 дня назад",2,source="chotot",
  descEn="1-bedroom flat, 56 m², Lê Hồng Phong, Gia Viên, Hai Phong — 1 bathroom, fully furnished.",
  details={"photos": ["https://cdn.chotot.com/VFjCZJZwMTsfrExDlNIgkX5dZ7qJuykz6rP33E7gV9g/preset:view/plain/dd2d574a3d9f6a5879c2f036b36a9c2f-3001448808672785006.jpg", "https://cdn.chotot.com/JMIbzw1yxjqLnV0kPxoYd1euSrDkWbe_jHoGQNsdW3k/preset:view/plain/8b4a6c44ba1c0b2a523839710c84e65f-3001448808507050676.jpg", "https://cdn.chotot.com/cPeF3hxZ5fn_2Pt2U0y5h3Ol5TIg6ttL2NQwIgzG7_s/preset:view/plain/460a19800cd60c287c81465e5ccf63f9-3001448808705723280.jpg", "https://cdn.chotot.com/Bdw3lwgvbajq8jWaR9QERcA5KWXbZ51SVONq6Bd3Ijk/preset:view/plain/fc85e2729ebe8a07013f631c10d09075-3001448808649392516.jpg", "https://cdn.chotot.com/NMJ60FWHO-imDQAMJ0Rag-LW4CK1n42wL_hseJ4GK1E/preset:view/plain/f4ffbe3e9206f55cf70bd55772cf0b57-3001448808432541912.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002631,"hai-phong","anb2","Квартира",13000000,71,
  "2-спальная квартира, 71 м², ул. Minato Residence, An Biên, Хайфон — 2 санузла, спортзал, стиральная машина.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-le-chan-hai-phong/134609453.htm","2 дня назад",2,source="chotot",
  descEn="2-bedroom flat, 71 m², Minato Residence, An Biên, Hai Phong — 2 bathrooms, gym, washing machine.",
  details={"photos": ["https://cdn.chotot.com/WDsS3av1oPH73j-Urk0N4wEBEwFC2WRP_hpb7L0Uo9E/preset:view/plain/b1d1a76e4b90b121521e4b563bea205f-3001451682926883438.jpg", "https://cdn.chotot.com/lRbhXsJDiB-_0Qz0QEeYF3ESPC9xGf-n4O5Uejw8_2g/preset:view/plain/577bcc778efae36fef26ff477076004b-3001451683180219280.jpg", "https://cdn.chotot.com/4QSB7-c-fKjMj_1TW6sXJdNXEDtkRreDQ1pX6PCV23o/preset:view/plain/5db72692e905c53959d50adf19c32869-3001451683144810328.jpg", "https://cdn.chotot.com/goJYbmpsYceriqb6c_zQ-M-2KkpE4KPLdqQyLi6Htxc/preset:view/plain/f9de47746ab388d430151b85dbbbdab6-3001451682938298584.jpg", "https://cdn.chotot.com/X5tTw2BIWY4xSt-kYhg70lAEcWEUtxyQAww8CNJQSmg/preset:view/plain/768c76cc5e5f096c77451910d983645c-3001451683129408789.jpg", "https://cdn.chotot.com/M_uuGPmz38DamgoPHp1sBNYShSxavwEupymggnCHxTs/preset:view/plain/716cd28ac5a48835c4987206ea036e82-3001451683120452002.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002632,"hai-phong","hbg","Комната",2000000,40,
  "Комната, 40 м², ул. Phố Cam Lộ, Hồng Bàng, Хайфон — базовая меблировка, кондиционер.",
  "https://www.nhatot.com/thue-phong-tro-quan-hong-bang-hai-phong/134586821.htm","3 дня назад",3,source="chotot",
  descEn="Room, 40 m², Phố Cam Lộ, Hồng Bàng, Hai Phong — basic furniture, air conditioning.",
  details={"photos": ["https://cdn.chotot.com/LhN4rycpAvkSmIm4E1z_6VDAnMZJ-0729dKIo-B-UCg/preset:view/plain/76ab60bf13599197e3593087c31e7370-3001233650184728417.jpg", "https://cdn.chotot.com/ZJIg2jQa5AHNxzq-w-k5lQ8iGYV2xPc0UplbmGBI_bg/preset:view/plain/9034f14365ece71776b53bcad3e7a025-3001233650634318766.jpg", "https://cdn.chotot.com/7mx4xJ-AumnoL_-dm6jo5QFV6RffPDL90R3cSnFUbT4/preset:view/plain/dbebdef861dd05c395dfd2a9d8431ffd-3001233649944316922.jpg", "https://cdn.chotot.com/9cTqtij52ho-DmNf5XLq1L8c59IqaIFAgHKheXibuEY/preset:view/plain/b5830c50e20e14718912cc0465cdb348-3001233650792113174.jpg", "https://cdn.chotot.com/aITHtGIwsWn3oBApwh1p2Rl3ajz2UirigN27DGMEPKc/preset:view/plain/223a1670a856ad873d9de62b4fa8c31c-3001233650690888222.jpg", "https://cdn.chotot.com/-cbR-w8q-6BCisbeRsPywYH3E5z4Jo-LYyg2C-eeQ_M/preset:view/plain/b2bf188e3d6e51045187db397390f00b-3001233650511888006.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002633,"hai-phong","anb2","Квартира",6000000,37,
  "1-спальная квартира, 37 м², ул. Võ Nguyên Giáp, An Biên, Хайфон — 1 санузел, балкон, лифт, парковка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-le-chan-hai-phong/134584583.htm","3 дня назад",3,source="chotot",
  descEn="1-bedroom flat, 37 m², Võ Nguyên Giáp, An Biên, Hai Phong — 1 bathroom, balcony, lift, parking.",
  details={"photos": ["https://cdn.chotot.com/i7YziNstPIrtDDD2fsulRl9l3-iLWKDHSj9P7T35X_4/preset:view/plain/3c12a23809849000ed34a44bcef51449-3001217336349706424.jpg", "https://cdn.chotot.com/HdTyzvK7askWVPxWT3hNekkBL1WTHUPNNVxn8_vg3II/preset:view/plain/511f02813234b2b9dfefed6dd2c63fcb-3001217335686390702.jpg", "https://cdn.chotot.com/14T6flgRGrhXvNwWio2H_qfIn6CNT6AnEDxXaiwckgc/preset:view/plain/2bf11d1e46375ce8872ce020df762147-3001217336082391347.jpg", "https://cdn.chotot.com/QAOa8xHyO5oWfmAAc5kgfjGhaBF5TomDVq1h7-S-6Ow/preset:view/plain/f9a8dc6e573e6830a781cb21b8ae620f-3001217335884976670.jpg", "https://cdn.chotot.com/ILzPwYuqQFUN1nbBqs1bRR8nq_5Qx5xeBsR9HLJyx2A/preset:view/plain/7d57be7d5428190160d3510459f3ddbd-3001217336186063866.jpg", "https://cdn.chotot.com/LRbkbfo7BoJShfipztwseUdIM4Pj1ivavyKcocc6jKU/preset:view/plain/62d99f007590f5c7eb2022a8ef9214c4-3001217336012816006.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002634,"hai-phong","nqu","Квартира",2000000,30,
  "2-спальная квартира, 30 м², ул. Đà Nẵng, Ngô Quyền, Хайфон — 2 санузла.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngo-quyen-hai-phong/134562713.htm","4 дня назад",4,source="chotot",
  descEn="2-bedroom flat, 30 m², Đà Nẵng, Ngô Quyền, Hai Phong — 2 bathrooms.",
  details={"photos": ["https://cdn.chotot.com/t56x2cBnF-X3eGjW-Z8yFNKU_AoyyMJPnItI8n-eRXg/preset:view/plain/a218fa55b300e51f10985ac80e40306e-3001065112598435894.jpg", "https://cdn.chotot.com/cDugo7IK6sD_bv1nyDy2Yasjjtd75wbePYXUsjHAFDY/preset:view/plain/f6b44f8af1d030013578ada770856ad1-3001065112469496750.jpg", "https://cdn.chotot.com/FDuVaZeOEknQ0X_0AuI3ACt9fjAZiJrrhMZcL9EZI24/preset:view/plain/312ae2b10666b91d9d9b9906c7c21191-3001065112895758767.jpg", "https://cdn.chotot.com/DQy2whrJNj7akTZdyAUQJHHSPwLgditUkJl9GyiM-8Y/preset:view/plain/e195c141dcd4acbd8c265ef9c4460b05-3001065113178160767.jpg", "https://cdn.chotot.com/NDovC6KGKPgu501tq9fhkaOnJSMCpZ2pF9dflILuWOw/preset:view/plain/6a067c7aa2ab9bc03036d86a13e48433-3001065112300651732.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002635,"hai-phong","gvi","Квартира",16000000,80,
  "1-спальная квартира, 80 м², ул. Phố Lạch Tray, Gia Viên, Хайфон — 1 санузел.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngo-quyen-hai-phong/134549124.htm","5 дней назад",5,source="chotot",
  descEn="1-bedroom flat, 80 m², Phố Lạch Tray, Gia Viên, Hai Phong — 1 bathroom.",
  details={"photos": ["https://cdn.chotot.com/n1rp9rLm90UNSQBUmTa4FyoPTNAwZ7UyFniJDwIeC6Q/preset:view/plain/86d93527d33e85ba4e2fd1dea8041c09-3000954936872093303.jpg", "https://cdn.chotot.com/DReeUMqpmN5umitqYKZV6gWF8XmrgrMCQZBmJKQxRcg/preset:view/plain/3adbe0e66b226a92a96e3b7ad7599da5-3000954936645741978.jpg", "https://cdn.chotot.com/u2suo2KG5nKBaOf9h_pSYzpX2TgWzeVqYRfpXENS2dE/preset:view/plain/8c7b230fee0bf30f054e8ff92d3df777-3000954939204191863.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002636,"hai-phong","anb2","Квартира",7000000,35,
  "1-спальная квартира, 35 м², ул. Võ Nguyên Giáp, An Biên, Хайфон — 1 санузел, балкон, лифт, парковка, стиральная машина.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-le-chan-hai-phong/133924348.htm","5 дней назад",5,source="chotot",
  descEn="1-bedroom flat, 35 m², Võ Nguyên Giáp, An Biên, Hai Phong — 1 bathroom, balcony, lift, parking, washing machine.",
  details={"photos": ["https://cdn.chotot.com/Arc--U1CZ6HjPPZXYnlQ5IWaB0QdILYh12ZZfco-HkA/preset:view/plain/72c79521763c4b1a61ebbc10d0807d40-2995994242143984250.jpg", "https://cdn.chotot.com/l-8Wrkrhd7dH3xCkTp54zcGXCzrzJ4fjPEI8Yn96iVk/preset:view/plain/c070539fe9b0ff719cfc3557da388fb4-2995994242313999359.jpg", "https://cdn.chotot.com/sZOnXh5J5QAsXjda65sRx0BFImx-DwBnekYBMESy4wc/preset:view/plain/fecc0580409c178961a71f1e0f6a5e5a-2995994241901809639.jpg", "https://cdn.chotot.com/tUP4p6xKXihv94PiCRJgExfhGxwAMiy30TAdr-YZnx8/preset:view/plain/091243c145143fb73d098cecd13f7013-2995994242114141289.jpg", "https://cdn.chotot.com/yDRtTZl0Z1jG0MPNQXnhA55OvZXyosslU717HJmFY0g/preset:view/plain/a8d3ec8cdac80fa6995b15b8bd8635cc-2995994241768319768.jpg", "https://cdn.chotot.com/nzlWrnuqOgD0yP1Pwowy6daUiCjvBSwjvHRHDGRbmyc/preset:view/plain/570b34bb47a0359393a90e6721255017-2995994241692158329.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002637,"hai-phong","anb2","Квартира",5500000,35,
  "1-спальная квартира, 35 м², ул. Võ Nguyên Giáp, An Biên, Хайфон — 1 санузел, полная меблировка, лифт, парковка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-le-chan-hai-phong/134237797.htm","5 дней назад",5,source="chotot",
  descEn="1-bedroom flat, 35 m², Võ Nguyên Giáp, An Biên, Hai Phong — 1 bathroom, fully furnished, lift, parking.",
  details={"photos": ["https://cdn.chotot.com/ntx5uu0ZDegL3a4TPV_BAnH8AtdDmryrLR8nL3igfyU/preset:view/plain/2982eca5efc8286a28d4d9b48dea66dc-2998312627316237971.jpg", "https://cdn.chotot.com/bTdQe-N_8kZPqiovws6RpSZVsg29KZjqjGy9teB-H1w/preset:view/plain/5500faf57992b06ee07efd54ae1ded3d-2998312627417027953.jpg", "https://cdn.chotot.com/K-db8BzZ-jqCfg92gOTb9RxAU0RIWM_5zYsOr19zqEY/preset:view/plain/68f1dcb5212aa57d4e1417665e34096e-2998312627340539101.jpg", "https://cdn.chotot.com/iD-OzoNgmajoj8MxhUymQEqaua4JCWsTgIjw2LGkO_c/preset:view/plain/eb4665e3e4978b16826a10ce5363ae9d-2998312627011871147.jpg", "https://cdn.chotot.com/92tJd3O1OnhV_G7E5GjzN7bWWM4LnR9HwGkQwSNLDSE/preset:view/plain/30b1076efff1eeda66bcba8db7d126d4-2998312627304127603.jpg", "https://cdn.chotot.com/sazxAqIG3_DBxX9z0Fr0uZ_27THs-i4nnkb-a46cP2U/preset:view/plain/1254ab5ba64a13bddb4c9c37fa441889-2998312627356278267.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002638,"hai-phong","anb2","Квартира",4500000,35,
  "1-спальная квартира, 35 м², ул. Võ Nguyên Giáp, An Biên, Хайфон — 1 санузел, полная меблировка, балкон, лифт, парковка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-le-chan-hai-phong/134521519.htm","7 дней назад",7,source="chotot",
  descEn="1-bedroom flat, 35 m², Võ Nguyên Giáp, An Biên, Hai Phong — 1 bathroom, fully furnished, balcony, lift, parking.",
  details={"photos": ["https://cdn.chotot.com/deGuh8qhzQbuA03IZqLJr0BDYY7mbqj2WmLMVdjjMss/preset:view/plain/f9353f9a56c324c330fea368daf385fa-3000743754851521019.jpg", "https://cdn.chotot.com/qSZ--Jl1FneDLtJf2JFB_id8Y__FefMdODh8j-G5asc/preset:view/plain/3955da278fb3d6de5bb7c673c96635b3-3000743754704206515.jpg", "https://cdn.chotot.com/Z28kB-Jnmp3x3muOMFvYByT9p6Gy3vUp4G3C6ZPV7B4/preset:view/plain/03e81d71b526118648d6221452c48f50-3000743754905606030.jpg", "https://cdn.chotot.com/gpR_Xe_sHBNSJuZgaEjqemgCDF1-9N97aa-OPCH2xW4/preset:view/plain/2d7f22088f9793336e2805f0b4a259ea-3000743754870048375.jpg", "https://cdn.chotot.com/L5EZwtpnpMMfOeZ4JuyHJqM_fdjoImxE462-NVoMzRc/preset:view/plain/a9d768aac34f4edbd98f2417af7a6e45-3000743754544138049.jpg", "https://cdn.chotot.com/7pfQBK15qV_J0ZPQqlKQrJbn1xoGcdrJVNFut17KDUA/preset:view/plain/471d15da07ddcb0c03f193229bf88550-3000743755012791540.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002639,"hai-phong","anb2","Квартира",6000000,57,
  "2-спальная квартира, 57 м², ул. Hoàng Huy Commerce, An Biên, Хайфон — 1 санузел, балкон, спортзал.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-le-chan-hai-phong/134490176.htm","8 дней назад",8,source="chotot",
  descEn="2-bedroom flat, 57 m², Hoàng Huy Commerce, An Biên, Hai Phong — 1 bathroom, balcony, gym.",
  details={"photos": ["https://cdn.chotot.com/PFJCBh4ahmlpE1YnRMP0BKyfnW9OXHjLco1BNzIK9Hg/preset:view/plain/d761a190c4a906811543a61cdae6eb59-3000481871739038088.jpg", "https://cdn.chotot.com/M3Q94cMPs4pphfFeVDua0AOnd0yAkwsG4XlXP9xL01I/preset:view/plain/230117ecfdbe9114f723596395be4d9c-3000481872063778380.jpg", "https://cdn.chotot.com/Tm1QWrftwHX_dKtLmF88ksTe4h00L-ooBDmkIY7l64s/preset:view/plain/02b1c0c28311c91b9c3311d2181ee904-3000481953143597448.jpg", "https://cdn.chotot.com/FDF1hKTJYtP3y2HdJ90vB1e2n116kThdxcxBdlgT2QU/preset:view/plain/4d59ee7ffccacf074cd265917de0d136-3000481952933114275.jpg", "https://cdn.chotot.com/MML_qtyAp36uR0CShFCXWM1Fvln8-aHqNDiIerbKYUc/preset:view/plain/4e4390d586afc38f0b8ad02bb34a437d-3000481954118959150.jpg", "https://cdn.chotot.com/dKAdynzQcIPQhycY7BRe6ejLqA_pMS_8zDTgO2evHzo/preset:view/plain/1ec7073ce21ad474989866934f73984f-3000481953940225888.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002640,"hai-phong","anb2","Квартира",6500000,35,
  "1-спальная квартира, 35 м², ул. Võ Nguyên Giáp, An Biên, Хайфон — 1 санузел, кондиционер, балкон, лифт, охрана.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-le-chan-hai-phong/134483184.htm","9 дней назад",9,source="chotot",
  descEn="1-bedroom flat, 35 m², Võ Nguyên Giáp, An Biên, Hai Phong — 1 bathroom, air conditioning, balcony, lift, security.",
  details={"photos": ["https://cdn.chotot.com/fpRUq40umaYsaw6-g5W0Utq-KXy1b1tU3Qgqt4TYLhw/preset:view/plain/ad56641f0b1b4e2aef2b1c31c29d5cb9-3000448349335941539.jpg", "https://cdn.chotot.com/WbvBdrIb6Ha88971mnTy1-zeX90UZTERbVvq-EsOd2I/preset:view/plain/fc4882621806351746aaa16018ec53a7-3000448349499712416.jpg", "https://cdn.chotot.com/vHg4F4tMmLHdRZ-WK3cZV1QVjsxSEq4vmeDGqcAwH2U/preset:view/plain/dcd99b951404585f6e697a1f3dcf3dcb-3000448349474021255.jpg", "https://cdn.chotot.com/omFl1dP046XjtX51QKci6FWe13PkJ0NfrLgxD1XfDIk/preset:view/plain/c908c9a484833130907f74a544e07231-3000448349492465510.jpg", "https://cdn.chotot.com/r3mR6rLhu4pNX4zALh9Cia3jsTtyNSQ94r64CxGT1RQ/preset:view/plain/2cc2b7db0731ee32e4852f6eb39a81dd-3000448350314244488.jpg", "https://cdn.chotot.com/Qu9FDN2e7BMbOpMT140GK4g2QGNGmWR4Pa1BD6CQFTI/preset:view/plain/d1f1d7bb0809dbf3956e17e5cd252baa-3000448349238853678.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002641,"hai-phong","anb2","Дом",4500000,56,
  "1-спальный дом, 56 м², ул. Lán Bè, An Biên, Хайфон — 1 санузел.",
  "https://www.nhatot.com/thue-nha-o-quan-le-chan-hai-phong/134481125.htm","9 дней назад",9,source="chotot",
  descEn="1-bedroom house, 56 m², Lán Bè, An Biên, Hai Phong — 1 bathroom.",
  details={"photos": ["https://cdn.chotot.com/RiaVt5Dymc-HUFHsfpIYTQ9U1rVIQBu0C0I7tIMFnqg/preset:view/plain/daa443fe4226931335f54fe5b6118e65-3000438425655970804.jpg", "https://cdn.chotot.com/xhNc8r_XHJv1_0dHbbnint5kp24SlQAV22odDD75Nqw/preset:view/plain/7d1fd5c3ed60286beace2b6c40555ae1-3000438869040376200.jpg", "https://cdn.chotot.com/SMlXUtn8E3oYTmezX3FjgODCf5sotBQDDo1fLgHWqBs/preset:view/plain/c95ae2ae27ce23a709f394cb68cf0225-3000438870969821576.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

# Оговорка одна на всю партию, поэтому в строках стоит метка, а не её текст:
# так партия остаётся читаемой глазами.
NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
