# Daily HCMC check 22 Aug 2026 (6th pass): 13 new listings across th(7)/ak(2)/tm(2)/kh(1)/bth(1).
#
# SKIPPED (not added):
#   134297792 (bth, "66 Phó Đức Chính" 76.6m2 35tr/mo) — listed under Chợ Tốt's house category but
#     the ad itself is for an office floor ("Cho Thuê Nguyên Sàn VP"), not residential.
#   133815199 (th, Trần Xuân Soạn 4x18m 3PN house, 12tr/72m2, agent "LHP") — confirmed same unit as
#     already-present L(783) (URL 133808666.htm), same agent/street/price/area, just a re-pushed ad ID.
#   Batdongsan: site was reachable today (not Cloudflare-blocked), but every ward-matching card found
#     for tm/th/kh was a multi-unit broker "gio hang" catalog ad (e.g. Millennium/Sunrise City agents
#     listing studio/1PN/2PN/3PN price tiers at once) with no single verifiable unit price/address —
#     skipped per the no-fabrication rule rather than guess which specific unit. No candidates found
#     for bth/bq on the pages that loaded (Q1 and Binh Thanh apartment pages only returned old-ward
#     listings from Ben Nghe/Thanh My Tay, neither of which is bth/bq).
#   Facebook: Marketplace search returned a 302 login-wall redirect as usual, not attempted further.
#
NEW_SRC = r'''
L(1258,"ho-chi-minh","bth","Дом",69000000,125,
  "Вилла целиком 5×25м (125м²), 1 цоколь + 3 этажа, 5 спален/5 с/у, ул. Sương Nguyệt Anh, Bến Thành (старый Quận 1) — редкий по площади участок в самом центре.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/133183764.htm","вчера",1,source="chotot",
  details={"notice":"в объявлении подчёркнута возможность использовать под офис/спа/клинику наравне с проживанием","contact":"Nhật Huệ","photos":["https://cdn.chotot.com/VP42Rzo_3axCo9CR124yrdRGwDyfQ1SdMOG471FdRjw/preset:view/plain/3c4b388e84fbb129b4d7bacf9224b239-2990326176150577863.jpg","https://cdn.chotot.com/5K8Hr00YxHgCbO_IWcERzJzNzstOFVA-jt8lRD5DG5g/preset:view/plain/9759c2f1f9e3df4eca810a0d0643a138-2990326176030615300.jpg"]}),

L(1259,"ho-chi-minh","kh","Студия",10000000,40,
  "Студия в ЖК Millennium, 132 Bến Vân Đồn, Khánh Hội (старый Q4) — полностью меблирована, готова к заезду, аренда краткосрочная и долгосрочная, рядом переход в Q1/Q7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/122009782.htm","3 дня назад",3,source="chotot",
  details={"contact":"Thu Phương","photos":["https://cdn.chotot.com/3x2MbodFPeMCCWmFTQRJZzQF03IEjQkX8R_KTv7bf08/preset:view/plain/6e3b1211dac7c7222f087e35353bf358-2911330071690475603.jpg","https://cdn.chotot.com/Hon2mOvjeAUEuS9sveG4tjH4saZ79D3WJ2zew-_aqjo/preset:view/plain/4bdcbf756563a8196147ed507d63e938-2911330071655814964.jpg"]}),

L(1260,"ho-chi-minh","tm","Комната",4000000,90,
  "Отдельная меблированная спальня (кровать, рабочий стол, стеллаж) в квартире 90м² на ул. 15B, Tân Mỹ (Phú Mỹ Hưng) — тихий район, рядом Circle K, Pharmacity, спортзал, автобус №139 и парк.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133502600.htm","сегодня",0,source="chotot",
  details={"notice":"шеринг — совместное проживание с хозяйкой квартиры","contact":"Trần Tiến Phát","photos":["https://cdn.chotot.com/8dVS5-Mr2EyYYUyqXQQD79pcHxDpbxTFvdx05CYyGQ4/preset:view/plain/ef08e251d01fdc10d55e1f91bb311c2d-2992780114331779127.jpg","https://cdn.chotot.com/QYEDv8f9JvPq-0mJnDmM5de5eW1zCht5JQU6ftRJ-WQ/preset:view/plain/a783ae641670c697bdba408a950f5700-2992780110170964023.jpg"]}),

L(1261,"ho-chi-minh","th","Квартира",9900000,50,
  "4-спальная квартира с полной меблировкой, 50м², ул. Trần Xuân Soạn, Tân Hưng — рядом ĐH Tôn Đức Thắng, RMIT, UFM, KCX Tân Thuận, Lotte Mart Q7, вариант под совместное заселение.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134299251.htm","сегодня",0,source="chotot",
  details={"contact":"Thanh Trúc","photos":["https://cdn.chotot.com/YTOgnIyKxaIPhyfoP573G0-g-KURp_gSxVeXRSkhXNw/preset:view/plain/a1bb003a3bb98de78db004fbfb976e89-2998769984229290393.jpg","https://cdn.chotot.com/WCBkew4M1WQrEIlEHgpKi14wG4y9DXdZoPG9JvFgSuE/preset:view/plain/ccaa7bbe8ee975c5acfdfb8c005d1254-2998769984419655011.jpg"]}),

L(1262,"ho-chi-minh","th","Квартира",5500000,25,
  "Дуплекс с балконом/окном, 25м², ул. Nguyễn Thị Thập, Tân Hưng — полная меблировка, лифт в доме, рядом RMIT, Tôn Đức Thắng, Lotte Mart Q7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133227925.htm","2 дня назад",2,source="chotot",
  details={"contact":"Lâm Nguyên","photos":["https://cdn.chotot.com/psnwU1l8f742TMlHiS5QRkBxa9pz6NhGYLHHcVw0Znk/preset:view/plain/6d40e4aeddbe8246467c2a54de371ba4-2990616487500103352.jpg","https://cdn.chotot.com/rjlComG7FWrRa6zcynycc0zAbT3j2RKpIRGg9TiS7Y4/preset:view/plain/80dddd221c431e44fee6e20d9b77633c-2990616487596963722.jpg"]}),

L(1263,"ho-chi-minh","th","Квартира",7000000,45,
  "Квартира с отдельной кухней и балконом, 45м², р-н Cầu Him Lam, Tân Hưng — рядом Lotte Mart Q7, удобно до Q1/Q4.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/126330488.htm","сегодня",0,source="chotot",
  details={"contact":"Trịnh Hoàng Tâm","photos":["https://cdn.chotot.com/ihXxkUhDEYAMJ6CNM1uSJaUnbiXslN_kUVCGMbrPu2A/preset:view/plain/aad84b31648964ed647c9c81a804c357-2940030875541718631.jpg","https://cdn.chotot.com/qsZ11oSFUvMO-n-9op_eCruMHdVbZcw1-g0PtcqP56M/preset:view/plain/5e7292aeeacafc95b635717c97f1d74b-2940030875996401214.jpg"]}),

L(1264,"ho-chi-minh","th","Студия",6500000,40,
  "Новая студия, 40м², ул. Nguyễn Thị Thập, Tân Hưng — полная меблировка, рядом Lotte Mart, RMIT (тот же арендодатель, что и ниже, другой юнит в том же доме).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/130477275.htm","сегодня",0,source="chotot",
  details={"contact":"Trịnh Hoàng Tâm","photos":["https://cdn.chotot.com/48qHrhgqAkrRXICn7OEuA8N7uKHUKa1Kuz1ubKS4Hoo/preset:view/plain/d05e20009d1279d96cb7686689babf2e-2968424068002470207.jpg","https://cdn.chotot.com/0Fg1o5CWWx3LMcGAIOhO-ok3Ydn3gs1V9y7g1ywMfwE/preset:view/plain/dc614533f3bf00c9bcc2c9b0683b557e-2968424068556087760.jpg"]}),

L(1265,"ho-chi-minh","th","Студия",6200000,35,
  "Студия/1-спальная, 35м², ул. Nguyễn Thị Thập, Tân Hưng — полная меблировка, у Lotte Mart Q7, удобно до Q1/Q4 (тот же арендодатель, что и два юнита выше).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/123630043.htm","сегодня",0,source="chotot",
  details={"contact":"Trịnh Hoàng Tâm","photos":["https://cdn.chotot.com/t_nKXrJunCmMRqh0J5Ks1ZUrf9KjZP6ZC6N2cJFSdcU/preset:view/plain/1747b43095c09652e383cb352c00fd92-2922973718822785560.jpg","https://cdn.chotot.com/cGKa2SlPz8xLpF-ZxLyZmWB_pJ8U665OrMWv7Sw2Or8/preset:view/plain/f68a346c59848bc8aea74eddaf21f4fb-2922973719322947445.jpg"]}),

L(1266,"ho-chi-minh","th","Студия",5500000,28,
  "Студия с балконом и окном, 28м², đường số 85, Tân Hưng — свежий ремонт, полная меблировка (кондиционер, водонагреватель, стиральная машина, кухня), рядом Q1/Q4/Q8, Crescent Mall, SC VivoCity, Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/131641428.htm","сегодня",0,source="chotot",
  details={"contact":"Huỳnh Nguyễn Tuấn Anh","photos":["https://cdn.chotot.com/Dmh532panthub0njmu-oVWphYVNrM94vfy787A35oAM/preset:view/plain/c6e6c42a42e2c15014b20846fdbf96b8-2978597238520960727.jpg","https://cdn.chotot.com/b6jhCtgz94-Yf79uhS8mHsjNzOCaZepi3Vqpt1Ni6wc/preset:view/plain/b577aaea00fcfd489b5a25dcd7914866-2978597253503145687.jpg"]}),

L(1267,"ho-chi-minh","tm","Дом",12000000,99,
  "Дом целиком 4,5×22м (99м²), 1 этаж + 1 этаж выше, 2 спальни, переулок 378 Phạm Hữu Lầu, Tân Mỹ — новый, у моста Phước Long, подходит для долгосрочного проживания семьи или под офис.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134298880.htm","сегодня",0,source="chotot",
  details={"contact":"Hồ Phan Huy Châu","photos":["https://cdn.chotot.com/PhBLzVqpKTCXSv7Dk5VKalzcajFWQZ8FbGyrNpNx2SM/preset:view/plain/ad37a2c79412435c70da4311ba0b00db-2998766962753221017.jpg","https://cdn.chotot.com/pq_OxC6vIj9jysO81cXSqtt-8tQWj68EoqJO9ppIsmg/preset:view/plain/7b714b379cfdd885a91a8f2ee8498282-2998766963003262802.jpg"]}),

L(1268,"ho-chi-minh","th","Дом",8000000,32,
  "Дом целиком 4×8м (32м²), цоколь + 2 этажа + мансарда, 3 спальни/3 с/у, переулок ул. Trần Xuân Soạn, Tân Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134298676.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Vân BĐS","photos":["https://cdn.chotot.com/KZ8tGGusvZdg-RlZ3MpIkSnZRnCR3wzku8L6dbsLhIU/preset:view/plain/624aa78231f15107f0a70f912800975d-2998765185058622348.jpg","https://cdn.chotot.com/YmM05Ak9ttDcUBhEOyYe9ivDpV15uuVQtz0WsFzgVFk/preset:view/plain/ec8331908c7e1d05095393f254588142-2998765185102415698.jpg"]}),

L(1269,"ho-chi-minh","ak","Квартира",15000000,61,
  "2-спальная угловая квартира (2 с/у), 61м², ЖК Sky Thủ Thiêm, ул. Nguyễn Văn Hưởng, An Khánh (Thảo Điền) — сквозной ветер, два вида, полная меблировка, можно с животными.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134267580.htm","вчера",1,source="chotot",
  details={"contact":"Địa Ốc 084","photos":["https://cdn.chotot.com/HfbtuQ8vVj4-2s2gPOZPS_yXQJz--_Ucp0kwBf79gao/preset:view/plain/ec42287f78e94211fa0ef36876fd6f2d-2998556980288242611.jpg","https://cdn.chotot.com/7ax4kvWtKJMiPRuYZ2wnYQNTASH3mdr2FEBxdy9JtsQ/preset:view/plain/5ee23d2e812d7b6e36d605712cae70b4-2998556980143212429.jpg"]}),

L(1270,"ho-chi-minh","ak","Квартира",7900000,40,
  "1-спальная квартира, 40м², ул. Song Hành, An Khánh — рядом станция метро, вход по отпечатку пальца, камеры видеонаблюдения 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134298620.htm","сегодня",0,source="chotot",
  details={"contact":"Thanh Nhã","photos":["https://cdn.chotot.com/tvOBb9mx9nweBvNW6moH1m_5piCxjY8KPGCyRVW1ZWs/preset:view/plain/14ecff580e69580419b39bd527a70c05-2998764567492462418.jpg","https://cdn.chotot.com/OBJf8jS-V-Lx6yrAhF6TQJNZPvArtKmO6nVBUzHzmrk/preset:view/plain/406b8e7d0da4892f7c9b3e31f58d396b-2998764567966094653.jpg"]}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted daily HCMC check 22 aug 2026 (6th pass): 13 listings (chotot) across th(7)/ak(2)/tm(2)/kh(1)/bth(1)")
