# -*- coding: utf-8 -*-
NEW_LISTINGS_SRC = r'''
L(82,"nha-trang","vh","Комната",2500000,22,
  "Комната у моря, охраняемый район с соблюдением норм пожарной безопасности.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-pho-phan-phu-tien-phuong-vinh-hai-350/cho-gia-2-5-tr-gan-bien-an-ninh-am-bao-pccc-pr46180393","сегодня",0,source="batdongsan"),

L(83,"nha-trang","vh","Комната",3000000,45,
  "Комната на ул. Nguyễn Khuyến, приоритет студентам.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-khuyen-phuong-vinh-hai-350/cho-3tr-thang-uu-tien-sinh-vien-pr46162044","4 дня назад",4,source="batdongsan"),

L(84,"nha-trang","ph","Дом",18000000,60,
  "Дом целиком, 4 этажа, 5 спален, 5 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-thich-quang-duc-phuong-phuoc-hai-350/cho-nguyen-can-4-tang-5-phong-ngu-5-ve-sinh-pr46136962","сегодня",0,source="batdongsan"),

L(85,"nha-trang","pl","Дом",10000000,142,
  "Дом 142 м² по акционной цене, район Vĩnh Phương (пригород, запад).",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-xa-vinh-phuong/cho-gia-uu-ai-tai-10-trieu-142m2-pr46178812","сегодня",0,source="batdongsan"),

L(86,"da-lat","lv","Комната",1600000,12,
  "Маленькая комната с антресолью, район Phường 9.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-yersin-phuong-9_2-391/cho-tai-9-da-lat-3x4-12m2-gia-1-6-trieu-thang-co-gac-lung-pr41472028","сегодня",0,source="batdongsan"),

L(87,"da-lat","xh","Студия",3800000,22,
  "Меблированная квартира-студия по хорошей цене, район Phường 2.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-van-troi-phuong-2_3-391/cho-can-ho-full-noi-that-gia-re-pr45648318","5 дней назад",5,source="batdongsan",
  details={"amenities":"полная мебель"}),

L(88,"da-lat","lv","Дом",7500000,70,
  "Дом 70 м², район Phường 8.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-huu-canh-phuong-8_2-391/cho-70m2-uong-8-a-lat-lam-ong-pr46181403","сегодня",0,source="batdongsan"),

L(89,"da-lat","cl","Дом",15000000,200,
  "Дом 200 м², 2 этажа, 4 спальни, 3 санузла, рядом рынок/школа/больница.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-kim-dong-phuong-6_3-391/cho-nguyen-can-200m-2-tang-ap-mai-4pn-3wc-gan-cho-truong-hoc-benh-vien-o-ngay-pr46140934","1 неделю назад",7,source="batdongsan"),

L(90,"da-nang","ns","Комната",2900000,18,
  "Комната, район Ngũ Hành Sơn (Khuê Mỹ).",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-ho-xuan-huong-phuong-khue-my-48/cho-tai-ngu-hanh-son-a-nang-gia-2-9tr-pr46168870","2 дня назад",2,source="batdongsan"),

L(91,"da-nang","hc","Комната",4200000,50,
  "Меблированная комната 50 м², район Hải Châu.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-thanh-thuy-phuong-hai-chau_1-46/cho-gia-re-uong-chau-dt-50m2-noi-that-ay-u-pr46165383","3 дня назад",3,source="batdongsan",
  details={"amenities":"полная мебель"}),

L(92,"da-nang","tk","Дом",14000000,90,
  "Дом с 3 спальнями, меблирован, район Thanh Khê (Xuân Hà).",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-do-phuong-xuan-ha-50/cho-kiet-uong-o-3-phong-ngu-u-noi-that-pr46175643","сегодня",0,source="batdongsan",
  details={"amenities":"3 спальни, полная мебель"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()

marker = '''L(81,"nha-trang","ps","Квартира",7500000,55,
  "Квартира, район Phương Sơn (запад).",
  N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133609077.htm","1 неделю назад",7),
]'''
assert marker in content, "listings marker not found!"
new_content = content.replace(marker, marker[:-1] + "\n" + NEW_LISTINGS_SRC.strip() + "\n]", 1)

old_src = '{"key":"batdongsan","label":"Batdongsan.com.vn","short":"Batdongsan","active":False,"color":"#E0862B"},'
new_src = '{"key":"batdongsan","label":"Batdongsan.com.vn","short":"Batdongsan","active":True,"color":"#E0862B"},'
assert old_src in new_content, "sources marker not found!"
new_content = new_content.replace(old_src, new_src, 1)

open(path, "w", encoding="utf-8").write(new_content)
print("inserted, new length", len(new_content))
