# Daily HCMC check 22 Aug 2026 (5th pass): 11 new listings across th(5)/ak(2)/kh(3)/bth(1).
#
# NOTE: a concurrent/earlier pass today already inserted IDs 1234-1246 (3rd+4th passes, the 4th
# pass landed literally while this sweep was running) before this run started; this sweep
# independently re-fetched Chợ Tốt for the 6 target wards and cross-checked candidates against
# the just-committed state to avoid re-adding them.
#
# SKIPPED as re-push/same-unit duplicates (not added):
#   133815199 (th, Trần Xuân Soạn 4x18m 3PN house) — same agent "LHP", identical specs/price/street
#     as already-present L(783) (URL 133808666), just a fresh ad ID from a re-push.
#   130710142 (ak, Nguyễn Bá Huân 50m2 1PN apt) — same agent "Phương An", same street/size/room-count
#     as already-present L(1095) (URL 133971394), price differs (9.5tr vs 11tr) but too likely the
#     same unit to treat as a new listing.
#
# GEOGRAPHY: bq (Bình Quới) had only 1 fresh candidate today and it was already caught by the prior
# pass; tm (Tân Mỹ) candidates from this sweep were also already caught by the prior pass.
#
NEW_SRC = r'''
L(1247,"ho-chi-minh","th","Квартира",6000000,40,
  "Новая 1-спальная квартира с балконом, ул. Nguyễn Thị Thập, KDC Him Lam, Q7 — полная качественная меблировка, вид открытый, можно заезжать сразу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133694439.htm","сегодня",0,source="chotot",
  details={"contact":"Quang Vũ Unite","photos":["https://cdn.chotot.com/KacYp8YSyCMuVmSplTXYgaIzI6AAhvQIVMVrnKwRLe0/preset:view/plain/5f2410668b2266ec77a01b76be73e002-2994240690396515197.jpg","https://cdn.chotot.com/1pdH8P3JpFGESv-iK6LbQL8fQktj_ZIsGZ7xhTeqM1k/preset:view/plain/b28bd7d6dad03a0df49632c4f7e66a68-2994240690612953980.jpg"]}),

L(1248,"ho-chi-minh","kh","Комната",4900000,25,
  "Комната-студия с полной меблировкой на ул. Tôn Thất Thuyết, Q4 — свободный график, без совместного проживания с хозяином, охраняемый паркинг, рядом ĐH Luật, RMIT, ĐH Tôn Đức Thắng, 5 мин до Crescent Mall/Lotte Mart/BigC.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/132422802.htm","сегодня",0,source="chotot",
  details={"contact":"Mạnh Tiến Newind","photos":["https://cdn.chotot.com/Df3kujxcQSoMoFIWcKgNz8MOdHZtkuOBOcozfAjwYbc/preset:view/plain/6927e3aa35d8215774d79a16c35305b0-2984530593435724683.jpg","https://cdn.chotot.com/KiDd18rZXzwiFoeZSde0jyHkHH0wKw5t8yw3vfn2oWA/preset:view/plain/0133850faad326e4b8718923effbdad8-2984530593545907026.jpg"]}),

L(1249,"ho-chi-minh","kh","Квартира",19000000,75,
  "2-спальная квартира (2 с/у) в ЖК Millennium, 132 Bến Vân Đồn, Khánh Hội, Q4 — просторный балкон, бассейн-инфинити, спортзал, зона BBQ, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/131749547.htm","сегодня",0,source="chotot",
  details={"contact":"Thu Phương","photos":["https://cdn.chotot.com/K9Gip1RvEIRcpavr_o-XGdzZ1-iPKCireT6YBRCYnWg/preset:view/plain/66d955361e1ba0e2ce5534dddef7c0ab-2979311849927051893.jpg","https://cdn.chotot.com/6Q2hA8XhcOpwb1eIIzuj0EIawk-9ckRombBCp93mTwM/preset:view/plain/97a256df2da867b1185412ae40307b3d-2979311849925688158.jpg"]}),

L(1250,"ho-chi-minh","th","Дом",75000000,150,
  "Цоколь + 3 этажа виллы целиком, 7,5×20м (150м²), полная меблировка, КДЦ Him Lam, Tân Hưng, Q7.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/132178144.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении отмечена возможность использовать под офис наравне с проживанием","contact":"Quân Phát Đạt","photos":["https://cdn.chotot.com/uNjnrAKJQaDEU0B968V5gRAPe1LGpVA9WoHgAlCD688/preset:view/plain/7449d84a98dfdcb4212692500160e560-2982785479712260489.jpg","https://cdn.chotot.com/E2Pk3eGWUlxQhpknqiQZNeBKHu2NrIVRM58-0EIatxo/preset:view/plain/54e1503ce844dbc2449a2fb0c90ac5bd-2982785479239451089.jpg"]}),

L(1251,"ho-chi-minh","th","Дом",50000000,150,
  "Цоколь + 2 этажа + терраса виллы целиком, 7,5×20м (150м²), полная меблировка, КДЦ Him Lam, Tân Hưng, Q7 (тот же квартал, что и вилла выше, другой объект).",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/132737899.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении отмечена возможность использовать под офис наравне с проживанием","contact":"Quân Phát Đạt","photos":["https://cdn.chotot.com/GWWtRDVmwTE3C5Ikq_AnK-T39pnCD0hD6uUwc3uOPWg/preset:view/plain/6f6e0298d24adcb0233d5d5f1d6fd226-2986967987273447527.jpg","https://cdn.chotot.com/evZ9Opu9fqy6gfNX9OV3e60rOaZW-9Obnq9BxwxA6Nw/preset:view/plain/88fb534cb6568f8c0a821ff130fa405b-2986967988072574454.jpg"]}),

L(1252,"ho-chi-minh","bth","Квартира",9000000,40,
  "Квартира с отдельным балконом, 40м², ул. Nguyễn Thái Bình, Bến Thành — полная меблировка премиум-класса, вход по отпечатку пальца, лифт, круглосуточная охрана. Рядом рынок Bến Thành, Takashimaya, Bitexco.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/131373172.htm","сегодня",0,source="chotot",
  details={"contact":"Cara unite","photos":["https://cdn.chotot.com/abVuG-aAtTIiQKgqs0a-3CVohN8WOTXC4PLgRjN46r0/preset:view/plain/67b41001f1bfc412e5cbcd437ec4e6c6-2976687217449121644.jpg","https://cdn.chotot.com/cHvjgAemRPsu43QFRsRxOg4FTlT8MnDscFkSEjtFI70/preset:view/plain/3136b8e2184ed62f07981e2ffc9ce7cf-2976687216802862504.jpg"]}),

L(1253,"ho-chi-minh","th","Дом",50000000,100,
  "Дом целиком 5×20м (100м²), 1 подвал + 1 этаж + 3 этажа + крыша, лифт, 6 спален/8 с/у, базовая мебель (8 кондиционеров, кровати, кухня). Мест для 2 машин в подвале. Ул. số, Tân Quy, Q7.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/132654787.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении отмечена возможность использовать под офис наравне с проживанием, цена договорная","contact":"Mr Ngọc","photos":["https://cdn.chotot.com/wCnKFO_DUj1XVylo1QgBIdn1BljUVRglK0fSjJ0ZoVo/preset:view/plain/86f6cb9d6cdef92500525556e6b0669a-2986278645902863299.jpg","https://cdn.chotot.com/SAdbVQJrQrlEHu28oQvi0XvCGHMrqicfEn-RKFnvhlQ/preset:view/plain/cd998cb7f9a9a5716401efd31d70b9e4-2986278645674308811.jpg"]}),

L(1254,"ho-chi-minh","th","Дом",90000000,200,
  "Дом целиком, подвал + 4 этажа, 10×20м (200м²), лифт, 6 спален/6 с/у, южная ориентация. КДЦ Him Lam, Tân Hưng, Q7.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133882424.htm","2 дня назад",2,source="chotot",
  details={"notice":"в объявлении упомянута возможность совмещать проживание и бизнес (офис/шоурум) наравне","contact":"Khánh Phan BDS","photos":["https://cdn.chotot.com/hVI8U98nGWjv2ra3vGfdiaJI-Jp9LmA_WmqA4X3Sw6c/preset:view/plain/3e9e6954ca538c340ca06e6dae167283-2995669560132554015.jpg","https://cdn.chotot.com/R9jefpY0sowBKrCA_lBdAHCCuhjQSPe9-0Uwpg5m-Hg/preset:view/plain/f1253d3d434f4d949d2dc55696c54f33-2995669560271554020.jpg"]}),

L(1255,"ho-chi-minh","kh","Студия",6000000,35,
  "Дуплекс-студия с антресолью, полная меблировка, современный ремонт, Q4 (Khánh Hội) — удобно до соседних центральных районов.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133077311.htm","2 дня назад",2,source="chotot",
  details={"contact":"Li Pao","photos":["https://cdn.chotot.com/lHgMlC6G_oCjpxqZsQ1lOi7dPRITfhcg7tfwFkfY_i0/preset:view/plain/34370bfba8fd5322a023e5d066bebc3a-2989506912186241110.jpg","https://cdn.chotot.com/fCGu7gQ_0UpcZ9oOCcpa2m9-p13EvEn1V7P_jdvHL7Y/preset:view/plain/ecff86c4b35c2532351621e44a448feb-2989506912231973782.jpg"]}),

L(1256,"ho-chi-minh","ak","Студия",7000000,30,
  "Студия с балконом, ул. Trần Não, An Khánh — полная меблировка, вход по отпечатку пальца, система пожарной сигнализации, свободный график.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133774804.htm","3 дня назад",3,source="chotot",
  details={"contact":"Thu Quyên HiFriendz","photos":["https://cdn.chotot.com/D2pJXWUfRCHaUCci2hoX7tRNh6Ih_Rxh6z9hH1B7hEk/preset:view/plain/7934282df61dd6ce58e98278980fe2c8-2994858193923860737.jpg","https://cdn.chotot.com/GG3kASeDNkHI2-3gpE01433b5k3AHG06XKrC16Yck4M/preset:view/plain/6a7897883b6091bad1ae94efd400490f-2994858194137240432.jpg"]}),

L(1257,"ho-chi-minh","ak","Студия",6000000,25,
  "Студия у рынка Đo Đạc, ул. Trần Não, An Khánh — базовая меблировка (кондиционер, холодильник, кровать, стиральная машина на крыше в общем пользовании), вход по отпечатку пальца, без совместного проживания с хозяином.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/132629979.htm","3 дня назад",3,source="chotot",
  details={"contact":"Thu Quyên HiFriendz","photos":["https://cdn.chotot.com/0ygSgnH4CWRrpe0zukyQ0GWcgrOcVjRFkFuR-MhEvGQ/preset:view/plain/61f2a89f6237521ac2bd92dea04148f2-2986109407168799571.jpg","https://cdn.chotot.com/_V6UT5CNMbE2gwadaCdiVyVW9CYOMA63rkDjJEtHSY4/preset:view/plain/5656aca67d33d3e2a552b24d81c29930-2986109407173456262.jpg"]}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted daily HCMC check 22 aug 2026 (5th pass): 11 listings (chotot) across th(5)/kh(3)/ak(2)/bth(1)")
