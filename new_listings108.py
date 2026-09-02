# -*- coding: utf-8 -*-
from listing_lock import insert_listings

IDS = [1000308, 1000309, 1000310, 1000311, 1000312, 1000313, 1000314, 1000315]

NEW_SRC = '''
L(1000308,"ho-chi-minh","ak","Комната",3800000,25,
  "Комната 25 м², Đường Số 38, An Khánh (район Trần Não) — рядом река. Свободный график, для студентов скидка на депозит. Оплата: вода 20 000 đ/м³, свет 3500 đ/кВт·ч, интернет + вывоз мусора 55 000 đ/мес.",
  "https://www.nhatot.com/thue-phong-tro-thanh-pho-thu-duc-tp-ho-chi-minh/134473943.htm","сегодня",0,source="chotot",
  descEn="Room, 25m², Đường Số 38, An Khánh (Trần Não area) — by the river. Flexible hours, deposit discount for students. Utilities: water 20,000 đ/m³, electricity 3,500 đ/kWh, wifi+trash 55,000 đ/month.",
  details={'photos': ["https://cdn.chotot.com/5b2JATrEWrO3LC3iQ6dQ-iwVYuDkH_XURj3mYGmsVGs/preset:view/plain/750e580a39a7995391d1ec435c2d0c5a-3000317428587361842.jpg", "https://cdn.chotot.com/7W20m9cfqtM_BSkDs5mXpxgl7rQryxFxYZ26kEpFJWM/preset:view/plain/5e2d011931bdadbf030bcd66c7547139-3000317429900915616.jpg", "https://cdn.chotot.com/qYeYxvRJA2suBbwxsb8dAQBq2cai8X1jAInC059tEmM/preset:view/plain/0de065d3cba6d7e00f34e02fde3cdcc0-3000317611376791977.jpg"]}),
L(1000309,"ho-chi-minh","tm","Квартира",8500000,68,
  "2-спальная квартира (2 с/у), 68 м², ЖК Era Town/Đức Khải, ул. 15B Nguyễn Lương Bằng, Tân Mỹ — рядом Phú Mỹ Hưng, 5–7 мин до ĐH Tôn Đức Thắng, RMIT, UFM, Crescent Mall. Большие окна, набережная больше 1 км, мини-маркет и рынок у дома, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134465319.htm","сегодня",0,source="chotot",
  descEn="2-bedroom apartment (2 bathrooms), 68m², Era Town/Đức Khải complex, 15B Nguyễn Lương Bằng St, Tân Mỹ — next to Phú Mỹ Hưng, 5-7 min to Tôn Đức Thắng University, RMIT, UFM, Crescent Mall. Large windows, 1km+ riverside park, mini-mart and market at the building, 24/7 security.",
  details={'photos': ["https://cdn.chotot.com/naO5i-RMyilRP5Pll-kIJ-7sHlIcY1PdwW8OzBk5SGs/preset:view/plain/87ba93d079f942ef569dad78441d6491-3000214884328902348.jpg", "https://cdn.chotot.com/2_68yLjfoVabX43VOqOUQH_wZ651-Yb-gPp-Ly8vnnk/preset:view/plain/d7ab9d6cc8ae958548cf9003ff7f7568-3000214884029641632.jpg", "https://cdn.chotot.com/1YwYIRtyvI0c28JO-yv_ylqL9cPa45hqLXKizG74cRg/preset:view/plain/462d752e48edf0b1fd97880e5ffffa27-3000214884095885358.jpg"]}),
L(1000310,"ho-chi-minh","btr","Студия",6000000,40,
  "Студия 40 м² в новом доме, полностью меблирована, ул. Song Hành, Bình Trưng — рядом Lakeview City, The Global City. Свободный график, вход по отпечатку пальца, охрана 24/7, есть прачечная и уборка на этаже.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/128980494.htm","сегодня",0,source="chotot",
  descEn="Studio, 40m², newly finished, fully furnished, Song Hành St, Bình Trưng — near Lakeview City, The Global City. Flexible hours, fingerprint entry, 24/7 security, on-floor laundry and cleaning service.",
  details={'photos': ["https://cdn.chotot.com/Y1EKW9aPg2_sRIIpaRFc48Rg84JlL9_Ub1cXG2b8zBs/preset:view/plain/a16ff0e38035b9e62f14177bc0e2073e-2967166758412862760.jpg", "https://cdn.chotot.com/OAQjG17vgZ7G3uA0P6pxogjgemWcScj8unWgBq6cQJc/preset:view/plain/304bf71b333e25874cd8221f396c5021-2967166758586573721.jpg", "https://cdn.chotot.com/E0IXpj51W3ylBXnTQ1aTxo65-y5szj9tiv-YIBIuNI0/preset:view/plain/f3b7dc9db5614f38ff4367b2f12152ac-2967166758644831391.jpg"]}),
L(1000311,"ho-chi-minh","btr","Студия",5500000,16,
  "Студия 16 м² по студенческой цене, 7 Đường Số 41, Bình Trưng (бывшая Bình Trưng Tây, старый Q2) — полностью меблирована, можно заезжать сразу. Стиральная машина, кондиционер, холодильник, Wi-Fi, есть парковка для мотоцикла/авто.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134459470.htm","вчера",1,source="chotot",
  descEn="Studio, 16m², student pricing, 7 Đường Số 41, Bình Trưng (former Bình Trưng Tây, old District 2) — fully furnished, move-in ready. Washing machine, AC, fridge, wifi, motorbike/car parking available.",
  details={'photos': ["https://cdn.chotot.com/vyLNfOd6THyAc_TCYLOmc5HLwm6NxFlTdnXfT-dwmyM/preset:view/plain/67150e84310a7488b20a921e8f61d968-3000167504202863495.jpg", "https://cdn.chotot.com/8VG4zD7ZjU--fJJPLar56W4QYmV3VRuPqRSrCi_TE24/preset:view/plain/46d68125cfabd893b9ad10d7cfcd28d3-3000167503932240800.jpg", "https://cdn.chotot.com/TaTQinX0tdorRXkTzx8lTv51PhJGcSQh1vvJhfcYZ1M/preset:view/plain/7be249717de7f9457fe2d2a14580b24c-3000167570001703840.jpg"]}),
L(1000312,"ho-chi-minh","th","Студия",6100000,35,
  "Студия с балконом, 35 м², новый дом, ул. Nguyễn Thị Thập, Tân Quy (Tân Hưng) — рядом Lotte Mart Q7, удобно до Q1 и Q4. Полная меблировка, светлая и просторная.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/132360399.htm","вчера",1,source="chotot",
  descEn="Studio with balcony, 35m², newly built, Nguyễn Thị Thập St, Tân Quy (Tân Hưng) — near Lotte Mart Q7, convenient to Q1 and Q4. Fully furnished, bright and spacious.",
  details={'photos': ["https://cdn.chotot.com/4F1ZIDFcGCYdUPl7eC5W_BmRNiwWxLflAXlE5VxRCmE/preset:view/plain/9004c8e032dad9dc81f7e70c9aece89f-2984084166014587999.jpg", "https://cdn.chotot.com/fbE7sTseksn4l0BlZH0DU14dAml2Ek0ENmCtKH7-lV0/preset:view/plain/236193cda31e99f82f8b1fc16b4f200e-2984084166926308880.jpg", "https://cdn.chotot.com/PPYJVBkedhEqxVtQ6QG7DKX5QxcAyZ51njPmaBYM28A/preset:view/plain/f5fd2e7de8c1f2559c32852cf88053a0-2984084165909386715.jpg"]}),
L(1000313,"ho-chi-minh","th","Студия",9300000,35,
  "Студия с 1 спальней, 35 м², ул. Đường Số 14, Tân Hưng — в центре Q7, рядом Lotte Mart, ĐH RMIT, ĐH Tôn Đức Thắng. Полная меблировка как на фото, отдельная стиральная машина.",
  "https://www.nhatot.com/thue-phong-tro-quan-7-tp-ho-chi-minh/134458202.htm","вчера",1,source="chotot",
  descEn="1-bedroom studio, 35m², Đường Số 14, Tân Hưng — central Q7, near Lotte Mart, RMIT University, Tôn Đức Thắng University. Fully furnished as pictured, own washing machine.",
  details={'photos': ["https://cdn.chotot.com/rv0taB0_iXlLKiKwzT6G28J5LLKGN48yD50j9fpt6pI/preset:view/plain/8c09e813fe62ee0fb00a799ad3eb0f90-3000160089868075054.jpg", "https://cdn.chotot.com/-M08BxUpuNMKP2NeN9iv3aHunoDENXv6BXFRFpRVU2w/preset:view/plain/6d33a0d4787c3b70886d4224897474fc-3000160089701626784.jpg", "https://cdn.chotot.com/esz5gJVdTu4oCK1F8FUugqaYMLu7ikZk46Oe-PCWBN4/preset:view/plain/6a956d7f99e192c35b5a86179b3887e4-3000160091126431790.jpg"]}),
L(1000314,"ho-chi-minh","btr","Студия",5000000,25,
  "Студия с балконом, 25 м², ул. Đường Số 41, Bình Trưng (бывшая Bình Trưng Tây) — полностью меблирована, рядом супермаркет, рынок, больница. Охрана 24/7, регулярное бесплатное обслуживание.",
  "https://www.nhatot.com/thue-phong-tro-thanh-pho-thu-duc-tp-ho-chi-minh/130847529.htm","вчера",1,source="chotot",
  descEn="Studio with balcony, 25m², Đường Số 41, Bình Trưng (former Bình Trưng Tây) — fully furnished, near supermarket, market, hospital. 24/7 security, free regular maintenance.",
  details={'photos': ["https://cdn.chotot.com/NKy_RXhrmbKXA4zh07vVOOAU8wsMP58I1dm_ALEx0d4/preset:view/plain/14c73399d25254906bc0749f75635b95-2972783852965404290.jpg", "https://cdn.chotot.com/65fCUEaZrDDnANxRKg3YmKgC5Ygk28X66Zi2T-JIwnQ/preset:view/plain/bdad530e0a5e283a1bcdd812b7325447-2972783855914274281.jpg", "https://cdn.chotot.com/kaUb8R8nk3ErMBFVnloJjOOjZ9PgmiXqbHoRfnWPtWc/preset:view/plain/7b220b610087b6106a299d4eaa80e804-2972783856371310210.jpg"]}),
L(1000315,"ho-chi-minh","btr","Торговая площадь",30000000,160,
  "Шопхаус на два фасада в ЖК Lakeview City, участок 8×20 м (160 м²), 1 этаж + 4 верхних (330 м² площади пола суммарно) — угловой, хорошая видимость. Базовая отделка, лифт, кондиционеры. На верхнем этаже 2 спальни, кабинет и кухня — можно совмещать проживание с бизнесом (шоурум, офис). Ул. Song Hành, Bình Trưng.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-thanh-pho-thu-duc-tp-ho-chi-minh/134435380.htm","2 дня назад",2,source="chotot",
  descEn="Two-frontage shophouse in Lakeview City, 8x20m lot (160m²), ground floor + 4 upper floors (330m² total floor area) — corner unit, good visibility. Basic fit-out, elevator, AC. Top floor has 2 bedrooms, a study, and kitchen — suitable for living plus business (showroom, office). Song Hành St, Bình Trưng.",
  details={'photos': ["https://cdn.chotot.com/0n_HUYkB6q7okjeIws5QDyWzeybik7iviuvXvEMCXWw/preset:view/plain/43b8c7edb6c87624ef0009bcf85b1057-2999918249337226368.jpg", "https://cdn.chotot.com/w8Ndw6u0mAs9GF9xdiQqO9yBTcefeFgqckhAXhofDyE/preset:view/plain/c9106079be5e58a7c266fdf981a7bd54-2999918246921241728.jpg", "https://cdn.chotot.com/MatYnKZbPjAPElxCDCcO_oibkTpTccdVC1UQi2pZnYk/preset:view/plain/f13d51f14d379922faf56189666e46f6-2999918247098957756.jpg"]}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
