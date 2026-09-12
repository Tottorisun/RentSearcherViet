# -*- coding: utf-8 -*-
"""Chợ Tốt, автоматический сбор: 16 объявлений, 2026-09-12.

Партию собрал collect_chotot.py -- без модели в контуре. Район взят точным
совпадением ward_name_v3 с CITIES, описание собрано из полей объявления, а не
пересказом текста продавца, возраст не больше 10.0 дней по orig_list_time.

Объявления, район которых не совпал ни с одним нашим, пропущены, а не приписаны
к соседнему -- в этом и разница с тем, как это делала сессия.
"""
from listing_lock import insert_listings

IDS = [1002642, 1002643, 1002644, 1002645, 1002646, 1002647, 1002648, 1002649, 1002650, 1002651, 1002652, 1002653, 1002654, 1002655, 1002656, 1002657]

N_RU = "Описание собрано программой из полей объявления на Chợ Tốt — тип, комнаты, площадь, улица, район, удобства по ключевым словам. Рекламный текст продавца не пересказан, названия районов оставлены вьетнамскими. Подробности смотрите по ссылке."
N_EN = "This description was assembled by a program from the ad's own fields on Chợ Tốt — type, rooms, size, street, ward and amenities matched by keyword. The seller's marketing copy is not retold and ward names are left in Vietnamese. See the source for the rest."

NEW_SRC = r'''
L(1002642,"hue","acu","Квартира",10000000,66,
  "2-спальная квартира, 66 м², ул. Tố Hữu, An Cựu, Хюэ — 2 санузла, полная меблировка, кондиционер, балкон, бассейн.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/134001587.htm","сегодня",0,source="chotot",
  descEn="2-bedroom flat, 66 m², Tố Hữu, An Cựu, Hue — 2 bathrooms, fully furnished, air conditioning, balcony, swimming pool.",
  details={"photos": ["https://cdn.chotot.com/x3gtR6U4E92b_nefYNLif0g72QULHFWSHQsEi3LHmd0/preset:view/plain/6242b6afba23c5b801a7c82d189fd81b-2996560094687325198.jpg", "https://cdn.chotot.com/KbIRpaRAdAhpi-pfXdrJhLlO1VMnIvRi-oWlnL3zmGo/preset:view/plain/7583101a4bbb3596f9f104e7de618fa0-2996560094733432151.jpg", "https://cdn.chotot.com/KDw80yrqkhrmoSWo-Q1fY4pd2eMIQEngTka9VQSmMiY/preset:view/plain/b34cdd45c967b5991864a3862a6c569a-2996560095059423202.jpg", "https://cdn.chotot.com/0CsDETY1VTj3NBc3rLSpd0MlTlQ511Lk18Md-YVxmDQ/preset:view/plain/27b638923e8c953c1970f87d32a16319-2996560095346423684.jpg", "https://cdn.chotot.com/s75IFFy_uEWFbVLFa8n-6A-7KHocctVKW1ggGrbGxFU/preset:view/plain/6bdea8cafbdd65442293030e3baaf133-2996560095513980058.jpg", "https://cdn.chotot.com/4JES_OISLTwyxNLXAO0faJnT90ijzlxGc3bDLsesC_o/preset:view/plain/fd9992b74eb39b062ad18101cc72dedc-2996560095055595163.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002643,"hue","vyd","Квартира",4500000,54,
  "2-спальная квартира, 54 м², ул. Tố Hữu, Vỹ Dạ, Хюэ — 1 санузел, балкон, лифт, охрана.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/134642105.htm","сегодня",0,source="chotot",
  descEn="2-bedroom flat, 54 m², Tố Hữu, Vỹ Dạ, Hue — 1 bathroom, balcony, lift, security.",
  details={"photos": ["https://cdn.chotot.com/H2bvdIjHBEMiRNCTGB-k7RAEfvZM5MoyRv3qs7I2T4A/preset:view/plain/ed0cf8a148f441df1f12cbc77c5bb5fe-3001677825009447534.jpg", "https://cdn.chotot.com/8hKSD5Bad9QN3OoZDPbkArmqVo1WJZk5T520Gg_dpFc/preset:view/plain/07b2fe96f5a2df4306a120309d0cf47a-3001677825175567501.jpg", "https://cdn.chotot.com/Nm3guqsCe8_3tPxeVU63W_8iv5UOMCCtpV6gSn5NiE8/preset:view/plain/fb31c3afd563d1d7f8a10cffa5589536-3001677825309266408.jpg", "https://cdn.chotot.com/mkLOOpBFCc-ka5bE8uI8oSKJLTiVNjparXP2YR_rEiI/preset:view/plain/3317447f93855ec190a744d1e0af0fb7-3001677825647047278.jpg", "https://cdn.chotot.com/ak9PHPl4U1cYt4n37v4Ikq3L_s5xyp8Uq379izOxrPM/preset:view/plain/aeff77b5910092cca39205fa83f8389e-3001677825392052916.jpg", "https://cdn.chotot.com/RlneLIsZ9O9z84m_bSj-Pk16Srm_xwdwLtVhlaYbIIo/preset:view/plain/4a5376febbf254400e20c90667138d1c-3001677825393953022.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002644,"hue","vyd","Квартира",7000000,66,
  "3-спальная квартира, 66 м², ул. Lê Đức Anh, Vỹ Dạ, Хюэ — полная меблировка, кондиционер, стиральная машина.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/134627788.htm","вчера",1,source="chotot",
  descEn="3-bedroom flat, 66 m², Lê Đức Anh, Vỹ Dạ, Hue — fully furnished, air conditioning, washing machine.",
  details={"photos": ["https://cdn.chotot.com/wkr15V1i6SwW1LaPxCguhFdNdVkGvWKUn7PD3VO-DL0/preset:view/plain/ac1ab80e75bc91e76bda76ffcabfa50b-3001598446299777716.jpg", "https://cdn.chotot.com/0nrOBk7D2AZk25UYwfpF0tVLCztaYwIGDHlNs7GlcmA/preset:view/plain/85d31dbf5bedbb21cec17c1c35eddf6c-3001598446236954803.jpg", "https://cdn.chotot.com/GSPvdsKbYIsfj3pWhvYrz_SS9N2WHjoLxa-C0khXTHo/preset:view/plain/98c4c34bcc81d966c8cc063df1c8b718-3001598445842805849.jpg", "https://cdn.chotot.com/Am1W8qcI4wg3JPRpw8tqNBT2h95Wjxg62pVPGAqUfXY/preset:view/plain/36f819ace40a9e3fde0f226d6a12e469-3001598446429275895.jpg", "https://cdn.chotot.com/gDDiOTwrEuyiMkTLhITky4XiYdPQkHFkWSz0e2BLkUU/preset:view/plain/aaa21823023adb05c6f71ca6c1702630-3001598446366339546.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002645,"hue","acu","Офис",4000000,80,
  "Офис, 80 м², ул. Tố Hữu, An Cựu, Хюэ — балкон.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-thanh-pho-hue-thua-thien-hue/134602108.htm","2 дня назад",2,source="chotot",
  descEn="Office, 80 m², Tố Hữu, An Cựu, Hue — balcony.",
  details={"photos": ["https://cdn.chotot.com/Uy9sNqvW9UhbrNIdrHvX0n41SqMQfOVN_ymRY7fCQw0/preset:view/plain/d256a73e79c47b723d79abf38c1212ae-3001356835865416266.jpg", "https://cdn.chotot.com/yZQZ4gpiskB1GZtc40vAiMgNnlQf6v7NQ-Q-rWShHsw/preset:view/plain/9ea977124b9b4cdd2f149054483df41b-3001356835812614575.jpg", "https://cdn.chotot.com/_Dcdy6n5BBLEGGEAFEfmLeW9fd8EVu-0JNQyHAPTtfI/preset:view/plain/a265487a5937d0c893a3dc54f06c05ac-3001356835830831566.jpg", "https://cdn.chotot.com/6YnYp-k-9wwb5F62hvT92lgXvA2W8PU9wuh8V_vC8Y8/preset:view/plain/a5a28606a5f94f7a9219cfd973dc92f5-3001356835869917310.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002646,"hue","acu","Комната",2500000,20,
  "Комната, 20 м², ул. âu lạc, An Cựu, Хюэ — стиральная машина.",
  "https://www.nhatot.com/thue-phong-tro-thanh-pho-hue-thua-thien-hue/134602009.htm","2 дня назад",2,source="chotot",
  descEn="Room, 20 m², âu lạc, An Cựu, Hue — washing machine.",
  details={"photos": ["https://cdn.chotot.com/v-qYs0QdwQZyKkf4K2Grzpe-p1iEyre7OREM7EB_FKo/preset:view/plain/596bcec85ee5bfcf8f186d729dae9a11-3001356358005095620.jpg", "https://cdn.chotot.com/ISuoa9Ef4miqOvqGpChx_5t0-UtVvh5nwPlPbxMqPkk/preset:view/plain/f248589756edcecf5edffd4c8fe63832-3001356358582084015.jpg", "https://cdn.chotot.com/HO-O3pmOHXvdeoYmkQ3chwKLPdUUUa-fCykfwcWxw0A/preset:view/plain/4d559368d7a9801e9afe4a2620f4c2c1-3001356358521551414.jpg", "https://cdn.chotot.com/dhhx6LcjqOsJCqxBnoMW05aSZMFRfqykSoMrkD_lqWA/preset:view/plain/b3b764ac539be2e7cb8def1c352e2d5b-3001356358408997556.jpg", "https://cdn.chotot.com/UV3WH7ZN-xguxg74TpGj6SdqAGYw9T0atsgp170V7_M/preset:view/plain/2be29eb6d7ab59263f6c247ea7bd2b58-3001356358423183486.jpg", "https://cdn.chotot.com/qsNrawOtjf0WxemuaUnFMiqx2XiMi5_KzRzCx5nlTpg/preset:view/plain/8be7549d265edbdc832946fe1f63e56f-3001356358837264097.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002647,"hue","acu","Квартира",5500000,50,
  "2-спальная квартира, 50 м², ул. Cao Đình Độ, An Cựu, Хюэ — 1 санузел, полная меблировка, кондиционер, стиральная машина.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/134586709.htm","3 дня назад",3,source="chotot",
  descEn="2-bedroom flat, 50 m², Cao Đình Độ, An Cựu, Hue — 1 bathroom, fully furnished, air conditioning, washing machine.",
  details={"photos": ["https://cdn.chotot.com/CIaZea12D1U5TdmRAsec4k4Trt8JvhUzGGQRfSBIQZM/preset:view/plain/891b7b35e814f0aab14825a09936b804-3001232399412421550.jpg", "https://cdn.chotot.com/eePDmaA0v1hSw8SJvJE7WQKInSB9bdQ5fec27VPKzFo/preset:view/plain/685885811118de800ee0a0ef6a1ef700-3001232398958349306.jpg", "https://cdn.chotot.com/mH51Y3-liEH5ht-HkH7vR0PEzlAn82Y7RC1nU07wKMg/preset:view/plain/308be2571a514ddadff06cfbcebc5add-3001232401057627782.jpg", "https://cdn.chotot.com/hcnlv02543uTrjoJFso1-t4T96SiErmy-LHOApQUaJo/preset:view/plain/42d85a2f57ea759a168fbff0d6076343-3001232401845248942.jpg", "https://cdn.chotot.com/EfbB1qDnJteVxUsKG0i2Xt4rEw7XrBonjFmCTcjMD6w/preset:view/plain/eb9f82678e10ad74d730b29f824520c1-3001232402589028894.jpg", "https://cdn.chotot.com/R8kZLVb8uBMXYcxdohAM0VXyLBmxZL1iQk3sTMYxvDI/preset:view/plain/ceef11e4f37d103a8a46b635d25a3cdc-3001232403948048926.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002648,"hue","vyd","Квартира",5000000,66,
  "3-спальная квартира, 66 м², ул. Võ Nguyên Giáp, Vỹ Dạ, Хюэ — 2 санузла.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/133774509.htm","3 дня назад",3,source="chotot",
  descEn="3-bedroom flat, 66 m², Võ Nguyên Giáp, Vỹ Dạ, Hue — 2 bathrooms.",
  details={"photos": ["https://cdn.chotot.com/_9XCw5s-tM7eVzCglN4Qwo254qz_xq4cR6frTmPQ4Tw/preset:view/plain/5c7591c37a3e6a4e0db750bae6b1f98d-2994856513871929920.jpg", "https://cdn.chotot.com/s6QzAjRssq5c8DBxlgpzFSLjkyj_3DOwQq8CUF7uXqc/preset:view/plain/38b16b20e3aef323b5a812e26f9e2887-2994856512922178416.jpg", "https://cdn.chotot.com/evxYi5SEJOu15tv9iMZO1NgsgerW6k5KG04EXhneewk/preset:view/plain/91b18d60412ec5378500e2ec6176e42a-2994856513004556273.jpg", "https://cdn.chotot.com/SmMe2BhUsTGcBFvz-UxHyU4lJUsQaQPXCb06fuZiOy8/preset:view/plain/518ff855f72912a8183c74e5e1ac73c3-2994856512952504192.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002649,"hue","vyd","Квартира",4000000,54,
  "2-спальная квартира, 54 м², ул. Phạm Văn Đồng, Vỹ Dạ, Хюэ — 1 санузел.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/134536462.htm","6 дней назад",6,source="chotot",
  descEn="2-bedroom flat, 54 m², Phạm Văn Đồng, Vỹ Dạ, Hue — 1 bathroom.",
  details={"photos": ["https://cdn.chotot.com/cYqkRSgwn0ZPDznyMw2wTq7g6vH7UV8EYWZpN-NEbCc/preset:view/plain/b1d33474c2d437986dc7e611f52e7b10-3000877368794548082.jpg", "https://cdn.chotot.com/Lle33YneIrXzGfTrexdGZGLv01CQQrKqFNlLNWA-sFU/preset:view/plain/e948dff364ba3e8b968574c09fa66afb-3000877368802559607.jpg", "https://cdn.chotot.com/Ea78wccAOW-RAGxHdUv0rVuRTYF63-Uxpd43FCYcaO0/preset:view/plain/c747146937bedf6a6f2156e68092ce33-3000877368913807599.jpg", "https://cdn.chotot.com/3WSZY3TX9tKWnJ6jJ-WHJaQGQ4e4EhY3_D9xDfsVJ8w/preset:view/plain/7c3c18189ae9d0c82037b22c4234acb2-3000877368914377084.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002650,"hue","vyd","Квартира",6500000,67,
  "3-спальная квартира, 67 м², ул. Lê Đức Anh, Vỹ Dạ, Хюэ — 2 санузла.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/134529427.htm","6 дней назад",6,source="chotot",
  descEn="3-bedroom flat, 67 m², Lê Đức Anh, Vỹ Dạ, Hue — 2 bathrooms.",
  details={"photos": ["https://cdn.chotot.com/9WsBOjbmEkf8Qdb6Kq8VaGdADcNOWrWlTYRme9GrqCs/preset:view/plain/44c11e4b649b1097377aaa366967c64c-3000782412744741768.jpg", "https://cdn.chotot.com/5AsIZIT66tlGrzkREITRavMHM_AROEG8G6Yl3xBo0xo/preset:view/plain/a53e1f3b9a16471985e43709748eb37f-3000782412319153440.jpg", "https://cdn.chotot.com/_7xhCgTJWhkDyIZIhUMG1a_tVGbwuWyxtosM3x4hjcY/preset:view/plain/3f08b7638fcead208d6b14f6124acdda-3000782411063969399.jpg", "https://cdn.chotot.com/muTQRxRjURi_Ay6UqN8Cxr07TdLM9ObYsajXEqTAlfI/preset:view/plain/b7b93ccc86b107afb3eadf9563031d59-3000782411500903444.jpg", "https://cdn.chotot.com/eUAuqb1H4hcVvEk3V5BLHAia5kcfmiZiZaVRNDSObPw/preset:view/plain/4f4812bbfaeb138982f20f5e17d054ab-3000782412869092884.jpg", "https://cdn.chotot.com/6MAARBFWAVbRYzjBfeAFi4laARljYTs5n8pBh3cIUV0/preset:view/plain/7b8fdeab9b51a0af43f9a22bf882ee8f-3000782411720747558.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002651,"hue","pxu","Офис",3500000,16,
  "Офис, 16 м², ул. Thái Phiên, Phú Xuân, Хюэ.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-thanh-pho-hue-thua-thien-hue/134540749.htm","6 дней назад",6,source="chotot",
  descEn="Office, 16 m², Thái Phiên, Phú Xuân, Hue.",
  details={"photos": ["https://cdn.chotot.com/J_gCz9NgRRyUrrWCLALfBZw514A8wzgLvHrCLGxfca4/preset:view/plain/e44ca54cb47622b84a186514385bb609-3000899014907390815.jpg", "https://cdn.chotot.com/fQb9eKanAQfXqO8jOtXC0xPG4zOqXBBgmre29PfOBm8/preset:view/plain/b2ec3a80d0ff655a6e7f6f27efc2c3aa-3000899014322607493.jpg", "https://cdn.chotot.com/C2UJF80Lxhyx1dP9MHnESPL06MUnM8f-2iGz9i3iDLw/preset:view/plain/8a909b1abc498c760ec8197f6864541c-3000899014841353847.jpg", "https://cdn.chotot.com/A8M655DWcczNYd5v4tWYIoVH8cxY2XG1wcc1vgh0ZQY/preset:view/plain/63859d07dfeecea85c9152e1ed9e5558-3000899015073381508.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002652,"hue","vyd","Квартира",6000000,54,
  "2-спальная квартира, 54 м², ул. VÕ NGUYÊN GIÁP, Vỹ Dạ, Хюэ — 1 санузел, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/134520898.htm","7 дней назад",7,source="chotot",
  descEn="2-bedroom flat, 54 m², VÕ NGUYÊN GIÁP, Vỹ Dạ, Hue — 1 bathroom, fully furnished.",
  details={"photos": ["https://cdn.chotot.com/nH4MU4oNnakI1-Eo2_23kXkV6z9OV-iJjBeg88CugZU/preset:view/plain/356f33f2c1fb08e8b604132e8f955d83-3000741337073409268.jpg", "https://cdn.chotot.com/7gWcVhSQyNZhXFLCIdl_yL5egIe2WQSE4cYclw-c4KU/preset:view/plain/c46d9bfe87f367436c8802440a72de58-3000741336891344503.jpg", "https://cdn.chotot.com/lFfZmqs8QZ1jI4Bh0QdySmtDwyUQztpVhUXcA79tM8s/preset:view/plain/b41ef1ac8bb747bf9ff56026815e83e4-3000741337122590771.jpg", "https://cdn.chotot.com/31_F8064XS-hNLn9XzQfX2h2pTU6b64SjvcHRcQyFdI/preset:view/plain/3670b82eab156f0c5a14c5fa19e4c810-3000741336984849872.jpg", "https://cdn.chotot.com/Iz6CYovlLGPaV8QIjyTWG1x1jZvW9chIoctC8SK8QVE/preset:view/plain/a64e72ad749638f473773cba1e215cb8-3000741336978310977.jpg", "https://cdn.chotot.com/A9pKRNXn1-xBa2ttpDkSgGzBmtlhDQeXqjcop2CKwnU/preset:view/plain/582ffbf8fe40feeb750a19ef032a5610-3000741337776716028.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002653,"hue","vyd","Квартира",6000000,66,
  "3-спальная квартира, 66 м², ул. VÕ NGUYÊN GIÁP, Vỹ Dạ, Хюэ — 2 санузла.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/134519432.htm","7 дней назад",7,source="chotot",
  descEn="3-bedroom flat, 66 m², VÕ NGUYÊN GIÁP, Vỹ Dạ, Hue — 2 bathrooms.",
  details={"photos": ["https://cdn.chotot.com/0Sc2JoIFbqAIJwv1wiwO0uF_dock2ML7PXHbOn3sbjI/preset:view/plain/733dfbb6f8e5ed7b1063ae80a71f0866-3000735496827426181.jpg", "https://cdn.chotot.com/ziDVBHNrnAn6SWuaVSyNi0vi7dS9Jncv4MnmFPRk-wU/preset:view/plain/84f7c53535cc2273d98c1fcb8d7b7e99-3000735496902405705.jpg", "https://cdn.chotot.com/_KCgkkaE-U3To7Lpep3VomsNZv_SWq-UTa9Pyxkbns0/preset:view/plain/10cae3c0cb06e1822941b147675ab8c2-3000735497014000307.jpg", "https://cdn.chotot.com/VmcHiBaALjOqQIO_5WZA-OoBdIAQspk0QK4psJs6b4o/preset:view/plain/44cc3e29831892d549f27f71f6669347-3000735497111788832.jpg", "https://cdn.chotot.com/feAeyMkKsu9WrC5n6PQAOQQkaQiKzRazPTpYqY4HyeA/preset:view/plain/647b05a58fe1bd37a3e2464f9e4b4dc9-3000735497501709200.jpg", "https://cdn.chotot.com/0H3PRrwBPj_KrjXzIZFaO_6PMsWkhyq0SzOgDuCWQvE/preset:view/plain/6a680e45b7f1521481dcc63b59c59065-3000735497426563664.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002654,"hue","vyd","Квартира",4500000,66,
  "3-спальная квартира, 66 м², ул. VÕ NGUYÊN GIÁP, Vỹ Dạ, Хюэ — 2 санузла.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/134519352.htm","7 дней назад",7,source="chotot",
  descEn="3-bedroom flat, 66 m², VÕ NGUYÊN GIÁP, Vỹ Dạ, Hue — 2 bathrooms.",
  details={"photos": ["https://cdn.chotot.com/s8v5ctvaouU7GZzfwYmO5zvXfrXu551EWwMr3rkZVOI/preset:view/plain/abf193dd482c1c4214e0754fcd047bd7-3000735206969788023.jpg", "https://cdn.chotot.com/1PFr2XzQM2ELZFGGi0ix3aVAHyhDszccV2mqlaPEKN8/preset:view/plain/62a4aacec12c4c7216d855d7e943c029-3000735213089721808.jpg", "https://cdn.chotot.com/Ikv7XDFkNmQAsLBoyAdA6oD35QC5oJDuJY08qg7bF8w/preset:view/plain/92670ec0d9fea72b27ba6b270c943a8e-3000735211166632010.jpg", "https://cdn.chotot.com/zNP2ZDm99DY1uzM2W3SBFfPt2KX0EtfRuZxRknuK3QY/preset:view/plain/452c273508423f2241713dba4aecbfb5-3000735211852239760.jpg", "https://cdn.chotot.com/t1wanDHQtfzIGkFJI3SCKby6Dr3UpD8AxtMLaZsW-Cc/preset:view/plain/33d0799d77632514e5351d32db0aa015-3000735210136906793.jpg", "https://cdn.chotot.com/bpR1GztCq206mLuWC11qsl46enNSy11OO1OjMmF5F0o/preset:view/plain/dc3244936a2c4e0cd1efa57ede2bd5a2-3000735212435658638.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002655,"hue","pxu","Офис",80000000,120,
  "Офис, 120 м², ул. Hùng Vương, Phú Xuân, Хюэ.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-thanh-pho-hue-thua-thien-hue/134519607.htm","7 дней назад",7,source="chotot",
  descEn="Office, 120 m², Hùng Vương, Phú Xuân, Hue.",
  details={"photos": ["https://cdn.chotot.com/-3x2q3CBJbvQ5ik20pLth2aOuX3QgGgdNtKWO80IQ_s/preset:view/plain/2de5c77790975fed7c8557a83e4fe6e4-3001600351706149486.jpg", "https://cdn.chotot.com/TRYzZqXKnjshM05EC2RlAVQENms21lq9VikIgWPk7oA/preset:view/plain/21f925551d63a465e454ee6b52dbef87-3001600372073951854.jpg", "https://cdn.chotot.com/hwPnVsFxc98vVgkT6Np24_zCM1q38w8aQ9PYGeXl4JM/preset:view/plain/4e07c68aa665907f2336b0ee207d88a3-3001600372130646708.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002656,"hue","acu","Офис",5000000,35,
  "Офис, 35 м², ул. gần Trường Chinh, An Cựu, Хюэ.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-thanh-pho-hue-thua-thien-hue/134507125.htm","7 дней назад",7,source="chotot",
  descEn="Office, 35 m², gần Trường Chinh, An Cựu, Hue.",
  details={"photos": ["https://cdn.chotot.com/ADm8yNeo7J6rXV13W_1UvnWEzNH5puvg20aN76agcJk/preset:view/plain/f50a9392faa700b47e35361e37efa39c-3000615886121024430.jpg", "https://cdn.chotot.com/1Vegeaf60SyJZmvGDjXUq_0Zy1v2W9TgZTvK6OH83MA/preset:view/plain/a4e5d9019603dcc666e1d7c2a8c00564-3000615886160086189.jpg", "https://cdn.chotot.com/Hepd08M_2GdOUb-qtZCU3AkdMfCdFoGO1-paQy4AJGI/preset:view/plain/8bbedaa0ec1965a30831eff099fec968-3000615886186417616.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
L(1002657,"hue","vyd","Квартира",4500000,66,
  "3-спальная квартира, 66 м², ул. lê đức anh, Vỹ Dạ, Хюэ — 2 санузла.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-hue-thua-thien-hue/133612293.htm","9 дней назад",9,source="chotot",
  descEn="3-bedroom flat, 66 m², lê đức anh, Vỹ Dạ, Hue — 2 bathrooms.",
  details={"photos": ["https://cdn.chotot.com/IkY8J30y05GCjfpmUUNVobVINqTXchyUwM1DjBsK_LE/preset:view/plain/e1314966324176e86e3815b2525f6773-2993627742502576138.jpg", "https://cdn.chotot.com/0zzRrjXjEpSa-jbX7VivVrO16wbIfZTvhESjPqofwjk/preset:view/plain/e8bf40026ccb9d981a2d6308ab4e45f1-2993627742310570823.jpg", "https://cdn.chotot.com/EwxgKIAiYt6dTumCmc37cRnJmoJSAeKMtA93AbG4Xr8/preset:view/plain/2a4be6b7e2ffc6b12399ecefe5df37a3-2993627743119680368.jpg", "https://cdn.chotot.com/b2SKKJ8OG1YzXK_v8Ro1bws53GeuI3huc0qHh29jUEA/preset:view/plain/1feba07b44e81b1697483169879c60c5-2993627743113014396.jpg"], "notice": "RU_N", "noticeEn": "EN_N"}),
'''

# Оговорка одна на всю партию, поэтому в строках стоит метка, а не её текст:
# так партия остаётся читаемой глазами.
NEW_SRC = NEW_SRC.replace("RU_N", N_RU).replace("EN_N", N_EN)

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
