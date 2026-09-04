# -*- coding: utf-8 -*-
"""SUPERSEDED -- do not run. Kept only as an audit trail.

Daily HCMC check, 4 Sep 2026: this batch (originally 8 listings across Tan
My/Tan Hung (Q7), Binh Trung (An Phu east), Ben Thanh (Q1), Chợ Tốt source)
was written and run as new_listings114.py and successfully inserted (ids
1000369-1000376, verified unique in rebuild_final.py) via the locked
insert_listings(). A second, concurrent instance of this exact daily check
was running on the same machine at the same time -- confirmed by
allocate_ids.py handing it the very next block, 1000377-1000385, for an
IDENTICAL set of 8 source ads (same Chợ Tốt list_ids, same buildings/streets)
plus one more this run had missed (133424510, a Sinh Lợi/Trung Sơn room) --
and it independently picked the same "next number" (114) for its own batch
file, overwriting new_listings114.py on disk with its own content.

The id-allocation and insertion themselves were unaffected by the race
(allocate_ids.py/insert_listings are lock-protected precisely for this
scenario, per their own docstrings) -- both batches landed cleanly with no
duplicate internal ids. But since both sessions had independently fetched
and vetted the SAME real-world Chợ Tốt ads, the result was 8 genuine
same-URL duplicates sitting in rebuild_final.py under two different id
ranges. Caught by the post-rebuild duplicate-URL check (rebuild_final.py's
own "N URLs shared by several listings" line jumped by exactly 8 against
the pre-existing legacy-debt baseline). Resolved by keeping the other
session's superset batch (1000377-1000385, in its new_listings114.py) and
removing this one via listing_lock.remove_listings([1000369..1000376]).

This file is what would have been new_listings115.py's permanent content,
renumbered post-hoc to preserve the incident's audit trail -- the ids below
are NOT live in rebuild_final.py."""
from listing_lock import insert_listings

IDS = [1000369, 1000370, 1000371, 1000372, 1000373, 1000374, 1000375, 1000376]

NEW_SRC = '''
L(1000369,"ho-chi-minh","tm","Квартира",32000000,132,
  "4-спальная квартира (3 с/у) 132м² в ЖК Sunshine Sky City, ул. Phú Thuận, Tân Mỹ, Q7 — полная меблировка, готова к заселению.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134486126.htm","сегодня",0,source="chotot",
  descEn="4-bedroom apartment (3 bathrooms) 132m² in the Sunshine Sky City complex, Phú Thuận St, Tân Mỹ, Q7 — fully furnished, move-in ready.",
  details={"photos":["https://cdn.chotot.com/skIgA3nP75es7p537MVjJE2GOO4EQ_ZzaUWWXp_ZRwM/preset:view/plain/0d49a455a0a477b6c01f347d5f75e49e-3000463314644656007.jpg", "https://cdn.chotot.com/si6zIkUJqqhOMBLbWscXAqT89VVFNa5ZQQDbJnn2ueM/preset:view/plain/b9855abe7f5c565728796f5d5ed0235c-3000463314423004554.jpg", "https://cdn.chotot.com/btjmV8qjkasH1fLOLOxF3yfS6s0akgfrw9ZgyIZoDms/preset:view/plain/37c2e5c8c5f3462fef5e2dcb4a701f5c-3000463314341799151.jpg", "https://cdn.chotot.com/Ecd55P58T6_SzYYTPBaZCRMfiqAL7bvI2gdYSpYcBAA/preset:view/plain/2f1b459343914811482c4c87692da2ed-3000463314315640677.jpg", "https://cdn.chotot.com/3kQEnq61izTCO3foHHBzbplPEi7Po2X7U8XWffttr-s/preset:view/plain/02644e671971f220d3c006c86029ce67-3000463314544765320.jpg", "https://cdn.chotot.com/QpdK8CvDI0VwisSKx30tGC0wibqIAKUiFrZfYtVBW3Y/preset:view/plain/d7fcfeaa2d9c9bf0bbae22b41f209afb-3000463314642548543.jpg"],"contact":"Nhung","notice":"тот же дом/район уже представлен на площадке ЖК Sunshine Sky City 132м² 4-спальной квартирой за 35 млн (ID 1273, объявление 11-дневной давности) — оставлено отдельной карточкой, т.к. цена и продавец отличаются, а адрес комплекса не даёт точной идентификации юнита","noticeEn":"the same Sunshine Sky City complex already has a 132m² 4-bedroom listing at 35 million (ID 1273, an 11-day-old ad) — kept as a separate card since the price and seller differ and the complex-level address does not pin down the exact unit"}),
L(1000370,"ho-chi-minh","tm","Комната",1700000,10,
  "Комната от 10м² в ЖК Era Town (Đức Khải), ул. 15B Nguyễn Lương Bằng, Tân Mỹ, Q7 — от 1,7 до 2,5 млн/мес (малые) и 3-4 млн/мес (большие), холодильник, стиральная машина, электроплита, общая кухня, еженедельная уборка, wifi, охрана 24/7, свободный график.",
  "https://www.nhatot.com/thue-phong-tro-quan-7-tp-ho-chi-minh/133021187.htm","вчера",1,source="chotot",
  descEn="Room from 10m² in the Era Town (Đức Khải) complex, 15B Nguyễn Lương Bằng St, Tân Mỹ, Q7 — 1.7 to 2.5 million/month (small rooms) and 3-4 million/month (large rooms), fridge, washing machine, electric stove, shared kitchen, weekly cleaning, wifi, 24/7 security, flexible hours.",
  details={"photos":["https://cdn.chotot.com/QpfbGv6mFW8-vDLUPtkGFSZYmopxNHSqdvIACW1rwHU/preset:view/plain/e1d5e3e985563630914a825a957611e0-2989129852415044857.jpg", "https://cdn.chotot.com/5liGWPFi03l4Iz1OCEWaVqPjg0oNaT5wBWW6OqQ3SP0/preset:view/plain/d6e63f2cee3653faf33b2f19524af1df-2989129852473251597.jpg", "https://cdn.chotot.com/qB8M1alatRw6kK3oEqVku5hwCfvAxJ6EP-z8rRo0pOU/preset:view/plain/ec80fa92b2fb4ddfb96dd175c75be998-2989129852540971495.jpg"],"contact":"Ms Tiên","notice":"указана минимальная цена диапазона; у того же агента в этом доме есть комнаты крупнее до 4 млн/мес","noticeEn":"the price shown is the bottom of the range; the same agent has larger rooms in this building up to 4 million/month"}),
L(1000371,"ho-chi-minh","th","Дом",16000000,77,
  "Дом целиком, 1 этаж + 1 этаж, 4 спальни/4 с/у, 7×11м, переулок для авто 30 Lâm Văn Bền, Tân Hưng, Q7 — электричество/вода по гос. тарифу, горячая вода, рядом рынок и школа Nguyễn Hữu Thọ.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134482039.htm","вчера",1,source="chotot",
  descEn="Whole house, ground floor + 1 upper floor, 4 bedrooms/4 bathrooms, 7×11m, car-accessible alley off Lâm Văn Bền St 30, Tân Hưng, Q7 — state-rate electricity/water, hot water, near a market and Nguyễn Hữu Thọ school.",
  details={"photos":["https://cdn.chotot.com/sOWpnDYiHkIAXDmz3nNGfjgM18VxADX7jzBaj5GaqKc/preset:view/plain/f3a9512c0bf97c7762da6e8a567f7cf0-3000442893734166368.jpg", "https://cdn.chotot.com/VDOHMsqGmR971Dqrd386ixkwqKMyXWtGymWb46yO98s/preset:view/plain/0a601eb61ef3a431876f53c2d1e278f0-3000442893421379429.jpg", "https://cdn.chotot.com/_wUP2rGqtvSM_o6v-m2h1vqAZ0roeg3kNlX06jo90NQ/preset:view/plain/99f826205c621ea812f52cc33de0bc44-3000442893203825568.jpg", "https://cdn.chotot.com/92B6Yz07GAOsLCbgey6HdQ_7NHg1KJlPRSdr6Dj4E8U/preset:view/plain/758a23edc836d614109090385597c895-3000442893099818887.jpg", "https://cdn.chotot.com/ymVn75vtBtJtiegyZKNtGqJBLNJqnXdcJbxmUBqExvY/preset:view/plain/f604398db35da23e49abcd0974d0825c-3000442893602194370.jpg", "https://cdn.chotot.com/qfcBGu_KzcgtEpU66cS1dTQcGkHgi8CpuZoNoqqeD-0/preset:view/plain/e0dcd7399c9741570dd14b68f7ea56e6-3000442893125334816.jpg"],"contact":"Ngọc"}),
L(1000372,"ho-chi-minh","th","Дом",53000000,150,
  "Дом целиком 7,5×20м (150м²), подвал + 1 этаж + 2 этажа + терраса, ЖК Him Lam Kênh Tẻ, Tân Hưng, Q7 — напротив парка, полная меблировка, цена договорная.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/132628482.htm","вчера",1,source="chotot",
  descEn="Whole house 7.5×20m (150m²), basement + ground floor + 2 upper floors + roof terrace, Him Lam Kênh Tẻ complex, Tân Hưng, Q7 — opposite a park, fully furnished, price negotiable.",
  details={"photos":["https://cdn.chotot.com/zaJEMvu9jKCMSxIeay99AUI6FQSrzZw1P1Iz1TaQg4k/preset:view/plain/8f5cbc4b8f1d96b114944380bd6bc6b3-2986103980398064006.jpg", "https://cdn.chotot.com/FLQjqAMw20FktX1be70hEJRgZlA4nztJAAXi80U4JsI/preset:view/plain/a53f344226ceaae7b4509320a988ca93-2986103980884601718.jpg", "https://cdn.chotot.com/mDkg2-S1vyYo14YJSdbfxUSJs29AVasQxEnbpobNo3o/preset:view/plain/48d874af27b71cc649b58f7b32909cc0-2986103980429844043.jpg", "https://cdn.chotot.com/I1A2BbA4yrpoq07ExbbjqhcYMzewHstjvZmkQ-JJEeM/preset:view/plain/e1a411ad7f9ac7ba472d9d0d5e54ab37-2986103980834236027.jpg", "https://cdn.chotot.com/8Ux2_O_UslqYWcTL0QCcmmtQUBqSj8T5B94ve4rsZeo/preset:view/plain/0385a65e52362ce0db87fba8edbf8dd7-2986103980462516644.jpg", "https://cdn.chotot.com/iRWmBFMcSY2Hc9SzLribbEgoc577yaU96bdxmwks0Sk/preset:view/plain/ae2af95f1effbef5d1f55416d03fe488-2986103980465573168.jpg"],"contact":"Hạnh"}),
L(1000373,"ho-chi-minh","btr","Квартира",6000000,40,
  "1-спальная квартира 40м² с 2 балконами на ул. в Bình Trưng, Thủ Đức — полная меблировка, своя стиральная машина, вход по отпечатку пальца, рядом рынок и Bách Hóa Xanh, большая вело/мотопарковка, лифт.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/131030160.htm","сегодня",0,source="chotot",
  descEn="1-bedroom apartment 40m² with 2 balconies in Bình Trưng, Thủ Đức — fully furnished, own washing machine, fingerprint entry, near a market and Bách Hóa Xanh, large bike/moto parking, elevator.",
  details={"photos":["https://cdn.chotot.com/TEDpFwhllnPEvUd_3OIS1qilCwYibFEyDTKeks5ASaU/preset:view/plain/d7c3a8986e44ce063bc546ffca81c1a5-2974219988194913457.jpg", "https://cdn.chotot.com/OwHe7rWngLDEKo6ZximY0nnNG10bXE4Wi8m89fAfTy4/preset:view/plain/59d5a05f8684a8992991aaab5447d167-2974219988520010910.jpg", "https://cdn.chotot.com/-lwpwsOAA0xFqdSFznY2nWpPQusss49B1Q7BrkKjJ74/preset:view/plain/319af66bf2cc4743097032e9a6fd5e5f-2974219988521288564.jpg", "https://cdn.chotot.com/iWKIPYUT7NbwcT2zC9JTIOSRhs4LGMyUjst3rb7LKOE/preset:view/plain/966b45c6affdfe204d37c2360f077357-2974219988788994353.jpg", "https://cdn.chotot.com/0_88mEtOoHH1Sb60Gx_JvSSVRxXUIpMo-Q7tgETB8Bc/preset:view/plain/db38a3ce74d62f1c5ca3ec55fdc9e4c9-2974219988833051142.jpg", "https://cdn.chotot.com/z7kvNZd1n7DGxQoAq4eytgpaTfNsW2tCLrsRm1b9kAU/preset:view/plain/d2864a8755a91db1532e33b72c47e5cd-2974219988466995100.jpg"]}),
L(1000374,"ho-chi-minh","btr","Квартира",6000000,80,
  "Целый этаж (2 спальни/1 с/у) 80м² на мансардном 2-м этаже, мебельная точка мебели и кондиционер, фасад ул. Nguyễn Duy Trinh, Bình Trưng, Thủ Đức — балкон, приоритет студенткам/сотрудницам, до 4 человек, цена договорная.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133434101.htm","сегодня",0,source="chotot",
  descEn="A whole 2nd floor (2 bedrooms/1 bathroom) 80m², wardrobe and air conditioner included, on the Nguyễn Duy Trinh St frontage, Bình Trưng, Thủ Đức — balcony, female students/office workers preferred, up to 4 people, price negotiable.",
  details={"photos":["https://cdn.chotot.com/In8Em23Hti1eZ4KyK5futTTZmEjQG9Ilttd5g7hNcUc/preset:view/plain/6f8866a1ff9493c6b85ad0682fb4b36f-2992228781214767682.jpg", "https://cdn.chotot.com/nX6dvRYY0h8-L-qEMnwqm6WkZ6eQpm3_J_iacGJWGHA/preset:view/plain/9d3720e237db084556275c5b6f668aec-2992228781275368966.jpg", "https://cdn.chotot.com/3kbw1BA7a8QX2aNZqOpbrAM1uDxIN4V1LqS5el-yyOI/preset:view/plain/0b03cde2bae50c04136e8c3ec7949359-2992228782659288277.jpg", "https://cdn.chotot.com/qm9PlrF-JuSm7ubz4qi5SJKC3ncapwoKWhklNDhWfBo/preset:view/plain/d422e5f07c622374b4cd3cd8e8b16b66-2992228781704350414.jpg", "https://cdn.chotot.com/XwOmSiU3bVNBsFypme30L2sTxX2q4SGjs127oh4h5Rc/preset:view/plain/f9d8ad1ead31777140c3ad84cc44210f-2992228782786597168.jpg", "https://cdn.chotot.com/67YXwwA_YxVcuzYEgyBdz-7EeZA7OmU1A7uiQREQyPA/preset:view/plain/beced51e79a0dd4def1e06479c17b4dc-2992228781580903300.jpg"]}),
L(1000375,"ho-chi-minh","btr","Комната",4000000,30,
  "Мансардная комната (гак) 30м² в Bình Trưng, Thủ Đức — своя кухня, холодильник, новый кондиционер, зона для учёбы/работы, новая деревянная мебель, тихий охраняемый район, подходит для работающих, студентов, пар.",
  "https://www.nhatot.com/thue-phong-tro-thanh-pho-thu-duc-tp-ho-chi-minh/126511649.htm","вчера",1,source="chotot",
  descEn="Loft-style room (gác) 30m² in Bình Trưng, Thủ Đức — own kitchen, fridge, new air conditioner, study/work nook, new wooden furniture, quiet guarded area, suitable for working people, students, couples.",
  details={"photos":["https://cdn.chotot.com/PpQSPSdxcSH3qOzBtYCIHDfYNkkGAzgxg6FG3O5NCds/preset:view/plain/d5b08f95de565a1053a3dc46f29cdf41-2941198302492372351.jpg", "https://cdn.chotot.com/Jvvh0RrtX5nIxpmtALkItWquB3MG9kNWvv2LvKiBHNo/preset:view/plain/ca5e0923e4c44a737064cc8004d6cd84-2941198302509611184.jpg", "https://cdn.chotot.com/BiGG2UmK2w2eI2AS_2pbhngq2dcsqz66o2_Y4YJTvv0/preset:view/plain/06dd93bdcea8abdabf8630d669f80fcd-2941198302748419300.jpg", "https://cdn.chotot.com/bdEzKWzEIm2ZlzjrM-yz-ZegL_4sIAUhvf-q2wpvY5c/preset:view/plain/d8091a9d4e0b670c7e8e2e20c41779b2-2941198302614582190.jpg", "https://cdn.chotot.com/msC-RID3sfDupUzgF1E55aoSBiPtIQ01xBHcLIz8y1I/preset:view/plain/f3ed32cc89374a18211a1c78a29b7cae-2941198303129347888.jpg", "https://cdn.chotot.com/bKrXPI5X4Xw5Bqvy49rKiS6B08jMR--rO1d8KDmwL6E/preset:view/plain/709b78093db2de195bf0967663df1950-2941198302680672445.jpg"]}),
L(1000376,"ho-chi-minh","bth","Торговая площадь",500000000,42,
  "Отдельное здание 8,5×25м (подвал + 6 этажей + терраса), фасад пер. 165 Nguyễn Thái Bình, Bến Thành, Q1 — сейчас 34 меблированные караоке-комнаты, есть лифт, лестница, пожарная система, подвал на 4-5 машин; подходит и под гостиницу. Аренда 20 000 $/мес без НДС, долгосрочно (5-10 лет).",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/119838174.htm","сегодня",0,source="chotot",
  descEn="Standalone building 8.5×25m (basement + 6 floors + roof terrace), frontage on alley 165 Nguyễn Thái Bình, Bến Thành, Q1 — currently 34 furnished karaoke rooms, has an elevator, stairs, fire-safety system, basement parking for 4-5 cars; also suitable as a hotel. Rent $20,000/month excl. VAT, long-term lease (5-10 years).",
  details={"photos":["https://cdn.chotot.com/ynDbMTc-MKaZdA8pPM9veqR31qd_XG7HVgBArfkG5kc/preset:view/plain/78ceec0f042081dab138c0816fc24ac9-2898701978154253729.jpg", "https://cdn.chotot.com/MREX27ouW4kcQFfHmVq6exaTGohLVqCV3L1EAGfICHA/preset:view/plain/9e180fafde3af8190408707c1449940f-2898701978125548479.jpg", "https://cdn.chotot.com/tHYyDAn-LbOMDf3fwNCCnkMtHC4vf1-kJ-a6tAmc9yA/preset:view/plain/d87912df905f186dbb059e6cdfb1a962-2898701978059670697.jpg", "https://cdn.chotot.com/jMwWPrclFtjVAD2K7ThdL87xHcVNxFtbUaAz6wWfRVA/preset:view/plain/009aec8bd96d488526af5d187185a7e7-2898701979267695785.jpg"],"notice":"цена указана в долларах в объявлении (20 000 $/мес); в карточке приведена в донгах по курсу ~25 000 (500 млн ₫) для сопоставимости с остальными объявлениями площадки","noticeEn":"the ad states the price in US dollars ($20,000/month); the card converts it to VND at ~25,000/USD (500 million VND) for comparability with the rest of the site's listings"}),
'''

if __name__ == "__main__":
    raise SystemExit(
        "SUPERSEDED: this batch was inserted (1000369-1000376), found to duplicate ids "
        "1000377-1000385 already live from a concurrent session's new_listings114.py, and "
        "removed again via listing_lock.remove_listings(). Nothing to run -- see the module "
        "docstring for the full story."
    )
