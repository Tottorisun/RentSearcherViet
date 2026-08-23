# Daily HCMC check 23 Aug 2026 (2nd pass): 10 new listings across th(6)/ak(2)/kh(1).
# (This pass ran after an earlier same-day 1st pass already added IDs 1271-1290 from Chợ Tốt;
#  existing-URL dedup list was regenerated from the current rebuild_final.py before filtering.)
#
# SKIPPED (not added):
#   Chợ Tốt, bth (8 candidates, all commercial/non-residential despite ward-tagged "Phường Bến Thành"):
#     134303642 (kinh doanh và ở, ambiguous business-first title, skipped conservatively)
#     134263101, 134273209, 134273141 (Sang nhượng/Sang CHDV — business/lease-rights transfer, not a rental)
#     129227763, 134278624, 130913921 (explicitly "phù hợp văn phòng/spa/showroom", no residential layout)
#   133995884 (th, "MẶT TIỀN TIỆN KINH DOANH" storefront, no bedroom/layout info) — commercial, skipped.
#   134273245 (tm, office/teaching building, no bedrooms) — commercial, skipped.
#   133815199 (th, Trần Xuân Soạn 4x18m 3PN house, 12tr/72m2, agent "LHP") — confirmed same unit as
#     already-present L(783), same agent/street/price/area (re-pushed ad ID); skipped again.
#   Batdongsan: reachable today (HTTP 200, no Cloudflare block). Q1 apartment search page returned
#     only Bến Nghé/Đa Kao ward listings (new-map "Phường Sài Gòn"), none tagged Bến Thành. Q4 page's
#     Khánh Hội matches were all multi-unit broker "rổ hàng" catalog ads (Delasol/Millennium price
#     tiers for stu/1PN/2PN/3PN at once) with no single verifiable unit price/address — skipped per
#     no-fabrication rule. Bình Thạnh house search redirected (301) and returned no bq matches on retry.
#   Facebook: Marketplace request returned HTTP 302 (login-wall redirect), not attempted further.
#
NEW_SRC = r'''
L(1291,"ho-chi-minh","kh","Студия",6500000,30,
  "Студия/1-спальная, 30м², ул. Bến Vân Đồn, Khánh Hội (старый Q4) — полная меблировка (диван, ТВ, стиральная машина), балкон без прямого солнца, рядом NTT, UEL, удобно до Q1/Q7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133626066.htm","сегодня",0,source="chotot",
  details={"contact":"Lâm Nguyên","photos":["https://cdn.chotot.com/IMXffQp1B4wXG76QM-jtMVs6aTKiUHGjQbM6TE4Pqb8/preset:view/plain/829f73bf757c88645d45b76a4e32c0b5-2993672719379456563.jpg","https://cdn.chotot.com/TORkq450B4_F2bPiHx4SBl71NTD81DOW0HnXvTjgv1o/preset:view/plain/095cac0981f16b1518968c87861c75eb-2993672719591246501.jpg"]}),

L(1292,"ho-chi-minh","th","Квартира",6500000,40,
  "1-спальная квартира с балконом, 40м², ул. D1, KDC Him Lam, Tân Hưng — полная меблировка (кровать, диван, кондиционер, холодильник, стиральная машина, кухня), рядом Lotte Mart, Crescent Mall, SC VivoCity, RMIT, Tôn Đức Thắng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133824074.htm","сегодня",0,source="chotot",
  details={"contact":"Quang Vũ Unite","photos":["https://cdn.chotot.com/sWA9r5efLsCfV1eWh0k7NqfRUQq0G3cf_SM56lFQA8M/preset:view/plain/ad14ba70f190225dbbbce28bdeb07413-2995241838128161826.jpg","https://cdn.chotot.com/4MLOMTKKUV445mAsmVRg5rT0i7xFMn246cWgkW6bqGI/preset:view/plain/dda6a6d2509a676384c2a3ea41e34c26-2995241838262236695.jpg"]}),

L(1293,"ho-chi-minh","th","Студия",7200000,50,
  "Студия с балконом, современный дизайн, 50м², ул. Lâm Văn Bền, Tân Hưng — полная меблировка, рядом Lotte Mart, KDC Trung Sơn, ВУЗы TDT/RMIT/UFM.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133828759.htm","сегодня",0,source="chotot",
  details={"contact":"Trịnh Hoàng Tâm","photos":["https://cdn.chotot.com/5IjJwfsqy3N8jeoRKFrswqoUTpa1a4kgVpXTFgXcdQ4/preset:view/plain/fdb6590b73d73aa5cf18fce79940ddd2-2995262484551256441.jpg","https://cdn.chotot.com/fBILkMj-h-RWCe50wr8r6x1iqrDl--5yK-54B_sijhI/preset:view/plain/027ac436b165707e98302524145f5b0f-2995262484721815946.jpg"]}),

L(1294,"ho-chi-minh","th","Квартира",13500000,70,
  "2-спальная квартира с полной меблировкой и естественным освещением, 70м², ул. Lê Văn Lương, Tân Hưng — возможен вывод счёта (hoá đơn), сдаётся иностранцам.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133822811.htm","вчера",1,source="chotot",
  details={"contact":"sala thanh","photos":["https://cdn.chotot.com/DXOGWN7dorAY7PnLkn6tai7iudFQKwY8Xw4hFk7apY0/preset:view/plain/c03f55f8b80b58ca4a6492a2feaedc8f-2995234433653482191.jpg","https://cdn.chotot.com/GbejLpVnacOdzGMKEt3mSMolE5EoNMv25obW-ICxT6w/preset:view/plain/386e0ac92dc5015d239bf0808285ebdf-2995234432220326145.jpg"]}),

L(1295,"ho-chi-minh","th","Квартира",6500000,40,
  "1-спальная квартира в новом сервисном доме, 40м², ул. Số 5, KDC Kim Sơn, Tân Hưng — новая меблировка (кровать, диван, ТВ, шкаф, стиральная машина, кондиционер-инвертор), рядом Nguyễn Hữu Thọ, RMIT, Tôn Đức Thắng, Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133940949.htm","вчера",1,source="chotot",
  details={"contact":"Danh Conal Unite","photos":["https://cdn.chotot.com/lFLxixoTYGJwD7B95TVV7cRgeEJIUFDrJoXjIlnxeNY/preset:view/plain/199b554ecd1e430786793de057cea445-2996122808401905124.jpg","https://cdn.chotot.com/T0y7JIEILgMfWU5X3uzKLhQPVf3QwI81foBLfqtAFLw/preset:view/plain/f943dfef35daaf6ef42454c6b1d651c9-2996122808508631417.jpg"]}),

L(1296,"ho-chi-minh","th","Дом",11000000,75,
  "Дом фасадом на улицу, 75м² (ширина 9м), 3 спальни/2 с/у, ул. 49, Tân Hưng — просторный, светлый.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134305417.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении дом позиционируется как торговая площадь (mặt tiền buôn bán), но по планировке (3 спальни/2 с/у) подходит и для обычного проживания","contact":"Vinh Trần","photos":["https://cdn.chotot.com/b33T0rY4i3EMmbaSoxlezxof-LlknYh8ckab7HoAAzI/preset:view/plain/bb238f0a130656cba7716c7c4618290e-2998855584109420764.jpg","https://cdn.chotot.com/2JW9dT0nocK-B0nhNi8Uu6JvDTxlp6dO_W8eAzVc9f4/preset:view/plain/efad94c5d7cbe4efda843f6d9f1df95e-2998855584948332563.jpg"]}),

L(1297,"ho-chi-minh","th","Дом",25000000,276,
  "Дом целиком 4×20м, 1 этаж + 3 этажа, 5 спален с отдельными санузлами, базовая меблировка, KDC Tân Quy Đông рядом ул. Nguyễn Thị Thập и Lotte Mart, Tân Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133982571.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении отмечена возможность использовать под офис/спа/шоурум наравне с семейным проживанием","contact":"Dương Khang","photos":["https://cdn.chotot.com/uVnrFS2CC2MlvR-ucXDng5Ro32VFRVMSXumhM5cmvx4/preset:view/plain/c90d8a06331e05e9fed5cf6a4846129e-2996419598738061188.jpg","https://cdn.chotot.com/Lt4N4nWpRznz-QjAteW1pAialUbN53aK6tF_rYcA2kE/preset:view/plain/bd7b94000d799876ae65abf4ab42ac9b-2996419599526547896.jpg"]}),

L(1298,"ho-chi-minh","th","Дом",25000000,72,
  "Дом целиком 4×18м, 1 этаж + 3 этажа, 4 спальни/3 с/у, базовая меблировка, фасадом на đường số, Tân Hưng (новый) — рядом другие районы Q7.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133983597.htm","вчера",1,source="chotot",
  details={"contact":"LHP","photos":["https://cdn.chotot.com/ihdVwx-rgOCSBg0MVTRccckbzdH8JRQiY69D3FybpsU/preset:view/plain/f3ef62b4d035e7ab314d28c975aae9e0-2996424223910067953.jpg","https://cdn.chotot.com/OOzn6A8GkV9xjyBNYhyFRvKZA1NNdHikDE-hEpbWiqs/preset:view/plain/2e953a498006b220deec3af3dbd59403-2996424224061631642.jpg"]}),

L(1299,"ho-chi-minh","ak","Квартира",9500000,45,
  "1-спальная квартира с балконом, 45м², ул. Quốc Hương, An Khánh (Thảo Điền) — рядом станция метро, лифт, охрана 24/7, общий холл, новая полная меблировка (диван, большой холодильник, кондиционер).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133705114.htm","сегодня",0,source="chotot",
  details={"contact":"Phan Trung Thực Apartment D2","photos":["https://cdn.chotot.com/fYh9o7_4NL9dnX10oaW2zyU0NgP7i3PinLZNtVvN48o/preset:view/plain/212ab4879d79befb74b8493780d464b6-2995100456833308420.jpg","https://cdn.chotot.com/k0E_H_qppyp72oJe5WMDQXtOQo-b2rc_YFYGwCtogqo/preset:view/plain/e3eb53fbd1b208d013906d4865e81b47-2995100456750273392.jpg"]}),

L(1300,"ho-chi-minh","ak","Квартира",20000000,72,
  "2-спальная квартира в Masteri Thảo Điền, 72м², вид с балкона на реку Сайгон и центр города — полная качественная меблировка (ТВ, диван, холодильник, стиральная машина, СВЧ, кровать, шкаф), бассейн (3 этаж)+BBQ, спортзал, теннис, баскетбол, парк бесплатно, цена по договорённости.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/129313705.htm","сегодня",0,source="chotot",
  details={"contact":"Ánh Trang","photos":["https://cdn.chotot.com/OyKOlSz16XR54LwjQNAQd-qfLA29CB5lrtOEIR2YQrg/preset:view/plain/1b2242153219cb74ce45011ecddb35ac-2959737416373472147.jpg","https://cdn.chotot.com/UhQwWdIUbUYgsllcQGK6_Ya-rybk0K4SstmDaYg4EJQ/preset:view/plain/47d5dabbf54342e19acb66b98787ec89-2959737416250337065.jpg"]}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted daily HCMC check 23 aug 2026 (2nd pass): 10 listings (chotot) across th(6)/ak(2)/kh(1)")
