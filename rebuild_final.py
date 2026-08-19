# -*- coding: utf-8 -*-
import json, re

W = "."
maps_data = json.load(open(W + "/maps_data.json", encoding="utf-8"))
nt_realtor = json.load(open(W + "/nt_realtor_map.json", encoding="utf-8"))

SHORT_LABEL = {
    "nt":"Nha Trang", "btr":"Bắc NT", "ntr":"Nam NT", "ttr":"Tây NT",
    "xh":"Xuân Hương", "lv":"Lâm Viên", "xt":"Xuân Trường", "cl":"Cam Ly", "lb":"Lang Biang",
    "hc":"Hải Châu", "hcg":"Hòa Cường", "tk":"Thanh Khê", "ak":"An Khê", "cl2":"Cẩm Lệ",
    "hx":"Hòa Xuân", "ns":"Ngũ Hành Sơn", "st":"Sơn Trà", "ah":"An Hải", "lc":"Liên Chiểu", "hk":"Hòa Khánh",
    "vtp":"Vũng Tàu", "tth":"Tam Thắng", "rd":"Rạch Dừa", "pth":"Phước Thắng",
    "qn":"Quy Nhơn", "qnd":"QN Đông", "qnt":"QN Tây", "qnn":"QN Nam", "qnb":"QN Bắc",
    "ha":"Hội An", "had":"Hội An Đông", "hat":"Hội An Tây",
    "pt":"Phan Thiết", "bt":"Bình Thuận", "put":"Phú Thủy", "mn":"Mũi Né", "tt":"Tiến Thành", "hth":"Hàm Thắng"
}
# city-scoped overrides — takes precedence when a district key collides with another city's key above
# (e.g. Ho Chi Minh's "ak"/An Khánh vs Da Nang's "ak"/An Khê, and the long-orphaned "btr"/"Bắc NT" entry)
SHORT_LABEL_SCOPED = {
    "ho-chi-minh:ak": "An Khánh", "ho-chi-minh:btr": "Bình Trưng"
}

def bbox_of(d):
    nums = [float(x) for x in re.findall(r'[-\d.]+', d)]
    xs, ys = nums[0::2], nums[1::2]
    return min(xs), min(ys), max(xs), max(ys)

for city, cdata in maps_data.items():
    for w in cdata["wards"]:
        x0,y0,x1,y1 = bbox_of(w["d"])
        w["bw"] = round(x1-x0,1); w["bh"] = round(y1-y0,1)
        w["showLabel"] = (min(w["bw"], w["bh"]) > 85)
        w["short"] = SHORT_LABEL_SCOPED.get(city+":"+w["key"], SHORT_LABEL.get(w["key"], w["name"]))

# ---------------- CITIES (real current wards) ----------------
CITIES = {
    "nha-trang": {
        "name": "Нячанг",
        "districts": [
            {"key":"vh","name":"Vĩnh Hải","hint":"север, Хон Чонг","color":"#4E79A7"},
            {"key":"vp","name":"Vĩnh Phước","hint":"север, Mường Thanh Viễn Triều","color":"#F28E2B"},
            {"key":"vt2","name":"Vạn Thạnh","hint":"центр-север, старый город","color":"#B07AA1"},
            {"key":"ps","name":"Phương Sài","hint":"у ж/д вокзала","color":"#76B7B2"},
            {"key":"nh","name":"Ngọc Hiệp","hint":"запад, у реки Cái","color":"#E15759"},
            {"key":"ph","name":"Phước Hải","hint":"рынок Chợ Đầm, Hà Quang 2","color":"#EDC949"},
            {"key":"lt","name":"Lộc Thọ","hint":"центр, набережная Trần Phú","color":"#9C755F"},
            {"key":"ph2","name":"Phước Hòa","hint":"центр-запад, Lam Sơn","color":"#D37295"},
            {"key":"tl","name":"Tân Lập","hint":"центр, «русский квартал»","color":"#86BCB6"},
            {"key":"pl","name":"Phước Long","hint":"запад, спальный район, HUD","color":"#FF9DA7"},
            {"key":"vt","name":"Vĩnh Trường","hint":"юг, An Viên","color":"#F1CE63"},
            {"key":"vn","name":"Vĩnh Nguyên","hint":"юг, паром на Хон Тре","color":"#D4A6C8"}
        ]
    },
    "da-lat": {
        "name": "Далат",
        "districts": [
            {"key":"xh","name":"Phường Xuân Hương - Đà Lạt","hint":"центр, озеро Xuân Hương"},
            {"key":"lv","name":"Phường Lâm Viên - Đà Lạt","hint":"юго-восток, у университета"},
            {"key":"xt","name":"Phường Xuân Trường - Đà Lạt","hint":"восток, пригород"},
            {"key":"cl","name":"Phường Cam Ly - Đà Lạt","hint":"запад"},
            {"key":"lb","name":"Phường Lang Biang - Đà Lạt","hint":"север, Măng Lin и гора Лангбианг"}
        ]
    },
    "da-nang": {
        "name": "Дананг",
        "districts": [
            {"key":"hc","name":"Phường Hải Châu","hint":"центр"},
            {"key":"hcg","name":"Phường Hòa Cường","hint":"центр-юг, много sleepbox/студий"},
            {"key":"tk","name":"Phường Thanh Khê","hint":"центр-север"},
            {"key":"ak","name":"Phường An Khê","hint":"запад-центр"},
            {"key":"cl2","name":"Phường Cẩm Lệ","hint":"юг"},
            {"key":"hx","name":"Phường Hòa Xuân","hint":"юг, за рекой"},
            {"key":"ns","name":"Phường Ngũ Hành Sơn","hint":"юго-восток, пляж Mỹ An, рядом FPT"},
            {"key":"st","name":"Phường Sơn Trà","hint":"полуостров, пляж Mỹ Khê"},
            {"key":"ah","name":"Phường An Hải","hint":"восток, у реки"},
            {"key":"lc","name":"Phường Liên Chiểu","hint":"север"},
            {"key":"hk","name":"Phường Hòa Khánh","hint":"северо-запад, студенческий район"}
        ]
    },
    "vung-tau": {
        "name": "Вунгтау",
        "districts": [
            {"key":"vtp","name":"Phường Vũng Tàu","hint":"центр, все старые пляжи Bãi Trước/Bãi Sau"},
            {"key":"rd","name":"Phường Rạch Dừa","hint":"север, у залива Bãi Trước"},
            {"key":"pth","name":"Phường Phước Thắng","hint":"юг, аэропорт, Bãi Sau на юге"},
            {"key":"tth","name":"Phường Tam Thắng","hint":"дальний север, Лонг Шон, промзона"}
        ]
    },
    "quy-nhon": {
        "name": "Куинён",
        "districts": [
            {"key":"qn","name":"Phường Quy Nhơn","hint":"центр, пляж Xuân Diệu"},
            {"key":"qnd","name":"Phường Quy Nhơn Đông","hint":"восток, полуостров Nhơn Lý/Nhơn Hải, Kỳ Co"},
            {"key":"qnt","name":"Phường Quy Nhơn Tây","hint":"запад, Bùi Thị Xuân"},
            {"key":"qnn","name":"Phường Quy Nhơn Nam","hint":"юг, Ghềnh Ráng, Quy Hòa"},
            {"key":"qnb","name":"Phường Quy Nhơn Bắc","hint":"север, Nhơn Phú"}
        ]
    },
    "hoi-an": {
        "name": "Хойан",
        "districts": [
            {"key":"ha","name":"Phường Hội An","hint":"старый город, центр"},
            {"key":"had","name":"Phường Hội An Đông","hint":"восток, пляж Cửa Đại"},
            {"key":"hat","name":"Phường Hội An Tây","hint":"запад, пляж An Bàng/Tân Thành"}
        ]
    },
    "phan-thiet": {
        "name": "Фантьет / Муйне",
        "districts": [
            {"key":"mn","name":"Phường Mũi Né","hint":"курортная зона, Хам Тьен, пляж Мюйне"},
            {"key":"pt","name":"Phường Phan Thiết","hint":"центр города"},
            {"key":"put","name":"Phường Phú Thủy","hint":"центр-восток, у моря"},
            {"key":"bt","name":"Phường Bình Thuận","hint":"запад, аэропорт"},
            {"key":"tt","name":"Phường Tiến Thành","hint":"юг, пляж Đồi Dương"},
            {"key":"hth","name":"Phường Hàm Thắng","hint":"северо-запад, вдали от моря"}
        ]
    },
    "ho-chi-minh": {
        "name": "Хошимин",
        "districts": [
            {"key":"tm","name":"Phường Tân Mỹ","hint":"Phú Mỹ Hưng, ЖК The Ascentia и рядом"},
            {"key":"th","name":"Phường Tân Hưng","hint":"Phú Mỹ Hưng, ядро — Crescent Mall, Cầu Ánh Sao"},
            {"key":"ak","name":"Phường An Khánh","hint":"Thảo Điền, экспат-район, Masteri Thảo Điền"},
            {"key":"btr","name":"Phường Bình Trưng","hint":"An Phú восточнее — Estella Heights, Palm Heights"},
            {"key":"bq","name":"Phường Bình Quới","hint":"полуостров Thanh Đa"},
            {"key":"bth","name":"Phường Bến Thành","hint":"исторический центр, бывший Quận 1"},
            {"key":"kh","name":"Phường Khánh Hội","hint":"бывший Quận 4, рядом с центром, набирает популярность"}
        ]
    }
}

SOURCES = [
    {"key":"chotot","label":"Chợ Tốt / Nhà Tốt","short":"Chợ Tốt","active":True,"color":"#C7452B"},
    {"key":"facebook","label":"Facebook-группы","short":"Facebook","active":True,"color":"#3B5FA6"},
    {"key":"batdongsan","label":"Batdongsan.com.vn","short":"Batdongsan","active":True,"color":"#E0862B"},
    {"key":"telegram","label":"Telegram-каналы","short":"Telegram","active":True,"color":"#1E9FE0"},
    {"key":"airbnb","label":"Airbnb (помесячно)","short":"Airbnb","active":True,"color":"#FF385C"},
    {"key":"tripcom","label":"Trip.com (помесячно)","short":"Trip.com","active":True,"color":"#1F6FD6"},
    {"key":"vrbo","label":"Vrbo (помесячно)","short":"Vrbo","active":True,"color":"#0074E4"},
    {"key":"booking","label":"Booking.com (помесячно)","short":"Booking","active":True,"color":"#003580"},
    {"key":"fbmarketplace","label":"Facebook Marketplace","short":"FB Marketplace","active":True,"color":"#2E7CF6"}
]

FB_GROUPS = {
    "nha-trang": [
        {"name":"NHÀ ĐẤT NHA TRANG ✅","members":"149,8 тыс.","url":"https://www.facebook.com/groups/NhaDatNhaTrang/","note":"недвижимость шире — есть и продажа, и аренда","joined":True},
        {"name":"Nha Trang Apartment And House For Rent ✅","members":"—","url":"https://www.facebook.com/groups/nhatrang.apartment.and.house/","note":"аренда квартир и домов","joined":True},
        {"name":"Căn hộ cho thuê Nha Trang","members":"62 тыс.","url":"https://www.facebook.com/groups/593714207638751/","note":"структурированные объявления с ценой, как Marketplace","joined":True},
        {"name":"Cho Thuê Căn Hộ Giá Rẻ Nha Trang","members":"—","url":"https://www.facebook.com/groups/chothuecanhogiarenhatrang/","note":"бюджетные квартиры","joined":True},
        {"name":"Cho Thuê Nhà & Phòng Trọ Sinh Viên NHA TRANG","members":"—","url":"https://www.facebook.com/groups/238809506689365/","note":"комнаты и жильё для студентов","joined":True}
    ],
    "da-lat": [
        {"name":"CHO THUÊ NHÀ NGUYÊN CĂN ĐÀ LẠT ✅","members":"105 тыс.","url":"https://www.facebook.com/groups/975470559939040/","note":"аренда домов целиком","joined":False},
        {"name":"PHÒNG TRỌ - NHÀ CHO THUÊ ĐÀ LẠT","members":"70 тыс.","url":"https://www.facebook.com/groups/211616406116962/","note":"комнаты и дома","joined":False},
        {"name":"NHÀ VÀ CĂN HỘ CHO THUÊ ĐÀ LẠT / DALAT HOUSE AND APARTMENT FOR RENT","members":"50 тыс.","url":"https://www.facebook.com/groups/356237492011374/","note":"дома и квартиры","joined":False},
        {"name":"CHO THUÊ NHÀ ĐÀ LẠT","members":"49 тыс.","url":"https://www.facebook.com/groups/1607478209766787/","note":"общая аренда домов","joined":False},
        {"name":"THUÊ PHÒNG ĐÀ LẠT","members":"42 тыс.","url":"https://www.facebook.com/groups/2132944206982026/","note":"комнаты, квартиры, дома целиком","joined":False}
    ],
    "da-nang": [
        {"name":"Phòng Trọ, Căn Hộ, Nhà Đà Nẵng Cho Thuê","members":"225 тыс.","url":"https://www.facebook.com/groups/phongtrocanhonhadanang/","note":"комнаты, квартиры, дома","joined":False},
        {"name":"Cho Thuê Nhà Nguyên Căn Đà Nẵng","members":"165 тыс.","url":"https://www.facebook.com/groups/476056366996433/","note":"аренда домов целиком","joined":False},
        {"name":"CĂN HỘ CHO THUÊ ĐÀ NẴNG","members":"145 тыс.","url":"https://www.facebook.com/groups/599988861199745/","note":"квартиры","joined":False},
        {"name":"Cho Thuê Nhà Nguyên Căn Giá Rẻ Đà Nẵng","members":"86 тыс.","url":"https://www.facebook.com/groups/682623845225623/","note":"бюджетные дома","joined":False},
        {"name":"Căn hộ cho thuê Đà Nẵng (Apartment for rent in Danang)","members":"68 тыс.","url":"https://www.facebook.com/groups/198876884532146/","note":"квартиры","joined":False}
    ],
    "ho-chi-minh": [
        {"name":"Housing in Saigon (Ho Chi Minh City, Vietnam)","members":"43 тыс.","url":"https://www.facebook.com/groups/housing.HCMC","note":"общегородская, охватывает все 5 районов подборки","joined":False},
        {"name":"PHÒNG TRỌ QUẬN 1","members":"249,7 тыс.","url":"https://www.facebook.com/groups/q1.phongtro.club/","note":"комнаты и квартиры именно по Quận 1 / Bến Thành","joined":False},
        {"name":"PHÒNG TRỌ QUẬN 4","members":"244 тыс.","url":"https://www.facebook.com/groups/q4.phongtro.club/","note":"комнаты и квартиры именно по Quận 4 / Khánh Hội","joined":False},
        {"name":"TÔI LÀ DÂN THẢO ĐIỀN - AN PHÚ - BÌNH AN","members":"—","url":"https://www.facebook.com/groups/anphuthaodienneighbours/","note":"резидентское сообщество Thảo Điền/An Phú, включает аренду","joined":False},
        {"name":"Phu My Hung District 7 Expats","members":"—","url":"https://www.facebook.com/groups/phumyhung7/","note":"экспат-сообщество Phú Mỹ Hưng","joined":False},
        {"name":"GROUP CĂN HỘ ASCENTIA - THE ANTONIA PHÚ MỸ HƯNG","members":"—","url":"https://www.facebook.com/groups/590911979369020/","note":"узкоспециализированная — именно по The Ascentia и соседнему The Antonia","joined":False}
    ]
}

N = "https://www.nhatot.com"

def L(id, city, district, type_, price, area, desc, url, posted, daysAgo, source="chotot", details=None):
    d = {"id":id,"city":city,"district":district,"type":type_,"price":price,"area":area,"desc":desc,
         "url":url,"posted":posted,"daysAgo":daysAgo,"source":source}
    if details: d["details"] = details
    return d

LISTINGS = [
L(1,"nha-trang","ps","Комната",1200000,15,"Свободная комната без мебели, в 500 м от супермаркета Go.",N+"/thue-phong-tro-thanh-pho-nha-trang-khanh-hoa/131349887.htm","4 дня назад",4,details={"deposit":"1,2 млн ₫ (1 мес.)","amenities":"свой санузел, wifi включён"}),
L(2,"nha-trang","ps","Комната",4500000,30,"Меблированная комната в 150 м от ж/д вокзала, в центре города.",N+"/thue-phong-tro-thanh-pho-nha-trang-khanh-hoa/133983315.htm","4 дня назад",4,details={"deposit":"9 млн ₫ (2 мес.)","electricity":"4 500 ₫/кВт·ч","water":"70 000 ₫/чел./мес","internet":"90 000 ₫/чел./мес","amenities":"холодильник, кровать, кондиционер, ТВ 50\", стиральная машина, индукционная плита с посудой, фильтр для воды, свой санузел с горячей водой, место для мотобайка в доме","contract":"гибкий, 3-6-12 мес."}),
L(3,"nha-trang","nh","Комната",3700000,26,"Меблированная комната у моста Cầu Hộ, район Phương Sài.",N+"/thue-phong-tro-thanh-pho-nha-trang-khanh-hoa/133818297.htm","2 недели назад",14,details={"deposit":"3,7 млн ₫ (1 мес.)","internet":"100 тыс ₫/мес (wifi отдельно)","amenities":"на 1-2 человек, не общий хозяин","contract":"6 мес. - 1 год"}),
L(4,"nha-trang","vt","Студия",6000000,27,"Студия с окном в переулке от ул. Trần Phú, лифт, вход по отпечатку пальца.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134095132.htm","2 дня назад",2,details={"deposit":"без отдельного депозита","electricity":"4 500 ₫/кВт·ч","water":"100 000 ₫/чел.","managementFee":"150 000 ₫/комната (wifi, мусор, лифт, управление)","amenities":"лифт, замок по отпечатку пальца, общая кухня/прачечная","policy":"разрешены животные, принимают электроскутеры, есть парковка авто","contract":"6 млн ₫ при 3-12 мес., 6,5 млн ₫ при 1-2 мес."}),
L(5,"nha-trang","tl","Квартира",26000000,89,"Угловая квартира с 3 спальнями, полностью новая мебель топ-класса, ЖК HUD Building.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133795648.htm","2 дня назад",2,details={"deposit":"2 месяца","amenities":"3 спальни, 2 санузла, 4 кондиционера, ТВ, стиральная машина, электроплита, вытяжка — всё новое","notice":"цена НЕ включает управление и коммунальные платежи","contract":"долгосрочная аренда; есть также вариант 2BR дешевле"}),
L(6,"nha-trang","vt","Студия",9500000,30,"VIP-студия в прибрежном квартале An Viên, южная часть города, бесплатный бассейн.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134094594.htm","2 дня назад",2,details={"deposit":"1 месяц","electricity":"4 500 ₫/кВт·ч","water":"150 000 ₫/чел.","internet":"150 000 ₫/мес","managementFee":"200 000 ₫/мес","amenities":"бесплатный бассейн, 4 этаж, лифт, своя кухня, общая прачечная","policy":"животные с доплатой, электроскутеры без зарядки, есть парковка авто"}),
L(7,"nha-trang","lt","Квартира",14000000,47,"Апартаменты в комплексе Panorama на первой линии, вид на море.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133287892.htm","1 день назад",1,details={"deposit":"2 мес. (оплата за 1)","electricity":"3 218 ₫/кВт·ч","water":"15 374 ₫/м³","managementFee":"25 300 ₫/м² (≈1,19 млн ₫ за 47 м²)","internet":"240 тыс ₫/мес (wifi)","amenities":"бассейн с бесконечным краем и тренажёрный зал бесплатно (9:00-18:00), рядом ночной рынок и квартал «Phố Tây»","notice":"парковка отдельно: авто 1,2 млн ₫/мес, мотобайк 180 тыс ₫/мес"}),
L(8,"da-lat","xh","Студия",3500000,25,"Меблированная студия в самом центре Далата, рядом рынок и озеро Xuân Hương.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/134125554.htm","13 часов назад",0,details={"deposit":"3,5 млн ₫","amenities":"ТВ, холодильник, шкаф, индукционная плита, аэрогриль, микроволновка, рисоварка, стиральная и сушильная машина, промышленный водонагреватель","notice":"электричество на горячую воду включено, скоростной wifi включён","contract":"цена 3,5-4,5 млн в зависимости от антресоли; 5 мин до рынка/ночного рынка/озера, 10 мин пешком до собора Кон Га, 10 мин до университета"}),
L(9,"da-lat","xh","Студия",3500000,20,"Меблированная студия рядом с центром, у озера Xuân Hương, охраняемый район.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/132775618.htm","16 часов назад",0,details={"deposit":"3,5 млн ₫","amenities":"балкон, парковка, охраняемый район","notice":"сдаются 2 квартиры, цена зависит от конкретной; 10 мин пешком до рынка, супермаркета и озера"}),
L(10,"da-lat","lv","Комната",1600000,25,"Комната с мебелью в 200 м от Далатского университета.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133999135.htm","2 дня назад",2,details={"deposit":"1 млн ₫ (ниже месячной платы)","electricity":"2 000 ₫/кВт·ч","water":"20 000 ₫/м³","amenities":"водонагреватель на солнечных батареях, свой санузел, можно готовить в комнате, скоростной wifi, охраняемая парковка, камеры 24/7","notice":"1,6 млн ₫ на 1 человека, +300 тыс за второго; 100 м до Bách Hóa Xanh/Vinmart, 150 м до рынка Bùi Thị Xuân"}),
L(11,"da-lat","xh","Студия",4500000,30,"Студия с лифтом и видом на улицу, рядом с рынком Далата.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/130989655.htm","9 дней назад",9,details={"deposit":"4,5 млн ₫","amenities":"лифт, полный набор кухонной утвари, еженедельная смена белья, бесплатная парковка мотобайков","notice":"есть посуточная аренда: 500 тыс ₫/сутки; 5 мин пешком до рынка Далата"}),
L(12,"da-lat","lb","Комната",2000000,25,"Просторная меблированная комната в районе Măng Lin, рядом гора Лангбианг.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/132696809.htm","11 дней назад",11,details={"deposit":"1 млн ₫","notice":"электричество, вода, стиральная машина, фильтр воды и wifi — ВСЁ ВКЛЮЧЕНО в цену","amenities":"деревянная кровать с толстым матрасом, шкаф, ТВ 50\", мини-холодильник, свой санузел, общая кухня, место для сушки белья, парковка","contract":"2 млн ₫ (+200 тыс за второго человека), есть более дешёвый цокольный вариант — 1,5 млн ₫; рядом резорт Lý Nhã Kỳ и The Nest Mây Lang Thang"}),
L(13,"da-nang","hc","Комната",1400000,38,"Койко-место в меблированной комнате (дорм), район Hải Châu.",N+"/thue-phong-tro-quan-hai-chau-da-nang/126893939.htm","4 дня назад",4,details={"deposit":"1 млн ₫","amenities":"кондиционер, холодильник, стиральная машина, просторная кухня и парковка, wifi бесплатно, отдельные хозяева","notice":"⚠ хозяин прямо указывает: не сдаёт иностранцам и не разрешает электроскутеры"}),
L(14,"da-nang","hk","Комната",3500000,25,"Комната с мебелью, лифт, повышенная безопасность, район Hòa Khánh (студенческий).",N+"/thue-phong-tro-quan-lien-chieu-da-nang/133224687.htm","12 дней назад",12,details={"deposit":"не указан отдельно","amenities":"японский дизайн, кухня отделена от спальни, звукоизоляция, своё эл./водоснабжение со счётчиком, wifi быстрый, кондиционер Sharp, водонагреватель Ariston, сантехника American/Inax, лифт с картой, стальная дверь, умный замок (отпечаток/код/карта), камеры 24/7, пожарная сигнализация","notice":"реальная цена 3,5-4,3 млн ₫ в зависимости от площади (20-25 м²); 6 мест для машин, 1 км до университетов, 2 км до пляжа"}),
L(15,"da-nang","hcg","Комната",2200000,25,"Sleepbox-комната у супермаркета Lotte, район Hòa Cường.",N+"/thue-phong-tro-quan-hai-chau-da-nang/133822106.htm","2 часа назад",0,details={"deposit":"2,2 млн ₫","notice":"цена всё включено (полный пакет, без доп. расходов)","amenities":"кондиционер 24/7, ежедневная уборка и смена белья, тихая читальная зона, общая кухня, скоростной лифт, камеры 24/7","contract":"рядом Lotte Mart, университеты Đông Á/Kiến Trúc/Ngoại Ngữ/Kinh Tế (5 мин), пляж Sao Biển (7 мин), Asia Park/ночной рынок/Helio (1 км)"}),
L(16,"da-nang","ns","Комната",7000000,35,"Комната рядом с университетами (Đà Nẵng, Kinh Tế), кухня отдельно от спальни.",N+"/thue-phong-tro-quan-ngu-hanh-son-da-nang/134112626.htm","2 часа назад",0,details={"deposit":"не указан","amenities":"кухня отдельно от спальни (без запаха), стиральная машина, водонагреватель, электроплита, холодильник, просторная комната","notice":"2 км до университета экономики"}),
L(17,"da-nang","ns","Студия",4000000,25,"Новая студия рядом с университетом FPT.",N+"/thue-phong-tro-quan-ngu-hanh-son-da-nang/133529184.htm","3 часа назад",0,details={"deposit":"4 млн ₫","amenities":"дом только что построен, лифт, холодильник, своя стиральная машина, кондиционер, водонагреватель, встроенная плита, кровать/шкаф/стол, просторная парковка","notice":"реальная цена 4-6 млн ₫ в зависимости от комнаты; рядом университеты FPT/Việt Hàn/Y Dược/Phan Châu Trinh"}),
L(18,"nha-trang","ph","Квартира",12500000,None,"Меблированная 1-спальная квартира с просторным балконом, тихий охраняемый ЖК Megas, район Ha Quang 2 (Phước Hải).","https://www.facebook.com/commerce/listing/2324510467957151/","несколько минут назад",0,source="facebook",details={"amenities":"качественная мебель, современный дизайн, просторный балкон, скоростной wifi","notice":"тихий охраняемый комплекс, рядом с центром"}),
L(19,"nha-trang","tl","Студия",7000000,30,"Студия у ул. Bạch Đằng, в самом центре, рядом с морем.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/132486128.htm","5 дней назад",5,details={"deposit":"7 млн ₫ (1 мес.)","electricity":"4 500 ₫/кВт·ч","water":"150 000 ₫/чел./мес","managementFee":"200 000 ₫/комната","amenities":"кухня, стиральная машина, кондиционер, кровать, шкаф, обеденный стол","policy":"разрешены животные, БЕЗ детей","contract":"гибкий, оплата помесячно"}),
L(20,"nha-trang","tl","Студия",6500000,35,"Студия на 6 этаже у рынка Xóm Mới, в центре Нячанга.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/132917328.htm","3 часа назад",0,details={"deposit":"6,5 млн ₫ (1 мес.)","electricity":"4 500 ₫/кВт·ч","water":"150 000 ₫/чел./мес","managementFee":"200 000 ₫/комната","policy":"БЕЗ животных, без детей","contract":"гибкий, оплата помесячно; рядом рынок Xóm Mới"}),
L(21,"nha-trang","vp","Квартира",16000000,74,"Угловая квартира с видом на море, средний этаж, роскошная мебель.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134136670.htm","1 час назад",0,details={"deposit":"2 мес. + 1 мес. оплата","amenities":"вся техника, качественный ремонт","contract":"6-12 мес."}),
L(22,"nha-trang","vh","Студия",3500000,35,"Студия с балконом, общая прачечная и санузел.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134136341.htm","2 часа назад",0,details={"water":"100 000 ₫/чел.","internet":"120 000 ₫ (wifi + прачечная)","electricity":"≈4 500 ₫/кВт·ч","contract":"12 мес."}),
L(23,"nha-trang","vh","Студия",16000000,42,"Премиум-студия в комплексе Vega City / Libera с видом на море.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134136252.htm","2 часа назад",0,details={"electricity":"4 500 ₫/кВт·ч","water":"100 000 ₫/чел.","internet":"250 000 ₫/мес","managementFee":"включена в цену","amenities":"5 этаж, бассейн и спортзал бесплатно","notice":"старый район — Phường Vĩnh Hòa, нанесена на ближайший район Vĩnh Hải"}),
L(24,"nha-trang","lt","Студия",15000000,35,"Премиум-студия в комплексе Panorama, вид на город, балкон.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134136030.htm","2 часа назад",0,details={"amenities":"большая кровать, бассейн и спортзал на 6 этаже бесплатно","policy":"животные запрещены"}),
L(25,"nha-trang","lt","Квартира",14000000,60,"Угловая 1-спальная квартира в ЖК Maple, вид на площадь, балкон.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134135900.htm","2 часа назад",0,details={"deposit":"1 месяц","notice":"коммуналка отдельно","policy":"животные запрещены"}),
L(26,"nha-trang","lt","Квартира",14000000,55,"Премиум 1-спальная квартира в Tui Blue/Ariyana, 19 этаж, вид на море.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134135732.htm","2 часа назад",0,details={"deposit":"1 месяц","amenities":"отдельная кухня, стиральная машина","notice":"от 6 мес. аренды, коммуналка отдельно"}),
L(27,"nha-trang","pl","Студия",6600000,40,"Студия на 1 этаже (без лифта), новая мебель.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134134611.htm","3 часа назад",0,details={"electricity":"4 500 ₫/кВт·ч","water":"120 000 ₫/чел.","managementFee":"100 000 ₫/комната","policy":"животные и электроскутеры запрещены"}),
L(28,"nha-trang","lt","Квартира",5800000,30,"1-спальная квартира от частного хозяина, безопасный район, 200 м до моря.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/132849433.htm","3 часа назад",0,details={"amenities":"лифт, новый чистый дом"}),
L(29,"nha-trang","vh","Студия",10000000,30,"Люкс-студия с лифтом, общая прачечная на крыше.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134133685.htm","4 часа назад",0,details={"deposit":"1 месяц","electricity":"4 500 ₫/кВт·ч","water":"120 000 ₫/чел.","managementFee":"200 000 ₫/мес","policy":"животные запрещены"}),
L(30,"nha-trang","vp","Квартира",13000000,62,"2-спальная квартира в Mường Thanh Viễn Triều, 22 этаж, полная мебель.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134132852.htm","4 часа назад",0,details={"managementFee":"500 000 ₫/мес","internet":"275 000 ₫/мес","notice":"сервис/проживание 200 000 ₫, свободна с 20.08, контракт 3-6-12 мес."}),
L(31,"nha-trang","vt","Квартира",10000000,70,"2-спальная квартира в ЖК PH, сдаёт собственник, рядом с морем.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134067952.htm","1 день назад",1,details={"deposit":"20 млн ₫","notice":"цена договорная для хороших арендаторов"}),
L(32,"da-lat","lb","Комната",2500000,120,"Просторная комната с отдельной кухней, у дороги.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/134111439.htm","1 день назад",1,details={"deposit":"2,5 млн ₫","notice":"цена договорная, 2,5-3 млн ₫"}),
L(33,"da-lat","xh","Комната",3000000,30,"Меблированная комната в комплексе «Phố Châu Âu», 2 км от рынка.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133796481.htm","2 дня назад",2,details={"deposit":"3 млн ₫","amenities":"свой санузел, свободный график","notice":"wifi и вывоз мусора бесплатно; депозит возвращают при уведомлении за месяц"}),
L(34,"da-lat","xh","Комната",3500000,35,"Меблированная комната в центре, готова к заселению.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/134089789.htm","2 дня назад",2,details={"deposit":"3,5 млн ₫","amenities":"матрас, холодильник, базовая мебель"}),
L(35,"da-lat","lv","Комната",4000000,45,"Комната с балконом на зелень, в охраняемом районе с камерами.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133017987.htm","5 дней назад",5,details={"amenities":"рядом школы, больница, рынок","notice":"подходит для семьи"}),
L(36,"da-lat","xh","Комната",3000000,30,"Комната с балконом, вид на «Европейский квартал» и закат в долине.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133979567.htm","6 дней назад",6,details={"notice":"3,3 млн ₫/чел при долгосрочной аренде от 4 мес., +500 тыс. за доп. человека, коммуналка отдельно"}),
L(37,"da-lat","lv","Дом",6000000,140,"Дом целиком с антресолью, 2 спальни, 2 санузла.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133998244.htm","7 дней назад",7,details={"deposit":"12 млн ₫ (договорной)","amenities":"солнечный водонагреватель","notice":"рядом рынок и школа"}),
L(38,"da-lat","cl","Комната",5000000,40,"Просторная комната/дом с 2 спальнями, кухней и большим двором.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133597996.htm","7 дней назад",7,details={"deposit":"5 млн ₫"}),
L(39,"da-lat","lv","Квартира",11000000,85,"2-спальная квартира с садом и видом на долину, парковка для авто.","https://www.facebook.com/groups/975470559939040/","12 августа",2,source="facebook",details={"deposit":"1+1","notice":"принимают иностранцев, рядом школа/больница/рынок. Прямой ссылки на пост нет — открывает группу, ищите по автору (Nguyễn Hiếu) или контакту 0854526727"}),
L(40,"da-lat","xh","Дом",20000000,None,"Вилла целиком, 4 комнаты, 3 санузла, зона барбекю.","https://www.facebook.com/groups/975470559939040/","недавно",2,source="facebook",details={"deposit":"2+2","amenities":"парковка на 2 авто, стиральная машина","notice":"только для проживания, не для бизнеса. Прямой ссылки на пост нет — открывает группу, контакт 0896520000"}),
L(41,"da-lat","xh","Дом",7000000,None,"Дом с антресолью, 2 спальни, полностью меблирован, в центре.","https://www.facebook.com/groups/975470559939040/","недавно",2,source="facebook",details={"deposit":"1+1","notice":"готов к заселению. Прямой ссылки на пост нет — открывает группу, контакт 0886985774"}),
L(42,"da-nang","ah","Комната",6500000,37,"Меблированная комната у моста Cầu Rồng и пляжа Mỹ Khê, свой санузел и кухня.",N+"/thue-phong-tro-quan-son-tra-da-nang/134138150.htm","38 минут назад",0,details={"amenities":"кондиционер, водонагреватель, оптоволоконный интернет, охрана и парковка","notice":"рассчитана на 2-3 человек"}),
L(43,"da-nang","ak","Комната",3000000,20,"Комната без мебели в новостройке, с антресолью.",N+"/thue-phong-tro-quan-thanh-khe-da-nang/134135087.htm","3 часа назад",0,details={"deposit":"1 млн ₫","amenities":"кондиционер, водонагреватель, своя кухня и санузел, отдельный счётчик электричества"}),
L(44,"da-nang","hcg","Комната",1900000,20,"Sleepbox-капсула с личным замком, всё включено.",N+"/thue-phong-tro-quan-hai-chau-da-nang/134109376.htm","1 час назад",0,details={"notice":"цена всё включено: кондиционер 24/7, wifi, общая прачечная и кухня; для студентов, рядом вузы"}),
L(45,"da-nang","lc","Комната",1000000,15,"Комната рядом с промзоной Hòa Khánh и университетом Bách Khoa.",N+"/thue-phong-tro-quan-lien-chieu-da-nang/132038009.htm","2 часа назад",0,details={"deposit":"1 месяц","notice":"тихо и безопасно, подходит для семьи"}),
L(46,"da-nang","tk","Комната",3500000,35,"Последняя свободная комната в вилле у дороги.",N+"/thue-phong-tro-quan-thanh-khe-da-nang/131337146.htm","2 часа назад",0,details={"amenities":"кондиционер, водонагреватель, ванна, отдельный санузел","notice":"приоритет студентам на долгий срок"}),
L(47,"da-nang","hx","Комната",2500000,30,"Комната с большими окнами и антресолью.",N+"/thue-phong-tro-quan-cam-le-da-nang/134052003.htm","2 часа назад",0,details={"notice":"водонагреватель включён в цену"}),
L(48,"da-nang","hcg","Комната",4500000,20,"Комната в новом здании рядом с университетским городком.",N+"/thue-phong-tro-quan-hai-chau-da-nang/134100312.htm","3 часа назад",0,details={"amenities":"общая кухня, парковка, отдельный вход","electricity":"по гостарифу","notice":"есть комбо из 2 комнат за 8 млн ₫"}),
L(49,"da-nang","ns","Студия",9000000,None,"Студия с лифтом и собственной стиркой/сушкой.","https://www.facebook.com/groups/phongtrocanhonhadanang/","недавно",1,source="facebook",details={"electricity":"≈4 000 ₫/кВт·ч","water":"150 000 ₫/чел. (включая сервис)","deposit":"1+1","contract":"6 мес., макс. 2 человека","notice":"принимают иностранцев. Прямой ссылки на пост нет — открывает группу, пост от HT Trúc, контакт 0398299098"}),
L(50,"da-nang","ns","Квартира",10000000,None,"1-спальная квартира (кв. P402), премиум-мебель, готова к заселению.","https://www.facebook.com/groups/phongtrocanhonhadanang/","недавно",1,source="facebook",details={"policy":"разрешены животные","notice":"Прямой ссылки на пост нет — открывает группу, контакт +84796777003"}),
L(51,"da-nang","cl2","Дом",15000000,105,"Дом целиком, 3 этажа, 2 спальни, 3 санузла, двор.","https://www.facebook.com/groups/476056366996433/","недавно",1,source="facebook",details={"deposit":"1 месяц","amenities":"кондиционер, водонагреватель","notice":"оплата за 3 или 6 мес.; подходит и для бизнеса. Прямой ссылки на пост нет — открывает группу"}),
L(52,"da-nang","ns","Другое",16000000,None,"1-спальная квартира, полностью меблирована — витринное помещение под смешанное использование (жильё или спа/салон).","https://www.facebook.com/groups/476056366996433/","недавно",1,source="facebook",details={"notice":"рядом университет экономики, район An Thượng. Прямой ссылки на пост нет — открывает группу"}),
L(53,"nha-trang","ph","Квартира",12000000,None,"Квартира в ЖК CT3 VCN Phước Hải, меблированная.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134081850.htm","вчера",1,details={"amenities":"полная мебель","notice":"площадь в объявлении указана некорректно (751 м² — опечатка), уточняйте у автора"}),
L(54,"nha-trang","pl","Квартира",16000000,72,"2-спальная квартира, район Phước Long.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133775400.htm","вчера",1),
L(55,"nha-trang","pl","Квартира",13000000,72,"2-спальная квартира, район Phước Long.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134101805.htm","вчера",1),
L(56,"nha-trang","tl","Квартира",7000000,30,"Квартира-студия в центре, район Tân Lập.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133965062.htm","2 дня назад",2),
L(57,"nha-trang","vp","Квартира",14000000,71,"Квартира, район Vĩnh Phước.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134096027.htm","2 дня назад",2),
L(58,"nha-trang","tl","Студия",4500000,28,"Бюджетная студия в центре, район Tân Lập.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/132649264.htm","2 дня назад",2),
L(59,"nha-trang","ph","Квартира",6000000,40,"Меблированная квартира, район Phước Hải.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134095066.htm","2 дня назад",2,details={"amenities":"полная мебель"}),
L(60,"nha-trang","pl","Квартира",6500000,50,"Меблированная квартира, район Phước Long.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134094975.htm","2 дня назад",2,details={"amenities":"полная мебель"}),
L(61,"nha-trang","ph2","Квартира",7500000,40,"Меблированная квартира, район Phước Hòa (Lam Sơn).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134094877.htm","2 дня назад",2,details={"amenities":"полная мебель"}),
L(62,"nha-trang","ph2","Студия",6500000,30,"Меблированная студия, район Phước Hòa (Lam Sơn).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134094820.htm","2 дня назад",2,details={"amenities":"полная мебель"}),
L(63,"nha-trang","ph2","Квартира",8800000,45,"Меблированная квартира с балконом, район Phước Hòa (Lam Sơn).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134094699.htm","2 дня назад",2,details={"amenities":"полная мебель, балкон"}),
L(64,"nha-trang","vh","Квартира",20000000,88,"Просторная квартира класса люкс, район Vĩnh Hòa (север).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133490987.htm","2 дня назад",2,details={"amenities":"премиальная мебель"}),
L(65,"nha-trang","pl","Квартира",5000000,45,"Меблированная квартира, район Phước Long.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134079239.htm","3 дня назад",3,details={"amenities":"полная мебель"}),
L(66,"nha-trang","lt","Квартира",14000000,68,"Квартира в центре, район Lộc Thọ.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134078746.htm","3 дня назад",3),
L(67,"nha-trang","pl","Квартира",6000000,30,"Квартира-студия, район Phước Long.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133700375.htm","3 дня назад",3),
L(68,"nha-trang","vt2","Квартира",11500000,80,"Просторная квартира, район Xương Huân (старый город, ближе к Vạn Thạnh).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/132796382.htm","4 дня назад",4),
L(69,"nha-trang","ph","Квартира",18000000,72,"Просторная квартира, район Phước Hải.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134053515.htm","4 дня назад",4),
L(70,"nha-trang","ph","Квартира",7000000,40,"Квартира «cao cấp» (повышенной комфортности), район Phước Hải.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133988450.htm","4 дня назад",4),
L(71,"nha-trang","tl","Квартира",18000000,60,"Просторная меблированная квартира в центре, район Tân Lập.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134032727.htm","5 дней назад",5,details={"amenities":"полная мебель"}),
L(72,"nha-trang","pl","Квартира",15000000,75,"Квартира повышенной комфортности, район Phước Long.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133621191.htm","6 дней назад",6,details={"amenities":"премиальная мебель"}),
L(73,"nha-trang","ps","Квартира",9200000,75,"Квартира, район Phương Sơn (запад).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133608633.htm","1 неделю назад",7),
L(74,"nha-trang","vt2","Квартира",13500000,68,"Квартира, район Xương Huân (старый город, ближе к Vạn Thạnh).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133968835.htm","1 неделю назад",7),
L(75,"nha-trang","vp","Квартира",15000000,79,"Квартира повышенной комфортности, район Vĩnh Phước.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133995215.htm","1 неделю назад",7,details={"amenities":"премиальная мебель"}),
L(76,"nha-trang","vt2","Студия",5800000,27,"Меблированная студия, район Vạn Thạnh.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133994574.htm","1 неделю назад",7,details={"amenities":"полная мебель"}),
L(77,"nha-trang","ps","Квартира",11000000,64,"Меблированная квартира, район Vĩnh Trung (запад).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133993178.htm","1 неделю назад",7,details={"amenities":"полная мебель"}),
L(78,"nha-trang","vt","Квартира",8500000,65,"Меблированная квартира, район Vĩnh Trường (юг).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133992753.htm","1 неделю назад",7,details={"amenities":"полная мебель"}),
L(79,"nha-trang","vt2","Квартира",13000000,45,"Квартира, район Vạn Thạnh.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133990835.htm","1 неделю назад",7),
L(80,"nha-trang","vp","Квартира",7000000,40,"Меблированная квартира, район Vĩnh Phước.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133984854.htm","1 неделю назад",7,details={"amenities":"полная мебель"}),
L(81,"nha-trang","ps","Квартира",7500000,55,"Квартира, район Phương Sơn (запад).",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133609077.htm","1 неделю назад",7),
L(82,"nha-trang","vh","Комната",2500000,22,"Комната у моря, охраняемый район с соблюдением норм пожарной безопасности.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-pho-phan-phu-tien-phuong-vinh-hai-350/cho-gia-2-5-tr-gan-bien-an-ninh-am-bao-pccc-pr46180393","сегодня",0,source="batdongsan"),
L(83,"nha-trang","vh","Комната",3000000,45,"Комната на ул. Nguyễn Khuyến, приоритет студентам.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-khuyen-phuong-vinh-hai-350/cho-3tr-thang-uu-tien-sinh-vien-pr46162044","4 дня назад",4,source="batdongsan"),
L(84,"nha-trang","ph","Дом",18000000,60,"Дом целиком, 4 этажа, 5 спален, 5 санузлов.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-thich-quang-duc-phuong-phuoc-hai-350/cho-nguyen-can-4-tang-5-phong-ngu-5-ve-sinh-pr46136962","сегодня",0,source="batdongsan"),
L(85,"nha-trang","pl","Дом",10000000,142,"Дом 142 м² по акционной цене, район Vĩnh Phương (пригород, запад).","https://batdongsan.com.vn/cho-thue-nha-rieng-xa-vinh-phuong/cho-gia-uu-ai-tai-10-trieu-142m2-pr46178812","сегодня",0,source="batdongsan"),
L(86,"da-lat","lv","Комната",1600000,12,"Маленькая комната с антресолью, район Phường 9.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-yersin-phuong-9_2-391/cho-tai-9-da-lat-3x4-12m2-gia-1-6-trieu-thang-co-gac-lung-pr41472028","сегодня",0,source="batdongsan"),
L(87,"da-lat","xh","Студия",3800000,22,"Меблированная квартира-студия по хорошей цене, район Phường 2.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-van-troi-phuong-2_3-391/cho-can-ho-full-noi-that-gia-re-pr45648318","5 дней назад",5,source="batdongsan",details={"amenities":"полная мебель"}),
L(88,"da-lat","lv","Дом",7500000,70,"Дом 70 м², район Phường 8.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-huu-canh-phuong-8_2-391/cho-70m2-uong-8-a-lat-lam-ong-pr46181403","сегодня",0,source="batdongsan"),
L(89,"da-lat","cl","Дом",15000000,200,"Дом 200 м², 2 этажа, 4 спальни, 3 санузла, рядом рынок/школа/больница.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-kim-dong-phuong-6_3-391/cho-nguyen-can-200m-2-tang-ap-mai-4pn-3wc-gan-cho-truong-hoc-benh-vien-o-ngay-pr46140934","1 неделю назад",7,source="batdongsan"),
L(90,"da-nang","ns","Комната",2900000,18,"Комната, район Ngũ Hành Sơn (Khuê Mỹ).","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-ho-xuan-huong-phuong-khue-my-48/cho-tai-ngu-hanh-son-a-nang-gia-2-9tr-pr46168870","2 дня назад",2,source="batdongsan"),
L(91,"da-nang","hc","Комната",4200000,50,"Меблированная комната 50 м², район Hải Châu.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-thanh-thuy-phuong-hai-chau_1-46/cho-gia-re-uong-chau-dt-50m2-noi-that-ay-u-pr46165383","3 дня назад",3,source="batdongsan",details={"amenities":"полная мебель"}),
L(92,"da-nang","tk","Дом",14000000,90,"Дом с 3 спальнями, меблирован, район Thanh Khê (Xuân Hà).","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-do-phuong-xuan-ha-50/cho-kiet-uong-o-3-phong-ngu-u-noi-that-pr46175643","сегодня",0,source="batdongsan",details={"amenities":"3 спальни, полная мебель"}),
L(93,"da-lat","xh","Комната",2500000,30,"Комната с полной мебелью, старый район Phường 10.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/128500800.htm","1 неделю назад",7),
L(94,"da-lat","lv","Комната",4000000,60,"Комната, старый район Phường 8.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133928386.htm","2 недели назад",14),
L(95,"da-lat","cl","Комната",1700000,16,"Комната с полной мебелью, старый район Phường 6.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/132629339.htm","2 недели назад",14),
L(96,"da-lat","xh","Комната",1500000,10,"Комната, старый район Phường 10.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133816047.htm","2 недели назад",14),
L(97,"da-lat","xh","Комната",3000000,30,"Комната без мебели, старый район Phường 3.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133947980.htm","1 неделю назад",7),
L(98,"da-lat","cl","Комната",2000000,20,"Комната с полной мебелью, старый район Phường 6.",N+"/thue-phong-tro-thanh-pho-da-lat-lam-dong/133591871.htm","3 недели назад",21),
L(99,"da-lat","lv","Квартира",8000000,35,"Квартира с мебелью повышенной комфортности, старый район Phường 8.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134097670.htm","8 часов назад",0),
L(100,"da-lat","lb","Квартира",2500000,25,"Квартира с мебелью повышенной комфортности, старый район Phường 7.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/130268488.htm","8 часов назад",0),
L(101,"da-lat","lv","Квартира",19000000,100,"Квартира, старый район Phường 9.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133825946.htm","9 часов назад",0),
L(102,"da-lat","lv","Квартира",6000000,60,"Квартира с полной мебелью, старый район Phường 8.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134124632.htm","20 часов назад",0),
L(103,"da-lat","lv","Квартира",11000000,80,"Квартира с полной мебелью, старый район Phường 8.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134123781.htm","21 час назад",0),
L(104,"da-lat","lv","Квартира",10000000,60,"Квартира с полной мебелью, старый район Phường 9.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134115149.htm","вчера",1),
L(105,"da-lat","xh","Квартира",12000000,70,"Квартира, старый район Phường 10.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134112254.htm","вчера",1),
L(106,"da-lat","xh","Квартира",4400000,40,"Квартира, старый район Phường 2.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134095713.htm","2 дня назад",2),
L(107,"da-lat","lv","Квартира",10500000,50,"Квартира, старый район Phường 8.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134089862.htm","2 дня назад",2),
L(108,"da-lat","cl","Квартира",4300000,35,"Квартира, старый район Phường 6.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134056221.htm","2 дня назад",2),
L(109,"da-lat","lv","Квартира",11500000,80,"Квартира, старый район Phường 8.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134088790.htm","2 дня назад",2),
L(110,"da-lat","xh","Квартира",6000000,40,"Квартира, старый район Phường 3.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134084852.htm","3 дня назад",3),
L(111,"da-lat","xh","Квартира",6000000,40,"Квартира с полной мебелью, старый район Phường 3.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134083526.htm","3 дня назад",3),
L(112,"da-lat","xh","Квартира",6000000,60,"Квартира, старый район Phường 2.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133066675.htm","4 дня назад",4),
L(113,"da-lat","xh","Квартира",8000000,50,"Квартира, старый район Phường 1.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133548219.htm","4 дня назад",4),
L(114,"da-lat","cl","Квартира",15500000,90,"Квартира, старый район Phường 5.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134031165.htm","5 дней назад",5),
L(115,"da-lat","lv","Квартира",4500000,40,"Квартира с полной мебелью, старый район Phường 9.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134031142.htm","5 дней назад",5),
L(116,"da-lat","lb","Квартира",12000000,100,"Квартира, старый район Phường 7.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134031058.htm","5 дней назад",5),
L(117,"da-lat","lv","Квартира",9000000,40,"Квартира, старый район Phường 8.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134027271.htm","6 дней назад",6),
L(118,"da-lat","cl","Квартира",4300000,30,"Квартира, старый район Phường 6.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134014611.htm","6 дней назад",6),
L(119,"da-nang","hx","Комната",4500000,35,"Комната с полной мебелью, старый район Q. Cẩm Lệ.",N+"/thue-phong-tro-quan-cam-le-da-nang/134101044.htm","7 часов назад",0),
L(120,"da-nang","hx","Комната",2200000,25,"Комната без мебели, старый район Q. Cẩm Lệ.",N+"/thue-phong-tro-quan-cam-le-da-nang/134132537.htm","7 часов назад",0),
L(121,"da-nang","ah","Комната",6000000,35,"Комната, старый район Q. Sơn Trà.",N+"/thue-phong-tro-quan-son-tra-da-nang/134088159.htm","8 часов назад",0),
L(122,"da-nang","hcg","Комната",1900000,25,"Комната, старый район Q. Hải Châu.",N+"/thue-phong-tro-quan-hai-chau-da-nang/134105033.htm","8 часов назад",0),
L(123,"da-nang","ns","Комната",2200000,15,"Комната с полной мебелью, старый район Q. Ngũ Hành Sơn.",N+"/thue-phong-tro-quan-ngu-hanh-son-da-nang/134130311.htm","8 часов назад",0),
L(124,"da-nang","hcg","Комната",2200000,10,"Комната с мебелью повышенной комфортности, старый район Q. Hải Châu.",N+"/thue-phong-tro-quan-hai-chau-da-nang/133256155.htm","11 часов назад",0),
L(125,"da-nang","hx","Комната",4600000,None,"Комната без мебели, старый район Q. Cẩm Lệ.",N+"/thue-phong-tro-quan-cam-le-da-nang/134127031.htm","11 часов назад",0),
L(126,"da-nang","hx","Комната",5800000,None,"Комната с полной мебелью, старый район Q. Cẩm Lệ.",N+"/thue-phong-tro-quan-cam-le-da-nang/134127028.htm","11 часов назад",0),
L(127,"da-nang","hx","Комната",4500000,None,"Комната с полной мебелью, старый район Q. Cẩm Lệ.",N+"/thue-phong-tro-quan-cam-le-da-nang/134126939.htm","11 часов назад",0),
L(128,"da-nang","hk","Комната",3500000,None,"Комната с полной мебелью, старый район Q. Liên Chiểu.",N+"/thue-phong-tro-quan-lien-chieu-da-nang/134126926.htm","11 часов назад",0),
L(129,"da-nang","ns","Квартира",7000000,35,"Квартира с полной мебелью, старый район Q. Ngũ Hành Sơn.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/133917935.htm","актуально",0),
L(130,"da-nang","lc","Квартира",7500000,63,"Квартира, старый район Q. Liên Chiểu.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134140024.htm","2 часа назад",0),
L(131,"da-nang","hx","Квартира",5500000,35,"Квартира с полной мебелью, старый район Q. Cẩm Lệ.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134130026.htm","актуально",0),
L(132,"da-nang","hcg","Квартира",10900000,40,"Квартира с полной мебелью, старый район Q. Hải Châu.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134141495.htm","20 минут назад",0),
L(133,"da-nang","tk","Квартира",8500000,40,"Квартира с мебелью повышенной комфортности, старый район Q. Thanh Khê.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134140642.htm","1 час назад",0),
L(134,"da-nang","ah","Квартира",23000000,82,"Квартира, старый район Q. Sơn Trà.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/133439929.htm","1 час назад",0),
L(135,"da-nang","ns","Квартира",7500000,35,"Квартира с полной мебелью, старый район Q. Ngũ Hành Sơn.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/133740340.htm","1 час назад",0),
L(136,"da-nang","tk","Квартира",14500000,40,"Квартира с полной мебелью, старый район Q. Thanh Khê.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134140345.htm","1 час назад",0),
L(137,"da-nang","hc","Квартира",10500000,30,"Квартира с мебелью повышенной комфортности, старый район Q. Hải Châu.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/133822899.htm","2 часа назад",0),
L(138,"da-nang","ns","Квартира",5500000,35,"Квартира, старый район Q. Ngũ Hành Sơn.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134139843.htm","2 часа назад",0),
L(139,"da-nang","tk","Квартира",8500000,45,"Квартира с мебелью повышенной комфортности, старый район Q. Thanh Khê.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134139722.htm","2 часа назад",0),
L(140,"da-nang","ns","Квартира",5200000,35,"Квартира, старый район Q. Ngũ Hành Sơn.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134139659.htm","2 часа назад",0),
L(141,"da-nang","st","Квартира",26000000,80,"Квартира с мебелью повышенной комфортности, старый район Q. Sơn Trà.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134139649.htm","2 часа назад",0),
L(142,"da-nang","hx","Квартира",6000000,35,"Квартира с полной мебелью, старый район Q. Cẩm Lệ.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134139642.htm","2 часа назад",0),
L(143,"da-nang","hx","Квартира",5990000,40,"Квартира, старый район Q. Cẩm Lệ.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134139582.htm","2 часа назад",0),
L(144,"da-nang","ns","Квартира",8000000,35,"Квартира, старый район Q. Ngũ Hành Sơn.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134139574.htm","2 часа назад",0),
L(145,"da-nang","ah","Квартира",24500000,40,"Квартира, старый район Q. Sơn Trà.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134139511.htm","2 часа назад",0),
L(146,"da-nang","ah","Квартира",10000000,35,"Квартира с полной мебелью, старый район Q. Sơn Trà.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134139223.htm","2 часа назад",0),
L(147,"da-nang","st","Квартира",14000000,77,"Квартира с мебелью повышенной комфортности, старый район Q. Sơn Trà.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134139157.htm","2 часа назад",0),
L(148,"da-nang","ns","Квартира",6000000,32,"Квартира с полной мебелью, старый район Q. Ngũ Hành Sơn.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134048057.htm","3 часа назад",0),
L(149,"da-nang","tk","Квартира",8500000,35,"Квартира с полной мебелью, старый район Q. Thanh Khê.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134057584.htm","3 часа назад",0),
L(150,"da-nang","ah","Квартира",10000000,35,"Квартира с мебелью повышенной комфортности, старый район Q. Sơn Trà.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/132402709.htm","3 часа назад",0),
L(151,"da-nang","hk","Квартира",8000000,63,"Квартира.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134119344.htm","7 ч. назад",0),
L(152,"da-nang","ns","Квартира",20000000,55,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134138255.htm","7 ч. назад",0),
L(153,"da-nang","ns","Квартира",23000000,68,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134097539.htm","7 ч. назад",0),
L(154,"da-nang","hc","Квартира",7900000,35,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134057362.htm","7 ч. назад",0),
L(155,"da-nang","hcg","Квартира",18000000,100,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134070668.htm","7 ч. назад",0),
L(156,"da-nang","ah","Квартира",9000000,25,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134138086.htm","7 ч. назад",0),
L(157,"da-nang","hcg","Квартира",21300000,76,"Квартира.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134076670.htm","7 ч. назад",0),
L(158,"da-nang","ns","Квартира",20000000,55,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134137996.htm","7 ч. назад",0),
L(159,"da-nang","tk","Квартира",8000000,35,"Квартира.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134137205.htm","8 ч. назад",0),
L(160,"da-nang","hk","Квартира",14000000,40,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134136942.htm","8 ч. назад",0),
L(161,"da-nang","tk","Квартира",10990000,45,"Квартира.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134136720.htm","8 ч. назад",0),
L(162,"da-nang","ah","Квартира",22000000,50,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134121701.htm","8 ч. назад",0),
L(163,"da-nang","ns","Квартира",5900000,45,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134136208.htm","8 ч. назад",0),
L(164,"da-nang","hc","Квартира",8000000,60,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134136043.htm","9 ч. назад",0),
L(165,"da-nang","ns","Квартира",4300000,30,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/132620225.htm","9 ч. назад",0),
L(166,"da-nang","ns","Квартира",19000000,67,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134088292.htm","9 ч. назад",0),
L(167,"da-nang","ns","Квартира",20000000,50,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134117501.htm","9 ч. назад",0),
L(168,"da-nang","ah","Квартира",7500000,45,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134135473.htm","9 ч. назад",0),
L(169,"da-nang","ns","Квартира",5000000,20,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/132301418.htm","9 ч. назад",0),
L(170,"da-nang","ah","Квартира",23000000,65,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134134975.htm","9 ч. назад",0),
L(171,"da-nang","hcg","Квартира",29000000,76,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134134849.htm","9 ч. назад",0),
L(172,"da-nang","ns","Квартира",15000000,60,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134109816.htm","9 ч. назад",0),
L(173,"da-nang","ah","Квартира",40000000,77,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134125290.htm","9 ч. назад",0),
L(174,"da-nang","ns","Квартира",20000000,39,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134134823.htm","9 ч. назад",0),
L(175,"da-nang","st","Квартира",16000000,77,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134095925.htm","10 ч. назад",0),
L(176,"da-nang","ns","Квартира",11000000,66,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134134521.htm","10 ч. назад",0),
L(177,"da-nang","hk","Квартира",12000000,40,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134106564.htm","10 ч. назад",0),
L(178,"da-nang","hcg","Квартира",7000000,30,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/133898921.htm","10 ч. назад",0),
L(179,"da-nang","tk","Квартира",6500000,40,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134105898.htm","10 ч. назад",0),
L(180,"da-nang","hk","Квартира",17000000,250,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/133815366.htm","10 ч. назад",0),
L(181,"da-nang","ah","Квартира",15000000,30,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/133722198.htm","10 ч. назад",0),
L(182,"da-nang","ns","Квартира",23000000,67,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134088243.htm","10 ч. назад",0),
L(183,"da-nang","ns","Квартира",8500000,40,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/133939353.htm","10 ч. назад",0),
L(184,"da-nang","ah","Квартира",30000000,100,"Квартира.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134120517.htm","10 ч. назад",0),
L(185,"da-nang","hx","Квартира",5000000,30,"Квартира.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134133582.htm","11 ч. назад",0),
L(186,"da-nang","hcg","Квартира",9500000,40,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/133843222.htm","11 ч. назад",0),
L(187,"da-nang","ns","Квартира",9000000,70,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134112569.htm","11 ч. назад",0),
L(188,"da-nang","ns","Квартира",6500000,45,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134114615.htm","11 ч. назад",0),
L(189,"da-nang","st","Квартира",5000000,50,"Квартира.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134058591.htm","11 ч. назад",0),
L(190,"da-nang","ak","Квартира",5000000,30,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134085781.htm","11 ч. назад",0),
L(191,"da-nang","ns","Квартира",7900000,30,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/133208685.htm","11 ч. назад",0),
L(192,"da-nang","lc","Квартира",6200000,40,"Квартира.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134132386.htm","11 ч. назад",0),
L(193,"da-nang","ns","Квартира",13000000,80,"Квартира, без мебели.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/131979734.htm","11 ч. назад",0),
L(194,"da-nang","lc","Квартира",5200000,30,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134091846.htm","11 ч. назад",0),
L(195,"da-nang","ns","Квартира",25000000,50,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134118105.htm","12 ч. назад",0),
L(196,"da-nang","hx","Квартира",6000000,30,"Квартира.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134131992.htm","12 ч. назад",0),
L(197,"da-nang","st","Квартира",14000000,60,"Квартира.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/131727326.htm","12 ч. назад",0),
L(198,"da-nang","hc","Квартира",16000000,50,"Квартира.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134131963.htm","12 ч. назад",0),
L(199,"da-nang","hk","Квартира",5800000,30,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134089158.htm","12 ч. назад",0),
L(200,"da-nang","ns","Квартира",16000000,35,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134131849.htm","12 ч. назад",0),
L(201,"da-nang","hc","Квартира",15000000,94,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134131653.htm","12 ч. назад",0),
L(202,"da-nang","ah","Квартира",9000000,35,"Квартира.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/133841055.htm","12 ч. назад",0),
L(203,"da-nang","hx","Квартира",6000000,30,"Квартира.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134131115.htm","12 ч. назад",0),
L(204,"da-nang","ns","Квартира",8000000,50,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/133187884.htm","12 ч. назад",0),
L(205,"da-nang","ns","Квартира",23000000,67,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134088120.htm","12 ч. назад",0),
L(206,"da-nang","tk","Квартира",6000000,30,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134130711.htm","12 ч. назад",0),
L(207,"da-nang","st","Квартира",13000000,40,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/133642068.htm","12 ч. назад",0),
L(208,"da-nang","ns","Квартира",13000000,70,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134130617.htm","12 ч. назад",0),
L(209,"da-nang","lc","Квартира",5500000,70,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134130472.htm","12 ч. назад",0),
L(210,"da-nang","cl2","Квартира",6000000,45,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134130463.htm","12 ч. назад",0),
L(211,"da-nang","ah","Квартира",6900000,30,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134058672.htm","13 ч. назад",0),
L(212,"da-nang","ah","Квартира",10000000,40,"Квартира.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134120446.htm","13 ч. назад",0),
L(213,"da-nang","ns","Квартира",10000000,40,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134130024.htm","13 ч. назад",0),
L(214,"da-nang","ns","Квартира",17000000,60,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134112382.htm","13 ч. назад",0),
L(215,"da-nang","hc","Квартира",22000000,109,"Квартира.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/132108706.htm","13 ч. назад",0),
L(216,"da-nang","tk","Квартира",9500000,35,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134129707.htm","13 ч. назад",0),
L(217,"da-nang","hk","Квартира",4990000,30,"Квартира.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134129457.htm","13 ч. назад",0),
L(218,"da-nang","ns","Квартира",8000000,40,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134129163.htm","13 ч. назад",0),
L(219,"da-nang","hk","Квартира",7000000,30,"Квартира.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134129030.htm","13 ч. назад",0),
L(220,"da-nang","hc","Квартира",15500000,30,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134128790.htm","13 ч. назад",0),
L(221,"da-nang","hc","Квартира",9500000,40,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134128414.htm","14 ч. назад",0),
L(222,"da-nang","ah","Квартира",17000000,75,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134097892.htm","14 ч. назад",0),
L(223,"da-nang","hc","Квартира",6000000,25,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134128286.htm","14 ч. назад",0),
L(224,"da-nang","hx","Квартира",6000000,45,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/134030449.htm","14 ч. назад",0),
L(225,"da-nang","ah","Квартира",22000000,69,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134090480.htm","14 ч. назад",0),
L(226,"da-nang","ns","Квартира",25000000,60,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134120637.htm","14 ч. назад",0),
L(227,"da-nang","hx","Квартира",10500000,45,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-cam-le-da-nang/133740391.htm","14 ч. назад",0),
L(228,"da-nang","ah","Квартира",6500000,40,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134124540.htm","14 ч. назад",0),
L(229,"da-nang","tk","Квартира",16000000,100,"Квартира.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134127969.htm","14 ч. назад",0),
L(230,"da-nang","ns","Квартира",15000000,45,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134113854.htm","14 ч. назад",0),
L(231,"da-nang","ns","Квартира",23000000,60,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134123233.htm","14 ч. назад",0),
L(232,"da-nang","hcg","Квартира",19000000,67,"Квартира.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/133682874.htm","14 ч. назад",0),
L(233,"da-nang","ns","Квартира",45000000,98,"Квартира.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/133681430.htm","14 ч. назад",0),
L(234,"da-nang","ah","Квартира",40000000,77,"Квартира.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/133674120.htm","14 ч. назад",0),
L(235,"da-nang","ns","Квартира",27000000,50,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134098290.htm","14 ч. назад",0),
L(236,"da-nang","tk","Квартира",7500000,25,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/133748138.htm","14 ч. назад",0),
L(237,"da-nang","lc","Квартира",8500000,63,"Квартира.",N+"/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134111179.htm","15 ч. назад",0),
L(238,"da-nang","hcg","Квартира",4500000,20,"Квартира.",N+"/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134099942.htm","15 ч. назад",0),
L(239,"da-nang","st","Квартира",15000000,52,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-quan-son-tra-da-nang/134098238.htm","15 ч. назад",0),
L(240,"nha-trang","ps","Квартира",9000000,68,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/132198573.htm","1 нед. назад",7),
L(241,"nha-trang","ph","Квартира",15000000,79,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133921326.htm","1 нед. назад",7),
L(242,"nha-trang","vh","Квартира",8900000,48,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133831778.htm","1 нед. назад",7),
L(243,"nha-trang","vt2","Квартира",3800000,20,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133067561.htm","1 нед. назад",7),
L(244,"nha-trang","vt2","Квартира",12000000,68,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133942478.htm","1 нед. назад",7),
L(245,"nha-trang","nh","Квартира",14000000,57,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133888000.htm","2 нед. назад",14),
L(246,"nha-trang","vh","Квартира",9000000,55,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133917382.htm","2 нед. назад",14),
L(247,"nha-trang","ps","Квартира",15000000,60,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133910603.htm","2 нед. назад",14),
L(248,"nha-trang","pl","Квартира",15000000,90,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133908371.htm","2 нед. назад",14),
L(249,"nha-trang","ph","Квартира",17000000,87,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133902981.htm","2 нед. назад",14),
L(250,"nha-trang","ps","Квартира",16000000,75,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133889871.htm","2 нед. назад",14),
L(251,"nha-trang","tl","Квартира",17000000,80,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133887024.htm","2 нед. назад",14),
L(252,"nha-trang","vt","Квартира",11000000,65,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133870522.htm","2 нед. назад",14),
L(253,"nha-trang","lt","Квартира",15000000,52,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133823017.htm","2 нед. назад",14),
L(254,"nha-trang","vt2","Квартира",10000000,100,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133864905.htm","2 нед. назад",14),
L(255,"nha-trang","lt","Квартира",10000000,67,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133860451.htm","2 нед. назад",14),
L(256,"da-lat","lv","Квартира",6000000,65,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134003728.htm","1 нед. назад",7),
L(257,"da-lat","cl","Квартира",11000000,40,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133981725.htm","1 нед. назад",7),
L(258,"da-lat","xh","Квартира",8000000,75,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133907815.htm","1 нед. назад",7),
L(259,"da-lat","lv","Квартира",6000000,40,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133966026.htm","1 нед. назад",7),
L(260,"da-lat","cl","Квартира",15500000,80,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133908781.htm","1 нед. назад",7),
L(261,"da-lat","lv","Квартира",6000000,40,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133964384.htm","1 нед. назад",7),
L(262,"da-lat","cl","Квартира",3300000,20,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133952656.htm","1 нед. назад",7),
L(263,"da-lat","xh","Квартира",6500000,35,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133040505.htm","2 нед. назад",14),
L(264,"da-lat","xh","Квартира",6500000,30,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133935033.htm","2 нед. назад",14),
L(265,"da-lat","xh","Квартира",9000000,40,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133935001.htm","2 нед. назад",14),
L(266,"da-lat","cl","Квартира",15500000,80,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133919654.htm","2 нед. назад",14),
L(267,"da-lat","cl","Квартира",10000000,60,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133917679.htm","2 нед. назад",14),
L(268,"da-lat","cl","Квартира",9000000,60,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133916990.htm","2 нед. назад",14),
L(269,"da-lat","cl","Квартира",10000000,60,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133916743.htm","2 нед. назад",14),
L(270,"da-lat","lb","Квартира",12000000,55,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133916228.htm","2 нед. назад",14),
L(271,"da-lat","lv","Квартира",19000000,100,"Квартира, с мебелью повышенной комфортности.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133878080.htm","2 нед. назад",14),
L(272,"da-lat","cl","Квартира",9000000,60,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133909277.htm","2 нед. назад",14),
L(273,"da-lat","lv","Квартира",4500000,50,"Квартира, без мебели.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133908953.htm","2 нед. назад",14),
L(274,"da-lat","xh","Квартира",6000000,50,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133888639.htm","2 нед. назад",14),
L(275,"da-lat","cl","Квартира",3300000,30,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133884334.htm","2 нед. назад",14),
L(276,"da-lat","cl","Квартира",6000000,72,"Квартира, с полной мебелью.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133868709.htm","2 нед. назад",14),
L(277,"da-lat","xh","Квартира",9000000,50,"Квартира.",N+"/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133861249.htm","2 нед. назад",14),
L(278,"da-nang","hcg","Комната",6000000,20,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-hai-chau-da-nang/134144787.htm","актуально",0),
L(279,"da-nang","hcg","Комната",None,15,"Комната, без мебели.",N+"/thue-phong-tro-quan-hai-chau-da-nang/134083703.htm","18 ч. назад",0,
  details={"notice":"⚠ на сайте указана цена-приманка 100 000 ₫/мес — продавец явно просит писать в личные сообщения за реальной ценой, реальная цена неизвестна."}),
L(280,"da-nang","hx","Комната",4600000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-cam-le-da-nang/134126366.htm","19 ч. назад",0),
L(281,"da-nang","ak","Комната",4700000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-cam-le-da-nang/134126363.htm","19 ч. назад",0),
L(282,"da-nang","hx","Комната",3500000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-cam-le-da-nang/134126358.htm","19 ч. назад",0),
L(283,"da-nang","hk","Комната",3000000,None,"Комната, без мебели.",N+"/thue-phong-tro-quan-lien-chieu-da-nang/134126356.htm","19 ч. назад",0),
L(284,"da-nang","lc","Комната",3500000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-lien-chieu-da-nang/134126355.htm","19 ч. назад",0),
L(285,"da-nang","hk","Комната",3600000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-lien-chieu-da-nang/134126352.htm","19 ч. назад",0),
L(286,"da-nang","hx","Комната",4700000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-cam-le-da-nang/134126222.htm","20 ч. назад",0),
L(287,"da-nang","ns","Комната",4500000,None,"Комната, без мебели.",N+"/thue-phong-tro-quan-ngu-hanh-son-da-nang/134126220.htm","20 ч. назад",0),
L(288,"da-nang","ns","Комната",4500000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-ngu-hanh-son-da-nang/134126215.htm","20 ч. назад",0),
L(289,"da-nang","hk","Комната",4000000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-lien-chieu-da-nang/134126214.htm","20 ч. назад",0),
L(290,"da-nang","hk","Комната",4500000,None,"Комната, без мебели.",N+"/thue-phong-tro-quan-lien-chieu-da-nang/134126208.htm","20 ч. назад",0),
L(291,"da-nang","hcg","Комната",3600000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-hai-chau-da-nang/134125551.htm","23 ч. назад",0),
L(292,"da-nang","hk","Комната",5000000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-lien-chieu-da-nang/134125545.htm","23 ч. назад",0),
L(293,"da-nang","ns","Комната",3800000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-ngu-hanh-son-da-nang/134125544.htm","23 ч. назад",0),
L(294,"da-nang","lc","Комната",3900000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-lien-chieu-da-nang/134125542.htm","23 ч. назад",0),
L(295,"da-nang","ns","Комната",4500000,None,"Комната, с полной мебелью.",N+"/thue-phong-tro-quan-ngu-hanh-son-da-nang/134125536.htm","23 ч. назад",0),
L(296,"nha-trang","vp","Квартира",6000000,52,"Квартира с видом, ул. 2/4, этаж 2, комната D2.2, район Vĩnh Phước.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-2-4-phuong-vinh-phuoc-350/cho-2-4-gia-4-trieu-52-m2-2-pn-view-dep-pr41413787","актуально",0,source="batdongsan",details={"amenities":"кухня видна на фото (гарнитур, мойка), 2 спальни, 1 санузел","notice":"брокер Lê Tài, 11 лет на площадке, 101 активное объявление"}),
L(297,"nha-trang","ps","Квартира",6000000,51,"CT6 Vĩnh Điềm Trung, базовая (не полная) мебель, район X. Vĩnh Hiệp.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-xa-vinh-hiep-1-khu-do-thi-vinh-diem-trung/cho-ct6-iem-tay-nha-trang-51m2-2pn-6tr-thang-noi-that-co-ban-pr46183236","актуально",0,source="batdongsan",details={"amenities":"2 спальни, 2 санузла","notice":"меблировка базовая (nội thất cơ bản), не полная — уточняйте состав"}),
L(298,"nha-trang","pl","Квартира",7000000,67,"Chung cư XH1 VCN Phước Long.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-28-phuong-phuoc-long-khu-do-thi-vcn-phuoc-long-2/cho-xh1-nha-trang-7-trieu-thang-pr46183238","актуально",0,source="batdongsan",details={"amenities":"2 спальни, 1 санузел","notice":"комплекс XH1 VCN Phước Long"}),
L(299,"nha-trang","tl","Квартира",6000000,None,"Căn hộ 2 phòng ngủ trung tâm Nha Trang — Nguyễn Thiện Thuật, тайng 6.","https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u","26 июня",30,source="facebook",details={"amenities":"2 спальни, 1 санузел, гостиная с ТВ, обеденный стол","notice":"автор Dương Yến. Прямой ссылки на пост нет — ссылка открывает поиск «6 triệu» в группе, пост среди первых результатов"}),
L(300,"nha-trang","vh","Квартира",6000000,None,"Chung cư Hoàng Quân — căn trống (пустая квартира без мебели).","https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u","16 часов назад",0,source="facebook",details={"amenities":"2 спальни, 2 санузла","policy":"без мебели и техники","notice":"автор Bích Lê, заселение 20 сентября. Ссылка открывает поиск «6 triệu» в группе"}),
L(301,"nha-trang","pl","Квартира",6500000,None,"Căn hộ 1PN khu vực Phước Long.","https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u","актуально",0,source="facebook",details={"amenities":"1 спальня, кухня и кондиционер видны на фото","notice":"автор Hồng Liên, контакт +84 819 070 270 (WhatsApp/Zalo). Ссылка открывает поиск «6 triệu» в группе"}),
L(302,"nha-trang","vp","Квартира",6000000,None,"Căn hộ 1 phòng ngủ — Lê Văn Huân, Phía Bắc Nha Trang.","https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u","актуально",0,source="facebook",details={"amenities":"1 спальня","notice":"автор Nguyễn Thị Mỹ Hiệp. Ссылка открывает поиск «6 triệu» в группе"}),
L(303,"nha-trang","ps","Квартира",6500000,None,"Chung cư CT5 Vĩnh Điềm Trung, полная мебель по фото.","https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u","актуально",0,source="facebook",details={"amenities":"гостиная с диваном, обеденная зона, кухонный уголок","notice":"автор Kim Qui, свободна с 22 июня. Ссылка открывает поиск «6 triệu» в группе"}),
L(304,"nha-trang","lt","Квартира",6000000,None,"Căn hộ new — полностью новая мебель и техника, современный ремонт.","https://www.facebook.com/groups/593714207638751/search/?q=6%20tri%E1%BB%87u","актуально",0,source="facebook",details={"amenities":"кухня со встроенной техникой (варочная панель, духовка) видна на фото","notice":"автор Thuý Quỳnh. Ссылка открывает поиск «6 triệu» в группе"}),
L(305,"da-nang","ns","Квартира",24000000,None,"Пентхаус 2 спальни, ул. Nguyễn Thiện Kế — отдельный просторный двор, зона кафе/барбекю.","https://www.facebook.com/groups/253329090046313/posts/1441019157943961/","только что",0,source="facebook",details={"notice":"автор Trần Tuấn, контакт +84 325 365 363"}),
L(306,"da-nang","st","Студия",8000000,None,"Меблированная студия на ул. Phạm Vấn, район Sơn Trà, максимум 2 человека, стирка на крыше.","https://www.facebook.com/groups/253329090046313/posts/1441023687943508/","недавно",0,source="facebook",details={"electricity":"4 000 ₫/кВт·ч","water":"150 000 ₫/чел. (вкл. сервис)","deposit":"1 месяц","contract":"6 месяцев","policy":"принимают иностранцев","notice":"контакт/Zalo 0935 126 743"}),
L(307,"da-nang","st","Квартира",13000000,None,"2 спальни, 2 балкона, ул. Thế Lữ, район Sơn Trà, своя стиральная машина, лифт.","https://www.facebook.com/groups/253329090046313/","только что",0,source="facebook",details={"electricity":"4 000 ₫/кВт·ч","water":"120 000 ₫/чел.","contract":"6 месяцев","policy":"принимают иностранцев и небольших животных","notice":"автор Bắc House. Прямой ссылки на пост нет — открывает группу"}),
L(308,"da-nang","st","Студия",None,None,"Студия P302 со своей кухней и окном, ул. Vũ Tông Phan, район Sơn Trà, общая стиральная машина.","https://www.facebook.com/groups/canhochothuedanangtot/posts/2180745062553153/","только что",0,source="facebook",details={"electricity":"4 500 ₫/кВт·ч","water":"150 000 ₫ (вкл. сервис)","notice":"цена только по запросу в Zalo/WhatsApp"}),
L(309,"da-nang","tk","Студия",None,None,"Студия №302 на ул. Trần Cao Vân, свободна и готова к заселению сейчас.","https://www.facebook.com/groups/canhochothuedanangtot/posts/2180744729219853/","1 час назад",0,source="facebook",details={"notice":"цена не указана, контакт через Zalo/WhatsApp"}),
L(310,"da-nang","ns","Квартира",8800000,38,"1-спальная квартира на ул. Phan Tứ, район Ngũ Hành Sơn, полностью меблирована.","https://www.facebook.com/groups/canhochothuedanangtot/posts/2180744892553170/","1 час назад",0,source="facebook",details={"policy":"принимают иностранцев","notice":"контакт только через Messenger"}),
L(311,"nha-trang","tl","Студия",3200000,15,"Студия на ул. Nguyễn Thiện Thuật, кухня и прачечная на 4 этаже.","https://www.facebook.com/groups/749128438763331/posts/2981750618834424/","недавно",0,source="facebook",details={"deposit":"1 месяц","electricity":"4 500 ₫/кВт·ч","water":"120 000 ₫/чел.","notice":"общий сервис-сбор 200 000 ₫/чел., Zalo 0938 418 101"}),
L(312,"nha-trang","tl","Комната",9000000,None,"Комната №501 (5 этаж), ул. 35/69 Nguyễn Thiện Thuật.","https://www.facebook.com/groups/749128438763331/posts/2955021024840717/","недавно",0,source="facebook",details={"electricity":"4 500 ₫/кВт·ч","water":"150 000 ₫/чел.","notice":"wifi+мусор+управление 100 000 ₫/чел., разрешены животные, без электровелосипедов, свободна с 01.08, тел. 0989 939 192"}),
L(313,"nha-trang","ph","Квартира",12500000,None,"1-спальная квартира с балконом, район Hà Quang 2 — Phước Hải.","https://www.facebook.com/groups/749128438763331/posts/2982464848763001/","недавно",0,source="facebook",details={"electricity":"4 500 ₫/кВт·ч","water":"200 000 ₫/чел.","notice":"управление+мусор+wifi 250 000 ₫/чел., депозит 1 мес., Zalo 0905 087 168"}),
L(314,"nha-trang","vp","Квартира",7500000,35,"1-спальная квартира в переулке Đoàn Trần Nghiệp, север города, балкон/световой колодец, новый ремонт.","https://www.facebook.com/groups/167625939644211/posts/1003639566042840/","недавно",0,source="facebook"),
L(315,"nha-trang","vt","Квартира",9000000,64,"2-спальная квартира у рынка Bình Tân (ул. Tô Hiệu), 5 минут до моря, меблирована.","https://www.facebook.com/groups/167625939644211/posts/1000756796331117/","недавно",0,source="facebook",details={"deposit":"2 месяца (оплата за 1)","notice":"Zalo/WhatsApp 0905 285 896"}),
L(316,"nha-trang","ps","Квартира",4200000,None,"Дуплекс в районе Gò Găng, Vĩnh Điềm Trung.","https://www.facebook.com/groups/167625939644211/posts/1004973992576064/","недавно",0,source="facebook",details={"deposit":"1 месяц","electricity":"4 000 ₫/кВт·ч","water":"100 000 ₫/чел."}),
L(317,"nha-trang","ph","Дом",18000000,None,"Дом целиком, 4 этажа, 5 спален со своими санузлами, район Phước Hải (ул. Thích Quảng Đức).","https://www.facebook.com/groups/chothuenhanguyencannhatrang/posts/4622871407963854/","недавно",0,source="facebook",details={"deposit":"2 месяца + 1 оплата","notice":"площадка для сушки белья, заселение с 1 сентября, тел. 0394 257 517"}),
L(318,"nha-trang","vt","Дом",35000000,300,"Новый дом 3 спальни в КДТ Mỹ Gia (район Vĩnh Thái), лифт, терраса, охраняемый район.","https://www.facebook.com/groups/chothuenhanguyencannhatrang/posts/4630872880497040/","недавно",0,source="facebook",details={"deposit":"2 месяца (оплата за 2)","contract":"1 год","managementFee":"770 000 ₫/мес","notice":"Zalo 0976 864 740"}),
L(319,"nha-trang","ps","Дом",4000000,None,"Одноэтажный дом, 2 спальни, район Chợ Ga (ул. Vĩnh Thạnh), долгосрочный контракт.","https://www.facebook.com/groups/chothuenhanguyencannhatrang/posts/4632286153689046/","недавно",0,source="facebook",details={"notice":"тел. 0935 709 788"}),
L(320,"nha-trang","pl","Квартира",10000000,65,"Угловая 2-спальная квартира в КДТ Phước Long (CT4 Hud, ул. 28), балкон, качественная мебель.","https://www.facebook.com/groups/chothuecanhonhatrangkhanhhoa/posts/27944490621827590/","недавно",0,source="facebook",details={"deposit":"2 месяца (оплата за 2)","notice":"тел. 0989 819 892"}),
L(321,"nha-trang","ps","Квартира",8500000,65,"2-спальная квартира в Vĩnh Điềm Trung (CT6), 3 кондиционера, рядом супермаркет Go.","https://www.facebook.com/groups/chothuecanhonhatrangkhanhhoa/posts/27965768696366449/","недавно",0,source="facebook",details={"amenities":"3 кондиционера","deposit":"2 месяца (оплата за 2)","contract":"1 год","notice":"тел. 0773 701 937"}),
L(322,"nha-trang","lt","Квартира",14000000,None,"2-спальная квартира в ЖК Mường Thanh, 04 Trần Phú, вид на реку и башню Понагар.","https://www.facebook.com/groups/chothuecanhonhatrangkhanhhoa/posts/27910007241942595/","недавно",0,source="facebook",details={"managementFee":"700 000 ₫/мес","notice":"паркинг мотоцикла 100 000 ₫/мес, wifi 250 000 ₫/мес"}),
L(323,"da-nang","ns","Дом",18000000,100,"Дом целиком, 3 этажа, 4 спальни, район Hói Kiểng (рядом ул. Minh Mạng), полная мебель.","https://www.facebook.com/groups/599988861199745/posts/1857447832120502/","недавно",0,source="facebook",details={"amenities":"4 кондиционера, холодильник, стиральная машина","contract":"1-2 года","notice":"тел. 0905 999 196"}),
L(324,"da-nang","ns","Квартира",7500000,None,"Новая квартира рядом с Университетом экономики Дананга, район Ngũ Hành Sơn, паркинг в цоколе.","https://www.facebook.com/groups/599988861199745/posts/1856747908857161/","недавно",0,source="facebook",details={"notice":"цена 7-8 млн ₫ в зависимости от планировки, тел. 0983 985 800 / 0983 136 134"}),
L(325,"da-nang","hcg","Квартира",6500000,30,"1-спальная квартира, район Hòa Cường (Hải Châu), лифт, бесплатная стирка.","https://www.facebook.com/groups/198876884532146/posts/1819268872492931/","недавно",0,source="facebook",details={"electricity":"4 000 ₫/кВт·ч","water":"100 000 ₫/чел.","amenities":"бесплатная стирка","notice":"площадь 27-33 м² в зависимости от планировки, тел. 0979 820 348"}),
L(326,"da-nang","hc","Студия",6500000,None,"Студия в центре на ул. Đống Đa, рядом рынок Cồn и университет Duy Tân.","https://www.facebook.com/groups/198876884532146/posts/1813916053028213/","недавно",0,source="facebook",details={"amenities":"своя стиральная машина","notice":"охрана 24/7, тел. 0846 034 456"}),
L(327,"da-lat","xh","Квартира",4200000,None,"1-спальная квартира на ул. Huyền Trân Công Chúa, балкон с видом на сосновый лес.","https://www.facebook.com/groups/356237492011374/posts/1855996578702117/","недавно",0,source="facebook",details={"amenities":"бесплатный wifi, солнечный водонагреватель","electricity":"4 000 ₫/кВт·ч","water":"70 000 ₫/чел.","deposit":"1 месяц","notice":"без посредников, тел. 098 357 1317"}),
L(328,"da-lat","xh","Квартира",7000000,None,"2-спальная квартира (3 санузла) на ул. Trần Phú, 1 этаж, 700 м от админцентра.","https://www.facebook.com/groups/356237492011374/posts/1850361402598968/","недавно",0,source="facebook",details={"deposit":"1 месяц","contract":"1 год","notice":"Zalo 0363 000 532"}),
L(329,"da-lat","xh","Квартира",9000000,None,"1-спальная квартира премиум-класса на ул. Lương Thế Vinh, рядом отель Dalat Palace, спальня + антресоль.","https://www.facebook.com/groups/356237492011374/posts/1851224225846019/","недавно",0,source="facebook",details={"amenities":"полная мебель","electricity":"2 500 ₫/кВт·ч","water":"24 000 ₫/чел.","deposit":"10 млн ₫","notice":"тел. 0814 467 907"}),
L(330,"da-lat","lv","Дом",6000000,140,"Дом целиком, 2 спальни, ул. Mê Linh, район Lâm Viên, солнечный водонагреватель.","https://www.facebook.com/nguyen.hieu.966682/posts/pfbid0oB73YvEAgycraFi51H4fHGrzZHvyJ6Z6k3sQkQSev56pEvPkBa7XP8ENXADXFERCl","недавно",0,source="facebook",details={"deposit":"1 месяц (торг уместен)","notice":"заселение с 15 августа, автор Nguyễn Hiếu, тел. 0854 526 727"}),
L(331,"da-lat","xh","Дом",5000000,180,"Дом целиком, 3 спальни, ул. Tô Hiến Thành, без мебели.","https://www.facebook.com/nguyen.hieu.966682/posts/pfbid02sW4yCfMCVMPvE3cD2HA4MLGmvysLoqTWHdBTuCC82N5WrLYbsQwSs5G2P8vUU8TRl","недавно",0,source="facebook",details={"policy":"без мебели","deposit":"1 месяц","notice":"переулок для мотоциклов в 50 м от дороги, автор Nguyễn Hiếu, тел. 0854 526 727"}),
L(332,"da-lat","cl","Квартира",8000000,None,"2-спальная квартира, ул. Ô Tô Thi Sách, район Phường 6, лифт, балкон, большие окна.","https://www.facebook.com/groups/975470559939040/posts/2324368275049255/","недавно",0,source="facebook",details={"amenities":"полная мебель, вода включена, wifi бесплатно","deposit":"1 месяц","contract":"от 1 года","notice":"тел. 07745 179 86"}),
L(333,"nha-trang","ps","Дом",25000000,270,
  "Новая вилла, 3 спальни/4 санузла, район Mỹ Gia (запад), 9 минут до моря.",
  "https://t.me/s/Viet_life_niachang","сегодня",0,source="telegram",
  details={"contract":"от 1 года","notice":"канал Viet_life_niachang, контакт @Viet_Life_rent_Vietnam / @KlimGorbunov1"}),

L(334,"nha-trang","vh","Студия",16000000,40,
  "Студия в новом комплексе Vega City, 1-я линия, север города, полная мебель.",
  "https://t.me/s/Viet_life_niachang","сегодня",0,source="telegram",
  details={"contract":"3-6 месяцев","notice":"канал Viet_life_niachang, менеджер Жанна @manager_viet_life"}),

L(335,"nha-trang","pl","Квартира",13000000,None,
  "Угловая 2-спальная квартира, комплекс HUD CCU01, район Phước Long, новая мебель и техника.",
  "https://t.me/s/Viet_life_niachang","сегодня",0,source="telegram",
  details={"deposit":"2 месяца","notice":"канал Viet_life_niachang, менеджер Жанна @manager_viet_life"}),

L(336,"nha-trang","lt","Квартира",21000000,None,
  "2-спальная квартира в ЖК Mường Thanh, центр (1-я линия), бассейн/зал/спа в комплексе.",
  "https://t.me/s/Viet_life_niachang","сегодня",0,source="telegram",
  details={"contract":"от 6 месяцев","amenities":"бассейн, спортзал, спа в комплексе","notice":"канал Viet_life_niachang, менеджер Жанна @manager_viet_life"}),

L(337,"nha-trang","vh","Квартира",21800000,70,
  "2-спальная квартира в ЖК Oceanus, север, панорамный вид на море, 7 этаж.",
  "https://t.me/s/Arenda_Nyachang_Zhilye","сегодня",0,source="telegram",
  details={"deposit":"1 месяц","managementFee":"≈25$/мес + интернет ≈11$/мес","notice":"цена в оригинале 865$/мес (≈21,8 млн ₫ по курсу ~25 200 ₫/$). Контакт @NhaTrang_arenda_Pavel_Mihail, WhatsApp/Zalo +84 813 101 501"}),

L(338,"nha-trang","vh","Квартира",37170000,163,
  "3-спальная квартира в ЖК Oceanus, север, панорамный вид, самая просторная в комплексе.",
  "https://t.me/s/Arenda_Nyachang_Zhilye","сегодня",0,source="telegram",
  details={"contract":"от 3 месяцев","notice":"цена в оригинале 1475$/мес (≈37,2 млн ₫ по курсу ~25 200 ₫/$). Контакт @NhaTrang_arenda_Pavel_Mihail"}),

L(339,"nha-trang","lt","Квартира",18770000,70,
  "2-спальная квартира в ЖК HUD Building, центр, панорамный вид на город.",
  "https://t.me/s/Arenda_Nyachang_Zhilye","сегодня",0,source="telegram",
  details={"notice":"цена в оригинале 745$/мес (≈18,8 млн ₫ по курсу ~25 200 ₫/$). Туристический центр. Контакт @NhaTrang_arenda_Pavel_Mihail"}),

L(340,"nha-trang","vh","Квартира",13860000,70,
  "2-спальная квартира в ЖК Oceanus, север, вид на город, 23 этаж.",
  "https://t.me/s/Arenda_Nyachang_Zhilye","сегодня",0,source="telegram",
  details={"contract":"от 1 месяца","notice":"цена в оригинале 550$/мес (≈13,9 млн ₫ по курсу ~25 200 ₫/$). Контакт @NhaTrang_arenda_Pavel_Mihail"}),

L(341,"nha-trang","vh","Квартира",21800000,88,
  "3-спальная квартира (2 санузла) в ЖК Oceanus, новый корпус, север, частичный вид на горы и город.",
  "https://t.me/s/Arenda_Nyachang_Zhilye","сегодня",0,source="telegram",
  details={"notice":"цена в оригинале 865$/мес (≈21,8 млн ₫ по курсу ~25 200 ₫/$). Контакт @NhaTrang_arenda_Pavel_Mihail"}),

L(342,"nha-trang","vh","Квартира",18770000,75,
  "2-спальная квартира в ЖК Oceanus, новый корпус, север, частичный вид на горы и город.",
  "https://t.me/s/Arenda_Nyachang_Zhilye","сегодня",0,source="telegram",
  details={"notice":"цена в оригинале 745$/мес (≈18,8 млн ₫ по курсу ~25 200 ₫/$). Контакт @NhaTrang_arenda_Pavel_Mihail"}),

L(343,"nha-trang","vh","Квартира",13360000,70,
  "2-спальная квартира в ЖК Oceanus, север, частичный вид на море, 100 м до пляжа.",
  "https://t.me/s/Arenda_Nyachang_Zhilye","сегодня",0,source="telegram",
  details={"contract":"от 2 месяцев","notice":"цена в оригинале 530$/мес (≈13,4 млн ₫ по курсу ~25 200 ₫/$). Контакт @NhaTrang_arenda_Pavel_Mihail"}),

L(344,"nha-trang","vh","Квартира",13500000,None,
  "2-спальная квартира в ЖК Oceanus, север.",
  "https://t.me/arenda_nhatrang/24353","6 августа",9,source="telegram",
  details={"deposit":"1 месяц + разовая комиссия 1,25 млн ₫","contract":"от 1 месяца","notice":"агент Алина @al_glotova"}),

L(345,"nha-trang","vh","Квартира",24000000,None,
  "2-спальная квартира в ЖК Oceanus, север, более просторный/дорогой вариант.",
  "https://t.me/arenda_nhatrang/24363","6 августа",9,source="telegram",
  details={"deposit":"1 месяц + разовая комиссия 1,25 млн ₫","contract":"от 2 месяцев","notice":"агент Алина @al_glotova"}),

L(346,"nha-trang","lt","Квартира",15000000,None,
  "Квартира в ЖК Maple, центр города.",
  "https://t.me/arenda_nhatrang/24371","13 августа",2,source="telegram",
  details={"deposit":"1 месяц + разовая комиссия 1,25 млн ₫","contract":"от 1 месяца","notice":"агент Алина @al_glotova"}),

L(347,"nha-trang","lt","Студия",15000000,None,
  "Студия в ЖК Tuy Blue, центр, фитнес-зал, бассейн, сауна в комплексе.",
  "https://t.me/arenda_nhatrang/24381","13 августа",2,source="telegram",
  details={"amenities":"фитнес-зал, бассейн, сауна в комплексе","deposit":"1 месяц + разовая комиссия 1,25 млн ₫","contract":"от 1 месяца","notice":"агент Алина @al_glotova"}),

L(348,"nha-trang","lt","Квартира",21500000,None,
  "2-спальная квартира в ЖК Mường Thanh у реки.",
  "https://t.me/arenda_nhatrang/24391","13 августа",2,source="telegram",
  details={"deposit":"1 месяц + разовая комиссия 1,25 млн ₫","contract":"от 3 месяцев","notice":"агент Алина @al_glotova"}),

L(349,"nha-trang","vh","Квартира",32000000,None,
  "3-спальная квартира в ЖК Oceanus, север, просторный вариант.",
  "https://t.me/arenda_nhatrang/24400","13 августа",2,source="telegram",
  details={"deposit":"1 месяц + разовая комиссия 1,25 млн ₫","contract":"от 2 месяцев","notice":"агент Алина @al_glotova"}),
L(350,"nha-trang","tl","Квартира",17000000,59.2,"2-спальная меблированная квартира в комплексе HUD Building на ул. Nguyễn Thiện Thuật, центр.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-pho-nguyen-thien-thuat-phuong-tan-tien_1-hud-building-nha-trang/cho-2pn-full-noi-that-04-trang-pr46030877","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(351,"nha-trang","ph","Квартира",14000000,90,"3-спальная квартира, ЖК CT2 VCN Phước Hải, полная меблировка, рядом море.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-to-huu-phuong-phuoc-hai-chung-cu-ct2-vcn-phuoc-hai/cho-90m-3pn-ay-u-noi-that-gia-chi-14-trieu-thang-gan-bien-pr46182090","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '3 спальни'}),
L(352,"nha-trang","lt","Студия",18000000,50,"Студия с видом на море, комплекс Panorama Nha Trang, набережная.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-thi-minh-khai-phuong-loc-tho-panorama-nha-trang/view-bien-ep-co-bon-tam-studio-50m2-gia-tot-pr46121971","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(353,"nha-trang","tl","Квартира",26000000,88.19,"Угловая 3-спальная квартира, HUD Building, новый ремонт, премиум-мебель.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-pho-nguyen-thien-thuat-phuong-tan-tien_1-hud-building-nha-trang/lvcc-cho-goc-3pn-full-noi-that-cao-cap-moi-keng-ap-hop-tai-chi-26-tr-thang-pr46103607","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '3 спальни'}),
L(354,"nha-trang","pl","Квартира",12000000,68,"Квартира в ЖК CCU01 Phước Long, меблирована.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-van-kiet-phuong-phuoc-long-chung-cu-ccu-01-phuoc-long/cho-ccu01-ay-u-noi-that-pr46139624","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(355,"nha-trang","tl","Квартира",28000000,90,"3-спальная квартира, HUD Building, полная меблировка.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-pho-nguyen-thien-thuat-phuong-tan-tien_1-hud-building-nha-trang/cho-3pn-uong-gia-28-trieu-pr45935961","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '3 спальни'}),
L(356,"nha-trang","lt","Студия",12000000,38,"Студия с видом на город, комплекс Panorama Nha Trang, просторная.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-thi-minh-khai-phuong-loc-tho-panorama-nha-trang/studio-38m-view-thanh-pho-thoang-ep-full-noi-that-pr46112884","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(357,"nha-trang","lt","Студия",16000000,43,"Студия с видом на море, комплекс Panorama Nha Trang, светлая.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-thi-minh-khai-phuong-loc-tho-panorama-nha-trang/cho-studio-view-bien-khong-gian-thoang-sang-va-ay-u-gia-16tr-thang-pr46112814","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(358,"nha-trang","lt","Комната",2500000,20,"Меблированная комната в центре, домофон с отпечатком пальца на воротах.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-hoang-hoa-tham-phuong-loc-tho-350/chinh-chu-cho-du-noi-that-o-trung-tam-trang-cong-mo-khoa-van-tay-gia-2-5tr-thang-pr45114842","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(359,"nha-trang","pl","Комната",3000000,20,"Комната в районе Phước Long, Нячанг.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-ngo-tat-to-phuong-phuoc-long-350/cho-7a-trang-khanh-hoa-pr45165973","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(360,"nha-trang","tl","Комната",3000000,20,"Комната по ул. Ngô Gia Tự, центр.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-ngo-gia-tu-phuong-tan-tien_1-350/cho-o-tai-236-tu-pr46071290","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(361,"nha-trang","ph","Комната",2200000,18,"Комната в центре, 300 м до Co.op Mart, 200 м до рынка.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-hoan-kiem-phuong-phuoc-hai-350/trung-tam-trang-dt-18m2-gia-2-tr-cach-co-op-mart-300m-cho-200m-pr45028767","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(362,"nha-trang","nh","Комната",2500000,50,"Комната у рынка на ул. 23/10, за ТЦ Hoàng Lan.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-pho-luong-dinh-cua-phuong-ngoc-hiep-350/cho-o-uong-23-10-sau-lung-hang-hoang-lan-pr45979935","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(363,"nha-trang","vh","Комната",2500000,22,"Уютная недорогая комната, центр Нячанга.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-thanh-nam-1-phuong-vinh-hai-350/dep-tien-nghi-gia-re-trung-tam-trang-pr43211408","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(364,"nha-trang","tl","Комната",4500000,28,"Комната в центре города, рядом рынок Xóm Mới.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-ngo-thoi-nhiem-phuong-tan-tien_1-350/cho-ngay-trung-tam-thanh-pho-gan-cho-xom-moi-pr45857308","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(365,"nha-trang","ps","Комната",1200000,20,"Бюджетная комната для семьи, спокойный район, рядом школа Hà Huy Tập.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-23-10-xa-vinh-thanh-10-350/cho-gia-dinh-khu-vuc-an-ninh-so-754-18-23-10-gan-truong-ha-huy-tap-o-pr39101985","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(366,"nha-trang","vp","Дом",6000000,50,"Отдельный дом, 2 спальни/2 санузла, рядом рынок и университет.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-2-4-phuong-vinh-phuoc-350/cho-nguyen-can-gan-cho-hai-gan-ai-hoc-trang-dt-50m-2pn-2-wc-gia-chi-6-trieu-th-pr46172178","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(367,"nha-trang","ps","Дом",7000000,180,"Дом 2 этажа, 3 спальни, полная меблировка, район Miếu Bà.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-mieu-ba-xa-vinh-thanh-10-350/cho-ep-2-tang-full-noi-that-dt-180m-3-phong-ngu-trang-gia-7trieu-pr46140118","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '3 спальни'}),
L(368,"nha-trang","pl","Дом",13000000,60,"Дом целиком, 5 спален, хорошая цена за район.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-phuoc-long-phuong-phuoc-long-350/cho-nguyen-can-5-phong-ngu-gia-13-trieu-khu-vuc-gia-tot-chi-13tr-thang-pr46129893","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '5 спален'}),
L(369,"nha-trang","ph","Дом",21000000,80,"Дом целиком, 3 спальни, полная меблировка, район Hà Quang 1, близко к центру.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-hong-phong-phuong-phuoc-hai-khu-do-thi-le-hong-phong-i/cho-nguyen-can-k-t-ha-quang-1-trang-80m-3pn-full-noi-that-gan-trung-tam-thanh-pho-pr46183213","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '3 спальни'}),
L(370,"nha-trang","ph","Дом",35000000,130,"Дом с лифтом, 4 спальни, полная меблировка, район Hà Quang 2, подходит и под бизнес.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-hong-phong-phuong-phuoc-hai-khu-do-thi-le-hong-phong-ii/cho-o-kinh-doanh-co-thang-may-4-ngu-full-noi-that-ha-quang-2-pr46171423","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '4 спальни'}),
L(371,"nha-trang","lt","Дом",40000000,360,"Большой дом, 3 спальни/3 санузла, 2 этажа, центр (ул. Trần Quang Khải).","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-tran-quang-khai-phuong-loc-tho-350/cho-tai-40-trieu-360m2-3pn-3wc-2-tang-pr44360158","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '3 спальни'}),
L(372,"da-lat","xt","Квартира",10000000,61,"Новая квартира в ЖК Sun Garden Đà Lạt, полная меблировка, заезд сразу.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nam-ho-phuong-11_1-sun-garden-da-lat/cho-nha-moi-o-lien-full-noi-that-lien-he-pr42512173","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(373,"da-lat","xh","Квартира",14000000,100,"2-спальная квартира в ЖК Osaka Garden, есть спортплощадка во дворе.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-dong-da-phuong-3_3-391/cho-14-trieu-osaka-ong-a-a-lat-2pn-2vs-co-san-the-thao-rong-pr46169987","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(374,"da-lat","xh","Квартира",11000000,60,"1-спальная квартира с красивым видом, ЖК The Panorama Đà Lạt.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-10_4-the-panorama-da-lat/cho-60m2-tai-view-dep-1-phong-ngu-pr44271365","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '1 спальня'}),
L(375,"da-lat","xh","Комната",3500000,20,"Комната в гостевом доме с лифтом, хозяин сдаёт лично.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-pham-ngu-lao-phuong-3_3-391/chinh-chu-cho-ks-theo-thang-co-thang-may-pr46185045","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(376,"da-lat","lv","Комната",2000000,16,"Комната 16 м², район Phường 8 (Lâm Viên).","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-huu-canh-phuong-8_2-391/cho-1pn-16m2-gia-2-2-trieu-tai-1-8-p8-a-lat-pr45703872","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(377,"da-lat","lv","Комната",3400000,45,"Комната с отдельным санузлом, 45 м², район Phường 9 (Lâm Viên).","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-hung-vuong-2-phuong-9_2-391/cho-1pn-1wc-45m2-3-4-trieu-tai-32-p-9-a-lat-pr45985291","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(378,"da-lat","lv","Комната",3500000,40,"Отдельная комната 40 м² в жилом комплексе, 3 минуты до озера Xuân Hương.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-yersin-phuong-9_2-391/40m2-rieng-biet-kqh-full-tien-ich-3-phut-ra-ho-xuan-huong-3-5tr-thang-pr45698255","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(379,"da-lat","lv","Комната",2800000,24,"Комната ~25 м² с балконом перед комнатой.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-pho-phu-dong-thien-vuong-phuong-8_2-391/cho-o-lau-dai-dien-tich-khoang-25m2-bao-gom-ca-ban-cong-truoc-phong-pr45420454","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(380,"da-lat","xh","Комната",3300000,18,"Отдельная комната, приоритет для девушек.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-dong-tam-phuong-4_3-391/cho-rieng-tai-so-7-uong-ong-uu-tien-cho-nu-pr45389983","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(381,"da-lat","cl","Комната",2000000,28,"Комната, чисто и просторно, сразу за школой Lam Sơn.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-ngo-quyen-phuong-6_3-391/an-ninh-sach-se-rong-rai-ngay-sau-truong-lam-son-pr45359268","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(382,"da-lat","cl","Дом",20000000,72,"Дом фасадом на улицу, 6 спален, район Phan Đình Giót.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-phan-dinh-giot-phuong-6_3-391/cho-6pn-mat-tien-uong-inh-a-lat-chi-20tr-thang-pr46159595","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '6 спален'}),
L(383,"da-lat","xh","Дом",9000000,45,"Дом на ул. Triệu Việt Vương, Đà Lạt.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-trieu-viet-vuong-phuong-4_3-391/vuong-pr46155722","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(384,"da-lat","xt","Дом",11000000,300,"Дом на ул. Trịnh Hoài Đức, просторный участок.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-trinh-hoai-duc-phuong-11_1-391/cho-ep-uong-uc-a-lat-lam-ong-pr46144431","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(385,"da-lat","xh","Дом",7000000,100,"Дом 100 м², фасад к озеру Xuân Hương, от хозяина напрямую.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-tran-hung-dao-phuong-3_3-391/chinh-chu-cho-100m2-mat-uong-ao-xuan-huong-a-lat-pr45962440","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(386,"da-lat","xh","Дом",6000000,50,"Дом по хорошей цене, у самого центра Đà Lạt.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-luong-the-vinh-phuong-3_3-391/cho-a-lat-gia-tot-o-ngay-trung-tam-pr45576808","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(387,"da-lat","lv","Дом",15000000,150,"Дом целиком, 4 спальни, район Lâm Viên, недалеко от парка.","https://batdongsan.com.vn/cho-thue-nha-rieng-pho-phu-dong-thien-vuong-phuong-8_2-391/cho-nguyen-can-4p-ngu-uong-ong-p-lam-vien-a-lat-gia-15-trieu-thang-pr45572182","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '4 спальни'}),
L(388,"da-lat","xh","Дом",40000000,1000,"Дом с большим садом 1000 м², участок.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-trieu-viet-vuong-phuong-4_3-391/cho-nnc-co-san-vuon-1000-m2-45-tr-thang-uyen-pr45517753","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(389,"da-lat","xh","Дом",80000000,300,"Дом 300 м², 4 санузла, престижный участок в центре.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-tran-hung-dao-phuong-3_3-391/cho-nr-300m2-80-trieu-4wc-tai-6a-ao-a-lat-pr45944071","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(390,"da-nang","st","Квартира",11000000,40,"2-спальная квартира, ЖК Azura, ул. Trần Hưng Đạo, район Sơn Trà.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-tho-quang-son-tra-ocean-view/cho-ch-2pn-1wc-40m2-11-trieu-tai-70-cao-cap-azura-tran-hung-ao-a-nang-pr46182911","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(391,"da-nang","tk","Студия",12000000,47.25,"Студия в ЖК TTC Plaza, самый центр города.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-dien-bien-phu-phuong-chinh-gian-ttc-plaza-da-nang/cho-studio-a-song-ngay-trung-tam-thanh-pho-pr46050515","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(392,"da-nang","lc","Квартира",7500000,63.3,"Меблированная квартира, ЖК Mia Center Point, район Hòa Khánh Bắc, готова к заезду.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ngo-thi-nham-phuong-hoa-khanh-bac-mia-center-point/cho-a-nang-cao-cap-ay-u-noi-that-don-vao-o-ngay-pr46136602","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(393,"da-nang","st","Квартира",23000000,82,"2-спальная квартира, ЖК Harmony Tower, полная меблировка, рядом пляж Mỹ Khê.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-pham-van-dong-phuong-an-hai-bac-harmony-tower/cho-2-phong-ngu-toa-a-nang-full-noi-that-gan-bien-my-khe-a-nang-pr46004445","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(394,"da-nang","st","Квартира",14000000,74,"2-спальная квартира с хорошей планировкой, ЖК Ocean View, разумная цена.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ngo-quyen-phuong-tho-quang-son-tra-ocean-view/cho-2pn-goc-dep-gia-phai-chang-lh-0905-552-556-zalo-pr34120847","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(395,"da-nang","st","Студия",18000000,30,"Редкая студия-дуплекс, ЖК Sun Ponte Residence, скидка от хозяина.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-an-hai-nam-sun-ponte-residence-da-nang/studio-duplex-sieu-hiem-tai-chi-1x-trieu-thang-chu-nha-giam-pr46107756","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(396,"da-nang","ns","Квартира",12000000,68,"2-спальная квартира, ЖК FPT Plaza 3, минималистичный интерьер, принимают иностранцев.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-hoang-minh-thang-phuong-hoa-hai-fpt-plaza-3/cho-2pn-68m-3-noi-that-toi-gian-sang-trong-co-nhan-khach-nuoc-ngoai-pr46099505","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(397,"da-nang","lc","Квартира",6500000,60,"2-спальная квартира, ЖК The Ori Garden, полная меблировка.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-me-linh-phuong-hoa-hiep-nam-the-ori-garden/cho-2pn-day-du-noi-that-gia-6-5tr-thang-pr44856263","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(398,"da-nang","ns","Квартира",18000000,60,"2-спальная квартира, ЖК Mường Thanh Đà Nẵng, у пляжа.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-nguyen-giap-phuong-my-an-muong-thanh-da-nang/cho-ngay-bien-khe-2pn-2wc-full-noi-that-pr46140163","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(399,"da-nang","tk","Квартира",13500000,110,"3-спальная квартира 110 м², ЖК Hoàng Anh Gia Lai Lake View Residence.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ham-nghi-phuong-thac-gian-hoang-anh-gia-lai-lake-view-residence/cho-3-phong-ngu-dien-tich-110m2-gian-pr45214947","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '3 спальни'}),
L(400,"da-nang","st","Студия",30000000,45,"Студия с видом на море, ЖК Times Square, готова к заезду.","https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-nguyen-giap-phuong-phuoc-my-da-nang-times-square/cho-studio-view-bien-a-gia-tot-vao-noi-that-on-gian-nhan-khach-ngay-pr46181929","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(401,"da-nang","ns","Комната",2700000,20,"Новый шоп-хаус, район Hòa Quý, рядом Đà Nẵng Petro.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-vo-chi-cong-phuong-hoa-quy-khu-do-thi-hoa-quy/cao-cap-gia-re-moi-xay-shophouse-dau-khi-da-nang-pr37012702","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(402,"da-nang","hcg","Комната",4000000,40,"Комната 40 м² в центре, район Hòa Cường (Hải Châu).","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-dang-thuy-tram-phuong-hoa-cuong-bac-46/trung-tam-uong-ang-40m2-gia-4-trieu-pr46156902","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(403,"da-nang","hx","Комната",2500000,24,"Комната фасадом на улицу 5,5 м, район Hòa Xuân.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-doan-ngoc-nhac-phuong-hoa-xuan-kdt-nam-cau-nguyen-tri-phuong/chinh-chu-cho-mat-tien-24m2-uong-5-5m-oan-p-tp-a-nang-gia-2-5tr-tg-pr46154262","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(404,"da-nang","hc","Комната",3000000,9,"Комната для девушек (без подселения), район Hải Châu.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-ong-ich-khiem-phuong-thanh-binh-46/nu-hai-chau-khong-ghep-pr46095691","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(405,"da-nang","ns","Комната",5500000,20,"Комната гостиничного типа, фасад на ул. Võ Nguyên Giáp, район Mỹ An.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-vo-nguyen-giap-phuong-my-an-48/cho-khach-san-mat-tien-giap-pr46113482","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(406,"da-nang","ns","Комната",2500000,25,"Новая комната, рядом FPT Plaza / F-Complex, район Hòa Hải.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-phan-chanh-phuong-hoa-hai-48/cho-moi-100-uong-gan-fpt-plaza-f-complex-pr45920533","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(407,"da-nang","hc","Комната",2600000,17,"Комната в центре, район Hòa Thuận Tây.","https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-huu-tho-phuong-hoa-thuan-tay-46/chinh-chu-cho-trung-tam-19-da-nang-pr35819466","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(408,"da-nang","hc","Дом",7000000,100,"Дом целиком, район Hải Châu, ул. Nguyễn Trường Tộ.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-truong-to-phuong-hai-chau_1-46/chinh-chu-cho-can-36-6-chau-tp-a-nang-7-trieu-thang-pr46157782","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(409,"da-nang","st","Дом",23000000,66,"Дом 2 этажа фасадом на улицу, можно под кафе/бизнес, район Sơn Trà.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ta-my-duat-phuong-phuoc-my-49/cho-2-tang-mat-tien-san-mo-hinh-cafe-hang-kinh-doanh-pr46089328","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(410,"da-nang","hx","Дом",12000000,100,"3-спальный дом целиком, район Hòa Xuân (Cẩm Lệ), надёжный хозяин.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-vo-chi-cong-phuong-hoa-xuan-kdt-nam-cau-nguyen-tri-phuong/cho-nr-tai-k-t-cam-le-12-trieu-100m2-chinh-chu-uy-tin-on-inh-pr46184876","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '3 спальни'}),
L(411,"da-nang","st","Дом",8500000,55,"2-спальный дом, район Sơn Trà, улица 3,75 м.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nai-nghia-3-phuong-nai-hien-dong-49/cho-2-phong-2vs-khu-vuc-son-tra-uong-3m75-pr46184306","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '2 спальни'}),
L(412,"da-nang","tk","Дом",23000000,65,"Дом 3 этажа, 4 спальни, центр района Thanh Khê.","https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-thac-gian/cho-3-tang-ep-4pn-trung-tam-thanh-khe-23-trieu-th-pr46181719","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '4 спальни'}),
L(413,"da-nang","tk","Дом",10000000,85,"Дом 2 этажа, 85 м², район Thạc Gián.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-van-linh-phuong-thac-gian-50/10tr-cho-2-tang-x85m2-k-a-nang-pr46176245","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(414,"da-nang","hcg","Дом",40000000,100,"Дом целиком, 4 спальни, район Nam Cầu Tuyên Sơn, новый.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-my-da-tay-5-phuong-khue-my-khu-do-thi-nam-cau-tuyen-son/cho-ep-4pn-viet-a-moi-tinh-pr46174083","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026", 'amenities': '4 спальни'}),
L(415,"da-nang","hc","Дом",23000000,71,"Дом целиком, район Hòa Thuận Tây.","https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-huu-tho-phuong-hoa-thuan-tay-46/cho-can-ep-tho-pr46099587","проверено 15 авг",1,source="batdongsan",details={'notice': "массовая выгрузка Batdongsan.com.vn — точная дата исходной публикации не извлекалась при бульк-сборе; объявление проверено как активное (не 'Tin đã hết hạn') на 15.08.2026"}),
L(416,"nha-trang","lt","Студия",12733048,None,"Студия с панорамными окнами в комплексе Panorama Nha Trang, высокий этаж, кровать king-size с постельным бельём 5 звёзд, рабочий стол, Smart TV 43\". Доступ к бассейну и залу на 7 этаже, ресепшен 24/7.","https://www.airbnb.com/rooms/765996255030512945","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 20 216 000 ₫ (≈505 $).', 'policy': 'Хозяин Holi Panorama, 7 лет на Airbnb, рейтинг 4.79 (19 отзывов).'}),
L(417,"nha-trang","vp","Комната",6132645,None,"Тихий номер в бутик-отеле на севере Нячанга, рядом мини-маркеты и кафе, терраса на крыше для сушки белья, хороший wifi для удалённой работы.","https://www.airbnb.com/rooms/40980317","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 25 788 645 ₫ (≈243 $).', 'policy': 'Хозяйка Rosé — суперхозяин, 7 лет, 258 отзывов, рейтинг 4.81. Бесплатная отмена за 48 ч.'}),
L(418,"nha-trang","lt","Дом",13406665,None,"Бюджетный пляжный дом, 1 спальня, 5 минут пешком до моря, семья хозяев живёт в этом же 6-этажном здании.","https://www.airbnb.com/rooms/1081619575834073158","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 19 765 256 ₫ (≈532 $).', 'policy': 'Хозяйка Felicia — суперхозяин, 10 лет, 111 отзывов, рейтинг 4.46.'}),
L(419,"nha-trang","lt","Студия",21850950,43,"Центральная квартира-студия с частичным видом на море и балконом, 16 Ton Dan Street (район Lộc Thọ), отель-апартаменты Maple. Уют в деревянном декоре, рядом башня Trầm Hương и площадь 2/4.","https://www.airbnb.com/rooms/1586122716584266266","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 41 000 000 ₫ (≈867 $).', 'policy': 'Электричество/вода/управление/парковка мотобайка — отдельно; депозит за коммуналку ≈3 млн ₫ (возвратный). 2 бесплатные уборки в месяц. Хозяин — суперхозяин, рейтинг 5.0 (10 отзывов).'}),
L(420,"nha-trang","vt","Комната",7448328,25,"Комната с отдельным санузлом в тихом переулке, 5-15 минут пешком до пляжа, Lotte Mart и ночного рынка.","https://www.airbnb.com/rooms/1148832525729396287","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 10 980 704 ₫ (≈296 $).', 'policy': 'Хозяин Đức — суперхозяин, 6 лет, 109 отзывов, рейтинг 4.87.'}),
L(421,"nha-trang","lt","Студия",22442040,44,"Студия на верхнем этаже комплекса Marina Suites (25 Phan Chu Trinh), вид на восход и океан, ТВ 65\", холодильник 350Л, wifi 250-350 Мбит/с.","https://www.airbnb.com/rooms/1691032684477198260","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 33 000 000 ₫ (≈891 $).', 'policy': 'Управление 17 600 ₫/м², электричество/вода/wifi 300 тыс ₫ — отдельно; депозит ≈5 млн ₫ ($200). Хозяйка Mỹ Linh — суперхозяин, 3 года, 752 отзыва, рейтинг 4.86.'}),
L(422,"nha-trang","lt","Студия",6959358,None,"Хорошая студия для пары у пляжа.","https://www.airbnb.com/rooms/1004654845042800303","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 26 600 000 ₫ (≈276 $).', 'policy': 'Рейтинг 4.93 (15 отзывов).'}),
L(423,"nha-trang","lt","Квартира",7300768,None,"Квартира с бесплатным парковочным местом, полностью новый интерьер.","https://www.airbnb.com/rooms/728033916638999709","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 15 220 768 ₫ (≈290 $).', 'policy': 'Рейтинг 4.91 (11 отзывов).'}),
L(424,"nha-trang","lt","Студия",7247672,None,"Комфортная тихая студия со своей кухней.","https://www.airbnb.com/rooms/996642984565872173","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 25 895 672 ₫ (≈288 $).', 'policy': 'Рейтинг 4.9 (21 отзыв).'}),
L(425,"nha-trang","lt","Студия",9078367,None,"Уютная студия в центре, рядом пляж.","https://www.airbnb.com/rooms/602755100493749581","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 13 384 000 ₫ (≈360 $).', 'policy': 'Бутик-отель, рейтинг 4.96 (23 отзыва).'}),
L(426,"nha-trang","lt","Квартира",24418800,None,"Тихая квартира с 2 спальнями, сверхбыстрый wifi.","https://www.airbnb.com/rooms/1648645593542196811","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 42 000 000 ₫ (≈969 $).', 'policy': 'Новое объявление, отзывов пока нет.'}),
L(427,"nha-trang","lt","Квартира",20717368,None,"Квартира в центральном комплексе Goldcoast, набережная Trần Phú.","https://www.airbnb.com/rooms/1087315374048385666","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 24 828 568 ₫ (≈822 $).', 'policy': 'Рейтинг 4.94 (33 отзыва).'}),
L(428,"nha-trang","lt","Квартира",20271480,None,"Квартира с видом на океан в комплексе Marina Suites.","https://www.airbnb.com/rooms/1194559142984200293","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 29 800 000 ₫ (≈804 $).', 'policy': 'Рейтинг 4.82 (33 отзыва).'}),
L(429,"nha-trang","vp","Студия",17824174,None,"Студия в комплексе StarCity, вид на море/пляж, север города.","https://www.airbnb.com/rooms/1049188310911945444","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 20 864 000 ₫ (≈707 $).', 'policy': 'Рейтинг 4.9 (59 отзывов).'}),
L(430,"nha-trang","lt","Комната",11558968,None,"Комната с 1 кроватью и видом на сад.","https://www.airbnb.com/rooms/1390250119267780510","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 14 372 000 ₫ (≈459 $).', 'policy': 'Рейтинг 5.0 (24 отзыва).'}),
L(431,"nha-trang","lt","Квартира",17160990,None,"Центральная квартира с 1 спальней и балконом, вариант для долгосрочной аренды.","https://www.airbnb.com/rooms/1666324748232583251","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 32 200 000 ₫ (≈681 $).', 'policy': 'Хозяин — суперхозяин.'}),
L(432,"nha-trang","lt","Комната",10699681,None,"Просторная стильная комната с джакузи.","https://www.airbnb.com/rooms/22351354","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 14 156 403 ₫ (≈425 $).', 'policy': 'Рейтинг 4.76 (103 отзыва).'}),
L(433,"nha-trang","lt","Комната",7942133,None,"Улучшенный номер с 2 кроватями (одна/двуспальная на выбор).","https://www.airbnb.com/rooms/823475382780042772","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 10 928 288 ₫ (≈315 $).', 'policy': 'Рейтинг 4.74 (39 отзывов).'}),
L(434,"da-lat","xh","Студия",11186136,24,"Просторная двухуровневая студия с собственным балконом, полностью оборудованная кухня, диван-кровать для третьего гостя.","https://www.airbnb.com/rooms/817212036990332976","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 20 520 000 ₫ (≈444 $).', 'policy': 'Хозяйка Thy — суперхозяин, 6 лет, 157 отзывов, рейтинг 4.84 (50 отзывов).'}),
L(435,"da-lat","xh","Комната",10508538,None,"Комната в гестхаусе в самом центре Далата, рядом озеро Xuân Hương, рынок и площадь Lâm Viên. У комнаты — окно или балкон.","https://www.airbnb.com/rooms/1362549612996630745","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 12 758 524 ₫ (≈417 $).', 'policy': 'Хозяйка Ngọc Quỳnh — суперхозяин, 2 года, 377 отзывов, рейтинг 4.96 (26 отзывов).'}),
L(436,"da-lat","lv","Комната",9081893,22,"Свежая просторная комната (>22 м²) с высокими потолками и своим санузлом, звукоизоляция, терраса на крыше с видом на закат, рядом озеро Xuân Hương и Далатский университет.","https://www.airbnb.com/rooms/1298883646511342856","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 12 439 189 ₫ (≈360 $).', 'policy': 'Хозяйка Nha Uyen (Lila) — суперхозяин, 7 лет, 77 отзывов, рейтинг 4.8 (15 отзывов).'}),
L(437,"da-lat","lv","Студия",16933288,None,"Просторная студия с видом на сад/долину, новая постройка, своя кухня и вход, 5 минут пешком до Летнего дворца императора (Dinh Bảo Đại).","https://www.airbnb.com/rooms/35277989","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 29 338 888 ₫ (≈672 $).', 'policy': 'Хозяйка Annie — суперхозяин, 8 лет, 345 отзывов, рейтинг 4.92 (89 отзывов).'}),
L(438,"da-lat","xh","Комната",5532986,None,"Комната в небольшой вилле среди старых французских вилл на тихой улице, 5 минут на мотобайке до центра — самая доступная находка в Далате.","https://www.airbnb.com/rooms/20836443","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 9 516 612 ₫ (≈220 $).', 'policy': 'Хозяйка Мỹ, 9 лет, 507 отзывов, рейтинг 4.8 (86 отзывов).'}),
L(439,"da-lat","xh","Комната",15183474,None,"Одноместная спальня в гестхаусе «Дом вашей тёти».","https://www.airbnb.com/rooms/1384133180748382814","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 20 892 312 ₫ (≈603 $).', 'policy': 'Рейтинг 4.95 (43 отзыва).'}),
L(440,"da-lat","xh","Комната",10824893,None,"Стандартный номер, Pahota House, хостел-формат.","https://www.airbnb.com/rooms/1742516114564152593","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 13 964 000 ₫ (≈430 $).', 'policy': 'Новое объявление, отзывов пока нет.'}),
L(441,"da-lat","xh","Комната",7046347,None,"Солнечная комната в доме «Тары».","https://www.airbnb.com/rooms/832477031918983298","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 13 676 347 ₫ (≈280 $).', 'policy': 'Рейтинг 5.0 (15 отзывов).'}),
L(442,"da-lat","xh","Квартира",18105241,None,"Квартира в центре Далата — балкон, кухня, кондиционер.","https://www.airbnb.com/rooms/34246313","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 38 109 841 ₫ (≈718 $).', 'policy': 'Рейтинг 4.78 (18 отзывов).'}),
L(443,"da-lat","xh","Студия",17516003,None,"Меблированная студия, Simplify House 203.","https://www.airbnb.com/rooms/588890285355750505","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 25 673 283 ₫ (≈695 $).', 'policy': 'Рейтинг 4.93 (61 отзыв).'}),
L(444,"da-lat","xh","Студия",14611557,None,"Роскошная студия Zea — кухня, вид на закат, своя стиральная машина.","https://www.airbnb.com/rooms/1494728217186581220","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 18 865 174 ₫ (≈580 $).', 'policy': 'Рейтинг 5.0 (6 отзывов).'}),
L(445,"da-lat","xh","Студия",21404790,None,"Квартира-студия с балконом и видом на город.","https://www.airbnb.com/rooms/1610540026256504085","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 26 242 350 ₫ (≈849 $).', 'policy': 'Рейтинг 4.86 (14 отзывов).'}),
L(446,"da-lat","xh","Другое",11303058,None,"Family-стей с видом на горы, вегетарианская кухня, кровать queen-size.","https://www.airbnb.com/rooms/1227157334346736477","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 17 673 684 ₫ (≈449 $).', 'policy': 'Рейтинг 5.0 (4 отзыва).'}),
L(447,"da-lat","xh","Квартира",25693773,None,"Квартира с видом — отмечена наградой Airbnb «Choice путешественников».","https://www.airbnb.com/rooms/32342033","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 40 680 856 ₫ (≈1020 $).', 'policy': 'Рейтинг 4.94 (156 отзывов). Дороже целевого бюджета — включена для полноты картины.'}),
L(448,"da-lat","xh","Дом",25244065,None,"Вилла Cocohome Đà Lạt с видом на долину, барбекю и бильярд, 2 спальни.","https://www.airbnb.com/rooms/1523765099275778630","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 36 398 065 ₫ (≈1002 $).', 'policy': 'Рейтинг 5.0 (18 отзывов). Дороже целевого бюджета — включена для полноты картины.'}),
L(449,"da-lat","xh","Квартира",32558400,None,"Элитная квартира Glamis House, 2 спальни.","https://www.airbnb.com/rooms/1702210020858484235","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 44 800 000 ₫ (≈1292 $).', 'policy': 'Новое объявление, отзывов пока нет. Существенно дороже целевого бюджета — включена для полноты картины.'}),
L(450,"da-lat","xh","Дом",14927195,None,"Микродом («tiny house») в Далате.","https://www.airbnb.com/rooms/933578084990058580","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 18 300 795 ₫ (≈592 $).', 'policy': 'Рейтинг 4.73 (33 отзыва).'}),
L(451,"da-lat","xh","Студия",17626110,None,"Homestay «Мой новый дом», студия №1.","https://www.airbnb.com/rooms/1102047573466049566","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 21 400 000 ₫ (≈699 $).', 'policy': 'Рейтинг 5.0 (16 отзывов).'}),
L(452,"da-nang","st","Квартира",16014836,None,"MioHome — уютная тропическая квартира №302, 250 м / 3 минуты пешком до пляжа Phạm Văn Đồng. Джакузи в ванной, мини-кухня, все счета за электричество/воду и еженедельную уборку включены в помесячную цену.","https://www.airbnb.com/rooms/1747902448219405787","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 19 574 836 ₫ (≈636 $).', 'policy': 'Хозяин Anh — суперхозяин, 1 год, 194 отзыва, рейтинг 4.9 (новое объявление — 1 отзыв 5★).'}),
L(453,"da-nang","ns","Комната",10811978,None,"HH201 — комната в хоумстее в 500 м / 7 минутах от пляжа Mỹ Khê, общая кухня на 2 этаже, вход по смарт-замку.","https://www.airbnb.com/rooms/1445686655424456594","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 14 877 160 ₫ (≈429 $).', 'policy': 'Хозяин Quốc Huy — суперхозяин, 1 год, 197 отзывов, рейтинг 5.0 (32). Для заселения нужно фото паспорта/визы — местная норма регистрации.'}),
L(454,"da-nang","hc","Квартира",10597041,None,"LonaHome — квартира с 1 спальней и большими окнами на первом этаже, 700 м до реки Хан, своя современная кухня. Электричество/вода/еженедельная уборка включены в цену.","https://www.airbnb.com/rooms/1471570753900473111","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 12 528 241 ₫ (≈420 $).', 'policy': 'Хозяин Cong Phuong — суперхозяин, 1 год, 209 отзывов, рейтинг 5.0 (11).'}),
L(455,"da-nang","ah","Комната",10965807,None,"«Дом Феликса 3» — комната в мини-хоуме в районе An Hải Đông, 10 минут пешком до Драконьего моста и пляжа Mỹ Khê, общая кухня/гостиная/крыша.","https://www.airbnb.com/rooms/34372247","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 10 965 807 ₫ (≈435 $).', 'policy': 'Фиксированная помесячная цена (без отдельной скидки). Хозяйка Quyên — суперхозяин, 7 лет, 822 отзыва, рейтинг 4.87 (131) — самое отзываемое предложение в подборке.'}),
L(456,"da-nang","st","Комната",14746106,None,"Комната с видом на город в комплексе отельного типа, бесконечный бассейн с золотой плиткой, быстрый wifi, район Nại Hiên Đông.","https://www.airbnb.com/rooms/1604854262110899884","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 25 654 000 ₫ (≈585 $).', 'policy': 'Управление 340 тыс ₫/мес + вода 100 тыс ₫/чел — отдельно, электричество не включено. Хозяйка Anna Nguyen — суперхозяин, 1 год, 89 отзывов, рейтинг 5.0 (3).'}),
L(457,"da-nang","st","Комната",14796359,None,"Квартира с видом на реку, большой балкон, бесплатный бассейн.","https://www.airbnb.com/rooms/1443170265866971607","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 24 506 000 ₫ (≈587 $).', 'policy': 'Рейтинг 5.0 (12 отзывов).'}),
L(458,"da-nang","st","Квартира",16088238,None,"BalizaHome — балкон, новый ремонт, 2 минуты до пляжа Mỹ Khê.","https://www.airbnb.com/rooms/1617400623486269779","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 18 644 238 ₫ (≈638 $).', 'policy': 'Рейтинг 5.0 (4 отзыва).'}),
L(459,"da-nang","st","Квартира",13395078,None,"Riverside — OceanSight Apartment 303.","https://www.airbnb.com/rooms/1385558226075937251","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 16 250 738 ₫ (≈532 $).', 'policy': 'Рейтинг 4.95 (19 отзывов).'}),
L(460,"da-nang","st","Квартира",16350000,None,"Квартира с проектором, скидка 25%.","https://www.airbnb.com/rooms/1618606855840390724","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 21 800 000 ₫ (≈649 $).', 'policy': 'Рейтинг 5.0 (11 отзывов).'}),
L(461,"da-nang","st","Комната",23635848,None,"Уютная квартира в 3 минутах от пляжа Mỹ Khê.","https://www.airbnb.com/rooms/1720827279524021872","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 27 080 000 ₫ (≈938 $).', 'policy': 'Рейтинг 5.0 (13 отзывов). Дороже целевого бюджета — включена для полноты картины.'}),
L(462,"da-nang","st","Комната",15657341,None,"Квартира Golden Bay — вид на улицу, балкон.","https://www.airbnb.com/rooms/1491694635601785752","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 26 700 835 ₫ (≈621 $).', 'policy': 'Рейтинг 5.0 (4 отзыва).'}),
L(463,"da-nang","st","Квартира",16296200,None,"Ami Foreign Center Da Nang 2.","https://www.airbnb.com/rooms/1149954660530924647","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 21 444 200 ₫ (≈647 $).', 'policy': 'Рейтинг 4.92 (83 отзыва).'}),
L(464,"da-nang","st","Квартира",16754599,None,"Mountain Sea DNG 2 — бассейн, вид на горы.","https://www.airbnb.com/rooms/1488276405515818283","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 22 048 199 ₫ (≈665 $).', 'policy': 'Рейтинг 4.88 (17 отзывов).'}),
L(465,"da-nang","st","Квартира",15656829,None,"BalizaHome Modern — балкон, вид на город.","https://www.airbnb.com/rooms/1489167395738705812","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 17 762 829 ₫ (≈621 $).', 'policy': 'Рейтинг 4.8 (15 отзывов).'}),
L(466,"da-nang","st","Квартира",15720988,None,"Квартира Ania — студия, 350 м до пляжа Ман-Тай.","https://www.airbnb.com/rooms/1688288614884404936","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 18 228 988 ₫ (≈624 $).', 'policy': 'Рейтинг 4.9 (10 отзывов).'}),
L(467,"da-nang","st","Комната",13358246,None,"Floriane 3.1 — вид на океан, тихий район.","https://www.airbnb.com/rooms/1315728605714872385","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 16 020 000 ₫ (≈530 $).', 'policy': 'Рейтинг 4.88 (33 отзыва).'}),
L(468,"da-nang","ns","Дом",14794741,None,"Солнечная студия с балконом, 5 минут до пляжа Mỹ Khê, район Ngũ Hành Sơn.","https://www.airbnb.com/rooms/1738054509551713839","проверено 15 авг",1,source="airbnb",details={'notice': 'Цена — «помесячная скидочная» стоимость Airbnb за бронь 15 сен – 13 окт 2026 (28 ночей), не отдельно выставленный месячный тариф. Полная (без скидки) сумма за этот период: 18 567 081 ₫ (≈587 $).', 'policy': 'Новое объявление, отзывов пока нет.'}),
L(469,"nha-trang","vp","Квартира",10480000,None,
  "2-спальная квартира в 7 минутах ходьбы от пляжа Bãi Dương, север города, тихий район.",
  "https://www.vrbo.com/7857196ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"цена указана как «Monthly stay $90 off» — скидка Vrbo за длительное проживание уже включена. Отзывов пока нет.","amenities":"парковка, кухня, стиральная машина, кондиционер, балкон, wifi","policy":"безвозвратное бронирование (без отмены)"}),

L(470,"nha-trang","lt","Квартира",22960000,None,
  "2-спальные апартаменты в том же здании, что и Muong Thanh Luxury Hotel 5*, центр, 1 минута до пляжа.",
  "https://www.vrbo.com/4271384ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"рейтинг 8.6/10 (106 отзывов на внешних площадках)","amenities":"бассейн, на первой линии пляжа, кухня, стиральная машина, кайяки и водный инвентарь у комплекса","policy":"безвозвратное бронирование"}),

L(471,"nha-trang","vt","Студия",37750000,None,
  "Студия с видом на море в комплексе The Costa Residence, рядом с InterContinental, набережная Trần Phú.",
  "https://www.vrbo.com/4102851ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","deposit":"200$ (по данным хозяина)","notice":"⚠ цена на Vrbo (30 ночей) — 1498$/мес, но хозяин в описании указывает более дешёвый прямой месячный тариф — 1050$/мес (без коммуналки) при бронировании от месяца напрямую, уточняйте у хозяина. Рейтинг 10/10 (2 отзыва).","amenities":"бассейн-инфинити, тренажёрный зал, кондиционер, стиральная машина","policy":"безвозвратное бронирование"}),

L(472,"nha-trang","ph","Квартира",33870000,None,
  "2-спальный кондо (2 санузла) с видом на море и горы, рядом с рынком Chợ Đầm, для удалённой работы — быстрый wifi, эргономичное кресло по запросу.",
  "https://www.vrbo.com/9958013ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"рейтинг 9.8/10 (12 отзывов). Бассейн и тренажёрный зал — за отдельную плату.","amenities":"полная кухня, быстрый wifi, опция стола/монитора для удалённой работы","policy":"безвозвратное бронирование"}),

L(473,"nha-trang","vh","Квартира",32840000,None,
  "2-спальный кондо (2 санузла) в 20 м от пляжа, напротив Hòn Chồng, современный дизайн, вид на море.",
  "https://www.vrbo.com/9211981ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"рейтинг 10/10 (3 отзыва)","policy":"безвозвратное бронирование"}),

L(474,"nha-trang","ph","Квартира",21650000,63,
  "2-спальная квартира (заявлена как «3 спальни» в заголовке) в комплексе с крытым бассейном и джакузи.",
  "https://www.vrbo.com/9341476ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","amenities":"крытый бассейн, джакузи, гараж/паркинг, кондиционер","notice":"отзывов пока нет","policy":"безвозвратное бронирование"}),

L(475,"da-lat","xh","Дом",47120000,None,
  "Целый таунхаус с 2 спальнями и полной кухней в центре Далата, 5 минут до озера Xuân Hương, для семьи/группы.",
  "https://www.vrbo.com/20129873ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"⚠ рейтинг 10/10, но всего 1 отзыв; у хозяина отмечена высокая доля отмен бронирований (50%) — уточняйте актуальность перед оплатой.","policy":"безвозвратное бронирование"}),

L(476,"da-lat","lv","Дом",20840000,20,
  "Отдельное двойное бунгало с видом на долину, у Деревни цветов Thái Phiên, приватная лестница и балкон.",
  "https://www.vrbo.com/1746945","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"рейтинг 10/10 (21 отзыв на внешних площадках)","policy":"безвозвратное бронирование"}),

L(477,"da-lat","lv","Дом",19250000,None,
  "Большой дом-хостел на 3 спальни (спит до 30 человек) в пешей доступности от Университета Далата — формат общежития/хостела, не обычная квартира.",
  "https://www.vrbo.com/9897894ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"формат — большой дом на много кроватей (dorm-style), не отдельная квартира. Отзывов пока нет."}),

L(478,"da-lat","xh","Студия",22650000,None,
  "Студия с видом на долину, рядом с Crazy House и дворцом Bảo Đại.",
  "https://www.vrbo.com/3963180","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"рейтинг 9.6/10 (24 отзыва на внешних площадках)","policy":"безвозвратное бронирование"}),

L(479,"da-nang","hc","Студия",26640000,None,
  "Студия в 2 минутах от реки Hàn / залива Đà Nẵng, бесплатная встреча в аэропорту при брони от 7 ночей.",
  "https://www.vrbo.com/20197146ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"рейтинг 9.8/10 (32 отзыва)","policy":"безвозвратное бронирование"}),

L(480,"da-nang","st","Квартира",25400000,None,
  "1-спальная квартира в 7 минутах ходьбы от пляжа Mỹ Khê.",
  "https://www.vrbo.com/20145803ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"рейтинг 8.8/10 (5 отзывов)","policy":"безвозвратное бронирование"}),

L(481,"da-nang","hcg","Квартира",44800000,150,
  "2-спальный дом с приватным садом и зоной барбекю, район Hòa Cường, кафе на первом этаже, йога-студия в здании.",
  "https://www.vrbo.com/5421085","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"есть номер регистрации объекта (048095001716) — редкость для этой площадки, признак легальности. Отзывов пока нет.","policy":"безвозвратное бронирование"}),

L(482,"da-nang","st","Студия",20430000,35,
  "Студия рядом с мостом Rồng (Dragon Bridge).",
  "https://www.vrbo.com/9504256ha","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","notice":"⚠ рейтинг всего 2.0/10 (1 отзыв, «Terrible») — включено для честности картины рынка, не как рекомендация. Проверяйте отзывы перед бронированием.","policy":"безвозвратное бронирование"}),

L(483,"da-nang","ah","Квартира",25500000,None,
  "1-спальная квартира с wifi и кондиционером, 8 минут ходьбы до пляжа Mỹ Khê, разрешено с собакой.",
  "https://www.vrbo.com/4269337","проверено 15 авг",1,source="vrbo",
  details={"contract":"помесячно, цена Vrbo за 30 ночей","policy":"безвозвратное бронирование, можно с животными","notice":"отзывов пока нет"}),
L(485,"nha-trang","vh","Студия",23310000,42,
  "Студия с видом на море в комплексе Scenia Bay, ул. Phạm Văn Đồng, север города, ~840 м до пляжа.",
  "https://www.trip.com/hotels/detail/?hotelId=131763518","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"рейтинг 8.9/10 (67 отзывов); скидка за длительное проживание уже применена (было 44$/ночь, стало 31$/ночь)","amenities":"полная кухня, стиральная машина, открытый бассейн-инфинити с видом на море, лифт, охрана 24ч"}),

L(486,"nha-trang","tl","Квартира",29280000,28,
  "Квартира в комплексе Viela Apartment, ул. Tôn Đản, центр города, 330 м до пляжа.",
  "https://www.trip.com/hotels/detail/?hotelId=122076725","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"рейтинг 9.4/10 (152 отзыва); скидка за длительное проживание уже применена (было 68$/ночь, стало 38$/ночь)","amenities":"кухонный уголок (плита, микроволновка), стиральная машина, мини-холодильник, ресепшен 24ч"}),

L(487,"nha-trang","vh","Квартира",23640000,35,
  "Апартаменты в новом комплексе Bai Tien Ocean Front Residences, район Bãi Tiên, север города, завтрак включён.",
  "https://www.trip.com/hotels/detail/?hotelId=135394927","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"новый объект, отзывов пока нет; скидка за длительное проживание уже применена (было 61$/ночь, стало 31$/ночь)","policy":"безвозвратное бронирование"}),

L(488,"nha-trang","vn","Дом",77160000,None,
  "Целый дом на 3 спальни/4 санузла с барбекю на крыше, район Mỹ Gia, юг города, самостоятельное заселение, ~3 км до моря.",
  "https://www.trip.com/hotels/detail/?hotelId=135524070","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей, вмещает до 6 человек","notice":"рейтинг 10/10 (новый объект, оценка со сторонних площадок)","amenities":"бесплатная парковка, самостоятельное заселение, барбекю на крыше, разрешены животные","policy":"безвозвратное бронирование"}),

L(489,"nha-trang","vn","Квартира",17440000,36,
  "Семейный номер-квартира в отеле Uy Dương, юг города, ~2,4 км / 20-25 мин пешком до пляжа.",
  "https://www.trip.com/hotels/detail/?hotelId=100411776","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей, 2 queen-кровати + диван-кровать, вмещает 4","notice":"рейтинг 8.7/10 (19 отзывов); стиральная машина и кухонный уголок есть не во всех номерах — уточняйте при бронировании","policy":"безвозвратное бронирование"}),

L(490,"da-lat","xh","Квартира",64390000,70,
  "2-спальная квартира в Dalat Center Residence, самый центр города, 150 м до Ночного рынка.",
  "https://www.trip.com/hotels/detail/?hotelId=23647948","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"рейтинг 9.0/10 (593 отзыва). Есть варианты меньше/больше: 1-спальная 50 м², 2-спальная/2 с/у 90 м², 3-спальная 100 м² — до 145$/ночь.","amenities":"кухонный уголок (плита, микроволновка), балкон, 2 queen-кровати","policy":"безвозвратное бронирование"}),

L(491,"da-lat","xh","Квартира",29180000,None,
  "Стандартный номер с окном, ENJOY APARTMENT.",
  "https://www.trip.com/hotels/detail/?hotelId=114978406","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"точный район не указан в объявлении, данные со страницы поиска (без глубокого просмотра). Рейтинг 10/10 (2 отзыва, новый объект)."}),

L(492,"da-lat","xt","Комната",8670000,None,
  "Стандартный двухместный номер, Family & Friends Homestay, рядом с Цветочной долиной Далата.",
  "https://www.trip.com/hotels/detail/?hotelId=125430623","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"бюджетный вариант; данные со страницы поиска. Рейтинг 10/10 (7 отзывов)."}),

L(493,"da-lat","xh","Комната",13410000,None,
  "Улучшенный номер с queen-кроватью, An Phu House Valley View.",
  "https://www.trip.com/hotels/detail/?hotelId=134619565","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"точный район не указан в объявлении, данные со страницы поиска. Рейтинг 8.9/10 (15 отзывов)."}),

L(494,"da-lat","xh","Комната",13830000,None,
  "Делюкс двухместный номер, Co Lang Mo Homestay.",
  "https://www.trip.com/hotels/detail/?hotelId=68045976","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"точный район не указан в объявлении, данные со страницы поиска. Рейтинг 10/10 (новый объект)."}),

L(495,"da-lat","xh","Комната",14840000,None,
  "Стандартный классический номер, De la Sol Villas Da Lat.",
  "https://www.trip.com/hotels/detail/?hotelId=92187138","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"точный район не указан в объявлении, данные со страницы поиска. Рейтинг 9.7/10 (4 отзыва)."}),

L(496,"da-lat","xh","Студия",17010000,None,
  "Улучшенный номер, Ngan Pho Studio & Hotel — отмечен тегом «сервисные апартаменты».",
  "https://www.trip.com/hotels/detail/?hotelId=38425094","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"точный район не указан в объявлении, данные со страницы поиска. Рейтинг 7.8/10 (2 отзыва)."}),

L(497,"da-nang","ns","Квартира",24370000,None,
  "Квартира в комплексе Minh Khang Apartments, ул. Trịnh Lỗi, район Ngũ Hành Sơn, ~3,6 км до пляжа Mỹ Khê.",
  "https://www.trip.com/hotels/detail/?hotelId=134807093","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"рейтинг 9.2/10. Есть варианты крупнее: сьют с балконом, семейный сьют 60 м², 2-спальная 85 м² — до 78$/ночь.","amenities":"бесплатная парковка, wifi, прачечная, лифт, кондиционер","policy":"возвратный депозит 1 000 000 ₫ при заселении"}),

L(498,"da-nang","hcg","Студия",17870000,20,
  "Студия Sunnie Apartment, район Hòa Cường.",
  "https://www.trip.com/hotels/detail/?hotelId=135531841","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"⚠ новый объект без отзывов; минимум удобств по описанию (wifi, лифт, видеонаблюдение). Дети не допускаются.","policy":"безвозвратное бронирование"}),

L(499,"da-nang","st","Студия",38200000,None,
  "Студия с балконом и видом, Golden View Resort Apartment.",
  "https://www.trip.com/hotels/detail/?hotelId=128510594","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"точный район не указан в объявлении, данные со страницы поиска. Рейтинг 10/10 (1 отзыв)."}),

L(500,"da-nang","st","Квартира",77190000,None,
  "Сьют с ванной, Draco Residence, район пляжа Mỹ Khê.",
  "https://www.trip.com/hotels/detail/?hotelId=134622342","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"рейтинг 7.8/10 (6 отзывов)"}),

L(501,"hoi-an","hat","Дом",12170000,None,
  "Вилла Ong Tam Tra Que, у деревни трав Trà Quế, запад Хойана.",
  "https://www.trip.com/hotels/detail/?hotelId=115830877","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"рейтинг 8.8/10, новый объект"}),

L(502,"hoi-an","ha","Комната",11770000,None,
  "Smart Garden Homestay, Хойан.",
  "https://www.trip.com/hotels/detail/?hotelId=130842745","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"точный район не указан в объявлении. Рейтинг 8.7/10 (40 отзывов)."}),

L(503,"hoi-an","ha","Дом",10660000,None,
  "My Anh Boutique Villa, Хойан.",
  "https://www.trip.com/hotels/detail/?hotelId=31410159","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"точный район не указан в объявлении. Рейтинг 8.8/10 (62 отзыва)."}),

L(504,"hoi-an","ha","Комната",12750000,None,
  "Terra Cotta Homestay, Хойан.",
  "https://www.trip.com/hotels/detail/?hotelId=9027264","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"точный район не указан в объявлении. Рейтинг 9.6/10 (4 отзыва)."}),

L(505,"hoi-an","hat","Дом",15620000,None,
  "Sam Retreat Hoi An Villa, среди рисовых полей на окраине города.",
  "https://www.trip.com/hotels/detail/?hotelId=108408250","проверено 15 авг",1,source="tripcom",
  details={"contract":"помесячно, цена Trip.com за 28 ночей","notice":"рейтинг 8.2/10 (19 отзывов)"}),
L(506,"nha-trang","vt","Квартира",19960000,70,
  "2-спальная квартира Napoleon Seaview Apartments, ул. Nguyễn Đình Chiểu, ~3,5 км до центра, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/ubuntu-napoleon-nha-trang-apartment.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей (скидка за длительное проживание уже применена)","notice":"рейтинг 7.5 «Хорошо» (160 отзывов)","amenities":"кухня, собственная ванная с биде, ТВ, холодильник, плита, балкон с видом на город, общая гостиная","policy":"бесплатная отмена"}),

L(507,"nha-trang","lt","Квартира",31370000,52,
  "1-спальная квартира Cozy GoldCoast Apartment, ул. Trần Hưng Đạo, район Lộc Thọ, 500 м до пляжа Nha Trang.",
  "https://www.booking.com/hotel/vn/cozy-gold-coast-nha-trang.ru.html","проверено 15 авг",1,source="booking",
  details={"deposit":"1 000 000 ₫ наличными при заселении (возвратный)","contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 8.9 «Хорошо» (27 отзывов). Оплата и депозит — только наличными.","amenities":"бар, вид на море, кухня с микроволновкой, прокат велосипедов, открытый бассейн","policy":"дешёвый тариф без возврата; более дорогие тарифы — с бесплатной отменой; животные не допускаются"}),

L(508,"nha-trang","lt","Квартира",42340000,35,
  "1-спальная квартира в комплексе Grands StarCity, 0,6 км до центра, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/grands-starcity.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.1 «Превосходно» (85 отзывов)","policy":"бесплатная отмена"}),

L(509,"nha-trang","lt","Квартира",15450000,30,
  "1-спальная квартира Laholm Hotel, 0,6 км до центра, на первой линии пляжа — самый бюджетный вариант подборки Booking.com.",
  "https://www.booking.com/hotel/vn/laholm-nha-trang.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 7.1 «Хорошо» (41 отзыв)","policy":"бесплатная отмена"}),

L(510,"nha-trang","vn","Квартира",26360000,68,
  "2-спальная квартира Sweet Homestay Sea View, ~4,1 км до центра, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/sweet-homestay-nha-trang.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 7.3 «Хорошо» (148 отзывов)","policy":"бесплатная отмена"}),

L(511,"da-lat","xh","Квартира",11240000,40,
  "1-спальная квартира CozyNook Boutique Apartments, ул. 3 tháng 2, 250 м до центра.",
  "https://www.booking.com/hotel/vn/cozynook-3-boutique-apartments.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.4 «Превосходно» (229 отзывов). Отопления нет почти ни у кого в Далате из-за прохладного климата — это норма, не недостаток.","amenities":"сад и терраса, прокат велосипедов и авто на месте, кухня (холодильник, микроволновка), быстрый wifi 128 Мбит/с","policy":"бесплатная отмена до 17.08.2026"}),

L(512,"da-lat","xh","Квартира",19230000,18,
  "1-спальная квартира Khách Sạn Căn Hộ XP, 100 м до центра.",
  "https://www.booking.com/hotel/vn/khach-san-can-ho-xp-da-lat.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"новый объект, отзывов пока нет"},
  ),

L(513,"da-lat","xh","Квартира",9830000,30,
  "1-спальная квартира All Be Condotel, 1,2 км до центра — самый бюджетный вариант подборки Booking.com в Далате.",
  "https://www.booking.com/hotel/vn/all-be-condotel.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг не показан на странице поиска","policy":"бесплатная отмена"}),

L(514,"da-lat","xh","Дом",26230000,60,
  "2-спальный дом Dalat Family House, 1,8 км до центра.",
  "https://www.booking.com/hotel/vn/dalat-family-house-thanh-pho-da-lat.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 8.5 «Хорошо» (123 отзыва)","policy":"бесплатная отмена"}),

L(515,"da-lat","xh","Студия",22580000,23,
  "Студия Feliz Dalat Homestay, 300 м до центра.",
  "https://www.booking.com/hotel/vn/dalat-feliz-home.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.6 «Превосходно» (444 отзыва) — один из самых высоко оценённых вариантов в подборке"}),

L(516,"da-nang","ah","Квартира",17790000,36,
  "1-спальные апартаменты ZENITH STAY by Lan's, ул. Ngô Quyền, 1,8 км до моста Rồng, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/zenith-stay-by-lans.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.8 «Превосходно» (15 отзывов) — гости отмечают быструю связь с хозяином и новое состояние жилья","amenities":"бесплатная частная парковка, пляжная зона, своя ванная, терраса, фен","policy":"бесплатная отмена до 19.08.2026"}),

L(517,"da-nang","ns","Квартира",12270000,35,
  "1-спальная квартира Papa Danang Beach Apartment, ~5,8 км до центра, 900 м до пляжа.",
  "https://www.booking.com/hotel/vn/papa-danang-beach-apartment.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 9.5 «Превосходно» (2 отзыва, новый объект)"}),

L(518,"da-nang","hc","Квартира",20660000,None,
  "1-спальная квартира с садом Sweet Garden Homestay, самый центр (0,8 км), район Hải Châu.",
  "https://www.booking.com/hotel/vn/sweet-garden-homestay-hai-chau.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 10 «Превосходно» (6 отзывов) — максимальная оценка в подборке Booking.com"}),

L(519,"da-nang","st","Квартира",15420000,27,
  "1-спальная квартира My Suites Danang Beach, ~2,6 км до центра, на первой линии пляжа.",
  "https://www.booking.com/hotel/vn/my-suites-danang-beach.ru.html","проверено 15 авг",1,source="booking",
  details={"contract":"помесячно, цена Booking.com за 30 ночей","notice":"рейтинг 7.7 «Хорошо» (113 отзывов)","policy":"бесплатная отмена"}),
L(520,"nha-trang","pl","Квартира",10000000,65,
  "Угловая 2-спальная квартира (2 с/у) с балконом в ЖК CT4 Hud, ул. 28, КГТ Phước Long, полностью меблирована, заезжай с чемоданом.",
  "https://www.facebook.com/marketplace/item/1491098622776266/","проверено 16 авг",1,source="fbmarketplace",
  details={"deposit":"2 месяца","notice":"⚠ на карточке FB отображается цена 1 000 000 ₫ — это баг ввода цены у продавца, в тексте описания указано 10 000 000 ₫/мес, используется цена из описания.","contact":"продавец Lê Đình Ngọc (на FB с 2018)"}),

L(521,"nha-trang","vt","Квартира",16000000,None,
  "3-спальная квартира (2 с/у) с видом на море в Napoleon Seaview Apartments, рядом с Университетом Нячанга, тихий охраняемый район, средний этаж.",
  "https://www.facebook.com/marketplace/item/1379138427501752/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"6-12 месяцев","deposit":"2 месяца","notice":"⚠ на карточке FB отображается цена 1 600 000 ₫ — баг ввода цены, в описании указано 16 000 000 ₫/мес. Тот же комплекс, что и объявление Booking.com (Napoleon Seaview Apartments).","contact":"продавец Phạm Quang Vinh (на FB с 2022)"}),

L(522,"nha-trang","vh","Квартира",14000000,68,
  "2-спальная квартира (2 с/у) + гостиная в ЖК Mường Thanh, ул. Trần Phú, в двух шагах от пляжа Hòn Chồng, высокий этаж с видом на море.",
  "https://www.facebook.com/marketplace/item/1765831987748168/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"6-12 месяцев","notice":"⚠ на карточке FB отображается цена 1 400 000 ₫ — баг ввода цены, в описании указано 14 000 000 ₫/мес.","contact":"продавец Phạm Quang Vinh (тот же, что и предыдущее объявление)"}),

L(523,"nha-trang","pl","Дом",7000000,None,
  "Шопхаус (2 спальни, первый этаж под коммерцию) на красной линии ул. B5, КГТ Vĩnh Điềm Trung — +500 тыс ₫/мес, если нужен кондиционер.",
  "https://www.facebook.com/marketplace/item/1358002595906876/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"договор на 2 года","notice":"Vĩnh Điềm Trung формально не входит в 12 центральных фан/районов Нячанга — район отмечен ориентировочно (ближайший — Phước Long), уточняйте точное расположение у продавца.","contact":"продавец Trần Nga (на FB с 2016)"}),

L(524,"nha-trang","vh","Студия",8500000,30,
  "Студия NVS-101 (первый этаж, отдельный вход) на ул. Ngô Văn Sở, район Vĩnh Hòa, север города, рядом с пляжем, доступна с 19 августа.",
  "https://www.facebook.com/marketplace/item/1831682444660681/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"3-6 месяцев","notice":"свет 5 000 ₫/кВт·ч, вода 100 000 ₫/чел. Разрешено с животными.","amenities":"своя стиральная машина, балкон с видом на горы","contact":"продавец Út Tiên (на FB с 2012)"}),

L(525,"nha-trang","vp","Дом",20000000,120,
  "Дом на красной линии (первый этаж + 2 верхних, 8 комнат, 4 с/у, фасад 4,5 м) под офис/шоурум/учебный центр, рядом с Hòn Chồng и Mường Thanh Viễn Triều.",
  "https://www.facebook.com/marketplace/item/1318995706466092/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 2 000 000 ₫ — баг ввода цены, в описании указано 20 000 000 ₫/мес. Формат — коммерческая недвижимость, а не обычное жильё.","contact":"продавец Thuhien Tranthi (на FB с 2012)"}),

L(526,"nha-trang","lt","Квартира",15000000,51,
  "Меблированная квартира с видом на море в Gold Coast, район Lộc Thọ.",
  "https://www.facebook.com/marketplace/item/1702036000907446/","проверено 16 авг",1,source="fbmarketplace",
  details={"deposit":"2 месяца","notice":"⚠ на карточке FB отображается цена 1 500 000 ₫ — баг ввода цены, в описании указано 15 000 000 ₫/мес. Тот же комплекс Gold Coast, что и объявление Booking.com.","contact":"продавец Lê Đình Ngọc (тот же, что и объявление №520)"}),

L(527,"da-lat","lv","Квартира",19000000,150,
  "3-спальная квартира (2 с/у) с парной, ул. Nguyễn Đình Chiểu, рядом с площадью Lâm Viên и Университетом Далата, 3 мин до озера Xuân Hương.",
  "https://www.facebook.com/marketplace/item/921137010467937/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"6-12 месяцев","notice":"продавец — новый аккаунт на FB (2026 год), доп. проверка не помешает","contact":"продавец Hương Mai"}),

L(528,"da-lat","xh","Дом",5000000,20,
  "3 смежных таунхауса (~20 м² + мансарда каждый, 1 спальня/1 с/у) в Ан Тон, район Xuân Hương Mới — часть ещё в отделке. Подходит под долгосрочное жильё, хоумстей или small business.",
  "https://www.facebook.com/marketplace/item/1702699750842770/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"от 1 года","notice":"3 отдельных юнита по цене 5 / 6 / 7 млн ₫ в месяц соответственно — указана цена самого дешёвого.","contact":"продавец Nhà Đất Đà Lạt (на FB с 2022)"}),

L(529,"da-lat","xh","Дом",5000000,120,
  "Отдельный дом (гостиная + кухня + 1 спальня/1 с/у + двор), без мебели, ул. Mê Linh, Phường 9, рядом с Bách Hóa Xanh и спортзалом, 10 мин до озера Xuân Hương.",
  "https://www.facebook.com/marketplace/item/1372181211516644/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"минимум 1 год","contact":"продавец Hương Mai (та же, что и объявление №527)"}),

L(530,"da-lat","lv","Комната",15750000,None,
  "Номер в формате resort-living с видом на сосны — wifi, уборка 2 раза в неделю, парковка, вода включена, ресторан на территории, свет отдельно. Рассчитано на экспатов и удалёнщиков.",
  "https://www.facebook.com/marketplace/item/1052881520557817/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"минимум 6 месяцев, депозит 1 месяц, оплата раз в 2 месяца вперёд","notice":"точный район не указан в объявлении, данные со страницы поиска","contact":"продавец Samsara Lê (на FB с 2025)"}),

L(531,"da-lat","xh","Квартира",15000000,60,
  "2-спальная квартира (1 с/у) с балконом и видом, полностью меблирована, Phường 6, рядом с Bách Hóa Xanh и школой Lam Sơn, 2,5 км до Ночного рынка.",
  "https://www.facebook.com/marketplace/item/1379400014146019/","проверено 16 авг",1,source="fbmarketplace",
  details={"contract":"6-12 месяцев","notice":"⚠ на карточке FB отображается цена 1 500 000 ₫ — баг ввода цены, в описании указано 15 000 000 ₫/мес.","contact":"продавец Ngân Go Home (на FB с 2025)"}),

L(532,"nha-trang","vn","Дом",25000000,100,
  "Новый дом на 3 спальни/4 с/у с двором, район Vĩnh Thái / КГТ Mỹ Gia, юг города.",
  "https://www.facebook.com/marketplace/item/1335062435448184/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на FB объявление помечено тегом «Đà Lạt, Lâm Đồng», но в самом тексте описания указаны Vĩnh Thái и КГТ Mỹ Gia — это реальные районы Нячанга, а не Далата. Похоже на неверную привязку города продавцом; в подборке отнесено к Нячангу по содержанию объявления. На карточке FB отображается цена 2 500 000 ₫ — баг ввода цены, в описании указано 25 000 000 ₫/мес.","contact":"продавец Ngan Hong Pham (на FB с 2018, высокий рейтинг)"}),

L(533,"da-nang","cl2","Комната",4000000,25,
  "Комната (269 кв. фут, ~20 м² без балкона) по адресу 16A-18A Nguyễn Quý Đức, Khuê Trung, Cẩm Lệ, рядом с мостом Nguyễn Tri Phương, новое 4-этажное здание с лифтом и электронными воротами.",
  "https://www.facebook.com/marketplace/item/1057757783316746/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"кондиционер, отопление, прачечная, парковка","notice":"цена варьируется 4-5 млн ₫ в зависимости от типа комнаты; только долгосрочным арендаторам","contact":"продавец Homebird Apt (на FB с 2026)"}),

L(534,"da-nang","hx","Квартира",7500000,None,
  "1-спальная квартира (1 с/у) в престижном комплексе, ул. Nguyễn Hiến Lê, район Hòa Cường, полностью меблирована (диван, обеденная группа, бельё), своя стиральная машина, кондиционер в гостиной и спальне.",
  "https://www.facebook.com/marketplace/item/911416194738049/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"доступна для заселения сейчас","contact":"продавец Võ Thị Thảo Nguyên (на FB с 2021)"}),

L(535,"da-nang","tk","Квартира",7000000,None,
  "Новая квартира в центре района Thanh Khê, ул. Hà Huy Tập, рядом с Aeon Mall, Coopmart, университетом Duy Tân, полная меблировка, отдельная прачечная, просторный балкон.",
  "https://www.facebook.com/marketplace/item/1576504187188353/","проверено 16 авг",1,source="fbmarketplace",
  details={"contact":"продавец Nguyen Huyen (на FB с 2022)"}),

L(536,"da-nang","tk","Квартира",7500000,None,
  "Полностью меблированная квартира с оборудованной кухней, ул. Điện Biên Phủ, район Thanh Khê.",
  "https://www.facebook.com/marketplace/item/1811352036957325/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"цена договорная","contact":"продавец Nguyễn Thị Mỹ Diệu (на FB с 2026)"}),

L(537,"da-nang","lc","Квартира",4000000,35,
  "Квартира 35 м² на ул. Âu Cơ, район Liên Chiểu.",
  "https://www.facebook.com/marketplace/item/1014448794912255/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на FB объявление помечено категорией «Quận Cẩm Lệ», но в тексте описания указана улица Âu Cơ в Liên Chiểu — расхождение между тегом и текстом, в подборке отнесено к Liên Chiểu по содержанию описания. Само описание минимальное, деталей мало.","contact":"продавец Trần Uyên (на FB с 2010)"}),

L(538,"hoi-an","ha","Квартира",14000000,None,
  "2-спальная квартира F Home, полностью меблирована.",
  "https://www.facebook.com/marketplace/item/1089695737060971/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 1 400 000 ₫ — баг ввода цены, в описании указано 14 000 000 ₫/мес. Объявление всплыло в выдаче по Дананга (радиус поиска 65 км), но фактически находится в Хойане (~30 км от центра Дананга) — в подборке отнесено к Хойану.","contact":"продавец Quyên Lê (на FB с 2015)"}),
L(539,"da-nang","ns","Квартира",7000000,40,
  "1-спальная квартира (1 с/у) в An Thượng 18, район Mỹ An, рядом с Torina Restaurant & Bakery, 1 мин на байке / 10 мин пешком до пляжа Mỹ Khê.",
  "https://www.facebook.com/marketplace/item/228701932045345/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"2 кондиционера, скоростной wifi, смарт-ТВ, полная кухня, своя стиральная машина, видеонаблюдение, паркинг в цоколе, лифт, кофейня и крыша в здании, уборка 2 раза/нед","electricity":"3 500 ₫/кВт·ч","water":"50 000 ₫/чел.","notice":"цена и все условия включены в аренду, кроме света и воды","contact":"facebook.com/DanangApartmentRentals, тел. 077 955 0817 / 056 391 9736, Zalo 078 566 8719"}),

L(540,"da-nang","st","Студия",5900000,None,
  "Меблированная студия в районе Sơn Trà, рядом с пляжем Phước Mỹ, вид из окна.",
  "https://www.facebook.com/marketplace/item/858766315655085/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"доступ к бассейну","notice":"локация на карте — ориентировочная метка, точный адрес не указан; контакты продавца скрыты без входа в FB"}),

L(541,"da-nang","st","Квартира",8000000,37,
  "Квартира на 21 этаже в Wyndham Golden Bay Da Nang, ул. Lê Văn Duyệt, район Nại Hiên Đông, Sơn Trà.",
  "https://www.facebook.com/marketplace/item/1241672263555919/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"инфинити-бассейн с позолотой, ресторан, бар, казино, конференц-зал, супермаркет, спортзал, охрана 24/7, рядом парк «7 Wonders»","notice":"контакты продавца скрыты без входа в FB"}),

L(542,"da-nang","st","Квартира",5500000,None,
  "1-спальная квартира на ул. Dương Tử Quan, район Sơn Trà, большой балкон с видом на море и город.",
  "https://www.facebook.com/marketplace/item/302415622710644/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 5 000 ₫ — баг ввода цены, в описании указано 5,5 млн ₫/мес. Контакты продавца скрыты без входа в FB (предлагает Zalo/WhatsApp/Messenger)."}),

L(543,"da-nang","st","Квартира",16000000,67,
  "Угловая 2-спальная квартира (2 с/у) в Hiyori Garden Tower, Sơn Trà, вид на мост Dragon Bridge из спальни, 700 м до пляжа Mỹ Khê, 100 м до моста.",
  "https://www.facebook.com/marketplace/item/997903025322091/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"полностью меблирована, бассейн, спортзал, паркинг, охрана 24/7, лобби","notice":"⚠ на карточке FB отображается цена 16 000 ₫ — баг ввода цены, в описании указано 16 млн ₫/мес (≈630 USD) с учётом сервисного сбора.","contact":"+84 931 914 941 (iMessage/звонок/Zalo/Viber/WhatsApp/KakaoTalk)"}),

L(544,"da-nang","st","Квартира",17000000,70,
  "Угловая 2-спальная квартира (2 с/у) в Sam Towers (Risemount Apartment Đà Nẵng), Sơn Trà, у реки, вид на реку Хан.",
  "https://www.facebook.com/marketplace/item/330540726796895/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"мебель высокого класса, гостиная, кухня, балкон, ресторан, кафе, инфинити-бассейн, спортзал, мини-маркет, ресепшн, охрана","notice":"⚠ на карточке FB отображается цена 17 ₫ — баг ввода цены, в описании указан диапазон 17-25 млн ₫/мес в зависимости от юнита, использована нижняя граница. Тот же продавец (Ms. Hiền, +84 931 914 941), что и предыдущее объявление — похоже, агент по нескольким комплексам.","contact":"Ms. Hiền, +84 931 914 941"}),

L(545,"da-nang","hc","Квартира",17000000,65,
  "Отдельная 1-спальная комната/квартира 65 м² на ул. Bạch Đằng, район Hải Châu, рядом с мостами Han River Bridge и Dragon Bridge, полностью меблирована, бассейн, спортзал, большой балкон.",
  "https://www.facebook.com/marketplace/item/1853075222160688/","проверено 16 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена не указана (0 ₫), в описании — 17 млн ₫/мес, использована цена из описания. Метка на карте объявления показывает район Ngũ Hành Sơn, но текст описания прямо называет Bạch Đằng/Hải Châu — расхождение между меткой и текстом, в подборке отнесено к Hải Châu по содержанию описания.","contact":"Mr. Tâm, 0395736699 (Zalo)"}),

L(546,"da-nang","hc","Квартира",38000000,None,
  "Люксовая 2-спальная квартира в The Filmore, район Hải Châu, панорамный вид на город и реку, окна в пол.",
  "https://www.facebook.com/marketplace/item/1068616929196867/","проверено 16 авг",1,source="fbmarketplace",
  details={"amenities":"холодильник Toshiba, стиральная машина LG ThinQ с фронтальной загрузкой, центральный кондиционер, обеденная группа, встроенные шкафы; в аренду включены сервисный сбор здания и скоростной wifi","notice":"⚠ дорогой люксовый вариант (≈1500 USD/мес). Продавец не заполнил номер телефона в объявлении (поле буквально гласит «(Insert your phone number)») — связаться можно только через Messenger по ссылке на объявление."}),
L(547,"ho-chi-minh","tm","Квартира",137000000,191,
  "Пентхаус в The Ascentia, 3 спальни/2 с/у, высокий этаж, ул. Nguyễn Lương Bằng. Объявление таргетировано на корейских экспатов (текст на корейском+вьетнамском).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133864284.htm","2 недели назад",17,source="chotot",
  details={"contact":"Annie (агент, 22 объявления)"}),

L(548,"ho-chi-minh","tm","Квартира",20000000,48,
  "1-спальная квартира (1 с/у), новая, ещё никто не жил. Привязана к проекту The Ascentia, ул. Nguyễn Lương Bằng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133101148.htm","6 дней назад",6,source="chotot",
  details={"notice":"⚠ в тексте само здание названо «The Aurora», а не Ascentia — либо ошибочная привязка к проекту на сайте, либо неофициальное имя одного из корпусов комплекса.","contact":"Homes With Tran / Ms Trân (10 объявлений)"}),

L(549,"ho-chi-minh","tm","Квартира",30000000,78,
  "2-спальная квартира в Midtown M8 «The Peak», Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134111789.htm","4 дня назад",4,source="chotot",
  details={}),

L(550,"ho-chi-minh","th","Квартира",15000000,72,
  "2-спальная квартира с террасой-садом в SkyGarden, ул. Phạm Văn Nghị, полностью меблирована.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134178964.htm","4 часа назад",1,source="chotot",
  details={"contact":"агент «MẶT BẰNG KINH DOANH Q7» (11 объявлений)"}),

L(551,"ho-chi-minh","th","Квартира",12000000,60,
  "2-спальная квартира в Sunrise Riverside, рядом университеты RMIT и TDTU, ул. Nguyễn Hữu Thọ.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/127916052.htm","10 часов назад",1,source="chotot",
  details={"contact":"Nguyễn Phúc Vinh (8 объявлений)"}),

L(552,"ho-chi-minh","th","Студия",8000000,30,
  "Студия с балконом (мини-сервисная квартира), центр Phú Mỹ Hưng, Hưng Gia 1.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/132121797.htm","3 часа назад",1,source="chotot",
  details={"contact":"Lộc Trần (3 объявления)"}),

L(553,"ho-chi-minh","th","Студия",6800000,35,
  "Новостройка рядом с Lotte Mart, Phú Mỹ Hưng, у моста Kênh Tẻ, ул. Số 39.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/132601227.htm","14 часов назад",1,source="chotot",
  details={"contact":"Đạt Nguyễn (10 объявлений)"}),

L(554,"ho-chi-minh","th","Студия",6100000,40,
  "Новая комната рядом с Crescent Mall / Lotte Mart / SC VivoCity, ул. Nguyễn Thị Thập.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/124520795.htm","2 часа назад",1,source="chotot",
  details={"contact":"агент «Thuận Hình Thật Giá Thật» (21 объявление)"}),

L(555,"ho-chi-minh","th","Студия",5700000,35,
  "Студия рядом с Lotte Mart и рынком Tân Quy, ул. Số 77.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/132261723.htm","вчера",1,source="chotot",
  details={"contact":"Ken Unitegroup (3 объявления)"}),

L(556,"ho-chi-minh","ak","Квартира",23000000,76,
  "2-спальная квартира в Masteri Thảo Điền, аренда 1-3 спальных вариантов.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133910188.htm","несколько дней назад",5,source="chotot",
  details={"contact":"Thu Hoài (4 объявления)"}),

L(557,"ho-chi-minh","ak","Квартира",22000000,75,
  "2-спальная квартира в Masteri Thảo Điền.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134058835.htm","несколько дней назад",5,source="chotot",
  details={"contact":"Thời Phạm Moji (3 объявления)"}),

L(558,"ho-chi-minh","ak","Квартира",18000000,75,
  "2-спальная квартира 75 м² в Masteri Thảo Điền.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133760467.htm","8 часов назад",1,source="chotot",
  details={"contact":"Trang Gun (2 объявления)"}),

L(559,"ho-chi-minh","ak","Квартира",12000000,80,
  "Сервисная квартира (studio/1PN/2PN на выбор), рядом Tropic Garden, полностью новая.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133769076.htm","несколько дней назад",5,source="chotot",
  details={"contact":"агент «Cho Thuê Căn Hộ Quận 2» (12 объявлений)"}),

L(560,"ho-chi-minh","ak","Квартира",9500000,50,
  "1-спальная квартира высокого класса, ул. Quốc Hương, рядом мост Sài Gòn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/125996300.htm","12 часов назад",1,source="chotot",
  details={"contact":"Gia Thụy Bùi (14 объявлений)"}),

L(561,"ho-chi-minh","ak","Квартира",20000000,50,
  "1-спальная квартира высокого класса, ул. Tống Hữu Định. Спортзал, бассейн, сауна.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133867491.htm","1 час назад",1,source="chotot",
  details={"contact":"BĐS Minh Hiếu38 (18 объявлений)"}),

L(562,"ho-chi-minh","ak","Квартира",16000000,80,
  "Комплекс сервисных квартир (1PN/2PN на выбор), ул. Nguyễn Văn Hưởng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/122570645.htm","несколько дней назад",5,source="chotot",
  details={"contact":"агент «Cho Thuê Căn Hộ Quận 2» (12 объявлений)"}),

L(563,"ho-chi-minh","ak","Квартира",10000000,50,
  "Люксовая сервисная квартира (studio/1PN/2PN), бесплатно бассейн и спортзал, ул. Nguyễn Văn Hưởng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/132865963.htm","2 часа назад",1,source="chotot",
  details={"contact":"Bích Thảo (7 объявлений)"}),

L(564,"ho-chi-minh","ak","Квартира",19000000,93,
  "3-спальная квартира в De Capella, ближе к мосту Thủ Thiêm/Sài Gòn, чем к историческому центру Thảo Điền, но формально в границах An Khánh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133869798.htm","16 часов назад",1,source="chotot",
  details={"contact":"Steven Phan (1 объявление)"}),

L(565,"ho-chi-minh","ak","Квартира",24000000,83,
  "3-спальная квартира в башне Bali, New City Thủ Thiêm — ближе к Thủ Thiêm, чем к историческому Thảo Điền, но формально в границах An Khánh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134133813.htm","16 часов назад",1,source="chotot",
  details={"contact":"Anh Thi (1 объявление)"}),

L(566,"ho-chi-minh","ak","Квартира",14000000,40,
  "1-спальная сервисная квартира с балконом, «в Тхао Дьен», ул. Số 60.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134168215.htm","14 часов назад",1,source="chotot",
  details={"contact":"агент «Quý Nhà Phố BDS» (27 объявлений)"}),

L(567,"ho-chi-minh","bq","Квартира",10500000,80,
  "2-спальная квартира (2 с/у), «супер-вид», ул. Bình Quới, Thanh Đa.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-binh-thanh-tp-ho-chi-minh/134173532.htm","9 часов назад",1,source="chotot",
  details={"contact":"Nguyễn Khang (1 объявление)"}),

L(568,"ho-chi-minh","bq","Комната",11900000,42,
  "1-спальная сервисная квартира, полная мебель, широкие окна и балкон, ул. Thanh Đa.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-binh-thanh-tp-ho-chi-minh/133976775.htm","2 недели назад",14,source="chotot",
  details={"contact":"агент «Công Danh Apartment» (28 объявлений)"}),

L(569,"ho-chi-minh","bq","Студия",5700000,35,
  "Студия с балконом, полная мебель, рядом университеты, ул. Bình Quới.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-binh-thanh-tp-ho-chi-minh/133897084.htm","2 недели назад",14,source="chotot",
  details={"contact":"агент «Dương An Apartment» (21 объявление)"}),

L(570,"ho-chi-minh","bq","Квартира",21000000,130,
  "3-спальная квартира 130 м² в комплексе Thanh Đa View, полная мебель, «срочно сдаётся».",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-binh-thanh-tp-ho-chi-minh/133691094.htm","4 недели назад",28,source="chotot",
  details={"contact":"Trần Ngọc Nhiễm (8 объявлений)"}),


L(573,"ho-chi-minh","tm","Квартира",27000000,80,
  "2-спальная квартира (2 с/у) в The Ascentia, полная мебель, окна на восток. Рядом Công viên Ánh Sao, Sakura Park, Winmart+.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-phuong-tan-phu-19-the-ascentia-phu-my-hung/cho-cc-2pn-2wc-80m2-tai-nha-ep-nhu-hinh-pr46165843","5 дней назад",5,source="batdongsan",
  details={"amenities":"242 квартиры в комплексе (1-3PN + дуплексы), бассейны, спортзал, йога, сауна, сад на крыше","contact":"Nhật Huy, 0989 920 ***"}),

L(574,"ho-chi-minh","tm","Квартира",35000000,107,
  "3-спальная квартира (2 с/у) в The Ascentia, вид на виллы (Chateau, Midtown), 10-15 мин до Q1/Q2/Q4. Полная премиум-мебель.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-phuong-tan-phu-19-the-ascentia-phu-my-hung/cho-ascentina-3pn-full-noi-that-view-biet-thu-lh-van-anh-pr43320826","вчера",1,source="batdongsan",
  details={"amenities":"рядом парк Sakura, школы SSIS/Canadian/Japanese","contact":"Văn Anh, 0849 160 ***"}),


L(576,"ho-chi-minh","th","Квартира",22000000,87,
  "3-спальная квартира (2 с/у), ядро Phú Mỹ Hưng, рядом Crescent Mall, международные школы, финансовый квартал, SECC. Импортная мебель.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-tan-phong-9-phu-my-hung/cho-cao-cap-ngay-crescent-mall-87m2-3pn-2wc-noi-that-moi-tinh-o-ngay-pr46180136","2 дня назад",2,source="batdongsan",
  details={"contact":"агентство Green House (4 офиса в PMH)"}),

L(577,"ho-chi-minh","th","Квартира",30000000,98,
  "3-спальная квартира (2 с/у) у моста Cầu Ánh Sao, 5 мин до рынка Tân Mỹ, импортная премиум-мебель.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-tan-phong-9-phu-my-hung/cho-cao-cap-cau-anh-sao-98m2-3pn-2wc-noi-that-cao-cap-nhap-khau-o-ngay-pr46168150","5 дней назад",5,source="batdongsan",
  details={"contact":"Green House, Ngọc Hân, 0773 962 ***"}),

L(578,"ho-chi-minh","th","Квартира",23000000,110,
  "3-спальная квартира (2 с/у) на главной улице Nguyễn Đức Cảnh, рядом школа SSIS. Мебель полная или базовая на выбор.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-tan-phong-9-phu-my-hung/chuyen-cho-110m2-3-ngu-ke-ben-truong-ssis-lh-em-huong-pr46166277","5 дней назад",5,source="batdongsan",
  details={"contact":"Nguyễn Hường (специалист по аренде в PMH), 0919 949 ***"}),

L(579,"ho-chi-minh","tm","Квартира",12000000,88,
  "Belleza Apartment, 2-спальная угловая квартира (2 с/у), свежий ремонт, не хватает части бытовой техники.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-pham-huu-lau-phuong-phu-my-9-belleza-apartment/cho-q7-88m2-2pn-2wc-noi-that-gan-u-gia-12tr-10-8-o-uoc-pr46067134","5 дней назад",5,source="batdongsan",
  details={"deposit":"2 месяца","contact":"Nguyễn Thị Hưng"}),

L(580,"ho-chi-minh","tm","Квартира",11500000,70,
  "Q7 Boulevard, 2-спальная квартира (2 с/у), 15 мин до PMH/SC VivoCity/RMIT, 10 мин до Crescent Mall/Lotte Mart.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-phuong-phu-my-9-q7-boulevard/gio-hang-cho-chon-loc-re-ep-sach-se-view-ep-thoang-yen-tinh-pr45661907","11 дней назад",11,source="batdongsan",
  details={"notice":"агентство NewHouse (офис B1.OF.14 прямо в здании) предлагает помощь с ВНЖ/визой арендаторам","contact":"Chí Tiền, 0963 214 ***"}),

L(581,"ho-chi-minh","ak","Квартира",25000000,50,
  "1-спальная квартира (1 с/у), ул. Võ Trường Toản, Thảo Điền, полная мебель, торг возможен.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-truong-toan-phuong-thao-dien-q2-thao-dien/ien-cho-1pn-full-nt-gia-25-trieu-thang-con-thuong-luong-pr45991617","11 дней назад",11,source="batdongsan",
  details={"contact":"Phúc Nguyễn, 0903 933 ***"}),

L(582,"ho-chi-minh","ak","Квартира",33000000,72,
  "2-спальная квартира (2 с/у), башня T2, отдельный лифтовой холл на этаж (приватность), 100% новая мебель, инфинити-бассейн, спортзал на крыше, библиотека.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-truong-toan-phuong-thao-dien-q2-thao-dien/cho-2pn-full-nt-hiem-ien-loi-thang-may-rieng-yen-tinh-pr45876268","3 дня назад",3,source="batdongsan",
  details={"contact":"Nhất Thạch, 0932 641 ***"}),

L(583,"ho-chi-minh","ak","Квартира",45000000,112,
  "3-спальная квартира (2 с/у) в ЖК Fraser, вид на реку, от собственника напрямую.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-truong-toan-phuong-thao-dien-q2-thao-dien/cho-3pn-ien-full-noi-that-view-song-chi-45-trieu-pr46064002","опубл. 18.07.26",30,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления — 17.08.26 (истекает буквально на днях от момента проверки)","contact":"собственник Nguyễn Thành Định, 0708 248 ***"}),

L(584,"ho-chi-minh","ak","Квартира",140000000,182,
  "Люкс-сегмент: 4-спальная квартира (3 с/у), 32-этажная башня застройщика Frasers Centrepoint (Сингапур), 300 квартир + 100+ сервисных апартаментов, вид на реку.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-truong-toan-phuong-thao-dien-q2-thao-dien/duy-nhat-4pn-3wc-182m2-140tr-thang-bao-khong-noi-that-tang-cao-view-song-xem-nha-24-7-pr46175001","3 дня назад",3,source="batdongsan",
  details={"notice":"без мебели («bao không nội thất»), топ-сегмент цен для ориентира","amenities":"рядом парки Thảo Điền/An Phú, госпиталь AIH, международные школы","contact":"Lê Thanh Tuấn, 0931 219 ***"}),

L(585,"ho-chi-minh","ak","Квартира",16000000,55,
  "Masteri Thảo Điền, самая большая 1-спальная планировка в комплексе, вид на Landmark 81, смарт-ТВ, полная кухонная техника.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-xa-lo-ha-noi-phuong-thao-dien-masteri-thao-dien/cho-1pn-re-nhat-co-ban-cong-pr39203415","6 дней назад",6,source="batdongsan",
  details={"amenities":"бесплатно бассейн/зал/BBQ/парк, рядом Vincom Mega Mall","contact":"Hoàng Phong"}),

L(586,"ho-chi-minh","ak","Квартира",18000000,70,
  "Masteri Thảo Điền, 2-спальная квартира (2 с/у), полная мебель, у того же агента широкий выбор планировок 1-4PN.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-xa-lo-ha-noi-phuong-thao-dien-masteri-thao-dien/gia-cuc-tot-cho-2-phong-ngu-tai-ien-chi-tu-18-trieu-pr46079479","опубл. 22.07.26",25,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа — 21.08.26 (через несколько дней от момента проверки)","contact":"Dư Huyền, 0943 707 ***"}),

L(587,"ho-chi-minh","btr","Квартира",26000000,89,
  "Estella Heights, 2-спальная квартира (2 с/у), ул. Song Hành. У агента полный прайс-лист здания (1PN от 22 до 4PN за 90-128 млн). Управление — Savills.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-song-hanh-phuong-an-phu-estella-heights/toan-bo-cho-thang-01-2026-chinh-chu-khong-gia-ao-lh-pr44943253","5 дней назад",5,source="batdongsan",
  details={"notice":"формально это Phường Bình Trưng (соседняя с An Khánh/Thảo Điền), не путать с историческим центром Thảo Điền","fees":"обслуживание 23 500 ₫/м²/мес, паркинг авто 1 080 000 ₫/мес, мотобайк 162 000 ₫/мес","amenities":"pet-friendly, помощь с временной регистрацией и налогами","contact":"Phan Thanh Trí Tâm, +8490 987 8***"}),

L(588,"ho-chi-minh","btr","Квартира",16000000,80,
  "Palm Heights, 2-спальная квартира (2 с/у), застройщик Keppel Land + Tiến Phước/Trần Thái, 3 башни по 34 этажа, 816 квартир вдоль рек. 8 км до Q1.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-song-hanh-phuong-an-phu-palm-heights/xanh-tai-cao-cap-cho-ngay-hom-nay-pr43626987","2 дня назад",2,source="batdongsan",
  details={"notice":"формально это Phường Bình Trưng, не An Khánh","amenities":"рядом Vincom Mega Mall/Estella Place","contact":"Ngô Hoàng Hiệp (говорит по-английски), 0375 786 ***"}),

L(589,"ho-chi-minh","ak","Квартира",35000000,77,
  "Lumière Riverside, 2-спальная квартира (2 с/у), вид на реку Сайгон, высокий этаж, широкий балкон.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-nguyen-giap-phuong-an-phu-lumiere-riverside/2pn-gia-35-trieu-thang-view-song-full-noi-that-cao-cap-pr46059606","вчера",1,source="batdongsan",
  details={"notice":"офис агента прямо на территории ЖК; у агента полный прайс здания (1PN от 25 млн, 3PN от 50 млн)","contact":"Yến Lumiere, 0986 581 ***"}),



L(592,"ho-chi-minh","bq","Квартира",21000000,120,
  "Thanh Đa View, 3-спальная квартира (2 с/у), рядом мост Thanh Đa и рынок, бассейн, спортзал, магазин у дома, вид на реку Сайгон.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-thanh-da-phuong-27-thanh-da-view/cho-3pn-a-so-7-a-p-27-quan-binh-dien-pr46066498","опубл. 04.08.26",13,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления — 14.08.26 (пару дней назад)","contact":"Nguyễn Tấn Huy, 0937 833 ***"}),


L(594,"ho-chi-minh","bq","Комната",4200000,40,
  "Отдельная комната-лофт на 2-4 человек, кондиционер, шкаф, своя зона стирки/сушки, охрана 24/7, рядом университет Hutech — больше подходит студентам, чем удалёнщикам.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-thanh-da-phuong-27-66/khai-truong-gac-cao-ung-uoc-ay-u-noi-that-o-2-4-nguoi-gan-hutech-khu-u-gtvt-ngoai-thuong-pr46069905","опубл. 20.07.26",28,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления — 04.08.26","contact":"агент Quỳnh Hương Uni"}),


L(597,"ho-chi-minh","th","Квартира",27000000,124,
  "3-спальная квартира в ЖК Nam Khang, рядом школа BCIS, Нам Сайгон.",
  "https://www.facebook.com/marketplace/item/1188672412601724/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 2 700 000 ₫ — баг ввода цены, в описании указано ~1100$ (≈27 млн ₫/мес).","amenities":"машиноместо","contact":"em Hùng, 0979555019"}),

L(598,"ho-chi-minh","tm","Квартира",70000000,125,
  "3-спальная квартира (2 с/у) с видом на реку, Hồ Bán Nguyệt, Phú Mỹ Hưng.",
  "https://www.facebook.com/marketplace/item/3579590115526281/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 7 000 000 ₫ — баг ввода цены ровно в 10 раз, в описании указано 70 млн ₫/мес.","amenities":"полная меблировка, 4 подземных паркинга, бассейн, спортзал, рядом шопхаусы","contact":"Mai Nguyễn"}),

L(599,"ho-chi-minh","tm","Квартира",27000000,84,
  "2-спальная квартира (2 с/у) в The Ascentia, вид на ул. Nguyễn Lương Bằng, цена договорная.",
  "https://www.facebook.com/marketplace/item/1915299205818961/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 27 000 ₫ — тот же баг округления, в описании 27 млн ₫/мес.","contact":"Đỗ Thủy"}),

L(600,"ho-chi-minh","tm","Квартира",40000000,None,
  "Угловая 3-спальная квартира (2 с/у) в The Ascentia, полная меблировка, 1 машиноместо.",
  "https://www.facebook.com/marketplace/item/1289312213382216/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 40 000 ₫, в описании 40 млн ₫/мес."}),

L(601,"ho-chi-minh","tm","Квартира",28000000,None,
  "2-спальная квартира (2 с/у) в The Ascentia, средний этаж, полная меблировка.",
  "https://www.facebook.com/marketplace/item/2074602626776916/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 28 000 ₫, в описании 28 млн ₫/мес («net price»).","amenities":"бассейн Oasis, джакузи, спортзал, рядом международные школы и банки","contact":"Hoang"}),

L(602,"ho-chi-minh","ak","Квартира",33000000,None,
  "Пентхаус, 2 спальни, собственная просторная терраса на крыше, ул. Nguyễn Thị Định, рядом An Phú, Thảo Điền, Thủ Thiêm, метро An Phú.",
  "https://www.facebook.com/marketplace/item/1364525298528370/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 33 ₫, в описании 33 млн ₫/мес. Свободна с 18.08.","amenities":"полная меблировка, можно с животными, уборка 2 раза/нед","contact":"Cảnh Kiều"}),

L(603,"ho-chi-minh","ak","Квартира",30000000,115,
  "Угловая 2-спальная квартира в Thảo Điền Pearl, свободна с 1 сентября.",
  "https://www.facebook.com/marketplace/item/1051717207346683/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"цена на карточке и в описании совпадают — редкий случай без расхождения."}),

L(604,"ho-chi-minh","ak","Квартира",25000000,140,
  "3-спальная квартира в ЖК Fideco, Thảo Điền.",
  "https://www.facebook.com/marketplace/item/1378751054224604/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 25 000 ₫, в описании 25 млн ₫/мес."}),

L(605,"ho-chi-minh","bq","Квартира",14000000,None,
  "2-спальная квартира (можно перегородить на 3), первый этаж, кооперативный дом («cư xá») Thanh Đa.",
  "https://www.facebook.com/marketplace/item/2784338871929282/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 14 000 ₫, в описании 14 млн ₫/мес. Метка местоположения на FB ошибочно показывала «Quận 3».","contact":"Chi"}),

L(606,"ho-chi-minh","bq","Квартира",21000000,120,
  "Угловая 3-спальная квартира (2 с/у) в комплексе Thanh Đa View №7, у моста Thanh Đa, напротив рынка, вид на реку Сайгон.",
  "https://www.facebook.com/marketplace/item/1578595263909443/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 21 000 ₫, в описании 21 млн ₫/мес.","amenities":"бассейн, спортзал, мини-маркет","contact":"Tấn Huy"}),

L(607,"ho-chi-minh","bq","Квартира",21000000,130,
  "3-спальная квартира (2 с/у) в охраняемом комплексе Thanh Đa View, бассейн, бесплатный спортзал, супермаркет.",
  "https://www.facebook.com/marketplace/item/1330550035468360/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 1 ₫ (баг), в описании указано «21TR» (21 млн ₫/мес)."}),

L(608,"ho-chi-minh","bq","Дом",8000000,100,
  "Отдельный 3-этажный дом, 3 спальни/3 с/у, точный адрес 28/3 Thanh Đa (район «Cháo Vịt»), рядом вузы (HUTECH, ГТВТ, Ngoại Thương, Văn Lang), рынок ~100м.",
  "https://www.facebook.com/marketplace/item/1552697653227922/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"цена на карточке и в описании совпадают.","contact":"Mr. Đức, 0903.67.0123"}),

L(609,"ho-chi-minh","tm","Квартира",30000000,84,
  "2-спальная квартира (2 с/у), The Ascentia, найдена через агентство VN Space (офисы Phú Mỹ Hưng и An Phú), торг возможен.",
  "https://www.facebook.com/vnspacehcm/posts/2br-fully-furnished-apartment-the-ascentia-phu-my-hung-dist-72-bedrooms-2-bathro/1511976834266386/","проверено 17 авг",1,source="facebook",
  details={"notice":"цена указана $1200/мес, переведено по курсу ~25000. Полная меблировка.","amenities":"бассейн, фитнес, йога-комната, детская площадка, сауна","contact":"агентство VN Space, офис PMH +84 28 5412 1570, офис An Phú +84 28 3740 6177"}),

L(610,"ho-chi-minh","ak","Квартира",22000000,None,
  "2-спальная квартира в Masteri Thảo Điền, современный ремонт.",
  "https://www.facebook.com/groups/1939999392801882/posts/masteri-thao-dien-2-bedroom-apartment-for-rent-ho-chi-minh-city-apartment-for-re/3747635085371628/","проверено 17 авг",1,source="facebook",
  details={"notice":"площадь и контакты не удалось подтвердить — карточка группы за логин-стеной Facebook, известна только цена и общее описание."}),
L(611,"ho-chi-minh","ak","Квартира",58200000,None,
  "Masteri Thảo Điền, угловая 2-спальная квартира, высокий этаж, вид на город.",
  "https://www.airbnb.com/rooms/1694147022114299071","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈1 940 000 ₫/сутки), реальную месячную цену Airbnb на эти даты не показал. Хозяин прямо пишет, что юнит подходит для долгосрочной аренды."}),

L(612,"ho-chi-minh","ak","Квартира",46600000,None,
  "Lumière Riverside, 1-спальная квартира с садом, «в сердце Thảo Điền», у реки.",
  "https://www.airbnb.com/rooms/1729523314432103971","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈1 552 000 ₫/сутки)."}),

L(613,"ho-chi-minh","ak","Квартира",46800000,None,
  "Masteri An Phú, 2-спальная квартира с видом на реку («Breeze Retreat»).",
  "https://www.airbnb.com/rooms/1672976370663587539","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈1 560 000 ₫/сутки)."}),

L(614,"ho-chi-minh","ak","Квартира",72100000,None,
  "Masteri Thảo Điền, 3-спальная квартира рядом с линией метро.",
  "https://www.airbnb.com/rooms/1319897937522165158","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена со скидкой — оценка по суточной ставке ×30 (≈2 403 742 ₫/сутки)."}),

L(615,"ho-chi-minh","tm","Квартира",62500000,None,
  "The Ascentia, «стильная» 2-спальная квартира виллового формата.",
  "https://www.airbnb.com/rooms/1662111483009910968","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈2 084 475 ₫/сутки)."}),

L(616,"ho-chi-minh","tm","Квартира",80600000,None,
  "The Ascentia, «A1206 Royal State», 2-спальная квартира — подтверждено, что реально внутри комплекса The Ascentia, КГТ Phú Mỹ Hưng.",
  "https://www.airbnb.com/rooms/980222889414625674","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена — оценка по суточной ставке ×30 (≈2 685 925 ₫/сутки)."}),

L(617,"ho-chi-minh","tm","Квартира",72000000,None,
  "The Antonia (соседнее с The Ascentia здание), 2-спальная квартира, Quận 7.",
  "https://www.airbnb.com/rooms/997286756324926973","проверено 17 авг",1,source="airbnb",
  details={"notice":"цена со скидкой — оценка по суточной ставке ×30 (≈2 399 999 ₫/сутки)."}),

L(618,"ho-chi-minh","ak","Квартира",50903829,80,
  "Glenwood Residences, 2-спальная квартира, ул. Nguyễn Văn Hưởng, Thảo Điền — «идеально для проживания от 30 ночей», как указано у площадки.",
  "https://www.booking.com/hotel/vn/glenwood-residence.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка Booking.com за 30 ночей (скидка от базовой цены 83,4 млн ₫)."}),

L(619,"ho-chi-minh","ak","Студия",36450000,35,
  "CHOWA HOME Thảo Điền (DNM Hospitality), ул. Xuân Thủy, Phường An Khánh — сервисный апарт-отель, есть варианты 1-спальных юнитов дороже.",
  "https://www.booking.com/hotel/vn/chowa-home-aparthotel-thao-dien-area.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, указана цена самого дешёвого юнита (студия 35 м²). В здании также: 1PN 45 м² за 40,5 млн, 1PN+балкон 48 м² за 41,31 млн."}),

L(620,"ho-chi-minh","ak","Квартира",57600000,50,
  "Masteri Thảo Điền Apartment (управляется M Living), ул. Xa lộ Hà Nội — сервисная аренда, доступны 1-3-спальные варианты.",
  "https://www.booking.com/hotel/vn/masteri-thao-dien-apartment-quan-22.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, указана цена самого дешёвого юнита (1PN 50 м²). Также: 2PN 70 м² за 60,48-63 млн, есть и 3PN 90 м²."}),

L(621,"ho-chi-minh","tm","Квартира",39600000,88,
  "Ascentia Serviced Apartment in Central Phu My Hung — подтверждённый адрес внутри The Ascentia, рядом Sakura Park PMH/SECC/Crescent Mall.",
  "https://www.booking.com/hotel/vn/ascentia-serviced-apartment-in-central-phu-my-hung.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, указана цена самого дешёвого юнита (2PN 88 м²). Также: 3PN+балкон 130 м² за 69,3-126 млн."}),

L(622,"ho-chi-minh","ak","Студия",26350000,None,
  "CHOWA HOME Thảo Điền (DNM Hospitality) — тот же объект, что и на Booking.com (проверка перекрёстно подтвердила существование), скидка 66%.",
  "https://www.trip.com/hotels/detail/?hotelId=132385067&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1054), переведено по курсу ~25000 ₫/$."}),

L(623,"ho-chi-minh","ak","Комната",25400000,None,
  "The Ninety Six Thảo Điền (DNM Hospitality), стандартный 1-спальный номер.",
  "https://www.trip.com/hotels/detail/?hotelId=134911274&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1016), переведено по курсу ~25000 ₫/$."}),

L(624,"ho-chi-minh","ak","Студия",26875000,None,
  "Express by M Village 59 Thảo Điền — реальный вьетнамский сеть сервисных апарт-отелей M Village, стандартная студия.",
  "https://www.trip.com/hotels/detail/?hotelId=114422004&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1075), переведено по курсу ~25000 ₫/$."}),

L(625,"ho-chi-minh","ak","Квартира",25125000,None,
  "Uhouse — MELIA Thảo Điền Hotel & Apartment, 1-спальная квартира с видом на город.",
  "https://www.trip.com/hotels/detail/?hotelId=132379263&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1005), переведено по курсу ~25000 ₫/$."}),

L(626,"ho-chi-minh","ak","Квартира",46025000,None,
  "Indochine Casa, Thảo Điền.",
  "https://www.trip.com/hotels/detail/?hotelId=134006768&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($1841), переведено по курсу ~25000 ₫/$."}),
L(631,"ho-chi-minh","th","Квартира",12525000,None,
  "Siris Mia Residence – Self Check In, квартира на цокольном этаже, 1 спальня. Адрес: 94 Đặng Đại Độ, 260 м от торгового центра Phú Mỹ Hưng.",
  "https://www.trip.com/hotels/detail/?hotelId=128666857&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($501), переведено по курсу ~25000 ₫/$."}),

L(632,"ho-chi-minh","th","Студия",24050000,None,
  "Phu My Hung – Saigon South Serviced Apartments (корпус 1), студия делюкс, рядом Vivo City Mall. Адрес: R4-88 Hưng Phước 1, Phú Mỹ Hưng, Tân Phong Ward.",
  "https://www.trip.com/hotels/detail/?hotelId=129333067&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($962), переведено по курсу ~25000 ₫/$."}),

L(633,"ho-chi-minh","th","Студия",16025000,None,
  "Phu My Hung – Saigon South Serviced Apartments (корпус 2), студия супериор. Адрес: R4-35 Hưng Phước 4.",
  "https://www.trip.com/hotels/detail/?hotelId=6231550&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($641), переведено по курсу ~25000 ₫/$."}),

L(634,"ho-chi-minh","th","Студия",22525000,None,
  "Hearth and Home Lavida, студия с балконом и видом на город (реальный комплекс Lavida в Phú Mỹ Hưng), 10 мин до Korea Town. Адрес: 1181 Nguyễn Văn Linh, Tân Phong.",
  "https://www.trip.com/hotels/detail/?hotelId=127834611&cityId=301","проверено 17 авг",1,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей ($901), переведено по курсу ~25000 ₫/$."}),
L(635,"ho-chi-minh","tm","Квартира",33000000,89,
  "2-спальная квартира (2 с/у) в Midtown M8, Phú Mỹ Hưng, рядом парк Sakura, бассейн, спортзал, охрана 24/7.",
  "https://www.facebook.com/marketplace/item/1611784017021810/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 33 000 ₫, в описании 33 млн ₫/мес.","contact":"Em Tuyết"}),

L(636,"ho-chi-minh","th","Квартира",16000000,None,
  "2-спальная квартира (2 с/у) в Scenic Valley, Phú Mỹ Hưng, рядом Crescent Mall, SECC.",
  "https://www.facebook.com/marketplace/item/1549785510228320/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 16 ₫ (баг), в описании 16 млн ₫/мес."}),

L(637,"ho-chi-minh","th","Квартира",25000000,90,
  "2-спальная квартира (2 с/у) в Hưng Phúc 1, Phú Mỹ Hưng, вид на реку, машиноместо.",
  "https://www.facebook.com/marketplace/item/1634051588728434/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 25 000 ₫, в описании 25 млн ₫/мес.","contact":"Em Tuyết"}),

L(638,"ho-chi-minh","tm","Квартира",23000000,70,
  "2-спальная квартира (2 с/у) в The Aurora, Phú Mỹ Hưng.",
  "https://www.facebook.com/marketplace/item/2606394956497598/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 23 ₫ (баг), в описании 23 млн ₫/мес.","contact":"Vàng"}),

L(639,"ho-chi-minh","tm","Квартира",50000000,None,
  "3-спальная квартира (2 с/у) в The Ascentia, гибкая тарифная сетка: посуточно 2,8 млн ₫/ночь, помесячно (краткий срок) 60 млн ₫, при долгосрочной аренде — 50 млн ₫/мес.",
  "https://www.facebook.com/marketplace/item/1802640117824551/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 1 000 ₫ (баг). Указана цена именно для долгосрочной аренды (50 млн), а не посуточного/помесячного краткосрочного тарифа.","contact":"Em Chiến"}),

L(640,"ho-chi-minh","ak","Квартира",18000000,71,
  "2-спальная квартира (2 с/у) в Masteri Thảo Điền, 159 Võ Nguyên Giáp, свободна с конца августа.",
  "https://www.facebook.com/marketplace/item/1118026880887837/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 1 ₫ (баг), в описании 18 млн ₫/мес."}),

L(641,"ho-chi-minh","ak","Квартира",23000000,87,
  "Угловая квартира (2 спальни + доп. помещение, 2 с/у) в Tropic Garden, Thảo Điền, вид на реку.",
  "https://www.facebook.com/marketplace/item/4478437129035950/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 23 ₫ (баг), в описании «23tr net».","contact":"Mai Hà"}),

L(642,"ho-chi-minh","ak","Квартира",55000000,92,
  "2-спальная квартира в The Berkley, центр Thảo Điền — премиум-бутик комплекс (~85 квартир всего), вид на Landmark 81.",
  "https://www.facebook.com/marketplace/item/1375278774568712/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB цена показана как 1$ (валютный баг), в описании 55 млн ₫/мес включая плату за управление.","contact":"Thịnh Trần, 0862.101.239"}),

L(643,"ho-chi-minh","ak","Комната",14000000,None,
  "1-спальная квартира с балконом, восточная сторона, вид на реку, Thảo Điền, Thủ Đức.",
  "https://www.facebook.com/marketplace/item/1248260610704261/","проверено 17 авг",1,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается усечённая цена 14 000 ₫, в описании 14 млн ₫/мес.","deposit":"1 месяц","amenities":"уборка 2 раза/нед, смена белья 1 раз/нед, wifi, бесплатный мопед, спортзал, BBQ, крыша","contact":"Anh Thi Min"}),
L(644,"ho-chi-minh","ak","Комната",33264000,40,
  "The Ninety Six Thảo Điền (DNM Hospitality), 1-спальный номер, ул. Quốc Hương, Phường An Khánh.",
  "https://www.booking.com/hotel/vn/the-ninety-six-thao-dien-by-dnm-hospitality.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка 52% от базовой цены 69,3 млн ₫."}),

L(645,"ho-chi-minh","ak","Квартира",33889500,40,
  "Kim Apartment, уютная 1-спальная квартира «для пар», переулок 49 Đường Võ Nguyên Giáp, Thảo Điền.",
  "https://www.booking.com/hotel/vn/kim-apartment-cozy-1br-for-couples-in-thao-dien.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка 15% от базовой цены."}),

L(646,"ho-chi-minh","ak","Студия",28240380,None,
  "Harbor Point, ул. Quốc Hương, Thảo Điền — сервисный апарт-отель, доступна студия (queen) и 1-спальный юнит 45 м².",
  "https://www.booking.com/hotel/vn/harbor-point-quoc-huong.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей (скидка 24%), указана цена самой дешёвой студии. 1-спальный юнит 45 м² — 30 098 520 ₫/30 ночей."}),

L(647,"ho-chi-minh","ak","Квартира",43116756,75,
  "Glenwood Suites, 2-спальная квартира, ул. 65, District 2 (Thảo Điền).",
  "https://www.booking.com/hotel/vn/glenwood-suites.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка 11% от базовой цены 48,4 млн ₫."}),

L(648,"ho-chi-minh","th","Квартира",49974030,90,
  "Scenic Valley 2, 2-спальная квартира с видом на сад, ул. Nguyễn Văn Linh, 200 м от SECC. Также доступны варианты 2PN/80 м² с балконом и 3PN+балкон/120 м².",
  "https://www.booking.com/hotel/vn/scenic-valley-2-ho-chi-minh.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей. Другие юниты в том же комплексе: 2PN/80м² с балконом — 49 976 973 ₫; 3PN+балкон/120м² — 82 523 670 ₫."}),

L(649,"ho-chi-minh","th","Квартира",34149600,99,
  "Starhill Phú Mỹ Hưng, 2-спальная квартира, блок E, рядом SECC.",
  "https://www.booking.com/hotel/vn/can-ho-2pn-starhill-phu-my-hung-q7.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка 38% от базовой цены 55,08 млн ₫ (самый дешёвый тариф)."}),

L(650,"ho-chi-minh","th","Квартира",31594500,74,
  "Lavida Plus, «2-спальная» квартира, ул. Nguyễn Văn Linh, District 7.",
  "https://www.booking.com/hotel/vn/lavida-plus-thanh-pho-ho-chi-minh.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей. ⚠ на странице объекта указано «2 спальни», но список кроватей показывает только 1 односпальную + диван-кровать — возможна неточность в карточке, уточняйте у площадки перед бронированием."}),

L(651,"ho-chi-minh","th","Комната",29054700,25,
  "La Serena Phú Mỹ Hưng — стандартный номер отеля (King, 25 м²), завтрак включён. R4-56/57, Hưng Phước 4, Phường Tân Phong.",
  "https://www.booking.com/hotel/vn/la-serena-phu-my-hung.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"⚠ это обычный номер 3-звёздочного отеля, а не квартира — нет кухни. Реальная котировка за 30 ночей (самый дешёвый тариф)."}),

L(652,"ho-chi-minh","th","Комната",36720000,20,
  "El Ocaso Phú Mỹ Hưng — стандартный номер отеля (double, 20 м²). R21/R4-59, Hưng Phước 2/5, District 7.",
  "https://www.booking.com/hotel/vn/el-ocaso-phu-my-hung.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"⚠ это обычный номер 3-звёздочного отеля, а не квартира — нет кухни. Реальная котировка за 30 ночей."}),

L(653,"ho-chi-minh","th","Квартира",27600000,30,
  "Ngan Ha 2 Apartment, 1-спальная квартира, ул. Cao Triều Phát, District 7. Также доступен вариант 47 м².",
  "https://www.booking.com/hotel/vn/jack-apartment.ru.html","проверено 17 авг",1,source="booking",
  details={"notice":"реальная котировка за 30 ночей (скидка 20%), указан самый дешёвый юнит (30 м²). Вариант 47 м² — 36 000 000 ₫/30 ночей (та же скидка)."}),
L(654,"ho-chi-minh","ak","Квартира",25800000,None,
  "Masteri Thảo Điền, 2-спальная квартира (2 с/у), полная мебель, вид на реку, бассейн/зал/BBQ/охрана 24/7.",
  "https://www.facebook.com/groups/masterithaodien.hcmc/posts/2042173693083446/","проверено 17 авг",0,source="facebook",
  details={"contact":"Noodle Chan, 0902836054"}),

L(655,"ho-chi-minh","bth","Комната",8000000,25,
  "Студия с балконом, ул. Nguyễn Thái Bình, Bến Thành. Старое здание пешком, полная мебель, камеры/пожарная сигнализация.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-thai-binh-phuong-ben-thanh-53/studio-25m2-balcony-decor-cuc-xinh-thoang-mat-tien-hay-ham-nghi-q1-pr45996596","7 дней назад",7,source="batdongsan",
  details={"deposit":"2 месяца, оплата за период вперёд, договор на 1 год (депозит можно обсудить)","fees":"вода 21 500 ₫/м³, лифт 30 000 ₫/чел, мусор 105 000 ₫/мес, паркинг от 150 000 ₫","notice":"разрешён небольшой бизнес (салон/ногтевая студия), Airbnb не разрешён","contact":"агент Nguyễn Nhất Hoàng HiFriendz (171 активное объявление — крупный брокер)"}),

L(656,"ho-chi-minh","bth","Квартира",27000000,100,
  "2-спальная квартира (1 с/у), 5 мин до рынка Bến Thành и делового квартала, этаж 4 без лифта, ул. Lý Tự Trọng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ly-tu-trong-phuong-ben-thanh-53/cho-mat-tien-trung-tam-q1-30tr-thang-vi-tri-sam-uat-thuan-tien-di-chuyen-pr44602783","11 дней назад",11,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (16.08.26, вчера) — сайт сам помечает «возможно ещё актуально».","contact":"агент NHƯ NGỌC BCONS"}),

L(657,"ho-chi-minh","bth","Квартира",9000000,32,
  "Дуплекс, 1 спальня/1 с/у, ул. Nguyễn Thái Bình, Bến Thành. Можно жить самому или сдавать под Airbnb.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-thai-binh-phuong-ben-thanh-53/cho-45-47-quan-1-pr46120468","17 дней назад",17,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (15.08.26, 2 дня назад).","contact":"Duy Khang Nguyễn (похоже на частное лицо, 3 объявления)"}),

L(658,"ho-chi-minh","bth","Квартира",14000000,110,
  "5-спальная квартира (3 с/у) в старом здании прямо у рынка Bến Thành, ул. Nguyễn Công Trứ, этаж 2, можно перепланировать под бизнес.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-cong-tru-phuong-ben-thanh-53/110m2-5pn-3wc-kinh-doanh-tu-do-phu-hop-shop-o-kho-hang-online-ngay-cho-q1-pr46091668","24 дня назад",24,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (08.08.26, 9 дней назад). Объект верифицирован сайтом (Tin xác thực).","contact":"агент Nguyễn Nhất Hoàng HiFriendz"}),

L(659,"ho-chi-minh","bth","Квартира",8000000,52,
  "2-спальная квартира (1 с/у), этаж 3, балкон с видом на Q1/Q4, ул. Võ Văn Kiệt, рядом мост Ông Lãnh.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-van-kiet-phuong-ben-thanh-53/cho-194-q1-2pn-8tr-pr46031934","27 дней назад",27,source="batdongsan",
  details={"notice":"⚠ дата истечения тарифа объявления прошла (05.08.26, 12 дней назад).","contact":"Nguyendangphuong (14 объявлений)"}),

L(660,"ho-chi-minh","kh","Студия",13000000,38,
  "Студия в Masteri Millennium, полная премиум-мебель, балкон, ориентация северо-запад. 132 Bến Vân Đồn.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-phuong-6-masteri-millennium/studio-full-noi-that-o-lien-lh-pr43746813","12 дней назад",12,source="batdongsan",
  details={"contact":"Phạm Minh Quân"}),

L(661,"ho-chi-minh","kh","Квартира",25000000,74,
  "Угловая 2-спальная квартира (2 с/у) в Masteri Millennium, вид на реку и башню Bitexco, бассейн/спортзал/охрана 24/7, 3 мин до Q1. 132 Bến Vân Đồn.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-phuong-6-masteri-millennium/goc-view-song-bitexco-cuc-ep-2pn-tang-cao-vao-o-ngay-pr45668681","5 дней назад",5,source="batdongsan",
  details={"notice":"верифицировано сайтом 13.08.26","contact":"Hồng Ngô Việt"}),

L(662,"ho-chi-minh","kh","Квартира",28000000,103,
  "3-спальная квартира (2 с/у) в Masteri Millennium, вид на город, бассейн-инфинити, спортзал, BBQ, терраса, рецепция, рядом Q1/Bitexco/Ba Son. 132 Bến Vân Đồn.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-phuong-6-masteri-millennium/gia-tot-nhat-3pn-103m-view-thanh-pho-full-noi-that-chi-28-trieu-lh-pr46193082","опубликовано сегодня",0,source="batdongsan",
  details={"contact":"агент Đặng Đình Thịnh (435 активных объявлений — крупное агентство)"}),

L(663,"ho-chi-minh","kh","Дом",8500000,27,
  "Отдельный дом целиком, 2 спальни/2 с/у, свежий ремонт, световой колодец, свет/вода по гостарифу, без платы за паркинг/управление. От собственника напрямую («chính chủ»). Переулок 1, ул. Tôn Đản.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ton-dan-phuong-15-56/quan-4-chinh-chu-cho-moi-nguyen-can-hem-1-an-2pn-2wc-pr45398771","2 дня назад",2,source="batdongsan",
  details={"contact":"собственница «Trâm»"}),

L(664,"ho-chi-minh","kh","Дом",14000000,48,
  "Дом в переулке (3×16м), 2 спальни/1 с/у, первый этаж + антресоль, 2 кондиционера, рядом мост Ông Lãnh. Ул. Bến Vân Đồn.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ben-van-don-phuong-phuong-9-2-56/cho-hem-3-5m-xh-on-p-9-q-4-14tr-pr46175440","4 дня назад",4,source="batdongsan",
  details={"contact":"агентство Nhà Đất Minh Đức (575 объявлений, 13 лет на рынке)"}),

L(665,"ho-chi-minh","kh","Дом",11000000,18,
  "Дом целиком (фасад 6м, 3 этажа), 3 спальни/3 с/у, 2 кондиционера, 3 камеры, напротив пагоды Giác Nguyên. Ул. Số 41.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-so-41-phuong-6-56/cho-nguyen-can-dai-han-uong-41-khanh-hoi-tp-hcm-oi-dien-chua-giac-nguyen-pr46165994","6 дней назад",6,source="batdongsan",
  details={"contact":"«Tan» (похоже на частное лицо)"}),

L(666,"ho-chi-minh","th","Квартира",26000000,80,
  "Угловая 2-спальная квартира (2 с/у) в Urban Hill, Phú Mỹ Hưng, новый ремонт, рядом VivoCity/Crescent Mall/международная школа Nam Sài Gòn. Ул. Nguyễn Văn Linh.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-van-linh-phuong-tan-phong-9-urban-hill/cho-80m2-26-trieu-vnd-2pn-2wc-full-noi-that-cao-cap-moi-99-lh-pr45693876","проверено 17 авг",0,source="batdongsan",
  details={"contact":"Mr. Đức Huy"}),

L(667,"ho-chi-minh","ak","Квартира",23000000,54,
  "1-спальная квартира (1 с/у, площадь по стенам 54 м² / по факту 46,8 м²) в Masteri An Phú, вид на реку. Ул. Xa Lộ Hà Nội.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-xa-lo-ha-noi-phuong-thao-dien-masteri-an-phu/cho-1pn-23tr-net-chuyen-gio-hang-gia-tot-cam-ket-uy-tin-bao-gia-that-pr46179485","3 дня назад",3,source="batdongsan",
  details={"notice":"цена указана как net (чистыми), верифицировано сайтом 14.08.26","contact":"агент Tuấn Sang Masteri (28 объявлений)"}),

L(668,"ho-chi-minh","ak","Квартира",40000000,88,
  "Угловая 2-спальная квартира (2 с/у) в Thảo Điền Green, вид на реку и Landmark 81, бассейн-инфинити, минимум год аренды. Ул. Nguyễn Văn Hưởng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-van-huong-phuong-thao-dien-thao-dien-green/goc-2pn-2wc-88m2-50tr-thang-tai-ien-om-tron-view-song-view-landmark81-xem-de-pr46074041","1 день назад",1,source="batdongsan",
  details={"contact":"агент Lê Thanh Tuấn (116 объявлений)"}),

L(669,"ho-chi-minh","ak","Квартира",20000000,70,
  "2-спальная квартира (2 с/у) в Masteri An Phú, полная мебель, свободна, можно смотреть в любое время. Ул. Xa Lộ Hà Nội.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-xa-lo-ha-noi-phuong-thao-dien-masteri-an-phu/for-rent-2-bedrooms-20-000-000-vnd-month-pr45195500","опубликовано сегодня",0,source="batdongsan",
  details={"contact":"агент Serena Juan (26 объявлений)"}),

L(670,"ho-chi-minh","bq","Студия",8500000,40,
  "Новая студия, замок по отпечатку пальца, камеры 24/7, без общего хозяина, рядом университет HUTECH. Ул. Thanh Đa.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-thanh-da-phuong-27-66/moi-khai-truong-studio-1-phong-ngu-full-noi-that-gan-ai-hoc-hutech-pr46177370","4 дня назад",4,source="batdongsan",
  details={"notice":"верифицировано сайтом 13.08.26","contact":"агент «Toàn Căn Hộ Đẹp»"}),

L(671,"ho-chi-minh","bq","Квартира",10000000,50,
  "1-спальная мини-квартира рядом с мостом Cầu Kinh, лифт, большой подземный паркинг, есть зарядка для электровелосипедов. Ул. Thanh Đa.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-thanh-da-phuong-27-66/1pn-ngay-cau-kinh-a-thang-may-ham-xe-lon-co-nhan-xe-ien-pr46146130","11 дней назад",11,source="batdongsan",
  details={"notice":"верифицировано сайтом 06.08.26","contact":"агент Thanh Duy - Uni Living (49 объявлений)"}),
L(672,"ho-chi-minh","bth","Комната",7200000,36,
  "Комната с балконом, полная мебель, ул. Lê Lai, Bến Thành.",
  "https://www.nhatot.com/thue-phong-tro-quan-1-tp-ho-chi-minh/134195225.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"1 месяц (7,2 млн ₫)"}),

L(673,"ho-chi-minh","bth","Комната",4000000,30,
  "Недорогая комната, своя ванная, без совместного хозяина, ул. Nam Kỳ Khởi Nghĩa, Bến Thành.",
  "https://www.nhatot.com/thue-phong-tro-quan-1-tp-ho-chi-minh/134166268.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"1 месяц"}),

L(674,"ho-chi-minh","bth","Комната",6900000,40,
  "Комната с окном на крышу (планировка на 2 «спальни»), рядом университеты UEH и Sài Gòn, ул. Nguyễn Thị Minh Khai, Bến Thành.",
  "https://www.nhatot.com/thue-phong-tro-quan-1-tp-ho-chi-minh/134053139.htm","7 дней назад",7,source="chotot",
  details={"notice":"свет/вода/сервис отдельно, краткосрочная аренда +15% к цене. В поле «депозит» стоит явно техническое значение — не ориентируйтесь на него."}),

L(675,"ho-chi-minh","bth","Студия",6500000,40,
  "Студия с отдельной кухней и балконом, рядом Bùi Viện, разрешены животные, рядом несколько вузов. Ул. Bùi Thị Xuân, Bến Thành.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134070750.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(676,"ho-chi-minh","bth","Квартира",30000000,100,
  "3-спальная квартира, этаж 4, в 100 м от рынка Bến Thành, подходит под хоумстей. Ул. Lý Tự Trọng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/132650643.htm","3 дня назад",3,source="chotot",
  details={}),

L(677,"ho-chi-minh","bth","Квартира",10500000,60,
  "«Пентхаус» в центре Bến Thành, 1 спальня, премиум-мебель, весь этаж. Ул. Nguyễn Thị Minh Khai.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/132326663.htm","5 дней назад",5,source="chotot",
  details={"notice":"поле «депозит» показывает явно ошибочное значение (1 000 000 ₫ при такой аренде) — не ориентируйтесь на него."}),

L(678,"ho-chi-minh","kh","Комната",4200000,20,
  "Комната, рядом университет Nguyễn Tất Thành, ул. Đoàn Văn Bơ.",
  "https://www.nhatot.com/thue-phong-tro-quan-4-tp-ho-chi-minh/129051597.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"1 месяц","electricity":"3 700 ₫/кВт·ч","water":"100 000 ₫/чел.","fees":"сервис 100 000 ₫/комната"}),

L(679,"ho-chi-minh","kh","Студия",6500000,25,
  "Студия в 500 м от университета права (ĐH Luật), ул. Nguyễn Trường Tộ.",
  "https://www.nhatot.com/thue-phong-tro-quan-4-tp-ho-chi-minh/134193231.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"1 месяц"}),

L(680,"ho-chi-minh","kh","Комната",4800000,18,
  "Комната на Xóm Chiếu, бонус 500 тыс ₫ при переезде в сентябре.",
  "https://www.nhatot.com/thue-phong-tro-quan-4-tp-ho-chi-minh/134154570.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"⚠ это переуступка — текущий жилец съезжает из своего 6-месячного контракта, гарантия аренды только на ~3 месяца.","electricity":"4 000 ₫/кВт·ч","water":"100 000 ₫/чел.","fees":"интернет+лифт+мусор 150 000 ₫/комната"}),

L(681,"ho-chi-minh","kh","Студия",9000000,38,
  "Студия с видом на Q1, рядом мост Ông Lãnh, ул. Hoàng Diệu.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134143475.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"2 месяца (18 млн ₫)","fees":"сервис-сбор ~200 000 ₫/мес"}),

L(682,"ho-chi-minh","kh","Квартира",13000000,65,
  "2-спальная квартира (1 с/у) в ЖК H1, угловая, стиральная+сушильная машина, холодильник, ТВ, рядом университет права, рынок Xóm Chiếu, Bến Nhà Rồng. Ул. Hoàng Diệu.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134162206.htm","проверено 17 авг",0,source="chotot",
  details={"deposit":"2 месяца (26 млн ₫)","contract":"от 1 года, без комиссии агенту","notice":"текущий жилец съезжает в конце августа, заезд с сентября"}),

L(683,"ho-chi-minh","kh","Квартира",20000000,74,
  "2-спальная квартира (2 с/у) в Masteri Millennium, прямо напротив Q1. Ул. Bến Vân Đồn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134142975.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"⚠ несостыковка площади: в структурированном поле 74 м², в тексте описания «rộng 65m2» — уточняйте у автора."}),

L(684,"ho-chi-minh","kh","Квартира",10500000,57,
  "Угловая 1-спальная квартира, полная мебель, высокий этаж, ЖК H3. Ул. Hoàng Diệu.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134186401.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(685,"ho-chi-minh","th","Квартира",13000000,70,
  "2-спальная квартира от 70 м² в Sky Garden 3 (застройщик Phú Mỹ Hưng), рядом SC VivoCity. Ул. Phạm Văn Nghị.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134194871.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"это агентский прайс-лист по нескольким юнитам в комплексе, не конкретная квартира: 2PN 70-75м² = 13-16 млн, 3PN 85-100м² = 18-30 млн. Указана нижняя граница."}),

L(686,"ho-chi-minh","th","Студия",9000000,28,
  "Студия-офистель в Lavida Plus, напротив Vivo City, рядом RMIT и Tôn Đức Thắng. Ул. Nguyễn Văn Linh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134194791.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(687,"ho-chi-minh","th","Квартира",40000000,100,
  "2-спальная квартира с видом на реку в Riverpark Premier (застройщик Phú Mỹ Hưng), рядом международная школа SSIS. Ул. Nguyễn Đức Cảnh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/131979965.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"премиум-сегмент"}),

L(688,"ho-chi-minh","ak","Студия",7200000,35,
  "Просторная студия, 15 мин до Q1/Bình Thạnh, охрана, паркинг. Ул. Trần Não.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/132504325.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(689,"ho-chi-minh","ak","Комната",8000000,50,
  "Комната в квартире De Capella (2 спальни/2 с/у, 50 м² на двоих), своя ванная, тарифы по гостарифу, заезд с начала августа. Ул. Lương Định Của.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134124945.htm","проверено 17 авг",0,source="chotot",
  details={"notice":"⚠ это подселение в комнату к текущему жильцу, а не аренда целой квартиры."}),

L(690,"ho-chi-minh","ak","Квартира",7000000,40,
  "1-спальная квартира с видом на Landmark 81, отдельная кухня. Ул. Số 38.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133932395.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(691,"ho-chi-minh","bq","Дом",12000000,160,
  "Дом целиком, 3 спальни, есть право собственности (сổ), 3 кондиционера. Ул. Bình Quới.",
  "https://www.nhatot.com/thue-nha-dat-quan-binh-thanh-tp-ho-chi-minh/133318523.htm","16 дней назад",16,source="chotot",
  details={}),

L(692,"ho-chi-minh","bq","Дом",3500000,42,
  "Домик в стиле хоумстей, 1 спальня, естественная вентиляция, без комиссии. Ул. Bình Quới.",
  "https://www.nhatot.com/thue-nha-dat-quan-binh-thanh-tp-ho-chi-minh/134165310.htm","проверено 17 авг",0,source="chotot",
  details={}),

L(693,"ho-chi-minh","bq","Дом",7000000,65,
  "Дом с видом на канал/озеро, свой сад, напротив зоны отдыха KDL Bình Quới 1, подходит под шоурум. Ул. Bình Quới.",
  "https://www.nhatot.com/thue-nha-dat-quan-binh-thanh-tp-ho-chi-minh/133516531.htm","5 дней назад",5,source="chotot",
  details={}),
L(694,"ho-chi-minh","bth","Квартира",12000000,None,
  "2-спальная квартира, этаж 6, лифт, большой балкон, можно с животными. Ул. Điện Biên Phủ, Quận 1.",
  "https://www.facebook.com/marketplace/item/1131674932395559/","проверено 17 авг",0,source="fbmarketplace",
  details={"fees":"обслуживание 400 000 ₫/мес, паркинг 300 000 ₫/машину, вода 150 000 ₫/чел.","electricity":"4 000 ₫/кВт·ч","contract":"от 1 года (базовая ставка без скидки — 12,5 млн ₫)","contact":"Nick Huynh (Zalo/WhatsApp)"}),

L(695,"ho-chi-minh","bth","Квартира",17000000,None,
  "Люкс-дуплекс апартаменты, ул. Nguyễn Bỉnh Khiêm, район Đa Kao — соседний с Bến Thành район старого Quận 1.",
  "https://www.facebook.com/marketplace/item/1370031828418845/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ формально это Phường Đa Kao, не Bến Thành — отдельных границ этого фыонга у нас пока нет, отнесено к Bến Thành приближённо (соседний район старого Quận 1).","electricity":"по гостарифу","contact":"Trần Trọng Trí"}),

L(696,"ho-chi-minh","bth","Квартира",9000000,45,
  "Сервисная 1-спальная квартира, полная мебель, бесплатная парковка мопеда. Переулок 121 Lê Thị Riêng, Phường Bến Thành.",
  "https://www.facebook.com/marketplace/item/2047820999471241/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 9 000 ₫ — баг ввода цены, в описании 9 млн ₫/мес (2-спальный вариант в этом же доме — 11 млн ₫).","electricity":"4 000 ₫/кВт·ч","water":"100 000 ₫/чел.","fees":"управление 200 000 ₫/комната","contact":"Zalo 093 250 1428"}),

L(697,"ho-chi-minh","bth","Квартира",5200000,None,
  "Квартира на 4 этаже без лифта, «заезжай с чемоданом», Quận 1 (точный адрес не указан).",
  "https://www.facebook.com/marketplace/item/1264979902190261/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"мало деталей в объявлении — площадь и точный адрес не указаны, продавец не назван."}),

L(698,"ho-chi-minh","kh","Квартира",21000000,74,
  "2-спальная квартира (2 с/у) в Masteri Millennium, балкон с видом на реку, заезд с 1 сентября. В этом же доме у продавца есть и другие юниты: 1BR/53м²/18тр, 2BR/74м²/22тр, 3BR/107м²/31тр, 3BR/100м²/32тр. 132 Đ. Bến Vân Đồn.",
  "https://www.facebook.com/marketplace/item/1780671263120441/","проверено 17 авг",0,source="fbmarketplace",
  details={"amenities":"спортзал, бассейн, BBQ","contact":"Tấn Huy"}),

L(699,"ho-chi-minh","kh","Квартира",17000000,65,
  "2-спальная квартира (1 с/у) в The Gold View, полная мебель, 3 мин до Q1. У того же агента в доме есть и другие юниты (81-123 м², 17-28 млн). 346 Bến Vân Đồn.",
  "https://www.facebook.com/marketplace/item/1064838342932304/","проверено 17 авг",0,source="fbmarketplace",
  details={"amenities":"спортзал, бассейн, BBQ, супермаркет, кинотеатр, кафе","contact":"Huy"}),

L(700,"ho-chi-minh","kh","Квартира",31000000,117,
  "3-спальная квартира (2 с/у) в The Gold View, полная мебель — другой юнит в том же доме, что и предыдущее объявление, у того же агента.",
  "https://www.facebook.com/marketplace/item/1391839039543431/","проверено 17 авг",0,source="fbmarketplace",
  details={"contact":"Huy"}),

L(701,"ho-chi-minh","kh","Комната",15000000,50,
  "1-спальная квартира (1 с/у) в ICON56, полная мебель, 5 мин до Q1. У продавца в доме также есть 3BR/90м² за 25 млн. 56 Bến Vân Đồn.",
  "https://www.facebook.com/marketplace/item/28805881365679369/","проверено 17 авг",0,source="fbmarketplace",
  details={"amenities":"бассейн, спортзал, магазин у дома","contact":"Tấn Huy (тот же агент, что и Masteri Millennium выше)"}),

L(702,"ho-chi-minh","kh","Комната",6000000,None,
  "1-спальный юнит у моста Khánh Hội, на границе с Q1/Q7. У хозяина есть прайс-лист: студия от 4 млн, дуплекс-антресоль от 5 млн, 1-спальная (это объявление) от 6 млн, 2-спальная от 8 млн.",
  "https://www.facebook.com/marketplace/item/1979493175975172/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 10 000 ₫ — баг ввода цены. В описании нет единой цены, только стартовая планка «от 6 млн» — финальная цена не подтверждена, указана стартовая.","amenities":"полная мебель, охрана 24/7"}),

L(703,"ho-chi-minh","tm","Квартира",22000000,55,
  "1-спальная квартира (1 с/у) в The Ascentia, высокий этаж, ул. Nguyễn Lương Bằng. Бассейны (взрослый+детский), спортзал, BBQ, парк, детская площадка, сад на крыше, рядом Crescent Mall/SC VivoCity/SECC и международные школы.",
  "https://www.facebook.com/marketplace/item/963438706325513/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 2 200 000 ₫ — баг ввода цены ровно в 10 раз, в описании 22 млн ₫/мес.","contact":"Phúc Hiền"}),

L(704,"ho-chi-minh","ak","Квартира",50000000,98,
  "3-спальная квартира (2 с/у) в Masteri Thảo Điền, высокий этаж, вид на город, торг возможен. 159 Võ Nguyên Giáp.",
  "https://www.facebook.com/marketplace/item/1202361709619200/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"цена без учёта платы за управление","amenities":"бассейн, спортзал, BBQ, детская площадка, магазин, ТЦ","contact":"Đỗ Thủy (тот же агент, что и объявление по Ascentia выше)"}),

L(705,"ho-chi-minh","ak","Квартира",27000000,None,
  "2-спальная квартира с прямым видом на реку в Masteri Thảo Điền, полная мебель. 159 Võ Nguyên Giáp.",
  "https://www.facebook.com/marketplace/item/955157487332449/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"цена net, без платы за управление","contact":"Mr. Phong"}),

L(706,"ho-chi-minh","bq","Дом",12000000,96,
  "Отдельный дом целиком (8×12м, 1 этаж + мансарда), свой двор/паркинг, 3 спальни (3 кондиционера), подходит для жизни или онлайн-бизнеса, торг возможен. Рядом рынок Thanh Đa.",
  "https://www.facebook.com/marketplace/item/1544404080572328/","проверено 17 авг",0,source="fbmarketplace",
  details={"notice":"⚠ на карточке FB отображается цена 1 200 000 ₫ — баг ввода цены ровно в 10 раз, в описании 12 млн ₫/мес.","contact":"Ngọc Lành — от собственника напрямую («chính chủ»), редкая находка для этого района"}),

L(707,"ho-chi-minh","bq","Квартира",21000000,120,
  "Угловая 3-спальная квартира (2 с/у) в ЖК Thanh Đa View, балкон, бассейн, спортзал, магазин у дома, напротив рынка Thanh Đa, у моста, вокруг река Сайгон.",
  "https://www.facebook.com/marketplace/item/1043456721722228/","проверено 17 авг",0,source="fbmarketplace",
  details={"contact":"Tấn Huy (тот же агент, что и объявления по Q4 выше)"}),
L(708,"ho-chi-minh","bth","Квартира",27966263,20,
  "Mersey Central Saigon Apart'Hotel, студия/1-спальная, ул. Yersin, Q1.",
  "https://www.booking.com/hotel/vn/mersey-central-saigon.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей (1-30 сент. 2026)."}),

L(709,"ho-chi-minh","bth","Студия",24161253,40,
  "Nicecy Hotel & Apartment, студия, ул. Trần Hưng Đạo, Phường Bến Thành.",
  "https://www.booking.com/hotel/vn/nicecy-amp-apartment-ho-chi-minh.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка от базовой цены 61,9 млн ₫."}),

L(710,"ho-chi-minh","bth","Квартира",27744000,27,
  "INDO Serviced Apartment, 1-спальная, ул. Thái Văn Lung, Q1.",
  "https://www.booking.com/hotel/vn/indo-serviced-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(711,"ho-chi-minh","bth","Студия",30492000,29,
  "International Residence (CityNest Saigon), студия с балконом, ул. Phạm Ngũ Lão, Q1.",
  "https://www.booking.com/hotel/vn/citynest-saigon-residence.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей, скидка от базовой цены 50,8 млн ₫."}),

L(712,"ho-chi-minh","bth","Квартира",44625000,40,
  "Journey Central – SOHO Residence, 1-спальная, ул. Cô Giang, Q1.",
  "https://www.booking.com/hotel/vn/the-lumiere-saigon-central.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей (со скидкой)."}),

L(713,"ho-chi-minh","bth","Квартира",65484000,60,
  "Yu Stay Apartment, Soho D1, 2-спальная, 100 Cô Giang, Q1.",
  "https://www.booking.com/hotel/vn/yu-stay.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(714,"ho-chi-minh","bth","Студия",79916099,35,
  "Soho Residences D1 (Veluxe Stay), студия, 100 Cô Giang, Q1.",
  "https://www.booking.com/hotel/vn/instaworthy-2br-central-prime-spot-wcity-views.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей — цена высокая для студии, возможно премиум-этаж/вид."}),

L(715,"ho-chi-minh","bth","Студия",37270800,35,
  "Aris Soho Balcony Suites, студия с балконом, 100 Cô Giang, Q1.",
  "https://www.booking.com/hotel/vn/anthesis-riverside-apartment-masteri-millennium.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(716,"ho-chi-minh","bth","Студия",30213000,36,
  "Chilli & Chum Apartment, студия, ул. Hồ Hảo Hớn, Q1.",
  "https://www.booking.com/hotel/vn/chilli-and-chum-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(717,"ho-chi-minh","bth","Квартира",19002454,30,
  "Wabi Sabi Saigon Hideout, вся квартира, 1 спальня, ул. Cô Giang, Q1.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=120250970","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(718,"ho-chi-minh","bth","Комната",17986066,None,
  "Peanuts Home Lê Lai, номер, ул. Lê Lai, Phường Bến Thành.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=132689258","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(719,"ho-chi-minh","bth","Студия",16872600,None,
  "Hearth and Home De Thám, делюкс-студия, ул. Đề Thám, район Cầu Ông Lãnh (соседний со старым Q1).",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=130052850","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей. Формально Phường Cầu Ông Lãnh, а не Bến Thành — отдельных границ пока нет."}),

L(720,"ho-chi-minh","bth","Комната",24891294,None,
  "Mari Queen Hotel, номер (double), ул. Bùi Thị Xuân, район Phạm Ngũ Lão.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=63988006","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей, завтрак включён."}),

L(721,"ho-chi-minh","bth","Комната",37070324,None,
  "A25 Premium Hotel, номер superior с завтраком, ул. Lê Anh Xuân, Phường Bến Thành.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=703836","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(722,"ho-chi-minh","bth","Дом",71033126,None,
  "Таунхаус 3 спальни/3,5 с/у с террасой и BBQ на крыше, центр Q1.",
  "https://www.airbnb.com/rooms/1747239434091228240","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (22 авг - 19 сент), скидка от 88,3 млн ₫."}),

L(723,"ho-chi-minh","bth","Квартира",20563986,None,
  "Студия Nomah, рядом с розовой церковью Тân Định.",
  "https://www.airbnb.com/rooms/1745711185555765792","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (24 авг - 21 сент), скидка от 26,5 млн ₫. Формально Phường Tân Định, соседний со старым Q1."}),

L(724,"ho-chi-minh","bth","Студия",29978283,45,
  "Студия рядом с рынком Bến Thành.",
  "https://www.airbnb.com/rooms/1729749566721861030","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (18 ноя - 16 дек), скидка от 36,4 млн ₫."}),

L(725,"ho-chi-minh","bth","Дом",81618003,None,
  "Ambré Suites, 3 спальни/4 кровати/2 с/у, 5 мин до Bùi Viện.",
  "https://www.airbnb.com/rooms/1743932104867038611","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 99 млн ₫."}),

L(726,"ho-chi-minh","bth","Дом",44668179,None,
  "Дом 2 спальни/3 с/у, пешком до ул. Nguyễn Huệ.",
  "https://www.airbnb.com/rooms/1740629101657606884","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (14 сент - 12 окт), скидка от 51,2 млн ₫."}),

L(727,"ho-chi-minh","bth","Студия",11013207,None,
  "Тихая студия в переулке, Q1 — самый бюджетный вариант в подборке по D1.",
  "https://www.airbnb.com/rooms/1714347796029268086","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 15,2 млн ₫."}),

L(728,"ho-chi-minh","bth","Дом",149851979,None,
  "Люксовый дуплекс 3 спальни/6 кроватей/2 с/у, бассейн и спортзал, Q1.",
  "https://www.airbnb.com/rooms/1744123735364525509","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 173,2 млн ₫ — топ-сегмент цен для ориентира."}),

L(729,"ho-chi-minh","kh","Студия",23680800,30,
  "S Lux Apartment, студия, ул. Nguyễn Trường Tộ, Q4.",
  "https://www.booking.com/hotel/vn/s-lux-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(730,"ho-chi-minh","kh","Студия",27816000,28,
  "Key & Code Serviced Apartments, студия, ЖК Rivergate Residence.",
  "https://www.booking.com/hotel/vn/key-amp-code-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(731,"ho-chi-minh","kh","Студия",23259428,28,
  "Refined Saigon, студия в ЖК River Gate, 155 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/saigon-memories-free-city-walk-experience-amazing-infinity-pool-amp-free-4g-sim.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(732,"ho-chi-minh","kh","Студия",34800000,40,
  "A&L Service Apartment, студия в ЖК Rivergate Residence, 154 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/a-amp-l-service-apartment-by-me-in-rivergate-building.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(733,"ho-chi-minh","kh","Квартира",34929312,35,
  "Smile Home, 1-спальная в ЖК Tresor, 39 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/tresor-cozy-and-spacious-studio-bitexco-view.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(734,"ho-chi-minh","kh","Квартира",52992000,80,
  "Lovely Apartment, 2-спальная в ЖК Goldview, ул. Khánh Hội.",
  "https://www.booking.com/hotel/vn/lovely-apartment-goldview-ben-van-don.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(735,"ho-chi-minh","kh","Квартира",24000000,55,
  "Loft Bedroom Apartment, 1-спальная, 34-35 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/loft-bedroom-apartment.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(736,"ho-chi-minh","kh","Студия",83303712,35,
  "Tresor Apartments D4 (Veluxe Stay), студия, 39 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/la-vela-homes-premium-studios-2-amp-3-br-apartments-tresor-apartments-d4-5mins-t.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей — цена высокая для студии, возможно верхний этаж/премиум."}),

L(737,"ho-chi-minh","kh","Студия",37320750,37,
  "Saigon Royal Apartment, студия, 34-35 Bến Vân Đồn.",
  "https://www.booking.com/hotel/vn/saigon-royal-apartment-ho-chi-minh.ru.html","проверено 17 авг",0,source="booking",
  details={"notice":"реальная котировка за 30 ночей."}),

L(738,"ho-chi-minh","kh","Студия",28898440,None,
  "Rivergate Central, студия-сюит с кухней и видом на город, 151 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=23519757","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(739,"ho-chi-minh","kh","Студия",27958306,None,
  "MIN' Apartment, стандартная студия в ЖК Rivergate Residence, 151 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=113290340","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(740,"ho-chi-minh","kh","Студия",26070630,28,
  "RiverGate Saigon, студия/1-спальная, 151-155 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=134812647","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(741,"ho-chi-minh","kh","Квартира",32072906,30,
  "GobyHome, 1-спальная в ЖК Rivergate Residence, 151-155 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=135371761","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(742,"ho-chi-minh","kh","Студия",32294450,None,
  "Chau Apartments, студия, 155 Bến Vân Đồn.",
  "https://www.trip.com/hotels/detail/?cityId=301&hotelId=25208785","проверено 17 авг",0,source="tripcom",
  details={"notice":"реальная котировка Trip.com за 30 ночей."}),

L(743,"ho-chi-minh","kh","Квартира",26087888,None,
  "Студия в ЖК Tresor, центральное расположение.",
  "https://www.airbnb.com/rooms/894482406449428240","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 28,3 млн ₫."}),

L(744,"ho-chi-minh","kh","Квартира",33289874,None,
  "Уютная 1-спальная квартира в ЖК Tresor.",
  "https://www.airbnb.com/rooms/1728983336700006983","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (10 сент - 8 окт), скидка от 40,4 млн ₫."}),

L(745,"ho-chi-minh","kh","Квартира",40387920,50,
  "1-спальная квартира в ЖК Tresor, 50 м².",
  "https://www.airbnb.com/rooms/1743356139409084608","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (10 сент - 8 окт), скидка от 52,1 млн ₫."}),

L(746,"ho-chi-minh","kh","Квартира",19306712,None,
  "1-спальная квартира в Saigon Royal, самый доступный вариант в подборке по D4.",
  "https://www.airbnb.com/rooms/1700801896456964053","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 24,9 млн ₫."}),

L(747,"ho-chi-minh","kh","Квартира",31371425,None,
  "The Burgundy House, 1-спальная квартира, Quận 4.",
  "https://www.airbnb.com/rooms/1496811395593577343","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (20 окт - 17 ноя)."}),

L(748,"ho-chi-minh","kh","Квартира",43012450,None,
  "2-спальная квартира в ЖК Tresor, вид на город.",
  "https://www.airbnb.com/rooms/1739773704635725660","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (17 авг - 14 сент), скидка от 55,4 млн ₫."}),

L(749,"ho-chi-minh","kh","Квартира",47698352,None,
  "2-спальная квартира (2 с/у) в ЖК Tresor, 5 мин до рынка Bến Thành.",
  "https://www.airbnb.com/rooms/1728145041120427061","проверено 17 авг",0,source="airbnb",
  details={"notice":"реальная котировка Airbnb за месяц (8 сент - 6 окт), скидка от 58,5 млн ₫."}),
L(750,"ho-chi-minh","ak","Дом",30000000,250,
  "Дом 2 этажа, 2 спальни/3 с/у, гостиная и кухня, мини-двор. Ул. Quốc Hương, центр Thảo Điền. Тихая охраняемая улица, рядом парк и супермаркет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133314010.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(751,"ho-chi-minh","ak","Дом",35000000,350,
  "Угловой дом на 2 фасада, гараж + 2 этажа, 4 спальни/5 с/у. Ул. Nguyễn Văn Hưởng, Thảo Điền. Улица 10 м, подходит под жильё или офис.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133314052.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(752,"ho-chi-minh","ak","Дом",100000000,120,
  "Вилла с бассейном и лифтом, 5 спален/7 с/у, цоколь + антресоль + 2 этажа. Ул. số 12, Trần Não, An Khánh (бывш. Quận 2). Полностью меблирована.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134174858.htm","2 дня назад",2,source="chotot",
  details={"contact":"Tony BĐS","notice":"⚠ 120 м² — это площадь застройки (7x17 м), общая площадь по этажам больше. Цена 100 млн ₫ указана без налога."}),

L(753,"ho-chi-minh","ak","Квартира",9000000,40,
  "1-спальная квартира с отдельной кухней, балкон, своя стиральная машина. Рядом с Tropic Garden, ул. Quốc Hương, Thảo Điền.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133727326.htm","3 дня назад",3,source="chotot",
  details={"contact":"Thiện HIFRIENDZ"}),

L(754,"ho-chi-minh","bth","Квартира",8000000,40,
  "1-спальная квартира 40 м² с балконом и своей стиральной машиной, ул. Nguyễn Thị Minh Khai, Q1. Пешком до университетов (KHXH&NV, Y Dược), рядом Hồ Con Rùa и собор Нотр-Дам.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/133035984.htm","сегодня",0,source="chotot",
  details={"contact":"Chiêu Minh Vĩ"}),

L(755,"ho-chi-minh","bth","Квартира",30000000,150,
  "3 спальни/2 с/у, полностью меблирована, 4-й этаж. 74 Lý Tự Trọng, Phường Bến Thành — прямо у рынка Bến Thành.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/133703704.htm","сегодня",0,source="chotot",
  details={"contact":"Duy Nguyễn","notice":"⚠ в поле площади указано 150 м², в тексте — 100 м² собственно квартиры плюс терраса, всего около 200 м². Уточняйте у продавца."}),

L(756,"ho-chi-minh","bth","Дом",14000000,27,
  "Дом в переулке с автомобильным заездом, 3x9 м: цоколь + 2 этажа + терраса, 2 спальни с кондиционерами, 3 с/у, солнечный водонагреватель. Ул. Calmette, Phường Bến Thành, у моста Calmette.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134195294.htm","вчера",1,source="chotot",
  details={"contact":"Phương","notice":"⚠ в поле цены стоит 14 млн ₫, в тексте объявления — «14,5 млн ₫, ещё торг». Использована цена из поля; ориентируйтесь на 14-14,5 млн."}),

L(757,"ho-chi-minh","bth","Квартира",8000000,45,
  "1-спальная квартира 45 м² с большим балконом, полная меблировка, вход по отпечатку пальца, лифт, круглосуточная охрана. Ул. Nguyễn Thái Bình (новый Phường Bến Thành), пешком до рынка Bến Thành и ул. Nguyễn Huệ.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134192560.htm","вчера",1,source="chotot",
  details={"contact":"Trần Hưng"}),

L(758,"ho-chi-minh","bth","Дом",15000000,24,
  "Дом целиком, 3x8 м (Г-образный), цоколь + 2 этажа + терраса, 2 спальни, 4 с/у, кондиционеры в каждой комнате, солнечный водонагреватель. Переулок с автозаездом, ул. Calmette.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134174699.htm","2 дня назад",2,source="chotot",
  details={"contact":"Thuy Vi","notice":"залог 2 месяца. Тот же дом продвигают ещё два агента отдельными объявлениями — при обзвоне возможны повторы."}),

L(759,"ho-chi-minh","bth","Дом",7500000,15,
  "Дом на 2 фасада в переулке, цоколь + 1 этаж, 2 спальни, балкон, свежий ремонт, есть кондиционер, водонагреватель, кровать и шкаф. Пер. 265 Phạm Ngũ Lão (новый Phường Bến Thành), у парка 23/9 и ул. Bùi Viện.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134172340.htm","2 дня назад",2,source="chotot",
  details={"contact":"Dang Lam Son","notice":"⚠ в поле площади 15 м², в тексте — 30 м² общей площади (цоколь + этаж)."}),

L(760,"ho-chi-minh","bth","Дом",9000000,27,
  "Дом целиком без мебели, 3x9 м, цоколь + 1 этаж, 2 спальни, 1 с/у + душевая. Электричество и вода по государственному тарифу. Пер. 120 Trần Hưng Đạo, 5 минут пешком до Bùi Viện.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134166853.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trần Minh","notice":"цена «9 млн, торг»."}),

L(761,"ho-chi-minh","bth","Дом",7500000,27,
  "Дом целиком без мебели, 2,5x7 м, цоколь + 1 этаж, 2 спальни, 1 с/у. Электричество и вода по государственному тарифу. Пер. 217 Đề Thám (новый Phường Bến Thành), 2 минуты до Bùi Viện.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/133546031.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trần Minh"}),

L(762,"ho-chi-minh","bth","Дом",12000000,48,
  "Полностью отремонтированный дом от собственника, 4 уровня: цоколь + 2 этажа + терраса, 2 спальни. Пер. Đỗ Quang Đẩu / 12 Bùi Viện, ~30 м от главной улицы, рядом пешеходная Nguyễn Huệ.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/133509519.htm","3 дня назад",3,source="chotot",
  details={"contact":"Thiện Tâm"}),

L(763,"ho-chi-minh","btr","Дом",40000000,410,
  "Дом с гаражом, цоколь + 3 этажа, 4 большие спальни, 5 с/у. Ул. số 57, Bình Trưng, рядом река и парк, улица 10 м.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133295504.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(764,"ho-chi-minh","btr","Дом",55000000,420,
  "Вилла с гаражом и двором, цоколь + 3 этажа, 5 спален, 5 с/у, ориентация юго-восток. Ул. Đỗ Pháp Thuận, Bình Trưng.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133220885.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(765,"ho-chi-minh","btr","Дом",35000000,410,
  "Дом целиком 8x20 м, гараж + цоколь + 3 этажа, 5 спален, 5 с/у. Bình Trưng Tây, рядом с Đảo Kim Cương (Diamond Island). Собственник предпочитает договор на 2-5 лет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133295237.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(766,"ho-chi-minh","btr","Дом",35000000,400,
  "Дом с гаражом, цоколь + 3 этажа, 5 больших спален, 5 с/у. Ул. Lương Định Của, Bình Trưng, рядом парк и супермаркет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133309816.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(767,"ho-chi-minh","btr","Дом",40000000,390,
  "Вилла с гаражом и двором, цоколь + 3 этажа, 5 спален, 5 с/у, юго-восток. Ул. Nguyễn Hoàng, Bình Trưng.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133179629.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Nam"}),

L(768,"ho-chi-minh","btr","Дом",33000000,100,
  "Таунхаус в Lakeview City с видом на озеро, 5x20 м, площадь застройки 262 м², полностью меблирован премиум-мебелью. Ул. Song Hành, рядом Đỗ Xuân Hợp, Mai Chí Thọ и The Global City.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134208435.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng, Mana Homes","notice":"⚠ в поле площади 100 м² (участок), в тексте — 262 м² застройки."}),

L(769,"ho-chi-minh","btr","Дом",50000000,95,
  "Новый таунхаус в The Global City, 5x19 м, полезная площадь 400 м², цоколь + 4 этажа, лифт, кондиционеры, мебель на верхнем этаже. Ул. Đỗ Xuân Hợp.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/130746503.htm","сегодня",0,source="chotot",
  details={"contact":"Mr. Kha","notice":"⚠ в поле площади 95 м² (участок), в тексте — 400 м² полезной. У агента есть и другие дома в The Global City, 45-120 млн ₫."}),

L(770,"ho-chi-minh","btr","Квартира",18500000,98,
  "3-спальная квартира 98 м² в Cantavil An Phú, высокий этаж, хороший вид, полностью меблирована, заезд сразу. Ул. Thái Thuận, район An Phú An Khánh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/132957410.htm","сегодня",0,source="chotot",
  details={"contact":"Hằng"}),

L(771,"ho-chi-minh","btr","Дом",32000000,265,
  "Таунхаус в закрытом комплексе Lakeview City, 5x20 м, цоколь + 3 этажа, 5 спален, 6 с/у, полная меблировка. Бассейн, спортзал, кафе и ТЦ в радиусе 200 м, экопарк 3,6 га.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134159448.htm","3 дня назад",3,source="chotot",
  details={"contact":"Võ Hữu Nhân","notice":"залог 2 месяца."}),

L(772,"ho-chi-minh","th","Дом",8000000,25,
  "Небольшой дом целиком, 2 спальни, 2 с/у. Ул. Số 27, бывший Phường Tân Quy (новый Tân Hưng). Широкий переулок с автозаездом, без подтоплений.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134208795.htm","сегодня",0,source="chotot",
  details={"contact":"Việt Tiến"}),

L(773,"ho-chi-minh","th","Дом",35000000,120,
  "Дом на первой линии 6x20 м, цоколь + 3 этажа, 5 спален (3 с мебелью), 6 с/у, двор спереди и сзади, терраса. Бывший Phường Tân Quy, несколько минут до Lotte Mart, SC VivoCity и Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134208458.htm","сегодня",0,source="chotot",
  details={"contact":"Gia Gia","notice":"собственник разрешает жильё в сочетании с работой, но запрещает переоборудование под сервисные апартаменты (CHDV)."}),

L(774,"ho-chi-minh","th","Дом",30000000,80,
  "Дом на первой линии ул. Phan Huy Thực, 4x20 м, цоколь + 2 этажа, 4 спальни, 4 с/у. Оживлённый жилой квартал со всей инфраструктурой.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134208354.htm","сегодня",0,source="chotot",
  details={"contact":"Quốc Đạt"}),

L(775,"ho-chi-minh","th","Дом",10000000,44,
  "Дом целиком 4x11 м, 1 этаж, 2 спальни, 1 с/у, базовая мебель. Пер. 1041 Trần Xuân Soạn, Phường Tân Hưng. Рядом мост Him Lam, Lotte Mart, университеты Tôn Đức Thắng и RMIT.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134208072.htm","сегодня",0,source="chotot",
  details={"contact":"Anh Quan"}),

L(776,"ho-chi-minh","th","Квартира",17000000,76,
  "2-спальная квартира 76 м², 2 с/у, полная меблировка, ЖК Sunrise City, ул. Nguyễn Hữu Thọ.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/131393439.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Quốc Thịnh","notice":"у того же агента в Sunrise City есть и другие варианты (106 м² 2 спальни — 18 млн, 99 м² Central — 20 млн)."}),

L(777,"ho-chi-minh","th","Дом",6500000,44,
  "Дом в переулке, 3,8x13 м, цоколь с антресолью, 3 спальни, 1 с/у. Ул. Trần Xuân Soạn, Phường Tân Hưng. Мотобайковый переулок, счётчики по основному тарифу, свободен.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134207211.htm","сегодня",0,source="chotot",
  details={"contact":"Vinh","notice":"залог 1 месяц."}),

L(778,"ho-chi-minh","th","Дом",8000000,48,
  "Дом целиком 4x12 м, цоколь + этаж, 2 спальни, 2 с/у. Переулок 2 м (только мотобайки), ул. Lê Văn Lương, Phường Tân Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134206954.htm","сегодня",0,source="chotot",
  details={"contact":"Vinh","notice":"⚠ только под жильё, коммерческая деятельность запрещена; собственник просит небольшую семью. Залог 1 месяц + 1 месяц вперёд."}),

L(779,"ho-chi-minh","th","Студия",6000000,28,
  "Студия с большим балконом на зелень, деревянный пол, полная премиум-меблировка (ТВ, кондиционер, большой холодильник, обеденный стол, своя кухня). Вилловый квартал Dragon Parc 2, охрана 24/7, ул. Nguyễn Hữu Thọ.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134205789.htm","сегодня",0,source="chotot",
  details={"contact":"Quốc Thắng Nguyễn"}),

L(780,"ho-chi-minh","th","Дом",38000000,89,
  "Дом целиком от собственника: 46 Mai Văn Vĩnh, Phường Tân Hưng, 50 м от перекрёстка с Nguyễn Thị Thập, оживлённый район рядом со школами, супермаркетом и рынком.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/127890819.htm","сегодня",0,source="chotot",
  details={"contact":"Thảo Thanh (собственник)","notice":"в одном объявлении сдаются два разных дома — второй по адресу 1172/12 Huỳnh Tấn Phát, Phường Tân Mỹ (4x18 м, цоколь + 2 этажа + терраса, 5 спален). Цена 38 млн ₫ относится к объекту на Mai Văn Vĩnh."}),

L(781,"ho-chi-minh","th","Дом",19000000,120,
  "Дом-вилла 8x15 м, цоколь + 1 этаж, 4 спальни, 2 с/у, гостиная, кухня, двор под машину. Пер. 1041 Trần Xuân Soạn, Phường Tân Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133904642.htm","сегодня",0,source="chotot",
  details={"contact":"LHP"}),

L(782,"ho-chi-minh","th","Дом",10000000,44,
  "Дом целиком 4x11 м, цоколь + этаж, 2 спальни, 1 с/у. Мебель: 2 кондиционера, стиральная машина, холодильник, водонагреватель, фильтр для воды, кухонный гарнитур. Пер. Trần Xuân Soạn рядом с Him Lam.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134200854.htm","вчера",1,source="chotot",
  details={"contact":"Gia Gia"}),

L(783,"ho-chi-minh","th","Дом",12000000,72,
  "Дом 4x18 м, цоколь + 1 этаж, 3 спальни, 2 с/у, гостиная, кухня, двор под машину. Ул. Trần Xuân Soạn, Phường Tân Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133808666.htm","вчера",1,source="chotot",
  details={"contact":"LHP"}),

L(784,"ho-chi-minh","th","Дом",10000000,30,
  "Новый дом целиком 3x10 м, цоколь + 1 этаж, 2 спальни, 2 с/у, 2 новых кондиционера, просторная кухня. Пер. 108 Lê Văn Lương, выход к мосту Kênh Tẻ — 5 минут до Quận 4.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134200113.htm","вчера",1,source="chotot",
  details={"contact":"Mec Nguyễn","notice":"⚠ домашние животные запрещены. Электричество и вода по государственному тарифу, оплата помесячно с залогом за месяц."}),

L(785,"ho-chi-minh","th","Студия",4500000,35,
  "Передача аренды дома целиком с антресолью, полная меблировка (кондиционер, холодильник, стиральная машина, большой шкаф, газовая плита). Крытый двор под сушку белья и 3-4 мотобайка. Пер. 791 Trần Xuân Soạn.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134199483.htm","вчера",1,source="chotot",
  details={"contact":"Anh Đức","notice":"заезд возможен с начала сентября 2026. 2 км до университетов Tài chính-Marketing и Tôn Đức Thắng."}),

L(786,"ho-chi-minh","th","Дом",15000000,110,
  "Одноэтажный дом на первой линии, 5x22 м, 2 спальни, 2 с/у, 2 кондиционера. Ул. số Lâm Văn Bền, бывший Phường Tân Quy.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134197944.htm","вчера",1,source="chotot",
  details={"contact":"Lê Vân BĐS","notice":"этажей нет — только цоколь."}),

L(787,"ho-chi-minh","th","Квартира",12000000,63,
  "2-спальная квартира 63 м², 1 с/у, с мебелью, ЖК M-One Nam Sài Gòn, бывший Phường Tân Kiểng. Бассейн, спортзал, спа, супермаркет, BBQ, парк вдоль реки.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/132046796.htm","вчера",1,source="chotot",
  details={"contact":"Hữu Nhân","notice":"у агента в этом ЖК есть и другие квартиры."}),

L(788,"ho-chi-minh","th","Дом",9700000,35,
  "Новый дом целиком, 2 спальни, полная новая меблировка, рассчитан на 2-4 человек. Ул. Trần Xuân Soạn, Phường Tân Hưng. Рядом Quận 1 и 4, университеты TĐT и RMIT.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133812034.htm","вчера",1,source="chotot",
  details={"contact":"Hang Pham","notice":"можно с животными и электробайком, цена обсуждается."}),

L(789,"ho-chi-minh","th","Студия",4500000,35,
  "Дуплекс-студия с балконом и полной меблировкой, большое окно. Ул. Nguyễn Thị Thập, напротив университета Tôn Đức Thắng, рядом UFM, NTTU, RMIT и Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134196108.htm","вчера",1,source="chotot",
  details={"contact":"Nhật Thiên","notice":"⚠ цена «от»: в объявлении диапазон 4,5-6 млн ₫ в зависимости от комнаты, ориентировано на студентов, в том числе подселение."}),

L(790,"ho-chi-minh","th","Дом",130000000,300,
  "Вилла Nam Thông I, 300 м², цоколь + 3 этажа, 5 спален, бассейн, премиум-мебель, 2 фасада. Напротив Канадской международной школы, Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134192547.htm","вчера",1,source="chotot",
  details={"contact":"Thảo","notice":"верхний ценовой сегмент — для ориентира по рынку вилл Phú Mỹ Hưng."}),

L(791,"ho-chi-minh","th","Дом",12000000,40,
  "Дом 8x6 м, цоколь + 3 этажа, 3 спальни (по одной на этаж), 4 с/у, большие балконы. Широкий переулок, ул. Lê Văn Lương, Tân Hưng. 200 м до университета Tôn Đức Thắng, 100 м до Lotte.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134192034.htm","вчера",1,source="chotot",
  details={"contact":"Phạm Tăng","notice":"цена обсуждается."}),

L(792,"ho-chi-minh","th","Студия",7000000,25,
  "Новая сервисная студия: окно, отдельный балкон, полная новая меблировка (кровать, шкаф, кондиционер, холодильник, рабочий стол, водонагреватель), своя кухня и с/у, wi-fi, камеры 24/7. Ул. Số 36, Phường Tân Hưng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133510216.htm","вчера",1,source="chotot",
  details={"contact":"Duy Tân","notice":"в здании несколько типов комнат по разным ценам — 7 млн ₫ относится к описанному варианту."}),

L(793,"ho-chi-minh","th","Студия",6000000,40,
  "Двухуровневый дуплекс с балконом, полная премиум-меблировка, оборудованная кухня, свободный режим входа. Ул. Số 37, Phường Tân Hưng. Несколько минут до Lotte Mart, SC VivoCity, TDTU, RMIT, UFM и Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133741374.htm","вчера",1,source="chotot",
  details={"contact":"Nhật Thiên Airways Unitegroup"}),

L(794,"ho-chi-minh","th","Студия",5500000,40,
  "Квартира-студия с отдельным балконом, полная меблировка, современный ремонт. Ул. Nguyễn Thị Thập, Tân Hưng — рядом TDTU, Lotte Mart, NTTU, удобный выезд в Quận 1, 4, 8 и Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134189415.htm","вчера",1,source="chotot",
  details={"contact":"Nguyễn Hữu Quyết"}),

L(795,"ho-chi-minh","th","Дом",25000000,150,
  "Цокольный этаж виллы с отдельным входом, 7,5x20 м, готовые комнаты с кондиционерами, двор спереди и сзади, свободная парковка у дома. Квартал Him Lam, Tân Hưng, напротив парка.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134187797.htm","вчера",1,source="chotot",
  details={"contact":"Nguyễn Hoàng Minh Sơn, S Home","notice":"сдаётся только цокольный этаж виллы, не дом целиком."}),

L(796,"ho-chi-minh","th","Дом",15000000,100,
  "Цокольный этаж виллы 5x20 м в квартале Him Lam Tân Hưng, напротив парка, двор спереди и сзади, свободная парковка. Заезд сразу.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134187999.htm","вчера",1,source="chotot",
  details={"contact":"Nguyễn Hoàng Minh Sơn, S Home","notice":"сдаётся только цокольный этаж виллы. ⚠ в заголовке 5x18 м, в тексте 5x20 м (100 м²)."}),

L(797,"ho-chi-minh","th","Студия",5800000,40,
  "Дуплекс с полной меблировкой и собственной стиральной машиной, просторно и приватно, на 1-2 человек. Ул. Trần Xuân Soạn, Quận 7. Рядом TDTU, RMIT, UFM.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134175843.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nhật Thiên Airways Unitegroup"}),

L(798,"ho-chi-minh","th","Студия",5500000,43,
  "Квартира с антресолью и дизайнерским ремонтом, деревянный пол, своя стиральная машина, большой холодильник, кондиционер, шкаф, обеденная зона, просторная кухня. Ул. Trần Xuân Soạn у мостов Rạch Ông и Him Lam.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134175552.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phong Nguyễn","notice":"в здании есть комнаты от 5 до 8 млн ₫ — 5,5 млн относится к описанной."}),

L(799,"ho-chi-minh","th","Студия",5400000,27,
  "Квартира с высокой антресолью на 3 человек, 2 больших панорамных окна, кондиционер, шкаф, отдельная кухонная зона, свой с/у. Есть лифт, камеры 24/7, вход по отпечатку, свободный режим, без подселения к хозяевам. Ул. Lê Văn Lương у рынка Tân Quy и Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134174630.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phong Nguyễn"}),

L(800,"ho-chi-minh","th","Студия",6000000,40,
  "Мини-квартира в жилом квартале Kim Sơn напротив университетов TĐT и RMIT (пешком). Полная современная меблировка, свободный режим, камеры 24/7, вход по отпечатку, лифт, пожарная система, парковка, общая стирально-сушильная зона, скоростной интернет и кабельное.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134172290.htm","2 дня назад",2,source="chotot",
  details={"contact":"агент «Hà cho thuê căn hộ mini Quận 7»"}),

L(801,"ho-chi-minh","th","Квартира",15000000,71,
  "Угловая 2-спальная квартира 71 м² с собственным садом-террасой 12 м², 3-й этаж, вид на VivoCity. ЖК Sky Garden 1, ул. Phạm Văn Nghị. Мебель: 3 новых кондиционера, кровать, новый холодильник, полностью оборудованная кухня.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133245543.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phạm Hồng Đức","notice":"цена включает эксплуатационный сбор и интернет. Ограничение: до 4 человек, без кошек и собак. Рядом больницы FV и Tâm Đức, парк Hồ Bán Nguyệt."}),

L(802,"ho-chi-minh","th","Студия",5000000,35,
  "Сервисная студия с балконом и отдельной кухней, полная меблировка, свежая уборка, заезд сразу. Ул. Mai Văn Vĩnh, центр Quận 7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134165695.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trịnh Hữu Nghị","notice":"при заезде в текущем месяце собственник обещает скидку 2 млн ₫."}),

L(803,"ho-chi-minh","tm","Квартира",22000000,82,
  "2-спальная квартира 82 м² в The Infiniti at Riviera Point, ул. Huỳnh Tấn Phát, бывший Phường Tân Phú (новый Tân Mỹ). Агент позиционирует как «2 спальни по цене однушки».",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-huynh-tan-phat-phuong-tan-phu-19-the-infiniti-riviera-point/cho-nhanh-2pn-gia-re-chi-bang-1pn-tro-xem-nha-24-7-pr46188496","2 дня назад",2,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «2 дня» это её собственная отметка. Цена 22 млн ₫ подтверждена дважды: в карточке выдачи и в блоке параметров объявления."}),

L(804,"ho-chi-minh","bth","Комната",4600000,20,
  "Студенческая комната 20 м² с окном, полностью оборудована. Ул. Phạm Ngũ Lão (новый Phường Bến Thành), рядом с улицей Bùi Viện, самый центр Q1.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-pham-ngu-lao-phuong-pham-ngu-lao-1-53/trong-sinh-vien-20m2-cua-so-full-tien-nghi-gia-chi-4x-ngay-trung-tam-gan-pho-bui-vien-q1-pr46194018","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 4,6 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(805,"ho-chi-minh","bth","Дом",10000000,21,
  "Дом 21 м², 2 этажа, ул. Lê Thị Riêng, Phường Bến Thành.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-thi-rieng-phuong-ben-thanh-53/cho-21m-2-tang-10-trieu-thang-pr46193043","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 10 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Описание у объявления очень краткое."}),

L(806,"ho-chi-minh","bth","Дом",20000000,36,
  "Дом 36 м², 4 этажа, ул. Tôn Thất Tùng (новый Phường Bến Thành).",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ton-that-tung-phuong-pham-ngu-lao-1-53/cho-36m-4-tang-20-trieu-thang-pr46192981","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 20 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Описание у объявления очень краткое."}),

L(807,"ho-chi-minh","bth","Дом",23000000,60,
  "Дом 60 м², 1 этаж, ул. Nguyễn Du, Phường Bến Thành.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-du-phuong-ben-thanh-53/cho-60m-1-tang-23-trieu-thang-pr46192828","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 23 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Описание у объявления очень краткое."}),

L(808,"ho-chi-minh","bth","Дом",18000000,36,
  "Дом 36 м², 1 этаж, ул. Thủ Khoa Huân, Phường Bến Thành — рядом с рынком Bến Thành.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-thu-khoa-huan-phuong-ben-thanh-53/cho-36m-1-tang-18-trieu-thang-pr46192816","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 18 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Описание у объявления очень краткое."}),

L(809,"ho-chi-minh","bth","Студия",6500000,45,
  "Студия с балконом 45 м², ул. Bùi Thị Xuân (новый Phường Bến Thành), самый центр Quận 1.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-bui-thi-xuan-phuong-pham-ngu-lao-1-53/studio-ban-cong-ngay-trung-tam-quan-1-pr46183646","3 дня назад",3,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «3 дня» это её собственная отметка. Цена 6,5 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(810,"ho-chi-minh","th","Дом",10000000,34,
  "Дом целиком в квартале Him Lam, 2 этажа, 2 комнаты, 34 м². Ул. Trần Xuân Soạn, Phường Tân Hưng.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-tran-xuan-soan-phuong-tan-hung-14-59/cho-nguyen-can-kdc-himlam-2-tang-2-phong-34m2-10tr-thang-pr46191418","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 10 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(811,"ho-chi-minh","th","Комната",5700000,30,
  "Комната 30 м² в доме 70 по ул. Nguyễn Văn Quỳ, бывший Phường Tân Kiểng (новый Tân Hưng). Свежий ремонт, много удобств поблизости.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-van-quy-phuong-tan-kieng-59/cho-70-5-7-trieu-30-m2-ep-nhieu-tien-ich-pr46190981","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 5,7 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(812,"ho-chi-minh","th","Комната",6000000,35,
  "Комната 35 м² с полной меблировкой, ул. Số 2, квартал Kim Sơn, бывший Phường Tân Phong (новый Tân Hưng). Напротив университета Tôn Đức Thắng и академии Cảnh sát Nhân dân.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-so-2-phuong-tan-phong-9-khu-dan-cu-kim-son/cho-full-noi-that-35m-oi-dien-h-ton-uc-thang-canh-sat-nhan-quan-7-pr46189179","вчера",1,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «вчера» это её собственная отметка. Цена 6 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(813,"ho-chi-minh","th","Комната",5800000,30,
  "Комната типа «master» 30 м² в ЖК Hoàng Anh Gia Lai 3, ул. Nguyễn Hữu Thọ, Phường Tân Hưng. Рядом университеты TDTU, UFM, RMIT.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-huu-tho-phuong-tan-hung-14-59/uu-tien-cho-sv-master-trong-chung-cu-hagl3-gan-h-tdtu-ufm-rmit-pr46184693","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 5,8 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Объявление ориентировано на студентов (подселение в квартире)."}),

L(814,"ho-chi-minh","th","Комната",4700000,20,
  "Комната 20 м², ул. 9A, Phường Tân Hưng. Рядом университеты Tôn Đức Thắng, RMIT и педагогический.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-9a-phuong-tan-hung-14-59/cho-gan-h-t-tu-rmit-su-pham-pr46184329","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 4,7 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),

L(815,"ho-chi-minh","th","Комната",4500000,20,
  "Комната 20 м² в ЖК Hồng Lĩnh, ул. 9A, Phường Tân Hưng. Рядом TDTU, RMIT и педагогический университет.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-9a-phuong-tan-hung-14-59/uu-tien-cho-sv-trong-chung-cu-hong-linh-gan-h-tdtu-rmit-h-su-pham-pr46184234","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 4,5 млн ₫ подтверждена в карточке выдачи и в блоке параметров. Объявление ориентировано на студентов (подселение)."}),

L(816,"ho-chi-minh","th","Дом",12000000,80,
  "Дом целиком 80 м², 2 спальни, 2 с/у, просторный, свежий ремонт. Район Lotte Mart, ул. Trần Xuân Soạn, Phường Tân Hưng.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-tran-xuan-soan-phuong-tan-hung-14-59/cho-nguyen-can-khu-vuc-lotte-mart-2pn-2wc-cuc-ki-rong-rai-ep-moi-lam-pr46169030","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» это её собственная отметка. Цена 12 млн ₫ подтверждена в карточке выдачи и в блоке параметров."}),
L(817,"ho-chi-minh","bth","Дом",112000000,55,
  "Дом 5,5x10 м, цоколь + 3 этажа, открытая планировка каждого этажа (под самостоятельную отделку). Ул. Nguyễn Thị Nghĩa, Phường Bến Thành. Оживлённый торговый район с большим потоком туристов, подходит под разные виды бизнеса.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/133890460.htm","вчера",1,source="chotot",
  details={"contact":"Trần Nguyễn Bảo Ngọc","notice":"⚠ цена в объявлении указана в долларах — 4300 USD/мес (≈112 млн ₫ по курсу на момент публикации), залог 3 месяца. Помещение без внутренней отделки/перегородок, больше подходит под коммерческое использование, чем под обычное жильё."}),

L(818,"ho-chi-minh","th","Квартира",8500000,40,
  "1-спальная квартира с отдельной кухней, окно и балкон в каждой комнате. Полная меблировка: кровать, шкаф, холодильник, кухонный гарнитур, кондиционер, рабочий стол. Лифт, подземный паркинг, парк рядом, круглосуточная охрана и камеры. Рядом Lotte Mart, UFM, TDTU, RMIT.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134201496.htm","вчера",1,source="chotot",
  details={"contact":"Phương Nam"}),

L(819,"ho-chi-minh","th","Квартира",5000000,30,
  "1-комнатная квартира с балконом напротив RMIT и TDTU, сдаёт лично собственник (фото реальные). Мебель: кровать, шкаф, холодильник, кондиционер, кулер с водой. Общая зона стирки.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134186111.htm","вчера",1,source="chotot",
  details={"contact":"Thắng Giá Thật","notice":"коммунальные платежи отдельно: свет 4 тыс.₫/кВт, вода+2 транспортных средства+управление+wifi — 200 тыс.₫ суммарно. До 2 жильцов, до 2 транспортных средств, можно с питомцами и детьми, иностранцам можно, электробайк без подзарядки."}),

L(820,"ho-chi-minh","th","Дом",25000000,72,
  "Дом на первой линии, ул. Số 30 (бывший APH, новый Phường Tân Hưng), 4x18 м, 3 этажа: цоколь + 5 комнат (у каждой свой с/у), терраса на 3-м этаже, ещё одна комната с с/у сзади, отдельная зона для стирки, просторный двор под машины.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134185850.htm","вчера",1,source="chotot",
  details={"contact":"Lực Villa Him Lam Quận 7","notice":"подходит под офис/спа/школу или другой бизнес, а не только под жильё."}),

L(821,"ho-chi-minh","th","Дом",50000000,142,
  "Вилла на первой линии, ул. Số 85 (бывший Tân Quy, новый Tân Hưng), 7x23 м, южная ориентация, цоколь + 2 этажа, 5 спален/5 с/у, новая постройка, большой двор под несколько машин. В 300 м — ЖК Hoàng Anh Gia Lai.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133708074.htm","вчера",1,source="chotot",
  details={"contact":"Phạm Tăng","notice":"подходит под офис, языковый центр, детсад, клинику/спа — упоминается как преимущество наравне с проживанием."}),

L(822,"ho-chi-minh","bq","Квартира",8000000,40,
  "1-спальная квартира с балконом у моста через канал, рядом с Тхань Да и университетом HUTECH. Полная меблировка, свободный график, отдельный вход (не совместно с хозяином), широкая улица с удобными выездами.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-binh-thanh-tp-ho-chi-minh/115633845.htm","вчера",1,source="chotot",
  details={"contact":"Đức Tư HiFriendz"}),

L(823,"ho-chi-minh","ak","Квартира",8000000,35,
  "Премиум-квартира-студия с широким светлым балконом, ул. Quốc Hương, Thảo Điền, рядом мост Sài Gòn (удобно до Q1, Q3, Q5, Q10, Bình Thạnh, Thủ Đức). Полная премиум-меблировка, еженедельная уборка, паркинг, лифт, охрана 24/7, можно с питомцами.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/116030187.htm","вчера",1,source="chotot",
  details={"contact":"Ngọc Thịnh Hifriendz","notice":"цена «от 8 млн» — за студийную комплектацию, у агента могут быть и другие варианты по этому адресу."}),

L(824,"ho-chi-minh","bth","Дом",15000000,24,
  "Дом целиком, свежий, переулок 29 с автомобильным заездом, ул. Calmette (бывшая Phường Nguyễn Thái Bình, Q1). 3x8 м, цоколь + 2 этажа + терраса: гостиная, 2 спальни, кухня, 4 с/у. Подходит для семьи или группы друзей, можно совмещать с онлайн-продажами.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134174076.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phạm Duy Luân","notice":"цена договорная. ⚠ дом на ул. Calmette, бывший Phường Nguyễn Thái Bình — по официальной реформе 2025 г. (Nghị quyết 1685/NQ-UBTVQH15) этот старый район был реально разделён между новыми Phường Sài Gòn и Phường Bến Thành, а не целиком ушёл в один из них. Chợ Tốt относит это объявление к Bến Thành (ward_name_v3); Calmette идёт вдоль канала Bến Nghé у восточного края бывшего района, рядом с новым Phường Cầu Ông Lãnh — по открытым источникам точная сторона границы для этой улицы не подтверждена однозначно. Для сравнения: два других объявления с этого же старого района (ул. Nguyễn Thái Bình, ID 655/657) получены напрямую с URL Batdongsan с явным `phuong-ben-thanh` в адресе — там принадлежность к Bến Thành подтверждена источником, а не выведена косвенно."}),

L(825,"ho-chi-minh","th","Квартира",6500000,50,
  "Новая сервисная квартира-дуплекс в мини-ЖК с балконом, ул. Số 75, рядом Lotte Mart, RMIT, TDTU. Лифт, большой подземный паркинг с охраной, отдельный вход (не общий с хозяином), свободный график.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134165501.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trịnh Hữu Nghị"}),

L(826,"ho-chi-minh","th","Квартира",7000000,35,
  "Квартира с большим балконом, полная меблировка, вход по отпечатку пальца, охрана, пожарная сигнализация. Ул. Nguyễn Thị Thập, рядом RMIT, TDTU, NTTU.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134180562.htm","2 дня назад",2,source="chotot",
  details={"contact":"Vũ Ngọc Anh","notice":"в заголовке объявления — «осталось всего 2 комнаты»: вероятно, часть мини-ЖК с несколькими похожими юнитами по этой цене."}),

L(827,"ho-chi-minh","th","Дом",30000000,76,
  "Новый дом на первой линии, ул. Phan Huy Thực, 4x19 м, 1 этаж + 2 лестничных пролёта + терраса, 4 спальни/4 с/у, свежий ремонт, светлая планировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134174430.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phan Thuận, B Đ S Phan Thuận","notice":"подходит и под жильё, и совместно под бизнес (офис/спа). Цена немного обсуждается."}),

L(828,"ho-chi-minh","ak","Квартира",10500000,50,
  "Отдельная 1-спальная квартира 50 м² с большим балконом, ул. Nguyễn Văn Hưởng, Thảo Điền. Полная меблировка, рядом метро, мост Sài Gòn, тоннель Thủ Thiêm, квартал Sala, удобно до Bình Thạnh, Q1, Q4, Q7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134168777.htm","2 дня назад",2,source="chotot",
  details={"contact":"Quỳnh Như HiFriendz","notice":"в объявлении указано «скоро освободится» — возможен небольшой срок ожидания перед заездом."}),

L(829,"ho-chi-minh","th","Квартира",6000000,30,
  "Новая квартира в мини-ЖК рядом с Lotte Mart, TDTU и RMIT, ул. Số 81 (бывший Tân Quy, новый Tân Hưng). Полная меблировка, своя стиральная машина, большие окна, лифт, вход по отпечатку пальца, камеры и пожарная сигнализация.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133395502.htm","3 дня назад",3,source="chotot",
  details={"contact":"Nhi Mira Hình Thật Giá Thật","notice":"доступна краткосрочная и долгосрочная аренда; при долгосрочной аренде к указанной цене добавляется 2 млн ₫."}),

L(830,"ho-chi-minh","th","Дом",10000000,35,
  "Дом в переулке 1041 Trần Xuân Soạn, Phường Tân Hưng, рядом мост Him Lam (5 минут до Lotte Mart). 3,5x10 м, 1 этаж, 2 спальни, 2 с/у, кондиционер, кухня, удобный автомобильный подъезд.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134151663.htm","3 дня назад",3,source="chotot",
  details={"contact":"Bđs Kiều Oanh","notice":"электричество и вода по государственному тарифу."}),

L(831,"ho-chi-minh","kh","Квартира",12000000,35,
  "1-спальная квартира со светлым балконом, ЖК Masteri Millennium, 132 Bến Vân Đồn, Phường 6 (новый Phường Khánh Hội). Полная меблировка, камеры, пожарная система.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-phuong-6-masteri-millennium/cho-studio-c-c-cao-cap-full-noi-that-tk-chi-tu-12tr-thang-q4-pr46196404","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» определено по тому, что ID объявления (pr46196404) оказался на самом верху дефолтной ленты района и выше максимального ID, виденного в сегодняшнем утреннем батче. Цена 12 млн ₫ подтверждена дважды: в карточке выдачи и в блоке «Khoảng giá» на странице объявления."}),

L(832,"ho-chi-minh","kh","Квартира",18700000,65,
  "2-спальная квартира 65 м², 2 с/у, с мебелью, балкон с видом на реку. ЖК Masteri Millennium, 132 Bến Vân Đồn, Phường 6 (новый Phường Khánh Hội). Бассейн, спортзал, зона BBQ, 3 минуты до центра Q1.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ben-van-don-phuong-6-masteri-millennium/cho-2pn-cc-milenium-132-on-6-quan-4-dien-tich-65m2-2pn-pr46195845","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» определено так же, как у ID 831 (топ ленты, ID выше вчерашнего максимума). Цена 18,7 млн ₫ подтверждена в карточке выдачи и в блоке «Khoảng giá». Заезд возможен до 28 августа."}),

L(833,"ho-chi-minh","ak","Дом",68000000,135,
  "Дом целиком, ул. Trần Não, Phường An Khánh, 6x23 м (135 м²), цоколь + 3 этажа + терраса, лифт, 5 спален/5 с/у. Рядом перекрёсток Lương Định Của, деловой район с офисами.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-tran-nao-phuong-an-khanh-2-71/cho-uong-thu-uc-dt-6x23m-ham-4-tang-68tr-thang-pr46195380","сегодня",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует точную дату создания объявления — «сегодня» определено так же, как у ID 831-832. Цена 68 млн ₫ подтверждена в карточке выдачи и в блоке «Khoảng giá». Собственник также предлагает дом под офис/бизнес — «подходит для проживания или совмещения с бизнесом»."}),
L(834,"ho-chi-minh","tm","Квартира",11000000,57,
  "2-спальная квартира в ЖК Q7 Boulevard, ул. Nguyễn Lương Bằng. Продуманная планировка, вид на реку с высокого этажа, очень тихо, хорошо проветривается.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134215711.htm","сегодня",0,source="chotot",
  details={"contact":"Tiền (Newhouse)"}),

L(835,"ho-chi-minh","tm","Дом",20000000,60,
  "Дом целиком у рынка Chợ Tân Mỹ (ул. Tân Mỹ): цоколь + антресоль + 2 этажа + терраса, 5 спален/3 с/у. Базовая меблировка. Подходит для семьи, компании друзей или под небольшой офис.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134211156.htm","сегодня",0,source="chotot",
  details={"contact":"Thanh Thủy"}),

L(836,"ho-chi-minh","th","Дом",20000000,72,
  "Дом целиком 4x18 м, цоколь + 1 этаж, 3 спальни/2 с/у, гостиная, кухня, место для машины. Бывший район Tân Kiểng, сейчас относится к Phường Tân Hưng. Подходит для проживания, интернет-торговли или под офис.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134209812.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Vân BĐS","notice":"⚠ в самом объявлении не указан номер улицы (только «Đường Số», без цифры) — адрес в источнике неполный."}),

L(837,"ho-chi-minh","th","Дом",20000000,76.5,
  "Дом целиком 4,5x17 м, цоколь + 1 этаж, 3 спальни. Ул. Phan Huy Thực (бывший район Tân Kiểng, сейчас Phường Tân Hưng). Подходит для семьи, офиса или онлайн-бизнеса.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134211833.htm","сегодня",0,source="chotot",
  details={"contact":"Văn Kiên","notice":"залог 2 месяца, оплата помесячно."}),

L(838,"ho-chi-minh","ak","Квартира",15000000,70,
  "1-спальная квартира с балконом, ул. Quốc Hương, Thảo Điền. Кондиционер, водонагреватель, кухня с гарнитуром, кровать, шкаф, холодильник, рабочий стол, своя стиральная/сушильная зона. Лифт, бассейн, спортзал, охрана 24/7, свободный график.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134215577.htm","сегодня",0,source="chotot",
  details={"contact":"Tony BĐS","notice":"у того же агента есть и другие варианты по этому же адресу — студии, 1-2-спальные, дуплекс, 5-20 млн ₫."}),

L(839,"ho-chi-minh","ak","Квартира",15500000,80,
  "2-спальная квартира 80 м² с гостиной, ул. Nguyễn Văn Hưởng, Thảo Điền. Кондиционер, водонагреватель, кухня с гарнитуром, кровать, шкаф, охрана 24/7, свободный график.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134215227.htm","сегодня",0,source="chotot",
  details={"contact":"Tony BĐS","notice":"тот же агент, что и у ID 838 — есть варианты по разным адресам в Thảo Điền."}),

L(840,"ho-chi-minh","ak","Дом",95000000,1000,
  "Вилла на участке 22x45 м (≈990 м²), ул. Nguyễn Văn Hưởng, Thảo Điền: цоколь + 1 этаж + 2 этажа, 5 спален/6 с/у, большой цокольный паркинг.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134214495.htm","сегодня",0,source="chotot",
  details={"contact":"Oanh Home","notice":"⚠ в объявлении здание позиционируется в первую очередь под офис/школу/спа/шоурум премиум-уровня, а не под обычное проживание — хотя структурно это вилла с 5 спальнями и 6 с/у."}),

L(841,"ho-chi-minh","bth","Квартира",10500000,45,
  "1-спальная квартира с балконом, ул. Ký Con, Bến Thành. Своя стиральная и сушильная машина, вход по отпечатку пальца, smart TV, отдельный интернет в каждой комнате, юридически чистый договор аренды, поддержка 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134215184.htm","сегодня",0,source="chotot",
  details={"contact":"Đạt","notice":"цена «от 10,5 до 16 млн ₫» — в зависимости от конкретной планировки/этажа в этом же доме; здесь указана нижняя граница."}),

L(842,"ho-chi-minh","kh","Квартира",7500000,45,
  "1-спальная квартира 45 м², светлая и просторная, подходит для 1-2 человек или пары. Полная меблировка: кровать, шкаф, диван, кондиционер, холодильник, кухня. Вход по отпечатку пальца, лифт, камеры, пожарная сигнализация. Рядом мост Cầu Ông Lãnh и рынок Xóm Chiếu, несколько минут до Q1 и Q7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134214546.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Hưng"}),

L(843,"ho-chi-minh","kh","Дом",30000000,72,
  "3-этажный дом 4x18 м целиком, на каждом этаже по 2 комнаты (перед/зад), отдельный въезд и задний выход, есть место для парковки байков. Можно снять как всё здание (30-35 млн ₫/мес) или отдельными комнатами с меблировкой (4-7 млн ₫/мес за комнату).",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134211238.htm","сегодня",0,source="chotot",
  details={"contact":"Phương Lê","notice":"⚠ на первом этаже с фасада сейчас работает кафе (действующий арендатор) — сдаётся не всё здание целиком свободным."}),

L(844,"ho-chi-minh","kh","Дом",6500000,45,
  "Дом от собственника, ул. Hoàng Diệu, Khánh Hội: гостиная, спальня, спальня-антресоль, кухня и санузел. Кондиционер, стиральная машина, 2 шкафа, вентилятор, диван и стол. 2 минуты до Q1, напротив Điện máy Chợ Lớn Q4, рядом кафе и рестораны.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134177271.htm","вчера",1,source="chotot",
  details={"contact":"Dung Phương"}),

L(845,"ho-chi-minh","kh","Дом",14000000,48,
  "Дом в переулке шириной 3,5 м, ул. Bến Vân Đồn, бывший округ P.9 (сейчас Phường Khánh Hội), рядом мост Cầu Ông Lãnh. 3x16 м, цоколь + антресоль, 2 спальни, 1 с/у, 2 кондиционера.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134153185.htm","3 дня назад",3,source="chotot",
  details={"contact":"cty bdsan Minh Đức"}),

L(846,"ho-chi-minh","bth","Дом",71000000,92,
  "Дом целиком в переулке ул. Lê Thị Hồng Gấm, Bến Thành, Q1: 3 этажа, 7 спален, общая площадь по этажам 276 м² (площадь участка 92 м²). Центр Q1, рядом рынок Bến Thành.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-thi-hong-gam-phuong-ben-thanh-53/cho-92m-3-tang-71-trieu-thang-pr46197409","сегодня",0,source="batdongsan",
  details={"notice":"⚠ в объявлении отмечено, что дом подходит под сервисные апартаменты или офис. Batdongsan не публикует точную дату создания объявления — «сегодня» определено по тому, что ID объявления (pr46197409) выше максимального ID, виденного в сегодняшних более ранних батчах (pr46196404). Цена 71 млн ₫ подтверждена дважды — в карточке выдачи и в блоке «Khoảng giá» на странице объявления."}),

L(847,"ho-chi-minh","th","Квартира",8000000,96,
  "2-спальная квартира 96 м², 2 с/у, от собственника, ЖК Hoàng Anh Gia Lai 2, 783 Trần Xuân Soạn, Tân Hưng. 2 встроенных шкафа, кухонный гарнитур сверху и снизу, отдельная кладовая. Без мебели — новый арендатор обустраивает по своему вкусу. Бассейн, охраняемый жилой комплекс; удобно до Q4, Q1, Phú Mỹ Hưng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-pho-tran-xuan-soan-phuong-tan-hung-14-hoang-anh-gia-lai-2/chinh-chu-cho-ii-tai-quan-7-dien-tich-96m-2pn-8-trieu-thang-pr46196899","сегодня",0,source="batdongsan",
  details={"notice":"цена 8 млн ₫ подтверждена дважды — в карточке выдачи и в блоке «Khoảng giá». Batdongsan не публикует точную дату — «сегодня» определено по тому же принципу (ID выше сегодняшнего утреннего максимума)."}),

L(848,"ho-chi-minh","tm","Квартира",30000000,80,
  "2-спальная квартира 80 м², 2 с/у, ЖК Midtown (кластер Hưng Phúc/Midtown/StarHill), Phú Mỹ Hưng. Полная премиум-меблировка, вид на бассейн и реку. Рядом Crescent Mall, мост Cầu Ánh Sao, международные школы.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-tan-phu-19-midtown-phu-my-hung/cho-1pn-2pn-3pn-view-ep-nhan-nha-ngay-pr46196496","сегодня",0,source="batdongsan",
  details={"contact":"Ngọc Mai","notice":"у агента есть и другие варианты в том же кластере (1-3-спальные, посуточно и на длительный срок). Цена 30 млн ₫ подтверждена дважды — в карточке выдачи и в блоке «Khoảng giá»."}),
L(849,"ho-chi-minh","th","Студия",5800000,35,
  "Студия 35 м² с балконом, ул. Trần Xuân Soạn, Tân Hưng. Полная премиум-меблировка: кровать, шкаф, кондиционер, холодильник, кухонный гарнитур, водонагреватель, отдельная стиральная машина. Рядом SC VivoCity, Lotte Mart Q7, Crescent Mall, международные школы, госпиталь FV.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134189594.htm","вчера",1,source="chotot",
  details={"contact":"Nhật Thiên Airways Unitegroup"}),

L(850,"ho-chi-minh","th","Дом",13000000,50,
  "Дом целиком, цоколь + 1 этаж, 2 комнаты, 50 м², в районе Kiều Đàm на ул. Trần Xuân Soạn, Tân Hưng. Широкий подъезд (заезд на машине/грузовике свободно), тихий безопасный квартал. Подходит для семьи или под небольшой офис.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133166016.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng Duy"}),
L(851,"ho-chi-minh","th","Комната",5000000,20,
  "Комната 20 м² в квартире-студии на ул. Trần Xuân Soạn, Tân Hưng (рассчитана на 2 девушек). Полная меблировка: кровать, шкаф, кондиционер, стиральная машина, кухня, окно. Тихий безопасный район, рядом Đại học Tôn Đức Thắng, Lotte Mart, остановки автобусов на Q1/Q4. Цена включает все платежи, торг возможен.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134219542.htm","сегодня",0,source="chotot",
  details={"contact":"Phượng Trần (Phoenix Trần)"}),

L(852,"ho-chi-minh","th","Квартира",20000000,76,
  "Квартира 2 спальни/2 санузла, 76 м², в ЖК Sunrise City View, ул. Nguyễn Hữu Thọ, Tân Hưng. Полная меблировка, просторный балкон с открытым видом. Сдаёт собственник напрямую. 10-15 минут до центральных районов города.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134218619.htm","сегодня",0,source="chotot",
  details={"contact":"Căn hộ giá tốt Quận 4"}),

L(853,"ho-chi-minh","th","Студия",4800000,50,
  "Новая мансардная студия (gác/лофт с окном) 50 м² на ул. Nguyễn Hữu Thọ, Tân Hưng. Полностью новая мебель, бесплатный бассейн и спортзал в комплексе, охраняемая вилла-зона. Рядом ДТУ, RMIT, NTTU — позиционируется под студентов.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134218187.htm","сегодня",0,source="chotot",
  details={"contact":"Auren T Nguyen"}),

L(854,"ho-chi-minh","th","Студия",6300000,30,
  "Квартира-студия 30 м² с балконом на Đường số 33, Tân Kiểng, Tân Hưng. Полная меблировка. Рядом Lâm Văn Bền, Trần Xuân Soạn, Nguyễn Thị Thập — 10-15 минут до Đại học Tôn Đức Thắng и RMIT.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134218081.htm","сегодня",0,source="chotot",
  details={"contact":"Mẫn Nhi"}),

L(855,"ho-chi-minh","th","Дом",25000000,72,
  "Дом целиком, 1 этаж + 2 надстройки, 4 спальни/3 санузла, 4x18 м (72 м²), фасад на переулочной улице в районе Tân Kiểng (старое название части Tân Hưng), Q7. Подходит и для жилья, и под небольшой офис компании.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134218405.htm","сегодня",0,source="chotot",
  details={"contact":"NGUYỄN HOA"}),

L(856,"ho-chi-minh","th","Студия",5200000,40,
  "Дуплекс-студия 40 м² на Đường số 79, Tân Hưng. Полная меблировка, отдельная стиральная машина, просторная комната. Отдельный вход, свободный график. Рядом Lotte Mart, Crescent Mall, КЭЗ Tân Thuận, RMIT, ДТУ, удобно до Q1/Q4.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134219039.htm","сегодня",0,source="chotot",
  details={"contact":"Dương Cần"}),
L(857,"ho-chi-minh","bth","Студия",6500000,40,
  "Меблированная мини-квартира (студия) 40 м² на ул. Bùi Viện, Bến Thành. Новая мебель, wifi, свободный график заселения. Рядом ĐH Khoa học Tự nhiên, ĐH Sư phạm, развлекательный квартал Bùi Viện.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134211907.htm","вчера",1,source="chotot",
  details={"contact":"Minh Khang"}),

L(858,"ho-chi-minh","th","Квартира",6000000,45,
  "1-спальная квартира с балконом, 45 м², в КДЦ Him Lam, ул. số 9, Tân Hưng. Полная меблировка: кровать, шкаф, диван, кондиционер, холодильник, кухня, водонагреватель, стиральная машина. Охраняемый комплекс, камеры 24/7, паркинг. Рядом RMIT, ĐH Tôn Đức Thắng, Crescent Mall, SC VivoCity, Lotte Mart Q7, до Q1/Q4/Q5 несколько минут.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133616242.htm","вчера",1,source="chotot",
  details={"contact":"Quang Vũ Unite"}),

L(859,"ho-chi-minh","th","Дом",13500000,80,
  "Дом (nhà cấp 4) на ул. số 12, старый район Tân Quy (сейчас часть Tân Hưng), Q7. Участок 4x20 м (80 м²), 1 спальня/1 санузел, кондиционер, задний двор с видом на реку. Новый ремонт, торг возможен.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134188757.htm","2 дня назад",2,source="chotot",
  details={"contact":"Ngọc Trang"}),

L(860,"ho-chi-minh","ak","Дом",80000000,250,
  "Вилла целиком на ул. Nguyễn Văn Hưởng, центр Thảo Điền. Участок 10x25 м (250 м²), цоколь + 1 этаж + 3 этажа, 5 спален, у каждой свой санузел, сад. Полная меблировка, можно заезжать сразу. Цена указана в объявлении как 3200 USD/мес (≈80 млн ₫ по текущему курсу). Подходит для семьи или экспатов, также предлагается под офис представительства компании.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133799419.htm","3 дня назад",2,source="chotot",
  details={"contact":"Phan Cường Rental D2","notice":"⚠ цена в объявлении дана в USD (3200 USD/мес), приведён пересчёт в донгах по текущему курсу."}),
L(861,"ho-chi-minh","bth","Студия",12000000,50,
  "Меблированная студия (сервисные апартаменты) 50 м² на ул. Ký Con, Bến Thành. Полная меблировка на фото, свободный график заселения, лифт, стирка отдельно, охрана 24/7. Рядом рынок Бен Тхань, вузы Văn Lang/OU/Luật, удобно до Q3/Q4/Q5/Q7/Thủ Đức.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134222845.htm","сегодня",0,source="chotot",
  details={"contact":"Minh Quân"}),

L(862,"ho-chi-minh","th","Дом",37000000,140,
  "Дом в жилом квартале (KDC) Tân Quy Đông, Tân Hưng, Q7. Участок 7x20 м (140 м²), 3 этажа + техэтаж (áp mái), 4 спальни.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134232627.htm","сегодня",0,source="chotot",
  details={"contact":"Ngọc Anh"}),

L(863,"ho-chi-minh","th","Дом",20000000,72,
  "Дом целиком, 1 этаж + 1 надстройка, в переулке в районе Tân Kiểng (старое название части Tân Hưng), Q7. Участок 4x18 м (72 м²), 3 спальни/2 санузла, гостиная, кухня, место для парковки. Подходит для жилья, также рассматривается как небольшой офис/для онлайн-бизнеса.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134230639.htm","сегодня",0,source="chotot",
  details={"contact":"Gia Gia"}),

L(864,"ho-chi-minh","th","Квартира",15000000,50,
  "1-спальная квартира в ЖК Lavida Plus, Tân Hưng, Q7. Полная меблировка, чистая, свободна — можно заезжать сразу. Рядом Nguyễn Văn Linh/Nguyễn Hữu Thọ, напротив SC VivoCity, рядом RMIT и Đại học Tôn Đức Thắng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134235598.htm","сегодня",0,source="chotot",
  details={"contact":"hà pihomes"}),

L(865,"ho-chi-minh","kh","Дом",4500000,12,
  "Маленький дом целиком в Q4 (Khánh Hội), 12 м² основания, 1 этаж + мезонин (lửng) + 1 надстройка, 1 санузел. Рядом рынок и школа, подъезд по переулку. Электричество/вода по основному тарифу. Сдаёт собственник напрямую.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134218900.htm","сегодня",0,source="chotot",
  details={"contact":"C Thanh (собственник)"}),

L(866,"ho-chi-minh","kh","Дом",30000000,58,
  "Дом целиком на фасадной улице Đoàn Văn Bơ, Q4 (Khánh Hội), новое строительство. Участок 3,2x18 м (58 м²), 2 этажа + терраса на крыше, 3 просторные спальни. Долгосрочный договор. В объявлении отдельно указано: общепит (đồ ăn uống) не разрешён.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134229291.htm","сегодня",0,source="chotot",
  details={"contact":"Mr. Khánh"}),

L(867,"ho-chi-minh","tm","Квартира",65000000,242,
  "Пентхаус в ЖК Star Hill, Phú Mỹ Hưng, Q7. Угловая квартира с открытым видом, 242 м², 3 спальни/3 санузла, полная меблировка, просторный сад/терраса, 2 паркоместа. Свободна, можно заезжать сразу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134207519.htm","вчера",1,source="chotot",
  details={"contact":"Minh Hiếu Phú Mỹ Hưng"}),

L(868,"ho-chi-minh","tm","Дом",9000000,45,
  "Дом целиком рядом с Phú Mỹ Hưng (ул. Huỳnh Tấn Phát), Q7. 45 м², 1 этаж + антресоль, 2 спальни/2 санузла. Тихий безопасный район, рядом школы и супермаркет. Меблировка как на фото. Депозит 1 месяц, возможна краткосрочная аренда.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134207572.htm","вчера",1,source="chotot",
  details={"contact":"Tấn Phát"}),

L(869,"ho-chi-minh","tm","Квартира",23000000,71,
  "2-спальная квартира в ЖК Scenic Valley 1, Phú Mỹ Hưng, вид на Crescent Mall. 71 м², 2 санузла, полная меблировка, заезд сразу. Бассейн, спортзал, охрана 24/7, крытый паркинг.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134189104.htm","2 дня назад",2,source="chotot",
  details={"contact":"Aley"}),

L(870,"ho-chi-minh","tm","Дом",65000000,126,
  "Вилла-таунхаус (biệt thự liền kề) в центре Phú Mỹ Hưng, рядом парк Nam Viên. Участок земли 7x18 м, 4 спальни (все мастер-спальни со своим санузлом) + 1 доп. санузел, место для авто во дворе. Бассейн, спортзал, зона барбекю, охрана 24/7 в комплексе. Премиальная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134235697.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng Trúc Loan"}),

L(871,"ho-chi-minh","ak","Дом",65000000,250,
  "Дом целиком рядом с рекой Сайгон, район An Khánh (старое название An Phú), Thủ Đức. Подвал для авто + 3 этажа, 5 просторных спален, 6 санузлов, рядом парк и река. Новый ремонт, современный дизайн. Подходит для проживания или под офис компании.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-an-phu/a-duy-can-cho-gan-song-sai-gon-view-cong-vien-ham-4-lau-5-phong-co-noi-that-chi-65-trieu-pr46201315","проверено 19 авг",0,source="batdongsan",
  details={"contact":"Namland","notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления (prNNNNNNNN) — выше максимального ID, зафиксированного как уже виденный в проверках по состоянию на 18 авг (46197409). Цена подтверждена дважды: в карточке поиска и на странице объявления (поле «Khoảng giá»)."}),

L(872,"ho-chi-minh","ak","Дом",25000000,120,
  "Дом, недавно отремонтирован (новая покраска), в центре района An Khánh (старое название An Phú), Thủ Đức. Двор для парковки + 2 этажа, 120 м², 4 комнаты. Подходит для проживания или под офис компании.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-an-phu/chi-duyen-cho-moi-son-sua-3-tang-4-phong-moi-ngay-trung-tam-e-o-van-phong-pr46200789","проверено 19 авг",0,source="batdongsan",
  details={"contact":"Namland","notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления (prNNNNNNNN) — выше максимального ID, зафиксированного как уже виденный в проверках по состоянию на 18 авг (46197409). Цена подтверждена дважды: в карточке поиска и на странице объявления (поле «Khoảng giá»)."}),

L(873,"ho-chi-minh","tm","Дом",30000000,80,
  "Дом целиком, ~300 м от рынка Tân Mỹ (старый центр Q7), Phường Tân Mỹ. Участок 4x20 м (80 м²), 3 этажа, 5 спален, отделка как на фото.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-12-phuong-tan-phu-19-59/cho-nguyen-can-uong-so-p-quan-7-nay-la-my-tp-hcm-ngay-cho-my-pr46202495","проверено 19 авг",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления (prNNNNNNNN) — выше максимального ID, зафиксированного как уже виденный в проверках по состоянию на 18 авг (46197409). Цена подтверждена дважды: в карточке поиска и на странице объявления (поле «Khoảng giá»). Этот же объект (тот же адрес-ориентир, площадь и цена) также был замечен опубликованным под 4 разными аккаунтами на Chợ Tốt — добавлена только эта версия во избежание задвоения."}),

L(874,"ho-chi-minh","tm","Дом",20000000,90,
  "Дом в жилом квартале (KDC/переселенческий) Phú Mỹ, Phường Tân Mỹ. Участок 5x18 м (90 м²), 1 этаж + 1 надстройка, 2 спальни/2 санузла, заезд авто во двор, базовая меблировка. Подходит для проживания, под небольшой офис или онлайн-бизнес.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-hoang-quoc-viet-phuong-phu-my-9-khu-dan-cu-phu-my/cho-kdc-20tr-thang-pr46199104","проверено 19 авг",0,source="batdongsan",
  details={"notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления (prNNNNNNNN) — выше максимального ID, зафиксированного как уже виденный в проверках по состоянию на 18 авг (46197409). Цена подтверждена дважды: в карточке поиска и на странице объявления (поле «Khoảng giá»)."}),
L(875,"nha-trang","lt","Студия",14000000,45,
  "Меблированная студия A1402 (вид на город) в комплексе Panorama на набережной Trần Phú. Балкон, есть кухня.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134236286.htm","сегодня",0,source="chotot",
  details={"amenities":"бесплатный бассейн и спортзал (6 этаж)","policy":"животные не принимаются","contact":"Hà Lương IT"}),

L(876,"nha-trang","lt","Квартира",27000000,70,
  "2-спальная квартира (2 с/у) на 12 этаже башни Nam в комплексе Gold Coast, набережная Trần Phú.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134235652.htm","сегодня",0,source="chotot",
  details={"deposit":"2 месяца (оплата за 1)","contact":"Hà Lương IT"}),

L(878,"nha-trang","vp","Квартира",10000000,65,
  "2-спальная квартира (2 с/у) в комплексе Mường Thanh Viễn Triều, 03 Phạm Văn Đồng, Vĩnh Phước — напротив пляжа Hòn Chồng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134235623.htm","сегодня",0,source="chotot",
  details={"amenities":"бассейн и спортзал в комплексе, ТЦ на 1 этаже, рядом больница и школа (50 м), рынок Vĩnh Hải (500 м)","notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Nguyễn Tuấn Đại"}),

L(879,"nha-trang","vh","Квартира",9000000,60,
  "2-спальная квартира (2 с/у), этаж 4, башня A1, ЖК Hoàng Quân, Бắc Нячанг. До моря 800 м.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134226591.htm","сегодня",0,source="chotot",
  details={"deposit":"2 месяца (оплата за 1)","contact":"Hà Lương IT"}),

L(880,"nha-trang","vh","Дом",20000000,110,
  "Дом целиком, новый ремонт, район Vĩnh Hoà (старое название, ближайший район проекта — Vĩnh Hải), 1 этаж + мезонин. 3 спальни, 2 с/у.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134215272.htm","вчера",1,source="chotot",
  details={"deposit":"2 месяца (оплата за 2)","electricity":"по гостарифу","water":"по гостарифу","contract":"от 1 года","contact":"Phương GoHome"}),

L(881,"nha-trang","vh","Дом",15000000,100,
  "Дом целиком (угловой участок), район Vĩnh Hải, городской квартал (KĐT), 3 этажа, 4 спальни, 2 с/у, гараж, крыша-терраса. 500 м до рынка Vĩnh Hải.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134187565.htm","2 дня назад",2,source="chotot",
  details={"deposit":"3 месяца (оплата за 3)","electricity":"по гостарифу","water":"по гостарифу","contract":"более 1 года","notice":"общепит не разрешён","contact":"Phương GoHome"}),

L(882,"nha-trang","pl","Квартира",10000000,65,
  "Угловая 2-спальная квартира (2 с/у) с балконом, ЖК CT4 Hud, ул. 28, КДТ Phước Long.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134184961.htm","2 дня назад",2,source="chotot",
  details={"deposit":"2 месяца (оплата за 2)","contact":"Hà Lương IT"}),

L(883,"nha-trang","ph","Квартира",10000000,67,
  "2-спальная квартира (2 с/у) в ЖК CT2 VCN Phước Hải. 3 кондиционера, 2 ТВ, водонагреватель, электроплита, стиралка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134206429.htm","вчера",1,source="chotot",
  details={"notice":"цена не включает сервис-сбор, электричество/воду, wifi и прочие расходы по управлению"}),

L(884,"nha-trang","ph","Дом",22000000,100,
  "Дом целиком, КДТ Hà Quang 1. 1 этаж + 3 надстройки, 4 спальни, 5 с/у, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134208448.htm","вчера",1,source="chotot",
  details={"deposit":"2 месяца (оплата за 1)","contact":"Hà Lương IT"}),

L(885,"nha-trang","vt","Дом",26000000,100,
  "Дом целиком, новое строительство, КДТ Mỹ Gia (старый район — Vĩnh Thái, по прецеденту проекта ближайший район — Vĩnh Trường). 3 этажа + техэтаж, 3 спальни, 4 с/у, двор.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/133827595.htm","вчера",1,source="chotot",
  details={"deposit":"2 месяца (оплата за 2)","electricity":"по гостарифу","water":"по гостарифу","contract":"1-3 года"}),

L(886,"nha-trang","ps","Дом",22000000,102,
  "Дом-магазин (1 этаж свободной планировки под бизнес + 2 этажа жилых комнат), район Vĩnh Hiệp рядом с супермаркетом GO! (район близок к Vĩnh Điềm Trung, по прецеденту проекта — Phương Sài). Терраса на крыше.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134187463.htm","2 дня назад",2,source="chotot",
  details={"deposit":"4 месяца (оплата за 3)","contract":"от 2 лет","notice":"первый этаж пустой под коммерцию, 2-3 этажи — жилые комнаты","contact":"Phương GoHome"}),

L(887,"nha-trang","ph2","Дом",25000000,58,
  "Дом-магазин на оживлённой ул. Nguyễn Thị Minh Khai, район Phước Hòa, рядом с «русским кварталом». 1 этаж + 2 надстройки, первый этаж свободный под бизнес, 4 комнаты, 3 с/у.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134187349.htm","2 дня назад",2,source="chotot",
  details={"deposit":"2 месяца (оплата за 3)","electricity":"по гостарифу","water":"по гостарифу","amenities":"4 кондиционера, 2 водонагревателя","notice":"первый этаж пустой под коммерцию","contact":"Phương GoHome"}),

L(888,"nha-trang","vn","Дом",20000000,100,
  "Дом целиком, квартал Tô Hiệu, ЖК Mipeco, район Vĩnh Nguyên. 4 этажа, 5 спален, 6 с/у. До моря 500 м. Можно заселяться сразу.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134191590.htm","2 дня назад",2,source="chotot",
  details={"deposit":"2 месяца (оплата за 2)","notice":"подходит и для проживания, и под небольшой офис (вторично)","contact":"Hà Văn Trạch"}),

L(889,"da-lat","lv","Квартира",6000000,40,
  "2-спальная квартира (мебель) на ул. Mê Linh, район Lâm Viên (старое — Phường 9), 7 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134187126.htm","2 дня назад",2,source="chotot",
  details={"electricity":"5 000 ₫/кВт·ч","water":"15 000 ₫/м³","deposit":"1 месяц","contract":"от 6 месяцев","contact":"Hương Lê"}),

L(890,"da-lat","lv","Студия",4500000,20,
  "Студия с балконом на ул. Trần Quang Khải, район Lâm Viên (старое — Phường 8), электричество/вода включены.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134186245.htm","2 дня назад",2,source="chotot",
  details={"deposit":"1 месяц","contract":"6-12 месяцев","amenities":"общая стиральная машина, кухня на террасе","contact":"Hương Lê"}),

L(891,"da-lat","xh","Студия",5200000,50,
  "Студия с видом на ул. Ngô Thì Sỹ, район Xuân Hương (старое — Phường 4), 5 мин до рынка Đà Lạt и озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134185628.htm","2 дня назад",2,source="chotot",
  details={"electricity":"2 600 ₫/кВт·ч","water":"16 000 ₫/м³","deposit":"1 месяц","contract":"3-6-12 месяцев","contact":"Hương Lê"}),

L(892,"da-lat","lv","Квартира",9000000,60,
  "1-спальная квартира с балконом на ул. Phan Chu Trinh, район Lâm Viên (старое — Phường 9), полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134181161.htm","3 дня назад",3,source="chotot",
  details={"electricity":"4 000 ₫/кВт·ч","water":"25 000 ₫/м³","deposit":"1 месяц","contract":"6-12 месяцев","contact":"Hương Lê"}),

L(893,"da-lat","cl","Квартира",15000000,60,
  "2-спальная квартира с балконом и видом, район Cam Ly (старое — Phường 6), рядом школа Lam Sơn, 2,5 км до ночного рынка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134181134.htm","3 дня назад",3,source="chotot",
  details={"electricity":"5 000 ₫/кВт·ч","water":"100 000 ₫/чел.","deposit":"1 месяц","contract":"6-12 месяцев","amenities":"кафе и коворкинг на первом/верхнем этаже здания","contact":"Hương Lê"}),

L(894,"da-lat","lv","Студия",5500000,40,
  "Студия на ул. Phan Chu Trinh, район Lâm Viên (старое — Phường 9), полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134181114.htm","3 дня назад",3,source="chotot",
  details={"electricity":"4 000 ₫/кВт·ч","water":"25 000 ₫/м³","deposit":"1 месяц","contract":"6-12 месяцев","contact":"Hương Lê"}),

L(895,"da-lat","cl","Дом",20000000,72,
  "Дом целиком напрямую от собственника, ул. Phan Đình Giót, район Cam Ly, 50 м до рынка. 1 этаж + 3 надстройки, 6 спален (у каждой свой с/у), комната для алтаря. Без мебели.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134232785.htm","сегодня",0,source="chotot",
  details={"deposit":"3 месяца (оплата за 3)","contract":"от 2 лет","contact":"Phạm Tăng Thắng (собственник)"}),

L(896,"da-lat","xh","Дом",12000000,54,
  "Дом целиком на ул. Cổ Loa (д.5), район Xuân Hương. 3 спальни, 3 с/у, гостиная, кухня, базовая меблировка.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134200385.htm","2 дня назад",2,source="chotot",
  details={"contact":"Ngọc Uyên"}),

L(897,"da-lat","xh","Дом",13000000,30,
  "Дом целиком в переулке за пекарней Bon Bon, угол Phan Đình Phùng/Nguyễn Lương Bằng, район Xuân Hương, 1,7 км до ночного рынка. 1 этаж + 2 надстройки с мезонином, 4 спальни, 4 с/у.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134213711.htm","вчера",1,source="chotot",
  details={"contact":"A Tèo"}),

L(898,"da-lat","xt","Дом",4000000,50,
  "Дом целиком, новое строительство, квартал Trại Mát, район Xuân Trường. Основная площадь 35-37 м² + антресоль 18 м². Свой двор, заезд для мотобайка. Заселение возможно с начала сентября.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134208763.htm","вчера",1,source="chotot",
  details={"deposit":"2 месяца","contact":"Trần Nguyễn"}),

L(899,"da-lat","xh","Дом",6000000,80,
  "Дом целиком (2 спальни, 2 с/у) на ул. Khe Sanh, район Xuân Hương (старое — Phường 10), 3 мин до озера Xuân Hương, рядом больница Hoàn Mỹ.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134199776.htm","2 дня назад",2,source="chotot",
  details={"electricity":"3 500 ₫/кВт·ч","water":"25 000 ₫/м³","deposit":"2 месяца (оплата за 1)","contract":"6 месяцев","contact":"Hương Lê"}),

L(900,"da-lat","lv","Дом",7000000,70,
  "Дом целиком (2 спальни, 1 с/у) на ул. Đinh Công Tráng, район Lâm Viên (старое — Phường 7), рядом школа Lam Sơn, 7 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134186697.htm","2 дня назад",2,source="chotot",
  details={"electricity":"4 000 ₫/кВт·ч","water":"25 000 ₫/м³","deposit":"10 млн ₫","contract":"от 2 лет","contact":"Hương Lê"}),

L(901,"da-lat","xt","Дом",4300000,55,
  "Дом целиком (1 спальня + мезонин), район Xuân Trường, 10 мин до озера Xuân Hương, рядом храм Linh Phước. Без мебели, свой двор.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134185872.htm","2 дня назад",2,source="chotot",
  details={"electricity":"по гостарифу","water":"по гостарифу","deposit":"2 месяца (оплата за 1)","contract":"от 1 года","contact":"Hương Lê"}),

L(902,"da-nang","ns","Студия",8000000,30,
  "Меблированная студия, ул. Hải Triều, район Ngũ Hành Sơn. Бассейн и спортзал в комплексе, еженедельная уборка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134236635.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","contact":"Mr Thịnh"}),

L(903,"da-nang","ah","Студия",17000000,29,
  "Студия на среднем этаже с видом на город и море, район An Hải. Полностью новая меблировка. Год без сервис-сбора.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134236553.htm","сегодня",0,source="chotot",
  details={"contact":"агентство «Thuê Nhà Đẹp Căn Hộ Cao Cấp Đà Nẵng»"}),

L(904,"da-nang","ns","Квартира",17000000,60,
  "Квартира на фасаде квартала An Thượng, район Ngũ Hành Sơn, с балконом. Разрешены животные, принимают иностранцев.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134236493.htm","сегодня",0,source="chotot",
  details={"contact":"Nhuận Oanh"}),

L(905,"da-nang","ah","Квартира",6500000,25,
  "1-спальная квартира, новая меблировка, своя стиральная машина, ул. Lương Thế Vinh (за Mỹ Khê 7, рядом Võ Văn Kiệt), район An Hải.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134236486.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении указан диапазон 6,5-7,5 млн ₫/мес — использована нижняя граница","contact":"Ms Nhu"}),

L(906,"da-nang","ns","Квартира",26500000,65,
  "2-спальная квартира (2 с/у) напрямую от собственника, этаж 20 (кв. 2034), ЖК Mường Thanh Luxury, район Ngũ Hành Sơn. 50 м до пляжа, вид на море с балкона.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134184287.htm","2 дня назад",2,source="chotot",
  details={"amenities":"Netflix и wifi 500 Мбит/с бесплатно, электронный замок (отпечаток/карта/пароль), подземный паркинг, охрана 24/7","contact":"+84 866 791 931 (собственник)"}),

L(907,"da-nang","lc","Квартира",7000000,56,
  "Угловая 2-спальная квартира на 19 этаже, вид на море и озеро Bàu Tràm, ЖК The Ori Garden. Район по ward_name_v3 — «Hải Vân» (не входит в список районов проекта явно; нанесена на ближайший — Liên Chiểu).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/132606104.htm","сегодня",0,source="chotot",
  details={"amenities":"2 кондиционера, ТВ, холодильник, стиралка","contract":"1 год","notice":"цена не включает сервис-сбор; контакт скрыт продавцом (номер замаскирован ***)"}),

L(908,"da-nang","hk","Квартира",9000000,40,
  "1-спальная квартира, ул. Nguyễn Tất Thành, район Hòa Khánh. В нескольких шагах от одноимённого пляжа, вид на море.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134235627.htm","сегодня",0,source="chotot",
  details={"amenities":"своя стиральная машина"}),

L(909,"da-nang","ah","Квартира",12500000,35,
  "1-спальная квартира, новое строительство (2026), этаж 6, рядом Vincom Plaza, район An Hải. Балкон, вид в сторону моря.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134235555.htm","сегодня",0,source="chotot",
  details={"electricity":"3 800 ₫/кВт·ч","water":"100 000 ₫/чел.","deposit":"1 месяц","amenities":"Smart TV, стиралка, диван, СВЧ, бесплатный wifi, уборка 1 раз/нед., прописка для иностранцев","policy":"животные и курение в помещении запрещены"}),

L(910,"da-nang","hc","Квартира",15000000,94,
  "2-спальная квартира (2 с/у) в ЖК Lapaz Tower, район Hải Châu, центр города. Кондиционер, стиралка, кровать, ТВ, диван.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134235191.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц (оплата за 3)"}),

L(911,"da-nang","hc","Квартира",11000000,75,
  "2-спальная квартира (2 с/у) с балконом, отдельная кухня и прачечная, ул. 07 Nguyễn Trãi, район Hải Châu. Рядом мост Dragon Bridge и ул. Nguyễn Văn Linh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134206247.htm","вчера",1,source="chotot",
  details={}),

L(912,"da-nang","ns","Дом",35000000,90,
  "Дом целиком напрямую от собственника, ул. Lê Văn Tâm, район Ngũ Hành Sơn (рядом Crowne Plaza, пляж Sơn Thủy). 3 этажа, 5 спален, 5 с/у, авто во дворе.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134236460.htm","сегодня",0,source="chotot",
  details={"contact":"Mr.Tú (собственник)"}),

L(913,"da-nang","st","Дом",14000000,90,
  "Дом целиком напрямую от собственника, переулок Phan Bá Phiến, район Sơn Trà. 3 этажа, 3 спальни, 2 с/у, 100 м до моря, рядом крупные отели и рыбные рынки.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/133570105.htm","2 дня назад",2,source="chotot",
  details={"notice":"подходит и для проживания, и под онлайн-бизнес (вторично)","contact":"Zalo (номер замаскирован ***)"}),

L(914,"da-nang","tk","Дом",22000000,50,
  "Дом целиком (2 этажа, полная меблировка), переулок с заездом для авто, ул. Nguyễn Văn Linh, район Thanh Khê. 2 спальни, 3 с/у, 1 км до моста Dragon Bridge.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134179368.htm","3 дня назад",3,source="chotot",
  details={}),

L(915,"da-nang","cl2","Дом",15000000,100,
  "Дом целиком, 3 этажа, ул. Cống Quỳnh, рядом с эстакадой Hòa Cẩm, район Cẩm Lệ. 3 спальни, 3 с/у, место для авто.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134235822.htm","сегодня",0,source="chotot",
  details={}),

L(916,"da-nang","ns","Дом",22000000,100,
  "Дом целиком, 2 этажа, ул. Mộc Sơn 2, район Ngũ Hành Sơn, рядом пляж Non Nước. 3 спальни, 3 с/у, двор для авто, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134235765.htm","сегодня",0,source="chotot",
  details={"notice":"контакт скрыт продавцом (номер замаскирован ***)"}),

L(917,"da-nang","tk","Дом",20000000,60,
  "Дом целиком, фасад ул. Thuận An (рядом Thái Thị Bôi и рынок), центр города, район Thanh Khê. 3 спальни, 4 с/у, полная меблировка, авто во дворе. Принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134216512.htm","вчера",1,source="chotot",
  details={"contact":"Nhuận Oanh"}),

L(918,"da-nang","ns","Дом",120000000,325,
  "Вилла с бассейном и садом, ул. Chế Lan Viên, район Ngũ Hành Sơn, рядом квартал An Thượng и море. 2 этажа, 5 спален, 6 с/у, полная премиальная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134235959.htm","сегодня",0,source="chotot",
  details={"notice":"позиционируется для семей/иностранных специалистов, дублируется описание на английском","contact":"Toan House"}),

L(919,"da-nang","ns","Дом",35000000,100,
  "Дом целиком, 3 этажа, ул. Phạm Hữu Kính, Mỹ An, район Ngũ Hành Sơn, рядом река Хан. 4 спальни.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-pham-huu-kinh_1-phuong-ngu-hanh-son-tp-da-nang/cho-3-tang-4pn-uong-kinh-my-an-gan-song-han-pr46202569","проверено 19 авг",0,source="batdongsan",
  details={"contact":"Ms Quyên","notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления (prNNNNNNNN) — выше потолка, зафиксированного сегодняшним HCMC-прогоном (46202495). Цена подтверждена дважды: в карточке поиска и на странице объявления (поле «Khoảng giá»)."}),

L(920,"da-nang","ns","Дом",40000000,100,
  "Дом целиком, новый ремонт, 3 этажа, квартал Nam Việt Á, район Ngũ Hành Sơn. 4 спальни, 5 с/у, балкон и терраса на крыше, полная современная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-doan-khue-1-phuong-ngu-hanh-son-tp-da-nang/cho-moi-ep-4pn-khu-nam-viet-a-full-noi-that-hien-ai-pr46202528","проверено 19 авг",0,source="batdongsan",
  details={"contact":"Ms Quyên","notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления — выше потолка 46202495. Цена подтверждена дважды (карточка + «Khoảng giá»). Для гостей из Китая владелец указывает повышенную ставку 45 млн ₫ — в качестве цены взята стандартная (40 млн ₫)."}),

L(921,"vung-tau","vtp","Квартира",10000000,74,
  "2-спальная квартира (2 с/у) в ЖК Goldsea, вид на море, ~50 м до пляжа Thùy Vân, район Vũng Tàu (центр).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134210077.htm","вчера",1,source="chotot",
  details={"notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Thiết Lê"}),

L(922,"vung-tau","rd","Квартира",16000000,91,
  "3-спальная квартира (2 с/у), новая меблировка (100%), ЖК Vũng Tàu Center Point, район Rạch Dừa.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134189479.htm","2 дня назад",2,source="chotot",
  details={"amenities":"бесплатное обслуживание дома и бассейн","contact":"Như Quỳnh"}),

L(923,"vung-tau","vtp","Квартира",8000000,74,
  "2-спальная квартира (2 с/у) в ЖК Melody, район Vũng Tàu (центр), прямой вид на море. Базовая меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134189418.htm","2 дня назад",2,source="chotot",
  details={"contract":"1 год","policy":"животные не принимаются","contact":"Như Quỳnh"}),

L(924,"vung-tau","rd","Дом",14000000,115,
  "Дом целиком на фасаде ул. Lê Quang Định, район Rạch Dừa. 1 этаж + 2 надстройки, 4 спальни, задний двор.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-vung-tau-ba-ria-vung-tau/133865836.htm","2 дня назад",2,source="chotot",
  details={"notice":"подходит и для проживания, и под офис/репетиторство (вторично)","contact":"Mr Mạnh"}),

L(925,"vung-tau","vtp","Квартира",9000000,92,
  "Квартира ~50 м от моря, район Vũng Tàu (центр).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134168519.htm","3 дня назад",3,source="chotot",
  details={"notice":"также предлагается посуточная аренда — приоритет отдаётся долгосрочным арендаторам","contact":"Loi Nguyen Văn"}),

L(926,"quy-nhon","qn","Квартира",8500000,58,
  "Угловая 2-спальная квартира на высоком этаже с видом на море, ЖК TMS Quy Nhơn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-qui-nhon-binh-dinh/134226216.htm","сегодня",0,source="chotot",
  details={"notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Vũ Thành Long"}),

L(927,"quy-nhon","qn","Квартира",13000000,96,
  "3-спальная квартира с видом на залив, новая меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-qui-nhon-binh-dinh/134166973.htm","3 дня назад",3,source="chotot",
  details={"notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Vũ Thành Long"}),

L(928,"quy-nhon","qn","Дом",3200000,40,
  "Дом с мезонином в переулке от ул. Nguyễn Huệ, рядом с провинциальной больницей, рынком и Университетом Куинён. Несколько шагов до моря.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-qui-nhon-binh-dinh/134220484.htm","вчера",1,source="chotot",
  details={"contact":"Chị Quỳnh"}),
]

# Real lat/lon per listing for the Leaflet map — precise geocoded address where extractable from
# the description, otherwise the listing's ward centroid (see build_leaflet_data.py).
try:
    _latlon = json.load(open(W + "/leaflet_listing_latlon.json", encoding="utf-8"))
    for _l in LISTINGS:
        _p = _latlon.get(str(_l["id"]))
        if _p:
            _l["lat"] = _p["lat"]; _l["lon"] = _p["lon"]; _l["geocoded"] = bool(_p.get("geocoded", True))
except FileNotFoundError:
    pass

try:
    WARD_BOUNDARIES = json.load(open(W + "/leaflet_ward_boundaries.json", encoding="utf-8"))
except FileNotFoundError:
    WARD_BOUNDARIES = {}

DATA = {
    "CITIES": CITIES, "SOURCES": SOURCES, "FB_GROUPS": FB_GROUPS,
    "LISTINGS": LISTINGS, "WARD_BOUNDARIES": WARD_BOUNDARIES
}
DATA_JSON = json.dumps(DATA, ensure_ascii=False, separators=(",",":"))
print("Data JSON size:", len(DATA_JSON))

# ================== HTML TEMPLATE ==================
HTML = r"""<meta charset="utf-8">
<title>Жильё во Вьетнаме — Нячанг · Далат · Дананг · Хошимин</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
<style>
  :root{
    --paper:#F2F5EC;
    --surface:#FFFFFF;
    --surface-2:#EAEFE1;
    --ink:#182016;
    --ink-dim:#5B6753;
    --ink-faint:#8A9480;
    --line:#DAE2CC;
    --line-strong:#C4CFB4;
    --accent:#1E7A4C;
    --accent-ink:#FFFFFF;
    --accent-soft:#DEEDE1;
    --accent-soft-line:#B7D8BF;
    --gold:#A86A1B;
    --gold-soft:#F3E4C4;
    --grey-empty:#EDF0E4;
    --grey-has:#C7D0B8;
    --grey-has-line:#AEBA9B;
    --sea:#C7DEE6;
    --sea-ink:#4C7385;
    --danger:#B44430;
    --warn-bg:#FBE7DD;
    --warn-ink:#9A3E1F;
    --shadow-sm:0 1px 2px rgba(24,32,22,0.07);
    --shadow-md:0 14px 34px -18px rgba(24,32,22,0.35);
    --radius-lg:18px;
    --radius-md:12px;
    --radius-sm:8px;
    --font-display:Georgia,'PT Serif','Noto Serif',serif;
    --font-body:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
  }
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]){
      --paper:#10140D; --surface:#181D14; --surface-2:#1E2418; --ink:#E9EEE0; --ink-dim:#A6B199; --ink-faint:#71806A;
      --line:#2A3322; --line-strong:#38452C; --accent:#43BD7C; --accent-ink:#0A1409; --accent-soft:#1B2E20; --accent-soft-line:#2C4A34;
      --gold:#E3A94D; --gold-soft:#3A2C13; --grey-empty:#1C2216; --grey-has:#333F27; --grey-has-line:#48583A;
      --sea:#152F3A; --sea-ink:#8FB9C9; --danger:#E08267; --warn-bg:#3A2417; --warn-ink:#F0B08F;
      --shadow-sm:0 1px 2px rgba(0,0,0,0.4); --shadow-md:0 18px 40px -20px rgba(0,0,0,0.6);
    }
  }
  :root[data-theme="dark"]{
    --paper:#10140D; --surface:#181D14; --surface-2:#1E2418; --ink:#E9EEE0; --ink-dim:#A6B199; --ink-faint:#71806A;
    --line:#2A3322; --line-strong:#38452C; --accent:#43BD7C; --accent-ink:#0A1409; --accent-soft:#1B2E20; --accent-soft-line:#2C4A34;
    --gold:#E3A94D; --gold-soft:#3A2C13; --grey-empty:#1C2216; --grey-has:#333F27; --grey-has-line:#48583A;
    --sea:#152F3A; --sea-ink:#8FB9C9; --danger:#E08267; --warn-bg:#3A2417; --warn-ink:#F0B08F;
    --shadow-sm:0 1px 2px rgba(0,0,0,0.4); --shadow-md:0 18px 40px -20px rgba(0,0,0,0.6);
  }

  *,*::before,*::after{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{background:var(--paper);color:var(--ink);font-family:var(--font-body);font-size:15.5px;line-height:1.5;-webkit-font-smoothing:antialiased;}
  h1,h2,h3{font-family:var(--font-display);font-weight:700;text-wrap:balance;margin:0;}
  a{color:inherit;}
  button{font-family:inherit;}
  ::selection{background:var(--accent-soft);}
  :focus-visible{outline:2.5px solid var(--accent);outline-offset:2px;border-radius:4px;}

  .page{max-width:1180px;margin:0 auto;padding:28px 20px 60px;display:flex;flex-direction:column;gap:26px;}

  .hero{display:flex;flex-direction:column;gap:20px;}
  .brand{display:flex;align-items:center;gap:14px;}
  .brand-mark{flex:none;width:46px;height:46px;border-radius:12px;background:var(--accent);display:flex;align-items:center;justify-content:center;box-shadow:var(--shadow-sm);}
  .brand-mark svg{width:26px;height:26px;}
  .brand h1{font-size:clamp(1.5rem,1.1rem + 1.3vw,2.05rem);letter-spacing:-0.01em;}
  .tagline{margin:4px 0 0;color:var(--ink-dim);font-size:0.98rem;max-width:60ch;}

  .city-tabs{display:flex;gap:8px;flex-wrap:wrap;}
  .city-tab{appearance:none;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink);padding:10px 18px;border-radius:999px;font-size:0.96rem;font-weight:600;cursor:pointer;transition:background .15s ease,color .15s ease,border-color .15s ease;}
  .city-tab .sub{display:block;font-weight:400;font-size:0.76rem;color:var(--ink-faint);margin-top:1px;}
  .city-tab[aria-selected="true"]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);}
  .city-tab[aria-selected="true"] .sub{color:var(--accent-ink);opacity:0.82;}
  .city-tab:hover{border-color:var(--accent);}

  .control-panel{display:grid;grid-template-columns:minmax(280px,1fr) minmax(300px,1.05fr);gap:18px;align-items:start;}
  @media (max-width:860px){.control-panel{grid-template-columns:1fr;}}

  .card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:var(--shadow-sm);}

  .filters{padding:22px 22px 18px;display:flex;flex-direction:column;gap:18px;}
  .field{display:flex;flex-direction:column;gap:8px;}
  .field label,.field-label{font-size:0.82rem;font-weight:700;color:var(--ink-dim);text-transform:uppercase;letter-spacing:0.045em;}
  .field-hint{font-size:0.78rem;color:var(--ink-faint);margin:0;}

  .range-cells{display:flex;gap:8px;align-items:center;}
  .range-cell{position:relative;flex:1;display:flex;align-items:center;border-radius:var(--radius-md);border:1px solid var(--line-strong);background:var(--paper);padding:6px 12px;gap:6px;}
  .range-cell-label{font-size:0.78rem;color:var(--ink-faint);flex-shrink:0;}
  .range-cell input{width:100%;min-width:0;border:none;background:transparent;color:var(--ink);font-size:1rem;font-variant-numeric:tabular-nums;padding:3px 0;}
  .range-cell input:focus{outline:none;}
  .range-cell:focus-within{border-color:var(--accent);}
  .range-cell-sep{color:var(--ink-faint);flex-shrink:0;}
  .range-cells .unit{color:var(--ink-faint);font-size:0.85rem;flex-shrink:0;}

  .range-slider{position:relative;height:28px;display:flex;align-items:center;margin-top:2px;}
  .range-track{position:absolute;left:0;right:0;height:4px;border-radius:2px;background:var(--line-strong);}
  .range-fill{position:absolute;height:4px;border-radius:2px;background:var(--accent);}
  .range-thumb{position:absolute;left:0;top:0;width:100%;height:28px;margin:0;background:transparent;pointer-events:none;-webkit-appearance:none;appearance:none;}
  .range-thumb:focus{outline:none;}
  .range-thumb::-webkit-slider-runnable-track{background:transparent;height:28px;}
  .range-thumb::-moz-range-track{background:transparent;height:28px;border:none;}
  .range-thumb::-webkit-slider-thumb{-webkit-appearance:none;pointer-events:auto;width:18px;height:18px;margin-top:5px;border-radius:50%;background:var(--accent);border:2px solid var(--surface);box-shadow:0 1px 3px rgba(0,0,0,.3);cursor:grab;}
  .range-thumb::-moz-range-thumb{pointer-events:auto;width:18px;height:18px;border-radius:50%;background:var(--accent);border:2px solid var(--surface);box-shadow:0 1px 3px rgba(0,0,0,.3);cursor:grab;}
  .range-thumb:active::-webkit-slider-thumb{cursor:grabbing;transform:scale(1.12);}
  .range-thumb:active::-moz-range-thumb{cursor:grabbing;transform:scale(1.12);}
  .range-thumb-min{z-index:3;}
  .range-thumb-max{z-index:4;}
  .range-thumb-min.on-top{z-index:5;}
  .chip-row{display:flex;gap:6px;flex-wrap:wrap;}
  .chip{appearance:none;border:1px solid var(--line-strong);background:var(--paper);color:var(--ink-dim);padding:6px 12px;border-radius:999px;font-size:0.82rem;font-weight:600;cursor:pointer;white-space:nowrap;}
  .chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);}
  .chip.gold[aria-pressed="true"]{background:var(--gold);border-color:var(--gold);color:#241701;}
  .chip:disabled{opacity:0.55;cursor:not-allowed;}
  .chip .dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:currentColor;margin-right:5px;opacity:0.6;vertical-align:middle;}

  .date-row{display:flex;gap:8px;align-items:center;}
  .date-row input{flex:1;padding:9px 10px;border-radius:var(--radius-md);border:1px solid var(--line-strong);background:var(--surface-2);color:var(--ink-faint);font-size:0.92rem;}
  .date-row span{color:var(--ink-faint);font-size:0.85rem;}

  .autocomplete{position:relative;}
  .autocomplete input{width:100%;padding:11px 36px 11px 14px;border-radius:var(--radius-md);border:1px solid var(--line-strong);background:var(--paper);color:var(--ink);font-size:1rem;}
  .autocomplete .clear-btn{position:absolute;right:6px;top:6px;width:28px;height:28px;border:none;background:transparent;color:var(--ink-faint);font-size:1.1rem;cursor:pointer;border-radius:50%;display:flex;align-items:center;justify-content:center;}
  .autocomplete .clear-btn:hover{background:var(--surface-2);}
  .suggest-list{position:absolute;left:0;right:0;top:calc(100% + 6px);background:var(--surface);border:1px solid var(--line-strong);border-radius:var(--radius-md);box-shadow:var(--shadow-md);list-style:none;margin:0;padding:6px;z-index:20;max-height:260px;overflow:auto;}
  .suggest-list li{border-radius:8px;}
  .suggest-list button{width:100%;text-align:left;background:none;border:none;padding:9px 10px;border-radius:8px;cursor:pointer;color:var(--ink);display:flex;justify-content:space-between;gap:10px;font-size:0.94rem;}
  .suggest-list button:hover,.suggest-list button:focus-visible{background:var(--accent-soft);}
  .suggest-list .hint{color:var(--ink-faint);font-size:0.8rem;}
  .suggest-empty{padding:9px 10px;color:var(--ink-faint);font-size:0.88rem;}

  .sort-toggle{display:flex;border:1px solid var(--line-strong);border-radius:999px;overflow:hidden;width:fit-content;}
  .sort-toggle button{appearance:none;border:none;background:var(--paper);color:var(--ink-dim);padding:9px 16px;font-size:0.86rem;font-weight:600;cursor:pointer;}
  .sort-toggle button.active{background:var(--accent);color:var(--accent-ink);}

  .map{padding:20px 20px 16px;display:flex;flex-direction:column;gap:12px;}
  .map-head{display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap;}
  .map-title{font-family:var(--font-display);font-size:1.08rem;font-weight:700;}
  .map-note{font-size:0.76rem;color:var(--ink-faint);font-style:italic;}

  .leaflet-map-el{width:100%;height:420px;border-radius:var(--radius-md);background:var(--paper);z-index:0;}
  .leaflet-popup-content-wrapper{background:var(--surface);color:var(--ink);border-radius:var(--radius-md);box-shadow:var(--shadow-md);}
  .leaflet-popup-tip{background:var(--surface);}
  .leaflet-popup-content{margin:10px 12px;font-family:var(--font-body);font-size:0.82rem;line-height:1.4;}
  .leaflet-container{background:var(--paper);font-family:var(--font-body);}
  .leaflet-control-attribution{background:var(--surface) !important;color:var(--ink-faint) !important;font-size:0.68rem !important;}
  .leaflet-control-attribution a{color:var(--ink-dim) !important;}
  .leaflet-bar a{background:var(--surface) !important;color:var(--ink) !important;border-bottom-color:var(--line) !important;}
  .leaflet-bar a:hover{background:var(--surface-2) !important;}

  .pt-top{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:4px;}
  .pt-src{font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.03em;color:var(--ink-faint);}
  .pt-price{font-family:var(--font-display);font-weight:700;font-size:0.98rem;color:var(--ink);}
  .pt-meta{color:var(--ink-dim);font-size:0.76rem;margin-bottom:3px;}
  .pt-desc{color:var(--ink);}
  .pt-hint{display:block;margin-top:6px;color:var(--accent);font-size:0.74rem;font-weight:600;text-decoration:none;}
  .pt-hint:hover{text-decoration:underline;}
  .pt-approx{margin-top:4px;color:var(--ink-faint);font-size:0.7rem;font-style:italic;}

  .map-legend{display:flex;gap:14px;flex-wrap:wrap;font-size:0.78rem;color:var(--ink-dim);}
  .map-legend span{display:inline-flex;align-items:center;gap:6px;}
  .swatch{width:12px;height:12px;border-radius:4px;display:inline-block;border:1px solid var(--line-strong);}
  .swatch-selected{background:var(--accent);border-color:var(--accent);}
  .swatch-has{background:var(--grey-has);}
  .swatch-empty{background:var(--grey-empty);}
  .map-credit{font-size:0.72rem;color:var(--ink-faint);}

  .results-head{display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:12px;}
  .results-head h2{font-size:1.3rem;}
  .results-sub{margin:4px 0 0;color:var(--ink-dim);font-size:0.9rem;}
  .reset-btn{appearance:none;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink-dim);padding:8px 14px;border-radius:999px;font-size:0.84rem;font-weight:600;cursor:pointer;}
  .reset-btn:hover{border-color:var(--danger);color:var(--danger);}

  .results-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin-top:16px;align-items:start;}

  .listing-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:var(--shadow-sm);}
  .listing-top{display:flex;justify-content:space-between;align-items:center;gap:8px;}
  .source-pill{display:inline-flex;align-items:center;gap:6px;font-size:0.72rem;font-weight:700;color:var(--ink-dim);background:var(--surface-2);border-radius:999px;padding:4px 10px;text-transform:uppercase;letter-spacing:0.03em;}
  .source-pill i{width:7px;height:7px;border-radius:50%;background:var(--danger);}
  .posted{font-size:0.76rem;color:var(--ink-faint);}

  .listing-type{font-size:0.78rem;font-weight:700;color:var(--gold);text-transform:uppercase;letter-spacing:0.03em;}
  .listing-meta{font-size:0.86rem;color:var(--ink-dim);}
  .listing-desc{font-size:0.92rem;color:var(--ink);margin:0;}

  .listing-notice{font-size:0.82rem;background:var(--warn-bg);color:var(--warn-ink);padding:8px 10px;border-radius:var(--radius-sm);font-weight:600;}

  .details-toggle{appearance:none;border:1px dashed var(--line-strong);background:transparent;color:var(--ink-dim);padding:7px 10px;border-radius:var(--radius-sm);font-size:0.82rem;font-weight:600;cursor:pointer;text-align:left;width:100%;}
  .details-toggle:hover{border-color:var(--accent);color:var(--accent);}
  .details-toggle .arrow{float:right;transition:transform .15s ease;}
  .details-toggle[aria-expanded="true"] .arrow{transform:rotate(180deg);}
  .details-panel{display:flex;flex-direction:column;gap:6px;padding:10px 12px;background:var(--surface-2);border-radius:var(--radius-sm);font-size:0.86rem;}
  .details-panel[hidden]{display:none;}
  .details-row{display:flex;gap:8px;}
  .details-row dt{flex:none;width:110px;color:var(--ink-faint);font-weight:600;}
  .details-row dd{margin:0;color:var(--ink);}

  .listing-bottom{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:auto;padding-top:8px;border-top:1px dashed var(--line);}
  .price{font-family:var(--font-display);font-size:1.28rem;font-weight:700;font-variant-numeric:tabular-nums;}
  .price small{font-family:var(--font-body);font-size:0.68rem;font-weight:600;color:var(--ink-faint);text-transform:uppercase;}
  .open-link{display:inline-flex;align-items:center;gap:6px;text-decoration:none;background:var(--accent);color:var(--accent-ink);padding:9px 14px;border-radius:999px;font-size:0.84rem;font-weight:700;white-space:nowrap;}
  .open-link:hover{filter:brightness(1.06);}

  .empty-state{margin-top:18px;padding:32px 20px;text-align:center;border:1px dashed var(--line-strong);border-radius:var(--radius-lg);color:var(--ink-dim);}
  .empty-state strong{display:block;color:var(--ink);font-size:1.05rem;margin-bottom:6px;font-family:var(--font-display);}

  .footer{border-top:1px solid var(--line);padding-top:20px;color:var(--ink-dim);font-size:0.84rem;line-height:1.6;}
  .footer h3{font-size:0.95rem;color:var(--ink);margin-bottom:6px;}
  .footer ul{margin:0 0 12px;padding-left:18px;}
  .footer .stamp{color:var(--ink-faint);font-size:0.78rem;}
</style>

<div class="page">

  <header class="hero">
    <div class="brand">
      <span class="brand-mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none"><path d="M4 11.5 12 4l8 7.5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M6 10.5V19a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-8.5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 20v-5h4v5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <div>
        <h1>Жильё во Вьетнаме</h1>
        <p class="tagline">Комнаты, студии и квартиры в Нячанге, Далате, Дананге и Хошимине — из реальных объявлений, отсортированные по цене.</p>
      </div>
    </div>
    <nav class="city-tabs" id="city-tabs" role="tablist" aria-label="Город"></nav>
  </header>

  <section class="control-panel">
    <div class="filters card">
      <div class="field">
        <label>Бюджет, млн ₫ / мес</label>
        <div class="range-cells">
          <div class="range-cell">
            <span class="range-cell-label">от</span>
            <input id="budget-min-input" type="number" min="0" max="45" step="0.5" inputmode="decimal">
          </div>
          <span class="range-cell-sep">—</span>
          <div class="range-cell">
            <span class="range-cell-label">до</span>
            <input id="budget-max-input" type="number" min="0" max="45" step="0.5" inputmode="decimal">
          </div>
          <span class="unit">млн ₫</span>
        </div>
        <div class="range-slider" id="budget-slider">
          <div class="range-track"></div>
          <div class="range-fill" id="budget-range-fill"></div>
          <input type="range" id="budget-min-range" class="range-thumb range-thumb-min" min="0" max="45" step="0.5">
          <input type="range" id="budget-max-range" class="range-thumb range-thumb-max" min="0" max="45" step="0.5">
        </div>
        <div class="chip-row" id="budget-chips"></div>
      </div>

      <div class="field">
        <label for="district-input">Район</label>
        <div class="autocomplete">
          <input id="district-input" type="text" autocomplete="off" placeholder="Начните вводить название района">
          <button class="clear-btn" id="district-clear" type="button" title="Сбросить район" aria-label="Сбросить район">×</button>
          <ul class="suggest-list" id="district-suggest" hidden></ul>
        </div>
      </div>

      <div class="field">
        <span class="field-label">Когда опубликовано</span>
        <div class="chip-row" id="days-chips"></div>
      </div>

      <div class="field">
        <span class="field-label">Источники</span>
        <div class="chip-row" id="source-chips"></div>
      </div>

      <div class="field">
        <span class="field-label">Даты заезда (Airbnb / Agoda / Trip.com / CozyCozy)</span>
        <div class="date-row">
          <input type="text" placeholder="16.08.2026" disabled>
          <span>—</span>
          <input type="text" placeholder="16.09.2026" disabled>
        </div>
        <p class="field-hint">Появится, когда подключим посуточные сервисы — там снимают на даты, а не на месяцы.</p>
      </div>

      <div class="field">
        <span class="field-label">Тип жилья</span>
        <div class="chip-row" id="type-chips"></div>
      </div>

      <div class="field">
        <span class="field-label">Сортировка</span>
        <div class="sort-toggle" id="sort-toggle">
          <button data-sort="asc" class="active" type="button">Дешевле</button>
          <button data-sort="desc" type="button">Дороже</button>
          <button data-sort="new" type="button">Новые</button>
        </div>
      </div>
    </div>

    <div class="map card">
      <div class="map-head">
        <span class="map-title" id="map-title">Карта района</span>
        <span class="map-note" id="map-note">реальные границы районов, OpenStreetMap</span>
      </div>
      <div id="leaflet-map" class="leaflet-map-el"></div>
      <div class="map-legend">
        <span><i class="swatch" style="background:var(--accent)" aria-hidden="true"></i>объявление (положение приблизительное)</span>
        <span>клик по району на карте — фильтр по нему</span>
      </div>
      <p class="map-credit" id="map-credit">Карта и адреса — © участники OpenStreetMap (ODbL). Границы районов актуальны после реформы административного деления 2025 года.</p>
    </div>
  </section>

  <section class="results">
    <div class="results-head">
      <div>
        <h2 id="results-count">— объявлений</h2>
        <p class="results-sub" id="results-context"></p>
      </div>
      <button class="reset-btn" id="reset-filters" type="button">Сбросить фильтры</button>
    </div>
    <div class="results-list" id="results-list"></div>
    <div class="empty-state" id="empty-state" hidden>
      <strong>По этим критериям пока пусто</strong>
      Попробуйте увеличить бюджет, выбрать другой район или снять фильтр по сроку публикации.
    </div>
  </section>

  <footer class="footer">
    <h3>Об этой подборке</h3>
    <ul>
      <li>Подключено 9 источников: <strong>Chợ Tốt / Nhà Tốt</strong>, <strong>Facebook-группы</strong>, <strong>Facebook Marketplace</strong>, <strong>Batdongsan.com.vn</strong>, <strong>Telegram-каналы</strong>, <strong>Airbnb</strong>, <strong>Trip.com</strong>, <strong>Booking.com</strong> и <strong>Vrbo</strong> (последние четыре — помесячные/долгосрочные тарифы на посуточных платформах, а не обычная посуточная аренда). Все __LISTING_COUNT__ карточек выше настоящие, ссылки ведут на оригинальные объявления — нажмите «Подробнее» на карточке, чтобы увидеть коммуналку, депозит и другие условия из оригинального объявления.</li>
      <li>Для Нячанга, Далата и Дананга собрано вручную по актуальным группам аренды (список — ниже, под соответствующим городом). Для Хошимина отдельная выборка — под три конкретных района личного поиска (Phú Mỹ Hưng, Thảo Điền/An Phú, Thanh Đa) плюс два дополнительно хороших района (Bến Thành, Khánh Hội).</li>
      <li>Даты заезда для посуточных платформ (Airbnb/Trip.com/Booking.com/Vrbo) — пока фиксированный период (обычно 30 ночей), а не гибкий выбор дат; свободный выбор даты заезда/выезда всё ещё в разработке.</li>
      <li>Facebook закрывает поиск по группам без входа в аккаунт и отдаёт ленту частями — поэтому автоматический постоянный сбор из групп ограничен; надёжнее всего работает точечная проверка групп вручную (список — ниже).</li>
      <li>Если в подборку добавятся риелторы/агентства — только вьетнамские, без посреднических наценок экспат-агентов.</li>
      <li>Карта теперь интерактивная (Leaflet + OpenStreetMap): у каждого объявления есть точка на карте, наведение показывает мини-карточку, клик открывает объявление. Точное положение — там, где адрес удалось определить по описанию, иначе точка стоит примерно по центру района. ⚠ Карта грузит внешние тайлы OpenStreetMap, поэтому не открывается по ссылке артефакта (там это заблокировано политикой безопасности) — работает только если открыть файл локально.</li>
      <li>Карта Нячанга — особый случай: после реформы 2025 года старые районы (Lộc Thọ, Tân Lập, Phước Hải и т.д.) официально объединили в 4 огромные зоны, которыми никто не пользуется, а официальных границ на уровне привычных районов больше не существует — поэтому точки там расставлены по правильному району, но не по точному адресу. Далат, Дананг, Хойан и Хошимин показаны по официальным границам районов 2025 года.</li>
    </ul>
    <h3 style="margin-top:16px;" id="fb-groups-title">Facebook-группы по аренде</h3>
    <ul id="fb-groups-list"></ul>
    <p class="stamp">Данные актуальны на 18 августа 2026 · объявления старше 30 дней исключены из подборки · перед созвоном с хозяином всегда проверяйте цену и наличие по ссылке на объявление.</p>
  </footer>

</div>

<script>
(function(){
  "use strict";

  var DATA = __DATA_JSON__;
  var CITIES = DATA.CITIES;
  var SOURCES = DATA.SOURCES;
  var FB_GROUPS = DATA.FB_GROUPS;
  var LISTINGS = DATA.LISTINGS;

  var SOURCE_LABEL = {};
  SOURCES.forEach(function(s){ SOURCE_LABEL[s.key] = s; });

  var DAY_OPTIONS = [1,3,7,14,30,60];
  var BUDGET_CHIPS = [3,5,10,15];
  var DETAIL_LABELS = {
    deposit:"Депозит", electricity:"Электричество", water:"Вода", internet:"Интернет/wifi",
    managementFee:"Управление", amenities:"Удобства", policy:"Правила", contract:"Договор", notice:"Важно"
  };
  var DETAIL_ORDER = ["deposit","electricity","water","internet","managementFee","contract","policy","amenities","notice"];

  var TYPE_OPTIONS = ["Комната","Студия","Квартира","Дом","Другое"];

  var state = {
    city: "nha-trang", district: null, minBudget: null, maxBudget: null, maxDays: 60, sort: "asc", type: null,
    sources: new Set(SOURCES.filter(function(s){ return s.active; }).map(function(s){ return s.key; })),
    openDetails: new Set()
  };

  var BUDGET_MIN = 0, BUDGET_MAX = 45;

  var el = {
    cityTabs: document.getElementById("city-tabs"),
    budgetMinInput: document.getElementById("budget-min-input"),
    budgetMaxInput: document.getElementById("budget-max-input"),
    budgetMinRange: document.getElementById("budget-min-range"),
    budgetMaxRange: document.getElementById("budget-max-range"),
    budgetRangeFill: document.getElementById("budget-range-fill"),
    budgetChips: document.getElementById("budget-chips"),
    districtInput: document.getElementById("district-input"),
    districtClear: document.getElementById("district-clear"),
    districtSuggest: document.getElementById("district-suggest"),
    daysChips: document.getElementById("days-chips"),
    sourceChips: document.getElementById("source-chips"),
    typeChips: document.getElementById("type-chips"),
    sortToggle: document.getElementById("sort-toggle"),
    mapTitle: document.getElementById("map-title"),
    mapSvgWrap: document.getElementById("leaflet-map"),
    resultsCount: document.getElementById("results-count"),
    resultsContext: document.getElementById("results-context"),
    resultsList: document.getElementById("results-list"),
    emptyState: document.getElementById("empty-state"),
    resetBtn: document.getElementById("reset-filters")
  };

  function fmtPrice(v){
    var m = v/1000000;
    var s = (m % 1 === 0) ? String(m) : m.toFixed(1).replace(".", ",");
    return s + " млн";
  }
  function districtByKey(cityKey, distKey){
    var list = CITIES[cityKey].districts;
    for (var i=0;i<list.length;i++){ if (list[i].key===distKey) return list[i]; }
    return null;
  }
  function countsForCity(cityKey){
    var counts = {};
    LISTINGS.forEach(function(l){ if (l.city !== cityKey) return; counts[l.district] = (counts[l.district]||0) + 1; });
    return counts;
  }

  function renderCityTabs(){
    el.cityTabs.innerHTML = "";
    Object.keys(CITIES).forEach(function(key){
      var c = CITIES[key];
      var btn = document.createElement("button");
      btn.className = "city-tab"; btn.type = "button"; btn.setAttribute("role","tab");
      btn.setAttribute("aria-selected", state.city===key ? "true":"false");
      btn.innerHTML = c.name + '<span class="sub">' + c.districts.length + " районов</span>";
      btn.addEventListener("click", function(){ selectCity(key); });
      el.cityTabs.appendChild(btn);
    });
  }

  function selectCity(key){
    state.city = key; state.district = null; el.districtInput.value = "";
    renderCityTabs(); renderCityMap(); renderFbGroups(); applyFilters();
  }

  var WARD_BOUNDARIES = DATA.WARD_BOUNDARIES || {};
  var leafletMap = null, wardLayerGroup = null, markerLayerGroup = null, leafletReady = false;
  var wardLayerByKey = {};

  function initLeafletMap(){
    if (leafletMap || typeof L === "undefined") return;
    leafletMap = L.map("leaflet-map", {scrollWheelZoom:true});
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors'
    }).addTo(leafletMap);
    wardLayerGroup = L.layerGroup().addTo(leafletMap);
    markerLayerGroup = L.layerGroup().addTo(leafletMap);
    leafletReady = true;
  }

  function wardStyle(cnt, selected){
    if (selected) return {color:"var(--accent)", weight:3, fillColor:"#1E7A4C", fillOpacity:0.35};
    if (cnt>0) return {color:"#7C8A6E", weight:1.5, fillColor:"#7C8A6E", fillOpacity:0.14};
    return {color:"#9AA48C", weight:1, fillColor:"#9AA48C", fillOpacity:0.05, dashArray:"3,4"};
  }

  function activateDistrict(key, name){
    state.district = (state.district===key) ? null : key;
    el.districtInput.value = state.district ? name : "";
    renderCityMap(); applyFilters();
  }

  function renderCityMap(){
    var city = CITIES[state.city];
    el.mapTitle.textContent = "Карта района — " + city.name;
    var noteEl = document.getElementById("map-note");
    var creditEl = document.getElementById("map-credit");
    var boundaries = WARD_BOUNDARIES[state.city];
    if (!boundaries){
      noteEl.textContent = "нет официальных границ районов — показаны только точки объявлений";
      creditEl.textContent = "После реформы 2025 года у Нячанга нет официальных границ на уровне районов, поэтому контуры не показаны — только примерные точки объявлений по районам. Карта — © участники OpenStreetMap (ODbL).";
    } else {
      noteEl.textContent = "официальные границы районов, OpenStreetMap";
      creditEl.textContent = "Карта и границы районов — © участники OpenStreetMap (ODbL), границы актуальны после реформы административного деления 2025 года.";
    }
    if (!leafletReady){
      el.mapSvgWrap.innerHTML = '<div style="padding:32px 16px;text-align:center;color:var(--ink-dim);font-size:0.88rem;">Карта недоступна в этом окне — внешние карты (OpenStreetMap) заблокированы политикой безопасности. Откройте страницу как локальный файл, чтобы увидеть интерактивную карту.</div>';
      return;
    }
    wardLayerGroup.clearLayers();
    wardLayerByKey = {};
    var counts = countsForCity(state.city);
    var boundsLayers = [];
    if (boundaries){
      city.districts.forEach(function(d){
        var w = boundaries[d.key];
        if (!w) return;
        var cnt = counts[d.key] || 0;
        var poly = L.polygon(w.rings, wardStyle(cnt, state.district===d.key));
        poly.bindTooltip(d.name + (cnt ? (" — " + cnt + " объяв.") : " — пока нет объявлений"));
        poly.on("click", function(){ activateDistrict(d.key, d.name); });
        poly.addTo(wardLayerGroup);
        wardLayerByKey[d.key] = poly;
        boundsLayers.push(poly);
      });
    }
    if (boundsLayers.length){
      leafletMap.fitBounds(L.featureGroup(boundsLayers).getBounds(), {padding:[12,12]});
    } else {
      var pts = LISTINGS.filter(function(l){ return l.city===state.city && typeof l.lat==="number"; });
      if (pts.length){
        var b = L.latLngBounds(pts.map(function(l){ return [l.lat, l.lon]; }));
        leafletMap.fitBounds(b, {padding:[24,24]});
      } else {
        leafletMap.setView([16.0,108.0], 6);
      }
    }
  }

  function popupHtml(l){
    var d = districtByKey(l.city, l.district);
    var src = SOURCE_LABEL[l.source];
    var desc = l.desc.length > 100 ? l.desc.slice(0,100) + "…" : l.desc;
    var priceHtml = (l.price===null) ? "цена по запросу" : (fmtPrice(l.price) + ' ₫');
    return '<div class="pt-top"><span class="pt-src">' + src.short + '</span><span class="pt-price">' + priceHtml + '</span></div>' +
      '<div class="pt-meta">' + l.type + ' · ' + d.name + (l.area ? (" · " + l.area + " м²") : "") + '</div>' +
      '<div class="pt-desc">' + desc + '</div>' +
      '<div class="pt-approx">📍 положение на карте приблизительное</div>' +
      '<a class="pt-hint" href="' + l.url + '" target="_blank" rel="noopener">Открыть объявление →</a>';
  }

  function renderLeafletMarkers(list){
    if (!leafletReady) return;
    markerLayerGroup.clearLayers();
    list.forEach(function(l){
      if (typeof l.lat !== "number" || typeof l.lon !== "number") return;
      var marker = L.circleMarker([l.lat, l.lon], {
        radius: 7, weight: 1.6, color: "var(--surface)",
        fillColor: "#1E7A4C", fillOpacity: 0.9
      });
      marker.bindPopup(popupHtml(l), {closeButton:false, maxWidth:240});
      var openListing = function(){ window.open(l.url, "_blank", "noopener"); };
      marker.on("mouseover", function(){ marker.openPopup(); marker.setStyle({radius:10}); });
      marker.on("mouseout", function(){ marker.closePopup(); marker.setStyle({radius:7}); });
      marker.on("click", openListing);
      marker.addTo(markerLayerGroup);
    });
  }

  function renderSuggestions(){
    var q = el.districtInput.value.trim().toLowerCase();
    var city = CITIES[state.city];
    var matches = city.districts.filter(function(d){
      return !q || d.name.toLowerCase().indexOf(q)!==-1 || d.hint.toLowerCase().indexOf(q)!==-1;
    });
    el.districtSuggest.innerHTML = "";
    if (matches.length===0){
      var li = document.createElement("li"); li.className = "suggest-empty"; li.textContent = "Районы не найдены";
      el.districtSuggest.appendChild(li);
    } else {
      matches.forEach(function(d){
        var li = document.createElement("li");
        var b = document.createElement("button"); b.type = "button";
        b.innerHTML = "<span>"+d.name+"</span><span class='hint'>"+d.hint+"</span>";
        b.addEventListener("click", function(){
          state.district = d.key; el.districtInput.value = d.name; el.districtSuggest.hidden = true;
          renderCityMap(); applyFilters();
        });
        li.appendChild(b); el.districtSuggest.appendChild(li);
      });
    }
    el.districtSuggest.hidden = false;
  }
  el.districtInput.addEventListener("focus", renderSuggestions);
  el.districtInput.addEventListener("input", function(){
    if (state.district && el.districtInput.value.trim() === "") state.district = null;
    renderSuggestions();
  });
  el.districtInput.addEventListener("keydown", function(e){ if (e.key === "Escape") el.districtSuggest.hidden = true; });
  document.addEventListener("click", function(e){ if (!e.target.closest(".autocomplete")) el.districtSuggest.hidden = true; });
  el.districtClear.addEventListener("click", function(){
    state.district = null; el.districtInput.value = ""; renderCityMap(); applyFilters(); el.districtInput.focus();
  });

  function renderBudgetChips(){
    el.budgetChips.innerHTML = "";
    var allBtn = document.createElement("button");
    allBtn.type="button"; allBtn.className="chip"; allBtn.textContent="Любой";
    allBtn.setAttribute("aria-pressed", (state.maxBudget===null && state.minBudget===null) ? "true":"false");
    allBtn.addEventListener("click", function(){ setBudgetRange(BUDGET_MIN, BUDGET_MAX); });
    el.budgetChips.appendChild(allBtn);
    BUDGET_CHIPS.forEach(function(v){
      var b = document.createElement("button");
      b.type="button"; b.className="chip"; b.textContent="до " + v;
      b.setAttribute("aria-pressed", (state.maxBudget===v && state.minBudget===null) ? "true":"false");
      b.addEventListener("click", function(){ setBudgetRange(BUDGET_MIN, v); });
      el.budgetChips.appendChild(b);
    });
  }

  function clampBudget(v){
    if (isNaN(v)) return BUDGET_MIN;
    return Math.max(BUDGET_MIN, Math.min(BUDGET_MAX, v));
  }

  function setBudgetRange(lo, hi){
    lo = clampBudget(lo); hi = clampBudget(hi);
    if (lo > hi){ var t=lo; lo=hi; hi=t; }
    state.minBudget = (lo <= BUDGET_MIN) ? null : lo;
    state.maxBudget = (hi >= BUDGET_MAX) ? null : hi;
    syncBudgetUI();
    renderBudgetChips();
    applyFilters();
  }

  function syncBudgetUI(){
    var lo = state.minBudget===null ? BUDGET_MIN : state.minBudget;
    var hi = state.maxBudget===null ? BUDGET_MAX : state.maxBudget;
    el.budgetMinInput.value = lo;
    el.budgetMaxInput.value = hi;
    el.budgetMinRange.value = lo;
    el.budgetMaxRange.value = hi;
    var pctLo = (lo - BUDGET_MIN) / (BUDGET_MAX - BUDGET_MIN) * 100;
    var pctHi = (hi - BUDGET_MIN) / (BUDGET_MAX - BUDGET_MIN) * 100;
    el.budgetRangeFill.style.left = pctLo + "%";
    el.budgetRangeFill.style.width = Math.max(0, pctHi - pctLo) + "%";
  }

  function setupBudgetSlider(){
    el.budgetMinRange.min = el.budgetMaxRange.min = el.budgetMinInput.min = el.budgetMaxInput.min = BUDGET_MIN;
    el.budgetMinRange.max = el.budgetMaxRange.max = el.budgetMinInput.max = el.budgetMaxInput.max = BUDGET_MAX;

    el.budgetMinRange.addEventListener("input", function(){
      var lo = parseFloat(el.budgetMinRange.value);
      var hi = state.maxBudget===null ? BUDGET_MAX : state.maxBudget;
      if (lo > hi) lo = hi;
      el.budgetMinRange.classList.add("on-top");
      state.minBudget = (lo <= BUDGET_MIN) ? null : lo;
      syncBudgetUI(); renderBudgetChips(); applyFilters();
    });
    el.budgetMaxRange.addEventListener("input", function(){
      var hi = parseFloat(el.budgetMaxRange.value);
      var lo = state.minBudget===null ? BUDGET_MIN : state.minBudget;
      if (hi < lo) hi = lo;
      el.budgetMinRange.classList.remove("on-top");
      state.maxBudget = (hi >= BUDGET_MAX) ? null : hi;
      syncBudgetUI(); renderBudgetChips(); applyFilters();
    });
    el.budgetMinInput.addEventListener("input", function(){
      var v = parseFloat(el.budgetMinInput.value.replace(",", "."));
      var hi = state.maxBudget===null ? BUDGET_MAX : state.maxBudget;
      setBudgetRange(isNaN(v) ? BUDGET_MIN : v, hi);
    });
    el.budgetMaxInput.addEventListener("input", function(){
      var v = parseFloat(el.budgetMaxInput.value.replace(",", "."));
      var lo = state.minBudget===null ? BUDGET_MIN : state.minBudget;
      setBudgetRange(lo, isNaN(v) ? BUDGET_MAX : v);
    });
    syncBudgetUI();
  }

  function renderDaysChips(){
    el.daysChips.innerHTML = "";
    DAY_OPTIONS.forEach(function(v){
      var b = document.createElement("button");
      b.type="button"; b.className="chip gold"; b.textContent = v + " " + dayWord(v);
      b.setAttribute("aria-pressed", state.maxDays===v ? "true":"false");
      b.addEventListener("click", function(){ state.maxDays=v; renderDaysChips(); applyFilters(); });
      el.daysChips.appendChild(b);
    });
  }
  function dayWord(n){
    if (n===1) return "день";
    if ([2,3,4].indexOf(n)!==-1) return "дня";
    return "дней";
  }

  function renderSourceChips(){
    el.sourceChips.innerHTML = "";
    SOURCES.forEach(function(s){
      var b = document.createElement("button");
      b.type="button"; b.className="chip"; b.disabled = !s.active;
      b.innerHTML = '<span class="dot" style="background:'+s.color+'"></span>' + s.label + (s.active ? "" : " · скоро");
      b.setAttribute("aria-pressed", (s.active && state.sources.has(s.key)) ? "true":"false");
      if (s.active){
        b.addEventListener("click", function(){
          if (state.sources.has(s.key)) state.sources.delete(s.key); else state.sources.add(s.key);
          renderSourceChips(); applyFilters();
        });
      }
      el.sourceChips.appendChild(b);
    });
  }

  function renderTypeChips(){
    el.typeChips.innerHTML = "";
    var allBtn = document.createElement("button");
    allBtn.type="button"; allBtn.className="chip"; allBtn.textContent="Все";
    allBtn.setAttribute("aria-pressed", state.type===null ? "true":"false");
    allBtn.addEventListener("click", function(){ state.type=null; renderTypeChips(); applyFilters(); });
    el.typeChips.appendChild(allBtn);
    TYPE_OPTIONS.forEach(function(t){
      var b = document.createElement("button");
      b.type="button"; b.className="chip"; b.textContent=t;
      b.setAttribute("aria-pressed", state.type===t ? "true":"false");
      b.addEventListener("click", function(){ state.type = (state.type===t) ? null : t; renderTypeChips(); applyFilters(); });
      el.typeChips.appendChild(b);
    });
  }

  el.sortToggle.addEventListener("click", function(e){
    var btn = e.target.closest("button[data-sort]");
    if (!btn) return;
    state.sort = btn.getAttribute("data-sort");
    Array.prototype.forEach.call(el.sortToggle.querySelectorAll("button"), function(b){ b.classList.toggle("active", b===btn); });
    applyFilters();
  });

  function detailsHtml(l){
    if (!l.details) return "";
    var rows = DETAIL_ORDER.filter(function(k){ return l.details[k]; }).map(function(k){
      return '<div class="details-row"><dt>' + DETAIL_LABELS[k] + '</dt><dd>' + l.details[k] + '</dd></div>';
    }).join("");
    var open = state.openDetails.has(l.id);
    return '<button class="details-toggle" type="button" data-details-for="'+l.id+'" aria-expanded="'+open+'">Подробнее (депозит, коммуналка, удобства) <span class="arrow">▾</span></button>' +
      '<dl class="details-panel"' + (open ? "" : " hidden") + ' id="details-'+l.id+'">' + rows + '</dl>';
  }

  function applyFilters(){
    var city = CITIES[state.city];
    var list = LISTINGS.filter(function(l){
      if (l.city !== state.city) return false;
      if (!state.sources.has(l.source)) return false;
      if (state.district && l.district !== state.district) return false;
      if (state.minBudget !== null && l.price < state.minBudget*1000000) return false;
      if (state.maxBudget !== null && l.price > state.maxBudget*1000000) return false;
      if (l.daysAgo > state.maxDays) return false;
      if (state.type && l.type !== state.type) return false;
      return true;
    });
    list.sort(function(a,b){
      if (a.price===null && b.price===null) return 0;
      if (a.price===null) return 1;
      if (b.price===null) return -1;
      if (state.sort==="new") return a.daysAgo-b.daysAgo || a.price-b.price;
      return state.sort==="asc" ? a.price-b.price : b.price-a.price;
    });

    el.resultsCount.textContent = list.length + " " + declineObjav(list.length);
    var distLabel = state.district ? districtByKey(state.city, state.district).name : "любой район";
    var budgetLabel;
    if (state.minBudget===null && state.maxBudget===null) budgetLabel = "любой бюджет";
    else if (state.minBudget===null) budgetLabel = "до " + fmtPrice(state.maxBudget*1000000) + " ₫/мес";
    else if (state.maxBudget===null) budgetLabel = "от " + fmtPrice(state.minBudget*1000000) + " ₫/мес";
    else budgetLabel = "от " + fmtPrice(state.minBudget*1000000) + " до " + fmtPrice(state.maxBudget*1000000) + " ₫/мес";
    var typeLabel = state.type ? state.type.toLowerCase() : "любой тип";
    el.resultsContext.textContent = city.name + " · " + distLabel + " · " + typeLabel + " · " + budgetLabel + " · за " + state.maxDays + " " + dayWord(state.maxDays);

    el.resultsList.innerHTML = "";
    el.emptyState.hidden = list.length !== 0;

    list.forEach(function(l){
      var d = districtByKey(l.city, l.district);
      var src = SOURCE_LABEL[l.source];
      var card = document.createElement("article");
      card.className = "listing-card";
      var noticeHtml = (l.details && l.details.notice && l.details.notice.indexOf("⚠")===0)
        ? '<p class="listing-notice">' + l.details.notice + '</p>' : "";
      card.innerHTML =
        '<div class="listing-top">' +
          '<span class="source-pill"><i style="background:'+src.color+'"></i>' + src.short + '</span>' +
          '<span class="posted">' + l.posted + '</span>' +
        '</div>' +
        '<div>' +
          '<div class="listing-type">' + l.type + '</div>' +
          '<div class="listing-meta">' + d.name + (l.area ? (" · " + l.area + " м²") : "") + '</div>' +
        '</div>' +
        '<p class="listing-desc">' + l.desc + '</p>' +
        noticeHtml +
        detailsHtml(l) +
        '<div class="listing-bottom">' +
          '<span class="price">' + (l.price===null ? "цена по запросу" : (fmtPrice(l.price) + ' <small>₫ / мес</small>')) + '</span>' +
          '<a class="open-link" href="' + l.url + '" target="_blank" rel="noopener">Открыть объявление →</a>' +
        '</div>';
      var toggleBtn = card.querySelector(".details-toggle");
      if (toggleBtn){
        toggleBtn.addEventListener("click", function(){
          var panel = card.querySelector(".details-panel");
          var willOpen = panel.hasAttribute("hidden");
          if (willOpen){ panel.removeAttribute("hidden"); state.openDetails.add(l.id); }
          else { panel.setAttribute("hidden",""); state.openDetails.delete(l.id); }
          toggleBtn.setAttribute("aria-expanded", willOpen);
        });
      }
      el.resultsList.appendChild(card);
    });
    renderLeafletMarkers(list);
  }

  function declineObjav(n){
    var mod10 = n%10, mod100 = n%100;
    if (mod10===1 && mod100!==11) return "объявление";
    if ([2,3,4].indexOf(mod10)!==-1 && (mod100<10 || mod100>=20)) return "объявления";
    return "объявлений";
  }

  el.resetBtn.addEventListener("click", function(){
    state.district = null; state.minBudget=null; state.maxBudget=null; state.maxDays=60; state.sort="asc"; state.type=null;
    state.sources = new Set(SOURCES.filter(function(s){ return s.active; }).map(function(s){ return s.key; }));
    el.districtInput.value="";
    Array.prototype.forEach.call(el.sortToggle.querySelectorAll("button"), function(b){ b.classList.toggle("active", b.getAttribute("data-sort")==="asc"); });
    syncBudgetUI(); renderBudgetChips(); renderDaysChips(); renderSourceChips(); renderTypeChips(); renderCityMap(); applyFilters();
  });

  function renderFbGroups(){
    var list = document.getElementById("fb-groups-list");
    var title = document.getElementById("fb-groups-title");
    if (!list) return;
    var groups = FB_GROUPS[state.city] || [];
    title.textContent = "Facebook-группы по аренде — " + CITIES[state.city].name;
    list.innerHTML = "";
    groups.forEach(function(g){
      var li = document.createElement("li");
      li.innerHTML = '<a href="'+g.url+'" target="_blank" rel="noopener"><strong>'+g.name+'</strong></a>' +
        (g.members!=="—" ? (" · " + g.members + " участников") : "") +
        (g.joined ? ' · <span style="color:var(--accent);font-weight:700;">вы уже состоите</span>' : "") +
        " — " + g.note;
      list.appendChild(li);
    });
  }

  initLeafletMap();
  renderCityTabs(); renderCityMap(); setupBudgetSlider(); renderBudgetChips(); renderDaysChips(); renderSourceChips(); renderTypeChips(); renderFbGroups(); applyFilters();
})();
</script>
"""

HTML = HTML.replace("__DATA_JSON__", DATA_JSON)
HTML = HTML.replace("__LISTING_COUNT__", str(len(LISTINGS)))

out_path = W + "/vietnam-rent-finder.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print("Wrote", out_path, "size", len(HTML))
