# -*- coding: utf-8 -*-
"""Daily HCMC check, 4 Sep 2026. Chợ Tốt sweep across ak/btr/th/tm/bq/bth/kh
(area_v2=13102 Q7, 13119 Thủ Đức, 13109 Bình Thạnh, 13096 Q1, 13099 Q4;
cg=1010/1020/1050/1030) found 1123 raw matches; after fixing an ms-vs-s unit
bug in the freshness calc (orig_list_time is milliseconds, not seconds --
first pass wrongly treated everything as fresh), filtering to <=3 days via
orig_list_time and deduping against every URL already in rebuild_final.py,
10 were genuinely new: tm 5, ak 2, th 1, btr 1, bth 1. All 10 verified FRESH
by check_freshness.py. Nothing fresh today in bq or kh.

Batdongsan was NOT blocked today (no Cf-Mitigated challenge). A same-ward
sweep (5 districts x 5 categories) matched 22 cards by ward-name substring,
but the substring test caught a false positive (a Q7 house ad merely
*mentioning* "gần chợ Tân Mỹ" while its own URL ward slug is Bình Thuận --
dropped). Product IDs have no published date, so freshness was estimated
against the highest batdongsan prid already stored in the file (46254842,
itself committed today) plus each ad's gallery-image upload-date path
(2026/09/03 or /09/04): 6 candidates cleared both checks, but one more
(prid 46256993, "Bình Quới") was dropped after its own body text named the
ward "Bình Lợi Trung" -- a different ward the street-name/old-ward-number
guess had missed. Final 5: th 1, bth 2, ak 2. Every batdongsan row carries
a notice: the site publishes no original post date, only a same-day/next-day
estimate from the id and photo timestamps.

RACE CONDITION, resolved after the fact: another session (rent-searcher-31)
ran the identical daily check concurrently and independently found 9 of
these same 10 Chợ Tốt ads plus one more (batdongsan pr46255069, Sunrise
City, th) -- see new_listings125.py, which THIS script's insert_listings()
call originally ran under before the collision was noticed (both scripts'
inserts succeeded, since they used disjoint ids: 1000450-1000464 here vs
1000465-1000474 there). The result was 9 exact-duplicate listing pairs in
rebuild_final.py (same source URL, two different internal ids -- one exact
URL match slipped past a naive string-equality dedup check too, because the
two sessions built slightly different nhatot.com slugs -- "thu-duc" vs
"thanh-pho-thu-duc" -- for the same list_id 122583044). Fixed by directly
deleting the 9 redundant L(...) rows for ids 1000465,1000466,1000467,
1000468,1000469,1000470,1000472,1000473,1000474 from rebuild_final.py
(kept the lower/this-batch id in each pair), while keeping the one
genuinely unique row from the other session, id 1000471 (Sunrise City).
Coordinated with rent-searcher-31 via SendMessage before touching the file
further, so neither session ran purge/rebuild/geocode/commit twice.

Facebook: not attempted from here (headless, no logged-in session -- see
facebook_check_prompt.txt for the attended pass and why it can't run here).

NOTE: by the time this file was written, new_listings125.py already held
rent-searcher-31's content and insert_listings() had already run (for both
batches). This file is kept as the accurate historical record of what THIS
session's sweep found and inserted; running it again would fail (ids
already in rebuild_final.py), which is correct -- it is not meant to be
re-run."""
from listing_lock import insert_listings

IDS = [1000450, 1000451, 1000452, 1000453, 1000454, 1000455, 1000456, 1000457, 1000458, 1000459, 1000460, 1000461, 1000462, 1000463, 1000464]

NEW_SRC = '''
L(1000450,"ho-chi-minh","tm","Студия",3500000,16,
  "Студия («căn hộ dịch vụ»), 16 м², ул. Phạm Hữu Lầu, KDC Tân Thành Lập, Tân Mỹ (Q7). Новая мебель: кондиционер, шкаф, рабочий стол, отдельная стиральная машина и место для сушки, просторная кухня.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/129561857.htm","сегодня",0,source="chotot",
  descEn="Studio (\\"căn hộ dịch vụ\\"), 16m², Phạm Hữu Lầu St, KDC Tân Thành Lập, Tân Mỹ (Q7). New furnishings: AC, wardrobe, desk, private washing machine and drying area, spacious kitchen.",
  details={"photos": ["https://cdn.chotot.com/iVScmWPL5QWx7DU3g0r5Vw9FPkXXny6vLWnBYn0DZKc/preset:view/plain/1d0659d69f3d1c5ca1a83065a067b592-2996588609382801089.jpg", "https://cdn.chotot.com/QyCUX4Kt6N9Y62nHu0GwYNMLv05TObvs8I3RD6BkwBw/preset:view/plain/fd995a12d7d391a29413201d7e8c994c-2996588595969183009.jpg", "https://cdn.chotot.com/P2Rky4doj2hh0olqIIH76R1Y_UkjVZEKirjuwcmnqr4/preset:view/plain/6a95b645d8f0bb6eaa594cbfadb8092f-2996588619785002689.jpg", "https://cdn.chotot.com/UuDcrfGslD0GqXZFTpUUenEvlvS9VlzxiD9HlABXM6c/preset:view/plain/e1443c59fa47aef79020300dc3f9d51a-2994940405845813423.jpg", "https://cdn.chotot.com/Enr8UC9Ja7PqJPvg6bZ_4jWyo0xjRTuiN-6yyFz026A/preset:view/plain/85d1ef9573d5ab7ccb09bc636a2bbabf-2994940406068682680.jpg"]}),
L(1000451,"ho-chi-minh","tm","Квартира",11000000,70,
  "2-спальная квартира, 70 м², ЖК Q7 Boulevard, ул. Nguyễn Lương Bằng, Tân Mỹ. Агентство сдаёт несколько планировок в комплексе: 1-спальная от 9 млн, 2-спальная от 11 млн (полная меблировка — 13,5 млн), 3-спальная от 13 млн.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134166757.htm","вчера",1,source="chotot",
  descEn="2-bedroom apartment, 70m², Q7 Boulevard complex, Nguyễn Lương Bằng St, Tân Mỹ. Agency listing covering several unit types in the complex: 1-bedroom from 9M, 2-bedroom from 11M (13.5M fully furnished), 3-bedroom from 13M.",
  details={"notice": "Объявление агентства с несколькими вариантами планировок — уточняйте конкретный этаж и вид при звонке.", "noticeEn": "Agency listing covering several unit configurations in the complex — confirm the exact floor and view when calling.", "photos": ["https://cdn.chotot.com/ACRmlqoo3yA6g9VQzqr5_RvuZbKEfu4iMn7qAouZvko/preset:view/plain/0d83178fa85621ee27107572ac679da3-2997826725660047651.jpg", "https://cdn.chotot.com/iz99ub8HbOdii8R5mkyj9gD1wTXRxVGGsRUxBoMiF1M/preset:view/plain/ff54ca1a2c9a4e67cc544f7571411383-2997826724528520279.jpg", "https://cdn.chotot.com/k7JCa-cGPMO54z-IKatAkWBVIjdiTMFEYt9ntncbbLM/preset:view/plain/dc71a1cc45614961bd7ff3cc22c6fdf0-2997826724516328139.jpg", "https://cdn.chotot.com/hvprqvowDbE09PwViO8N_OTAjmTK4BmIM9NlciVcGB8/preset:view/plain/bdd6950f64f770da5f0d0809b668a3d9-2997826724602075525.jpg", "https://cdn.chotot.com/7T87_2VFk811z94cw2oVm7ZfAxRGXZ_tu1v3iGRB6do/preset:view/plain/1c7162ea91e880bf102370aade8e8503-2997826724698820313.jpg", "https://cdn.chotot.com/kxD0yZSzuGeDZcIvbzCmxa49qiKRPD2n10EkX65bW6M/preset:view/plain/b08a5cfd041885c53ae03a298f84b8e0-2997826725726817574.jpg"]}),
L(1000452,"ho-chi-minh","tm","Квартира",16000000,75,
  "2-спальная квартира (2 с/у), 75 м², ЖК Sunshine Sky City, 23 Phú Thuận, Tân Mỹ (Q7). Полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134483749.htm","вчера",1,source="chotot",
  descEn="2-bedroom apartment (2 bathrooms), 75m², Sunshine Sky City complex, 23 Phú Thuận, Tân Mỹ (Q7). Fully furnished.",
  details={"photos": ["https://cdn.chotot.com/pyatqAIwRiaDuNKuVY6wh-mv1doRF9man_3jeiFB308/preset:view/plain/8c44e1d19934b85c7873eaa1681cae9b-3000450808745918259.jpg", "https://cdn.chotot.com/uD_Ll4hL_o9slCOQMwweG_VHgLMHha4yXlxH_rMBkiA/preset:view/plain/7bb8e27b9e7a03c2c9194d48d9d00066-3000450808544939878.jpg", "https://cdn.chotot.com/V13z4A6T-AXUSUaOS3xdHES2ZKL7xo668kAd46FTCn8/preset:view/plain/b50d5bb4e8a5031af2d20ec5061ca21a-3000450808710430766.jpg", "https://cdn.chotot.com/n0NQwmv4jFa98RHL9eNEjnDCXVjlPWB8Ia6B_mP4srs/preset:view/plain/5e34b3f806f4a60e5b796a985ba5b2ca-3000450809331253294.jpg"]}),
L(1000453,"ho-chi-minh","th","Квартира",13000000,131,
  "3-спальная квартира, 131 м², ЖК Quốc Cường Gia Lai 1, ул. Trần Xuân Soạn, Tân Hưng. Базовая меблировка, хороший вид, просторно.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134489768.htm","вчера",1,source="chotot",
  descEn="3-bedroom apartment, 131m², Quốc Cường Gia Lai 1 complex, Trần Xuân Soạn St, Tân Hưng. Basic furnishings, good view, spacious.",
  details={"photos": ["https://cdn.chotot.com/T_c9oi9KDxCsWQvHgz-LEFOpy3CZsPVmosNeFucLMyU/preset:view/plain/d50f348d2f19c65e43f72c75b07fdf77-3000481830307544928.jpg", "https://cdn.chotot.com/Ma-7fibYh91ZHecIe-FF0HUgE3rzTcsiFcaSxEGAdps/preset:view/plain/f0efaf76e30b102065f87dc3dce1bc18-3000481831562243024.jpg", "https://cdn.chotot.com/bNbt8uj9NFZ6wKWN7Zur9eH_T68eRuV307NOWgYuQ0M/preset:view/plain/2ee3f918e9cd768b7bb934b32392f88e-3000481831408828462.jpg", "https://cdn.chotot.com/sKyD4YpbbIGpB_EUL1sHdUNdmsjxkfKlzqxYQwTljK4/preset:view/plain/19d6cd6cb750408c57481937367eb3f6-3000481830254829630.jpg", "https://cdn.chotot.com/e3ga63nm_R5rAAoG8hmpbl_25wDockkc75ydhk0vIuE/preset:view/plain/87faf1f0187fd13fa48abc50dfc71c5b-3000481830390755747.jpg", "https://cdn.chotot.com/RV1WEJXndqCvuHjUmye3R6iwKLfptdz4OC7_lNEX4mg/preset:view/plain/fd3f057912a07d6abc74275260dacacb-3000481831540937119.jpg"]}),
L(1000454,"ho-chi-minh","tm","Квартира",9000000,80,
  "2-спальная квартира (2 с/у), 80 м², ЖК Belleza, ул. Phạm Hữu Lầu, Tân Mỹ (Q7). Базовая меблировка, просторная и светлая, для семьи. В комплексе бассейн, парк, супермаркет, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134481798.htm","вчера",1,source="chotot",
  descEn="2-bedroom apartment (2 bathrooms), 80m², Belleza complex, Phạm Hữu Lầu St, Tân Mỹ (Q7). Basic furnishings, spacious and airy, family-friendly. Complex has a pool, park, supermarket, 24/7 security.",
  details={"photos": ["https://cdn.chotot.com/uYjhIbdv1ebD0FUgWF5UAkoy1DkvMaBc0ixuX_v8d3A/preset:view/plain/1b02a3a4535e41af92e37b14034b3696-3000441867309047687.jpg", "https://cdn.chotot.com/V7_xl-0uqegCdsWHzGFx7QlpaNDLnegwFIml5yC2-Ps/preset:view/plain/98866816647be3b7c879f757e72b2978-3000441879972023284.jpg", "https://cdn.chotot.com/RsMhbZRuSmlUEKzxHyM3y-Kbt7kZ3AgU1SIPvXbjoN0/preset:view/plain/41f0bd72a7fed7ce14287d072e7d625c-3000441890295163305.jpg", "https://cdn.chotot.com/wHjMLmO-qMW83Y56Tul4ZYJIzMF-uJC3HAsYI8UrF1o/preset:view/plain/e0f55031e938328d03cc503b96242086-3000441901065199495.jpg"]}),
L(1000455,"ho-chi-minh","tm","Студия",5800000,35,
  "Студия («căn hộ dịch vụ cao cấp»), 35 м², комната №202, 16 Đường số 1 (заезд с 233 Phạm Hữu Lầu), Tân Mỹ (Q7). Кухня со шкафами, кондиционер, холодильник, просторный балкон, терраса для сушки белья, бесплатная стирка.",
  "https://www.nhatot.com/thue-phong-tro-quan-7-tp-ho-chi-minh/134487108.htm","вчера",1,source="chotot",
  descEn="Studio (\\"premium service apartment\\"), 35m², room #202, 16 Đường số 1 (entrance from 233 Phạm Hữu Lầu), Tân Mỹ (Q7). Kitchen with cabinets, AC, fridge, spacious balcony, rooftop drying terrace, free laundry.",
  details={"photos": ["https://cdn.chotot.com/IcYGUhD1sRg7I7K03cFsao4Ujwpkfa6t5ZSVBZWVKC0/preset:view/plain/8271d8e52b35cacd2fcd3cb03579d3c5-3000468495231199045.jpg", "https://cdn.chotot.com/28wocZIZ-fHNfNDDrB9jiTINcewV2JEdoeLoGJtrcMA/preset:view/plain/5fc14d9b298bafeb8e4fdc1a63c2559f-3000468495344230279.jpg", "https://cdn.chotot.com/IzYhE6Lnfmf9X5UqJb-ULkFdLNZqU4MaVmvgwIBzGsc/preset:view/plain/f010bee98b0db4665ff85216afd8aff2-3000468495315168727.jpg"]}),
L(1000456,"ho-chi-minh","ak","Квартира",7000000,30,
  "1-спальная квартира, 30 м², ул. Trần Não, An Khánh, у подножия моста Sài Gòn. Новый ремонт, современный дизайн, просторно; быстрый выезд на Mai Chí Thọ и в тоннель Thủ Thiêm, рядом An Phú, Thảo Điền, Bình Thạnh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134155495.htm","вчера",1,source="chotot",
  descEn="1-bedroom apartment, 30m², Trần Não St, An Khánh, at the foot of the Sài Gòn Bridge. Newly renovated, modern design, spacious; quick access to Mai Chí Thọ and the Thủ Thiêm tunnel, near An Phú, Thảo Điền, Bình Thạnh.",
  details={"photos": ["https://cdn.chotot.com/FLDRUBnRjtKRfVWRkbd4EOBo2we8apvd7cWuy83e9IA/preset:view/plain/a87a4b83a858c2f8663fb4cc8aa5c226-2997717931783903621.jpg", "https://cdn.chotot.com/yf7JPF4eLTok_R17KIejzsxxahGJQLeSPpl_tUhvogA/preset:view/plain/8c570aec821560200ceacb5f79d3168c-2997717973841877454.jpg", "https://cdn.chotot.com/dY1N5gd96GD4pg3mM9pPTotFoN5wHbMpB-ZaO5IWNpY/preset:view/plain/5be6262e7f718e53d6c861c1d46cbc49-2997717973851574173.jpg", "https://cdn.chotot.com/Pv5c5J5hJ3U03LuTGDkW338y0pi-TiK4zeVTt-ghRtQ/preset:view/plain/7b93dd2461c51c9a7a126be56151c289-2997717973710035320.jpg", "https://cdn.chotot.com/SmcraEm_QXiH0LLj7zKQm9RBux2_JiKl0YKIfZFB6To/preset:view/plain/bff59038e28104322fdf150a7940300a-2997717973700452774.jpg", "https://cdn.chotot.com/uT5jTSZOHcOCUGrgw5o6OuAszGqeK7Arnn78BQXJWFs/preset:view/plain/fbdb264cc62a409c32f5cc5ba2e15507-2997717973828655493.jpg"]}),
L(1000457,"ho-chi-minh","btr","Комната",2000000,20,
  "Комната, 20 м², первая линия ул. Nguyễn Duy Trinh, Bình Trưng. Свободный график заселения, рядом больница, школа, рынок, напротив Bách Hóa Xanh. Приоритет долгосрочной аренде, без посредников.",
  "https://www.nhatot.com/thue-phong-tro-thanh-pho-thu-duc-tp-ho-chi-minh/122583044.htm","сегодня",0,source="chotot",
  descEn="Room, 20m², street-front on Nguyễn Duy Trinh St, Bình Trưng. Move in anytime, near a hospital, school, market, opposite a Bách Hóa Xanh store. Long-term tenants preferred, no agent fee.",
  details={"photos": ["https://cdn.chotot.com/EvVrKZRQMVH942qXNQFALNIu07qxP9moxd84f8jWKtE/preset:view/plain/d7b4890b82e2265a310738bf195b5edf-2916714585834329773.jpg", "https://cdn.chotot.com/Z1CYuk_vgfgkl_DcqXkCaK3FsZ-39DdQDfrbqQsKuuI/preset:view/plain/09d5a1e38a1e74cc06bcdc3d3e9949bb-2916714585948134155.jpg", "https://cdn.chotot.com/t2cLAUNXdywjkWqM1hjRtUlcsaSbWcOGm3oTtO5rmtw/preset:view/plain/05ea6849864ba686b88e0d2fcdb0effb-2916714586820614923.jpg", "https://cdn.chotot.com/871YVwdKS6gOJfBfsx4StBWNEx0hRpu_W3fRiSCyvDw/preset:view/plain/61ae477dfd2440a1c514a05440d70022-2916714586841028269.jpg", "https://cdn.chotot.com/VhzYhNxmiakXoG-Ej67LN3gXXAmArXnpi_WG836rLKo/preset:view/plain/23ad4455c1a32934143adf2f207278f3-2916714587609209611.jpg", "https://cdn.chotot.com/ATzFs6xYyge62scXoXbByCIUG8b4u46Y4iDjQqfOVFc/preset:view/plain/7b67e792c0b7023257cd6d77860ec557-2916714587629622957.jpg"]}),
L(1000458,"ho-chi-minh","ak","Склад",10000000,80,
  "Склад, 80 м², ул. Lương Định Của, An Khánh — рядом развязка An Phú и ул. Mai Chí Thọ. Заезд для грузового автомобиля, подходит для хранения товара и логистики.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-thanh-pho-thu-duc-tp-ho-chi-minh/134484194.htm","вчера",1,source="chotot",
  descEn="Warehouse, 80m², Lương Định Của St, An Khánh — near the An Phú interchange and Mai Chí Thọ St. Truck access, suits storage and logistics use.",
  details={"photos": ["https://cdn.chotot.com/BoE6oDZw225-jDwx_N4hmJRXclm5Z6olUl91AijLOA0/preset:view/plain/856e404ef00557b4a8293d2af60ab29b-3000452001805904264.jpg", "https://cdn.chotot.com/0SSH2ZptW4PyDD1WnRmteJJtCF3dCj2wUB6qTo_mOPw/preset:view/plain/bb55e7b0b16a23f471489e5c8d29212c-3000452002007965575.jpg", "https://cdn.chotot.com/st_2FHJ7WiKTtIvT_NM4y0HX92oeIBQ1-eSf1H0WXwo/preset:view/plain/316e6ac0e2ecbc12d185682997d7f5e6-3000452002123284526.jpg", "https://cdn.chotot.com/8KA6zE3MlZ6vzxxhLg9qEPs9TXyi6Vz-5hFkLrrhlEY/preset:view/plain/a6b745119900afa1e511b7c59d7cc148-3000452002150809445.jpg", "https://cdn.chotot.com/-1TxLgskUXCAb5eiuoIpzDPF3cuv09J2QBiSFRJg71Q/preset:view/plain/eb10f361c384412cec2a5c994d0d5a3d-3000452002177657257.jpg", "https://cdn.chotot.com/UjJ3NAzhbz1vc_33_OCgO1__nTwf5x8ubg-5opLAonc/preset:view/plain/734e14f049bdd20ece2cc89aad41445b-3000452002092142438.jpg"]}),
L(1000459,"ho-chi-minh","bth","Торговая площадь",100000000,800,
  "Торговая площадь на первой линии ул. Lê Thánh Tôn, у рынка Bến Thành, 8×20 м с расширением, 3 этажа, 800 м². Плотный поток людей, рядом офисные центры, супермаркеты; подходит под офис, банк, ресторан, стоматологию, языковую школу, салон красоты. Сдаётся целиком или частями.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-quan-1-tp-ho-chi-minh/133656659.htm","вчера",1,source="chotot",
  descEn="Street-front retail space on Lê Thánh Tôn St, near Bến Thành Market, 8x20m widening lot, 3 floors, 800m². Heavy foot traffic, near office towers and supermarkets; suits an office, bank, restaurant, dental clinic, language school, or beauty salon. Available whole or in parts.",
  details={"photos": ["https://cdn.chotot.com/KQAHQYKwyGFuR0qVZw7bHtQw2ZeW-gwaQJ8Nr2iNCUs/preset:view/plain/dbdf9236ae1b05ea746644650e0b1975-2993957101190727095.jpg", "https://cdn.chotot.com/sqId6f5x5IhpxUkhtu77KlV86wvlTU_HhLzHGzkKIvU/preset:view/plain/ece14ee808fa93d5a0c43ea1d6cfe8ce-2993957101397558839.jpg", "https://cdn.chotot.com/1H5pfFa0_l2bdKj1wv0CNDjoKOzamlkIPnbv9AmSYxE/preset:view/plain/dd4a2ee4050136ae000c26975f6498f5-2993957101376152290.jpg"]}),
L(1000460,"ho-chi-minh","th","Дом",50000000,100,
  "Таунхаус целиком, 100 м², ул. Trần Xuân Soạn, Tân Hưng — рядом Lotte Mart Nam Sài Gòn и ЖК Sunrise City View, выезд на Nguyễn Hữu Thọ. 7 спален, 4 санузла, широкая дорога для машины и грузовика, тихий район.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-tran-xuan-soan-phuong-tan-hung-14-59/cho-moi-7pn-4wc-50-trieu-100m2-tai-p-q7-hcm-pr46250636","вчера",1,source="batdongsan",
  descEn="Whole townhouse, 100m², Trần Xuân Soạn St, Tân Hưng — near Lotte Mart Nam Sài Gòn and the Sunrise City View complex, access to Nguyễn Hữu Thọ St. 7 bedrooms, 4 bathrooms, wide car/truck-accessible street, quiet area.",
  details={"notice": "Batdongsan не публикует дату объявления; возраст оценён по номеру объявления и дате фото в галерее (~1 день).", "noticeEn": "Batdongsan doesn't publish a post date; age estimated from the listing ID and gallery photo timestamps (~1 day).", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903105031-210f_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903105031-5c4b_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903105031-a2ae_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903105031-e346_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903105031-3e34_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903105031-4148_wm.jpg"]}),
L(1000461,"ho-chi-minh","bth","Студия",4700000,18,
  "Студия, 18 м², центр Q1 (Bến Thành) — рядом рынок Bến Thành, ул. Bùi Viện, мост Ông Lãnh, несколько минут до Q3/Q10/Q4. Полная меблировка «как на фото», 2 этаж без лифта, общая стиральная машина на первом этаже, тихий охраняемый дом.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-co-giang-phuong-co-giang-53/trong-sinh-vien-4x-full-tien-nghi-y-anh-chi-phi-hssv-vi-tri-trung-tam-gan-cho-ben-thanh-q1-pr46254902","сегодня",0,source="batdongsan",
  descEn="Studio, 18m², central Q1 (Bến Thành) — near Bến Thành Market, Bùi Viện St, Ông Lãnh Bridge, minutes from Q3/Q10/Q4. Fully furnished \\"as pictured\\", 2nd floor walk-up, shared washing machine on the ground floor, quiet guarded building.",
  details={"notice": "Batdongsan не публикует дату объявления; возраст оценён по номеру объявления и дате фото в галерее (~сегодня).", "noticeEn": "Batdongsan doesn't publish a post date; age estimated from the listing ID and gallery photo timestamps (~today).", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/09/04/20260904102058-e6ef_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/04/20260904102104-c71a_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/04/20260904102104-e79c_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/04/20260904102104-5ea4_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/04/20260904102104-38a1_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/04/20260904102104-4437_wm.jpg"]}),
L(1000462,"ho-chi-minh","bth","Офис",84400000,200,
  "Офис, 200 м², новое здание Atlas, ул. Phó Đức Chính, Q1 — рядом рынок Bến Thành, банковская улица Hàm Nghi, станция метро Bến Thành. Панорамное остекление, подвесной потолок со светодиодной подсветкой, центральный кондиционер, сдаётся с открытой планировкой или перегородками по запросу. Цена — расчётная (422 тыс. ₫/м²/мес × 200 м²).",
  "https://batdongsan.com.vn/cho-thue-van-phong-pho-pho-duc-chinh-phuong-nguyen-thai-binh-53/cho-toa-moi-atlas-uc-quan-1-sat-cho-ben-thanh-metro-ham-nghi-pr46249614","вчера",1,source="batdongsan",
  descEn="Office, 200m², new Atlas building, Phó Đức Chính St, Q1 — near Bến Thành Market, the Hàm Nghi banking street, and Bến Thành metro station. Floor-to-ceiling glazing, suspended LED ceiling, central AC, open-plan or partitioned layout on request. Price is computed (422,000₫/m²/month x 200m²).",
  details={"notice": "Batdongsan не публикует дату объявления; возраст оценён по номеру объявления и дате фото в галерее (~1 день). Цена расчётная — уточняйте у арендодателя.", "noticeEn": "Batdongsan doesn't publish a post date; age estimated from the listing ID and gallery photo timestamps (~1 day). Price is computed per-sqm -- confirm with the landlord.", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903084615-ade0_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903084615-ed04_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903084615-55dc_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903084615-3047_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903084615-29f9_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903084615-6639_wm.jpg"]}),
L(1000463,"ho-chi-minh","ak","Дом",45000000,120,
  "Дом целиком, 6×20 м с расширением до 7,5 м, 1 этаж + 2 этажа, 5 спален, ул. Cao Đức Lân, An Phú (An Khánh), рядом бывший Q2. Широкая дорога для машины и грузовика; подходит и под офис компании или студию.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-cao-duc-lan-phuong-an-phu-1-71/gia-45-trieu-thang-cho-khanh-q2-gan-uc-lan-pr46253494","вчера",1,source="batdongsan",
  descEn="Whole house, 6x20m widening to 7.5m, ground floor + 2 upper floors, 5 bedrooms, Cao Đức Lân St, An Phú (An Khánh), near the former Q2. Wide car/truck-accessible street; also suits a company office or studio use.",
  details={"notice": "Batdongsan не публикует дату объявления; возраст оценён по номеру объявления и дате фото в галерее (~1 день).", "noticeEn": "Batdongsan doesn't publish a post date; age estimated from the listing ID and gallery photo timestamps (~1 day).", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903215012-0a8c_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903215036-0e1a_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903215036-6111_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903215037-1f6d_wm.jpg"]}),
L(1000464,"ho-chi-minh","ak","Офис",145000000,1200,
  "Офисное здание, 1200 м² (10×20 м, подвал + 4 этажа + крыша), первая линия ул. Lương Định Của, An Khánh (бывш. Q2). Лифт, пожарная сигнализация, кондиционеры, генератор; подходит под банк, шоурум, ресторан, языковой центр, клинику, спа. Срок аренды 5-10 лет.",
  "https://batdongsan.com.vn/cho-thue-van-phong-phuong-an-khanh-2/toa-nha-1-200m2-mat-tien-quan-2-pr46256729","вчера",1,source="batdongsan",
  descEn="Office building, 1200m² (10x20m, basement + 4 floors + roof), street-front on Lương Định Của St, An Khánh (former Q2). Elevator, fire alarm system, AC, generator; suits a bank, showroom, restaurant, language center, clinic, or spa. 5-10 year lease term.",
  details={"notice": "Batdongsan не публикует дату объявления; возраст оценён по номеру объявления и дате фото в галерее (~1 день).", "noticeEn": "Batdongsan doesn't publish a post date; age estimated from the listing ID and gallery photo timestamps (~1 day).", "photos": ["https://file4.batdongsan.com.vn/crop/600x315/2026/09/04/20260904100553-0bf9_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903223301-9fea_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903223301-b4b6_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903223301-911b_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903223301-41c6_wm.jpg", "https://file4.batdongsan.com.vn/crop/600x315/2026/09/03/20260903223301-3c0b_wm.jpg"]}),
'''

if __name__ == "__main__":
    raise SystemExit("already applied under the original filename before the new_listings125.py collision was noticed -- do not re-run; kept for history only")
