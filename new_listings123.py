# -*- coding: utf-8 -*-
"""Daily HCMC check, 4 Sep 2026 -- Phú Mỹ Hưng / Thảo Điền-An Phú / Thanh Đa /
Bến Thành / Khánh Hội sweep. 19 candidates within 3 days across all 7 wards;
12 already added by an earlier run today. 7 genuinely new listings across
btr, th, bth, bq -- nothing new today in tm, ak, kh."""
from listing_lock import insert_listings

IDS = [1000405, 1000406, 1000407, 1000408, 1000409, 1000410, 1000411]

NEW_SRC = '''
L(1000405,"ho-chi-minh","btr","Квартира",15000000,68,
  "2-спальная квартира, 68 м², 2 санузла, ЖК Precia, ул. Nguyễn Thị Định, Bình Trưng (быв. Q2), рядом с развязкой An Phú. У хозяина есть ещё несколько свободных квартир в этом доме.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134500009.htm","сегодня",0,source="chotot",
  descEn="2-bedroom apartment, 68m², 2 bathrooms, Precia complex, Nguyen Thi Dinh St, Binh Trung (former Q2), near the An Phu interchange. Owner has several more units available in the same building.",
  details={"photos": ["https://cdn.chotot.com/tEwPFPJS4zMCakFKXDgvbOuDg2NPJlj6GEXuLnzwUlU/preset:view/plain/1d1c2f7ce4582cf5aa01c686d8e4e44c-3000582004748789723.jpg", "https://cdn.chotot.com/yue5O5dfbtTpu0TGgJ0zaNT3afj3rU9AHMrIjLk-rKk/preset:view/plain/9da850894392d701d189ad5428eb2297-3000582003976875049.jpg", "https://cdn.chotot.com/5RKC87C1yhv9mSbIdposaQ5xrbWUhPn4PAMGFLSFYgg/preset:view/plain/4682ce93308e35c8fb2392e58584babc-3000582003979744726.jpg", "https://cdn.chotot.com/t84ydA1xY-V0BAI-F906-wPQiJhgnLRqQXYq705FuoI/preset:view/plain/c6e80f1e84a65c161dcd680433bf8ae7-3000582004251809157.jpg", "https://cdn.chotot.com/MvpB0ryyQo8miFLH1F_o5tK3X1GMNjrOZNKIIMnLWgI/preset:view/plain/fda3c53f0e749646d3882d2a2333b7d9-3000582004690061093.jpg", "https://cdn.chotot.com/RomnydX-I2q4MldV0gjt5cJrYwVs513kMpPc-r7vKHw/preset:view/plain/815153dbe072b948b34b000d87e6df0b-3000582005017424151.jpg"]}),
L(1000406,"ho-chi-minh","th","Комната",6800000,35,
  "Комната 35 м² в Phú Mỹ Hưng (Tân Hưng, Q7), сдаёт хозяин напрямую. Отдельный санузел, кондиционер, wifi, парковка, общая кухня и прачечная. Тихий безопасный район рядом с рынком и супермаркетом. Цена договорная.",
  "https://www.nhatot.com/thue-phong-tro-quan-7-tp-ho-chi-minh/133763996.htm","сегодня",0,source="chotot",
  descEn="Room, 35m², Phu My Hung (Tan Hung, Q7), rented directly from the owner. Private bathroom, AC, wifi, parking, shared kitchen and laundry area. Quiet, secure area near a market and supermarket. Price negotiable.",
  details={"photos": ["https://cdn.chotot.com/TsgHKOqbWAKkeyHWZBsPzkYFFKrDGQnq6kyHTzRu4Hg/preset:view/plain/5318238d7846060626cadfb54d7ef79e-2997124153976740989.jpg", "https://cdn.chotot.com/_ngL1xiQNqJ__lmvY1ZuZxJawFxZhC53VAJzyL17tn4/preset:view/plain/f6d8ef1c1dd81ef097aaca3fc73b6240-2997124153992247368.jpg", "https://cdn.chotot.com/tkNNzH0pJh8hSGzNsQtsS3R97m43s11TYvJcig_a-IQ/preset:view/plain/068fc34567e0d3337255c8602b5aa5d8-2997124163388890237.jpg", "https://cdn.chotot.com/H30Ya8eoc82SZQlUfBD1QmtsQOiQKbxpaNTKbvjBafs/preset:view/plain/e975f2ddf8f42ee8219c81fa1c6d3613-2997124163299045986.jpg", "https://cdn.chotot.com/fEZSr70JvO7HuKUwnccXUc-GaCR2UwSrBCGj4_MK8JU/preset:view/plain/4526f7587049cbcb0dc5b372258173bf-2997124163370776648.jpg"]}),
L(1000407,"ho-chi-minh","bth","Торговая площадь",100000000,110,
  "Угловое помещение с фасадом на 2 улицы, 5×22 м (1 этаж + 4 этажа), ул. Bùi Thị Xuân, Bến Thành, Q1. Подходит под офис, шоу-рум, спа, клинику, учебный центр или розничный бренд.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-quan-1-tp-ho-chi-minh/134487292.htm","вчера",1,source="chotot",
  descEn="Corner premises with frontage on 2 streets, 5x22m (ground floor + 4 upper floors), Bui Thi Xuan St, Ben Thanh, Q1. Suits an office, showroom, spa, clinic, training center, or retail brand.",
  details={"photos": ["https://cdn.chotot.com/EZKySpduy1pP2ssDQPapoU7i_dELUPjxo07som_MUhQ/preset:view/plain/d0205d8a90908b0d17f94948c481c02f-3000469496742346798.jpg", "https://cdn.chotot.com/sDYt2wAJTRiYAk8rc065DGAP_K1pdGpbFVQdRlgzdPs/preset:view/plain/12d4c926e315145cb45c13a7071825fa-3000469496483752328.jpg", "https://cdn.chotot.com/BU4JwX20GivR1wYzXG3M3sn7WEGc8b2rNFIxSQa3wv0/preset:view/plain/34b70b2fa63e65f37874f926d272ff50-3000469608424623692.jpg", "https://cdn.chotot.com/fuvDsDZu-q2gJ14Rj6AiTLxkj3CkyexhZLhOZQJ9hio/preset:view/plain/5e89d4bfcb03374481834a50c6911330-3000469608456923528.jpg"]}),
L(1000408,"ho-chi-minh","th","Дом",4000000,30,
  "Отдельный домик на 1 этаже, 30 м², 2 спальни, у каждой свой санузел, переулок для машины на ул. Lâm Văn Bền, Tân Hưng, Q7. Свежий ремонт, кондиционер, мебель в наличии. Подходит небольшой семье или студентам (до 4 человек). Депозит 1 месяц, свет 3500 донг/квт·ч, вода 25000 донг/м³.",
  "https://www.nhatot.com/thue-phong-tro-quan-7-tp-ho-chi-minh/134486147.htm","вчера",1,source="chotot",
  descEn="Standalone ground-floor house, 30m², 2 bedrooms each with its own bathroom, car-width alley off Lam Van Ben St, Tan Hung, Q7. Freshly repainted, AC and furniture included. Suits a small family or students (up to 4 people). 1-month deposit, electricity 3500 VND/kWh, water 25000 VND/m3.",
  details={"photos": ["https://cdn.chotot.com/-FU1O1plM8Whx64wrwGC9FzS1HpwqC8-gXafyg7j_eg/preset:view/plain/d04f09131447e7e681db80e68737ec59-3000462450487273864.jpg", "https://cdn.chotot.com/lmV13twAhC0sZCBpaG-cNuXCjXpNBWp4Rc_UwBlo5xE/preset:view/plain/e79786604b604241a8f72acd767fcc7e-3000462450060279648.jpg", "https://cdn.chotot.com/OkAmkODjTVRNHn_-oCWlWhaDNJiLt3aE92VAwXAP3ms/preset:view/plain/4b585c34fe9888696b0dff007df85dbf-3000462503510212654.jpg"]}),
L(1000409,"ho-chi-minh","btr","Торговая площадь",10000000,35,
  "Свободное помещение 35 м², ул. 64 BTĐ, Bình Trưng, Thủ Đức. Подходит под офис, студию танцев или йоги. Депозит 30 млн донгов.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-thanh-pho-thu-duc-tp-ho-chi-minh/134485093.htm","вчера",1,source="chotot",
  descEn="Vacant space, 35m², 64 BTD St, Binh Trung, Thu Duc. Suits an office, dance studio, or yoga studio. Deposit 30 million VND.",
  details={"photos": ["https://cdn.chotot.com/-ABIcUTK9m9MI9EkT-IDzLB9rqohHIjlzrIGsCxLO0s/preset:view/plain/b78c8dfb3fac1199e4718a350d92988b-3000456273946683784.jpg", "https://cdn.chotot.com/u9z2jGVC4UTt0Q8Yv3qfR9IBCU9cMfNiC5igdYNpiHQ/preset:view/plain/b623a1f7304e091d1a4b12ea23bc9789-3000456338200264750.jpg", "https://cdn.chotot.com/NCkoEZNsBFOQkAK8MZmX9Fu1HlP6nS4phgdXnRedF54/preset:view/plain/cf93427e7f5ced89c4a084a8e7626fed-3000456338506393992.jpg"]}),
L(1000410,"ho-chi-minh","bq","Торговая площадь",20000000,144,
  "Отдельный дом, 1 этаж + 1 этаж, фасад на ул. Bình Quới, Bình Quới, Bình Thạnh. Первый этаж 36×4 м, второй этаж 24×4 м, двор перед входом 5×4 м. Пустое помещение, подходит для проживания, офиса или торговли. Депозит 20 млн донгов.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-quan-binh-thanh-tp-ho-chi-minh/134481909.htm","вчера",1,source="chotot",
  descEn="Standalone house, ground floor + 1 upper floor, frontage on Binh Quoi St, Binh Quoi, Binh Thanh. Ground floor 36x4m, upper floor 24x4m, front yard 5x4m. Empty space, suits living, an office, or a business. Deposit 20 million VND.",
  details={"photos": ["https://cdn.chotot.com/2xI9QNbUoidY1BqqZeetShc62btLJvP7-Pn0qa-Ot7s/preset:view/plain/e21d6bc5fc07253f1271f578bd4f1467-3000442155656546594.jpg", "https://cdn.chotot.com/vpC3imCcWn7eAY8IWMY-D_5_ElxZXZr2Aj6_scBc7AY/preset:view/plain/4dcafac24d29ba21d2ad2418c65e1c27-3000442156155994158.jpg", "https://cdn.chotot.com/msZCCc9RmneO939YTdadl9-v9dK0Ryhu5UHozrgCOdY/preset:view/plain/d9d8fe2844a04c7eeed4978b2dc4bec2-3000442154015402376.jpg", "https://cdn.chotot.com/0R9EzzIN6Xmeutkfj9X7A8DUppQ1sQ94TyRHyLQCe30/preset:view/plain/59aaec9437d95975fcc8b4caa8fff7da-3000442154142519142.jpg"]}),
L(1000411,"ho-chi-minh","bth","Торговая площадь",130000000,112,
  "Фасадное помещение на ул. Bùi Viện, Bến Thành, Q1, 7×16 м (расширяется до 8,6 м вглубь), 5 капитальных этажей. В центре туристического квартала. Подходит под ресторан, паб/бар, бутик-отель, спа или шоу-рум. Сдаётся пустым, под ремонт по проекту арендатора.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-quan-1-tp-ho-chi-minh/133003382.htm","вчера",1,source="chotot",
  descEn="Street-front premises on Bui Vien St, Ben Thanh, Q1, 7x16m (widening to 8.6m towards the back), 5 solid floors. Right in the heart of the tourist district. Suits a restaurant, pub/bar, boutique hotel, spa, or showroom. Handed over empty for fit-out to the tenant's own design.",
  details={"photos": ["https://cdn.chotot.com/3KlEUz7e_3dr5Ps8cx5UBbW3woNKwRW8uP_mC7Zc75c/preset:view/plain/02e8da19b30c35ed2aa8c19d1f7f60ff-2988992092550065401.jpg", "https://cdn.chotot.com/45vNHjeD3V92cmDrvkFP3x5XWFUHbUq8kiFrDIBXb6c/preset:view/plain/1ccbde87612176d4e6e1f5bba350baa8-2988992103963308286.jpg", "https://cdn.chotot.com/zmAJK_lqOyimn2SEXzrN-LuZTVXDFe2mzBMYI0i0UeY/preset:view/plain/02fdf7e539025bedda2e672678c0befc-2988992104023457513.jpg", "https://cdn.chotot.com/Zpemk9G9fEtcF30GS2OgzIMA0oZrRnQuS6uRlxRFujs/preset:view/plain/435740f880a19808f469566561919646-2988992104059181864.jpg"]}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
