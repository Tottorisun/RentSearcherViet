# -*- coding: utf-8 -*-
import re

N = "https://www.nhatot.com"

# (city, old_district_text, my_key, kind, price, area_or_None, furniture, url_suffix, posted_text, daysAgo)
ROWS = [
("da-lat","Phường 10","xh","room",2500000,30,"Nội thất đầy đủ","/thue-phong-tro-thanh-pho-da-lat-lam-dong/128500800.htm","1 неделю назад",7),
("da-lat","Phường 8","lv","room",4000000,60,None,"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133928386.htm","2 недели назад",14),
("da-lat","Phường 6","cl","room",1700000,16,"Nội thất đầy đủ","/thue-phong-tro-thanh-pho-da-lat-lam-dong/132629339.htm","2 недели назад",14),
("da-lat","Phường 10","xh","room",1500000,10,None,"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133816047.htm","2 недели назад",14),
("da-lat","Phường 3","xh","room",3000000,30,"Nhà trống","/thue-phong-tro-thanh-pho-da-lat-lam-dong/133947980.htm","1 неделю назад",7),
("da-lat","Phường 6","cl","room",2000000,20,"Nội thất đầy đủ","/thue-phong-tro-thanh-pho-da-lat-lam-dong/133591871.htm","3 недели назад",21),

("da-lat","Phường 8","lv","apartment",8000000,35,"Nội thất cao cấp","/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134097670.htm","8 часов назад",0),
("da-lat","Phường 7","lb","apartment",2500000,25,"Nội thất cao cấp","/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/130268488.htm","8 часов назад",0),
("da-lat","Phường 9","lv","apartment",19000000,100,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133825946.htm","9 часов назад",0),
("da-lat","Phường 8","lv","apartment",6000000,60,"Nội thất đầy đủ","/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134124632.htm","20 часов назад",0),
("da-lat","Phường 8","lv","apartment",11000000,80,"Nội thất đầy đủ","/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134123781.htm","21 час назад",0),
("da-lat","Phường 9","lv","apartment",10000000,60,"Nội thất đầy đủ","/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134115149.htm","вчера",1),
("da-lat","Phường 10","xh","apartment",12000000,70,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134112254.htm","вчера",1),
("da-lat","Phường 2","xh","apartment",4400000,40,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134095713.htm","2 дня назад",2),
("da-lat","Phường 8","lv","apartment",10500000,50,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134089862.htm","2 дня назад",2),
("da-lat","Phường 6","cl","apartment",4300000,35,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134056221.htm","2 дня назад",2),
("da-lat","Phường 8","lv","apartment",11500000,80,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134088790.htm","2 дня назад",2),
("da-lat","Phường 3","xh","apartment",6000000,40,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134084852.htm","3 дня назад",3),
("da-lat","Phường 3","xh","apartment",6000000,40,"Nội thất đầy đủ","/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134083526.htm","3 дня назад",3),
("da-lat","Phường 2","xh","apartment",6000000,60,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133066675.htm","4 дня назад",4),
("da-lat","Phường 1","xh","apartment",8000000,50,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133548219.htm","4 дня назад",4),
("da-lat","Phường 5","cl","apartment",15500000,90,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134031165.htm","5 дней назад",5),
("da-lat","Phường 9","lv","apartment",4500000,40,"Nội thất đầy đủ","/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134031142.htm","5 дней назад",5),
("da-lat","Phường 7","lb","apartment",12000000,100,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134031058.htm","5 дней назад",5),
("da-lat","Phường 8","lv","apartment",9000000,40,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134027271.htm","6 дней назад",6),
("da-lat","Phường 6","cl","apartment",4300000,30,None,"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134014611.htm","6 дней назад",6),

("da-nang","Q. Cẩm Lệ","hx","room",4500000,35,"Nội thất đầy đủ","/thue-phong-tro-quan-cam-le-da-nang/134101044.htm","7 часов назад",0),
("da-nang","Q. Cẩm Lệ","hx","room",2200000,25,"Nhà trống","/thue-phong-tro-quan-cam-le-da-nang/134132537.htm","7 часов назад",0),
("da-nang","Q. Sơn Trà","ah","room",6000000,35,None,"/thue-phong-tro-quan-son-tra-da-nang/134088159.htm","8 часов назад",0),
("da-nang","Q. Hải Châu","hcg","room",1900000,25,None,"/thue-phong-tro-quan-hai-chau-da-nang/134105033.htm","8 часов назад",0),
("da-nang","Q. Ngũ Hành Sơn","ns","room",2200000,15,"Nội thất đầy đủ","/thue-phong-tro-quan-ngu-hanh-son-da-nang/134130311.htm","8 часов назад",0),
("da-nang","Q. Hải Châu","hcg","room",2200000,10,"Nội thất cao cấp","/thue-phong-tro-quan-hai-chau-da-nang/133256155.htm","11 часов назад",0),
("da-nang","Q. Cẩm Lệ","hx","room",4600000,None,"Nhà trống","/thue-phong-tro-quan-cam-le-da-nang/134127031.htm","11 часов назад",0),
("da-nang","Q. Cẩm Lệ","hx","room",5800000,None,"Nội thất đầy đủ","/thue-phong-tro-quan-cam-le-da-nang/134127028.htm","11 часов назад",0),
("da-nang","Q. Cẩm Lệ","hx","room",4500000,None,"Nội thất đầy đủ","/thue-phong-tro-quan-cam-le-da-nang/134126939.htm","11 часов назад",0),
("da-nang","Q. Liên Chiểu","hk","room",3500000,None,"Nội thất đầy đủ","/thue-phong-tro-quan-lien-chieu-da-nang/134126926.htm","11 часов назад",0),

("da-nang","Q. Ngũ Hành Sơn","ns","apartment",7000000,35,"Nội thất đầy đủ","/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/133917935.htm","актуально",0),
("da-nang","Q. Liên Chiểu","lc","apartment",7500000,63,None,"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134140024.htm","2 часа назад",0),
("da-nang","Q. Cẩm Lệ","hx","apartment",5500000,35,"Nội thất đầy đủ","/thue-can-ho-chung-cu-quan-cam-le-da-nang/134130026.htm","актуально",0),
("da-nang","Q. Hải Châu","hcg","apartment",10900000,40,"Nội thất đầy đủ","/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134141495.htm","20 минут назад",0),
("da-nang","Q. Thanh Khê","tk","apartment",8500000,40,"Nội thất cao cấp","/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134140642.htm","1 час назад",0),
("da-nang","Q. Sơn Trà","ah","apartment",23000000,82,None,"/thue-can-ho-chung-cu-quan-son-tra-da-nang/133439929.htm","1 час назад",0),
("da-nang","Q. Ngũ Hành Sơn","ns","apartment",7500000,35,"Nội thất đầy đủ","/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/133740340.htm","1 час назад",0),
("da-nang","Q. Thanh Khê","tk","apartment",14500000,40,"Nội thất đầy đủ","/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134140345.htm","1 час назад",0),
("da-nang","Q. Hải Châu","hc","apartment",10500000,30,"Nội thất cao cấp","/thue-can-ho-chung-cu-quan-hai-chau-da-nang/133822899.htm","2 часа назад",0),
("da-nang","Q. Ngũ Hành Sơn","ns","apartment",5500000,35,None,"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134139843.htm","2 часа назад",0),
("da-nang","Q. Thanh Khê","tk","apartment",8500000,45,"Nội thất cao cấp","/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134139722.htm","2 часа назад",0),
("da-nang","Q. Ngũ Hành Sơn","ns","apartment",5200000,35,None,"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134139659.htm","2 часа назад",0),
("da-nang","Q. Sơn Trà","st","apartment",26000000,80,"Nội thất cao cấp","/thue-can-ho-chung-cu-quan-son-tra-da-nang/134139649.htm","2 часа назад",0),
("da-nang","Q. Cẩm Lệ","hx","apartment",6000000,35,"Nội thất đầy đủ","/thue-can-ho-chung-cu-quan-cam-le-da-nang/134139642.htm","2 часа назад",0),
("da-nang","Q. Cẩm Lệ","hx","apartment",5990000,40,None,"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134139582.htm","2 часа назад",0),
("da-nang","Q. Ngũ Hành Sơn","ns","apartment",8000000,35,None,"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134139574.htm","2 часа назад",0),
("da-nang","Q. Sơn Trà","ah","apartment",24500000,40,None,"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134139511.htm","2 часа назад",0),
("da-nang","Q. Sơn Trà","ah","apartment",10000000,35,"Nội thất đầy đủ","/thue-can-ho-chung-cu-quan-son-tra-da-nang/134139223.htm","2 часа назад",0),
("da-nang","Q. Sơn Trà","st","apartment",14000000,77,"Nội thất cao cấp","/thue-can-ho-chung-cu-quan-son-tra-da-nang/134139157.htm","2 часа назад",0),
("da-nang","Q. Ngũ Hành Sơn","ns","apartment",6000000,32,"Nội thất đầy đủ","/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134048057.htm","3 часа назад",0),
("da-nang","Q. Thanh Khê","tk","apartment",8500000,35,"Nội thất đầy đủ","/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134057584.htm","3 часа назад",0),
("da-nang","Q. Sơn Trà","ah","apartment",10000000,35,"Nội thất cao cấp","/thue-can-ho-chung-cu-quan-son-tra-da-nang/132402709.htm","3 часа назад",0),
]

TYPE_RU = {"room":"Комната","apartment":"Квартира"}
FURN_RU = {
  "Nội thất đầy đủ":"с полной мебелью","Nội thất cao cấp":"с мебелью повышенной комфортности",
  "Nhà trống":"без мебели",
}

lines = []
id_counter = 93
for city, old_d, key, kind, price, area, furn, suffix, posted, daysAgo in ROWS:
    type_ru = TYPE_RU[kind]
    furn_txt = (" " + FURN_RU[furn]) if furn in FURN_RU else ""
    city_ru = {"da-lat":"Далат","da-nang":"Дананг"}[city]
    desc = f"{type_ru}{furn_txt}, старый район {old_d}." if kind=="room" else f"Квартира{furn_txt}, старый район {old_d}."
    area_lit = "None" if area is None else str(area)
    desc_escaped = desc.replace('"','\\"')
    lines.append(
        f'L({id_counter},"{city}","{key}","{type_ru}",{price},{area_lit},\n'
        f'  "{desc_escaped}",\n'
        f'  N+"{suffix}","{posted}",{daysAgo},source="chotot"),\n'
    )
    id_counter += 1

NEW_LISTINGS_SRC = "\n".join(lines)

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = '''L(92,"da-nang","tk","Дом",14000000,90,
  "Дом с 3 спальнями, меблирован, район Thanh Khê (Xuân Hà).",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-do-phuong-xuan-ha-50/cho-kiet-uong-o-3-phong-ngu-u-noi-that-pr46175643","сегодня",0,source="batdongsan",
  details={"amenities":"3 спальни, полная мебель"}),
]'''
assert marker in content, "marker not found!"
new_content = content.replace(marker, marker[:-1] + "\n" + NEW_LISTINGS_SRC.strip() + "\n]", 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", id_counter-93, "listings, new length", len(new_content))
