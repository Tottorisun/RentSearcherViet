# -*- coding: utf-8 -*-
import json, re
import datetime

RU_MONTHS_GENITIVE = ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]
def ru_today_stamp():
    d = datetime.date.today()
    return f"{d.day} {RU_MONTHS_GENITIVE[d.month-1]} {d.year}"

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
        {"name":"NHÀ ĐẤT NHA TRANG ✅","members":"149,8 тыс.","url":"https://www.facebook.com/groups/NhaDatNhaTrang/","note":"недвижимость шире — есть и продажа, и аренда"},
        {"name":"Nha Trang Apartment And House For Rent ✅","members":"—","url":"https://www.facebook.com/groups/nhatrang.apartment.and.house/","note":"аренда квартир и домов"},
        {"name":"Căn hộ cho thuê Nha Trang","members":"62 тыс.","url":"https://www.facebook.com/groups/593714207638751/","note":"структурированные объявления с ценой, как Marketplace"},
        {"name":"Cho Thuê Căn Hộ Giá Rẻ Nha Trang","members":"—","url":"https://www.facebook.com/groups/chothuecanhogiarenhatrang/","note":"бюджетные квартиры"},
        {"name":"Cho Thuê Nhà & Phòng Trọ Sinh Viên NHA TRANG","members":"—","url":"https://www.facebook.com/groups/238809506689365/","note":"комнаты и жильё для студентов"}
    ],
    "da-lat": [
        {"name":"CHO THUÊ NHÀ NGUYÊN CĂN ĐÀ LẠT ✅","members":"105 тыс.","url":"https://www.facebook.com/groups/975470559939040/","note":"аренда домов целиком"},
        {"name":"PHÒNG TRỌ - NHÀ CHO THUÊ ĐÀ LẠT","members":"70 тыс.","url":"https://www.facebook.com/groups/211616406116962/","note":"комнаты и дома"},
        {"name":"NHÀ VÀ CĂN HỘ CHO THUÊ ĐÀ LẠT / DALAT HOUSE AND APARTMENT FOR RENT","members":"50 тыс.","url":"https://www.facebook.com/groups/356237492011374/","note":"дома и квартиры"},
        {"name":"CHO THUÊ NHÀ ĐÀ LẠT","members":"49 тыс.","url":"https://www.facebook.com/groups/1607478209766787/","note":"общая аренда домов"},
        {"name":"THUÊ PHÒNG ĐÀ LẠT","members":"42 тыс.","url":"https://www.facebook.com/groups/2132944206982026/","note":"комнаты, квартиры, дома целиком"}
    ],
    "da-nang": [
        {"name":"Phòng Trọ, Căn Hộ, Nhà Đà Nẵng Cho Thuê","members":"225 тыс.","url":"https://www.facebook.com/groups/phongtrocanhonhadanang/","note":"комнаты, квартиры, дома"},
        {"name":"Cho Thuê Nhà Nguyên Căn Đà Nẵng","members":"165 тыс.","url":"https://www.facebook.com/groups/476056366996433/","note":"аренда домов целиком"},
        {"name":"CĂN HỘ CHO THUÊ ĐÀ NẴNG","members":"145 тыс.","url":"https://www.facebook.com/groups/599988861199745/","note":"квартиры"},
        {"name":"Cho Thuê Nhà Nguyên Căn Giá Rẻ Đà Nẵng","members":"86 тыс.","url":"https://www.facebook.com/groups/682623845225623/","note":"бюджетные дома"},
        {"name":"Căn hộ cho thuê Đà Nẵng (Apartment for rent in Danang)","members":"68 тыс.","url":"https://www.facebook.com/groups/198876884532146/","note":"квартиры"}
    ],
    "ho-chi-minh": [
        {"name":"Housing in Saigon (Ho Chi Minh City, Vietnam)","members":"43 тыс.","url":"https://www.facebook.com/groups/housing.HCMC","note":"общегородская, охватывает все 5 районов подборки"},
        {"name":"PHÒNG TRỌ QUẬN 1","members":"249,7 тыс.","url":"https://www.facebook.com/groups/q1.phongtro.club/","note":"комнаты и квартиры именно по Quận 1 / Bến Thành"},
        {"name":"PHÒNG TRỌ QUẬN 4","members":"244 тыс.","url":"https://www.facebook.com/groups/q4.phongtro.club/","note":"комнаты и квартиры именно по Quận 4 / Khánh Hội"},
        {"name":"TÔI LÀ DÂN THẢO ĐIỀN - AN PHÚ - BÌNH AN","members":"—","url":"https://www.facebook.com/groups/anphuthaodienneighbours/","note":"резидентское сообщество Thảo Điền/An Phú, включает аренду"},
        {"name":"Phu My Hung District 7 Expats","members":"—","url":"https://www.facebook.com/groups/phumyhung7/","note":"экспат-сообщество Phú Mỹ Hưng"},
        {"name":"GROUP CĂN HỘ ASCENTIA - THE ANTONIA PHÚ MỸ HƯNG","members":"—","url":"https://www.facebook.com/groups/590911979369020/","note":"узкоспециализированная — именно по The Ascentia и соседнему The Antonia"}
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
L(320,"nha-trang","pl","Квартира",10000000,65,"Угловая 2-спальная квартира в КДТ Phước Long (CT4 Hud, ул. 28), балкон, качественная мебель.","https://www.facebook.com/groups/chothuecanhonhatrangkhanhhoa/posts/27944490621827590/","недавно",0,source="facebook",details={"alsoOn":[{"source":"fbmarketplace","url":"https://www.facebook.com/marketplace/item/1491098622776266/"},{"source":"chotot","url":"https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134184961.htm"}],"deposit":"2 месяца (оплата за 2)","notice":"тел. 0989 819 892"}),
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
  details={"duplicateOf":320,"deposit":"2 месяца","notice":"⚠ на карточке FB отображается цена 1 000 000 ₫ — это баг ввода цены у продавца, в тексте описания указано 10 000 000 ₫/мес, используется цена из описания.","contact":"продавец Lê Đình Ngọc (на FB с 2018)"}),

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
  details={"amenities":"полностью меблирована, бассейн, спортзал, паркинг, охрана 24/7, лобби","notice":"⚠ на карточке FB отображается цена 16 000 ₫ — баг ввода цены, в описании указано 16 млн ₫/мес (≈630 USD) с учётом сервисного сбора.","contact":"+84 931 914 941 (iMessage/звонок/Zalo/Viber/WhatsApp/KakaoTalk)","alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-hiyori-garden-tower-phuong-an-hai-tp-da-nang/cho-2-phong-ngu-view-cau-rong-son-tra-a-nang-pr46219424"}]}),

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
  details={"alsoOn":[{"source":"fbmarketplace","url":"https://www.facebook.com/marketplace/item/1330550035468360/"}],"contact":"Trần Ngọc Nhiễm (8 объявлений)"}),


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
  details={"alsoOn":[{"source":"fbmarketplace","url":"https://www.facebook.com/marketplace/item/1578595263909443/"},{"source":"fbmarketplace","url":"https://www.facebook.com/marketplace/item/1043456721722228/"}],"notice":"⚠ дата истечения тарифа объявления — 14.08.26 (пару дней назад)","contact":"Nguyễn Tấn Huy, 0937 833 ***"}),


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
  details={"duplicateOf":592,"notice":"⚠ на карточке FB отображается усечённая цена 21 000 ₫, в описании 21 млн ₫/мес.","amenities":"бассейн, спортзал, мини-маркет","contact":"Tấn Huy"}),

L(607,"ho-chi-minh","bq","Квартира",21000000,130,
  "3-спальная квартира (2 с/у) в охраняемом комплексе Thanh Đa View, бассейн, бесплатный спортзал, супермаркет.",
  "https://www.facebook.com/marketplace/item/1330550035468360/","проверено 17 авг",1,source="fbmarketplace",
  details={"duplicateOf":570,"notice":"⚠ на карточке FB цена показана как 1 ₫ (баг), в описании указано «21TR» (21 млн ₫/мес)."}),

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
  details={"duplicateOf":592,"contact":"Tấn Huy (тот же агент, что и объявления по Q4 выше)"}),
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
  details={"alsoOn":[{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134218405.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134273371.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134221426.htm"}],"contact":"Lực Villa Him Lam Quận 7","notice":"подходит под офис/спа/школу или другой бизнес, а не только под жильё."}),

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
  details={"contact":"Quỳnh Như HiFriendz","notice":"в объявлении указано «скоро освободится» — возможен небольшой срок ожидания перед заездом.","alsoOn":[{"source":"chotot","url":"https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134295878.htm"}]}),

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
  details={"duplicateOf":820,"contact":"NGUYỄN HOA"}),

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
  details={"contact":"hà pihomes","alsoOn":[{"source":"chotot","url":"https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134295111.htm"}]}),

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
  details={"alsoOn":[{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134234709.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134273497.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134254961.htm"},{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134244463.htm"}],"notice":"Batdongsan не публикует дату размещения; свежесть определена по ID объявления (prNNNNNNNN) — выше максимального ID, зафиксированного как уже виденный в проверках по состоянию на 18 авг (46197409). Цена подтверждена дважды: в карточке поиска и на странице объявления (поле «Khoảng giá»). Этот же объект (тот же адрес-ориентир, площадь и цена) также был замечен опубликованным под 4 разными аккаунтами на Chợ Tốt — добавлена только эта версия во избежание задвоения."}),

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

L(878,"nha-trang","vp","Квартира",12000000,65,
  "2-спальная квартира (2 с/у) в комплексе Mường Thanh Viễn Triều, 03 Phạm Văn Đồng, Vĩnh Phước — напротив пляжа Hòn Chồng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134235623.htm","сегодня",0,source="chotot",
  details={"amenities":"бассейн и спортзал в комплексе, ТЦ на 1 этаже, рядом больница и школа (50 м), рынок Vĩnh Hải (500 м)","notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Nguyễn Tuấn Đại","priceHistory":[{"price":10000000,"date":"2026-08-24"}]}),

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
  details={"duplicateOf":320,"deposit":"2 месяца (оплата за 2)","contact":"Hà Lương IT"}),

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
  details={"notice":"контакт скрыт продавцом (номер замаскирован ***)","contact":"Vũ Thành Long","alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phu-tai-residence-phuong-quy-nhon-tinh-gia-lai/view-ep-mat-me-ca-ngay-13-trieu-thang-full-noi-that-moi-pr46187120"}]}),

L(928,"quy-nhon","qn","Дом",3200000,40,
  "Дом с мезонином в переулке от ул. Nguyễn Huệ, рядом с провинциальной больницей, рынком и Университетом Куинён. Несколько шагов до моря.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-qui-nhon-binh-dinh/134220484.htm","вчера",1,source="chotot",
  details={"contact":"Chị Quỳnh"}),
L(929,"ho-chi-minh","th","Квартира",10000000,98,
  "2-спальная квартира (2 с/у) в ЖК Hoàng Anh 2, ул. Trần Xuân Soạn (д.783), Tân Hưng, Q7. Высокий этаж, светлая, меблировка в наличии.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134237102.htm","сегодня",0,source="chotot",
  details={"notice":"рядом крупные вузы, удобно до Q1/Q4/Q8","contact":"N.Phương"}),

L(930,"ho-chi-minh","th","Квартира",9400000,50,
  "2-спальная квартира целиком, ул. Trần Xuân Soạn (д.1041), Tân Hưng, Q7, рядом KDC Him Lam. Полная меблировка, своя стиральная машина.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134237670.htm","сегодня",0,source="chotot",
  details={"amenities":"рядом Lotte Mart, SC VivoCity, ТDTU/RMIT","contact":"Phú (Thanh Phú HiFriendz)"}),

L(931,"ho-chi-minh","kh","Квартира",19000000,65,
  "2-спальная квартира (2 с/у) в ЖК Millennium, Q4, рядом центр Q1 и рынок. Полная меблировка, заезд сразу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134209596.htm","вчера",1,source="chotot",
  details={"contact":"Ngân"}),

L(932,"ho-chi-minh","kh","Квартира",20000000,75,
  "2-спальная квартира (2 с/у) в ЖК Millennium, ул. Bến Vân Đồn (д.138), Q4, у моста Calmette рядом Q1. Вид на город.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133116832.htm","вчера",1,source="chotot",
  details={"amenities":"бассейн, спортзал, ресторан в комплексе","contact":"Việt Hoàng"}),

L(933,"ho-chi-minh","tm","Квартира",7200000,50,
  "1-спальная квартира с полной меблировкой прямо у рынка Tân Mỹ, рядом Phú Mỹ Hưng, Q7. Отдельная спальня, заезд сразу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134205509.htm","вчера",1,source="chotot",
  details={"contact":"Linh"}),

L(934,"ho-chi-minh","ak","Квартира",15000000,51,
  "1-спальная квартира в ЖК New City Thủ Thiêм, Thủ Đức. Полная современная меблировка, заезд сразу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134204593.htm","вчера",1,source="chotot",
  details={"notice":"в объявлении внутреннее расхождение: заголовок и поле «Thiết kế» указывают 1 спальню, но один абзац текста ошибочно упоминает 2 — использовано устойчивое значение (1 спальня)","contact":"Trang"}),

L(935,"ho-chi-minh","tm","Квартира",28000000,84,
  "Угловая 2-спальная квартира (2 с/у) в ЖК The Ascentia, Phú Mỹ Hưng, Q7. Премиальная меблировка, светлая, естественная вентиляция. Бассейн, спортзал, лаунж, зона барбекю, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134195347.htm","2 дня назад",2,source="chotot",
  details={"contact":"Hoàng Trúc Loan"}),

L(936,"ho-chi-minh","tm","Дом",16000000,52,
  "Дом целиком, полная качественная меблировка, ул. Huỳnh Tấn Phát, Tân Phú/Tân Mỹ, Q7. 2 спальни, гостиная, кухня-столовая, 2 с/у, ТВ 65\".",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134196283.htm","2 дня назад",2,source="chotot",
  details={"contact":"Mr Ngọc"}),

L(937,"ho-chi-minh","tm","Квартира",23000000,132,
  "4-спальная квартира (3 с/у, +кладовая) в ЖК Sunshine Sky City, 23 Phú Thuận, Tân Mỹ, Q7. 2 балкона, базовая меблировка (шторы, кондиционеры, водонагреватель, кухонный гарнитур с индукционной плитой). Освобождается с 15.09.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134176311.htm","3 дня назад",3,source="chotot",
  details={"notice":"расхождение цены: структурное поле API отдаёт 22 000 000, но заголовок и текст объявления говорят «23tr/thương lượng» — использована цена из текста (торг возможен)","contact":"Nhung"}),
L(938,"ho-chi-minh","th","Квартира",9000000,50,
  "1-спальная квартира (1 с/у) с новой полной меблировкой, ул. Đường Số 79, Tân Hưng, Q7, рядом Lotte Mart. Светлая, отдельная кухня, естественная вентиляция.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133129867.htm","сегодня",0,source="chotot",
  details={"contact":"Trịnh Hoàng Tâm"}),
L(939,"ho-chi-minh","th","Дом",15000000,100,
  "Дом целиком (5×20-22м, 2 спальни, 2 с/у) на ул. Lâm Văn Bền, Tân Hưng, Q7. Подходит для жилья или под небольшой офис. Витринная дата API вводила в заблуждение (repush) — использован честный orig_list_time (~2 дня).",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134196586.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nguyễn Hoa"}),

L(940,"ho-chi-minh","tm","Квартира",14000000,65,
  "2-спальная квартира (2 с/у) в River Panorama, Tân Mỹ (Phú Mỹ Hưng), Q7. Средний этаж, светлый вид, полная меблировка, готова к заселению.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/131760231.htm","2 часа назад",0,source="chotot",
  details={"contact":"BDS Premium Sky (Minh Thành)"}),

L(941,"ho-chi-minh","tm","Дом",45000000,140,
  "Вилла в закрытом комплексе Green Star Hưng Lộc Phát рядом с Phú Mỹ Hưng, Tân Mỹ, Q7. Участок 7×20м (140м²), 1 этаж + 2 верхних, ориентация СЗ, документы HĐMB.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134238016.htm","2 часа назад",0,source="chotot",
  details={"contact":"Xuyến Liễu"}),

L(942,"ho-chi-minh","tm","Дом",12500000,48,
  "Дом целиком (1 этаж+1 этаж, 4×12м, 2 спальни, 3 с/у) в переулке ул. Nguyễn Thị Thập рядом с рынком Tân Mỹ, Q7. С мебелью, подходит под жильё или небольшой офис.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133909291.htm","10 часов назад",0,source="chotot",
  details={"contact":"LHP"}),

L(943,"ho-chi-minh","tm","Дом",7200000,25,
  "Дом целиком (1 этаж+1 этаж, гостиная, 2 спальни, с/у, кухня) в широком переулке для машины, 730 Huỳnh Tấn Phát, Tân Mỹ, Q7. Рядом супермаркет GO! (бывший Big C) и рынок. Приоритет длительной аренде.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134228666.htm","9 часов назад",0,source="chotot",
  details={"contact":"Tuấn Anh Land"}),

L(944,"ho-chi-minh","ak","Квартира",25000000,72,
  "2-спальная квартира (2 с/у, 71,6м²) в ЖК De Capella, 116 Lương Định Của, An Khánh (Thảo Điền), Thủ Đức. Полная меблировка. Ward подтверждён геокодингом адреса.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134233963.htm","5 часов назад",0,source="chotot",
  details={"contact":"Lê Thanh Trung"}),

L(945,"ho-chi-minh","ak","Квартира",16000000,75,
  "2-спальная квартира с дизайнерским ремонтом в Masteri Thảo Điền, An Khánh, Thủ Đức. Высокий этаж, вид на реку.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/126685241.htm","5 часов назад",0,source="chotot",
  details={"contact":"Phương Nhi"}),

L(946,"ho-chi-minh","kh","Квартира",17000000,77,
  "2-спальная квартира (самая большая 2BR-планировка в комплексе) в Millennium на ул. Bến Vân Đồn, Khánh Hội, Q4. Высокий этаж, вид на Bitexco.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/126278417.htm","5 часов назад",0,source="chotot",
  details={"contact":"Phương Nhi"}),

L(947,"ho-chi-minh","kh","Студия",5500000,35,
  "Студия с отдельной кухней (без запаха от соседей), своей стиральной машиной и большим окном, у моста Calmette (Bến Vân Đồn), Khánh Hội, Q4 — рядом Q1/Q3/Q10. Свободный график, без совместного проживания с хозяином. Цена за 1 чел. — 5,5 млн ₫, за 2 чел. — 7,5 млн ₫.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/132262424.htm","21 час назад",0,source="chotot",
  details={"contact":"Duy Khoa Neway","occupancy_price":"1 чел. — 5,5 млн ₫, 2 чел. — 7,5 млн ₫"}),

L(948,"ho-chi-minh","bth","Студия",6400000,30,
  "Студия с отдельной кухней на ул. Phạm Ngũ Lão, Bến Thành, Q1 (между Bùi Viện и парком 23/9), 5 минут пешком до метро Bến Thành.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134226838.htm","10 часов назад",0,source="chotot",
  details={"contact":"Huỳnh Kỳ Đức"}),
L(949,"ho-chi-minh","bth","Студия",7000000,35,
  "Квартира-студия (1 антресоль/спальное место) в старом доме на ул. Nguyễn Thái Bình, Bến Thành, Q1 — рядом рынок Bến Thành, мост Ông Lãnh, Đại học Ngân hàng, пешеходная улица Bùi Viện. Полная меблировка, лифт, электричество/вода по гос. тарифу, большой охраняемый паркинг.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134243647.htm","11 часов назад",0,source="chotot",
  details={"contact":"Thành Khang"}),

L(950,"ho-chi-minh","bth","Студия",6900000,35,
  "Студия с большим светлым окном рядом с ДХ Ngân Hàng/Văn Lang/Hoa Sen, Bến Thành, Q1. Полная меблировка, своя стиральная машина, замок по отпечатку пальца, свободный график без совместного проживания с хозяином. Точный адрес/название дома в объявлении не указан — только ориентиры на близлежащие вузы.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134235095.htm","20 часов назад",0,source="chotot",
  details={"contact":"Boon Apartments"}),

L(951,"ho-chi-minh","kh","Квартира",13000000,70,
  "2-спальная квартира (1 с/у, угловая, 3 окна) в ЖК H1 Hoàng Diệu, Khánh Hội, Q4 — в 1 мосту (Calmette) от Q1. Полная меблировка (стиралка, сушилка, холодильник, ТВ), рядом рынок, автобусы, Đại học Luật, порт Nhà Rồng, рынок Xóm Chiếu. Сдаёт напрямую хозяин (chính chủ), без посредников. Депозит 2 мес., договор от 1 года.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134227261.htm","1 день назад",1,source="chotot",
  details={"contact":"Hari Nguyễn","deposit":"2 месяца"}),

L(952,"ho-chi-minh","th","Студия",11000000,38,
  "Квартира-студия с полной меблировкой в ЖК Sunrise CityView, Tân Hưng, Q7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134228509.htm","1 день назад",1,source="chotot",
  details={"contact":"Minh Anh"}),

L(953,"ho-chi-minh","th","Студия",8000000,30,
  "Новая студия с балконом (только что построена, 100% новая мебель) рядом с Lotte Mart, центр Q7, Tân Hưng. Лифт, вход по отпечатку пальца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134234495.htm","20 часов назад",0,source="chotot",
  details={"contact":"Thanh Trúc"}),

L(954,"ho-chi-minh","tm","Студия",6500000,20,
  "Студия в новом закрытом жилом комплексе, Tân Mỹ, Q7 — только что освободилась. Замок по отпечатку пальца, матрас, шкаф, кухонная стойка, кондиционер, балкон, подземный паркинг, лифт, охрана, общая стиральная машина. Тарифы отдельно: электричество 4000 ₫/кВт·ч, вода 100 000 ₫/чел., паркинг 100 000 ₫/место, сервис 150 000 ₫/комната. Депозит 1 мес., договор 12 мес., животные не разрешены.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134223529.htm","1 день назад",1,source="chotot",
  details={"contact":"Hồ Quang Huy","electricity":"4 000 ₫/кВт·ч","water":"100 000 ₫/чел.","deposit":"1 месяц (12 мес. договор)"}),

L(955,"ho-chi-minh","tm","Квартира",10500000,58,
  "2-спальная квартира (1 с/у) свободна для заезда, Tân Mỹ, Q7, ~10 минут до Phú Mỹ Hưng. 3 кондиционера, водонагреватель. Точный адрес/название ЖК в объявлении не указан.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134243194.htm","12 часов назад",0,source="chotot",
  details={"contact":"Nguyễn Thị Minh Trang"}),

L(956,"ho-chi-minh","tm","Дом",30000000,80,
  "Дом целиком (4×20м, 3 этажа, 6 спален, кухня, 3 с/у, 7 кондиционеров) в 300 м от рынка Tân Mỹ, Q7. Подходит для жилья или под небольшой бизнес.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134234709.htm","20 часов назад",0,source="chotot",
  details={"duplicateOf":873,"contact":"Dương Văn Bảo"}),

L(957,"ho-chi-minh","ak","Студия",7500000,35,
  "Квартира с отдельной кухней и просторным балконом, Thảo Điền (An Khánh), рядом мост Sài Gòn — удобно до Q1/Q3/Q5/Q10/Bình Thạnh/Thủ Đức. Премиальная меблировка, еженедельная уборка, паркинг с лифтом и охраной 24/7, разрешены животные.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/116727047.htm","1 день назад",1,source="chotot",
  details={"contact":"Ngọc Thịnh Hifriendz"}),

L(958,"ho-chi-minh","ak","Дом",20000000,80,
  "Дом целиком на Đường số 10, Trần Não, An Khánh (центр бывшего Q2). Оживлённый район рядом с магазинами/супермаркетами/рынком, широкий переулок для машины, крепкий дом с хорошим ремонтом.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/133870652.htm","15 часов назад",0,source="chotot",
  details={"contact":"Mi"}),
L(959,"ho-chi-minh","ak","Дом",20000000,60,
  "Дом целиком (4 этажа, 4 спальни, 4 с/у) фасадом на улицу у Trần Não, An Khánh (бывший Q2) — рядом выход к реке. Участок 5×13м (60м²), дом почти новый.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134255413.htm","4 минуты назад",0,source="chotot",
  details={"contact":"Vũ Trường Sơn"}),

L(960,"ho-chi-minh","th","Квартира",25000000,124,
  "3-спальная квартира (2 с/у) 124м² в ЖК Mỹ Khánh, в центре Phú Mỹ Hưng, Tân Hưng, Q7 — рядом ул. Nguyễn Đức Cảnh. Премиальная меблировка, бассейн и другие удобства комплекса.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134255412.htm","4 минуты назад",0,source="chotot",
  details={"contact":"Trịnh Hồng Thảo"}),

L(961,"ho-chi-minh","ak","Дом",30000000,135,
  "Дом-вилла (3 этажа, 5 комнат, кондиционеры) рядом с Trần Não, An Khánh (бывший Q2) — фасад 9 м, подходит и под офис. Долгосрочный договор.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134255116.htm","15 минут назад",0,source="chotot",
  details={"contact":"Bảo Ngọc"}),

L(962,"ho-chi-minh","tm","Квартира",15000000,84,
  "Пентхаус с террасой/садом (~80 м² сада), декорирован, с мебелью, ул. Phạm Hữu Lầu, Tân Mỹ, Q7. Просторный, светлый вид. Точная планировка (число спален) в объявлении не указана.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134255102.htm","16 минут назад",0,source="chotot",
  details={"contact":"Trang"}),

L(963,"ho-chi-minh","tm","Дом",22000000,90,
  "Дом целиком (1 этаж + 3 этажа, 4 спальни, 3 с/у) в KDC Phạm Hữu Lầu, Tân Mỹ, Q7 — в 5 минутах от Phú Mỹ Hưng, рядом школы, супермаркеты, университет Tôn Đức Thắng и RMIT (10 мин).",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134254565.htm","36 минут назад",0,source="chotot",
  details={"contact":"LHP"}),

L(964,"ho-chi-minh","ak","Квартира",15500000,50,
  "1-спальная квартира (1 с/у) 50м² в ЖК New City, An Khánh (бывший Q2), ул. Mai Chí Thọ. Полная меблировка, бассейн, спортзал, кафе Highlands, магазин у дома.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134254257.htm","47 минут назад",0,source="chotot",
  details={"contact":"Trần Hải"}),

L(965,"ho-chi-minh","kh","Квартира",29000000,108,
  "3-спальная квартира (2 с/у) 108м² в ЖК Millennium, Khánh Hội, Q4 — рядом ул. Bến Vân Đồn, вплотную к Q1. Полная меблировка, подходит для семьи или группы.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134254719.htm","31 минуту назад",0,source="chotot",
  details={"contact":"Ngân Ngân"}),

L(966,"ho-chi-minh","ak","Дом",45000000,167,
  "Вилла в закрытом компаунде на Đường số 4 (Lưu Đình Lễ), An Khánh — 1 этаж + 2 этажа, 9,5×17,5м, 3 спальни + 2 рабочих кабинета, 4 с/у, кухня, гостиная, паркинг для машины. Долгосрочный договор, торг возможен.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/132703911.htm","3 часа назад",0,source="chotot",
  details={"contact":"Huỳnh Thanh Sang"}),

L(967,"ho-chi-minh","bq","Дом",7000000,40,
  "Дом-таунхаус (1 этаж + 1 этаж с антресолью, стиральная машина есть, холодильника нет) на Thanh Đa, Bình Quới, Bình Thạnh. Свободный график, без совместного проживания с хозяином, охраняемая парковка.",
  "https://www.nhatot.com/thue-nha-dat-quan-binh-thanh-tp-ho-chi-minh/134250341.htm","4 часа назад",0,source="chotot",
  details={"contact":"Nguyễn Hoàng Danh","electricity":"4 000 ₫/кВт·ч","water":"20 000 ₫/м³","other_fees":"wifi 100 000 ₫/мес., вывоз мусора 50 000 ₫/мес., паркинг мотоцикла бесплатно"}),

L(968,"ho-chi-minh","bth","Студия",5500000,30,
  "Студия со светлым окном в центре Q1, рядом перекрёсток Ngã 6 Phù Đổng (улицы Lý Tự Trọng/Nguyễn Thái Học/Lê Thị Riêng), Bến Thành. Полная меблировка, замок по отпечатку пальца, свободный график, рядом парк 23/9 и рынок Bến Thành.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134251920.htm","2 часа назад",0,source="chotot",
  details={"contact":"CHO THUÊ CĂN HỘ DỊCH VỤ TPHCM"}),

L(969,"ho-chi-minh","kh","Квартира",18900000,65,
  "2-спальная квартира (2 с/у) 65м² в ЖК Millennium, Khánh Hội, Q4 — бассейн, спортзал, супермаркет, кафе в комплексе. По словам агента — конкурентная цена по рынку.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134250500.htm","4 часа назад",0,source="chotot",
  details={"contact":"Hương Dung (Danh Land)"}),
L(970,"da-lat","lb","Студия",4500000,35,
  "Меблированная студия-дуплекс (мансарда + первый этаж, гостиная совмещена с кухней, 1 с/у) на ул. Tô Hiệu, район Lang Biang (старое — Phường 7). Просторный общий двор, общая стиральная машина, 8 мин до долины Thung Lũng Tình Yêu.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134252520.htm","7 часов назад",0,source="chotot",
  details={"electricity":"по гостарифу","water":"по гостарифу","deposit":"1 месяц (оплата за 1)","contract":"6-12 месяцев","contact":"Hương Lê"}),

L(971,"da-lat","lv","Дом",6500000,120,
  "Дом целиком под жильё (подходит и под небольшой homestay-бизнес), ул. Hùng Vương, район Lâm Viên (старое — Phường 9). 1 этаж + терраса на крыше (зона под кофе/барбекю), 3 спальни, 4 с/у. 7 мин до озера Xuân Hương и ночного рынка.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134249060.htm","9 часов назад",0,source="chotot",
  details={"electricity":"по гостарифу","water":"по гостарифу","deposit":"2 месяца (оплата за 1)","contract":"от 12 месяцев","notice":"подходит и для проживания, и под homestay-бизнес (вторично); нет стиральной машины","contact":"Hương Lê"}),

L(972,"da-lat","cl","Квартира",11000000,100,
  "2-спальная квартира (2 с/у) на ул. La Sơn Phu Tử, район Cam Ly (старое — Phường 6). Полная меблировка, лифт и подземный паркинг в доме.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133442551.htm","10 часов назад",0,source="chotot",
  details={"deposit":"2 месяца (оплата за 1)","contract":"6-12 месяцев","contact":"Trần Thị Bích Thuỳ (Bích Thùy Land)"}),

L(973,"da-lat","lv","Дом",16000000,160,
  "Дом целиком (новое строительство, чистый и готов к заселению), квартал Lữ Gia, район Lâm Viên (старое — Phường 9). 3 просторные спальни, 2 отдельных с/у, полная меблировка, свой двор для машины, сильный wifi.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/132145853.htm","10 часов назад",0,source="chotot",
  details={"deposit":"1 месяц (оплата за 1)","notice":"только для проживания, не под бизнес","contact":"Trần Thị Bích Thuỳ (Bích Thùy Land)"}),

L(974,"da-lat","cl","Дом",21000000,72,
  "Дом-магазин (1 этаж + 3 надстройки, есть комната для алтаря), ул. Lê Thánh Tôn, район Cam Ly (старое — Phường 5). 4 спальни, 5 с/у, площадь застройки 72м² (общая площадь этажей 288м²). Первый этаж пустой под коммерцию — разрешён только «чистый» бизнес или кофейня (без общепита/баров).",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134239752.htm","вчера",1,source="chotot",
  details={"electricity":"по гостарифу","water":"по гостарифу","deposit":"1 месяц (оплата за 6)","contract":"долгосрочный","notice":"без мебели; первый этаж — под коммерцию (вторично)","contact":"Hương Lê"}),

L(975,"da-lat","lv","Квартира",9000000,40,
  "1-спальная квартира (1 с/у) на ул. Phù Đổng Thiên Vương, район Lâm Viên (старое — Phường 8). Полная меблировка (кухня, ТВ, холодильник, диван), общая стиральная машина на первом этаже, рядом Университет Далата и ночной рынок (5 мин на байке).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134239437.htm","вчера",1,source="chotot",
  details={"deposit":"1 месяц (оплата за 1)","contract":"3-6 месяцев","notice":"цена уже включает электричество, воду и wifi","contact":"Hương Lê"}),

L(976,"vung-tau","vtp","Дом",15000000,88,
  "Дом целиком (1 этаж + 2 этажа, 3 спальни, 3 с/у, комната для алтаря) на фасаде ул. Đinh Tiên Hoàng, район Vũng Tàu (старое — P.2), рядом рынок Xóm Lưới и пляж Bãi Trước. Пустой, планировка под любые нужды.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-vung-tau-ba-ria-vung-tau/134183246.htm","3 дня назад",3,source="chotot",
  details={"notice":"дата пересчитана честно по orig_list_time — сайт показывал «2 ngày trước» по list_time (после повторной публикации), фактическая разница ~24 часа (1 день)","contact":"Mỹ Lệ Vũng Tàu 79"}),

L(977,"vung-tau","vtp","Дом",10000000,64,
  "Дом целиком (1 этаж + 2 этажа, 3 спальни, 3 с/у) на ул. Bạch Đằng, район Vũng Tàu (центр). Рядом рынок, супермаркет, школа, больница, банк, торговый центр.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-vung-tau-ba-ria-vung-tau/134169720.htm","4 дня назад",4,source="chotot",
  details={"contact":"Đặng Trung Hậu"}),

L(978,"vung-tau","vtp","Дом",35000000,240,
  "Дом целиком на фасаде ул. Huỳnh Thúc Kháng, район Vũng Tàu (центр). 1 этаж + 1 этаж, 4 спальни, 4 с/у, 3 кондиционера. Подходит и для проживания, и под офис/шоурум/спа (вторично).",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-vung-tau-ba-ria-vung-tau/134169024.htm","4 дня назад",4,source="chotot",
  details={"deposit":"2 месяца","contact":"Anh Thư Vũng Tàu"}),
L(979,"ho-chi-minh","tm","Квартира",8500000,70,
  "2-спальная квартира (2 с/у) 70м² в ЖК Beleza, Tân Mỹ, Q7 — угловая, светлая (юго-восток), тихий этаж. Базовая меблировка (2 кондиционера, холодильник, стиральная машина, кровати, шкаф). Заезд с начала сентября.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134260939.htm","11 минут назад",0,source="chotot",
  details={"contact":"Nguyễn Thu Hà"}),

L(980,"ho-chi-minh","tm","Дом",21000000,60,
  "Дом целиком (1 этаж + 3 этажа, 3 спальни, 3 с/у) в переулке у ул. Huỳnh Tấn Phát, Tân Mỹ (Phú Mỹ), Q7. Полная меблировка, готов к заселению.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134259758.htm","2 часа назад",0,source="chotot",
  details={"contact":"Nhà Thuê Nguyên Căn Quận 7"}),

L(981,"ho-chi-minh","tm","Квартира",10000000,74,
  "2-спальная квартира (2 с/у) 74м² в ЖК Res3, у рынка Tân Mỹ, Q7 — угловая, напротив больницы FV. Частичная меблировка (кондиционер, кровать, шкаф, кухонный гарнитур, стиральная машина).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134258752.htm","3 часа назад",0,source="chotot",
  details={"contact":"Hồng Thúy"}),

L(982,"ho-chi-minh","tm","Квартира",12500000,75,
  "3-спальная квартира (2 с/у) 75м² в ЖК Q7 Boulevard (ул. Nguyễn Lương Bằng 600), Tân Mỹ. Угловая, светлая, базовая меблировка (шторы, кондиционер).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134255720.htm","5 часов назад",0,source="chotot",
  details={"contact":"Diễm Phương","other_fees":"управление 9 500 ₫/м², мотобайк 110 000 ₫/мес."}),

L(983,"ho-chi-minh","tm","Дом",7500000,54,
  "Дом целиком (1 этаж + 1 этаж, 2 спальни, участок 3×9м, общая жилая площадь 54м²) в переулке в районе Phú Mỹ, Tân Mỹ, Q7. Тихий жилой квартал; по словам хозяйки — не подходит под интенсивную коммерцию (общий вход с соседями).",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133443768.htm","11 часов назад",0,source="chotot",
  details={"contact":"NGUYEN THI DUNG"}),

L(984,"ho-chi-minh","th","Квартира",11000000,73,
  "2-спальная квартира 73м² в ЖК Hoàng Anh Thanh Bình, у моста Kênh Tẻ (на границе с Q4), Tân Hưng, Q7. С меблировкой (кондиционер, шторы, кухонный гарнитур, шкафы), рядом Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/131626796.htm","8 минут назад",0,source="chotot",
  details={"contact":"Nguyễn Lê"}),

L(985,"ho-chi-minh","th","Квартира",9500000,45,
  "1-спальная квартира (1 с/у) 45м² в ЖК Him Lam, Tân Hưng, Q7. Премиальная меблировка, большой подземный паркинг, рядом RMIT, Crescent Mall, Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/131274046.htm","23 минуты назад",0,source="chotot",
  details={"contact":"Hoàng Tú Homie"}),

L(986,"ho-chi-minh","th","Квартира",9500000,40,
  "1-спальная квартира с балконом 40м² в ЖК Kim Sơn (ул. Số 6), Tân Hưng, Q7 — рядом Tôn Đức Thắng, Lotte Mart, 5 минут до Q1. Полная меблировка, своя стиральная машина, принимают животных и иностранцев.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134259686.htm","2 часа назад",0,source="chotot",
  details={"contact":"Mr Luân (Chuyên căn hộ đẹp Quận 7)"}),

L(987,"ho-chi-minh","th","Дом",10000000,40,
  "Дом целиком (1 этаж + 1 этаж, 2 комнаты, 2 с/у, гостиная, кухня, 3,5×15м) в переулке для авто у ул. Lê Văn Lương, Tân Hưng, Q7.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134260240.htm","1 час назад",0,source="chotot",
  details={"contact":"Lê Vân BĐS"}),

L(988,"ho-chi-minh","th","Квартира",10000000,88,
  "2-спальная квартира (2 с/у) 88м² в ЖК Minh Thành (259 Lê Văn Lương), Tân Hưng, Q7 — рядом Lotte Mart. Просторный балкон, полная меблировка (ТВ, холодильник, стиралка, кровати, шкафы, диван, обеденный стол).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134257848.htm","3 часа назад",0,source="chotot",
  details={"contact":"Linh"}),

L(989,"ho-chi-minh","th","Квартира",32000000,130,
  "3-спальная квартира 130м² в ЖК Mỹ Phát, ул. Nguyễn Đức Cảnh, Phú Mỹ Hưng, Tân Hưng, Q7 — напротив школы Đinh Thiện Lý. Современный ремонт, тихий благоустроенный квартал.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134255579.htm","5 часов назад",0,source="chotot",
  details={"contact":"Trịnh Hồng Thảo"}),

L(990,"ho-chi-minh","th","Дом",120000000,262,
  "Вилла-квадрохаус «Mỹ Gia 1» (участок 15×17,5м = 262,5м², жилая площадь этажей 295м², 1 этаж + 2 этажа), фасад ул. Số 19, Phú Mỹ Hưng, Tân Hưng, Q7. 4 спальни, 4 с/у, собственный бассейн, сад, машиноместо.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134250972.htm","8 часов назад",0,source="chotot",
  details={"contact":"Thanh Phan (Thanh Villa)"}),

L(991,"ho-chi-minh","ak","Квартира",10500000,60,
  "1-спальная квартира (отдельный вход, первый этаж дома) 60м², переулок 11/2 Đường Số 13 у ул. Trần Não, An Khánh (бывший Q2). Полная меблировка, бесплатная парковка для 2 машин.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134259135.htm","2 часа назад",0,source="chotot",
  details={"contact":"chị Uyên (chính chủ)"}),

L(992,"ho-chi-minh","ak","Квартира",18000000,61,
  "2-спальная квартира (2 с/у) 61м² в ЖК New City, ул. Mai Chí Thọ, An Khánh (бывший Q2). Полная меблировка, бассейн, спортзал, кафе Highlands, магазин у дома.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134258399.htm","3 часа назад",0,source="chotot",
  details={"contact":"Trần Hải"}),

L(993,"ho-chi-minh","ak","Студия",9000000,35,
  "Студия 35м² с большими окнами у моста Sài Gòn, An Khánh (бывший Q2) — рядом Tropic Garden, Thảo Điền Pearl, станция метро, The Ascent. Полная меблировка, свободный график, без совместного проживания с хозяином.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/132964161.htm","вчера",1,source="chotot",
  details={"contact":"Nguyễn Quốc Thắng"}),

L(994,"ho-chi-minh","bth","Студия",8000000,40,
  "Студия с балконом ~30м² (официальная площадь карточки объявления — 40м²) на ул. Nguyễn Công Trứ 146, Bến Thành, Q1 — рядом Bitexco, TNR Tower, музей изобразительных искусств. Меблировка, общая стиральная машина на крыше, уборка 2 раза/нед. Электричество отдельно.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/133447083.htm","3 часа назад",0,source="chotot",
  details={"contact":"Hari Nguyễn","electricity":"4 000 ₫/кВт·ч","notice":"в тексте объявления цена указана дважды подряд (9 млн, затем 7 млн) — использована официальная цена карточки объявления, 8 млн"}),

L(995,"ho-chi-minh","bth","Квартира",12300000,40,
  "1-спальная квартира с балконом на ул. Cách Mạng Tháng 8, Bến Thành, Q1. Полная меблировка, вход по отпечатку пальца, отдельная зона стирки и сушки, камеры видеонаблюдения 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134253550.htm","6 часов назад",0,source="chotot",
  details={"contact":"Đinh Thành Đạt"}),

L(996,"ho-chi-minh","bth","Дом",24000000,24,
  "Дом целиком (1 этаж + 2 этажа + терраса, 2 спальни, 3 с/у, участок 3,2×7,5м) в переулке (заезд для 2 мотобайков) на ул. Phạm Ngũ Lão 265/, Bến Thành, Q1. Новый ремонт, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/132189144.htm","вчера",1,source="chotot",
  details={"contact":"Chi"}),

L(997,"ho-chi-minh","kh","Квартира",18000000,56,
  "2-спальная квартира (1 с/у) 56м² в ЖК River Gate, Khánh Hội, Q4 — вид на реку. Полная меблировка, свободна, готова к заселению сразу. Бассейн, спортзал, охрана 24/7, несколько минут до Q1.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133193043.htm","23 минуты назад",0,source="chotot",
  details={"contact":"Thúy An Huỳnh Thị"}),

L(998,"ho-chi-minh","kh","Студия",12000000,30,
  "Студия 30м² в ЖК Millennium, Khánh Hội, Q4. Полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/132875569.htm","29 минут назад",0,source="chotot",
  details={"contact":"Thúy An Huỳnh Thị (Danh Land)"}),

L(999,"ho-chi-minh","kh","Дом",13000000,63,
  "Дом (1 этаж + мезонин, 2 комнаты, 2 с/у, кухня, гостиная, 3,5×18м), новый ремонт, переулок 576 Đoàn Văn Bơ, Khánh Hội, Q4. Тихий переулок.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/133938667.htm","2 часа назад",0,source="chotot",
  details={"contact":"Huỳnh Thanh Sang"}),

L(1000,"ho-chi-minh","kh","Квартира",21000000,65,
  "2-спальная квартира (2 с/у) 65м² в ЖК Masteri Millennium (132 Bến Vân Đồn), Khánh Hội, Q4. Полная меблировка, бассейн и спортзал бесплатно.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133964659.htm","2 часа назад",0,source="chotot",
  details={"contact":"Căn hộ giá tốt Quận 4"}),

L(1001,"ho-chi-minh","kh","Дом",10000000,36,
  "Дом целиком (1 этаж + 2 этажа, 3×12м, 2 спальни, 2 с/у) в переулке у ул. Vĩnh Khánh, Khánh Hội, Q4 — рядом рынок, супермаркет, университеты Nguyễn Tất Thành и Luật, мост Khánh Hội.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134249817.htm","9 часов назад",0,source="chotot",
  details={"contact":"Đặng Trung Hậu"}),
L(1002,"da-nang","ah","Дом",26000000,100,
  "Дом целиком (3 спальни, 2 с/у) на ул. Tạ Mỹ Duật, квартал Khu Phố Hàn, An Hải. Чистый, подходит для семьи или группы.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134260965.htm","сегодня",0,source="chotot",
  details={"contact":"Nhựt Lê"}),

L(1003,"da-nang","ns","Квартира",7500000,45,
  "Дуплекс-квартира (1 спальня, 1 с/у) на ул. Lê Văn Hiến. Собственный сад на первом этаже (корпус B), своя стиральная машина, фильтр для воды, животные разрешены.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134260771.htm","сегодня",0,source="chotot",
  details={"contact":"Huy ho"}),

L(1004,"da-nang","ah","Дом",25000000,70,
  "Дом целиком (2 этажа, 3 спальни, 2 с/у), переулок Kiệt 02 Lâm Hoành (от Võ Văn Kiệt вглубь 50 м), P. Phước Mỹ, рядом пляж Mỹ Khê. Полная меблировка, принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134260398.htm","сегодня",0,source="chotot",
  details={"contact":"A Minh"}),

L(1005,"da-nang","ns","Дом",16000000,100,
  "Дом с садом (3 спальни, 3 с/у) фасадом на ул. Nguyễn Đình Chiểu, КДТ Nam Việt Á, P. Khuê Mỹ. Полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134260263.htm","сегодня",0,source="chotot",
  details={"contact":"A Phước"}),

L(1006,"da-nang","ns","Дом",25000000,100,
  "Дом-шопхаус (3 этажа, 4 спальни, 4 с/у) в комплексе Shophouse FPT. Задний двор, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134259736.htm","сегодня",0,source="chotot",
  details={"deposit":"2 месяца (оплата за 3)","contact":"Diep Nguyen"}),

L(1007,"da-nang","ah","Дом",18000000,65,
  "Дом целиком (3 этажа, ширина 6 м, 3 спальни, 2 с/у), Khu An Trung, рядом мост Trần Thị Lý и ЖК Monarchy. Первый этаж свободной планировки — подходит и под офис/шоурум (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/132401067.htm","сегодня",0,source="chotot",
  details={"contact":"Xuân Kỳ"}),

L(1008,"da-nang","ns","Квартира",12000000,50,
  "2-спальная квартира (1 с/у) на ул. Nguyễn Lữ, Khuê Mỹ, КДТ Nam Việt Á, рядом мост Tiên Sơn. Полная меблировка, балкон, своя стиральная машина.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134259223.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","contact":"HAVILAND HOUSE"}),

L(1009,"da-nang","hcg","Студия",11000000,40,
  "Студия (новое строительство, 100%) с балконом на ул. Hoa Sơn 7, рядом ТЦ Lotte, Hải Châu. Своя стиральная и сушильная машина. Доступны этажи 3 и 4, цена по объявлению 11-13 млн ₫ — указана нижняя граница.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134258765.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","notice":"диапазон цены по этажам 11-13 млн ₫ — использована нижняя граница (совпадает со структурным полем цены)","contact":"HAVILAND HOUSE"}),

L(1010,"da-nang","ns","Квартира",10000000,40,
  "1-спальная квартира (в тексте объявления указано 45 м², по данным площадки — 40 м²) с балконом, ул. An Thượng 17, рядом пляж. Этаж 2, можно въезжать сразу, еженедельная уборка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134258787.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","contact":"HAVILAND HOUSE"}),

L(1011,"da-nang","cl2","Дом",15000000,125,
  "Дом целиком (3 этажа, 4 спальни, 3 с/у) фасадом на ул. 48 Nguyễn Nhàn, напротив больницы Cẩm Lệ. Терраса, место для сушки белья.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134258860.htm","сегодня",0,source="chotot",
  details={"deposit":"6 месяцев","contact":"Thái Văn Bình"}),

L(1012,"da-nang","hcg","Студия",7400000,30,
  "Студия (комн. 301) на ул. Nguyễn Văn Linh 302, 5 минут пешком до аэропорта, рядом парк 29/3. Полная меблировка, лифт, бесплатная стирка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134258803.htm","сегодня",0,source="chotot",
  details={"contact":"Quyên Quyên"}),

L(1013,"da-nang","ns","Квартира",10500000,45,
  "1-спальная квартира с балконом на ул. Nguyễn Lữ, Khuê Mỹ. Своя стиральная машина, лифт, еженедельная уборка. Доступны этажи 3-5, цена по объявлению 10,5-12 млн ₫ — указана нижняя граница.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134258633.htm","сегодня",0,source="chotot",
  details={"notice":"диапазон цены по этажам 10,5-12 млн ₫ — использована нижняя граница","contact":"HAVILAND HOUSE ĐÀ NẴNG"}),

L(1014,"da-nang","ns","Студия",10000000,40,
  "Студия на ул. Tôn Thất Thiệp. Своя прачечная, водоочиститель, wifi. Этаж 2 (10 млн ₫, готова сейчас) или этаж 4 (11,5 млн ₫, скоро освободится) — в цене указан этаж 2.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134258586.htm","сегодня",0,source="chotot",
  details={"notice":"два варианта по этажам — использована цена этажа 2 (10 млн ₫)","contact":"HAVILAND HOUSE ĐÀ NẴNG"}),

L(1015,"da-nang","ns","Квартира",7000000,45,
  "1-спальная квартира на ул. Lê Quang Đạo 133, 5 минут пешком до моря. Балкон, своя стиральная машина, лифт, электронный замок. Цена варьируется по этажу (1/3/6) от 7 до 10,5 млн ₫ — указана нижняя граница.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134257990.htm","сегодня",0,source="chotot",
  details={"notice":"диапазон цены по этажам 7-10,5 млн ₫ — использована нижняя граница","contact":"1W05.Lê Phan Cẩm Ly"}),

L(1016,"da-nang","ns","Дом",40000000,100,
  "Дом целиком (4 этажа, 5 спален, 6 с/у, полезная площадь 400 м²) фасадом на ул. Khuê Mỹ Đông 7, рядом ул. Hồ Xuân Hương и пляж Mỹ Khê, район с высокой концентрацией иностранцев. Премиальная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134257545.htm","сегодня",0,source="chotot",
  details={"contact":"A Phong"}),

L(1017,"da-nang","ns","Дом",30000000,125,
  "Дом целиком (3 этажа, 6 спален, 6 с/у) на ул. Đoàn Khuê, КДТ Nam Việt Á. Двор для авто, меблирован, подходит и под офис/для проживания. Для вьетнамцев 30 млн ₫/мес, для иностранцев — 40 млн ₫/мес.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134257509.htm","сегодня",0,source="chotot",
  details={"notice":"цена для иностранных арендаторов выше (40 млн ₫) — указана базовая цена для местных (30 млн ₫)","contact":"Mr.Tú"}),

L(1018,"da-nang","hx","Дом",11000000,100,
  "Дом целиком (3 этажа, 3 спальни, 3 с/у) на ул. Phù Đổng, Hòa Xuân. Полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134257231.htm","сегодня",0,source="chotot",
  details={"contact":"Thuỷ DT"}),

L(1019,"da-nang","ns","Дом",35000000,70,
  "Дом целиком (3 этажа, 4 спальни, 3 с/у), квартал An Thượng, рядом множество удобств. Без мебели, только кондиционеры — подходит и для проживания, и под офис (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134257191.htm","сегодня",0,source="chotot",
  details={"contact":"Mr.Tú"}),

L(1020,"da-nang","ns","Дом",17000000,100,
  "Дом целиком (3 этажа, 4 спальни) фасадом на ул. Tùng Thiện Vương, КДТ Nam Việt Á. Приоритет долгосрочной аренде.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134257141.htm","сегодня",0,source="chotot",
  details={"contact":"Mr.Thắng"}),

L(1021,"da-nang","cl2","Дом",23000000,120,
  "Дом целиком (3 этажа, 4 спальни, 4 с/у) фасадом на ул. Trịnh Đình Thảo, Khuê Trung, рядом ул. Nguyễn Hữu Thọ. Просторный двор для авто, подходит и под офис/учебный центр (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134256971.htm","сегодня",0,source="chotot",
  details={"contact":"BÌNH CAPITAL"}),

L(1022,"da-nang","tk","Квартира",10000000,45,
  "2-спальная квартира (1 с/у) на ул. Phan Thanh, рядом университет Duy Tân. Полная меблировка, лифт, принимают иностранцев, животные не разрешены. Контракт от 6 месяцев.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134256882.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц","contact":"Minh Kiệt Haviland"}),

L(1023,"da-nang","ns","Студия",5500000,20,
  "Компактная квартира (20 м²) с балконом на ул. An Thượng 37, рядом университет экономики, рынок Bắc Mỹ An, пляж Mỹ Khê. ТВ, холодильник, кондиционер, кухонная утварь.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134256438.htm","сегодня",0,source="chotot",
  details={"contact":"Hòa"}),

L(1024,"da-nang","ns","Квартира",6300000,40,
  "Квартира (40 м²) с балконом на ул. Chế Lan Viên 08, рядом университет экономики, рынок Bắc Mỹ An, пляж Mỹ Khê. Полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134256378.htm","сегодня",0,source="chotot",
  details={"contact":"Hòa"}),

L(1025,"da-nang","hk","Студия",8500000,40,
  "Студия с просторным балконом на ул. Hòa Phú 30, Hòa Khánh. Своя стиральная и сушильная машина, свободна сейчас.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134256189.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Thanh Kiệt"}),

L(1026,"da-nang","hx","Дом",25000000,100,
  "Дом целиком (3 этажа, сквозной, новое строительство) на ул. 10м5 Lê Quảng Chí, Hòa Xuân. Подходит и для проживания, и под бизнес/офис (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134256080.htm","сегодня",0,source="chotot",
  details={"contact":"mr AN"}),

L(1027,"da-nang","ah","Дом",20000000,66,
  "Дом новой постройки (2 этажа, 2 спальни, 3 с/у) на ул. Tạ Mỹ Duật, рядом пляж Mỹ Khê. 3 кондиционера, стиралка, ТВ, холодильник, водонагреватель. Первый этаж уже оборудован под кафе (барная стойка, мебель) — подходит и для совмещённого проживания с бизнесом.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134255960.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Anh Tuyền"}),

L(1028,"da-nang","hx","Дом",12000000,100,
  "Дом целиком (2 этажа, 3 спальни) на ул. Hoàng Hiệp, Hòa Xuân. Двор для авто, базовая меблировка, подходит и под офис (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134255879.htm","сегодня",0,source="chotot",
  details={"contact":"Quyên Lê"}),

L(1029,"da-nang","st","Дом",130000000,300,
  "Вилла премиум-класса (3 этажа, 6 спален, у каждой свой с/у) рядом мостом Thuận Phước, ул. Phan Bá Vành. Бассейн, лифт, karaoke, сауна, терраса для BBQ, элитный закрытый квартал.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134255725.htm","сегодня",0,source="chotot",
  details={"contact":"Ruby Ho (Toan Huy Hoang Realty)"}),

L(1030,"da-nang","hx","Дом",15000000,100,
  "Дом целиком (3 этажа, немного смещённой планировки, 3 спальни, 3 с/у) фасадом на ул. Hoàng Đình Ái, рядом рынок Hòa Xuân. Комната для алтаря, место для сушки белья, двор для авто, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134255706.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Dự"}),

L(1031,"da-nang","ah","Дом",70000000,250,
  "Вилла в комплексе Euro Village 1 (3 этажа, 4 спальни, у каждой свой с/у). Премиальная меблировка, много зелени, охраняемый квартал.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134255692.htm","сегодня",0,source="chotot",
  details={"contact":"Ruby Ho (Toan Huy Hoang Realty)"}),

L(1032,"da-nang","ah","Квартира",50000000,94,
  "1-спальная квартира 94 м² в комплексе Wyndham Soleil Ánh Dương, ~50 м от пляжа Phạm Văn Đồng. Вид на море и гору Sơn Trà, премиальная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134255320.htm","сегодня",0,source="chotot",
  details={"contact":"Chanh Phạm"}),

L(1033,"da-nang","ah","Студия",6500000,35,
  "Студия/1-спальная на ул. Trần Hưng Đạo, P. An Hải Tây, рядом мост Dragon Bridge, ночной рынок Sơn Trà и набережная реки Хан. Полная меблировка, лифт, охраняемая парковка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134255065.htm","сегодня",0,source="chotot",
  details={"contact":"Apartment Đà Nẵng"}),

L(1034,"da-nang","ah","Дом",26000000,76,
  "Дом целиком (3 этажа, 3 спальни, 2 с/у) на ул. Tạ Mỹ Duật, An Hải Bắc, рядом Phạm Văn Đồng. Полная меблировка, рядом пляж.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134255017.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Quân Land"}),

L(1035,"da-nang","ah","Дом",23000000,150,
  "Дом целиком (4 спальни, 3 с/у) в квартале Phúc Lộc Viên, ул. Ngô Quyền.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134254990.htm","сегодня",0,source="chotot",
  details={"contact":"Nhựt Lê"}),

L(1036,"da-nang","st","Квартира",24000000,50,
  "2-спальная квартира на высоком этаже комплекса Golden Bay, вид на реку. Премиальная меблировка, свободна сейчас.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134254924.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц (оплата за 3)","contact":"Nguyễn Công Chinh"}),

L(1037,"da-nang","ah","Дом",30000000,90,
  "Дом в переулке для авто (3 этажа, 5 спален, 3 с/у, полезная площадь 270 м²) на ул. Nguyễn Văn Thoại, рядом пляж Mỹ Khê. Чистый; в объявлении также предлагается под спа/нейл-салон/хостел (вторично).",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134254920.htm","сегодня",0,source="chotot",
  details={"contact":"Hải (NCC)"}),

L(1038,"da-nang","ns","Дом",25000000,300,
  "Дом с большим садом (2 спальни, 2 с/у) на ул. Bình Kỳ, Hòa Quý, рядом мост Khuê Đông. Пруд с карпами кои, тихий район.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134254862.htm","сегодня",0,source="chotot",
  details={"contact":"Hải"}),

L(1039,"da-nang","st","Квартира",14000000,70,
  "2-спальная квартира (2 с/у) на ул. Mân Quang 9, рядом супермаркет Coopmart Sơn Trà. Бассейн на 1 этаже, терраса с мангалом, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134254820.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Diêm"}),

L(1040,"da-nang","ns","Квартира",20000000,50,
  "2-спальная квартира на ул. Khuê Mỹ Đông 15 (в объявлении также фигурирует Khuê Mỹ Đông 14). Полная меблировка, животные разрешены.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134254543.htm","сегодня",0,source="chotot",
  details={"contact":"Huy ho"}),

L(1041,"da-nang","lc","Квартира",5500000,56,
  "2-спальная квартира (2 с/у) в ЖК The Ori Garden, Hòa Hiệp Nam. Район по ward_name_v3 — «Hải Vân» (не входит в список районов проекта явно, нанесена на ближайший — Liên Chiểu, по прецеденту L907). Цена не включает сервис-сбор. В том же объявлении также предлагается 3-спальная квартира за 7,5 млн ₫ — не добавлена отдельно (нет данных о площади).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/133562284.htm","сегодня",0,source="chotot",
  details={"deposit":"1 месяц (оплата за 3)","contact":"Hồ sỹ ánh"}),

L(1042,"da-nang","hcg","Квартира",14000000,72,
  "2-спальная квартира (2 с/у) 72 м² на ул. Nguyễn Hữu Thọ, рядом центр и аэропорт. Полная меблировка, животные разрешены, свободна сейчас.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134253638.htm","сегодня",0,source="chotot",
  details={"contact":"Kiều Oanh"}),

L(1043,"da-nang","ns","Квартира",32000000,70,
  "2-спальная квартира (2 с/у) 70 м² в ЖК Panoma, ул. Trần Thị Lý, рядом мост Dragon Bridge и пляж Mỹ Khê. Бассейн, спортзал, ресепшен, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134253562.htm","сегодня",0,source="chotot",
  details={"notice":"структурное поле цены и заголовок объявления указывают 32 млн ₫, но в тексте описания фигурирует 35 млн ₫ (похоже на кусок шаблона от другого юнита) — использована цена из заголовка/структурного поля","contact":"Kiều Oanh"}),

L(1044,"da-nang","ns","Квартира",9000000,45,
  "Квартира на ул. Lê Văn Hưu, Ngũ Hành Sơn. Своя стиральная машина, wifi, лифт, замок по отпечатку пальца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134253015.htm","сегодня",0,source="chotot",
  details={"contact":"Khánh Linh"}),

L(1045,"da-nang","ns","Квартира",9500000,60,
  "2-спальная квартира (2 с/у) 60 м² на ул. Hói Kiểng 27, вид на реку. Полная меблировка, кондиционер, холодильник, свой паркинг для авто — подходит для 3-4 человек.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134246817.htm","сегодня",0,source="chotot",
  details={"contact":"Trường Giang"}),
L(1046,"ho-chi-minh","tm","Дом",8000000,24,
  "Дом целиком в переулке 167, ул. Phạm Hữu Lầu, Tân Mỹ, Q7 — 50 м до асфальтированной дороги, рядом Phú Mỹ Hưng. Участок 3×8 м, 1 этаж + 1 этаж, балкон 1,8 м, 2 спальни, 2 с/у, гостиная, кухня. Новый дом, никто ещё не жил.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134277555.htm","1 час назад",0,source="chotot",
  details={"alsoOn":[{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134289080.htm"}],"deposit":"1 месяц","contact":"Lý Thuỷ Mộc (chính chủ)"}),

L(1047,"ho-chi-minh","tm","Квартира",9500000,75,
  "2-спальная квартира (2 с/у) 75м² в ЖК Sunshine Sky City, рядом Phú Mỹ Hưng. Базовая меблировка. Бесплатное управление первые 2 года. Бассейн, спортзал, охрана 24/7, паркинг.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134277538.htm","1 час назад",0,source="chotot",
  details={"contact":"Trịnh Đình Đức Anh"}),

L(1048,"ho-chi-minh","tm","Дом",115000000,275,
  "Отдельностоящая вилла-дуплекс Nam Viên, Phú Mỹ Hưng — участок 17,2×16м (275,2м²), 1 этаж + 2 этажа, 4 спальни, 4 с/у, комната для сауны, свой сад с прудом кои, юго-восточная ориентация. Премиальная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134276783.htm","2 часа назад",0,source="chotot",
  details={"notice":"в объявлении отмечено «есть торг»","contact":"ThienhuongLand"}),

L(1049,"ho-chi-minh","tm","Квартира",29000000,77,
  "2-спальная квартира (2 с/у) 77м² в ЖК The Ascentia, Phú Mỹ Hưng — вид на бассейн из окна, гостиная смотрит на тихие виллы, кровать в мастер-спальне 2×2м. Полная современная меблировка. Рядом Crescent Mall, международная школа SSIS, госпиталь FV.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134275646.htm","3 часа назад",0,source="chotot",
  details={"contact":"Hoàng Trúc Loan"}),

L(1050,"ho-chi-minh","tm","Квартира",13000000,75,
  "2-спальная квартира 75м² в ЖК Sunshine City (корпуса S1-S4, скоро сдача), адрес 23 Phú Thuận, Phú Mỹ Hưng, 10 минут пешком до Crescent Mall. Базовая меблировка (шторы, кондиционер, водонагреватель).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133558168.htm","3 часа назад",0,source="chotot",
  details={"notice":"указана нижняя граница диапазона 13-14 млн ₫ для базовой меблировки этой планировки; агент также предлагает другие юниты в этом же комплексе","contact":"Thái Học Jimmy"}),

L(1051,"ho-chi-minh","tm","Дом",30000000,80,
  "Дом целиком (5 спален), 300 м от рынка Tân Mỹ, старый центр Q7. Участок 4×20м (80м²), 3 этажа, полная меблировка, западная ориентация.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134273497.htm","4 часа назад",0,source="chotot",
  details={"duplicateOf":873,"contact":"phượng"}),

L(1052,"ho-chi-minh","tm","Дом",17000000,64,
  "Дом целиком в переулке 1422, ул. Huỳnh Tấn Phát, Q7 — участок 4×16м (64м²), 1 этаж + 2 этажа + терраса, 3 спальни, 3 с/у. Полная качественная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134271286.htm","6 часов назад",0,source="chotot",
  details={"contact":"Dương Văn Bảo"}),

L(1053,"ho-chi-minh","tm","Дом",6500000,80,
  "Дом целиком (>80м²) с видом на реку, ул. Phạm Hữu Lầu, Tân Mỹ, Q7 — 2 отдельные спальни (деревянный пол), просторные гостиная и коридор, большой двор перед домом, утреннее солнце (восточная ориентация). Кондиционер, кухня со встроенной мойкой, водонагреватель. Рядом Phú Mỹ Hưng, RMIT, Tôn Đức Thắng. Электричество 4000₫/кВт·ч, вода 100 000₫/чел., wifi+уборка+управление 150 000₫, вывоз мусора 85 000₫. Договор от 12 месяцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/132504178.htm","7 часов назад",0,source="chotot",
  details={"electricity":"4 000 ₫/кВт·ч","other_fees":"вода 100 000₫/чел., wifi+уборка+управление 150 000₫, мусор 85 000₫","contact":"Nhân Võ (BĐS PMH)"}),

L(1054,"ho-chi-minh","tm","Дом",21000000,80,
  "Угловой дом (2 фасада на переулок), переулок 1422, ул. Huỳnh Tấn Phát, Q7 — новое строительство 100%. 1 этаж + 2 этажа + терраса, 3 спальни, 3 с/у. Мебель в подарок: диван, обеденный стол, кондиционеры, кровати, шкафы, трюмо.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134269836.htm","7 часов назад",0,source="chotot",
  details={"notice":"расхождение площади: в тексте объявления указаны размеры 4×16м=64м², в структурном поле площадки — 80м² (использовано структурное поле)","contact":"Mai Tố (BĐS Nhà Bè Q7)"}),

L(1055,"ho-chi-minh","tm","Дом",21000000,64,
  "Дом целиком в переулке 1422, ул. Huỳnh Tấn Phát, Q7 — участок 4×16м (64м²), 1 этаж + 2 этажа + терраса, 3 спальни, 3 с/у. Полная качественная меблировка, готов к заезду.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134269632.htm","7 часов назад",0,source="chotot",
  details={"contact":"Thanh Phan","alsoOn":[{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134261616.htm"}]}),

L(1056,"ho-chi-minh","tm","Дом",13000000,72,
  "Дом целиком (адрес 1156) в переулке, ул. Huỳnh Tấn Phát, Q7 — участок 4×18м (72м²), 1 этаж + 2 этажа + терраса, 5 спален, 3 с/у, гостиная, кухня, место для авто.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133973942.htm","7 часов назад",0,source="chotot",
  details={"contact":"Gia Gia"}),

L(1057,"ho-chi-minh","tm","Квартира",15000000,90,
  "3-спальная квартира (2 с/у) 90м² в ЖК River Panorama (89 Hoàng Quốc Việt), Q7 — балкон + лоджия. Базовая меблировка: шторы, кондиционер, шкаф, встроенная электроплита, вытяжка, сантехника. Свободна, можно заезжать сразу. Бассейн-инфинити на крыше, сауна, зона BBQ, детская площадка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/130364871.htm","3 дня назад",3,source="chotot",
  details={"contact":"Huy"}),

L(1058,"ho-chi-minh","th","Студия",6200000,40,
  "Студия с отдельной кухней (дуплекс-планировка), балкон, ул. D4, Tân Hưng, Q7 — рядом Lotte Mart, университеты Tôn Đức Thắng и RMIT. Своя стиральная машина, полная меблировка, готова к заезду. Удобно добираться до Q1 и Q4.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134279104.htm","6 минут назад",0,source="chotot",
  details={"contact":"Trần Văn"}),

L(1059,"ho-chi-minh","th","Квартира",16000000,72,
  "2-спальная квартира (2 с/у) 72м² в ЖК Florita, ул. D1, Tân Hưng, у моста Him Lam, Q7 — высокий этаж, хороший обзор. Премиальная меблировка, бассейн, спортзал, кафе. Цена с торгом.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134278766.htm","26 минут назад",0,source="chotot",
  details={"contact":"Nguyễn Trường"}),

L(1060,"ho-chi-minh","th","Комната",5500000,20,
  "Комната на 3 этаже (из двух сдающихся, можно снять обе со скидкой), 20м² — кровать с матрасом, стол со стульями, кухонный уголок, холодильник, кондиционер, просторный балкон. Санузел и стиральная машина общие. Цена указана за одну комнату.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134278249.htm","56 минут назад",0,source="chotot",
  details={"contact":"Nguyễn Khang"}),

L(1061,"ho-chi-minh","th","Дом",10000000,50,
  "Дом целиком, 1 этаж + 2 этажа, 3 спальни, 50м² — тихий безопасный квартал рядом с ЖК Him Lam, 5 минут до Lotte Mart, Q1, Q5, Q8.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134276917.htm","2 часа назад",0,source="chotot",
  details={"contact":"Ngoc Truong"}),

L(1062,"ho-chi-minh","th","Студия",5200000,25,
  "Студия рядом с университетом UFM, ул. Lâm Văn Bền, Q7 — современный дизайн, охраняемое здание, паркинг в цоколе, лифт. Полная качественная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134276578.htm","2 часа назад",0,source="chotot",
  details={"contact":"Huy Lê"}),

L(1063,"ho-chi-minh","th","Квартира",15000000,80,
  "2-спальная квартира (2 с/у) 80м² в ЖК Cosmo City (99 Nguyễn Thị Thập), Tân Hưng, Q7 — новая качественная меблировка, бассейн, спортзал, ТЦ в комплексе. Прямая аренда от хозяина, с торгом.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134275110.htm","3 часа назад",0,source="chotot",
  details={"contact":"Lê Minh (BĐS)"}),

L(1064,"ho-chi-minh","th","Дом",9000000,36,
  "Дом целиком в переулке 1041, ул. Trần Xuân Soạn, рядом Him Lam, Q7 — участок 3,6×10м (36м²), 1 этаж + 1 этаж, 2 спальни, 2 с/у, гостиная, кухня.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134274782.htm","3 часа назад",0,source="chotot",
  details={"contact":"LHP"}),

L(1065,"ho-chi-minh","th","Студия",5600000,35,
  "Студия (căn hộ dịch vụ) на ул. Lâm Văn Bền, Q7 — рядом университеты TDTU, RMIT, UFM, большая парковка, новое здание с качественной меблировкой, разрешены животные, охрана и лифт круглосуточно.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/127275867.htm","4 часа назад",0,source="chotot",
  details={"notice":"в заголовке указано «от 5 млн» — использовано структурное поле цены 5,6 млн","contact":"hà"}),

L(1066,"ho-chi-minh","th","Дом",25000000,72,
  "Дом целиком, 3 этажа, Tân Hưng, Q7, фасад на улицу — участок 4×18м (72м²), 1 этаж + 3 этажа, 4 спальни, 3 с/у, гостиная, кухня, место для авто.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134273371.htm","4 часа назад",0,source="chotot",
  details={"duplicateOf":820,"contact":"Nhà Thuê Nguyên Căn Quận 7"}),

L(1067,"ho-chi-minh","th","Дом",15000000,110,
  "Дом целиком фасадом на улицу, ул. Lâm Văn Bền, Q7 — участок 5×22м (110м²), 1 сквозной этаж, 2 спальни, 2 с/у, гостиная, кухня, место для авто.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134270769.htm","6 часов назад",0,source="chotot",
  details={"contact":"LHP","alsoOn":[{"source":"chotot","url":"https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134296828.htm"}]}),

L(1068,"ho-chi-minh","th","Дом",7000000,36,
  "Дом целиком в центре Q7, участок 4×9м (36м²), 1 этаж + 1 этаж, 2 спальни, 2 с/у — безопасный тихий переулок, подходит для семьи на долгий срок.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134269282.htm","7 часов назад",0,source="chotot",
  details={"contact":"Phạm văn Ngữ"}),

L(1069,"ho-chi-minh","th","Дом",14000000,120,
  "Дом фасадом на улицу, ул. Lâm Văn Bền, Q7 — участок 4×30м (расширяется вглубь до 5м, 120м²), есть антресоль.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134268815.htm","8 часов назад",0,source="chotot",
  details={"notice":"в объявлении отмечено «подходит для проживания в сочетании с небольшим бизнесом»","contact":"Văn Kiên (Nhà Phố Quận 7)"}),

L(1070,"ho-chi-minh","th","Дом",8000000,60,
  "Дом целиком рядом с Him Lam и Lotte Mart, Q7 — участок 4,3×14м (60м²), 1 этаж + 1 этаж, 2 спальни, 1 с/у. Чистый, можно заезжать сразу.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133858941.htm","10 часов назад",0,source="chotot",
  details={"contact":"Phạm văn Ngữ"}),

L(1071,"ho-chi-minh","th","Студия",6500000,35,
  "Студия с балконом, ул. Số 79, Tân Hưng, Q7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134247009.htm","вчера",1,source="chotot",
  details={"notice":"акционная цена открытия для первых 5 арендаторов, дальше цена вырастет до обычной","contact":"Li Pao"}),

L(1072,"ho-chi-minh","th","Квартира",148000000,300,
  "Пентхаус 300м² в ЖК Sky Garden 2, мащ Nguyễn Văn Linh, Q7 — 9 спален (2 зоны гостиной, большая терраса), пространство на 3 уровнях, вид на бассейн, парк комплекса и Landmark 81. Полностью новая премиальная меблировка. Цена с учётом налога.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134240166.htm","вчера",1,source="chotot",
  details={"notice":"срочная сдача (в заголовке «cho thuê gấp»)","contact":"Thu Dinh"}),

L(1073,"ho-chi-minh","th","Дом",37000000,128,
  "Дом целиком, КДТ Tân Quy Đông, ул. 46, Tân Hưng, Q7 — фасад 7м, свой отдельный гараж на авто. Участок 7×18м (128м²), 1 этаж + 2 этажа, 5 спален, 3 с/у, есть небольшая ниша-комната внутри большой спальни (удобно для семьи с детьми). Южная ориентация.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134226759.htm","2 дня назад",2,source="chotot",
  details={"notice":"хозяин использует верхний этаж для разведения ласточек на гнёзда (сбор урожая раз в 3-4 месяца), заверяет, что это не мешает жильцам","contact":"Thanh Villa"}),

L(1074,"ho-chi-minh","th","Студия",6500000,30,
  "Студия/мини-квартира 30м² рядом с Lotte Mart, RMIT, TDTU, Phú Mỹ Hưng, Q7 — премиальная меблировка как на фото, просторный балкон, вход по отпечатку пальца, пожарная безопасность.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134221622.htm","2 дня назад",2,source="chotot",
  details={"notice":"сдача только до конца сентября 2026 года (краткосрочный договор)","contact":"Nhi Mira"}),

L(1075,"ho-chi-minh","th","Дом",25000000,72,
  "Дом фасадом на улицу, ул. Tân Kiểng, Q7 — участок 4×18м (72м²), 1 этаж + 3 этажа, 4 спальни, 3 с/у, гостиная, кухня, место для авто.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134221426.htm","2 дня назад",2,source="chotot",
  details={"duplicateOf":820,"contact":"LHP"}),

L(1076,"ho-chi-minh","ak","Квартира",22000000,83,
  "3-спальная квартира (2 с/у) 83м² в ЖК New City, ул. Mai Chí Thọ, An Khánh — полная меблировка, бассейн, спортзал, кафе Highlands, магазин у дома.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134278700.htm","31 минуту назад",0,source="chotot",
  details={"contact":"Trần Hải"}),

L(1077,"ho-chi-minh","ak","Квартира",30000000,50,
  "1-спальная квартира (1 с/у) 50м² в ЖК The Galleria Residences, ул. Mai Chí Thọ — 3 минуты до центра Q1. Полная меблировка. Бассейн с минеральной водой, спортзал, йога, сауна.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134277828.htm","1 час назад",0,source="chotot",
  details={"notice":"указана нижняя граница диапазона цены 30-35 млн ₫","contact":"Hạnh"}),

L(1078,"ho-chi-minh","ak","Квартира",9800000,37,
  "1-спальная квартира (новое здание) с балконом, ул. Quốc Hương, рядом станция метро Thảo Điền — полная премиальная меблировка, тихий охраняемый квартал, паркинг в цоколе, лифт.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/131519696.htm","2 часа назад",0,source="chotot",
  details={"contact":"Phan Trung Thực"}),

L(1079,"ho-chi-minh","ak","Студия",9000000,40,
  "Студия с отдельной кухней и балконом, ул. Quốc Hương / Xuân Thủy / Làng Báo Chí, рядом Nguyễn Văn Hưởng и станция метро, Thảo Điền — премиальная меблировка, разрешены животные, из коммунальных платится только свет/вода. Лифт, просторный паркинг в цоколе.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/132486238.htm","2 часа назад",0,source="chotot",
  details={"contact":"Thuỳ Dương"}),

L(1080,"ho-chi-minh","ak","Квартира",25000000,88,
  "2-спальная квартира (2 с/у) 88м² в ЖК Sadora, Khu đô thị Sala (Thủ Thiêm) — вид на Q1, меблировка на выбор (пустая или полная). Супермаркет Emart, мини-маркеты GS25/7-Eleven, бассейн, спортзал, детская площадка, зона BBQ, сауна.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134276778.htm","2 часа назад",0,source="chotot",
  details={"notice":"указана нижняя граница диапазона цены 25-28 млн ₫ (в зависимости от меблировки)","contact":"Hạnh"}),

L(1081,"ho-chi-minh","ak","Дом",221000000,1200,
  "Вилла на берегу реки Сайгон, фасад на ул. Nguyễn Văn Hưởng, Thảo Điền — участок 1200м² (801м² жилой земли), фасад по улице 19,5м, до реки 61,5м. 1 этаж + 2 этажа, много просторных комнат, 4 спальни.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134276017.htm","3 часа назад",0,source="chotot",
  details={"notice":"структурная цена соответствует ставке для проживания (8500$/мес ≈ 221 млн ₫); ставка для аренды под бизнес выше — 9000$/мес","contact":"ThienhuongLand"}),

L(1082,"ho-chi-minh","ak","Дом",19000000,80,
  "Дом целиком, 1 этаж + 2 этажа, 4 спальни, 3 с/у, 80м², An Khánh (бывший Q2), ул. Số 2, рядом Trần Não. Цена с торгом, залог — оплата за 3 месяца сразу.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/121346163.htm","4 часа назад",0,source="chotot",
  details={"contact":"Khánh Duyên"}),

L(1083,"ho-chi-minh","bth","Дом",8500000,22,
  "Отдельный дом в переулке, ул. Nguyễn Du, Bến Thành, Q1, в паре шагов от парка Tao Đàn — суммарная полезная площадь по объявлению 44м² на 2 этажах (в структурном поле площадки указано 22м²), 1 этаж + 1 этаж, вытяжка, 3 кондиционера, стиральная машина, ТВ. Рядом школы, больницы, рынок.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/132506096.htm","35 минут назад",0,source="chotot",
  details={"notice":"площадь по тексту объявления 44м² (2 этажа), в структурном поле площадки — 22м²","contact":"ms Tien"}),

L(1084,"ho-chi-minh","kh","Квартира",29000000,107,
  "3-спальная квартира (2 с/у) 107м² в ЖК Millennium (132 Bến Vân Đồn), Khánh Hội, Q4 — полная меблировка, красивый вид. Бассейн, спортзал, мини-маркет, кафе. Рядом мост Calmette, 3-5 минут до Q1/2/3/5/6/7/8.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133931229.htm","1 час назад",0,source="chotot",
  details={"contact":"Tú Hằng (Q4)"}),

L(1085,"ho-chi-minh","kh","Квартира",33000000,107,
  "Угловая 3-спальная квартира (2 с/у) 107м² в ЖК Millennium (132 Bến Vân Đồn), Khánh Hội, Q4 — вид на Bitexco и городской skyline, много света и воздуха. Полная премиальная меблировка. Бассейн, спортзал, зона BBQ, кафе, ресепшен и охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133741969.htm","1 час назад",0,source="chotot",
  details={"contact":"Tú Hằng (Q4)"}),

L(1086,"ho-chi-minh","kh","Квартира",22000000,75,
  "2-спальная квартира (2 с/у) 75м² в ЖК Millennium (132 Bến Vân Đồn), Khánh Hội, Q4 — вид на канал Bến Vân Đồn, полная премиальная меблировка, готова к заезду. Бассейн, спортзал, мини-маркет, ресепшен и охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133735223.htm","1 час назад",0,source="chotot",
  details={"notice":"в объявлении предлагается и в аренду, и на продажу — указана ставка аренды","contact":"Tú Hằng (Q4)"}),

L(1087,"ho-chi-minh","kh","Квартира",18000000,65,
  "2-спальная квартира (2 с/у) 65м² в ЖК Masteri Millennium, Khánh Hội, Q4 — базовая меблировка (кухня, шторы, кондиционер), электричество/вода по счётчику государственного тарифа. Бассейн и спортзал бесплатно.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133683618.htm","1 час назад",0,source="chotot",
  details={"contact":"Căn hộ giá tốt Quận 4"}),

L(1088,"ho-chi-minh","kh","Квартира",10500000,57,
  "1-спальная квартира 57м² в доме H3, 384 Hoàng Diệu, Khánh Hội, Q4 — полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/133973110.htm","1 час назад",0,source="chotot",
  details={"contact":"Căn hộ giá tốt Quận 4"}),

L(1089,"ho-chi-minh","kh","Дом",8000000,24,
  "Дом целиком в переулке Đoàn Văn Bơ (538), Khánh Hội, Q4 — фасад переулка 3м, по тексту объявления 40м² (2 спальни, 2 с/у), в структурном поле площадки — 24м². Новое строительство, чисто, юго-восточная ориентация. Приоритет долгосрочной аренде, напрямую от хозяйки, без посредников.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134263711.htm","18 часов назад",0,source="chotot",
  details={"notice":"площадь по тексту объявления 40м², в структурном поле площадки — 24м²","contact":"Oanh"}),

L(1090,"ho-chi-minh","kh","Студия",12000000,30,
  "Студия-officetel с отдельной спальной нишей, вид на Bitexco, в ЖК Millennium, Khánh Hội, Q4 — 30м², полная меблировка. Бассейн, спортзал, мини-маркет, кафе.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134256731.htm","вчера",1,source="chotot",
  details={"contact":"Hương Dung (Danh Land)"}),
L(1091,"ho-chi-minh","th","Квартира",7000000,45,
  "1-спальная квартира с балконом в жилом комплексе Him Lam, ул. Hoàng Trọng Mậu. Полная меблировка, рядом ĐH Tôn Đức Thắng, Lotte Mart, RMIT, Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134212202.htm","3 дня назад",3,source="chotot",
  details={"contact":"Nguyễn Hữu Quyết"}),

L(1092,"ho-chi-minh","th","Студия",7300000,30,
  "Студия с балконом на ул. Số 7. Свободный график, вход по отпечатку пальца, крупный чистый жилой комплекс, своя стирально-сушильная машина, рядом ĐH Tôn Đức Thắng, UFM, RMIT.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134279201.htm","сегодня",0,source="chotot",
  details={"contact":"Hang Pham"}),

L(1093,"ho-chi-minh","th","Дом",8500000,66,
  "Дом целиком (2 спальни) на ул. Số 25 (бывший район Tân Quy), рядом рынок и парк.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134245968.htm","1 день назад",1,source="chotot",
  details={"contact":"Thu Anh"}),

L(1094,"ho-chi-minh","ak","Студия",5500000,35,
  "Студия с отдельной кухонной зоной на ул. Trần Não, An Khánh. Полная меблировка (кондиционер, холодильник, стиралка, кровать), несколько минут до Thảo Điền, Sala, Thủ Thiêm.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133969162.htm","сегодня",0,source="chotot",
  details={"contact":"Phương An"}),

L(1095,"ho-chi-minh","ak","Квартира",11000000,50,
  "1-спальная квартира на ул. Nguyễn Bá Huân, Thảo Điền. Премиальная меблировка, рядом Vincom Mega Mall, станция метро An Phú, охрана 24/7, лифт, подземный паркинг.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/133971394.htm","сегодня",0,source="chotot",
  details={"contact":"Phương An"}),
L(1096,"da-nang","ah","Дом",27000000,70,
  "Дом целиком на ул. Thạch Lam (Phước Mỹ), 2 спальни/2 с/у, гостиная и оборудованная кухня. Полная меблировка высокого класса, заезд сразу.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134279517.htm","сегодня",0,source="chotot",
  details={"contact":"Thuê Nhà Đẹp Căn Hộ Cao Cấp Đà Nẵng"}),

L(1097,"da-nang","ns","Квартира",16000000,40,
  "Квартира B2-8-8 в ЖК Sun Cosmo (Andy Apartment by Haviland) на ул. Trần Thị Lý, Mỹ An — 1 спальня, полная меблировка люкс, своя стирально-сушильная машина, балкон.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134279511.htm","сегодня",0,source="chotot",
  details={"notice":"без животных и электробайков","contact":"Thanh Trung Haviland"}),

L(1098,"da-nang","ah","Дом",35000000,90,
  "Новый дом в переулке Phạm Cự Lượng рядом с пляжем Mỹ Khê — 4 спальни/5 с/у, гостиная, кухня. Мебель новая, дом на этапе сдачи. Принимают иностранцев (специалистов, семьи на долгий срок).",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134279487.htm","сегодня",0,source="chotot",
  details={"notice":"дом в стадии завершения отделки","contact":"Thuê Nhà Đẹp Căn Hộ Cao Cấp Đà Nẵng"}),

L(1099,"da-nang","ah","Студия",10000000,35,
  "Студия на ул. Cao Bá Quát в паре шагов от моста Rồng — 35м². Лифт, wi-fi, еженедельная уборка, отдельная зона сушки белья, своя парковка для байков.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134279347.htm","сегодня",0,source="chotot",
  details={"contact":"HAVILAND HOUSE ĐÀ NẴNG"}),

L(1100,"da-nang","ak","Квартира",15000000,250,
  "Пентхаус с садом на ул. Lê Thạch — 250м², 2 спальни/2 с/у, очень просторная гостиная, современная кухня, большой балкон с зеленью. Полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134279295.htm","сегодня",0,source="chotot",
  details={"notice":"для иностранцев хозяин указывает цену 17 млн ₫/мес вместо 15 млн","contact":"Thuê Nhà Đẹp Căn Hộ Cao Cấp Đà Nẵng"}),

L(1101,"da-nang","tk","Дом",15000000,50,
  "Новый двухэтажный дом в переулке Hùng Vương в центре города — 3 спальни, полная меблировка, заезд сразу. Переулок широкий и чистый (проезд для байков). Принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134279055.htm","сегодня",0,source="chotot",
  details={"contact":"Dĩnh Dĩnh"}),

L(1102,"da-nang","ah","Дом",35000000,100,
  "Трёхэтажный дом в закрытом квартале Euro Village 1 у моста Trần Thị Lý — 4 спальни/4 с/у, полная меблировка, охраняемая территория. Принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134278997.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Thị Duyên"}),

L(1103,"da-nang","hcg","Квартира",19500000,45,
  "Квартира с 1 спальней на ул. Trưng Nữ Vương — 45м², полная меблировка, своя зона стирки-сушки в квартире. Лифт, еженедельная уборка, просторная общая терраса.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134278754.htm","сегодня",0,source="chotot",
  details={"contact":"HAVILAND HOUSE ĐÀ NẴNG"}),

L(1104,"da-nang","hk","Дом",25000000,64,
  "Трёхэтажный дом в переулке Trần Đình Tri (Hòa Minh) — 3 спальни/4 с/у, мебель новая. Переулок 5 м, машина проезжает. Подходит для семьи или специалиста.",
  "https://www.nhatot.com/thue-nha-dat-quan-lien-chieu-da-nang/134278743.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Thị Duyên"}),

L(1105,"da-nang","st","Дом",18000000,75,
  "Дом в квартале Tân Thái (Mân Thái) у моря — 2 спальни, гостиная, кухня, санузлы. Полная современная меблировка, охраняемый район, морской воздух. Принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134278633.htm","сегодня",0,source="chotot",
  details={"contact":"Thuê Nhà Đẹp Căn Hộ Cao Cấp Đà Nẵng"}),

L(1106,"da-nang","ah","Квартира",9000000,35,
  "Квартира с выделенной спальней на ул. Lê Hữu Trác — 35м², полная меблировка, своя стиральная машина, сильный wi-fi, просторный балкон. Рядом мост Trần Thị Lý, рынок An Hải Đông, пляж Mỹ Khê.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134278530.htm","сегодня",0,source="chotot",
  details={"amenities":"можно с животными, принимают иностранцев и заезд от 1 месяца","contact":"Ha for rent APT"}),

L(1107,"da-nang","ns","Дом",26000000,85,
  "Новый дом на ул. Vũ Mộng Nguyên (Khuê Mỹ) — 2 изолированные спальни, 3 с/у (свой санузел в каждой спальне), просторная гостиная и кухня. Мебель новая, большой двор, машина паркуется у дома.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134278495.htm","сегодня",0,source="chotot",
  details={"contact":"Thuê Nhà Đẹp Căn Hộ Cao Cấp Đà Nẵng"}),

L(1108,"da-nang","ns","Квартира",10000000,45,
  "Квартира с 1 спальней на ул. Khuê Mỹ Đông 3 рядом с районом An Thượng и пляжем Mỹ Khê — 45м², полная меблировка, своя стиральная машина, большой отдельный балкон, паркинг внутри здания.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134277617.htm","сегодня",0,source="chotot",
  details={"notice":"в структурном поле площадки цена 9 999 999 ₫, в тексте объявления — 10 млн ₫/мес","contact":"MrNam Căn Hộ Giá Tốt Đà Nẵng"}),

L(1109,"da-nang","hx","Квартира",5800000,30,
  "Квартира с 1 спальней и антресолью на ул. Thanh Lương 26 (Hòa Xuân) — 30м², полная меблировка (кровать, шкаф, кухня, кондиционер), своя стиральная машина. Рядом рынок Hòa Xuân, университеты Đông Á и Kiến Trúc, Mega Market.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134277426.htm","сегодня",0,source="chotot",
  details={"contact":"Hùng Home"}),

L(1110,"da-nang","tk","Дом",35000000,78,
  "Трёхэтажный дом на ул. Yên Khê 2 — 78м², 3 спальни/3 с/у плюс отдельный кабинет и собственный мини-бассейн. Подходит семье или специалисту на удалённой работе, заезд сразу.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134277405.htm","сегодня",0,source="chotot",
  details={"contact":"Ngọc Minh"}),

L(1111,"da-nang","st","Квартира",8000000,37,
  "Квартира в ЖК Golden Bay (ул. Lê Văn Duyệt) — 37м², 1 спальня, с/у, гостиная, кухня, балкон. Меблировка уровня 5 звёзд, вид на город, море, реку и залив. Бассейн-инфинити, ресторан, бар, спортзал, супермаркет, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134276949.htm","сегодня",0,source="chotot",
  details={"contact":"Huynh Phong (напрямую от хозяина)"}),

L(1112,"da-nang","ns","Студия",3800000,30,
  "Студия на ул. Nguyễn Duy Trinh (Hoà Hải) — 30м², балкон, телевизор, холодильник, кухня, кровать. Рядом кампус FPT и Университетская деревня.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134276792.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении указан диапазон 3,7-4,2 млн ₫/мес на несколько свободных комнат; в структурном поле площадки — 3,8 млн ₫","contact":"Tuấn Trần bds ngũ hành sơn"}),

L(1113,"da-nang","ah","Дом",55000000,112,
  "Вилла на первой линии ул. Phạm Tu (Phước Mỹ) — 112м², фасад 8 м, 5 спален/6 с/у, джакузи, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134276768.htm","сегодня",0,source="chotot",
  details={"contact":"MR HUY"}),

L(1114,"da-nang","hx","Дом",6500000,120,
  "Одноэтажный дом целиком на первой линии ул. Kiều Phụng (Hòa Xuân) — 2 спальни, 126,5м². Долгосрочная аренда, подходит семье или молодой паре.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134276488.htm","сегодня",0,source="chotot",
  details={"notice":"площадь по тексту объявления 126,5м², в структурном поле площадки — 120м²","contact":"Cẩm Nhung"}),

L(1115,"da-nang","ah","Квартира",12000000,40,
  "Sandy House 3, 45 Phan Huy Ích — квартира с отдельной спальней, 40м². Полная меблировка (индукционная плита, посуда, микроволновка, рисоварка), своя стиральная машина. Угловой блок с двумя фасадами: много окон и свой балкон.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134276235.htm","сегодня",0,source="chotot",
  details={"notice":"цена 11,5-12 млн ₫/мес в зависимости от срока договора; лифта нет; без животных, электробайков и мотоциклов большого объёма","contact":"Huy Trương"}),

L(1116,"da-nang","ns","Квартира",8500000,30,
  "Квартира с 1 спальней в районе Mỹ An у реки Хан (ул. Lê Văn Hưu) — полная меблировка, очень тихое место, вокруг нет строек.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134276065.htm","сегодня",0,source="chotot",
  details={"notice":"дом открывается в начале сентября, посмотреть можно уже сейчас; договор от 3 месяцев; без животных","contact":"Văn Cần"}),

L(1117,"da-nang","ns","Квартира",8000000,45,
  "Квартира с отдельной спальней в квартале Nam Việt Á, 79 Nghiêm Xuân Yêm — полная меблировка (кондиционер, холодильник, стиральная машина, матрас, водонагреватель, стол со стульями), просторный паркинг, крытая сушилка. Рядом Университет экономики, кампус FPT, больница на 600 коек.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134276011.htm","сегодня",0,source="chotot",
  details={"notice":"в тексте объявления цена обозначена как «7,x млн», в структурном поле площадки — 8 млн ₫/мес","contact":"TUYẾT LỤA (напрямую от хозяина)"}),

L(1118,"da-nang","ns","Студия",13500000,35,
  "Студия на ул. Lê Quang Đạo (Mỹ An) — 35м², просторный балкон, еженедельная уборка. До пляжа несколько минут пешком, свободна сейчас.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134275768.htm","сегодня",0,source="chotot",
  details={"notice":"цена обсуждается","contact":"HAVILAND CĂN HỘ GIÁ TỐT"}),

L(1119,"da-nang","lc","Дом",4500000,90,
  "Одноэтажный дом с антресолью на ул. Nguyễn Phước Chu — 89м², 2 спальни, просторные гостиная и кухня, дом почти новый. Рядом администрация района Hải Vân и рынок, до пляжа около 150 м.",
  "https://www.nhatot.com/thue-nha-dat-quan-lien-chieu-da-nang/134275716.htm","сегодня",0,source="chotot",
  details={"notice":"старый район — Phường Hòa Hiệp Bắc, в новой сетке Phường Hải Vân; отнесён к ближайшему району проекта Liên Chiểu (по прецеденту прошлого батча)","contact":"nguyễn văn khôi"}),

L(1120,"da-nang","ns","Квартира",5200000,35,
  "Мини-квартира на ул. Phạm Khiêm Ích (Ngũ Hành Sơn) — 35м², полная меблировка (кондиционер, холодильник, матрас, водонагреватель, стол со стульями), стиральная машина общая, просторный паркинг. Рядом Университет экономики, кампус FPT, больница на 600 коек.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134275705.htm","сегодня",0,source="chotot",
  details={"contact":"TUYẾT LỤA (напрямую от хозяина)"}),

L(1121,"da-nang","st","Квартира",8500000,45,
  "Квартира с 1 спальней на ул. Nguyễn Đăng Tuyến (Thọ Quang) — 45м², вид на море, полная меблировка, много естественного света. Тихий охраняемый жилой квартал, заезд сразу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134274738.htm","сегодня",0,source="chotot",
  details={"contact":"Huy ho"}),

L(1122,"da-nang","ah","Квартира",18000000,65,
  "Угловая квартира в ЖК Harmony на ул. Phạm Văn Đồng — 65м², 2 спальни/2 с/у, гостиная, кухня, балкон с прямым видом на пляж Mỹ Khê, высокий этаж. Полная меблировка высокого класса.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134274203.htm","сегодня",0,source="chotot",
  details={"notice":"договор от 6 месяцев, залог 1 месяц, оплата раз в 3 месяца","contact":"Trần Thuyết DXMT"}),

L(1123,"da-nang","ah","Квартира",17500000,82,
  "Квартира в ЖК Monarchy (An Trung 2) — 82м², 2 спальни/2 с/у, полная меблировка, просторный балкон. Бассейн, мини-маркет, кафе, охрана 24/7. Рядом река Хан, мост Rồng и море. Свободна, заезд сразу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134273428.htm","сегодня",0,source="chotot",
  details={"contact":"Kiều Oanh"}),

L(1124,"da-nang","ns","Квартира",8000000,35,
  "Новая квартира с 1 спальней на ул. Mai Thúc Lân (Ngũ Hành Sơn) — 35м², окно, полная меблировка, своя стиральная машина, сильный wi-fi. Рядом мост Trần Thị Lý, пляж Mỹ Khê, ул. Nguyễn Văn Thoại. Есть где поставить машину.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134273062.htm","сегодня",0,source="chotot",
  details={"amenities":"принимают иностранцев и заезд от 1 месяца","contact":"Ha for rent APT"}),

L(1125,"da-nang","ns","Дом",35000000,150,
  "Вилла в районе Ngũ Hành Sơn рядом с FPT Plaza (ул. Vùng Trung 4) — 150м² с садом, 2 этажа, 3 спальни/4 с/у, современная мебель. Тихий квартал, подходит семье или специалисту.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134272994.htm","сегодня",0,source="chotot",
  details={"contact":"Diep Nguyen"}),

L(1126,"da-nang","ns","Квартира",21000000,51,
  "Квартира в ЖК Panoma 1 (ул. Phạm Hữu Kính, Mỹ An) — 51м², планировка «1 спальня+», две кровати. Светлая современная отделка, хороший матрас, новая сантехника. Подходит одному, паре или небольшой семье на долгий срок.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134272870.htm","сегодня",0,source="chotot",
  details={"contact":"Danang Luxury Realty"}),

L(1127,"da-nang","hcg","Дом",15000000,86,
  "Трёхэтажный дом в переулке K40 Nguyễn Hữu Thọ (квартал Bộ Đội) — участок 86м², общая площадь 232м², спальни, 3 с/у, терраса на крыше. Дом только что отремонтирован и покрашен, пустой. Переулок с проездом для машины, тихо и безопасно.",
  "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134272817.htm","сегодня",0,source="chotot",
  details={"notice":"в тексте объявления 5 спален, в структурном поле площадки — 4","contact":"THANH"}),

L(1128,"da-nang","ah","Дом",22000000,150,
  "Вилла в квартале Phúc Lộc Viên (ул. Ngô Quyền) — 150м², 2 этажа, 4 спальни/3 с/у. Тихий охраняемый жилой квартал, просторно. Подходит семье или иностранному специалисту на долгий срок.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134272669.htm","сегодня",0,source="chotot",
  details={"contact":"Danang Luxury Realty (код V0177)"}),

L(1129,"da-nang","ns","Квартира",40000000,83,
  "Квартира в ЖК Panoma 2, 23-й этаж — 83м², 2 спальни/2 с/у, вид на море, современная полная меблировка. Ресепшн, спортзал, бассейн, сауна, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134272232.htm","сегодня",0,source="chotot",
  details={"notice":"в структурном поле площадки район указан как An Hải, в тексте объявления — Nguyễn Tư Giãn, Mỹ An, Ngũ Hành Sơn; отнесён по тексту","contact":"Hồ Diệu Quỳnh"}),

L(1130,"da-nang","ns","Студия",6000000,50,
  "Студия в жилом квартале FPT — 50м², балкон, полная меблировка, просторный сад, своя стиральная машина, общая терраса. Камеры 24/7, свободный режим входа, уборка общих зон.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134271680.htm","сегодня",0,source="chotot",
  details={"notice":"хозяин не принимает иностранцев и животных","contact":"MrNam Căn Hộ Giá Tốt Đà Nẵng"}),

L(1131,"da-nang","tk","Дом",16000000,75,
  "Трёхэтажный дом в переулке K149 Lê Đình Lý — 75м², просторная гостиная, 3 спальни, 4 кондиционера, 3 с/у, кухня, стиральная машина, водонагреватель. Переулок 15 м, долгосрочная аренда.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134271050.htm","сегодня",0,source="chotot",
  details={"contact":"lethimylinh"}),

L(1132,"da-nang","ns","Квартира",32000000,70,
  "Квартира в ЖК Panoma (ул. Trần Thị Lý) — 70м², 2 спальни/2 с/у, полная меблировка и техника (кондиционер, стиральная машина, телевизор). Бассейн, спортзал, спа, ресепшн, охрана 24/7. Рядом река Хан, мосты Rồng и Trần Thị Lý, пляж Mỹ Khê. Свободна.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134270865.htm","сегодня",0,source="chotot",
  details={"amenities":"в этом же доме есть студии от 14 млн, 1-спальные от 23 млн, 3-спальные от 40 млн ₫/мес","contact":"Kiều Oanh"}),

L(1133,"da-nang","ah","Дом",17000000,88,
  "Трёхэтажный дом на первой линии ул. Phước Mỹ 1 рядом с рынком Phước Mỹ — 88м² (4,4x20), гостиная, кухня, 3 спальни/4 с/у. До пляжа Mỹ Khê около 200 м. Договор на год.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134270842.htm","сегодня",0,source="chotot",
  details={"contact":"агентство BĐS Newlands"}),

L(1134,"da-nang","lc","Квартира",13000000,63,
  "Квартира на ул. Ngô Thì Nhậm (Liên Chiểu) — 63м², 2 спальни/2 с/у, полная меблировка, вид на море. Новый дом, подходит семье или специалисту.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134270598.htm","сегодня",0,source="chotot",
  details={"notice":"в заголовке и структурном поле цена 13 млн ₫/мес, в тексте описания — 15 млн ₫/мес; взята цена из заголовка и структурного поля","contact":"Tùng Lưu Căn Hộ Đà Nẵng"}),

L(1135,"da-nang","ns","Дом",195000000,200,
  "Новая вилла с бассейном в переулке Trần Văn Dư — 200м², фасад 9,5 м, 4 этажа, 7 изолированных спален, комната для караоке, сауна, большой бассейн, терраса на крыше, лифт. Полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134270556.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng Huy"}),

L(1136,"da-nang","ns","Дом",100000000,91,
  "Новая вилла с бассейном в районе An Thượng — фасад 7 м, 3 этажа, 5 спален, бассейн, сауна, джакузи. Полная меблировка, сдача новая.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134270466.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng Huy"}),

L(1137,"da-nang","ns","Дом",115000000,100,
  "Вилла с бассейном на ул. Trần Văn Dư (Mỹ An) — 100м², фасад 5 м, 3 этажа, 4 изолированные спальни (5 кроватей), у каждой спальни свой балкон. Бассейн с электролизной очисткой солью внутри дома, современная кухня, барбекю на верхней террасе.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134270292.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng Huy"}),

L(1138,"da-nang","hk","Дом",12000000,85,
  "Новый дом рядом с развязкой Ngã 3 Huế и ул. Hoàng Thị Loan — 85м², 2 спальни/2 с/у, двор под парковку, свежая плитка. Дорога 5,5 м, тротуар 3 м.",
  "https://www.nhatot.com/thue-nha-dat-quan-lien-chieu-da-nang/134269897.htm","сегодня",0,source="chotot",
  details={"notice":"дом сдаётся без мебели","contact":"Nhà Xanh (напрямую от хозяина)"}),

L(1139,"da-nang","ns","Дом",38000000,95,
  "Новый дом на ул. Đoàn Khuê — 95м², 4 этажа плюс терраса, 4 изолированные спальни/5 с/у. Техника высокого класса: большой холодильник side-by-side, канальный кондиционер в гостиной, солнечные панели. Заезд сразу.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134269773.htm","сегодня",0,source="chotot",
  details={"contact":"Ngọc Minh"}),

L(1140,"da-nang","hk","Дом",22000000,100,
  "Новая мини-вилла на ул. Tô Hiệu (Hòa Minh) — участок 65м², 3 этажа, 3 спальни/3 с/у, свой балкон и терраса на крыше. Полная меблировка, заезд сразу. Принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-lien-chieu-da-nang/134269771.htm","сегодня",0,source="chotot",
  details={"contact":"BÌNH CAPITAL"}),

L(1141,"da-nang","ns","Дом",25000000,300,
  "Вилла с садом на ул. Đạm Phương — 300м², фасад 12 м, 2 спальни/2 с/у, полная меблировка, большой двор.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134248682.htm","вчера",1,source="chotot",
  details={"contact":"T An"}),

L(1142,"da-nang","hx","Дом",18000000,100,
  "Трёхэтажный дом на ул. Diên Hồng (Hòa Xuân) — 100м², 3 спальни, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134247953.htm","вчера",1,source="chotot",
  details={"contact":"Mr Zco"}),

L(1143,"da-nang","hcg","Студия",13000000,35,
  "Студия с отделённой кухней на ул. Hóa Sơn 7 — 35м², очень просторная и светлая, большой балкон, своя стиральная и сушильная машина. Дом новый, рядом Lotte.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134246815.htm","вчера",1,source="chotot",
  details={"notice":"в объявлении указан диапазон 11-13 млн ₫/мес; в структурном поле площадки — 13 млн ₫","contact":"HAVILAND CĂN HỘ GIÁ TỐT"}),

L(1144,"da-nang","st","Дом",85000000,180,
  "Вилла рядом с мостом Thuận Phước (ул. Nguyễn Hữu An) — 180м², 3 этажа, 4 спальни с собственными санузлами, ванна в спальне, свой бассейн, большая терраса на крыше.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134246680.htm","вчера",1,source="chotot",
  details={"contact":"Ruby Ho, Toan Huy Hoang Realty (код V0231)"}),

L(1145,"da-nang","hx","Дом",8000000,100,
  "Одноэтажный дом на ул. Khương Hữu Dụng (Hòa Xuân) — 100м², фасад 5 м, 2 спальни, базовая мебель.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134246520.htm","вчера",1,source="chotot",
  details={"contact":"MR AN"}),

L(1146,"da-nang","ns","Дом",35000000,100,
  "Четырёхэтажный дом на ул. Trương Quang Được — 100м², фасад 5 м, 5 спален/4 с/у.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134246016.htm","вчера",1,source="chotot",
  details={"contact":"MR AN"}),

L(1147,"da-nang","ah","Квартира",25000000,66,
  "Квартира в ЖК Hiyori на ул. Võ Văn Kiệt, 22-й этаж — 66м², 2 спальни/2 с/у, полная меблировка, хороший вид. До моря 5 минут.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134245862.htm","вчера",1,source="chotot",
  details={"notice":"договор от 6 месяцев, залог 2 месяца, оплата раз в 3 месяца; можно с животными","contact":"Thanh Trung Haviland"}),

L(1148,"da-nang","hc","Квартира",20000000,50,
  "Квартира в SAM Tower на ул. Như Nguyệt у реки Хан — отдельная спальня, просторная гостиная, современная кухня, большие окна на реку. Мебель новая, всё необходимое есть. Рядом мост Rồng, Vincom, рынок Hàn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134234433.htm","2 дня назад",2,source="chotot",
  details={"notice":"площадь по тексту объявления 54м², в структурном поле площадки — 50м²","contact":"Minh Trang"}),

L(1149,"da-nang","ns","Дом",35000000,90,
  "Трёхэтажный дом на ул. Lê Văn Tâm — 90м², фасад 5 м, 5 спален/5 с/у, базовая мебель.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134233711.htm","2 дня назад",2,source="chotot",
  details={"contact":"mr An"}),

L(1150,"da-nang","hc","Квартира",15500000,65,
  "Квартира в ЖК F.Home (Thạch Thang) — 65м², 2 спальни/2 с/у, полная меблировка, высокий этаж, светло и просторно.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134225742.htm","2 дня назад",2,source="chotot",
  details={"notice":"описание в объявлении минимальное — указаны только дом, площадь, планировка и цена","contact":"Nam Văn"}),

L(1151,"da-nang","hx","Квартира",10500000,50,
  "Новая квартира по адресу 245 Nguyễn Kim рядом с ул. Phạm Hùng — 50м², 2 спальни, свой просторный балкон, полная меблировка, заезд сразу. Тихий жилой квартал, рядом супермаркет, кафе, рестораны.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134225216.htm","2 дня назад",2,source="chotot",
  details={"notice":"цена обсуждается","contact":"Huy ho"}),

L(1152,"da-nang","ah","Дом",20000000,70,
  "Двухэтажный дом на ул. Nguyễn Duy Hiệu (An Hải, Sơn Trà) — 70м², 3 спальни/2 с/у, полная меблировка. Рядом море и рынок.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134218440.htm","3 дня назад",3,source="chotot",
  details={"contact":"Ms Diễm"}),

L(1153,"da-nang","ah","Дом",18000000,90,
  "Двухэтажный дом на первой линии в квартале Hồ Nghinh — 90м², 3 спальни/3 с/у, всё необходимое есть. Приоритет долгосрочной аренде.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134216301.htm","3 дня назад",3,source="chotot",
  details={"contact":"Ms Diễm"}),

L(1154,"da-nang","hx","Студия",4600000,30,
  "Новая студия на первой линии по адресу 123 Mẹ Thứ в центре Hòa Xuân — 30м², мебель новая, своя стиральная машина и сушилка, свободный режим входа, охрана. Рядом рынок Hòa Xuân, Mega Market, улицы 29/3 и Võ Chí Công.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134211490.htm","3 дня назад",3,source="chotot",
  details={"notice":"хозяин не принимает иностранцев и электробайки; электричество 4 000 ₫/кВт·ч, вода 100 000 ₫/чел.","contact":"Nguyễn Nhật Tân"}),

L(1155,"nha-trang","vp","Квартира",16000000,73,
  "Квартира в ЖК Mường Thanh Viễn Triều, корпус OC3 — 73м², 2 спальни/2 с/у. Залог 1 месяц, оплата за 2, договор на год.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134278034.htm","сегодня",0,source="chotot",
  details={"contact":"Văn Hoà"}),

L(1156,"nha-trang","vp","Квартира",11000000,60,
  "Квартира в ЖК Mường Thanh Viễn Triều, корпус OC1A, 15-й этаж — 60м², 2 спальни/2 с/у.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134277411.htm","сегодня",0,source="chotot",
  details={"notice":"цена не включает коммунальные платежи; животных не принимают; договор 3-12 месяцев","contact":"Hà Lương IT"}),

L(1157,"nha-trang","ph","Дом",32000000,100,
  "Четырёхэтажный дом с лифтом в квартале Hà Quang 2 (Phước Hải) — этаж 100м² (фасад 5 м), общая площадь 420м², 4 спальни, кухня, сауна, полная меблировка. Дорога перед домом 16 м, тротуар 3 м. Рядом море, рынок, школы, супермаркет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134275771.htm","сегодня",0,source="chotot",
  details={"notice":"первый этаж — свободная площадь под «чистый» бизнес; цена обсуждается","contact":"Nguyễn Trần Duy Phước (код NOK-2981)"}),

L(1158,"nha-trang","ph","Дом",16000000,80,
  "Трёхэтажный дом в квартале Hà Quang 2 (Phước Hải) — этаж 90м² (5x18), общая площадь 270м², 3 спальни/4 с/у, гостиная, кухня. Базовая мебель: стиральная машина, холодильник, индукционная плита, телевизор.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134275621.htm","сегодня",0,source="chotot",
  details={"notice":"площадь этажа по тексту объявления 90м², в структурном поле площадки — 80м²","contact":"Nguyễn Trần Duy Phước (код NOK-2320)"}),

L(1159,"nha-trang","vh","Дом",7000000,80,
  "Дом на первой линии в районе Vĩnh Hải недалеко от моря — 110м², 2 комнаты, кухня, санузел и ванная, кондиционер. Рядом центр, пляж, рынок, супермаркет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134275505.htm","сегодня",0,source="chotot",
  details={"notice":"площадь по тексту объявления 110м², в структурном поле площадки — 80м²; формат «дом с возможностью торговли на первом этаже»","contact":"Nguyễn Trần Duy Phước (код NOK-2465)"}),

L(1160,"nha-trang","lt","Дом",18000000,70,
  "Двухэтажный дом в Западном квартале (Lộc Thọ) — 70м², фасад 4,5 м. Первый этаж: свободная площадь, спальня, кухня, с/у; антресольный этаж: спальня и с/у. Полная меблировка. Рядом море, рынок, школы, супермаркет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134275258.htm","сегодня",0,source="chotot",
  details={"notice":"первый этаж — свободная площадь под «чистый» бизнес","contact":"Nguyễn Trần Duy Phước (код NOK-2983)"}),

L(1161,"nha-trang","ph","Дом",35000000,130,
  "Трёхэтажный дом с лифтом в квартале Hà Quang 2 (Phước Hải) — этаж 130м² (5x26), общая площадь 390м², двор, гостиная, кухня, 4 спальни/5 с/у, площадка для сушки. Полная меблировка из массива. Дорога перед домом 8 м, парковка свободная.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134273956.htm","сегодня",0,source="chotot",
  details={"notice":"хозяин отмечает, что дом подходит для совмещения жилья и офиса","contact":"Phương GoHome (код NOK-2986)"}),

L(1162,"nha-trang","vt2","Дом",25000000,32,
  "Трёхэтажный дом рядом с морем в центре города (ул. Hàn Thuyên) — этаж 32м² (фасад около 3 м), общая площадь 120м², 3 спальни/2 с/у, кухня, гостиная, мансарда. Мебель новая. Рядом пляж и рынок Chợ Đầm, тихий квартал, переулок 3 м.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134273713.htm","сегодня",0,source="chotot",
  details={"notice":"старый район — Phường Xương Huân, отнесён к ближайшему району проекта Vạn Thạnh (по прецеденту прошлых батчей)","contact":"Phương GoHome (код NNC-2439)"}),

L(1163,"nha-trang","vh","Дом",30000000,94,
  "Новый дом на ул. Phạm Tu (Vĩnh Hải) — 94м², фасад 6 м. Первый этаж: просторный двор для машины, гостиная-кухня в два света, 2 спальни/2 с/у; второй: спальня, большая терраса и кабинет. Мебель новая, полная.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134274485.htm","сегодня",0,source="chotot",
  details={"contact":"Phương GoHome (код NNC-2438)"}),

L(1164,"nha-trang","ps","Дом",9000000,60,
  "Трёхэтажный дом в районе Vĩnh Hiệp рядом с супермаркетом GO! (ул. Cầu Dứa Phú Nông) — этаж 60м² (4x15), общая площадь около 300м², 3 спальни/4 с/у, гостиная, полная меблировка. Переулок 3 м, места для машины нет.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134274180.htm","сегодня",0,source="chotot",
  details={"notice":"старый район — Xã Vĩnh Hiệp, отнесён к ближайшему району проекта Phương Sài (по прецеденту прошлых батчей)","contact":"Phương GoHome (код NNC-2406)"}),

L(1165,"nha-trang","pl","Дом",6000000,50,
  "Дом в переулке ул. Đồng Nai (Phước Long), 30 м от ул. Phùng Thế Tài — 50м², два уровня, 3 спальни. Дом пустой, без мебели.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134268104.htm","сегодня",0,source="chotot",
  details={"contact":"Phan Thị Lan"}),

L(1166,"nha-trang","pl","Квартира",14000000,68,
  "Новая квартира в ЖК CCU-01 (Phước Long) — 68м², 2 спальни/2 с/у, полная меблировка высокого класса, открытый вид.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134267508.htm","сегодня",0,source="chotot",
  details={"contact":"Phan Thị Lan"}),

L(1167,"nha-trang","tl","Квартира",17000000,68,
  "Квартира в HUD Building на ул. Nguyễn Thiện Thuật в центре города — 68м², 2 спальни/2 с/у, полная меблировка. До моря несколько минут пешком.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134266282.htm","сегодня",0,source="chotot",
  details={"contact":"Phan Thị Lan"}),

L(1168,"nha-trang","tl","Дом",17000000,35,
  "Дом на ул. Lạc Long Quân — этаж 35м² (фасад 5 м), общая площадь 120м², 4 спальни/3 с/у, базовая мебель. Залог 1 месяц, оплата за 3.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134258607.htm","вчера",1,source="chotot",
  details={"contact":"Hà Lương IT"}),

L(1169,"nha-trang","lt","Квартира",13500000,50,
  "Квартира в ЖК GoldCoast, 1 Trần Hưng Đạo — 50м², 1 спальня/1 с/у, балкон, вид на море. Дом новый, до пляжа шаг. Lotte Mart, кинотеатр, бассейн, спортзал, спа в здании, охрана 24/7, лифт с картой на этаж, есть машиноместо.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134256127.htm","вчера",1,source="chotot",
  details={"contact":"Thuy Do (напрямую от хозяина)"}),

L(1170,"nha-trang","tl","Квартира",16000000,60,
  "Квартира в HUD Building на ул. Nguyễn Thiện Thuật в центре города — 60м², 2 спальни/2 с/у, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134255602.htm","вчера",1,source="chotot",
  details={"contact":"Phan Thị Lan"}),

L(1171,"nha-trang","ph","Квартира",7500000,40,
  "Новая квартира с отдельной спальней в районе Phước Hải (ул. Lê Hồng Phong), 3-й этаж без лифта — 40м², кухня и зона стирки за стеклянной перегородкой, чистый санузел, балкон. Мебель новая. В объявлении есть описание на русском.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134254948.htm","вчера",1,source="chotot",
  details={"notice":"без животных и маленьких детей; электричество 5 000 ₫/кВт·ч, вода 120 000 ₫/чел., wi-fi и уборка 100 000 ₫/мес","contact":"Thanh Nhã Apartment (напрямую от хозяина)"}),

L(1172,"nha-trang","pl","Дом",12000000,100,
  "Дом в переулке Đồng Muối (Phước Long) с проездом для машины — 100м², 2 спальни, гостиная, просторная кухня, полная меблировка. Залог 2 месяца, оплата раз в 2 месяца.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134254894.htm","вчера",1,source="chotot",
  details={"contact":"Phan Thị Lan"}),

L(1173,"nha-trang","vt2","Квартира",15000000,76,
  "Квартира в ЖК Mường Thanh Khánh Hòa — 2 спальни/2 с/у, кухня, гостиная, небольшой балкон для сушки белья, полная меблировка. До рынка Chợ Đầm около 1 км, до пляжа 4 минуты пешком; на первом этаже дома кофейни и мини-маркеты. В объявлении есть описание на английском.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134249405.htm","вчера",1,source="chotot",
  details={"notice":"площадь по тексту объявления 68м², в структурном поле площадки — 76м²; сверх цены: обслуживание 500 000 ₫, регистрация проживания 200 000 ₫, интернет 275 000 ₫/мес; старый район — Phường Xương Huân, отнесён к ближайшему району проекта Vạn Thạnh","contact":"Mai Anh"}),

L(1174,"nha-trang","pl","Квартира",11000000,68,
  "Квартира в ЖК CCU-01 (Phước Long) — 68м², 2 спальни/2 с/у, юго-восточный балкон. Дом новый, мебель новая.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134249078.htm","вчера",1,source="chotot",
  details={"contact":"Phan Thị Lan"}),

L(1175,"nha-trang","pl","Квартира",16000000,88,
  "Угловая квартира в ЖК CCU-01 (Phước Long) — 88м², 3 спальни/2 с/у, широкий балкон, хорошо проветривается. Дом новый, полная меблировка высокого класса.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134248169.htm","вчера",1,source="chotot",
  details={"contact":"Phan Thị Lan"}),

L(1176,"nha-trang","pl","Квартира",10500000,65,
  "Квартира в ЖК CCU-01 (Phước Long), высокий этаж — 65м², 2 спальни/2 с/у, базовая мебель. Дом новый. Залог 2 месяца, оплата за 1.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134247857.htm","вчера",1,source="chotot",
  details={"contact":"Phan Thị Lan"}),

L(1177,"nha-trang","vp","Квартира",12000000,60,
  "Квартира в ЖК Mường Thanh Viễn Triều, 22-й этаж — 60м², 2 спальни/2 с/у, полная меблировка. Залог 1 месяц, оплата за 1.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134242754.htm","2 дня назад",2,source="chotot",
  details={"notice":"в тексте объявления дом указан как Mường Thanh Viễn Triều (Vĩnh Phước), в структурном поле площадки район — Xương Huân; отнесён по тексту","contact":"Nguyễn Đại Sơn"}),

L(1178,"nha-trang","vp","Квартира",11000000,55,
  "Квартира в ЖК Napoleon на ул. Nguyễn Đình Chiểu (Vĩnh Phước) — 55м², 2 спальни/1 с/у, полная меблировка, заезд сразу. Рядом Университет Нячанга.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134242583.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nguyễn Đại Sơn"}),

L(1179,"nha-trang","vh","Дом",30000000,150,
  "Новый дом целиком рядом с пляжем Hòn Chồng — 150м², 2 спальни/2 с/у, терраса на крыше с барбекю. Полная новая меблировка. Рядом море и рынок, можно с животными.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134242555.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nguyễn Đại Sơn"}),

L(1180,"nha-trang","vh","Квартира",10000000,60,
  "Угловая квартира в ЖК Hoàng Quân на севере города (ул. Trịnh Hoài Đức) — 60м², 2 спальни/2 с/у, мебель новая.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134240026.htm","2 дня назад",2,source="chotot",
  details={"notice":"описание в объявлении очень краткое; старый район — Phường Vĩnh Hòa, отнесён к ближайшему району проекта Vĩnh Hải (по прецеденту прошлых батчей)","contact":"Binh"}),

L(1181,"nha-trang","ph2","Дом",30000000,60,
  "Новый дом целиком в квартале KĐT ACC Vườn Xoài (Phước Hòa) — 4 этажа, этаж 60м², общая площадь 240м², гостиная-кухня, 4 спальни/5 с/у, полная меблировка. Охраняемый квартал, вокруг вся инфраструктура.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134239876.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trần Minh Tiến"}),

L(1182,"nha-trang","vt","Квартира",11000000,65,
  "Квартира в ЖК PH — 65м², 2 спальни/2 с/у, просторный балкон, высокий этаж, вид на море и город. Полная меблировка, заезд сразу. Охрана 24/7, подземный паркинг. Рядом море, супермаркет, школы.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134235687.htm","2 дня назад",2,source="chotot",
  details={"contact":"Hà Lương IT"}),

L(1183,"nha-trang","lt","Студия",16000000,51,
  "Студия в ЖК Gold Coast, южная башня, 29-й этаж — 51м². Залог 2 месяца, оплата за 1.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134235610.htm","2 дня назад",2,source="chotot",
  details={"contact":"Hà Lương IT"}),

L(1184,"nha-trang","vp","Студия",7000000,30,
  "Студия в ЖК Mường Thanh Viễn Triều — 30м², полная меблировка (телевизор, холодильник, кондиционер), варианты с одной или двумя кроватями. Прямо у пляжа Hòn Chồng, 5 минут до центра. Подземный паркинг, охрана.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134234541.htm","2 дня назад",2,source="chotot",
  details={"notice":"хозяин сдаёт и посуточно (600 000 ₫/сутки), помесячная ставка — 7 млн ₫","contact":"Nguyễn Tuấn Đại"}),

L(1185,"nha-trang","vt2","Квартира",13500000,68,
  "Квартира в ЖК Mường Thanh Khánh Hòa у моста Trần Phú — 68м², 2 спальни/2 с/у, вид на реку. Залог 2 месяца, оплата за 1, договор долгосрочный.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134231254.htm","2 дня назад",2,source="chotot",
  details={"notice":"обслуживание и регистрация проживания — 700 000 ₫/мес сверх цены; старый район — Phường Xương Huân, отнесён к ближайшему району проекта Vạn Thạnh","contact":"Văn Hoà"}),

L(1186,"nha-trang","vh","Дом",30000000,150,
  "Новый дом в переулке ул. 2/4 на севере города — 150м², 2 спальни/2 с/у, комната для алтаря, просторная терраса на крыше для барбекю. Дом на этапе финальной отделки, современная планировка.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134225123.htm","2 дня назад",2,source="chotot",
  details={"notice":"залог 3 месяца, оплата раз в 3 месяца, договор на 12 месяцев","contact":"Quang Lộc Nha Trang"}),

L(1187,"nha-trang","ph","Дом",26000000,100,
  "Дом в квартале Hà Quang 2 (Phước Hải) — 100м² (5x20), 3 этажа с мансардой, 4 спальни/5 с/у. Кондиционеры, солнечные панели, место для машины. Дорога перед домом 13 м.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134210870.htm","3 дня назад",3,source="chotot",
  details={"notice":"хозяин отдаёт приоритет арендаторам под «чистый» офис","contact":"Hồ Như Ý"}),

L(1188,"nha-trang","lt","Квартира",5800000,30,
  "Квартира с 1 спальней на ул. Hoàng Hoa Thám (Lộc Thọ) — 30м², с мебелью. До моря около 150 м пешком.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134204527.htm","3 дня назад",3,source="chotot",
  details={"notice":"описание в объявлении очень краткое — указаны только улица, площадь, наличие мебели и расстояние до моря","contact":"Vũ Huy Hoàng"}),

L(1189,"da-lat","lb","Дом",4000000,100,
  "Дом целиком на ул. Châu Văn Liêm — 100м², гостиная, 2 спальни, кухня, отдельная комната для сушки белья (можно переделать в третью спальню). Дорога, где разъезжаются две машины, напротив зарядная станция VinFast. Есть двор для байков и машины, широкий тротуар.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134279006.htm","сегодня",0,source="chotot",
  details={"contact":"Minh"}),

L(1190,"da-lat","lb","Дом",7000000,70,
  "Дом целиком на ул. Đinh Công Tráng — 70м², 2 спальни/1 с/у, гостиная и кухня, полная меблировка (холодильник, кровать, диван, кухонный гарнитур, посуда). Место для байка и машины, свободный режим входа. Около 7 минут до озера Xuân Hương.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134268504.htm","сегодня",0,source="chotot",
  details={"notice":"залог 10 млн ₫, оплата помесячно, договор минимум на 2 года; электричество 4 000 ₫/кВт·ч, вода 25 000 ₫/м³, интернет арендатор проводит сам","contact":"Thanh Thủy (код NNC-67)"}),

L(1191,"da-lat","lv","Квартира",6000000,40,
  "Квартира на ул. Mê Linh — 40м², 2 спальни/1 с/у, большие окна, полная меблировка (холодильник, стиральная машина, телевизор, диван, кухня). Лифт и лестница, просторный подземный паркинг, свободный режим входа. Рядом Bách Hóa Xanh и Highlands Coffee, около 7 минут до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134268367.htm","сегодня",0,source="chotot",
  details={"notice":"электричество 5 000 ₫/кВт·ч, вода 15 000 ₫/м³; залог 1 месяц, договор минимум на 6 месяцев","contact":"Thanh Thủy (код CH-24)"}),

L(1192,"da-lat","cl","Студия",3500000,40,
  "Новая студия с просторной антресолью на ул. Tô Vĩnh Diện — 40м², с/у, кухонный гарнитур, мебель как на фото. Просторная парковка, свободный режим входа, вход по лестнице. Рядом рынок Ngô Quyền, храм, стадион, школы, больница.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134268248.htm","сегодня",0,source="chotot",
  details={"notice":"электричество и вода по государственному тарифу; залог 1,5 месяца (обсуждается), договор 3/6/12 месяцев","contact":"Thanh Thủy (код STU-150)"}),

L(1193,"da-lat","xh","Студия",4000000,40,
  "Студия на ул. Phan Đình Phùng, 2-й этаж — 40м², полная меблировка (кровать с матрасом, шкаф, холодильник, стиральная машина, кухня, обеденный стол, водонагреватель). Просторная парковка для байков, свободный режим входа. Рядом Nam Á Bank, WinMart, Bách Hóa Xanh, Highlands Coffee, около 3 минут до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134267995.htm","сегодня",0,source="chotot",
  details={"notice":"электричество 3 000 ₫/кВт·ч, вода 20 000 ₫/м³; залог 1 месяц, договор 3/6/12 месяцев","contact":"Thanh Thủy (код STU-144)"}),

L(1194,"da-lat","lv","Дом",6500000,60,
  "Дом на ул. Hùng Vương — этаж 60м², общая площадь 120м², 3 спальни/4 с/у, гостиная, кухня, просторная терраса под кафе и барбекю. Базовая меблировка: кухонный гарнитур, посуда, холодильник. Переулок с проездом для машины, есть парковка. Около 7 минут до озера Xuân Hương и ночного рынка.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134267340.htm","сегодня",0,source="chotot",
  details={"notice":"хозяин отмечает, что дом подходит под хоумстей и уже к этому подготовлен","contact":"Thanh Thủy (код NOK-34)"}),

L(1195,"da-lat","lv","Квартира",9000000,45,
  "Квартира на ул. Phù Đổng Thiên Vương — 45м², 1 спальня/1 с/у, кухня, полная меблировка (телевизор, холодильник, диван), восточная ориентация. Стиральная машина общая на первом этаже, лифт и лестница, охраняемый район, свободный режим входа. Рядом Университет Далата, около 5 минут до ночного рынка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134266898.htm","сегодня",0,source="chotot",
  details={"notice":"цена включает электричество, воду и wi-fi; машину и байк ставят на улице; договор 3-6 месяцев","contact":"Thanh Thủy (код CH-179)"}),

L(1196,"da-lat","lb","Студия",4500000,35,
  "Двухуровневая студия на ул. Tô Hiệu — 35м², первый уровень плюс антресоль, с/у, гостиная совмещена с кухней. Просторный сад, стиральная машина общая. Рядом автовокзал и больница, около 8 минут до Долины Любви.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134266736.htm","сегодня",0,source="chotot",
  details={"notice":"электричество и вода по государственному тарифу; залог 1 месяц, договор 6-12 месяцев","contact":"Thanh Thủy (код STU-146)"}),

L(1197,"vung-tau","tth","Квартира",12000000,75,
  "Квартира 20.06 в ЖК Gateway A на ул. Nguyễn An Ninh — 75м², 2 спальни/2 с/у, вся мебель остаётся, балкон с видом на море (по выходным видно фейерверк). Общий паркинг для машин.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134271271.htm","сегодня",0,source="chotot",
  details={"notice":"цена не включает коммунальные платежи ЖК; договор минимум на год, оплата помесячно или поквартально; хозяин отдаёт приоритет компаниям для сотрудников и иностранцам, помогает с регистрацией проживания и выдаёт счёт-фактуру","contact":"Vũ Minh Hiếu"}),
L(1198,"ho-chi-minh","tm","Квартира",30000000,128,
  "3-спальная квартира (2 с/у) 128м² в ЖК Docklands на ул. Nguyễn Thị Thập, Q7 — полная меблировка, готова к заезду. Цена с торгом, залог 2 месяца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134293885.htm","сегодня",0,source="chotot",
  details={"contact":"владелец напрямую"}),

L(1199,"ho-chi-minh","tm","Квартира",10000000,75,
  "2-спальная квартира (2 с/у) 75м² в ЖК Res III рядом с рынком Tân Mỹ, у ворот Phú Mỹ Hưng. Полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134282442.htm","сегодня",0,source="chotot",
  details={"contact":"Thiên Lộc"}),

L(1200,"ho-chi-minh","tm","Квартира",8500000,70,
  "Угловая 2-спальная квартира (2 с/у) 70м² в ЖК Belleza, блок B, Tân Mỹ — почти полная меблировка. Цена фиксированная: залог 2 месяца + 1 месяц вперёд.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134260804.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nguyễn Thị Hưng (em Hưng)"}),

L(1201,"ho-chi-minh","tm","Дом",30000000,80,
  "Дом целиком, 3 этажа, ул. Đường số, старый центр Q7 (ныне Tân Mỹ) — 300 м от рынка Tân Mỹ. Участок 4×20м (80м²), 6 спален, кухня, 3 санузла. Чистый, отделка как на фото.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134254961.htm","2 дня назад",2,source="chotot",
  details={"duplicateOf":873,"contact":"Khánh Phan BDS"}),

L(1202,"ho-chi-minh","th","Студия",6000000,30,
  "Студия (căn hộ dịch vụ) напротив университетов RMIT и TDTU, Tân Hưng, Q7 — рядом Phú Mỹ Hưng, Lotte Mart, Crescent Mall, VivoCity. Полная меблировка, балкон.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134292943.htm","сегодня",0,source="chotot",
  details={"contact":"Đức Quyền"}),

L(1203,"ho-chi-minh","th","Комната",6500000,35,
  "Комната 35м² в новом доме на 20 комнат (только что открылся), Tân Hưng, Q7, напротив Tôn Đức Thắng и RMIT. Полная меблировка, лифт, просторный двор, паркинг для машин, без общего с хозяином входа.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134292612.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng Phước Newind"}),

L(1204,"ho-chi-minh","th","Квартира",8000000,50,
  "1-спальная квартира 50м² в жилом комплексе Kim Sơn, Tân Hưng, Q7, рядом Lotte Mart. Полная меблировка, своя стиральная машина. Новый дом.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134292525.htm","сегодня",0,source="chotot",
  details={"contact":"Li Pao"}),

L(1205,"ho-chi-minh","th","Квартира",9500000,50,
  "1-спальная квартира 50м² в жилом комплексе Kim Sơn, Tân Hưng, Q7 — только что открылся. Премиальная меблировка, своя стиральная машина, пожарная безопасность подтверждена. Пешком до TDTU.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134292452.htm","сегодня",0,source="chotot",
  details={"notice":"электричество 4000 ₫/кВт·ч, вода+парковка+управление 300 000 ₫/мес","contact":"Huy Phan Megas"}),

L(1206,"ho-chi-minh","th","Квартира",10000000,37,
  "2-спальная квартира (2 с/у) 37м² в ЖК Lavida Plus, Tân Hưng, Q7 — полная меблировка (диван, кровать, шкаф, обеденный стол, холодильник, стиралка, кондиционер в каждой комнате). Бассейн, супермаркет в комплексе. Рядом RMIT, Tôn Đức Thắng, Lotte Mart, VivoCity, Crescent Mall.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134270761.htm","1 день назад",1,source="chotot",
  details={"contact":"Võ Thị Kim Thy"}),

L(1207,"ho-chi-minh","th","Студия",5400000,30,
  "Студия с балконом рядом с Lotte Mart, Tân Hưng, Q7 — чисто, тихий охраняемый квартал у парка, лифт, просторная парковка, камеры 24/7. Заезд без хозяина в доме, свободный режим входа.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134263452.htm","2 дня назад",2,source="chotot",
  details={"contact":"Thúy Doll"}),

L(1208,"ho-chi-minh","th","Студия",5900000,30,
  "Студия напротив RMIT, речной квартал Tân Hưng, Q7 — только что открылся дом, разные комнаты по цене 5,9-8,0 млн, лифт, подземный паркинг. Разрешены животные, принимают иностранцев, электровелосипед без подзарядки.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134290959.htm","сегодня",0,source="chotot",
  details={"notice":"диапазон цен по комнатам 5,9-8,0 млн ₫, взята нижняя граница; электричество 4000 ₫/кВт·ч, вода+парковка+управление 300 000 ₫/мес","contact":"Phạm Lộc Newind"}),

L(1209,"ho-chi-minh","th","Дом",15000000,80,
  "Дом целиком фасадом на Đường số, Tân Kiểng, Tân Hưng, Q7 — участок 3×26м, расширяется вглубь до 5,5м (80м²), 1 этаж + 1 этаж, 3 спальни/3 с/у + отдельная комната для алтаря. Южная ориентация, базовая меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134293765.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении отмечено «подходит для проживания в сочетании с бизнесом»","contact":"Gia Gia"}),

L(1210,"ho-chi-minh","th","Дом",90000000,200,
  "Вилла 10×20м в закрытом квартале Him Lam, Tân Hưng, Q7 — цоколь + 4 этажа, лифт премиум-класса, общая площадь застройки 1000м², 6 комнат/5 с/у, кондиционеры, большой двор с трёх сторон, просторный подземный паркинг.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134288266.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении отмечено «подходит для проживания, офиса или бизнеса»","contact":"Nguyễn Hoàng Minh Sơn"}),

L(1211,"ho-chi-minh","th","Дом",60000000,100,
  "Таунхаус 5×20м в закрытом квартале Him Lam, Tân Hưng, Q7, рядом ул. Nguyễn Thị Thập — цоколь + 4 этажа, общая площадь застройки 500м², 6 комнат/5 с/у, кондиционеры, двор спереди и сзади.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134288048.htm","сегодня",0,source="chotot",
  details={"notice":"цена указана «со всеми налогами»; в объявлении отмечено «подходит для проживания, офиса или бизнеса»","contact":"Nguyễn Hoàng Minh Sơn"}),

L(1212,"ho-chi-minh","th","Дом",5000000,20,
  "Дом целиком с антресолью в 100м от моста Him Lam, Tân Hưng, Q7 — переулок для машины шириной 8м, плотный жилой квартал, прямое электричество и вода.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134281630.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении отмечено «подходит для проживания вместе с небольшой торговлей»"}),

L(1213,"ho-chi-minh","th","Дом",10000000,50,
  "Дом целиком (3 комнаты) в переулке ул. Trần Xuân Soạn, Tân Hưng, Q7 — участок 5×10м, 1 этаж + 2 этажа, 3 спальни/3 с/у, гостиная, кухня. Центральное расположение, удобно до других районов.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134282685.htm","сегодня",0,source="chotot",
  details={}),

L(1214,"ho-chi-minh","ak","Квартира",20000000,70,
  "2-спальная квартира в ЖК Masteri Thảo Điền — средний этаж, прямой вид на реку. Полная качественная меблировка. Рядом ТЦ Vincom Mega Mall, станция метро №1, бассейн, спортзал, зона BBQ.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134255526.htm","2 дня назад",2,source="chotot",
  details={"contact":"Thái"}),

L(1215,"ho-chi-minh","ak","Студия",8000000,45,
  "Просторная студия в центре Thảo Điền, рядом мост Sài Gòn — 45м², свой балкон. Полная меблировка, заезд сразу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134255071.htm","2 дня назад",2,source="chotot",
  details={"contact":"Minh Khôi Chuyên Căn Hộ Quận 2"}),

L(1216,"ho-chi-minh","ak","Дом",18000000,35,
  "Дом целиком в переулке для машины, Thảo Điền — участок 4,3×8,1м (35м²), 1 этаж + 2 этажа, 3 спальни, 2 с/у, терраса на крыше. Тихий безопасный квартал.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134292991.htm","сегодня",0,source="chotot",
  details={"contact":"Thomas"}),

L(1217,"ho-chi-minh","bq","Квартира",7500000,60,
  "2-спальная квартира (1 с/у) в доме Chung cư Dầu Khí, Bình Quới, Bình Thạnh — 60м². Пустая (без мебели), заезд сразу. Подходит для семьи или компании друзей, долгосрочная аренда.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-binh-thanh-tp-ho-chi-minh/134292834.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Phước Đăng Khoa"}),

L(1218,"ho-chi-minh","bq","Дом",3500000,50,
  "Отдельно стоящий дом в переулке 480 (Hẻm Gà Nướng Bảy Đực), Bình Quới, Bình Thạnh, на территории большого частного земельного участка — 1 спальня, гостиная, санузел, маленькая кухня. Тихо, зелено, вид на Landmark 81 и высотки Q2.",
  "https://www.nhatot.com/thue-nha-dat-quan-binh-thanh-tp-ho-chi-minh/134291718.htm","сегодня",0,source="chotot",
  details={"notice":"в структурном поле площадки ошибочно указана площадь 10000м² (это площадь всего участка комплекса из текста объявления, не самого юнита); по тексту размер блока 5×10м = 50м²","contact":"Cô Thảo"}),

L(1219,"ho-chi-minh","bth","Студия",7500000,35,
  "Апартамент в центре Q1 — 35м², светлая просторная комната, полная новая меблировка, большой подземный паркинг, лифт.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134291185.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении не указан точный адрес","contact":"Kiều Nga Megas"}),

L(1220,"ho-chi-minh","bth","Студия",11000000,25,
  "Студия 25-30м² в районе Nguyễn Thái Bình, Q1 — полная меблировка, отдельная кухня, стиральная машина, свой балкон, лифт, бесплатная парковка. Рядом рынок Bến Thành, Saigon Centre, пешеходная Nguyễn Huệ, Дворец Независимости. Своя разводка электричества (по счётчику), вода 150 000₫/чел.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134288291.htm","сегодня",0,source="chotot",
  details={"notice":"диапазон цены в объявлении 11-13 млн ₫/мес за 25-30м² в зависимости от конкретной комнаты, взята нижняя граница (структурное поле)","other_fees":"вода 150 000 ₫/чел., парковка бесплатно","contact":"Việt Lương Quốc"}),

L(1221,"ho-chi-minh","bth","Студия",5000000,24,
  "Мини-квартира на 134 Trần Hưng Đạo, Bến Thành, Q1 — от собственника, без комиссии. Полная меблировка, заезд сразу. Рядом школы, больница, Bến Thành, Bùi Viện.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134285592.htm","сегодня",0,source="chotot",
  details={"contact":"Mây (chính chủ)"}),

L(1222,"ho-chi-minh","bth","Дом",14000000,40,
  "Дом целиком, 2 спальни/4 с/у, ул. Nguyễn Thái Bình, Q1, у моста Calmette (тупиковый переулок, дом в самом конце) — 1 этаж + 2 этажа + терраса на крыше, кондиционер в каждой комнате, двор на 3 байка, тупик проезжий для машины. Северо-западная ориентация. Договор на 2 года.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134280462.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении отмечено «подходит для семьи или онлайн-бизнеса»"}),

L(1223,"ho-chi-minh","kh","Квартира",19000000,54,
  "1-спальная квартира 54м² в ЖК Millennium, Khánh Hội, Q4 — вид на реку, освобождается в сентябре. Полная современная меблировка, дом ухоженный. Бассейн-инфинити, спортзал, зона BBQ, парк в комплексе, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134287137.htm","сегодня",0,source="chotot",
  details={"contact":"hà pihomes"}),

L(1224,"ho-chi-minh","kh","Студия",12000000,31,
  "Студия с балконом 31м² (1 спальня, 1 с/у) в ЖК Masteri Millennium, Khánh Hội, Q4 — полная меблировка. Бесплатный доступ к бассейну, спортзалу и другим удобствам комплекса.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134284028.htm","сегодня",0,source="chotot",
  details={"contact":"Căn hộ giá tốt Quận 4"}),
L(1225,"ho-chi-minh","th","Дом",15000000,78,
  "Дом целиком на переулочной улице рядом с Lotte Mart — 1 этаж+1 этаж, 3x26м (78м²), 3 спальни/3 с/у. Рядом рынок Тан Куи, ун-т Тон Дык Тханг, мост Кэнь Тэ.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134292844.htm","сегодня",0,source="chotot",
  details={"contact":"Đặng Trung Hậu"}),

L(1226,"ho-chi-minh","th","Квартира",5500000,35,
  "Дуплекс с антресолью рядом с Lotte Mart, TDTU и RMIT — 35м², полная меблировка, окна, вход по отпечатку пальца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134291760.htm","сегодня",0,source="chotot",
  details={"contact":"MỸ HƯƠNG"}),

L(1227,"ho-chi-minh","tm","Дом",8000000,24,
  "Дом целиком в переулке 167 ул. Phạm Hữu Lầu, в 50м от проезжей части, рядом с Фу Ми Хынг — 3x8м (24м²), 1 этаж+1 этаж, балкон, 2 спальни/2 с/у. Новый дом, никто ещё не жил.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134289080.htm","сегодня",0,source="chotot",
  details={"duplicateOf":1046,"contact":"Nguyễn duy tú"}),

L(1228,"ho-chi-minh","bth","Дом",182000000,117,
  "Дом на красной линии ул. Nguyễn Công Trứ, Q1, от собственника — 4,5x23м (117м²), 1 этаж + 5 этажей, 10 комнат.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134283541.htm","вчера",1,source="chotot",
  details={"notice":"крупный масштаб (10 комнат, депозит 540 млн ₫) — похоже на объект под гостевой дом/инвестицию, а не типовую семейную аренду; указано честно как есть","contact":"Phi Nguyễn"}),

L(1229,"ho-chi-minh","th","Дом",15000000,78,
  "Дом на красной линии, ул. Số 04 (старый район Tân Kiểng, ныне Tân Hưng) — 3x26м, сужается к 5,5м вглубь (форма «желудка» по фэн-шуй), 1 этаж+1 этаж, 3 спальни/3 с/у, отдельная комната для алтаря. Рядом рынок Tân Quy, Lotte Mart, больница Tâm Anh, мост Kênh Tẻ.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134281528.htm","вчера",1,source="chotot",
  details={"notice":"в объявлении цена ошибочно указана со знаком доллара «$15.000.000»; по контексту это вьетнамские донги, не доллары; действует договор аренды по этой цене, торг не предполагается","contact":"Zara Tâm An"}),

L(1230,"ho-chi-minh","th","Студия",5500000,40,
  "Студия и дуплекс с балконом в центре Куан 7, рядом Lotte Mart, RMIT, TDTU — 40м², полная меблировка, своя стиральная машина, заезд сразу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134280507.htm","вчера",1,source="chotot",
  details={"contact":"Trần Văn"}),

L(1231,"ho-chi-minh","kh","Квартира",11000000,68,
  "Квартира 2 спальни/1 с/у с 2 балконами на ул. Tôn Thất Thuyết, Q4 — 68м², полная меблировка, своя стиральная машина, угловая квартира. Рядом университеты Luật и Nguyễn Tất Thành, Q1/Q5/Q7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134278124.htm","вчера",1,source="chotot",
  details={"contact":"Thanh Phú HiFriendz"}),

L(1232,"ho-chi-minh","th","Квартира",6900000,30,
  "Дуплекс в пешей доступности от Lotte Mart, рядом ун-ты Tôn Đức Thắng, RMIT, Tài chính-Marketing — 30м², рядом промзона Tân Thuận, Eco Green, рынки Tân Quy и Tân Mỹ.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134272313.htm","вчера",1,source="chotot",
  details={"contact":"Thanh Trúc hình thật giá thật"}),

L(1233,"ho-chi-minh","bth","Квартира",7000000,35,
  "Квартира на красной линии ул. Trần Hưng Đạo, Bến Thành, Q1 — 35м², полная меблировка, удобно добираться до Q1/Q4/Q5/Bình Thạnh. Электричество и вода по гостарифу.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134270103.htm","вчера",1,source="chotot",
  details={"notice":"по тексту объявления подходит и для небольшого бизнеса (маникюр/спа/парикмахерская) на дому — указано честно как доп. опция","contact":"Nguyễn Văn Ước"}),
L(1234,"ho-chi-minh","tm","Комната",3500000,16,
  "Комната 4x4м в доме на ул. Phạm Hữu Lầu (Q7, район рынка Tân Mỹ) — железная лестница, без кондиционера. Хозяйка сдаёт 2 комнаты в доме: эта дешевле (3,5 млн, без кондиционера), вторая дороже (4,5 млн, с кондиционером на верхнем этаже). Приоритет студентам или семье из 3 человек с 2 мотобайками.",
  "https://www.nhatot.com/thue-phong-tro-quan-7-tp-ho-chi-minh/134294038.htm","сегодня",0,source="chotot",
  details={"contact":"BĐS TPLAND"}),

L(1235,"ho-chi-minh","bth","Дом",40000000,33,
  "Дом на ул. Tôn Thất Tùng (Q1) — этаж 33м², 6 уровней (первый этаж, антресоль и 4 этажа), 3 спальни/4 с/у.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134244968.htm","2 дня назад",2,source="chotot",
  details={"notice":"хозяин разрешает любой вид бизнеса на первом этаже наравне с проживанием","contact":"binh Ta"}),

L(1236,"ho-chi-minh","tm","Дом",30000000,80,
  "Дом на Đường Số 14 рядом с рынком Tân Mỹ (старый район Tân Phú, Q7) — 80м² (4x20), 3 этажа, 5 спален.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134244463.htm","2 дня назад",2,source="chotot",
  details={"duplicateOf":873,"contact":"Phạm Tăng"}),
L(1237,"ho-chi-minh","th","Студия",6000000,30,
  "Студия 30м² с балконом на Đường số 2 (Q7, старый район Тân Phong, новый Tân Hưng) — новое окно (полностью переделано), полная меблировка, тихий охраняемый ЖК. Напротив RMIT и TDTU (~5 мин пешком).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134296236.htm","сегодня",0,source="chotot",
  details={"notice":"в цену не входит только электричество","contact":"Hang Pham"}),

L(1238,"ho-chi-minh","th","Студия",6200000,25,
  "Мини-квартира 25м² в квартале Tân Quy (новый Tân Hưng) рядом с университетами TDTU, UFM, NTTU, UL, Q7 — полная меблировка, большие окна, круглосуточная охрана, подземный паркинг со входом по отпечатку пальца, лифт.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134295718.htm","сегодня",0,source="chotot",
  details={"notice":"не более 2 человек и 2 мотобайков","contact":"Duy CHDV HiFriendz"}),

L(1239,"ho-chi-minh","th","Дом",18000000,72,
  "Дом на фасаде улицы в районе Tân Hưng, Q7 — участок 4×18м (72м²), 1 этаж + 1 этаж, 3 спальни, 3 с/у.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134295688.htm","сегодня",0,source="chotot",
  details={"notice":"цена договорная (заявлено 18 млн), хозяин допускает проживание и бизнес/офис компании","contact":"Nguyễn Hoa"}),

L(1240,"ho-chi-minh","th","Дом",8000000,28,
  "Дом в переулке 861/72/11 ул. Trần Xuân Soạn (Q7, район Tân Hưng), 28м², 3 спальни.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134295028.htm","сегодня",0,source="chotot",
  details={"notice":"объявление от риелтора, комиссия 0,5 месячной аренды","contact":"Phạm Quang Viễn"}),

L(1241,"ho-chi-minh","tm","Квартира",15000000,186,
  "Квартира 186м² (1 этаж + антресоль), 3 спальни, 3 с/у в ЖК Belleza, ул. Phạm Hữu Lầu, Tân Mỹ (Phú Mỹ Hưng), Q7 — 2 кондиционера, 2 водонагревателя.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134295630.htm","сегодня",0,source="chotot",
  details={"notice":"заезд с начала октября 2026","contact":"Trần Thị Thu Hà"}),

L(1242,"ho-chi-minh","tm","Квартира",35000000,125,
  "Угловая квартира 125м², 3 спальни, 2 с/у в ЖК Green Valley, ул. Tôn Dật Tiên, Phú Mỹ Hưng — 3 балкона, машиноместо в подземном паркинге, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134294275.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng Trúc Loan"}),

L(1243,"ho-chi-minh","ak","Квартира",9500000,40,
  "Квартира 40м², первый этаж, на Đường Số 13, An Khánh (старый Q2) — 1 спальня, отдельная кухня, полная меблировка, кондиционер, место для машины, разрешены животные.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134296087.htm","сегодня",0,source="chotot",
  details={"contact":"House Center"}),

L(1244,"ho-chi-minh","ak","Дом",80000000,160,
  "Дом 8×20м, 1 этаж + 2 этажа, 7 спален, 4 с/у, полная меблировка, ул. Nguyễn Văn Hưởng (204B7), Thảo Điền.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134294852.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении упомянута возможность использования под офис/бизнес наравне с проживанием (не спутать с виллой 250м²/5 спален на той же улице, уже в базе)","contact":"Lan Đào"}),

L(1245,"ho-chi-minh","ak","Дом",10000000,50,
  "Дом 35/5A, ул. số 59, Thảо Điền — 1 этаж + 1 этаж, всего ~50м² (внизу гостиная/кухня/санузел, наверху спальня с кондиционером и санузлом). Тихий безопасный переулок рядом с рынком, школами, ТЦ.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/134271284.htm","сегодня",0,source="chotot",
  details={"notice":"структурное поле площадки даёт 25м² (видимо, площадь одного этажа) — использована площадь из текста «tổng dt 50m²» как более полная","other_fees":"электричество и вода по счётчику отдельно","contact":"Ngọc"}),

L(1246,"ho-chi-minh","bq","Квартира",10000000,75,
  "Квартира 75м², 2 спальни, 2 с/у на ул. Phan Văn Trị (Thanh Đa / Bình Quới) — лоджия для сушки белья, балкон в гостиной, лифт по карте, охраняемый дом. При въезде: 2 кондиционера, водонагреватель, индукционная плита.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-binh-thanh-tp-ho-chi-minh/134295958.htm","сегодня",0,source="chotot",
  details={"notice":"депозит 1 месяц","contact":"Lê Bích"}),
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
L(1271,"ho-chi-minh","tm","Квартира",4500000,36,
  "1-спальная квартира, 36м², ЖК Chung cư Tân Mỹ, ул. Nguyễn Lương Bằng, Tân Mỹ — без мебели, лифт, рядом рынок (50м), школа, полиция района.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134305208.htm","сегодня",0,source="chotot",
  details={"contact":"Bich Tram","photos":["https://cdn.chotot.com/DHk9imCpriLaIwXWkQVAf_B7_Mvr5oX5_TwsjX9WMY4/preset:view/plain/feff17fcd8e4465258f846818261645a-2998855843620637474.jpg","https://cdn.chotot.com/zTCIRhjCZG6gyXRD6_ho5cyvuRzrQYJ6oKq-NpwQGiw/preset:view/plain/9bb8f26c18c9beced41270087178834d-2998855843676368963.jpg"]}),

L(1272,"ho-chi-minh","tm","Дом",21000000,64,
  "Угловой дом 4×16м (64м²), новый (100%), переулок 1422 Huỳnh Tấn Phát, Tân Mỹ — 1 этаж + 2 этажа + терраса, 3 спальни/3 с/у, полная меблировка (диван, кровати, шкафы, кондиционеры).",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134305144.htm","сегодня",0,source="chotot",
  details={"contact":"Mr Ngọc","photos":["https://cdn.chotot.com/RJPBqSdC4pOVmtnQeelEUanYnEG06W852sP3lWwZ2K4/preset:view/plain/c76def76c1e8dbb93dfdfb134a912556-2998855137948435027.jpg","https://cdn.chotot.com/IkVnN8Soi8ZxJ8Fv-61CGYvcDvuSvPrNZWCxW-zl_PY/preset:view/plain/b69d46a66e046d8c8597222eb7f04d1d-2998855137899751443.jpg"]}),

L(1273,"ho-chi-minh","tm","Квартира",35000000,132,
  "4-спальная квартира (3 с/у), 132м², ЖК Sunshine Sky City, ул. Phú Thuận, Tân Mỹ — полная меблировка, рядом Phú Mỹ Hưng, Crescent Mall.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134304819.htm","сегодня",0,source="chotot",
  details={"contact":"Huy","photos":["https://cdn.chotot.com/WY0cbEh0WPxpTiTafoXRas97zmjA_T4fY2N1lTe72-s/preset:view/plain/57ab107e69dc0a2c0597ba1d3aa69be3-2998854254263371602.jpg","https://cdn.chotot.com/kbZS5n7kJh0fOXT1QAelZcqfguwpuhdcWdjP-NOa1e0/preset:view/plain/5aad3212279b82b13adb616304e45625-2998854254804126498.jpg"]}),

L(1274,"ho-chi-minh","th","Квартира",13000000,50,
  "2-спальная квартира, 50м², ЖК Sunrise Riverside, Tân Hưng — в квартале Phú Mỹ Hưng, охрана 24/7, полная меблировка, рядом Lotte Mart и рынок.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134304426.htm","сегодня",0,source="chotot",
  details={"contact":"Châu Thành Đạt","photos":["https://cdn.chotot.com/NqqRFS0ptGdvaLkFpiYM04YFrIpFzgTFv2ozVzjgYlY/preset:view/plain/2a8ecf07cdcb1596bab34afd28e906ad-2998851711972290969.jpg","https://cdn.chotot.com/rgTJFJlD844VamTHJVeXd-Sw5QNQU5sZzTJ-DWxXxDg/preset:view/plain/c1ea105fae85d17c321f61da2eba2a69-2998851711957743116.jpg"]}),

L(1275,"ho-chi-minh","tm","Квартира",10000000,75,
  "2-спальная квартира (2 с/у), 75м², ЖК Sunshine Sky City, Tân Mỹ — рядом Phú Mỹ Hưng, удобно до Q1/Q4, полная меблировка, возможна скидка на управляющий сбор.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134304322.htm","сегодня",0,source="chotot",
  details={"contact":"Đức Anh BĐS Triệu Đô","photos":["https://cdn.chotot.com/WrIMsuqJTAQeID9oRMKH96t3T0qWLE05e7ktVgzY7E0/preset:view/plain/1d30fdbcb8c2939a852d22a08d029c66-2998851425032031116.jpg","https://cdn.chotot.com/3x59eNByRLgulTMRGuGQf4ZI6fDFVO_BRsrYFr9WeRc/preset:view/plain/a0cf4f617e40611b0e47565e2463c63a-2998851425082124307.jpg"]}),

L(1276,"ho-chi-minh","tm","Квартира",17000000,100,
  "3-спальная квартира (3 с/у), 100м², ЖК Sunshine Sky City, ул. Phú Thuận, Tân Mỹ — заселение в сентябре, 2 года без платы за управление, панорамные окна, вид на р. Сайгон.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134304282.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Văn Thanh","photos":["https://cdn.chotot.com/hhX8luPEEzcAkfFf0c4dc9TpchkXHWhRJShOwsv5I6w/preset:view/plain/7e7d93afadd9033d4995b8feed39460b-2998851503931949651.jpg","https://cdn.chotot.com/4azXjnoGYPSYum41POTvWRksxV_Jqu8FM3tdfYtYh1s/preset:view/plain/597aa3223e632c7f1a71fc97fe208a06-2998851503704213330.jpg"]}),

L(1277,"ho-chi-minh","tm","Квартира",13000000,85,
  "2-спальная квартира (2 с/у) с балконом, 85м², ЖК Era Town/Đức Khải, блок A1, ул. 15B Nguyễn Lương Bằng, Tân Mỹ — вид на реку, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134301792.htm","сегодня",0,source="chotot",
  details={"contact":"Quang Huy","photos":["https://cdn.chotot.com/QNKS7ZzY_h73JVfILKqyYy0syHdUoJIxc0kEnTgoDOU/preset:view/plain/823a0e6e4ea7b7f2e33864b5bdaab44d-2998835425746454354.jpg","https://cdn.chotot.com/rBDmqZcPmb0rNrzw9N2cp2NbvBjjH8oBOb-jUmfdtIM/preset:view/plain/81336c9c2aed27bc2da2bf35663f1709-2998835426736375634.jpg"]}),

L(1278,"ho-chi-minh","th","Студия",6000000,30,
  "Новая студия с окном/балконом, 30м², ул. D4, Tân Hưng — только что построено, никто ещё не жил, полная меблировка, можно с животными, рядом Lotte Mart, UFM, TDTU, пешком до RMIT.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134299791.htm","сегодня",0,source="chotot",
  details={"contact":"Đạt Nguyễn","photos":["https://cdn.chotot.com/dAzLgIFiir11R1jvzqAvm-lLPILgzplL4JVbS4zpLdA/preset:view/plain/73bdc4f135dc011bf8de16c8e19e537b-2998774111785030973.jpg","https://cdn.chotot.com/gs6KPMP552DKGA0UoGm7kRCeTrWKxaCRTE4lvvQ3IJI/preset:view/plain/e54268f0d0e1c9b9c8191fc667c1778a-2998774111878269093.jpg"]}),

L(1279,"ho-chi-minh","th","Комната",4500000,15,
  "Комната 3×5м, 15м² (санузел отдельно, окна + световой люк), пер. 793/28 Trần Xuân Soạn, Tân Hưng — кондиционер, диван-кровать, шкаф, холодильник, стиральная машина и кухня общего пользования; рядом Lotte Mart Q7.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134299781.htm","сегодня",0,source="chotot",
  details={"contact":"THẮNG NHÀ ĐẸP 78","photos":["https://cdn.chotot.com/PYt-pe8tVcuAQBG3oas-a_5vzHXfWbL_MXb1ek_IwGc/preset:view/plain/894b3a4f377707586ce321eb40db8a49-2998855932318064787.jpg","https://cdn.chotot.com/37CX2V5ZqzNqa5D8UXt8EQustoai6lpoxcPKe-oATm4/preset:view/plain/eff01da6569015183d7766e33ec64582-2998855932490992418.jpg"]}),

L(1280,"ho-chi-minh","tm","Студия",3000000,15,
  "Студия на 2 этаже, 15м², ул. Huỳnh Tấn Phát, Tân Mỹ — отдельный санузел, кондиционер, свободный график, электронный замок, можно с животными.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134289373.htm","сегодня",0,source="chotot",
  details={"contact":"Thảo Duyên Văn Thị","photos":["https://cdn.chotot.com/gp7PG9k_7IinV--4yPkYOSib-6Ahjgywu9r9Air4_Yo/preset:view/plain/ad14c7344330e85a0226d53270cf23d2-2998713741169559378.jpg","https://cdn.chotot.com/be5z9OmocG2XeNYxNhmF3eVZnIUJ_5k67IQhWdLAVFY/preset:view/plain/a03d837e2cbcaa5976150bb4ddf826a4-2998713741160541539.jpg"]}),

L(1281,"ho-chi-minh","th","Студия",5500000,27,
  "Мини-квартира, 27м², ул. Mai Văn Vĩnh, Tân Hưng — новая, большой балкон, свободный график, охрана 24/7, залог 1 месяц, можно с животными; рядом TDTU, RMIT, Crescent Mall.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134287864.htm","сегодня",0,source="chotot",
  details={"contact":"Đức Huy Chuyên Cho Thuê Căn Hộ Quận 7","photos":["https://cdn.chotot.com/FhrTrxbSqqWvEUGjZ4BUs7zwf4H4w_anAmFYE6By3PI/preset:view/plain/0646394fb210dc6a87c019dece5520cb-2998708116630286745.jpg","https://cdn.chotot.com/hKMWqsRakllUfZeZHnghc9Sy5uxL8eKH28uJZp_QKkM/preset:view/plain/ad0b4d185aefd567ee02c6c4de52fd9e-2998708117035911323.jpg"]}),

L(1282,"ho-chi-minh","tm","Студия",6200000,50,
  "Угловая студия с видом на реку, 50м², ЖК Era Town/Đức Khải, ул. 15B, Tân Mỹ — полная меблировка, залог 1,5 месяца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134281943.htm","вчера",1,source="chotot",
  details={"contact":"Lê Tú","photos":["https://cdn.chotot.com/MBSplpvayqC5j7nw6fdQgj_bZ7D32nSBVP8a__Z4NCk/preset:view/plain/7a2d25888b6d585359b4b053d726c6e5-2998627885769444236.jpg","https://cdn.chotot.com/HTrEULeuUgrpIyA6ufMdJ2jydCZ6Z224qcUCqec4eQw/preset:view/plain/940b36a65cc814fe2a1465ab2a1905e9-2998627885775350741.jpg"]}),

L(1283,"ho-chi-minh","tm","Квартира",8000000,67,
  "2-спальная квартира (2 с/у), 67м², блок B, ЖК Era Town/Đức Khải, ул. Nguyễn Lương Bằng, Tân Mỹ — охрана 24/7, доступ по карте, автобус №139 у дома.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134267869.htm","2 дня назад",2,source="chotot",
  details={"contact":"Quang Huy","photos":["https://cdn.chotot.com/B-kQTUokkk9TbFoHV0wYTHI_dve6JzHnRz8XJLspakY/preset:view/plain/b659129455c348e6ff1252ccd4ac70ea-2998557567747982061.jpg","https://cdn.chotot.com/AVWpF2fQgnWATKbytC5xVf8uiO1wswMYb4pBp5ktyS8/preset:view/plain/3ba3d8a025d5f57a0695d046318d1c2d-2998557567608607665.jpg"]}),

L(1284,"ho-chi-minh","th","Комната",4800000,25,
  "Новая комната, 25м², ул. Nguyễn Văn Linh, Tân Hưng — балкон, окно, полная меблировка, вход по отпечатку пальца, рядом TDTU, RMIT.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134262011.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phương Hoài Bảo","photos":["https://cdn.chotot.com/uffrnF3EnA18zlI91bf3AWDO5WnNn7t6v4G2UWL8HYw/preset:view/plain/a9a2188a41c622f354f74569c09141c5-2998484088118460533.jpg","https://cdn.chotot.com/YasxPFxpmETkd2PUB8zcDC7SV8z1koqV9vX3lEy7jvE/preset:view/plain/ece83378c7c55ca9b4d45c774e145676-2998484088599740569.jpg"]}),

L(1285,"ho-chi-minh","tm","Квартира",12000000,161,
  "3-спальная квартира (4 с/у), 161м², ЖК Era Town, ул. 15B, Tân Mỹ — без мебели, просторная, подходит для большой семьи.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134254910.htm","2 дня назад",2,source="chotot",
  details={"contact":"BĐS HƯNG PHÚC","photos":["https://cdn.chotot.com/cToAkHN7dg3vUwF6QCIFx0P-IiYZTLpbUzqtwEFXhqg/preset:view/plain/b41e8c40b87f871d445c7879bfcc9d82-2998444171213568159.jpg","https://cdn.chotot.com/BZi84JLTwUU34PphtxXJzhdpZ2oeVtElZ0rThDjZmKI/preset:view/plain/9724edb9c4c73340fd3486bd7f8ae326-2998444171225412653.jpg"]}),

L(1286,"ho-chi-minh","tm","Квартира",9000000,90,
  "2-спальная квартира (3 с/у), 90м², ЖК Era Town/Đức Khải, ул. 15B Nguyễn Lương Bằng, Tân Mỹ — отдельная кухня, просторная гостиная, рядом Phú Mỹ Hưng.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134242523.htm","3 дня назад",3,source="chotot",
  details={"contact":"Hồ Phan Huy Châu","photos":["https://cdn.chotot.com/xEEVy5eQlvyMFUcJugmBl7A-8IitpZ9NJQt6V0_wlCA/preset:view/plain/daaf0bfbb9ff5212172365aaf3adf589-2998342302185881753.jpg","https://cdn.chotot.com/7b9d47bmWlJgbAxArnYXMFp0UyWay4tOGAPF7lxMxoY/preset:view/plain/6c8a9a9191201780fedb6967fd2d5dc7-2998342302191748946.jpg"]}),

L(1287,"ho-chi-minh","th","Студия",5000000,40,
  "Студия-дуплекс, 40м², ул. Nguyễn Thị Thập, Tân Hưng — полная меблировка, лифт, дом не подтапливает, оплата только за электричество, свободный график; рядом мосты Phú Mỹ и Tân Thuận.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134240006.htm","3 дня назад",3,source="chotot",
  details={"contact":"Trần Văn","photos":["https://cdn.chotot.com/KvzAQwXj1hMASCD6OvG1Z3p9tACgW1Ed1Pj3NcXoQP4/preset:view/plain/bfe2ee38d6aec23c93ed6eae4bb78f78-2998313180331507865.jpg","https://cdn.chotot.com/BJNe_QfyTwX3LeaHijAXnRPgQrMxF_V_NNI67-gp0vs/preset:view/plain/fe857e7eb485b499c287bfb998145fcf-2998313180467860849.jpg"]}),

L(1288,"ho-chi-minh","ak","Квартира",20000000,79,
  "3-спальная квартира (2 с/у), 79м², ЖК Paris Hoàng Kim, ул. Lương Định Của, An Khánh — средний этаж, вид на Landmark 81 и р. Сайгон, полная меблировка, тихо.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134236579.htm","3 дня назад",3,source="chotot",
  details={"contact":"Phạm Minh Lãnh","photos":["https://cdn.chotot.com/rGiYXN7rj3S-8nvOXVcrt2rwbTuY3GRZO2UqnsVrNUc/preset:view/plain/0ef62af7d0650d8254af4af216497722-2998308042877470546.jpg","https://cdn.chotot.com/wJk4QbFcd1J9ci07va56GjfqvsBoZTI-16On0HzsYfo/preset:view/plain/f384cafda719ebfb6db0b89b10e5d343-2998308042842740081.jpg"]}),

L(1289,"ho-chi-minh","tm","Квартира",11500000,90,
  "3-спальная квартира (2 с/у) с видом на реку, 90м², ЖК Era Town/Đức Khải, ул. 15B Nguyễn Lương Bằng, Tân Mỹ — просторная, подходит для семьи (тот же агент, что и юнит 9tr/90м² выше, другая планировка).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134236330.htm","3 дня назад",3,source="chotot",
  details={"contact":"Hồ Phan Huy Châu","photos":["https://cdn.chotot.com/HIpqPIC1DQsGQ1AVK0gUKhFvfZPsGLjqDuNEMmCZVm4/preset:view/plain/dcaecc7fd73ed4a62f046cce5837c991-2998306759803329651.jpg","https://cdn.chotot.com/Kz4eYbyv7m5Ws23MIm0ubcSTU7aCZCMSfCwkD8HM-Eo/preset:view/plain/7635ad99c3c1856dfc139db8f4ae5b47-2998306760093565464.jpg"]}),

L(1290,"ho-chi-minh","th","Студия",7500000,35,
  "Новая студия в здании сервисных апартаментов (CHDV), 35м², ул. 71, Tân Hưng — полная меблировка (не была в использовании), лифт, большой паркинг, пожарная сигнализация; рядом KCX Tân Thuận, TDTU, RMIT.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134234673.htm","3 дня назад",3,source="chotot",
  details={"contact":"Nguyễn Bá Thiên Lân","photos":["https://cdn.chotot.com/mwRA7nBYTRgNAAov8qi0N6GhaKlTuTueeFKgnq8FGcE/preset:view/plain/cf2e91b02594727e01fd4928b8a6fd46-2998299527839716721.jpg","https://cdn.chotot.com/ZkC30sknhWaThK0NvbDOJEcoNO-hEJxD_8kLbdAM8nA/preset:view/plain/cd86129546e152d519bdcde48cee0503-2998299527745423683.jpg"]}),
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
L(1301,"da-nang","tk","Квартира",6000000,45,
  '1-спальная квартира в новостройке, 45м², ул. Nguyễn Tất Thành (Thanh Khê) — полная меблировка (диван, холодильник, кондиционер, кухня), балкон, рядом медцентр, администрация района, школы, супермаркет. В доме бассейн, лифт, охрана, парковка.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134305439.htm","сегодня",0,source="chotot",
  details={'contact': 'Văn Vĩnh Duy', 'photos': ['https://cdn.chotot.com/Nbw-fuuUkrQuFnq7YvQUTq_MyRBDQmGOVt8Cfzlk7s0/preset:view/plain/f099da1e4def2bac101dd8e8630ba590-2998856851644364300.jpg', 'https://cdn.chotot.com/ydFb_iDFVNnCyNeme3_6zpG8BVVez3M97dEXmiqrmSM/preset:view/plain/b3998516d930b20e206f075982e17bd3-2998856852098829090.jpg']}),

L(1302,"da-nang","hcg","Квартира",17000000,70,
  '2-спальная квартира B2-2-22 в ЖК на ул. Hóa Sơn 8 (Hòa Cường) — полная меблировка, отдельные стиральная и сушильная машины, тренажёрный зал в доме, просторная терраса на крыше.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134304686.htm","сегодня",0,source="chotot",
  details={'contact': 'HAVILAND CĂN HỘ GIÁ TỐT', 'photos': ['https://cdn.chotot.com/Q_EH27eORQtbaC2Rvp2m2EuRHtaS8rdCKbq2-21y6GI/preset:view/plain/f741b315308b7343e4da5c450124a28b-2998853598770946268.jpg', 'https://cdn.chotot.com/tqHY_A97APEm33hXF4laztKx5Rs6qlKtzL3gO_oqJS4/preset:view/plain/3fcd322c184e9d415e9cf9c900331a39-2998853594689939475.jpg']}),

L(1303,"da-nang","ns","Дом",17000000,52,
  'Дом целиком 3 этажа на ул. Ngũ Hành Sơn (Mỹ An) — участок 52м², общая площадь 156м², гостиная, 3 спальни, столовая, кухня, 2 с/у. Базовая мебель, рядом Университет экономики Đà Nẵng.',
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134304453.htm","сегодня",0,source="chotot",
  details={'notice': 'в объявлении отмечено удобное расположение и для проживания, и для бизнеса', 'contact': 'THANH', 'photos': ['https://cdn.chotot.com/HSlfLUhKBZhqjfpemTQqotPsVHLcHPxYaeKDwXb79CA/preset:view/plain/3351ab86f002d9628bb8fc106453c42b-2998852264551557139.jpg', 'https://cdn.chotot.com/rpgEL4ODfOYpb0DbsEbvaCJFMFwhSLkS7mtYtMHn4C8/preset:view/plain/1937657b83ae60184b3ce66e6e54fa85-2998852264329988898.jpg']}),

L(1304,"da-nang","hk","Дом",15000000,110,
  'Дом целиком 3 этажа рядом с ул. Hoàng Văn Thái (Hòa Minh) — 110м², 3 спальни/4 с/у, гостиная, кухня, терраса на крыше, место для сушки белья и парковки. Полная меблировка, цена по договорённости.',
  "https://www.nhatot.com/thue-nha-dat-quan-lien-chieu-da-nang/134304253.htm","сегодня",0,source="chotot",
  details={'notice': 'передача дома — середина сентября 2026', 'contact': 'Nhà Xanh', 'photos': ['https://cdn.chotot.com/p9ZZKYvTaGMfl-Tz1bvupvngMPAwoTxEsNcFWl7A2oo/preset:view/plain/5d101a1f338e7cf44b57905b56ac53b5-2998851384097802066.jpg', 'https://cdn.chotot.com/Adn9qiuWPFonGNNSFCGtc7gDf3k_3IdeaMR9X6lBcXI/preset:view/plain/22bb8aa27c51d7fa8f82a03dcd19666f-2998851384161087555.jpg']}),

L(1305,"da-nang","ah","Дом",20000000,110,
  'Дом целиком 3 этажа на ул. Cao Bá Nhạ (An Hải Bắc) — 110м², 3 спальни + рабочий кабинет, 4 с/у, большая гостиная, кухня, просторный двор и терраса на крыше. Полная меблировка (4 кондиционера, водонагреватели, ТВ, холодильник Samsung side-by-side, СВЧ, стиральная машина).',
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134303876.htm","сегодня",0,source="chotot",
  details={'notice': 'площадь по тексту объявления 110м², в структурном поле площадки — 100м²', 'contact': 'BÌNH CAPITAL', 'photos': ['https://cdn.chotot.com/QksbRKMVAIBilV2GTvfHK4scsPgO1_CSwmq3MjfigoQ/preset:view/plain/393aa814e2af70226a6a9410125eb740-2998849341468849676.jpg', 'https://cdn.chotot.com/xTF61xmbF3N5TbpKG9CTfLL67s512P8QHZlRSoEs4ns/preset:view/plain/9c8213fc8f215c18c2232c591333bbc9-2998849341310732114.jpg']}),

L(1306,"da-nang","ah","Квартира",7000000,45,
  'Меблированная квартира современного дизайна на ул. An Đồn 5 (An Hải Bắc) — рядом мост Sông Hàn и Vincom (500 м), около 1 км до парка на берегу моря.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134303835.htm","сегодня",0,source="chotot",
  details={'contact': '1W05.Lê Phan Cẩm Ly', 'photos': ['https://cdn.chotot.com/ulqJXSoXi2ViI4M-6gBkqhLXZ-521k9GJhXSEo4m8G8/preset:view/plain/ef12135a06baa348ea533c289573e4fe-2998848988846654035.jpg', 'https://cdn.chotot.com/pKEF348xmBrzqOxwHPX3cBDKl1wrh39Sbv_h1LUE7JY/preset:view/plain/e718cb383973821c69325f0e46a9dd69-2998848988743540883.jpg']}),

L(1307,"da-nang","tk","Студия",6000000,30,
  'Студия с двумя фасадами и балконом на ул. Đoàn Nhữ Hài (Hòa Khê) — полная меблировка, своя стирально-сушильная машина, отдельный wifi.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134303411.htm","сегодня",0,source="chotot",
  details={'notice': 'последняя свободная комната в доме', 'contact': 'Bùi Đoàn Tiến', 'photos': ['https://cdn.chotot.com/a9XTKHrBX1gUfp6E9ghJH0sFTRriNUIuWTxptCTIm80/preset:view/plain/eebb9eff34b21a1647a65724bd4f0e5a-2998846066671108133.jpg', 'https://cdn.chotot.com/ug13I6ORrd9algbCLznKcOX-XVlEggRdCvQsiBDwZos/preset:view/plain/9961b9d89077b6d7f0b44d420640fa87-2998846066730510355.jpg']}),

L(1308,"da-nang","ns","Квартира",8500000,35,
  'Квартира с балконом на ул. An Thượng 4 (Mỹ An) — 35м², 200 м до пляжа Mỹ Khê, полная меблировка, своя стиральная машина, принимают иностранцев и аренду от 1 месяца.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134303362.htm","сегодня",0,source="chotot",
  details={'contact': 'Ha for rent APT', 'photos': ['https://cdn.chotot.com/35z973GjTaev3-vJrIkeiAzs_aGlfBuox5IwilQ4KpU/preset:view/plain/bcec245a15ca689d3f6a18f3dd5b82b9-2998846463510742866.jpg', 'https://cdn.chotot.com/iPhr-5gwsvsVUYhagyzJ7but9pqtEmoBcHPa8FfSgxA/preset:view/plain/f1f5f0b760caa571468df4c1246f0666-2998846463379229474.jpg']}),

L(1309,"da-nang","ns","Дом",22000000,100,
  'Дом целиком 3 этажа на ул. Đa Phước 2, квартал Nam Việt Á (Khuê Mỹ) — 100м², 3 спальни/3 с/у, полная меблировка, у реки, тихий квартал.',
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134303217.htm","сегодня",0,source="chotot",
  details={'notice': 'цена по тексту объявления обсуждается; отмечена возможность использовать дом и под офис', 'contact': 'Trần Quân Land', 'photos': ['https://cdn.chotot.com/n53yLgT-NRKuRZKrP6qDdLjt9YXn7gU-tIj8lI0Fk0U/preset:view/plain/833995c38ff240cbb884c4f55a6bc837-2998846148761870556.jpg', 'https://cdn.chotot.com/aPvqsRaBZUpKPk82YfPPbN7_sk1jjE5WTtCyiPLF0HU/preset:view/plain/ad713b0cd58ee88b138896257bebeddc-2998846148718873378.jpg']}),

L(1310,"da-nang","tk","Дом",8000000,52,
  'Дом целиком в переулке 2,5 м, ул. Điện Biên Phủ (Chính Gián) — 52м², гостиная, 2 спальни, 1 с/у, кухня, кондиционер, вентилятор, стиральная машина. Рядом супермаркет Aeon и парк 29/3.',
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134302772.htm","сегодня",0,source="chotot",
  details={'notice': 'площадь по тексту объявления 52м², в структурном поле площадки — 80м²', 'contact': 'BÌNH CAPITAL', 'photos': ['https://cdn.chotot.com/gstjUPSpheQ2a7cwgb5M452QJJCXwl4HT8feYIVUK-s/preset:view/plain/88dac9571432c41ee889b741ae0f6cc1-2998843373276493354.jpg', 'https://cdn.chotot.com/L6gQGTTxh-Fe0FHGCYIyxZ6LnuOMqdoy0DlhLo1VT0E/preset:view/plain/0e3a6ac9b1c27bcac0ac2029cbad16b3-2998843373173230476.jpg']}),

L(1311,"da-nang","ns","Квартира",8000000,45,
  'Квартира с садом на ул. 26.5 (Hòa Hải), рядом Đại học FPT — 45м², 1 спальня, полная меблировка, подходит для 2-3 человек.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134302470.htm","сегодня",0,source="chotot",
  details={'notice': 'освобождается с 29 августа', 'contact': 'Phương Trang', 'photos': ['https://cdn.chotot.com/WmCVbjPOWck11GUV_OZQbEebxahce0MWolB4z4cXakM/preset:view/plain/9d1c7a88addda4367be4b0a75ec07949-2998841419304255273.jpg', 'https://cdn.chotot.com/GW6sKxCk6vcMKrhWjAKSGR4CXA_JWVIxxdpuBYtoKIo/preset:view/plain/e56218c949787f25bf721b613fca914c-2998841419267061260.jpg']}),

L(1312,"da-nang","ns","Студия",8000000,None,
  'Сервисная квартира-студия с отдельной спальней на Hói Kiểng 23 (Hòa Quý) — балкон, место для сушки белья, электронный замок с распознаванием лица, 3-5 минут до ĐH FPT/VKU/Làng Đại học, 7 минут до пляжа Mỹ Khê. Полная меблировка.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134299946.htm","вчера",1,source="chotot",
  details={'contact': 'Nhung Nguyen', 'photos': ['https://cdn.chotot.com/LkYyFQV_BM9nIw5-uR6mNl9IyZxV7n3p5iKn5ebLbEU/preset:view/plain/77236ebc87c19e6bfa4589ce452fbd4f-2998777248596364983.jpg', 'https://cdn.chotot.com/-txn830ewu_LvBjVChJFDNvz5eSVp2DfQiNKUUuhKp4/preset:view/plain/d435a697bb2afd3662b8b710c28eb16f-2998776460571783577.jpg']}),

L(1313,"da-nang","hx","Студия",6500000,22,
  'Новая студия/1-спальная квартира на ул. Nguyễn Sắc Kim (Hòa Xuân) — полная меблировка, своя стиральная и сушильная машина, на главной улице, принимают иностранцев, для 1-2 человек.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134299295.htm","вчера",1,source="chotot",
  details={'contact': 'Sơn Kim', 'photos': ['https://cdn.chotot.com/hCOb-4nexq27I-5FweNQKFSwUdmWihKTAT3z-Ht2E9E/preset:view/plain/2eb59b3f59a95c12c1dee0cb3e089195-2998769161448999077.jpg', 'https://cdn.chotot.com/DSELDMMukDY5fkWzsMpgWG9EH6xaXxnIB-hVnJsmZtY/preset:view/plain/eb92773df32e9fffab99b6ce9bf8b8ea-2998769160319593827.jpg']}),

L(1314,"da-nang","ns","Квартира",5000000,25,
  'Новая квартира (только что отделана) рядом с Đại học FPT (Hòa Hải) — полная меблировка, готова к заезду.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134299001.htm","вчера",1,source="chotot",
  details={'contact': 'Nhieu Phan', 'photos': ['https://cdn.chotot.com/5S0l87QiVflkF_hWTUrKGtms1huCecI2nPpx1bDby14/preset:view/plain/0e197163f2aff5abdb5d2898a26dafe5-2998749720483301202.jpg', 'https://cdn.chotot.com/RvnYriTrIHw0QTfemzbuuoiIYFt4l4Snt29bfY8XLrg/preset:view/plain/17d74d67db42d4c21d2abceb2c6d2016-2998749720152715673.jpg']}),

L(1315,"da-nang","ns","Квартира",6000000,40,
  'Новая квартира за улицей Huỳnh Lắm (Hòa Quý) — полная меблировка, тихий прохладный район.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134296983.htm","вчера",1,source="chotot",
  details={'contact': 'Đăng Khoa', 'photos': ['https://cdn.chotot.com/kplLWjVvqYDyw4O_f87fyCZ5vuFHjApV9AF2PnYGzTw/preset:view/plain/439ec45c95e9a7ed672111a72636d411-2998752437887666002.jpg', 'https://cdn.chotot.com/J0Zfjpj0pKRTtRxtKa58Ubfrl0Ybn_zyRxw5vVHKuFY/preset:view/plain/c3706aed1258eae50190207f427e04a0-2998752423593324953.jpg']}),

L(1316,"da-nang","ns","Квартира",9500000,40,
  '1-спальная квартира на 4 этаже в Đầm Sen 5 by Haviland (Hòa Quý) — балкон с видом на город, своя стиральная и сушильная машина, еженедельная уборка, диван и обеденный стол.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134296840.htm","вчера",1,source="chotot",
  details={'contact': 'HAVILAND HOUSE ĐÀ NẴNG', 'photos': ['https://cdn.chotot.com/O2P6TMXGjhbUhQFD3ci79DBcuR2DDkxf3PlL6NcYAcM/preset:view/plain/500a7161f7112761f5c79bc5ed266373-2998751551170169740.jpg', 'https://cdn.chotot.com/_tyAkuNM9bU-h5VoEW8ZAxddqa76dhLoTPBeFs0HOAg/preset:view/plain/5b094fa5e002c9b227255878a232ef4f-2998751551495186451.jpg']}),

L(1317,"da-nang","hk","Квартира",8000000,40,
  'Меблированная квартира 40м² с отдельной спальней на ул. Trần Nguyên Đán (Hòa Khánh Nam), рядом ĐH Sư phạm, ĐH Bách khoa, Mega Market, 500 м до пляжа Nguyễn Tất Thành. Лифт в доме.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134293624.htm","вчера",1,source="chotot",
  details={'notice': 'у того же хозяина в этом же доме есть студия 30м² за 6 млн ₫/мес', 'contact': 'Lê Đào Dương', 'photos': ['https://cdn.chotot.com/2JsLydXFV01GX9JDxBvGKHAX3XWaek5PeEA9tRpeKqo/preset:view/plain/ab7d2df471aa9f7e6aec8b26b3fb11ef-2998734900602202727.jpg', 'https://cdn.chotot.com/cW1_snymgw3Me3Zsi3YfvsAv82wuNGGDaWUczwBqYF4/preset:view/plain/e98ad9e43e38eee4fb3f57a76d7911c2-2998734900886981516.jpg']}),

L(1318,"da-nang","ah","Дом",32000000,120,
  'Вилла целиком 2 этажа на ул. Đinh Đạt (Phước Mỹ), 200 м до моря — 2 спальни/2 с/у (с ванной), кондиционер 3HP в гостиной, кухня-остров, отдельная прачечная со стиральной и сушильной машиной. Полная премиальная меблировка.',
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134289636.htm","вчера",1,source="chotot",
  details={'contact': 'Phương', 'photos': ['https://cdn.chotot.com/TYy4EjWt3miXMXrI1QWWK648gYjieVM6TvEfjjuvlzk/preset:view/plain/dbb37e8a91a21ba3546741f408f37965-2998715218158291661.jpg', 'https://cdn.chotot.com/PZ2_FfjKyvUVs5SjpYhgR8XZbZuIKOB0cx07UQdohf4/preset:view/plain/c8e1ed98b0479e5db820659b48bbed19-2998715218524045051.jpg']}),

L(1319,"da-nang","hcg","Дом",75000000,263,
  'Вилла целиком 3 этажа на ул. Núi Thành (Hòa Cường Bắc) — 263м² (фасад 9 м), 5 спален, полная меблировка.',
  "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134288721.htm","вчера",1,source="chotot",
  details={'contact': 'Mr AN', 'photos': ['https://cdn.chotot.com/Bvkf06OUqD0sjElPnM31xaWuF6elwqfx9qUep6u_PIc/preset:view/plain/ef6307e2d7e13d6e82ae1a63afd63fbf-2998711398057527461.jpg', 'https://cdn.chotot.com/bsZN3N0VjVzZnwM0WNejROpQ4joA3YzLx8hRzTRJCE8/preset:view/plain/b9688d19a85dd06941ec9e4996c90aaa-2998711398064555858.jpg']}),

L(1320,"da-nang","ns","Квартира",30000000,82,
  'Квартира в ЖК The Ponte (ул. Trần Thị Lý) — 82м², 2 спальни, средний этаж, прямой вид на мост Cầu Rồng, полная премиальная меблировка.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134288660.htm","вчера",1,source="chotot",
  details={'contact': 'Phương', 'photos': ['https://cdn.chotot.com/-3G1NvBzFlZlJhywQlpk5uQ_CDcYqFh1e93EhcgfGC8/preset:view/plain/31632fa5fc0e2c3f16ccb10c92783091-2998711010219674508.jpg', 'https://cdn.chotot.com/REN-_CYr9aHyP4809jb1JTa2bVtv-cBmjv3yF62oG2g/preset:view/plain/29c2f2be38462a61e935d2ea8adab3b7-2998711013273193356.jpg']}),

L(1321,"da-nang","tk","Дом",30000000,78,
  'Новый дом целиком на ул. Trần Xuân Lê (Thanh Khê) — 3 спальни/3 с/у, полная меблировка, тихий район, есть место для машины.',
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134288614.htm","вчера",1,source="chotot",
  details={'notice': 'цена по объявлению обсуждается', 'contact': 'Được Phan', 'photos': ['https://cdn.chotot.com/Unx0n341bCC9foQTr9uYizOFuI-U9HC5XsO78wEmWIY/preset:view/plain/7d39dad14acdc3f1b625cec85e67cd10-2998710958184006431.jpg', 'https://cdn.chotot.com/nwzPxFwkvwpn2Mqf5VPLxiGCUsvCr--C-lElv6J6y8c/preset:view/plain/f6139df3e194df541c3a49de4348fec9-2998710957774636882.jpg']}),

L(1322,"da-nang","st","Дом",200000000,800,
  'Вилла целиком 5 этажей на первой линии ул. Hoàng Sa (Mân Thái) — 800м², 8 спален/8 с/у, бассейн, сад, прямой вид на море. Полная меблировка.',
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134287222.htm","вчера",1,source="chotot",
  details={'contact': 'MR HUY', 'photos': ['https://cdn.chotot.com/WAGn6gPNx6Vw-gB3Qwq6ILJvjCCTgzLJh3RiomfLp1o/preset:view/plain/d4e13a4a7d1d71c55e77cded0099aa15-2998705510599557919.jpg', 'https://cdn.chotot.com/nrCcS29VeQzGIor4wwnW96OCWjaC-BHNnnwm3K2aJ8Y/preset:view/plain/54df5814a865076852a58371937b2fff-2998705511178973593.jpg']}),

L(1323,"da-nang","ah","Дом",30000000,75,
  'Дом целиком 3 этажа на ул. Trần Thanh Mại (An Hải Bắc) — 75м² (фасад 4,5 м), 3 спальни/2 с/у.',
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134287173.htm","вчера",1,source="chotot",
  details={'notice': 'площадь по тексту объявления 75м², в структурном поле площадки — 70м²', 'contact': 'Mr AN', 'photos': ['https://cdn.chotot.com/tJW-M3UAjmPtfqCjx7sJvlTqHfHtTnsmdU6u2pw68-s/preset:view/plain/c8593dd64a1852f92bbf84b4c2b27587-2998705552991934220.jpg', 'https://cdn.chotot.com/uislR-tORLRyWzqzKRqJOKcTs2TiX03CfJJF9Ye2X_A/preset:view/plain/79b0409b4314a77c2df7cecaa6a3bf11-2998705553036838738.jpg']}),

L(1324,"da-nang","ns","Дом",20000000,100,
  'Дом целиком 3 этажа на ул. Mỹ Đa Tây 6, квартал Nam Việt Á (Khuê Mỹ) — 100м²/этаж, 4 спальни/5 с/у, полная меблировка.',
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134285932.htm","вчера",1,source="chotot",
  details={'notice': 'хозяин принимает иностранцев и допускает сдачу в краткосрочную аренду (lưu trú)', 'contact': 'Ms Diễm', 'photos': ['https://cdn.chotot.com/vlAioQNBpT5VOuJzPQyTeuHMLKY4ePh7Yz_b8dYi6ZY/preset:view/plain/60c51046ee1250416dabfd95e31d7871-2998700008630530457.jpg', 'https://cdn.chotot.com/O8oqzbNLlOqKXo_pO8OQGB9QJOcDxgP-VOn16-JUnh4/preset:view/plain/391ad88b10641ff456c6a78cf1ca4dca-2998700008913536850.jpg']}),

L(1325,"da-nang","ah","Квартира",19000000,68,
  'Квартира Monarchy A (An Trung 2) — 68м², 2 спальни/2 с/у, просторная гостиная с балконом, полная премиальная меблировка. Бассейн, детская площадка, ресепшн и охрана 24/7, большой подземный паркинг. Несколько минут до моста Rồng, Trần Thị Lý, реки Хан и пляжа Mỹ Khê.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134285564.htm","вчера",1,source="chotot",
  details={'notice': 'заезд с сентября 2026', 'contact': 'Hoàng Thiện Duyên ', 'photos': ['https://cdn.chotot.com/nBpYFs73kJmlCsQ0J5VGAcBJl6Pp3lZGyQrwBLaDnyo/preset:view/plain/f38157309dfdc14c32dab55fd93ccc45-2998697696377953395.jpg', 'https://cdn.chotot.com/edqgO8cmDWgDUPmUxRtN261y09e-SjxMqkygWJ3SOc8/preset:view/plain/e346f7b52a7b0884a2959ee6eddc0eab-2998697698069383885.jpg']}),

L(1326,"da-nang","ah","Дом",18000000,90,
  'Дом целиком 3 этажа рядом с парком Hồ Nghinh (An Hải Bắc) — 90м², 4 спальни, кондиционеры есть, без мебели.',
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134285443.htm","вчера",1,source="chotot",
  details={'contact': 'BĐS Sơn Trà', 'photos': ['https://cdn.chotot.com/vtzZeN1lRV9_7020CF0whvNaASq12tUUB_rk4rgqFoI/preset:view/plain/628e09d5c19f818688e97fde9d491673-2998697394363782924.jpg', 'https://cdn.chotot.com/JunQplH91FdJ35_8XfmcNfwfq_DLq6K3-BDvS-3Xzp8/preset:view/plain/6e758d1b7791913b0cd6e6f8e02b01a1-2998697394501573747.jpg']}),

L(1327,"da-nang","tk","Дом",15000000,60,
  'Дом целиком 2 этажа в переулке K96 Điện Biên Phủ (Chính Gián), выход на Lê Độ — участок 60м², общая площадь 110м², 3 спальни/3 с/у. Полная меблировка и техника (стиральная и сушильная машины, фильтр воды, холодильник, 4 ТВ, 3 водонагревателя, 5 кондиционеров), рядом AEON Mall (500 м), аэропорт, вокзал, рынок Cồn.',
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134285136.htm","вчера",1,source="chotot",
  details={'notice': 'для иностранных арендаторов цена 18 млн ₫/мес', 'contact': 'Nguyễn Tấn Luân', 'photos': ['https://cdn.chotot.com/oovATt0B-RXg7aUliAW6MFF2HCojtnLezPeiTneUxS0/preset:view/plain/c69c45c5d56747b1b1967be71de8c537-2998695574223161170.jpg', 'https://cdn.chotot.com/n3al3ncTf4FVQXv64eVAyFA-goNK-trz9TQH3VfWugc/preset:view/plain/9d0e5e286cf922294c70d43f148996f1-2998695575884171090.jpg']}),

L(1328,"da-nang","ns","Квартира",15000000,50,
  'Угловая квартира с видом на город в ЖК Mường Thanh (Mỹ An), 18 этаж — 1 спальня, полная меблировка.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134280530.htm","2 дня назад",2,source="chotot",
  details={'notice': 'указанная цена не включает плату за управление и wifi', 'contact': 'Võ Thị Hồng Sương', 'photos': ['https://cdn.chotot.com/VmBEqUClDhzXqV5M8QuHOXq-8UgSCxRzVU0c1ewT_-Y/preset:view/plain/2e8f5ed88637226dfbcb19f834b63cde-2998616821187774290.jpg', 'https://cdn.chotot.com/sQJp0Ey8nTpxVTyphX9kidL1bvdkI3syF0WR0iYqlcw/preset:view/plain/23858609cb1d32931250ee12b9c15117-2998616821677672534.jpg']}),

L(1329,"da-nang","st","Дом",25000000,100,
  'Дом с садом целиком на ул. Trương Định (Mân Thái), у моря — 2 спальни/1 с/у, гостиная, кухня, просторный двор перед домом. Полная меблировка.',
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134280472.htm","2 дня назад",2,source="chotot",
  details={'contact': 'Trân Duy Hải', 'photos': ['https://cdn.chotot.com/IC5oVGTeAlrChC8ay5UjcNvBIoMtKS8nfIHlAJNdbR4/preset:view/plain/5e66d864aef1a71fb15e083464ace2cf-2998616113163306834.jpg', 'https://cdn.chotot.com/BRe7w_KPnWmL9D98wHqYrkxA88JL07__b9AdIWlh9Tg/preset:view/plain/2c94c1151547e5e3e3469ad04f644a7f-2998616113737096307.jpg']}),

L(1330,"da-nang","ns","Квартира",20000000,67,
  'Квартира с видом на город в ЖК Mường Thanh (Mỹ An), 40 этаж — 2 спальни, 67м², договор на 1 год.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134279906.htm","2 дня назад",2,source="chotot",
  details={'contact': 'Võ Thị Hồng Sương', 'photos': ['https://cdn.chotot.com/DJEcGR1ALQ_pb8RPIcFx7MsoQSkJes9KSI7BVNZEGgo/preset:view/plain/d841016d3dc239651d345f8758d18ebd-2998612177451707349.jpg', 'https://cdn.chotot.com/tD1jNvtPwL_2OsJeVTeOjBytdw55A9WkEXzzWVVAAv0/preset:view/plain/edda665856df181c0d9678312bd8dacc-2998612177675129990.jpg']}),

L(1331,"da-nang","hcg","Квартира",8000000,50,
  '1-спальная квартира P403 на ул. Trưng Nữ Vương (Hòa Cường) — бассейн на крыше, полная меблировка, свободна сейчас.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134268892.htm","2 дня назад",2,source="chotot",
  details={'notice': 'хозяин принимает только вьетнамских арендаторов', 'contact': 'Được Phan', 'photos': ['https://cdn.chotot.com/kQ0NBIgRzu6CIfIo1yDgMcKl2SisB5iqlLgDPrRojk4/preset:view/plain/627b4d8c7b2fe30f878f0f28caf62712-2998561532746762066.jpg', 'https://cdn.chotot.com/fXUIV83cmaeQQCCv4nLFT_ZXsuB7DyGuGq9YkbFzkAY/preset:view/plain/a9f28f80a5e586b9a20f8b861185955d-2998561532660274097.jpg']}),

L(1332,"da-nang","hcg","Дом",31500000,55,
  'Дом целиком 3,5 этажа в переулке (4,5 м, для машины) у ул. Lê Đình Lý рядом с Nguyễn Văn Linh (Bình Hiên) — 55м², фасад 9 м, гараж для машины, 3 спальни со своими балконами и с/у, терраса на крыше с барбекю и видом на салют. Полная меблировка и техника.',
  "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134268868.htm","2 дня назад",2,source="chotot",
  details={'notice': 'хозяин допускает совмещение с небольшим бизнесом (спа, шоурум, take away) на первом этаже', 'contact': 'KHOA Nhà phố Đà Nẵng', 'photos': ['https://cdn.chotot.com/_t_2VJq78W_KNXYUBLQS4AGjOCAA5BSNatK3dOlTws0/preset:view/plain/f639f4808d6585d8f2637afb9182dad5-2998560700333066066.jpg', 'https://cdn.chotot.com/3asP34qX3_cNprPqRHVjOiMMM2gfltiq0ytavxuHqmc/preset:view/plain/1abc16e109708034383d7e0e2568b27a-2998560700847518040.jpg']}),

L(1333,"da-nang","hc","Дом",18000000,70,
  'Дом целиком 3 этажа на ул. Thanh Thuỷ (Thanh Bình, центр Hải Châu) — участок 70м² (4,5×16 м), общая площадь 210м², гостиная, кухня, 3 спальни/3 с/у. Полная меблировка.',
  "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134254268.htm","3 дня назад",3,source="chotot",
  details={'contact': 'THANH', 'photos': ['https://cdn.chotot.com/vvgMxz2FWaVVoxvUqR1TnLJEMoSXO4YttxPlWtX8pZA/preset:view/plain/f5c4dac89f20791643aa082eddc875c8-2998442058823762073.jpg', 'https://cdn.chotot.com/yDk06dSVmwGCnCaMOyG3C9AZ8xyZDEJjSh1TOdwcWdY/preset:view/plain/a8435aff2b9f85b87ed699387ea729df-2998442044411871385.jpg']}),

L(1334,"da-nang","hc","Дом",10000000,85,
  'Дом целиком 2 этажа в переулке (3 м, для грузовика) на ул. Nguyễn Văn Linh (Hải Châu II), рядом мост Rồng — участок 85м² (фасад 5 м), общая площадь 170м², 4 спальни/2 с/у, место для машины и терраса на крыше.',
  "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134250151.htm","3 дня назад",3,source="chotot",
  details={'notice': 'без мебели', 'contact': 'THANH', 'photos': ['https://cdn.chotot.com/FBj48k9b-uQyBmYRyDMQzFE9hPZ-kFbehnaBOond5KY/preset:view/plain/1e7b487b05ed96f7262c10b7c08e85be-2998423897823213690.jpg', 'https://cdn.chotot.com/mSO3LVWOoxq7nYo1Hl6-8mVs0Z1GjrEKBEWEEHVbHbU/preset:view/plain/7c855706aa661caf27b67991f26e6e38-2998423897665821811.jpg']}),

L(1335,"da-nang","ns","Квартира",15500000,60,
  'Квартира Mường Thanh рядом с кварталом An Thượng (Mỹ An) — 2 спальни/2 с/у, гостиная, кухня, балкон, полная меблировка (ТВ, холодильник, кондиционер, водонагреватель, индукционная плита, вытяжка, вентилятор).',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134249033.htm","3 дня назад",3,source="chotot",
  details={'notice': 'в структурном поле площадки цена 15 млн ₫, в тексте объявления — 15,5 млн ₫; взята цена из текста', 'contact': 'Khánh Thuận', 'photos': ['https://cdn.chotot.com/_7ztF99pW69BznKvyqaxRLZBuBWpAGhzVPKQky8VT_I/preset:view/plain/cd3da6309b44101895e8e128a3eb8fe5-2998420207382201774.jpg', 'https://cdn.chotot.com/CSMouxrvjcjg0oHPB_WXefJMy8HMu9CvO8TKoQlIsMI/preset:view/plain/959d2327a0f689843bc45eb61fc9d9fd-2998420207629584269.jpg'], 'alsoOn':[{'source':'batdongsan','url':'https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-muong-thanh-da-nang-phuong-ngu-hanh-son-tp-da-nang/cho-ch-ay-u-noi-that-60m2-16-trieu-vnd-tai-so-phong-3614-a-nang-pr46198901'}]}),

L(1336,"da-nang","ah","Квартира",35000000,120,
  'Дизайнерская квартира у пляжа Phạm Văn Đồng (An Hải Bắc) — 120м², 2 спальни/2 с/у, интерьер в стиле тропического леса со встроенным бассейном вдоль гостиной и водопадом, панорамное остекление, дворик с деревьями. Бесплатная уборка 2 раза в неделю и обслуживание бассейна, высокоскоростной wifi.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134248095.htm","3 дня назад",3,source="chotot",
  details={'contact': 'Huỳnh Đức Việt', 'photos': ['https://cdn.chotot.com/Mq1y8DQEwH5Pf6mO6EpeLQWsyGOrF31C8ivggmvOGRQ/preset:view/plain/748e86927cdf19dc3e933a9015058c1f-2998164110733146390.jpg', 'https://cdn.chotot.com/9XvmWt9F-Y9jYNaQSh5r21986j6rJpiFJqxg3BxeQzw/preset:view/plain/f14f9e5c85723b9fc76d5cf5fd6bb6b7-2998164196224439665.jpg']}),

L(1337,"da-nang","hk","Квартира",7500000,67,
  'Угловая квартира в ЖК MIA Center Point (ул. Ngô Thì Nhậm) — 67м², 2 спальни/2 с/у, гостиная, кухня, балкон, вид на море (СВ).',
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134241864.htm","4 дня назад",4,source="chotot",
  details={'notice': 'в этом же доме есть варианты подороже с более полной меблировкой: 8 млн (частично), 11-12 млн и 15 млн ₫/мес (полностью меблированные)', 'contact': 'Khắc Dũng', 'photos': ['https://cdn.chotot.com/GBlosSO0RCyf-pVRj-mR-CR2DxGeJdNSJpZRbRMNhqA/preset:view/plain/f8f94da29f66c8546d2f4047822b623e-2998337160547261555.jpg', 'https://cdn.chotot.com/Vq7Ff0PDwl8hj8bOhIJx9AcYom77SShPVpXEn4LOXdc/preset:view/plain/68e042377a6484c9230c470a903806c4-2998337160475734840.jpg']}),

L(1338,"nha-trang","pl","Дом",17000000,100,
  'Дом целиком с лифтом в квартале An Bình Tân (Phước Long) — 1 этаж + 3, 4 спальни/5 с/у, кондиционер, вентиляторы, кухня. Дорога перед домом 8 м, есть место для машины.',
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134296775.htm","вчера",1,source="chotot",
  details={'notice': 'хозяин допускает совмещение с небольшим офисом', 'contact': 'Phương GoHome', 'photos': ['https://cdn.chotot.com/AsMBKkwDCvheZ96YCR9gAb1cQyDwPHV9ACdawiEiv54/preset:view/plain/57156e8d3c3679b0ba03e6504404cb89-2998751094369897356.jpg', 'https://cdn.chotot.com/VYt-nih5WO17vyCCrM0Am1-V7ADip3o2Q2UY3cKBjIE/preset:view/plain/64be44d381ef35462d1a96025adfa1db-2998751094449154067.jpg']}),

L(1339,"nha-trang","vn","Дом",20000000,142,
  'Дом с садом целиком 2 этажа в переулке 52 Trần Phú (Vĩnh Nguyên), рядом международная больница Vinmec — 142м² (фасад 8 м), 3 спальни/3 с/у, просторная терраса на крыше.',
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134295900.htm","вчера",1,source="chotot",
  details={'contact': 'Nghĩa Phạm', 'photos': ['https://cdn.chotot.com/mqDhZW6msQEjTgRMSXUriIwo2ICASbCh9GqXFk-NVbs/preset:view/plain/5dd96c785444538b30ca1aeee85523d5-2998745958583654277.jpg', 'https://cdn.chotot.com/wMcBp40QUCM8X6l8DR3LQKgDlwta0dH3eN46EKFfvMo/preset:view/plain/85dd8d37cfd3338f82cc066c67f1fa75-2998745958620261731.jpg']}),

L(1340,"nha-trang","vt2","Квартира",17000000,93,
  'Квартира в ЖК Mường Thanh Khánh Hòa рядом с мостом Trần Phú — 93м², 2 спальни/2 с/у, вид на реку.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134286336.htm","вчера",1,source="chotot",
  details={'notice': 'старый район — Phường Xương Huân, отнесён к ближайшему району проекта Vạn Thạnh (по прецеденту прошлых батчей); плата за управление/проживание 700 тыс. ₫/мес отдельно', 'contact': 'Văn Hoà', 'photos': ['https://cdn.chotot.com/pbik1kY8YEYKyPmXhcQXvZPG7ePtntLrzm15Shiv4pg/preset:view/plain/5054cd24677aeb6ab2730ea185f04d45-2998701997902026508.jpg', 'https://cdn.chotot.com/mJIAIK49mTqUFDvJRfsVlT7NxLfAR6LPBsRH2FmvjBQ/preset:view/plain/802a4434ed600f51281199ddd36f14a4-2998702001005877004.jpg']}),

L(1341,"nha-trang","pl","Дом",8500000,85,
  'Новый дом целиком (cấp 4) в переулке 4 м с выходом на ул. Thích Quảng Đức (Phước Long) — 85м², 2 спальни/1 с/у, просторная гостиная, кухня, 2 кондиционера. Приоритет семьям или девушкам, длительная аренда.',
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134286137.htm","вчера",1,source="chotot",
  details={'photos': ['https://cdn.chotot.com/oocXAIxBz7Yj2KlKx6VWxGA6mmXJKG8p21w_issHJ0w/preset:view/plain/f086193e1bd6644e9d057ac45f195d5d-2998700685585943245.jpg', 'https://cdn.chotot.com/Wlu_YWPMkv20otgpcMbrkJxZj6UF35mKGxe-eCZselo/preset:view/plain/e8a113670e2f18d6d49742566a042e86-2998700685033032588.jpg']}),

L(1342,"nha-trang","nh","Квартира",12000000,45,
  'Квартира Champa Uma на о. Champa Island (Ngọc Hiệp, север Nha Trang) — 45,1м², 2 спальни/1 с/у, кухня, гостиная, полная меблировка. Бассейн, спортзал, ресторан, массаж на территории. Цена уже включает плату за управление (890 тыс. ₫).',
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134284320.htm","вчера",1,source="chotot",
  details={'notice': 'дополнительно: интернет 220 тыс., комбо-сбор за инфраструктуру 600 тыс. ₫/чел. в месяц', 'contact': 'Trần Minh Tiến', 'photos': ['https://cdn.chotot.com/0uolJMawWfZyFm4qm_Zg3TjXrkSx-GGYL6D7VRAJ_ek/preset:view/plain/25b09241c966261483fdcab107bdb7ae-2998638808064084876.jpg', 'https://cdn.chotot.com/efI80DC1DwrGlhDT2eTx_5Cl_yBGNqk7xcwM2Huriew/preset:view/plain/a68866b8d10fbdb0e2173835e94f56fe-2998638808220294259.jpg']}),

L(1343,"nha-trang","ph","Квартира",10000000,35,
  'Квартира с балконом в VCN Phước Hải (đường số 13) — 35м², умная меблировка, лифт, электронный ключ, охрана.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134282062.htm","2 дня назад",2,source="chotot",
  details={'contact': 'Quang Long Megas', 'photos': ['https://cdn.chotot.com/MD_ZUofC11P1Fxv_OBlzJEfLRHxuso-Bfs2ZtVwbu5U/preset:view/plain/0084760e93b46eee22f6349761b345ee-2998629076901358947.jpg', 'https://cdn.chotot.com/c_mIyHH_Ik6jXwjk9nDD2Ml5FqWFmzl5BEq6L1WJluk/preset:view/plain/181aa7f8302893dd0ed7300fa371cb33-2998629076872096725.jpg']}),

L(1344,"nha-trang","ps","Дом",20000000,50,
  'Дом целиком 3 этажа на ул. Yersin (Phương Sài), 2 минуты до моря — этаж 50м² (фасад 9 м), общая площадь 150м², 3 спальни/4 с/у, гостиная, кухня, комната для алтаря, прачечная. Полная меблировка, переулок для машины.',
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134280777.htm","2 дня назад",2,source="chotot",
  details={'contact': 'Thu Vân', 'photos': ['https://cdn.chotot.com/m_P_djS3CgvCzdx0PJpfSk0eGRaXd6udzSYHhMHgKS0/preset:view/plain/189e143912843e6933004687b5a3d6fa-2998618958913410304.jpg', 'https://cdn.chotot.com/bJp_MyhRaPkLz9wqbnWXFTwjUt2ig0DZrCoH31ZxkeE/preset:view/plain/48dcd99a7575369964ea6da90f198e84-2998618968378869586.jpg']}),

L(1345,"da-lat","lv","Квартира",10000000,55,
  'Квартира на ул. Yersin в центре Đà Lạt — 55м², 2 спальни/1 с/у, полностью новая меблировка.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134293235.htm","вчера",1,source="chotot",
  details={'notice': 'хозяин отдаёт приоритет договору на 1-2 года', 'contact': 'Căn Hộ Chung Cư', 'photos': ['https://cdn.chotot.com/0ccqUQ64tv4mMXR6urY4pE7EjsbCeBc5HBcUP9oK7a8/preset:view/plain/1ade7c84863d1af43e2b88289683e2fd-2998733135979407975.jpg', 'https://cdn.chotot.com/rb8_JGQxYZKNO0k791wE0-g1YODZE2P7M6TYRoEGiP8/preset:view/plain/7a188711d56fcb34e052fc29280320d9-2998733135988600051.jpg']}),

L(1346,"da-lat","cl","Дом",5000000,100,
  'Дом целиком на ул. Kim Đồng (рядом рынок Ngô Quyền) — 100м² в использовании, 2 спальни, гостиная, кухня, просторный двор для машины.',
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134287487.htm","вчера",1,source="chotot",
  details={'contact': 'khanh nguyên Trần Nguyễ', 'photos': ['https://cdn.chotot.com/AGgWr9fyr3Y7ehHd6vLa98Xhsr2boqzOxAk-0sD_xq4/preset:view/plain/9666eecd0c18184a8884a442dbe52251-2998706809482479442.jpg', 'https://cdn.chotot.com/IpxabwyJsRTUJRNANIQfY0tTxkazUdodfeTF6-ReRkI/preset:view/plain/fba164c0ebca35de1eef313cb4c458de-2998706808884975372.jpg']}),

L(1347,"da-lat","xh","Дом",10000000,70,
  'Дом целиком на ул. Thông Thiên Học — 1 этаж + 2 этажа, 4 спальни/3 с/у, свободная планировка, заезд по дороге для машины.',
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134287446.htm","вчера",1,source="chotot",
  details={'notice': 'дом сдаётся пустым, без мебели', 'contact': 'khanh nguyên Trần Nguyễ', 'photos': ['https://cdn.chotot.com/JrA7BdzGCg7uHT4KEyg_S1POocuz7zmAmmE7EctotYs/preset:view/plain/abdc8c68b97b5a45ecba3c9405af95c8-2998706665158663283.jpg', 'https://cdn.chotot.com/RoFg2I8-3pqrZuvKFnxtBZYVEreGmJoMP9Qcl8GE3jQ/preset:view/plain/209fb88ed158c2b1132300d955a5d6b7-2998706665005253407.jpg']}),

L(1348,"da-lat","cl","Дом",12000000,70,
  'Дом на главной дороге на ул. An Sơn — 3 спальни/3 с/у, гостиная, кухня-столовая, мансардный этаж.',
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134287410.htm","вчера",1,source="chotot",
  details={'notice': 'в объявлении отмечена возможность использовать дом и под небольшой бизнес', 'contact': 'khanh nguyên Trần Nguyễ', 'photos': ['https://cdn.chotot.com/nMMOBWOL5k_iWxMX3hohdDcIKe8lTYZh0M7gocW3b8A/preset:view/plain/db41d3f58c33fe0a605829eaf90dc65b-2998706470030366476.jpg', 'https://cdn.chotot.com/u7jsFNpivblkh_6VSQDnLRDzG8dutLlwLCo94I-Jetc/preset:view/plain/45baa847d997138306a43d90cdddd7e9-2998706469950325535.jpg']}),

L(1349,"vung-tau","vtp","Квартира",6500000,64,
  'Квартира в блоке A ЖК на ул. Nam Kỳ Khởi Nghĩa — 64м², 2 спальни/1 с/у, чистая, с полной меблировкой.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134284950.htm","вчера",1,source="chotot",
  details={'notice': 'заезд с 1 сентября', 'contact': 'Mạnh Nguyễn', 'photos': ['https://cdn.chotot.com/RzPg5ISeNpyuPmwOA5kYmTYmvvC31gd9OVn2LAbR5a4/preset:view/plain/01d48067d4383df8afab0ad967a60ccb-2998694149226491235.jpg', 'https://cdn.chotot.com/xPuIPaZ-cPevYz4icW6d40ayVMHJ5IRwHrb7m39Mfnw/preset:view/plain/82543cf008bc8c8c1be4f15f55737985-2998694149006248844.jpg']}),

L(1350,"vung-tau","vtp","Квартира",12000000,49,
  'Сервисная квартира The Sóng рядом с площадью Tam Thắng, 300 м до моря — 2 спальни/1 с/у, полная меблировка.',
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134280314.htm","2 дня назад",2,source="chotot",
  details={'notice': 'в объявлении отмечена возможность использовать под офис или сдачу через Airbnb', 'contact': 'Hoàng Anh Nhà Đất', 'photos': ['https://cdn.chotot.com/J1m_ZJDt8JiUyrUqIMQfDNHxiV_aUsezSZqdduESjqA/preset:view/plain/96c11cb76923023b3b3a5c23972df28d-2998614686482149806.jpg', 'https://cdn.chotot.com/6YUB_xL4W8tXcweEJX253uka_OSlVlW-tbDRIO3S51c/preset:view/plain/172ef98374646029587d7a2825f821b6-2998614687602367603.jpg']}),

L(1351,"quy-nhon","qnn","Квартира",8500000,35,
  'Квартира с видом на море в FLC Sea Tower (ул. An Dương Vương) — 35м².',
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-qui-nhon-binh-dinh/134286420.htm","вчера",1,source="chotot",
  details={'notice': 'в объявлении отмечена возможность как проживания, так и сдачи в краткосрочную аренду (lưu trú)', 'contact': 'Nguyễn Trường HiFriendz', 'photos': ['https://cdn.chotot.com/20-2DMm_bHdIvVoBh--dzD3YdVcRouzsZIjD2EaEN38/preset:view/plain/4dedb35d21370271dac2e6583ec3dc3f-2998701972143507282.jpg', 'https://cdn.chotot.com/d_uuaTJBsjYUHZJ91MLJdcEuP7BFbGuY4spKKDuvTfU/preset:view/plain/8c8219368ecae6dcf6d7dc984f26d75b-2998701972199069452.jpg']}),

L(1352,"hoi-an","hat","Дом",45000000,150,
  'Вилла целиком в комплексе Casamia Calm (ул. Đồng Nà 1) — 150м², 3 спальни/3 с/у, кабинет, премиальная полная меблировка. Приоритет долгосрочной аренде.',
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-hoi-an-quang-nam/134288419.htm","вчера",1,source="chotot",
  details={'notice': 'старый район — Xã Cẩm Hà, в новой сетке — Phường Hội An Tây', 'contact': 'Phương', 'photos': ['https://cdn.chotot.com/T8yd6E1uy6FXSBhNcJEp5kRMzz66fPVM43nd5RXc1bQ/preset:view/plain/4cff3bfcb36cfb15933faf1550381eb6-2998710325895180697.jpg', 'https://cdn.chotot.com/8PPBhBbAuiD3OYhBgBW510Hmpc3-sJo0R0B13WuDafM/preset:view/plain/f258359e3e5e9001f7bc2ab76e68d824-2998710325929396389.jpg']}),
L(1353,"ho-chi-minh","ak","Квартира",18000000,70,
  "2-спальная квартира в ЖК Masteri Thảo Điền, 70м² (2 с/у) — полная меблировка (диван, ТВ, холодильник, стиральная машина, кондиционер, духовка).",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/127642824.htm","вчера",1,source="chotot",
  details={"contact":"Ánh Trang","photos":["https://cdn.chotot.com/WuQw251SjdiRWoLPULS86V3hgwCVauUnh2ET_wt8P20/preset:view/plain/ca23e686dae2e482ee55079e9702a4dc-2948704728612356285.jpg","https://cdn.chotot.com/oTIwqzfJzpd0LNxT43Av9SR2obS3Uw-qskaublX6XjQ/preset:view/plain/8b05ae79376a0be6692f95f6ecfc5634-2948704728359137249.jpg"]}),

L(1354,"ho-chi-minh","ak","Дом",11500000,50,
  "Дом целиком (1 этаж + мансарда) на ул. Nguyễn Văn Hưởng, Thảo Điền — 50м², отдельный двор, своя стиральная машина, уборка 2 раза/неделю, рядом мост Sài Gòn и туннель Thủ Thiêm.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-thu-duc-tp-ho-chi-minh/125923392.htm","сегодня",0,source="chotot",
  details={"notice":"в тексте объявления упомянут старый район Thảo Điền/Quận 2, в структурном поле площадки — An Khánh","contact":"Quỳnh Như HiFriendz","photos":["https://cdn.chotot.com/-GNqDERs5F5g9nqxS2K3DX_aAgsfd4arLU2IbBHmhxg/preset:view/plain/03d76c0612ef24bcdd052068ff48f4a8-2937394671807805177.jpg","https://cdn.chotot.com/IKLgH6KYVWDwYNchQmKTUWF4r731YS1q4kvT8aDtrAc/preset:view/plain/dfc7b4ecf099b07fea86e85d4cc9b557-2937394671992836861.jpg"]}),

L(1355,"ho-chi-minh","bth","Комната",10000000,60,
  "2-й этаж дома на ул. Cống Quỳnh, Bến Thành (центр Q1) — 60м², 2 комнаты/1 с/у, кондиционер, своя ванная, водонагреватель, окно с естественным светом, рядом пешеходная улица, супермаркеты, 7-Eleven.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134303642.htm","сегодня",0,source="chotot",
  details={"notice":"в объявлении указано разрешённое смешанное использование (для бизнеса и проживания)","contact":"TÔ TIẾN","photos":["https://cdn.chotot.com/Bd0JPC5bVsHT_IzcPXBOzIfyzVLhZcdKcHSyEv9cTBA/preset:view/plain/f147721e2973e9d99a3f156b5249477d-2998847171717408787.jpg","https://cdn.chotot.com/7R6pJkAYdEQT3gS4BPpMv4WkJqDkZo0R1ThPJ6pGTmE/preset:view/plain/e56fd2b5d8680c1c24139d3ac1b52004-2998847171134218460.jpg"]}),

L(1356,"ho-chi-minh","th","Квартира",10000000,37,
  "1-спальная квартира Lavida Plus, 37м² — угол Nguyễn Văn Linh/Nguyễn Hữu Thọ, рядом Phú Mỹ Hưng, полная меблировка (диван, кровать, шкаф, холодильник), бассейн и супермаркет в доме.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134271328.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nguyễn Hồng Khánh Mỹ","photos":["https://cdn.chotot.com/bRpNVuoGbr74n5LUf5ZXbmxLaRFz8g6stm1C0Wu4CKE/preset:view/plain/7a163b7d1d810ef342abd1ccf62b859e-2998565581989324058.jpg","https://cdn.chotot.com/kYpx54eYnSUuwPIOFhj5aLN6fPP7Nq_qKzClw8sxTWk/preset:view/plain/2b6ed62daac4a420b4b12b18747c3958-2998565582113397875.jpg"]}),

L(1357,"ho-chi-minh","th","Студия",6500000,35,
  "Студия с балконом и отдельной кухней, 35м², ул. Số 13 (Tân Kiểng/Tân Hưng) — полная качественная меблировка, для 1-2 человек.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134279561.htm","вчера",1,source="chotot",
  details={"contact":"Nguyễn Hữu Quyết","photos":["https://cdn.chotot.com/7lHp_se5k_cO3FTJwo2kQX8ov0ow5IxkAT_GVV_WqHw/preset:view/plain/402ec351e55aae483cbd9885073ef70f-2998609796764108626.jpg","https://cdn.chotot.com/CAgZH8eUOG64AawYjrw72Apw8wSkJN5T_OKPxtIZlYE/preset:view/plain/42999792d4a21feac3df0d3b5b60951b-2998609796812917644.jpg"]}),

L(1358,"ho-chi-minh","th","Квартира",6000000,35,
  "Дуплекс с полной новой меблировкой, 35м², ул. Lâm Văn Bền, рядом UFM — современный дизайн, подходит для работающих, студентов, иностранцев.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134268216.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nguyễn Hữu Quyết","photos":["https://cdn.chotot.com/2PBe5f-tRdXir7lUw9nJG8xiGp-IKoS_wul6xkadrw8/preset:view/plain/a60e1a4e68b1c47715caaec168a5efc6-2998559218612585395.jpg","https://cdn.chotot.com/zhoJ8YZtfZUZjCXUGh74VoBFt7AnhsWRRNf55pS-dqY/preset:view/plain/2ae732cd7d29b4411f57bf5523666091-2998559218235595891.jpg"]}),

L(1359,"ho-chi-minh","th","Комната",4800000,50,
  "Отдельный этаж в переулке 380 Lê Văn Lương, Tân Hưng — 50м², свободный график, меблировка (холодильник, мебель, диван, кухня, водонагреватель, шкаф), 5-10 мин до ĐH Tôn Đức Thắng, RMIT, ĐH Luật, рядом Lotte.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134305922.htm","сегодня",0,source="chotot",
  details={"contact":"Thủy","photos":["https://cdn.chotot.com/jJnMynmakiMJE4L9R5p4y8kaXiaaoeAfwENMQGSWaJ0/preset:view/plain/f64962830e4f1a04845946cab35a859f-2998858999564415385.jpg","https://cdn.chotot.com/VvOpUerV3KZOWaHJiGfzrjq4HEEojyPVIKH9tQtCRuI/preset:view/plain/f5b9b71c6f964b9a8716579d5987efd0-2998859013003162009.jpg"]}),

L(1360,"ho-chi-minh","tm","Квартира",14500000,75,
  "2-спальная квартира Sunshine Sky City, 75м² (2 с/у) — полная меблировка, широкий балкон, рядом Phú Mỹ Hưng, 10-15 мин до Q4/Q1.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133169223.htm","вчера",1,source="chotot",
  details={"notice":"в тексте объявления площадь указана как 70м², в структурном поле площадки — 75м²","contact":"Huy","photos":["https://cdn.chotot.com/bVl0sPixoqoMXMOEvl-JebtVqhqpMRP1via-e7is59g/preset:view/plain/e30863eae50edfda4e35d12fe5bc2cbd-2990202856087645669.jpg","https://cdn.chotot.com/UPk7yLxwl-xs8vQF--5EF3au1LsDULJKOX7r5pPexxw/preset:view/plain/b532556023236eb72156953b13dd28d1-2990202856238867970.jpg"]}),

L(1361,"ho-chi-minh","tm","Студия",2600000,18,
  "Студия 18м² на 2 этаже, ул. Phạm Hữu Lầu (Tân Mỹ/Phú Mỹ) — свободный график, электронный замок, кондиционер, до 2 человек.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134290027.htm","вчера",1,source="chotot",
  details={"contact":"Thảo Duyên Văn Thị","photos":["https://cdn.chotot.com/vR_tmOoHQOd40J4KqoIGmOilsMyUUdspxXsly1zmFp8/preset:view/plain/2265e4c06d7e0fff24636b8e960f8e3a-2998717275185448786.jpg","https://cdn.chotot.com/6alGMCpZ4ctTLPOsoaZCHW9x0_0i1qj1G9zYbyoHpjU/preset:view/plain/1f8215ac0dc630659f6030f5f1c16fa8-2998717275195722636.jpg"]}),

L(1362,"ho-chi-minh","tm","Квартира",8000000,50,
  "1-спальная квартира, 50м², ул. 15B Nguyễn Lương Bằng, Tân Mỹ — кухня, гостиная, охрана 24/7, доступ по карте в лифт и квартиру, рядом Phú Mỹ Hưng, автобус №139 у дома.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134287583.htm","вчера",1,source="chotot",
  details={"contact":"Quang Huy","photos":["https://cdn.chotot.com/dxHO3B0GK4OvQSqPrem0PPMgVaRNe7kQCpk8Mpqeo-g/preset:view/plain/d959298a7a95f85c287da6e9caf73543-2998706023219911795.jpg","https://cdn.chotot.com/GQ3TQogezH0eGVUbCnYZCLPV_B5odPXXz1FHjxj7QAw/preset:view/plain/5b92b0ddad8c8fe193d8d909713961b4-2998706023230753676.jpg"]}),
L(1363,"ho-chi-minh","bth","Дом",7500000,17,
  "Дом целиком на ул. Đề Thám, Bến Thành (Q1) — 18м² (3x6м), подходит для семьи 3-4 человека, 2 спальни, 2 с/у.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/134306054.htm","сегодня",0,source="chotot",
  details={"contact":"Mr Điền","photos":["https://cdn.chotot.com/5sSzYR3zSD4FjSs4EUdmUNpUw6vikMGKT9KwcKy2rWc/preset:view/plain/ff98baba1647757254aea5798f961aa3-2998844117389707090.jpg","https://cdn.chotot.com/UKOuxna7nvEFZ8UiLCpVacknOCcsw97b_IfLjF-lXRs/preset:view/plain/71922691a65862fcf05043055ee425c7-2998844117440234067.jpg"]}),

L(1364,"ho-chi-minh","tm","Квартира",19000000,85,
  "3-спальная квартира (2 с/у) в ЖК The Golden Star, 85м², ул. Nguyễn Thị Thập, Tân Mỹ (Q7), юнит b9-06 — готова к заезду с 1 августа.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133998312.htm","сегодня",0,source="chotot",
  details={"contact":"Thanh Phan","photos":["https://cdn.chotot.com/RenlwMeQ9ogtH6Z9vcEy8JRDXoLzoFVVNSwIhMdYyCs/preset:view/plain/26db407e717398d4b63b54235efaea6a-2996546162446005591.jpg","https://cdn.chotot.com/Je_TPembxp2UfLHGN15grJsI5y-QwJS46zFjHUW5zlo/preset:view/plain/4a01ac2ce0d41591731dcbb02c8b1702-2996546165767959895.jpg"]}),

L(1365,"ho-chi-minh","th","Студия",6800000,35,
  "Открытие нового CHDV (сервисной квартиры) с полной меблировкой и балконом, ул. Lê Văn Lương, Tân Hưng (Q7) — 35м², рядом Lotte Mart, TDTU, RMIT, 5 мин до Q4/Q1.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134256193.htm","2 дня назад",2,source="chotot",
  details={"notice":"здание с несколькими юнитами, указанная цена стартовая — точная цена зависит от конкретной комнаты","contact":"Tú Quyên Neway","photos":["https://cdn.chotot.com/o_WeeP8k0nghsa6RQDCWilpQMfYU7MEelyAzA7H3_eQ/preset:view/plain/0f067cb915fb4a939089fb43d7e4cbbc-2998448753805002158.jpg","https://cdn.chotot.com/zFiXRz1E0VaDCPLqpSsFHPVnzgXhDV29Thpq4jMRAwQ/preset:view/plain/62197b57da8ca1cef28735166dfe04dc-2998448754042373970.jpg"]}),

L(1366,"ho-chi-minh","th","Квартира",7500000,45,
  "1-спальная квартира с полной меблировкой, ул. Số 79, Tân Hưng (Q7) — 45м², рядом Lotte Mart. У арендодателя также есть варианты студии и дуплекса той же локации, от 4 до 8 млн/мес в зависимости от площади.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134263763.htm","2 дня назад",2,source="chotot",
  details={"contact":"Mạnh Tiến Newind","photos":["https://cdn.chotot.com/ZERX52qQuc_FKqF5zguPGiPz_6C58xP6wRMzxO0pEYc/preset:view/plain/08cfadeb346272914899b748b9cdde82-2998502246962317197.jpg","https://cdn.chotot.com/QbapGYmAjU0R6e1Zukzr80yFytBTo3PYjKiYGR-Lk9U/preset:view/plain/0d2ee29843d7711d71e50f854c870f73-2998502247144545395.jpg"]}),

L(1367,"ho-chi-minh","tm","Дом",7000000,35,
  "Дом целиком (1 этаж + 1 этаж + терраса), 35м² (3.3x9.5м), рядом рынок Phú Xuân, Q7 — 2 спальни, 2 с/у, вид на реку, мебель есть (кровать, шкаф, кухня, кондиционер, стиральная машина, водонагреватель).",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134306691.htm","сегодня",0,source="chotot",
  details={"contact":"Bđs Ngô Huy Đông","photos":["https://cdn.chotot.com/axuf--ItOMcbQG-hiOOjdcWnl11HHDip14IqX81FO2M/preset:view/plain/11471aa788d49328e6a70efd22118c76-2998862645715744268.jpg","https://cdn.chotot.com/rRuBXX6dk1xrt3mpb1iqnucYl2FrRnbT_RO-gK__Gn0/preset:view/plain/1e4d7c69c2a07d366a3436d8deee53f0-2998862660765103628.jpg"]}),

L(1368,"ho-chi-minh","tm","Дом",25000000,90,
  "Дом целиком (5x18м) в Khu Tái Định Cư Phú Mỹ, ул. Hoàng Quốc Việt, Tân Mỹ (Q7) — 4 большие спальни, 5 с/у, фасад 20м, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133906822.htm","сегодня",0,source="chotot",
  details={"notice":"подходит под офис/шоурум наравне с проживанием","contact":"Thanh Phan","photos":["https://cdn.chotot.com/ukPIhnhlbKCmoBo-7BPF12yZl4NiylPqyR2xLiLWCgk/preset:view/plain/d9479f01c82458c2900c1d6dfe09f0cc-2995853421177718244.jpg","https://cdn.chotot.com/M-DJW1mIDG1KNpp6lzaEf81ZuodJXbtQNcN9edCNjwA/preset:view/plain/eec1cff0287328d5dcbb2cf97a81f7d4-2995853421071073676.jpg"]}),

L(1369,"ho-chi-minh","th","Дом",11000000,40,
  "Дом на первой линии (4x10м), номерная улица, Tân Hưng (Q7) — 40м², 1 этаж, подходит для жилья с возможностью совмещения с небольшим бизнесом (магазин, офис, интернет-продажи).",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133995884.htm","сегодня",0,source="chotot",
  details={"contact":"Nhà Thuê Nguyên Căn Quận 7","photos":["https://cdn.chotot.com/POAVcxBYvih9KLTdMY6YwTuJDVVWokzcEJAaVayfoEA/preset:view/plain/f331689672edffa83022bf8a0aa4dd04-2996535214902782333.jpg","https://cdn.chotot.com/k_A5WDJAS0fBSCJM7xgxPm2Vgdd2d9cnOTtLgs8Wn5U/preset:view/plain/c844ec814a07d11df4117bd3ef2f7c66-2996535214971808782.jpg"]}),
L(1370,"ho-chi-minh","bth","Студия",5900000,35,
  "Студия с большим окном на ул. Lý Tự Trọng, Bến Thành (Q1), у рынка Chợ Bến Thành — полная меблировка, вход по отпечатку пальца, фасад улицы, парковка у дома.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134320741.htm","сегодня",0,source="chotot",
  details={"contact":"Đỗ Toán HiFriendz","photos":["https://cdn.chotot.com/MpbROuCgFMCwpwA4waQW9f8pFAhXpaiW9NjwKYfLtZk/preset:view/plain/cbb03fe2079879f3ef9bd0d673756e7d-2998993294404438924.jpg","https://cdn.chotot.com/FfJU18mKBn-1khpazLTHSHcUer1h-3zmjUT_NqsZG-E/preset:view/plain/0c7f24c8a8253d8bde903535f4ee5f3e-2998993294741370597.jpg"]}),

L(1371,"ho-chi-minh","bth","Дом",15000000,23,
  "Дом целиком в переулке ул. Phạm Ngũ Lão, Bến Thành (Q1) — участок 3,5x8м (23м²), 1 этаж + 2 этажа + терраса, 2 спальни, 3 с/у, новый ремонт, полная меблировка, рядом Q5/Q3/Q10.",
  "https://www.nhatot.com/thue-nha-dat-quan-1-tp-ho-chi-minh/133740133.htm","1 день назад",1,source="chotot",
  details={"contact":"Thế Hạo","photos":["https://cdn.chotot.com/wQemd8HJZjMI5QCRF4QZZyni9zUdQpZ_kOZ5UBw8-yA/preset:view/plain/bdb5049da526dcdfa7f0dba5f1a34d39-2994571543749393139.jpg","https://cdn.chotot.com/aaduArNRKTbE0gccTqkaVladkEav-D4G3GyxAk6xAfE/preset:view/plain/84d02bf177855616918aa67903c480f4-2994571543691580272.jpg"]}),

L(1372,"ho-chi-minh","kh","Студия",14000000,35,
  "Студия в ЖК Millennium, Khánh Hội (Q4) — 35м², полная меблировка, несколько минут до Q1, бассейн, спортзал, охрана 24/7, паркинг.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134315424.htm","1 день назад",1,source="chotot",
  details={"contact":"Lâm Hậu","photos":["https://cdn.chotot.com/emjL4tfo5Cwqtf-r3g2nuiW-qi-IleiGzi8VKFtPQtw/preset:view/plain/be180766b4444428ae70075b2c116005-2998920837819326684.jpg","https://cdn.chotot.com/jIr9i4Z7Pit7GorzONgp3An_8K2tApJ3UTGH0roFHeY/preset:view/plain/a2eff0e30c127d894dfb72848b3b5935-2998920839233081922.jpg"]}),

L(1373,"ho-chi-minh","kh","Дом",11000000,22,
  "Дом целиком на ул. Đoàn Văn Bơ, Khánh Hội (Q4) — участок 3,2x7м (22м²), 2 спальни, 3 с/у, свободен с 16 августа.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134322631.htm","сегодня",0,source="chotot",
  details={"contact":"Huy Nguyễn","photos":["https://cdn.chotot.com/svwQBATcN88dZweUDfqJWCzf_0_hvq4isnEg_rzNpMc/preset:view/plain/d07e88c37987d7fb9877159f5a20d1c6-2998999544571317132.jpg","https://cdn.chotot.com/HYE88k_xFuS4kOOe4CDblLzDmoxboXZLhu1MswK4yZI/preset:view/plain/7fef4e8992a089f77fd985bf3bef2074-2998999544717223955.jpg"]}),

L(1374,"ho-chi-minh","kh","Дом",13000000,35,
  "Дом целиком, Khánh Hội (Q4) — участок 3,3x10м (35м²), 1 этаж + 2 этажа + терраса, 3 спальни, 2 с/у, полная меблировка (3 кондиционера, стиральная машина), рядом Q1.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134320990.htm","сегодня",0,source="chotot",
  details={"contact":"Đông Thiên","photos":["https://cdn.chotot.com/uIWHW92gZg_uwAKOtFsOG0fu0wVcfzOsKcXb1sGA3Fk/preset:view/plain/59b03344f88515694f72d90b415b4c3f-2998994151044696972.jpg","https://cdn.chotot.com/1edpOnV2sCa8jxgnQzp4IlNoA8DNklGa1vxakqwNyd4/preset:view/plain/d85417fab9a87285fab6fb6114b6ded3-2998994150921867343.jpg"]}),

L(1375,"ho-chi-minh","kh","Комната",3000000,22,
  "Комната-мансарда с окном и отдельным двориком, Khánh Hội (Q4) — 22м², без мебели, электричество 5 тыс ₫/кВт, вода 100 тыс ₫/чел.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134311370.htm","1 день назад",1,source="chotot",
  details={"contact":"Vy","photos":["https://cdn.chotot.com/uP0EOEwK95qJYemMWjEda4Dw864caLjXnWPL9yZ3d1g/preset:view/plain/45d5b28425039c1371fa26c87cc57d26-2998889384092623068.jpg","https://cdn.chotot.com/ZHxRRkmOK9PIZQ5YFfsgsyhfjs2tm0hQLge1HG1YM_s/preset:view/plain/4a36c39abd243560e5f0e04d554f17df-2998889384523368274.jpg"]}),

L(1376,"ho-chi-minh","kh","Дом",11000000,24,
  "Дом целиком, Khánh Hội (Q4) — участок 3x8м (24м²), 1 этаж + мезонин + 1 этаж + терраса, 2 спальни, 3 с/у, рядом рынок Xóm Chiếu, мост Khánh Hội, университеты Luật и Nguyễn Tất Thành.",
  "https://www.nhatot.com/thue-nha-dat-quan-4-tp-ho-chi-minh/134307060.htm","1 день назад",1,source="chotot",
  details={"contact":"Đặng Trung Hậu","photos":["https://cdn.chotot.com/iSTpeA0FqoXGq8JNspHjBHRB-7XP7nWaVYBo43S5c6Y/preset:view/plain/7e1d40f2d66f06832350f03fa0066d3d-2998864718030809371.jpg","https://cdn.chotot.com/GIA0wl0E2n4DY776z-ebxJZ_L6SK3oGM_6k5_1eowqw/preset:view/plain/cd8b8dc5f3d51125a1654359f29216a0-2998864718112421418.jpg"]}),

L(1377,"ho-chi-minh","tm","Квартира",11500000,92,
  "3-спальная квартира (2 с/у), 92м², угловая с видом на реку, ЖК Era Town Đức Khải, Tân Mỹ (Q7) — полная меблировка, бассейн, спортзал, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134323259.htm","сегодня",0,source="chotot",
  details={"contact":"Loc Phan","photos":["https://cdn.chotot.com/hokfUKMelYZwy4DhDaX77tOVCtXhAYJRJJlpwBKGj2A/preset:view/plain/e2f8318608cd3f38d01b9b855143cc03-2999001894875913990.jpg","https://cdn.chotot.com/HqeKjmOWXfndzmmmNcLPaOKUEB7ecMNBzmEHeBZL9V0/preset:view/plain/07a5019d9bd80d2dd149422af1bdec93-2999001895432957383.jpg"]}),

L(1378,"ho-chi-minh","th","Студия",5400000,30,
  "Просторная студия с балконом, 30м², ул. Lê Văn Lương, Tân Hưng (Q7) — полная меблировка, лифт, паркинг, рядом TDTU/Lotte Mart.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133239075.htm","сегодня",0,source="chotot",
  details={"contact":"Nhân Bùi","photos":["https://cdn.chotot.com/mYeo1bvEcHRufro2K1QYhSnje6rzI-wqzpXzoOwQJRE/preset:view/plain/b6fd16b78fd2da4cb179592246098133-2990759507291738271.jpg","https://cdn.chotot.com/hGeHfnZAjbDjQ25aTmNyh86wdpac0eUvd2AKa0PcDbM/preset:view/plain/5455db6a66c882ae816e35d37fac986d-2990759507350378830.jpg"]}),

L(1379,"ho-chi-minh","th","Студия",6000000,35,
  "Студия, напротив RMIT/TDTU/Lotte Mart/SC VivoCity, Tân Hưng (Q7) — полная меблировка (Smart TV, кондиционер, холодильник), можно с животными, депозит 1 месяц, охрана и камеры 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134309572.htm","1 день назад",1,source="chotot",
  details={"notice":"цена варьируется по типу окна: 6 млн (обычное окно) / 7,6 млн (с балконом)","contact":"Nguyễn Từ (CHDV Q7)","photos":["https://cdn.chotot.com/k7wBOseF6Cs_UyXicwKgi-6agbcSpRAhYuv5sceCNZw/preset:view/plain/4e98e7fc8da185eab26faff9edb801e7-2998879570211173930.jpg","https://cdn.chotot.com/OZsTGOcLV7cUwQQogD_rvso0jM6bvAyP7wK5fV1IjYY/preset:view/plain/9604d3cdb2df7e1f59c53ea049293217-2998879569953436057.jpg"]}),

L(1380,"ho-chi-minh","tm","Дом",20000000,64,
  "Дом целиком (1 этаж + 3 этажа), переулок ул. Huỳnh Tấn Phát, Tân Mỹ (Q7) — участок 4x16м (64м²), 3 спальни, 3 с/у, полная меблировка, подходит и под небольшой офис/интернет-магазин.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134319649.htm","сегодня",0,source="chotot",
  details={"contact":"LHP","photos":["https://cdn.chotot.com/AVa7QXzbZVDS-ylqKwW8y_nhvZx65cK17IgIVERnat8/preset:view/plain/b98ba7653de06619b8e78534d75055ce-2998989206928565261.jpg","https://cdn.chotot.com/ownU6sRftwJ8UkijRth2SsSh4SUHzxKdp1dD6gncYNQ/preset:view/plain/fefe2a1440d27920b6821e0197691bbc-2998989206681547542.jpg"]}),
L(1381,"ho-chi-minh","kh","Квартира",12000000,35,
  "1-спальная квартира-студия в ЖК River Gate, 155 Bến Vân Đồn, Khánh Hội (Q4) — 35м², полностью меблирована.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/99386324.htm","сегодня",0,source="chotot",
  details={"contact": "Loan Nguyen", "photos": ["https://cdn.chotot.com/8ssskbPOgEcMsA9dATPE7W-q-ObWyIPZwoW6a4EMTKg/preset:view/plain/ca5af63dc4764356458f789197093882-2816127432114907501.jpg", "https://cdn.chotot.com/X0c-0khlHWP0BVjoHj3aKsHZSMvX1v7sHeZyE2GdUwc/preset:view/plain/f6f760368ce3b6f27b0952c14a9a45f6-2816127431208872301.jpg"]}),

L(1382,"ho-chi-minh","kh","Квартира",11000000,35,
  "Офистель (1 спальня) в ЖК Masteri Millennium, 132 Bến Vân Đồn, Khánh Hội (Q4) — 35м², современная мебель.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/118028498.htm","сегодня",0,source="chotot",
  details={"contact": "Loan Nguyen", "photos": ["https://cdn.chotot.com/R3IFOmJyfCOmD9g-vXywUnskOXiwxcNLO3qQFOFAFH8/preset:view/plain/95e66c7c0e9ff6b39f20390c2ae7c424-2888148752845519860.jpg", "https://cdn.chotot.com/aUKHYnhCAfE8wAcKfCyyGuxQONqitz_3p45rZ85OnQc/preset:view/plain/ec9cb5e930117fe7f42e7015a3383049-2888148752661497938.jpg"]}),

L(1383,"ho-chi-minh","kh","Квартира",18000000,74,
  "2-спальная квартира (2 с/у) в ЖК Masteri Millennium, 132 Bến Vân Đồn, Khánh Hội (Q4) — 74м², полная меблировка, бассейн, спортзал, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/117823076.htm","сегодня",0,source="chotot",
  details={"contact": "Loan Nguyen", "photos": ["https://cdn.chotot.com/mM5mKZVwvnE6bSWMfbTssgy2b7wjqXgrIh9IBrzn7bs/preset:view/plain/43b37b02df1f930dcb5d7a29751b6653-2886985782541872413.jpg", "https://cdn.chotot.com/Sm-sdNqbStYM_XVOO8jYbUVtn4BbquXCs1APyCtUEnc/preset:view/plain/6adc1e66e46cf1eb46ef5ea61faded9a-2886985804763816983.jpg"]}),

L(1384,"ho-chi-minh","th","Студия",5500000,35,
  "Сервисная квартира (CHDV) на Đường Số 13, Tân Hưng (Q7), рядом Lotte Mart, ТДТ — 35м², полная меблировка, гибкий договор (депозит 1 месяц), можно с животными.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134320311.htm","сегодня",0,source="chotot",
  details={"notice": "у арендодателя также есть варианты с чердаком (6 млн) и с окном на чердаке (7,6 млн)", "contact": "Nguyễn Từ chuyên CHDV Q7", "photos": ["https://cdn.chotot.com/aT95xsT2jhblS7DMI-QG4WkRXYaEr6dN09zVDglKAnM/preset:view/plain/98667303f3ca04c9fceb5e2181af90cc-2998991505296396367.jpg", "https://cdn.chotot.com/vckp9VIL9QZ7dLOC4xARvSyTkXvNMkDwx936zV28xRs/preset:view/plain/f06a25115e54bef1484e6777622fdc21-2998991505379226390.jpg"]}),

L(1385,"ho-chi-minh","kh","Квартира",19500000,75,
  "2-спальная квартира (2 с/у) в ЖК Masteri Millennium, Khánh Hội (Q4), вид на Bitexco — 75м².",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/129619671.htm","сегодня",0,source="chotot",
  details={"notice": "у арендодателя есть ещё около 15 готовых к показу юнитов в этом доме", "contact": "Căn Hộ Q4 Kim", "photos": ["https://cdn.chotot.com/1qw6Zu4cdHGjO6YvcBKdP0N8JHr6Y0rLC-PR4PKhaZM/preset:view/plain/ecd53c7f971f0e986d414fd6dc872112-2976299825171901025.jpg", "https://cdn.chotot.com/XYuYmgvEN_k1unQSO31dmhoUwLF94RoAeZUK5LNodEY/preset:view/plain/bf4821c506a1ba2cbac3e2c441686131-2976299825212020434.jpg"]}),

L(1386,"ho-chi-minh","tm","Квартира",30000000,103,
  "2-спальная квартира (2 с/у) в ЖК Midtown M8, Phú Mỹ Hưng, Tân Mỹ (Q7) — 103м².",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134318907.htm","сегодня",0,source="chotot",
  details={"contact": "Khỏe Nguyễn BDS PMH Q7", "photos": ["https://cdn.chotot.com/eeCplhAjwei3OfZg4ANL42Urckj_u92gCpw3Eyh_eog/preset:view/plain/32ecd5de935d71c35cb081d209d783cb-2998985226199195398.jpg", "https://cdn.chotot.com/CSMAAoWu2cads4fCVbg7cKbskQOdd6yIVmkLrkoPI7g/preset:view/plain/b8697d4bbfc28ee84a62ef8fd783e54f-2998985226213987622.jpg"]}),

L(1387,"ho-chi-minh","th","Студия",6600000,45,
  "Дуплекс-студия с балконом на Đường Số 13, Tân Hưng (Q7), рядом Lotte Mart, ДХ Tôn Đức Thắng — 45м².",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134318164.htm","сегодня",0,source="chotot",
  details={"contact": "Ken Unitegroup", "photos": ["https://cdn.chotot.com/YmduXbaS7U6acb2qaWvycmdZk63vcEAbUrIm4J1fKYw/preset:view/plain/6e6377f00d0ea91331d264379f201dcb-2998927961553324940.jpg", "https://cdn.chotot.com/0xT66wQRc-_dNxd14wdk_hEsaxbFjyxiYHpC_iqdQe0/preset:view/plain/8bfdc9182b8fc5c754473c8381e1f418-2998927961538209811.jpg"]}),

L(1388,"ho-chi-minh","tm","Квартира",15000000,160,
  "3-спальная квартира большой площади в ЖК Era Town/Đức Khải, ул. Nguyễn Lương Bằng, Tân Mỹ (Q7) — 160м², полная меблировка, депозит 2 месяца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134318094.htm","сегодня",0,source="chotot",
  details={"contact": "Quang Huy", "photos": ["https://cdn.chotot.com/RA7jKpdonDj2C4pI8J9XkIaZBwtX2WmVBn_846MnkjA/preset:view/plain/8c3b690d5524dbdd0be9d659b3487bcf-2998920080250275666.jpg", "https://cdn.chotot.com/j8tfC_QTWAHDd2rCRr6Y-VDo9JWkRu_kSzAJeeUdT9Y/preset:view/plain/d16f1e1dc67069b7237a15608befd043-2998920080288402316.jpg"]}),

L(1389,"ho-chi-minh","kh","Квартира",30000000,108,
  "3-спальная квартира (2 с/у) в ЖК Masteri Millennium, Khánh Hội (Q4) — 108м², полная меблировка, подходит для семьи.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134315363.htm","сегодня",0,source="chotot",
  details={"contact": "Lâm Hậu", "photos": ["https://cdn.chotot.com/shdpTQFsEQOoMZJ-0gxJrgO5IZg17_AQVdNFHqDzRh4/preset:view/plain/a3ec200f46d20b999087660331c5bf66-2998920365903481377.jpg", "https://cdn.chotot.com/6xzQRuzG8k6PgPFTWDw5p-GVQ6q3UZ-bfGUp_se1vsI/preset:view/plain/fd7c85cf6d8cb6ec6ac6600dfe08e655-2998920366023920524.jpg"]}),

L(1390,"ho-chi-minh","tm","Дом",28000000,90,
  "Дом целиком (5x18м, 1 этаж + 3 этажа) в КДЦ Phạm Hữu Lầu, Tân Mỹ (Q7) — 90м², 5 спален, 6 с/у, полная меблировка, подходит для семьи или иностранного специалиста.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/133659480.htm","сегодня",0,source="chotot",
  details={"contact": "Gia Gia", "photos": ["https://cdn.chotot.com/tygTGHjJaRh93cLgsl7sQo34xfEVz4Ch-ZQo1Kl8QaA/preset:view/plain/5ecceb06422559dfb5c25110c415ce9e-2993970305649481518.jpg", "https://cdn.chotot.com/5kFuOQvw7itBsf82U_IvgA6u0KG5p2WprvcZrYQljpY/preset:view/plain/a68a94b2f445850b1ce8b10321400f26-2993970305757299338.jpg"]}),

L(1391,"ho-chi-minh","tm","Дом",120000000,1500,
  "Вилла в Phú Mỹ Hưng, Tân Mỹ (Q7) — участок 15x16м, 1 этаж + 2 этажа, 4 просторные спальни, полная меблировка премиум-класса, охраняемый район.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/132635940.htm","сегодня",0,source="chotot",
  details={"notice": "площадь по данным объявления (1500 м²) не согласуется с указанными габаритами участка 15x16м (240 м²) — вероятно неточность продавца, уточняйте при осмотре", "contact": "Nguyễn Minh Phương", "photos": ["https://cdn.chotot.com/zvv2WTjzuZZaghGBfBvpwn5C11Q1VCglbLOhrpp05NY/preset:view/plain/00c075d4a0518da1e1f68f4a3996c549-2986117847218005721.jpg", "https://cdn.chotot.com/evEiCDXgl_Kjy2d8E0SIUEi-1BQKwhpU5BQgKckkB6E/preset:view/plain/eb51c7d2c43afb939ce34e54a6ab1bc5-2986117847830000843.jpg"]}),

L(1392,"ho-chi-minh","kh","Квартира",20000000,75,
  "Квартира в ЖК Masteri Millennium, 132 Bến Vân Đồn, Khánh Hội (Q4) — от 75м², многие юниты с видом на реку, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/132638654.htm","сегодня",0,source="chotot",
  details={"contact": "Thu Phương", "photos": ["https://cdn.chotot.com/nWBEYNsq4WXn1SkHxJ3NALF_ynzj_yIimJtAnq5l-Jk/preset:view/plain/7444134471350b87a317df146eead353-2986156567677158588.jpg", "https://cdn.chotot.com/Kp6Unugnp1Fydo4PD2g4Rw_OBTDr0e4aMvuzvAMjjiE/preset:view/plain/c558b4358dba9f7733aaac7980dece9f-2986156567454840011.jpg"]}),

L(1393,"ho-chi-minh","th","Дом",11000000,45,
  "Дом целиком (5x9м, 1 этаж + 2 этажа) в переулке на ул. Trần Xuân Soạn, рядом КДЦ Him Lam, Tân Hưng (Q7) — 45м², 3 спальни, 3 с/у, гостиная, кухня.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134314052.htm","сегодня",0,source="chotot",
  details={"contact": "LHP", "photos": ["https://cdn.chotot.com/zUlKJL4et4cy6QUPG4xk_DCcgGtmkKI6dXe64RBBk6E/preset:view/plain/d4a7359439b265393cc40035f9f017b8-2998909729671236492.jpg", "https://cdn.chotot.com/fWp8nCRKTLITcF5a3_-FK271Ug-yQK2fs-3Z15JSC6U/preset:view/plain/7f92a07473572cc42f40ba9ab3f089d1-2998909729448101714.jpg"]}),

L(1394,"ho-chi-minh","tm","Квартира",16000000,124,
  "3-спальная квартира в ЖК Belleza, 15 этаж, Tân Mỹ (Q7) — 124м², просторная, окна во всех спальнях, вид на реку и парк, рядом рынок и кафе.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134309726.htm","сегодня",0,source="chotot",
  details={"contact": "Nguyễn Thị Hạnh", "photos": ["https://cdn.chotot.com/PJAcO3Q_CKAiU3MVsK0aZx0jh0bCnLpeWsLfNulYNB4/preset:view/plain/f3bd5e60bab81aa6b67056053ffbd8e9-2998869392093774419.jpg", "https://cdn.chotot.com/X45gs5iWjgz_wqHCPT3Se7Xj9JbU6AdudH21b8uid9g/preset:view/plain/3e0cd7ebf7d59cf1a6af8bbe90754e05-2998869392789761915.jpg"]}),

L(1395,"ho-chi-minh","th","Квартира",18000000,200,
  "1-спальный пентхаус с отдельной кухней, Tân Hưng (Q7) — заявленная площадь 200м².",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134309389.htm","сегодня",0,source="chotot",
  details={"notice": "необычно большая площадь для 1-спальной планировки и указанной цены — возможна неточность в объявлении, уточняйте при осмотре", "contact": "sala thanh", "photos": ["https://cdn.chotot.com/wSjGRZ-7W6vb7Q69FpNZsFf4MQtM24AQE-P6nSFK1M8/preset:view/plain/df622478296861d7e5c1b4c8b474f3fb-2998878728397643996.jpg", "https://cdn.chotot.com/oQ-fjriA8BLrzUcrAamk5eYN7gOwPpCG3Pdt44D-w4s/preset:view/plain/facbbf0b50fab590473f0548ac036cef-2998878728365093111.jpg"]}),

L(1396,"ho-chi-minh","kh","Студия",5500000,25,
  "Студия с балконом на ул. Đoàn Văn Bơ, Khánh Hội (Q4), рядом ДХ Luật и ДХ Nguyễn Tất Thành — 25м², полная меблировка, вход по отпечатку пальца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134309186.htm","сегодня",0,source="chotot",
  details={"contact": "Thế Hùng", "photos": ["https://cdn.chotot.com/BlTWU_xHVmzwnjAtyQ_Sq-FqkNzLXCNr7lJqsAvFQZY/preset:view/plain/78fa5e1e0e69ab2094a95624f0b8e04e-2998877795982265228.jpg", "https://cdn.chotot.com/c_cfjLcvlud5iuxpVCXMKj6TZr6oFnmY4Ee23_ZbG0w/preset:view/plain/02339bfa27794858966b052dd4bf6207-2998877796053104140.jpg"]}),

L(1397,"ho-chi-minh","th","Студия",4900000,40,
  "Студия в новом здании, Tân Hưng (Q7) — 40м², полностью меблирована, вход по отпечатку пальца, круглосуточная охрана.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133223874.htm","сегодня",0,source="chotot",
  details={"notice": "точный адрес в объявлении не указан — у агента система студий по цене от 4,9 млн в разных домах Q7", "contact": "Nguyễn Phi Long", "photos": ["https://cdn.chotot.com/_jcvTtGmKuPRh4Xy_VsgZ4wuBn_12z6GOkeGrqyRzaM/preset:view/plain/3ba68e6541bd45929c719ef69e761e4d-2990623547964582433.jpg", "https://cdn.chotot.com/_tYF3FPXZ9-bsTLLP3eJz2QODPxSpXk8xChnSEzVxPg/preset:view/plain/3b4986ace10281f054c8d5ea85d66e07-2990623548210580391.jpg"]}),

L(1398,"ho-chi-minh","bth","Студия",6500000,40,
  "Квартира с 2 балконами на ул. Nguyễn Trãi, Bến Thành (Q1), рядом рынок Bến Thành и ДХ Nhân Văn — 40м², полная меблировка, панорамные окна.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-1-tp-ho-chi-minh/134308326.htm","сегодня",0,source="chotot",
  details={"contact": "Vũ Khoa Apartment", "photos": ["https://cdn.chotot.com/DC8n3sBIrKjVjkM0EoTN1iNHeRnKeLRBK70kTJn0o84/preset:view/plain/f5b0d87dd0ec32c8161622958efc39a1-2998872356116989778.jpg", "https://cdn.chotot.com/XAXMELjYbyr7GY-R2CMhrTM1WiA1JAR1J-THEx0PFuc/preset:view/plain/c79d335fe30422a3a31e117117eb8254-2998872356243518988.jpg"]}),
L(1399,"ho-chi-minh","bq","Студия",6500000,45,
  "Студия в доме Tiến Lân Apartment, ул. Bình Quới, Bình Quới (Thanh Đa) — 45м², 1 спальня, окно, тихо, лифт, водонагреватель на солнечных батареях, спортзал, прачечная, фильтр воды, Wi-Fi, рядом Landmark 81 и Thảo Điền.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-binh-thanh-tp-ho-chi-minh/134315847.htm","сегодня",1,source="chotot",
  details={"notice":"в карточке указана цена 6,5 млн ₫/мес, но в тексте объявления также встречается «Studio B301 – 9 млн ₫/мес» (похоже на описание другого юнита в этом же доме) — указана официальная цена карточки объявления.","contact":"Tiến Lân Apartment","photos":["https://cdn.chotot.com/Cup0UHpcDo9Z7icxMay4Bw4jcJ1nld2WdLIU53JPyu8/preset:view/plain/94abd55b9c203154e137de2432530493-2998925054659872455.jpg","https://cdn.chotot.com/v29YZ83BiIHrEhwA3lbUGeC5h6VXuZEce7oH056X5YQ/preset:view/plain/8b884704b1610372887ac76a8132dda4-2998925054830522615.jpg"]}),

L(1400,"ho-chi-minh","th","Квартира",12000000,65,
  "2-спальная квартира (1 с/у), 65м², ЖК M-One Nam Sài Gòn, ул. Bế Văn Cấm, Tân Hưng (Q7) — полная меблировка, залог 24 млн ₫, реальные фото без прикрас.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134307339.htm","1 день назад",1,source="chotot",
  details={"contact":"Võ Tấn Hùng","photos":["https://cdn.chotot.com/h3VM2XPJDJ6tbEurfkopMHAKEGrb1TuWvoAycnRViRs/preset:view/plain/98e70b299bd9eff00864c791020e0297-2998866615736697427.jpg","https://cdn.chotot.com/MbjiV1w1oOpUEf49ikPqlrcQgHsYQJF3fYhea9S2NZc/preset:view/plain/652398621fdcda8df4fc599a3cb890d0-2998866615802000938.jpg"]}),

L(1401,"ho-chi-minh","ak","Студия",8800000,35,
  "Студия/1-спальная квартира индивидуальной планировки, 35м², ул. Trần Não, An Khánh (Thảo Điền/An Phú) — в квартале вилл, много зелени, полная меблировка, вход по отпечатку пальца, свободный график, рядом мост через Sài Gòn и туннель Thủ Thiêm. Залог 8,8 млн ₫.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thu-duc-tp-ho-chi-minh/131731670.htm","2 дня назад",2,source="chotot",
  details={"contact":"Quỳnh Như HiFriendz","photos":["https://cdn.chotot.com/vNd4tcGQgaDX7qc7bYipB2o6292jjlnzW2UimWrzO5U/preset:view/plain/615348a095cb7a4ba7bdfab8587dda1a-2979264075986461222.jpg","https://cdn.chotot.com/gFIABRA-lQbsm0npQVnqpTabGbN4UT7qHRvYp2TnUWo/preset:view/plain/0872b2e832da34a3239aa7e5c58c71ad-2979264076607283750.jpg"]}),

L(1402,"ho-chi-minh","th","Дом",15000000,60,
  "Дом целиком в переулке 118, ул. Nguyễn Thị Thập, Tân Hưng (Q7) — участок 4x15м (60м²), 1 этаж + 2 этажа, 2 спальни, 3 с/у, новый ремонт, полная меблировка. Рядом перекрёсток Nguyễn Văn Linh, университет Marketing, Lotte Mart, рынок Tân Mỹ (~100м), КПЗ Tân Thuận, выставочный центр Phú Mỹ Hưng. Цена договорная для добросовестных арендаторов.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-thi-thap-phuong-tan-hung-14-59/heart-heart-cho-can-hem-118-ep-moi-full-noi-that-pr46204765","4 дня назад",4,source="batdongsan",
  details={"notice":"дата размещения по данным страницы объявления (Ngày đăng): 20.08.2026 — как и на других объявлениях Batdongsan, это может быть датой обновления/переразмещения, а не гарантированно первой публикацией. Цена 15 млн ₫ подтверждена дважды — в карточке выдачи и в блоке «Khoảng giá» на странице объявления.","contact":"Ngọc Trang","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/20/20260820095356-2f5a_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/20/20260820095356-f27f_wm.jpg"]}),
L(1403,"da-lat","xh","Квартира",6500000,30,
  "Меблированная 1-спальная квартира с балконом, ул. Phan Đình Phùng, Xuân Hương — гостиная, спальня, с/у, полная меблировка (холодильник, ТВ, водонагреватель), рядом Nam Á Bank, Winmart, Bách Hóa Xanh, ~3 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134314653.htm","сегодня",0,source="chotot",
  details={"contact":"Hương Lê","photos":["https://cdn.chotot.com/ESnEI6Jq26IxNKVpq2ejtvrhI6CeYO5KkJ3_p7qu7v0/preset:view/plain/8b198a637d3b6ae7a2ff580ca341494d-2998914273611287258.jpg"]}),

L(1404,"da-lat","lv","Квартира",11500000,80,
  "2-спальная квартира с балконом, ул. Trần Quang Khải, Lâm Viên — 1 с/у, вид на долину, полная меблировка (холодильник, ТВ, стиральная машина), общий двор, ~5 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134314528.htm","сегодня",0,source="chotot",
  details={"contact":"Hương Lê","photos":["https://cdn.chotot.com/EpqELwuK-pP9k2lqOsLYxiuxDJMjohK1RlslsHxBBYw/preset:view/plain/81c755c702078eb42ff396deb7d7280b-2998913502304002268.jpg"]}),

L(1405,"da-lat","lv","Квартира",3500000,45,
  "1-спальная квартира с антресолью, ул. Mê Linh, Lâm Viên — базовая меблировка (кровать, водонагреватель, кухонная зона), рядом Bách Hóa Xanh, рынок, спортзал, ~10 мин до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134314396.htm","сегодня",0,source="chotot",
  details={"notice":"меблировка базовая (в структурном поле объявления отмечено «Nhà trống», но в тексте указана базовая мебель)","contact":"Hương Lê","photos":["https://cdn.chotot.com/taMX-k3aNI3SVVHDNI_0Gxc108GosStl1j_gEEgQoiQ/preset:view/plain/e01f5e49d6652b0437cb7cebaabe2141-2998912618945596300.jpg"]}),

L(1406,"da-lat","lv","Квартира",7500000,45,
  "1-спальная квартира, ул. Trương Văn Hoàn, Lâm Viên — полная меблировка (холодильник, стиральная машина, ТВ, диван), ~5 мин до озера Than Thở.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134311932.htm","сегодня",0,source="chotot",
  details={"notice":"цена зависит от этажа — 7,5 млн (3-й этаж) или 8 млн (1-й этаж)","contact":"Hương Lê","photos":["https://cdn.chotot.com/D4UMJFzK0t5OPXWwuGyI8j15UMR_1iyKGwqvSJdjR0s/preset:view/plain/66705e049a964ecd6c33c7ca4e33aeca-2998892933897336332.jpg"]}),

L(1407,"da-lat","lv","Квартира",8000000,50,
  "2-спальная квартира в ЖК Yersin, Lâm Viên — новая полная меблировка, лифт, тихий охраняемый район, 600 м до озера Xuân Hương.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134311179.htm","сегодня",0,source="chotot",
  details={"notice":"цена 8 млн — при контракте от 3 лет; при контракте на 1-2 года цена другая (не указана в объявлении); депозит 2 месяца, оплата за 1","contact":"Minh Anh","photos":["https://cdn.chotot.com/ppJ-3Qgcn6HiUWd3Q0UoK16Lxl2j3AHwj9iDD2welWY/preset:view/plain/3aa33e63c1dbf6c0d196168e17570de9-2998888351407623052.jpg"]}),

L(1408,"da-lat","lv","Квартира",9000000,60,
  "2-спальная квартира с полной меблировкой, ул. Nguyễn Đình Chiểu, Lâm Viên — «заезжай с чемоданом», депозит 1 месяц.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/133600009.htm","2 дня назад",2,source="chotot",
  details={"contact":"Trần Thị Bích Thuỳ","photos":["https://cdn.chotot.com/93A-xa6ShB_fcCn4ZlnmIoXlExUDWMRXQ9U44Nyf1wo/preset:view/plain/2aec2c3908bd144cdd832a312f75e6c9-2993511507454289101.jpg"]}),

L(1409,"da-lat","cl","Дом",21000000,72,
  "Дом целиком на ул. Lê Thánh Tôn, Cam Ly — 1 этаж + 3 надстройки, участок 288м², 4 спальни/5 с/у, кухня, комната для алтаря, сдаётся пустым (без мебели), рядом рынок, школы, больница, АЗС.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134268166.htm","3 дня назад",3,source="chotot",
  details={"notice":"пригоден под небольшой бизнес (кафе, офис, гостевой дом), но не под общепит/бар","contact":"Thanh Thủy","photos":["https://cdn.chotot.com/4NpKlo7WEsYhwMo_3SL5l9pZoRtjatEhfEe0thpTjFI/preset:view/plain/db99c4e55e9e9b23afb218a1f5506074-2998559063886219149.jpg"]}),

L(1410,"phan-thiet","mn","Студия",5000000,32,
  "Студия с видом на море в жилом комплексе Apec Mandala, Mũi Né — 32м², в стоимость входят управление домом и WiFi. Аренда от 6 месяцев до 1 года.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-apec-mandala-wyndham-binh-thuan-phuong-mui-ne-tinh-lam-dong/cho-view-bien-32m-gia-5-trieu-thang-bao-phi-quan-ly-wifi-pr46210314","3 дня назад",3,source="batdongsan",
  details={"contact":"Hoàng My","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/21/20260821111923-4fa4_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/21/20260821111927-6315_wm.jpg"]}),

L(1411,"quy-nhon","qnn","Квартира",6000000,46,
  "1-спальная квартира с полной меблировкой (кондиционер, кровать, холодильник), FLC SeaTower, ул. An Dương Vương, Quy Nhơn Nam; минимальный срок аренды 1 год.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-flc-seatower-phuong-quy-nhon-nam-tinh-gia-lai/cho-ch-1pn-46m2-an-duong-vuong-nguyen-van-500k-em-pr45577797","вчера",1,source="batdongsan",
  details={"contact":"Ngô Minh Hiếu","photos":["https://file4.batdongsan.com.vn/crop/600x315/2025/12/04/20251204084249-11ff_wm.jpg"]}),

L(1412,"quy-nhon","qnn","Квартира",None,108,
  "3-спальная квартира в FLC SeaTower, ул. An Dương Vương, Quy Nhơn Nam, вмещает 8-12 человек, полная меблировка; минимальный срок 6 месяцев.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-flc-seatower-phuong-quy-nhon-nam-tinh-gia-lai/cho-3pn-an-duong-vuong-1-5-trieu-vnd-em-108m2-pr45577841","вчера",1,source="batdongsan",
  details={"notice":"цена по запросу — карточка и детальная страница показывают «Thỏa thuận», в тексте только посуточная ставка (1,5 млн/ночь), помесячная цена не указана","contact":"Ngô Minh Hiếu","photos":["https://file4.batdongsan.com.vn/crop/600x315/2025/12/04/20251204062036-f001_wm.jpg"]}),

L(1413,"quy-nhon","qnn","Студия",6500000,46,
  "Студия в FLC SeaTower, ул. Võ Thị Yến 44, Quy Nhơn Nam — 200 м до моря, меблирована.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-flc-seatower-phuong-quy-nhon-nam-tinh-gia-lai/cho-tot-1pn-45m2-cach-bien-200m-pr46208672","3 дня назад",3,source="batdongsan",
  details={"contact":"Tùng Quy Nhơn Safehome","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/20/20260820232929-8d4c_wm.jpg"]}),

L(1414,"quy-nhon","qn","Квартира",8000000,65,
  "Угловая 2-спальная квартира (2 с/у), Altara Residences, 76 Trần Hưng Đạo, Quy Nhơn — высокий этаж, вид на море, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-altara-residences-phuong-quy-nhon-tinh-gia-lai/cho-residence-1pn-2pn-2wc-2pn-goc-tang-trung-cao-view-bien-full-nt-pr45172456","сегодня",0,source="batdongsan",
  details={"contact":"Mỹ Linh","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/07/20260807142931-622e_wm.jpg"]}),

L(1415,"quy-nhon","qn","Квартира",8000000,65,
  "2-спальная квартира (2 с/у), Phú Tài Residence, ул. Lê Đức Thọ, Quy Nhơn — большой балкон, бассейн на 3 этаже, зал, 5 мин до пляжа Xuân Diệu.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phu-tai-residence-phuong-quy-nhon-tinh-gia-lai/cho-cc-cao-cap-2-phong-ngu-full-nt-7tr-th-view-bien-mat-pr43127816","3 дня назад",3,source="batdongsan",
  details={"contact":"Minh Dũng Land","photos":["https://file4.batdongsan.com.vn/crop/600x315/2025/05/31/20250531084558-b82f_wm.jpg"]}),

L(1416,"quy-nhon","qn","Квартира",8500000,65,
  "Угловая 2-спальная квартира (2 с/у), Altara Residences, ул. Trần Hưng Đạo, этаж 41 — вид на море, полная меблировка, документы готовы.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-altara-residences-phuong-quy-nhon-tinh-gia-lai/cho-residence-6-5tr-7-5tr-th-2pn-2wc-tang-trung-cao-view-bien-pr42954925","3 дня назад",3,source="batdongsan",
  details={"contact":"Minh Dũng Land","photos":["https://file4.batdongsan.com.vn/crop/600x315/2025/03/06/20250306104506-923b_wm.jpg"]}),

L(1417,"quy-nhon","qn","Квартира",8500000,65,
  "2-спальная квартира (2 с/у), Altara Residences, 76 Trần Hưng Đạo — 300 м до моря, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-altara-residences-phuong-quy-nhon-tinh-gia-lai/cho-tot-2pn-65m2-cach-bien-200m-pr46208542","3 дня назад",3,source="batdongsan",
  details={"notice":"похожа на другую квартиру в этом же доме (тот же метраж и близкая цена), но другой контакт/агент — возможна параллельная продажа одного юнита разными брокерами; не объединено из-за отсутствия точного совпадения номера квартиры","contact":"Tùng Quy Nhơn Safehome","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/20/20260820222205-643c_wm.jpg"]}),

L(1418,"quy-nhon","qn","Студия",None,47,
  "Студия в TMS Luxury Hotel & Residences, 28 ул. Nguyễn Huệ — 50 м до моря, вид на город/лагуну Thị Nại, доступ к ресторану, скайбару, бассейну.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-tms-luxury-hotel-residences-phuong-quy-nhon-tinh-gia-lai/cho-pull-man-ngan-han-va-dai-han-lien-he-pr39050214","3 дня назад",3,source="batdongsan",
  details={"notice":"цена по запросу («Thỏa thuận», меняется от срока аренды)","contact":"Nguyễn Lê Nhã Phương","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/03/14/20260314085524-e9c8_wm.jpg"]}),

L(1419,"quy-nhon","qnd","Квартира",3500000,64,
  "Квартира в ЖК Ecolife Riverside, ул. Điện Biên Phủ, Quy Nhơn Đông — полная меблировка, доступны разные планировки у того же продавца.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-ecolife-riverside-phuong-quy-nhon-dong-tinh-gia-lai/cho-chi-tu-3-6-trieu-nha-moi-pr36709073","3 дня назад",3,source="batdongsan",
  details={"contact":"Ngô Minh Hoàn","photos":["https://file4.batdongsan.com.vn/crop/600x315/2023/03/12/20230312143222-8769_wm.jpg"]}),

L(1420,"vung-tau","vtp","Квартира",8000000,30,
  "Меблированная квартира (телевизор, холодильник, кондиционер, стиральная машина, кухня), ул. Hoàng Văn Hòe (C19), Vũng Tàu — ~800 м до пляжа Bãi Sau, ~10 мин на машине до рынка Vũng Tàu.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134313813.htm","сегодня",0,source="chotot",
  details={"contact":"Mùi Phan Thị","photos":["https://cdn.chotot.com/wFg1YuMuCXFl1tAiPgfRLyhkV-wj5MNuAeTT1rYtnhw/preset:view/plain/77623251fc8ef018a29cf9ed4f24d1ec-2998906905357398425.jpg"]}),

L(1421,"vung-tau","rd","Дом",7500000,150,
  "Дом на первой линии по ул. Ba Tháng Hai (3/2), №28, Rạch Dừa — вид на море, рядом парк Sun World Vũng Tàu (салюты), 2 спальни/1 с/у, подходит под жильё или небольшой бизнес.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-vung-tau-ba-ria-vung-tau/134315419.htm","сегодня",0,source="chotot",
  details={"contact":"Phuong Chi","photos":["https://cdn.chotot.com/ZsNz-n2OuSeqhHE_evVFIdfX-70tVYYLgBc5wCOQtJ8/preset:view/plain/9712f1bcd071d09dce838da421d2e99e-2998916394546276371.jpg"]}),

L(1422,"vung-tau","vtp","Дом",12000000,100,
  "Дом 1 этаж + 3 этажа (5×20м), 4 спальни/5 с/у, тихий тупиковый переулок для авто, ул. Lê Lợi, Vũng Tàu — рядом рынок и школа, подходит под семью, офис или онлайн-бизнес.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-loi-1-phuong-vung-tau-tp-ho-chi-minh/cho-ep-1-tret-3-lau-hem-o-to-uong-gia-12tr-thang-pr46213330","2 дня назад",2,source="batdongsan",
  details={"notice":"точной даты публикации сайт не даёт, оценено по дате загрузки фото на CDN (22 авг)","contact":"Nguyễn Ngọc Long","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/22/20260822085447-acd7_wm.jpg"]}),

L(1423,"vung-tau","vtp","Квартира",20000000,80,
  "Квартира в ЖК The Sóng, ул. Thi Sách, Vũng Tàu — 2 спальни/2 с/у, вид на море и башню Tam Thắng, мебель почти новая (99%), только долгосрочная аренда.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-pho-thi-sach-the-song/cho-o-lau-dai-80m2-2pn-2wc-view-truc-dien-bien-va-thap-tam-thang-pr46210093","3 дня назад",3,source="batdongsan",
  details={"notice":"точной даты публикации сайт не даёт, оценено по дате загрузки фото на CDN (21 авг)","contact":"phạm anh phương","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/21/20260821104912-7afe_wm.jpg"]}),

L(1424,"da-nang","ah","Квартира",8500000,50,
  "1-спальная квартира с 2 кондиционерами и своей стиральной машиной на ул. Trần Đình Đàn, An Hải — лифт, паркинг, 300 м до пляжа Phạm Văn Đồng, можно с животными.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134322571.htm","сегодня",0,source="chotot",
  details={"contact":"Thái An","photos":["https://cdn.chotot.com/56PzBNpWBiOtzsEwNBoif7HOR1yBOTHG4pZ9N2lYrD4/preset:view/plain/79f1d192c999d222aa49ba3e6599cf4e-2998999543594553423.jpg"]}),

L(1425,"da-nang","ah","Квартира",17500000,82,
  "2-спальная квартира в ЖК Monarchy (An Trung 2), An Hải — полная меблировка, бассейн, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134321049.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Thị Minh Thư"}),

L(1426,"da-nang","ah","Квартира",8000000,40,
  "1-спальная меблированная квартира на ул. Tô Hiến Thành, An Hải — принимают иностранцев и краткосрочную аренду от 1 месяца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134320946.htm","сегодня",0,source="chotot",
  details={"contact":"Ha for rent APT"}),

L(1427,"da-nang","ah","Квартира",10000000,40,
  "Пентхаус с полной меблировкой на ул. Phạm Tu, An Hải — рядом пляж, животные не разрешены.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134320232.htm","сегодня",0,source="chotot",
  details={"contact":"MrNam Căn Hộ Giá Tốt Đà Nẵng"}),

L(1428,"da-nang","ah","Дом",40000000,210,
  "Дом в закрытом комплексе Euro Village у моста Trần Thị Lý на реке Hàn, An Hải — участок 100м², 4 спальни, охрана 24/7, 1,5 км до моря.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/133708643.htm","сегодня",0,source="chotot",
  details={"contact":"hồ ngọc minh"}),

L(1429,"da-nang","ah","Дом",22000000,75,
  "Дом на 3 спальни (полная меблировка) на ул. Nguyễn Công Trứ, An Hải — тихий переулок, умный замок, Smart TV, 10 мин пешком до моря.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134323156.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Đức Minh Tuấn"}),

L(1430,"da-nang","ah","Дом",18000000,90,
  "3-этажный дом (4 спальни/2 с/у) на ул. Hồ Nghinh, An Hải, рядом с пляжем — без мебели, подходит для жилья и бизнеса.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134322143.htm","сегодня",0,source="chotot",
  details={"contact":"Trân Duy Hải"}),

L(1431,"da-nang","ah","Дом",220000000,155,
  "Здание (8 этажей) с 18 квартирами (студии 25-30м², 1-спальные 30-35м², пентхаус 90м²) + коммерческое помещение у пляжа, р-н Hồ Nghinh, An Hải.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134321307.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"MR HUY"}),

L(1432,"da-nang","ah","Дом",110000000,100,
  "Здание (5 этажей) на 10 квартир (5 студий + 5 1-спальных) на ул. Nguyễn Xuân Khoát, An Hải — антресоль под бизнес.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134321176.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"MR HUY"}),

L(1433,"da-nang","ak","Квартира",5000000,40,
  "1-спальная меблированная квартира на ул. Bùi Tấn Diên, An Khê, рядом с автовокзалом — свободна с 30 августа.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134321478.htm","сегодня",0,source="chotot",
  details={"contact":"Lê Thanh Phong"}),

L(1434,"da-nang","ak","Дом",27000000,100,
  "Дом (3 этажа) с 4 спальнями/4 с/у, полная меблировка, ул. Cần Giuộc, An Khê — ширина фасада 7,5 м.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134307159.htm","сегодня",0,source="chotot",
  details={"contact":"Nhuận Oanh"}),

L(1435,"da-nang","cl2","Квартира",5800000,45,
  "Новая 1-спальная квартира на 4 этаже с балконом на ул. Bình Hòa 15, Cẩm Lệ, рядом университет Đông Á.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134322315.htm","сегодня",0,source="chotot",
  details={"contact":"Apartment Đà Nẵng"}),

L(1436,"da-nang","cl2","Квартира",4400000,40,
  "1-спальная квартира на ул. Bàu Gia Thượng 1, Cẩm Lệ — центр района, 500 м до рынка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134320547.htm","сегодня",0,source="chotot",
  details={"contact":"Đỗ Đăng Khôi"}),

L(1437,"da-nang","cl2","Дом",16000000,280,
  "4-этажный дом (70м²/этаж) с 4 спальнями на ул. Nguyễn Nhàn 100, Cẩm Lệ, напротив больницы Cẩm Lệ, рядом УК района.",
  "https://batdongsan.com.vn/cho-thue-nha-mat-pho-duong-nguyen-nhan_1-phuong-cam-le-tp-da-nang/cho-4-tang-4pn-16-trieu-thuong-luong-tien-100-nhan-uong-10-5m-pr46219871","сегодня",0,source="batdongsan",
  details={"notice":"цена по договорённости («thương lượng»); похожий дом на этой же улице уже есть в базе (48 Nguyễn Nhàn, 125м², 3 этажа), но параметры заметно отличаются (280м² vs 125м², 4 этажа vs 3, №100 vs №48) — не объединено","contact":"Mr.Phúc"}),

L(1438,"da-nang","hx","Студия",5000000,30,
  "Меблированная студия у моста Hòa Xuân, ул. Cồn Dầu 15, Hòa Xuân — своя стиральная машина, терраса на крыше.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/133965392.htm","сегодня",0,source="chotot",
  details={"contact":"CĂN HỘ LKA HOÀ XUÂN"}),

L(1439,"da-nang","hx","Квартира",10000000,85,
  "2-спальная квартира на ул. Vũ Thành Năm, Hòa Xuân — базовая меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134320313.htm","сегодня",0,source="chotot",
  details={"contact":"Công Bình"}),

L(1440,"da-nang","hx","Дом",18000000,100,
  "3-спальный дом (2 этажа, 3 кондиционера), фасад 10,5 м, ул. Mai Chí Thọ, Hòa Xuân.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134322444.htm","сегодня",0,source="chotot",
  details={"contact":"DAVICO LAND"}),

L(1441,"da-nang","hx","Дом",25000000,100,
  "Новый сквозной дом (3 этажа) на ул. Lê Quảng Chí, Hòa Xuân.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134322306.htm","сегодня",0,source="chotot",
  details={"contact":"Mr AN"}),

L(1442,"da-nang","hx","Дом",18000000,100,
  "Новый дом (3 этажа, 3 спальни) на ул. Diên Hồng, Hòa Xuân, полная меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134322068.htm","сегодня",0,source="chotot",
  details={"contact":"Mr AN"}),

L(1443,"da-nang","hx","Дом",23000000,100,
  "Дом (3 этажа, 3 спальни/3 с/у) с полной меблировкой, ул. Mai Chí Thọ (10,5 м), Hòa Xuân.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134322015.htm","сегодня",0,source="chotot",
  details={"contact":"Mr AN"}),

L(1444,"da-nang","hx","Дом",8000000,100,
  "Одноэтажный дом (2 спальни/2 с/у) на ул. Khương Hữu Dụng, Hòa Xuân — кондиционер, парковка на 7 мест, рядом рынок Hòa Xuân.",
  "https://www.nhatot.com/thue-nha-dat-quan-cam-le-da-nang/134254135.htm","3 дня назад",3,source="chotot",
  details={"contact":"Thuỷ DT"}),

L(1445,"da-nang","lc","Квартира",9000000,55,
  "1-спальная меблированная квартира на ул. Nguyễn Lương Bằng 173, Liên Chiểu, рядом университет Bách Khoa — отдельная стирка/сушка, бесплатная уборка раз в месяц.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/107137945.htm","2 дня назад",2,source="chotot",
  details={"contact":"Van Dong Nguyen"}),

L(1446,"da-nang","lc","Квартира",10500000,60,
  "2-спальная квартира, тот же дом на ул. Nguyễn Lương Bằng 173, Liên Chiểu — другая планировка, тот же агент.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/127121957.htm","2 дня назад",2,source="chotot",
  details={"contact":"Van Dong Nguyen"}),

L(1447,"da-nang","lc","Квартира",30000000,97,
  "3-спальная квартира в ЖК MIA Center Point, ул. Ngô Thì Nhậm, Liên Chiểu — полная меблировка, готова к заезду.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mia-center-point-phuong-lien-chieu-tp-da-nang/cho-3-phong-ngu-gia-30-trieu-a-nang-pr46218726","сегодня",0,source="batdongsan",
  details={"notice":"в базе уже есть меньшие юниты этого же ЖК (63-67м², 2 спальни) — этот 97м²/3-спальный явно другой юнит, не дубль","contact":"Nguyễn Lê Vương"}),

L(1448,"da-nang","ns","Квартира",7500000,40,
  "1-спальная квартира, ул. Nguyễn Lữ (Khu Nam Việt Á), Ngũ Hành Sơn, рядом река Hàn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134323185.htm","сегодня",0,source="chotot",
  details={"contact":"Hiền Nguyễn"}),

L(1449,"da-nang","ns","Квартира",32000000,70,
  "2-спальная квартира в ЖК Panoma, ул. Trần Thị Lý, Ngũ Hành Sơn — бассейн, спортзал, охрана 24/7, рядом мост Trần Thị Lý и пляж Mỹ Khê.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134322599.htm","сегодня",0,source="chotot",
  details={"contact":"Kiều Oanh"}),

L(1450,"da-nang","ns","Квартира",32000000,70,
  "Квартира в том же ЖК Panoma, ул. Trần Thị Lý, Ngũ Hành Sơn — параллельное объявление другого агента.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134322008.htm","сегодня",0,source="chotot",
  details={"notice":"параметры идентичны соседнему объявлению этого же ЖК (Panoma, 2 спальни, 70м², 32 млн) — возможно, тот же физический юнит через другого посредника; оставлено отдельно, т.к. номер квартиры не указан ни там, ни там","contact":"My Trần"}),

L(1451,"da-nang","ns","Квартира",20000000,50,
  "1-спальная премиум-квартира, ЖК Panoma 2, ул. Phạm Hữu Kính, Ngũ Hành Sơn.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134321580.htm","сегодня",0,source="chotot",
  details={"contact":"Thanh Trung Haviland"}),

L(1452,"da-nang","ns","Студия",6100000,30,
  "Тихая студия на 4 этаже, кв. 405, ул. Đa Mặn 5, Ngũ Hành Sơn, рядом университет Kinh tế — общая прачечная и терраса; принимают иностранцев (кроме Китая/Индии), без животных/детей.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134321203.htm","сегодня",0,source="chotot",
  details={"contact":"Viết Đức Trần"}),

L(1453,"da-nang","ns","Квартира",14000000,30,
  "1-спальная квартира на ул. Lê Quang Đạo, Ngũ Hành Sơn, рядом пляж Mỹ Khê и Phố Tây An Thượng — можно с животными, есть уборка, wifi.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134321165.htm","сегодня",0,source="chotot",
  details={"contact":"Mr Khanh Haviland"}),

L(1454,"da-nang","ns","Квартира",9900000,48,
  "1-спальная квартира, кв. 202, ул. Đa Mặn 5, Ngũ Hành Sơn — большие окна и балкон, рядом университет Kinh tế.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134320885.htm","сегодня",0,source="chotot",
  details={"contact":"Viết Đức Trần"}),

L(1455,"da-nang","ns","Квартира",18000000,65,
  "2-спальная квартира со 100% новой мебелью, 2 балкона, ул. Trần Quốc Vượng, Khu đô thị FPT, Ngũ Hành Sơn — рядом школа Singapore, река и море.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/132930327.htm","сегодня",0,source="chotot",
  details={"contact":"Hiền Nguyễn"}),

L(1456,"da-nang","ns","Квартира",8500000,50,
  "1-спальная квартира на ул. An Thượng 15, Ngũ Hành Sơn — можно с животными, уборка раз в 2 недели, рядом пляж Mỹ Khê.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134320787.htm","сегодня",0,source="chotot",
  details={"contact":"HAVILAND HOUSE"}),

L(1457,"da-nang","ns","Квартира",5500000,50,
  "1-спальная квартира на ул. Nguyễn Đình Chiểu, Ngũ Hành Sơn, рядом больница на 600 коек и рынок Khuê Mỹ — кондиционер Daikin, стиральная машина Electrolux.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134313622.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Nhật Tân"}),

L(1458,"da-nang","ns","Квартира",5800000,45,
  "1-спальная квартира (кухня отдельно), ул. Nguyễn Xiển 94, Ngũ Hành Sơn, рядом Minh Mạng/Lê Văn Hiến/больница/море — принимают чистых кошек/собак.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134313527.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Nhật Tân"}),

L(1459,"da-nang","ns","Студия",9500000,40,
  "Новая меблированная студия на 5 этаже с балконом и ТВ, ул. Thủy Sơn 4, кв. P501, Ngũ Hành Sơn — въезд с 30 августа.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-ngu-hanh-son-da-nang/134319928.htm","сегодня",0,source="chotot",
  details={"contact":"Huy ho"}),

L(1460,"da-nang","ns","Дом",35000000,102,
  "Меблированный дом (3 этажа, 3 спальни/2 с/у) на ул. Khuê Mỹ Đông, Ngũ Hành Sơn — без животных, не сдаётся гражданам Китая.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134323198.htm","сегодня",0,source="chotot",
  details={"contact":"MR HUY"}),

L(1461,"da-nang","ns","Дом",25000000,78,
  "Меблированный дом (2 этажа, 4 спальни/3 с/у) на ул. Mỹ Đa Đông 8, Ngũ Hành Sơn, рядом рынок Bắc Mỹ An.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134323068.htm","сегодня",0,source="chotot",
  details={"contact":"MR HUY"}),

L(1462,"da-nang","ns","Дом",25000000,90,
  "Дом (3 этажа, 3 спальни/3 с/у) с полной меблировкой, пер. Đa Phước 2 (фасад Nam Việt Á), Ngũ Hành Sơn — принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322934.htm","сегодня",0,source="chotot",
  details={"contact":"Anh Nữ"}),

L(1463,"da-nang","ns","Дом",7500000,60,
  "Дом целиком (1 спальня) в тихом переулке для авто, ул. Chế Lan Viên, Ngũ Hành Sơn — 5 мин пешком до пляжа Mỹ Khê.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322459.htm","сегодня",0,source="chotot",
  details={"contact":"Bích Tuyền"}),

L(1464,"da-nang","ns","Дом",70000000,275,
  "Вилла (5 спален/6 с/у) с бассейном, большой двор, ул. Đặng Đoàn Bằng (Sơn Thuỷ), Ngũ Hành Sơn, рядом Minh Mạng.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322244.htm","сегодня",0,source="chotot",
  details={"contact":"MR HUY"}),

L(1465,"da-nang","ns","Дом",250000000,380,
  "Здание (5 этажей, 17 юнитов: 8 квартир + 9 номеров) с бассейном и лифтом, 150 м до пляжа Mỹ Khê, Ngũ Hành Sơn.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322142.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"MR HUY"}),

L(1466,"da-nang","ns","Дом",100000000,100,
  "Вилла (3 этажа, 5 спален) с бассейном, сауной, джакузи, р-н An Thượng, Ngũ Hành Sơn — новая меблировка.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134322036.htm","сегодня",0,source="chotot",
  details={"contact":"MR HUY"}),

L(1467,"da-nang","ns","Дом",100000000,100,
  "Здание (6 этажей, 8 юнитов) с лифтом и пожарной сигнализацией, р-н Mỹ An, Ngũ Hành Sơn, рядом ул. Chương Dương.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134321793.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"MR HUY"}),

L(1468,"da-nang","ns","Дом",19000000,100,
  "Дом (2 этажа, 2 спальни/2 с/у) с полной меблировкой, р-н Khu FPT (Hoà Hải), Ngũ Hành Sơn — свободен с 3 сентября.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134321692.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng na"}),

L(1469,"da-nang","ns","Дом",22000000,80,
  "Дом (3 этажа, 5 спален/3 с/у + помещение под бизнес) на ул. Ngũ Hành Sơn, рядом университет Kinh tế Đà Nẵng.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/133957612.htm","сегодня",0,source="chotot",
  details={"contact":"Hiền Nguyễn"}),

L(1470,"da-nang","ns","Дом",120000000,300,
  "Вилла (5 спален/6 с/у) с большим бассейном и садом, ул. Chế Lan Viên, Ngũ Hành Sơn — 500 м до Phố Tây An Thượng.",
  "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134287364.htm","2 дня назад",2,source="chotot",
  details={"contact":"NGUYỄN NGỌC SƠN"}),

L(1471,"da-nang","ns","Квартира",11000000,68,
  "2-спальная/2 с/у квартира в ЖК FPT Plaza 2, Ngũ Hành Sơn — полная меблировка, стирально-сушильная машина, бассейн, рядом супермаркет, принимают иностранцев.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-fpt-plaza-2-phuong-ngu-hanh-son-tp-da-nang/chinh-chu-cho-2pn-gia-11-tr-o-ngay-nhan-khach-nuoc-ngoai-pr45753847","3 дня назад",3,source="batdongsan",
  details={"notice":"фото объявления датированы 18 мая 2026 — есть риск, что объявление неактуально/висит давно, стоит проверить при обращении"}),

L(1472,"da-nang","ns","Квартира",15000000,45,
  "Меблированная мини-квартира (стиральная/сушильная машина, кондиционер) на ул. Nguyễn Văn Thoại, Ngũ Hành Sơn, рядом пляж Mỹ Khê, река Hàn, Vincom.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-nguyen-van-thoai-phuong-ngu-hanh-son-tp-da-nang/cho-nhanh-full-noi-that-ay-u-may-giat-say-ieu-hoa-dien-tich-rong-pr46059746","3 дня назад",3,source="batdongsan",
  details={"notice":"фото объявления от 17 июля 2026 — тоже риск неактуальности","contact":"Tấn Sự"}),

L(1473,"da-nang","st","Студия",10000000,37,
  "Студия на высоком этаже гостиничного стандарта в ЖК Golden Bay, ул. 01 Lê Văn Duyệt, Sơn Trà — бассейн, спортзал, минимаркет в здании.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/127786776.htm","сегодня",0,source="chotot",
  details={"contact":"hồ ngọc minh"}),

L(1474,"da-nang","st","Квартира",16000000,76,
  "2-спальная квартира с видом на море, полная меблировка, дом Sơn Trà Ocean View (ул. Ngô Quyền 95), Sơn Trà.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134320825.htm","сегодня",0,source="chotot",
  details={"contact":"MAI CHI LAND"}),

L(1475,"da-nang","st","Квартира",14000000,76,
  "Квартира в том же доме Sơn Trà Ocean View (ул. Ngô Quyền 95), Sơn Trà — другой этаж/юнит.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134319761.htm","сегодня",0,source="chotot",
  details={"contact":"MAI CHI LAND"}),

L(1476,"da-nang","st","Дом",25000000,110,
  "Дом (2 спальни/1 с/у) с двором перед домом, ул. Trương Định (р-н Mân Thái), Sơn Trà, рядом пляж.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134314963.htm","сегодня",0,source="chotot",
  details={"contact":"Phạm Cát"}),

L(1477,"da-nang","st","Дом",30000000,100,
  "Дом (3 этажа, 5 спален, санузел в каждой) с новой противопожарной системой, подходит под хостел/homestay, принимают иностранцев (ул. Chu Huy Mân, Mân Thái, Sơn Trà).",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134322982.htm","сегодня",0,source="chotot",
  details={"contact":"Phạm Cát"}),

L(1478,"da-nang","st","Дом",35000000,360,
  "Дом (участок 180м², 2 этажа, 3 спальни/3 с/у) с премиум-меблировкой, ул. Trần Sâm, Sơn Trà, рядом залив Đà Nẵng и мост Thuận Phước — принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-son-tra-da-nang/134321706.htm","сегодня",0,source="chotot",
  details={"contact":"Nga Lê"}),

L(1479,"da-nang","tk","Квартира",15000000,117,
  "Просторная 3-спальная квартира на высоком этаже, ЖК Hoàng Anh Gia Lai (ул. Hàm Nghi 72), Thanh Khê, рядом аэропорт и центр.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-thanh-khe-da-nang/134322160.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Tuấn"}),

L(1480,"da-nang","tk","Дом",160000000,148,
  "Здание (9 этажей, 48 квартир) с видом на море, ул. Nguyễn Tất Thành, Thanh Khê.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134323123.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"Mr AN"}),

L(1481,"da-nang","tk","Дом",27000000,150,
  "Дом (3 этажа, 65м²/этаж, 3 спальни/4 с/у) с премиум-меблировкой, пер. Huỳnh Ngọc Huệ, Thanh Khê, 2 км до аэропорта — принимают иностранцев.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134322046.htm","сегодня",0,source="chotot",
  details={"contact":"Trung BĐS Dòng Tiền Đà Nẵng"}),

L(1482,"da-nang","tk","Дом",35000000,78,
  "Мини-вилла (3 этажа, 3 спальни/3 с/у) с крытым бассейном, отдельный кабинет, балкон 360°, угловой участок, 100 м до моря, ул. Yên Khê 2, Thanh Khê.",
  "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134288699.htm","2 дня назад",2,source="chotot",
  details={"contact":"Được Phan"}),

L(1483,"da-nang","tk","Квартира",None,94,
  "2-спальная квартира ЖК HAGL Lake View Residence (ул. Hàm Nghi 72), Thanh Khê — бассейн, спортзал, детская площадка, рядом ТЦ GO!, адм. центр, мост Rồng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-hoang-anh-gia-lai-lake-view-residence-phuong-thanh-khe-tp-da-nang/cho-dt-93-8m-4-mat-tien-ngay-trung-tam-a-nang-pr46203271","2 дня назад",2,source="batdongsan",
  details={"notice":"цена по запросу — цифры нет ни на карточке («Giá thỏa thuận»), ни в тексте","contact":"Ms Dung"}),

L(1484,"da-nang","hk","Дом",18000000,100,
  "Дом (3 этажа, 4 спальни/4 с/у) с полной меблировкой, ул. Tú Quỳ (р-н Hòa Minh), Hòa Khánh, фасад 7,5 м — приоритет семьям/компаниям.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-tu-quy-phuong-hoa-khanh-tp-da-nang/cho-3-tang-full-noi-that-18-trieu-1-thang-pr46219445","сегодня",0,source="batdongsan",
  details={"contact":"Xuân Cảm"}),

L(1485,"da-nang","hcg","Дом",150000000,200,
  "Угловой дом (5 этажей, 15 квартир) с 2 фасадами, рядом Lotte Mart и река Hàn, ул. Thăng Long, Hòa Cường.",
  "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134322392.htm","сегодня",0,source="chotot",
  details={"notice":"сдаётся целое здание, не отдельная квартира — цена указана за весь объект","contact":"Mr Zco"}),

L(1486,"da-nang","hcg","Дом",30000000,78,
  "Сквозной дом (4,5×17м, 3 этажа) на торговой ул. Lê Duẩn, Hòa Cường.",
  "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134321079.htm","сегодня",0,source="chotot",
  details={"contact":"Nguyễn Đức Lộc"}),

L(1487,"da-nang","hcg","Квартира",6500000,25,
  "1-спальная квартира на ул. Lưu Quý Kỳ, Hòa Cường (рядом Helio/Sunwheel) — максимум 1-2 человека, животные и иностранцы не принимаются.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/133168205.htm","вчера",1,source="chotot",
  details={"contact":"Thuỷ DT"}),

L(1488,"da-nang","hcg","Квартира",6000000,40,
  "1-спальная квартира с современной техникой (смарт-ТВ, холодильник, индукционная плита), ул. Núi Thành 187, Hòa Cường.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-mini-duong-nui-thanh-phuong-hoa-cuong-tp-da-nang/cho-187-quan-hai-chau-a-gia-chi-6-tr-thang-lh-pr46107388","3 дня назад",3,source="batdongsan",
  details={"notice":"⚠ фото объявления датированы 22.10.2018 — сильное подозрение на просроченное/неактуальное объявление, проверить перед контактом","contact":"Võ Văn Hoàng"}),

L(1489,"da-nang","hcg","Квартира",25000000,76,
  "Угловая 2-спальная квартира на 10 этаже ЖК The Vista Residence (ул. Xô Viết Nghệ Tĩnh 40A), Hòa Cường — вид на фейерверк/реку Hàn/мост Rồng, рядом больница Vinmec, университеты.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-vista-residence-da-nang-phuong-hoa-cuong-tp-da-nang/cho-goc-2pn-a-view-toa-tang-10-dt-76m2-view-phao-song-han-downtown-pr46219360","сегодня",0,source="batdongsan",
  details={"notice":"точная цена встретилась только на карточке поиска, не в тексте объявления — рекомендуется уточнить"}),

L(1490,"da-nang","hc","Квартира",22000000,70,
  "2-спальная квартира в ЖК Sam Towers (ул. Như Nguyệt), Hải Châu — полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134321769.htm","сегодня",0,source="chotot",
  details={"contact":"Hoàng Trưởng"}),

L(1491,"da-nang","hc","Квартира",25000000,131,
  "3-спальная квартира в ЖК Đà Nẵng Plaza (Thạch Thang), Hải Châu — вид на реку Hàn, полная меблировка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/133251940.htm","сегодня",0,source="chotot",
  details={"contact":"Trần Thị Lanh"}),

L(1492,"da-nang","hc","Квартира",8000000,40,
  "1-спальная квартира в 10-этажном доме на ул. Nguyễn Thị Minh Khai 142, Hải Châu — охрана 24/7, приём почты на ресепшн.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134291462.htm","вчера",1,source="chotot",
  details={"contact":"Văn Hiệu Nguyễn"}),

L(1493,"nha-trang","lt","Студия",17000000,45,
  "Студия Mường Thanh Luxury, 60 Trần Phú, Lộc Thọ — рядом с центральной площадью, полностью меблирована, залог 2 месяца.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134322776.htm","сегодня",0,source="chotot",
  details={"contact":"Văn Hoà","photos":["https://cdn.chotot.com/bYIPSYH7E1JCo6C9_F2wZGjy3jaHoaFLp_zANhf40TM/preset:view/plain/30bc6020f4b262b64be0ec5a9b2526a1-2999000449694634975.jpg"]}),

L(1494,"nha-trang","vp","Квартира",20000000,72,
  "2-спальная угловая квартира с балконом, ул. Phạm Văn Đồng, Vĩnh Phước — премиальная мебель, управление 700 тыс/мес, wifi 275 тыс.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134313119.htm","сегодня",0,source="chotot",
  details={"contact":"Runa Vu","photos":["https://cdn.chotot.com/Kw3MrWsBVQkzCleUkyjZjKNBI9QVNlsuHOyE_mibhlU/preset:view/plain/e33c87efb38153b287c738a45d92b477-2998900976936962956.jpg"],"alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-muong-thanh-vien-trieu-phuong-bac-nha-trang-tinh-khanh-hoa/2-phong-ngu-2-toilet-co-ban-cong-goc-thoang-cung-noi-that-cao-cap-pr46217898"}]}),

L(1495,"nha-trang","vt2","Квартира",14000000,68,
  "2-спальная квартира Mường Thanh Khánh Hòa у моста Trần Phú (старый район Xương Huân), Vạn Thạnh — управление и проживание 700 тыс.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134319931.htm","сегодня",0,source="chotot",
  details={"contact":"Văn Hoà","photos":["https://cdn.chotot.com/Qb3tojOm9pnWytfyQAaBrkV6U4E1e6v_aODfgILnsbA/preset:view/plain/d65224358a330be90cf631b103073343-2998990481354597389.jpg"]}),

L(1496,"nha-trang","lt","Студия",5500000,22,
  "Небольшая студия, 132 Hùng Vương, Lộc Thọ — рядом с морем, в районе «Phố Tây», безопасный район.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134298187.htm","вчера",1,source="chotot",
  details={"contact":"Vũ Duy","photos":["https://cdn.chotot.com/6UBlaFBggtDzXIAm0PpjAQJ9_vHWxnRq-vSWznkUKOQ/preset:view/plain/82cf59d689a9717c096ed599999bf6ce-2998911947193928588.jpg"]}),

L(1497,"nha-trang","pl","Квартира",9000000,88,
  "3-спальная квартира, ЖК CCU-01, Phước Long — вид на реку, высокий этаж.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134314646.htm","сегодня",0,source="chotot",
  details={"notice":"без мебели («không nội thất»), депозит 1 платёж×2","contact":"Hà Lương IT","photos":["https://cdn.chotot.com/sSDCb5_refGJ6Da1xh7OcuREHWU2uiTW0JiPrX4RFdw/preset:view/plain/194aa54b88e315f8e295b3a08408b02a-2998914286732674898.jpg"]}),

L(1498,"nha-trang","ps","Квартира",8000000,60,
  "2-спальная квартира CT5, ЖК Vĩnh Điềm Trung (старый район Vĩnh Hiệp), Phương Sài — полностью меблирована, депозит 2×2, контракт на 1 год.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134314620.htm","сегодня",0,source="chotot",
  details={"contact":"Hà Lương IT","photos":["https://cdn.chotot.com/wVilie-7rqHqH5HuZ2oyj0Zi6s8B55omeV_NKKAuctE/preset:view/plain/64676d190c9a0ec9f49f9e543b4c7ce1-2998914026342274582.jpg"]}),

L(1499,"nha-trang","lt","Студия",21000000,68,
  "Люкс-студия 5*, The Costa Nha Trang, 32-34 Trần Phú, Lộc Thọ — King-кровать, бассейн-инфинити, спортзал, частный пляж, охрана 24/7.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/133495451.htm","сегодня",0,source="chotot",
  details={"contact":"Runa Vu","photos":["https://cdn.chotot.com/E-OtjHsqeDoIt3hq2iZJLHzpaUa8QMWtkHqlpMICe5M/preset:view/plain/10a032b7f1fa482732ebaf3214306838-2992715781090394167.jpg"],"alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-the-costa-nha-trang-phuong-nha-trang-tinh-khanh-hoa/cho-cc-30-trieu-vnd-68-m2-gia-sieu-hoi-uy-tin-pr46040104"}]}),

L(1500,"nha-trang","vp","Квартира",24000000,75,
  "2-спальная квартира с видом прямо на море (Hòn Chồng), ул. Phạm Văn Đồng, Vĩnh Phước — высокий этаж, депозит 2×1.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134313247.htm","сегодня",0,source="chotot",
  details={"contact":"Runa Vu","photos":["https://cdn.chotot.com/nNlTgBjBgbWV0naQyih1x4F4lQaPMd6JP8LPEOeu1CA/preset:view/plain/b2472b9c5dd6b5db9998a5ef343fd254-2998901700360636242.jpg"],"alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-muong-thanh-vien-trieu-phuong-bac-nha-trang-tinh-khanh-hoa/2-phong-ngu-2-toilet-view-truc-dien-bien-co-ban-cong-tang-cao-cuc-chill-pr46217907"}]}),

L(1501,"nha-trang","pl","Квартира",14000000,67,
  "2-спальная квартира CCU-01, Phước Long — новая мебель «как новая», высокий этаж, балкон.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134283852.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phan Thị Lan","photos":["https://cdn.chotot.com/bRXnkLQ-PM429s8u_m5GV4eJEtx6bW_qbIsg2KTPZ4s/preset:view/plain/43ed694f6ad24376fc9d38f9161031e2-2998680383627237643.jpg"],"alsoOn":[{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-chung-cu-ccu-01-phuoc-long-phuong-nam-nha-trang-tinh-khanh-hoa/cho-full-noi-that-moi-pr46216867"},{"source":"batdongsan","url":"https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-khu-do-thi-moi-phuoc-long-phuong-nam-nha-trang-tinh-khanh-hoa/cho-ccu01-hud-pl-dt-67m2-2pn-2wc-full-nt-gia-14tr-thg-lh-thanh-pr46213594"}]}),

L(1502,"nha-trang","vt","Дом",45000000,130,
  "Дом (6 спален/6 с/у), КГТ Mỹ Gia (пакет 5), ул. Phùng Hưng (старый район Vĩnh Thái), Vĩnh Trường — 3 этажа, полная качественная мебель.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134314524.htm","сегодня",0,source="chotot",
  details={"contact":"Hà Lương IT","photos":["https://cdn.chotot.com/urtb7uvaGw4IKy1-m0n3Cc2qQ77KFGBZI-ICzHkhqEE/preset:view/plain/c3ac2843bfcb99b24d83e0299789a6cf-2998913470869818252.jpg"]}),

L(1503,"nha-trang","pl","Дом",8000000,200,
  "Дом целиком, фасад ул. Nguyễn Tất Thành, Phước Long — в 200 м от круговой Lê Hồng Phong, 1 этаж+мансарда (5×20м, 100м²/этаж), 3 спальни, 2 с/у, световой колодец, безопасный район без затоплений.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134305793.htm","вчера",1,source="chotot",
  details={"contact":"Phuong","photos":["https://cdn.chotot.com/OF2z67CAmaofmyJ4pOXJ36fN3ZoxrHzAvoQd0YRHqso/preset:view/plain/728183d849b164ab923d347886918a88-2998858850089651084.jpg"]}),

L(1504,"nha-trang","vt","Дом",26000000,100,
  "Дом (3 спальни), КГТ Mỹ Gia (пакет 7), ул. Phùng Hưng, напротив футбольного поля — 3 этажа, полная мебель, свободный первый этаж.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134291250.htm","вчера",1,source="chotot",
  details={"contact":"Phan Thị Lan","photos":["https://cdn.chotot.com/3jtGEHTlMOnrF5bBMkZXqoxmzy0oQ-_d3em5Tv14fnc/preset:view/plain/0b406069d8c8b910c7d612a30f378cc4-2998723603996299106.jpg"]}),

L(1505,"nha-trang","pl","Дом",18000000,173,
  "Дом-фасад ул. Bửu Đoá, Phước Long (6,5×26,6 м), у рынка Bửu Đoá — разрешён свободный бизнес, депозит 2×3.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134280252.htm","2 дня назад",2,source="chotot",
  details={"contact":"Hà Văn Trạch","photos":["https://cdn.chotot.com/aRSXTawenRUKR1wAHQNWt1sAwbhaIznXA1TnsyEw7hU/preset:view/plain/f76d33f3347fe07137fdcba0ad5a8404-2998614614026537046.jpg"]}),

L(1506,"nha-trang","vt","Дом",18000000,200,
  "Вилла (гостиная+3 спальни+4 с/у), КГТ Mỹ Gia (пакет 2), ул. Phùng Hưng, напротив парка — фасад 10 м, 1 этаж+2 уровня, базовая мебель.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134276763.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phan Thị Lan","photos":["https://cdn.chotot.com/2d2WwbqcHqyedYhTw1RciHlUyhCdPvKwWKHtDp7IPdk/preset:view/plain/9cbc588bdd274bb464f7cb71c4144ef1-2998769803284918681.jpg"]}),

L(1507,"nha-trang","vt","Дом",25000000,100,
  "Дом (3 спальни/4 с/у), КГТ Mỹ Gia (пакет 8) / The Capella, ул. Võ Nguyên Giáp (18 м, широкий тротуар) — полная мебель, умное электричество, кондиционер в потолке, бассейн, охрана 24/7.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134276554.htm","2 дня назад",2,source="chotot",
  details={"notice":"в структурном поле площадки указан старый район Vĩnh Hiệp, но текст и проект (Mỹ Gia) явно указывают на Vĩnh Thái — район определён по тексту","contact":"Phan Thị Lan","photos":["https://cdn.chotot.com/O5QRVpywlp8WA00yo3SwfVCQaPZwyoNbL0o7sPPtdps/preset:view/plain/2fe7b4626f31406e840e72b4f940a7a2-2998595039860087923.jpg"]}),

L(1508,"nha-trang","ph","Дом",45000000,450,
  "Коммерческий дом (4 этажа с лифтом), ул. Thích Quảng Đức, Phước Hải — участок 126м², 2 комнаты на этаже со своим с/у, кондиционеры, пожарная сигнализация, тротуар 3 м.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134275397.htm","2 дня назад",2,source="chotot",
  details={"contact":"Nguyễn Trần Duy Phước","photos":["https://cdn.chotot.com/8PTNPsVnAXuvEugFhZt5gHWph362RTAfKa0djKlLPzk/preset:view/plain/987e06e08220be96b7660fe044dc8566-2998590684166048652.jpg"]}),

L(1509,"nha-trang","vt","Дом",18000000,120,
  "Новый хоумстей (2 спальни), ул. Phong Châu, район Vĩnh Thái (запад), рядом с проектом Sun Group — участок 70м², антресоль, ориентация север.",
  "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134274673.htm","2 дня назад",2,source="chotot",
  details={"contact":"Phương GoHome","photos":["https://cdn.chotot.com/892d_hsu7fT9j86Sdf7BHPy0cgfwkvXPlEqjiyb4r5A/preset:view/plain/e6d7197a1aaa5e2371cc69f0d5c2f221-2998588565536394124.jpg"]}),

L(1510,"nha-trang","lt","Квартира",300000000,362,
  "VIP-квартира (4 спальни/4 с/у) на 17 этаже, The Costa Nha Trang, вид на восток — консьерж 24/7, уборка, частный пляж-клуб, спортзал, бассейн.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-the-costa-nha-trang-phuong-nha-trang-tinh-khanh-hoa/cho-vip-4-phong-ngu-trang-pr46218257","сегодня",0,source="batdongsan",
  details={"notice":"⚠ очень высокая цена — люкс-пентхаус, стоит перепроверить актуальность при обращении","contact":"Lê Hữu Khánh"}),

L(1511,"nha-trang","vp","Квартира",None,83,
  "2-спальная квартира, ЖК Scenia Bay, Vĩnh Phước (Bắc Nha Trang) — бассейн-инфинити, сад, детская комната; агент сдаёт несколько типов юнитов.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-scenia-bay-nha-trang-phuong-bac-nha-trang-tinh-khanh-hoa/chuyen-cho-va-van-hanh-gom-studio-1pn-1pn-2pn-2pn-pr46217862","вчера",1,source="batdongsan",
  details={"notice":"цена по запросу","contact":"Nguyễn Thị Hồng"}),

L(1512,"nha-trang","vp","Квартира",None,45,
  "1-спальная квартира, Scenia Bay, 25-26 Phạm Văn Đồng, Vĩnh Phước — свободна с 3 сентября, бассейн-инфинити на 31 этаже, детская комната.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-scenia-bay-nha-trang-phuong-bac-nha-trang-tinh-khanh-hoa/cho-1pn-ay-u-noi-that-1-bedroom-for-rent-pr46217796","вчера",1,source="batdongsan",
  details={"notice":"цена по запросу","contact":"Nguyễn Thị Hồng"}),

L(1513,"nha-trang","vp","Квартира",14000000,94,
  "2-спальная квартира, ЖК Sông Đà Nha Trang, Vĩnh Phước — полная мебель, рядом рынок/школа/супермаркет.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-bai-duong-phuong-bac-nha-trang-tinh-khanh-hoa/cho-song-a-uong-cach-bien-hon-chong-100m-pr46216577","вчера",1,source="batdongsan",
  details={"notice":"точная улица в объявлении не указана, район определён приблизительно по кластеру похожих Bắc Nha Trang объявлений — стоит уточнить"}),

L(1514,"nha-trang","vp","Квартира",9500000,70,
  "2-спальная квартира, Mường Thanh Viễn Triều, район Hòn Chồng, ул. Phạm Văn Đồng, Vĩnh Phước — полная мебель, лифт, охрана, парковка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-muong-thanh-vien-trieu-phuong-bac-nha-trang-tinh-khanh-hoa/cho-gia-chi-tu-9-thang-2-pn-2wc-uc-pr46216424","вчера",1,source="batdongsan",
  details={}),

L(1515,"nha-trang","pl","Квартира",11000000,67,
  "2-спальная квартира CCU-01, Phước Long — новая, полная мебель, балкон юго-восток.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-chung-cu-ccu-01-phuoc-long-phuong-nam-nha-trang-tinh-khanh-hoa/cho-2-pn-2vs-full-noi-that-gia-11-trieu-thang-pr46214858","2 дня назад",2,source="batdongsan",
  details={"contact":"Nguyễn Minh Sâm"}),

L(1516,"nha-trang","lt","Дом",30000000,221,
  "Дом под бизнес с двором, ул. Nguyễn Thiện Thuật, Lộc Thọ (переулок квартала «Phố Tây», фасад 6,6 м) — 1 этаж: двор+открытая площадка+3 спальни+кухня+4 с/у, без мебели, контракт до 5 лет.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-nguyen-thien-thuat-phuong-nha-trang-tinh-khanh-hoa/cho-o-kinh-doanh-san-vuon-221m2-ngang-6-6m-hem-khu-tay-pr46214598","2 дня назад",2,source="batdongsan",
  details={"contact":"Phương Gohome"}),

L(1517,"nha-trang","vt","Дом",20000000,100,
  "Дом (4 спальни/3 с/у), КГТ Mỹ Gia (пакет 3), Vĩnh Thái — 5×20 м, 3 этажа, базовая мебель (кондиционер+кухня); полная меблировка доступна за 22 млн.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-khu-do-thi-my-gia-phuong-nam-nha-trang-tinh-khanh-hoa/cho-4-phong-ngu-o-goi-3-20-trieu-thang-pr46214556","2 дня назад",2,source="batdongsan",
  details={"contact":"Phương Gohome"}),

L(1518,"nha-trang","vn","Дом",140000000,100,
  "Целое здание из 18 комнат (6 этажей + подвал), ул. Tô Hiếu, Vĩnh Nguyên — каждая комната 25-30м² с полной мебелью (кровать, ТВ, холодильник, стиральная/сушильная машина, своя кухня и водонагреватель).",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-to-hieu-phuong-nha-trang-tinh-khanh-hoa/cho-toa-can-ho-18-phong-moi-xay-sieu-ep-co-thang-may-pccc-ay-u-pr46214523","2 дня назад",2,source="batdongsan",
  details={"notice":"сдаётся целое здание, не отдельная комната — цена указана за весь объект","contact":"Phương Gohome"}),

L(1519,"nha-trang","vp","Дом",30000000,154,
  "Новый дом целиком (4 спальни/2 с/у/2 гостиных/2 кухни), Vĩnh Phước, фасад 5 м — у центра/рынка/школы, полная новая мебель.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ngo-den-phuong-bac-nha-trang-tinh-khanh-hoa/moi-xay-full-noi-that-4-phong-ngu-co-san-phia-trang-pr46211264","3 дня назад",3,source="batdongsan",
  details={"contact":"Phương Gohome"}),

L(1520,"nha-trang","ps","Дом",12000000,279.5,
  "Дом с садом, ул. Vĩnh Châu (старый район Vĩnh Hiệp), Phương Sài — рядом ресторан Hoàng Lan/дамба, 200 м от ул. 23/10, сад с прудом с рыбками, 2 этажа, 2 спальни/2 с/у, комната для алтаря, терраса, базовая мебель.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-vinh-chau-phuong-tay-nha-trang-tinh-khanh-hoa/cho-hiep-gan-hang-hoang-lan-ap-nuoc-pr46210704","3 дня назад",3,source="batdongsan",
  details={"contact":"Hồ Quang Minh"}),

L(1521,"nha-trang","vp","Дом",7500000,64,
  "Дом (1 этаж+2 уровня), район Hòn Sện, рядом с ул. Phạm Văn Đồng и морем — 3 спальни/2 с/у, аккуратный, много света.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-bac-nha-trang-tinh-khanh-hoa/cho-hon-sen-1-tret-2-lau-noi-that-ep-gia-7-5-trieu-pr46208909","3 дня назад",3,source="batdongsan",
  details={"notice":"точный район приблизительный (в объявлении нет старого названия района) — стоит уточнить"}),
L(1522,"ho-chi-minh","ak","Студия",7500000,40,
  "Студия/1-спальная квартира с балконом, 40м², ул. Trần Não, An Khánh (бывш. Quận 2) — рядом мост через Sài Gòn, удобный выезд в Q1/Q3/Q5/Q10 и Bình Thạnh, полная меблировка, охраняемая парковка, круглосуточная охрана и камеры, не затапливает.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thu-duc-tp-ho-chi-minh/111628706.htm","4 дня назад",4,source="chotot",
  details={"contact":"Ngọc Thịnh Hifriendz","photos":["https://cdn.chotot.com/GsGv0JHV4Pz2i--NY06aRndMXJk14v01g7I-MplZENY/preset:view/plain/fd4990a46412011868767343119075db-2937131054670844901.jpg","https://cdn.chotot.com/7kROGUXTadDnmxK11TaZD65dzduS30IJ-lxsazd0Gl4/preset:view/plain/7db7b0c008224edb7ecb9a3569ea8d03-2937131054798736558.jpg"]}),

L(1523,"ho-chi-minh","th","Комната",5100000,30,
  "Комната с отдельным санузлом в ЖК Phú Hoàng Anh, рядом Phú Mỹ Hưng, ул. Nguyễn Hữu Thọ, Tân Hưng (Q7) — 30м², кровать, кондиционер, общая кухня и стиральная машина. Причина сдачи — переезд хозяина по работе.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/134263434.htm","4 дня назад",4,source="chotot",
  details={"contact":"Lin Nguyễn","photos":["https://cdn.chotot.com/GtpXlvUKBITO28qSJ8TqPtznG921gXShDa0A9XSU2_g/preset:view/plain/0b67ca187e810d498fee54800b7544c7-2998497080314364057.jpg","https://cdn.chotot.com/pVkl5U91rX2pEanU8vBJw8jTfqPAncx0UjZmxsit_aw/preset:view/plain/1b0785fe302c9ce2e54f7dce35aba819-2998497080374582387.jpg"]}),

L(1524,"ho-chi-minh","tm","Дом",30000000,80,
  "Дом целиком, 4x20м (80м²), 3 этажа, 6 спален, кухня, 3 с/у, 7 кондиционеров. Tân Mỹ (старая P. Tân Phú, Q7), ~300м от рынка Tân Mỹ, удобно для проживания и бизнеса.",
  "https://www.nhatot.com/thue-nha-dat-quan-7-tp-ho-chi-minh/134237230.htm","5 дней назад",5,source="chotot",
  details={"contact":"Thanh Phan","photos":["https://cdn.chotot.com/m-Q-U97hW_juxoFUL9sFYnKvtQ3pXhu5LfK9A7tyZbw/preset:view/plain/3a4cebbd86c5652416f5f2d08b86ea49-2998310724968644761.jpg","https://cdn.chotot.com/PI2TJY7uazMXFgq-xxnBxQNHEjE6a8C-jiRCebv2ZgM/preset:view/plain/43777b6a7bcfb9eea7f5143bcb5f7b5f-2998310724665340817.jpg"]}),

L(1525,"ho-chi-minh","tm","Квартира",40000000,107,
  "3-спальная квартира (2 с/у), 107м², ЖК The Ascentia, ул. Nguyễn Lương Bằng, Tân Mỹ (Phú Mỹ Hưng) — полная меблировка (кондиционеры, кровати, холодильник, плита, ТВ), рядом больница, супермаркет, парк и школы Phú Mỹ Hưng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-the-ascentia-phu-my-hung/cho-3pn-2wc-tai-phuong-tan-tp-chi-minh-pr46221245","сегодня",0,source="batdongsan",
  details={"notice":"дата размещения оценена по диапазону ID объявления Batdongsan (самый свежий на момент проверки) — сайт не публикует исходную дату, это не гарантированно первая публикация. Цена 40 млн ₫ подтверждена дважды — в карточке выдачи и в тексте описания.","contact":"Zoom Land","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152920-ecc5_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152920-e4e0_wm.jpg"]}),

L(1526,"ho-chi-minh","tm","Квартира",30000000,75,
  "2-спальная квартира (2 с/у), 75м², ЖК The Aurora, ул. Nguyễn Lương Bằng, Tân Mỹ (Phú Mỹ Hưng) — новая полная меблировка, свободна, можно въезжать сразу. Цена договорная.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-the-aurora-phu-my-hung/2pn-tang-cao-u-noi-that-cho-gia-30-trieu-thuong-luong-pr46221219","сегодня",0,source="batdongsan",
  details={"notice":"дата размещения оценена по диапазону ID объявления Batdongsan (самый свежий на момент проверки) — сайт не публикует исходную дату. Цена 30 млн ₫ подтверждена дважды — в карточке выдачи и в тексте описания (указана как договорная).","contact":"Huỳnh Quyên","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152632-0010_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152632-8f85_wm.jpg"]}),

L(1527,"ho-chi-minh","tm","Квартира",23000000,49,
  "1-спальная квартира (1 с/у), 49м², ЖК The Aurora (Aurora), Tân Mỹ (Phú Mỹ Hưng) — полная меблировка, свободна, высокий этаж.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-the-aurora-phu-my-hung/1pn-u-noi-that-cho-gia-23-trieu-pr46221176","сегодня",0,source="batdongsan",
  details={"notice":"дата размещения оценена по диапазону ID объявления Batdongsan (самый свежий на момент проверки) — сайт не публикует исходную дату. Цена 23 млн ₫ подтверждена дважды — в карточке выдачи и в тексте описания.","contact":"Huỳnh Quyên","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152138-502c_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824152139-6017_wm.jpg"]}),

L(1528,"ho-chi-minh","kh","Дом",15000000,37,
  "Дом целиком, 37м² (1 этаж + 2 этажа + терраса), 4 спальни (1 внизу), 3 с/у, двор на 10 мотобайков, кондиционеры во всех комнатах. Квартал 20 Thước, рядом Hoàng Diệu/Vĩnh Khánh, Khánh Hội (Q4) — ~300м до Q1 и юрфака ĐH Luật.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-20-thuoc-phuong-khanh-hoi-tp-ho-chi-minh/cho-nguyen-can-moi-khu-20-15tr-thang-pr46221305","сегодня",0,source="batdongsan",
  details={"notice":"дата размещения оценена по диапазону ID объявления Batdongsan (самый свежий на момент проверки) — сайт не публикует исходную дату. Цена 15 млн ₫ подтверждена дважды — в карточке выдачи и в тексте описания.","contact":"Tỉnh","photos":["https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824153850-03a4_wm.jpg","https://file4.batdongsan.com.vn/crop/600x315/2026/08/24/20260824153851-41f1_wm.jpg"]}),
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

# Real points of interest near the tracked HCMC wards (metro/hospitals/international
# schools), fetched from OpenStreetMap Overpass (bbox 10.72,106.66,10.83,106.78) 22 Aug 2026.
# Metro stations are Line 1 (Bến Thành - Suối Tiên), several right by An Khánh (Thảo Điền/An Phú).
POIS = {
    "ho-chi-minh": [
        {"type":"metro","name":"Công viên Văn Thánh","lat":10.7960548,"lon":106.7155056},
        {"type":"metro","name":"Tân Cảng","lat":10.7985879,"lon":106.7232392},
        {"type":"metro","name":"Thảo Điền","lat":10.8004871,"lon":106.7336512},
        {"type":"metro","name":"An Phú","lat":10.8021337,"lon":106.7422498},
        {"type":"metro","name":"Rạch Chiếc","lat":10.8085535,"lon":106.755277},
        {"type":"metro","name":"Phước Long","lat":10.821435,"lon":106.758185},
        {"type":"school","name":"Renaissance International School Saigon","lat":10.7817518,"lon":106.6869549},
        {"type":"school","name":"European International School HCMC","lat":10.8055241,"lon":106.7346208},
        {"type":"hospital","name":"Columbia Asia Saigon","lat":10.7795758,"lon":106.6965213},
        {"type":"hospital","name":"Bệnh viện Đa khoa Tân Hưng","lat":10.7515951,"lon":106.696342},
        {"type":"hospital","name":"Bệnh Viện Mắt Sài Gòn","lat":10.7713711,"lon":106.6909391},
        {"type":"hospital","name":"Bệnh viện Quận 1 (cơ sở 2)","lat":10.7651115,"lon":106.6932273},
        {"type":"hospital","name":"Bệnh Viện Sài Gòn ITO","lat":10.7950017,"lon":106.6672345},
        {"type":"hospital","name":"Bệnh viện Phụ sản Mekong","lat":10.7998479,"lon":106.6675233},
    ]
}

DATA = {
    "CITIES": CITIES, "SOURCES": SOURCES,
    "LISTINGS": LISTINGS, "WARD_BOUNDARIES": WARD_BOUNDARIES, "POIS": POIS
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
  .poi-toggle-label{display:inline-flex;align-items:center;gap:6px;cursor:pointer;}
  .poi-marker{border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;box-shadow:0 1px 3px rgba(0,0,0,0.35);border:1.5px solid #fff;}
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
  .listing-photos{display:flex;gap:4px;overflow-x:auto;-webkit-overflow-scrolling:touch;}
  .listing-photo{flex:0 0 auto;width:110px;aspect-ratio:4/3;object-fit:cover;border-radius:var(--radius-sm);background:var(--surface-2);display:block;cursor:zoom-in;}
  .listing-photos .listing-photo:only-child{flex-basis:100%;width:100%;}

  .lightbox{position:fixed;inset:0;z-index:1000;background:rgba(10,14,8,0.92);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:24px;}
  .lightbox[hidden]{display:none;}
  .lightbox-main{max-width:min(900px,90vw);max-height:70vh;object-fit:contain;border-radius:var(--radius-sm);background:var(--surface-2);}
  .lightbox-close{position:absolute;top:16px;right:20px;background:transparent;border:none;color:#fff;font-size:1.6rem;cursor:pointer;line-height:1;padding:6px 10px;}
  .lightbox-nav{position:absolute;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.12);border:none;color:#fff;font-size:2.2rem;width:48px;height:48px;border-radius:50%;cursor:pointer;line-height:1;}
  .lightbox-nav:hover{background:rgba(255,255,255,0.24);}
  .lightbox-prev{left:16px;}
  .lightbox-next{right:16px;}
  .lightbox-thumbs{display:flex;gap:6px;overflow-x:auto;max-width:90vw;padding:4px;}
  .lightbox-thumbs img{flex:0 0 auto;width:64px;height:48px;object-fit:cover;border-radius:6px;cursor:pointer;opacity:0.55;border:2px solid transparent;}
  .lightbox-thumbs img.active{opacity:1;border-color:var(--accent);}
  .listing-top{display:flex;justify-content:space-between;align-items:center;gap:8px;}
  .source-pill{display:inline-flex;align-items:center;gap:6px;font-size:0.72rem;font-weight:700;color:var(--ink-dim);background:var(--surface-2);border-radius:999px;padding:4px 10px;text-transform:uppercase;letter-spacing:0.03em;}
  .source-pill i{width:7px;height:7px;border-radius:50%;background:var(--danger);}
  .posted{font-size:0.76rem;color:var(--ink-faint);}

  .listing-type{font-size:0.78rem;font-weight:700;color:var(--gold);text-transform:uppercase;letter-spacing:0.03em;}
  .listing-meta{font-size:0.86rem;color:var(--ink-dim);}
  .listing-desc{font-size:0.92rem;color:var(--ink);margin:0;}

  .listing-notice{font-size:0.82rem;background:var(--warn-bg);color:var(--warn-ink);padding:8px 10px;border-radius:var(--radius-sm);font-weight:600;}
  .listing-also{font-size:0.8rem;color:var(--ink-faint);margin:0;}
  .listing-also a{color:var(--accent);text-decoration:underline;}

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
  .price-change{display:block;font-size:0.72rem;font-weight:600;}
  .price-change.down{color:var(--accent);}
  .price-change.up{color:var(--danger);}
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
        <label class="poi-toggle-label"><input type="checkbox" id="poi-toggle">метро / школы / госпитали</label>
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
    <p class="stamp">Данные актуальны на __TODAY_DATE__ · объявления старше 30 дней исключены из подборки · перед созвоном с хозяином всегда проверяйте цену и наличие по ссылке на объявление.</p>
  </footer>

</div>

<div id="lightbox" class="lightbox" hidden>
  <button type="button" class="lightbox-close" id="lightbox-close" aria-label="Закрыть">✕</button>
  <button type="button" class="lightbox-nav lightbox-prev" id="lightbox-prev" aria-label="Предыдущее фото">‹</button>
  <img class="lightbox-main" id="lightbox-main" src="" alt="">
  <button type="button" class="lightbox-nav lightbox-next" id="lightbox-next" aria-label="Следующее фото">›</button>
  <div class="lightbox-thumbs" id="lightbox-thumbs"></div>
</div>

<script>
(function(){
  "use strict";

  var DATA = __DATA_JSON__;
  var CITIES = DATA.CITIES;
  var SOURCES = DATA.SOURCES;
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
  var POIS = DATA.POIS || {};
  var POI_STYLE = {
    metro: {bg:"#1E6FBF", icon:"🚇"},
    school: {bg:"#7A3FA0", icon:"🎓"},
    hospital: {bg:"#B44430", icon:"✚"}
  };
  var leafletMap = null, wardLayerGroup = null, markerLayerGroup = null, poiLayerGroup = null, leafletReady = false;
  var wardLayerByKey = {};
  var showPois = false;

  function initLeafletMap(){
    if (leafletMap || typeof L === "undefined") return;
    leafletMap = L.map("leaflet-map", {scrollWheelZoom:true});
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors'
    }).addTo(leafletMap);
    wardLayerGroup = L.layerGroup().addTo(leafletMap);
    markerLayerGroup = L.layerGroup().addTo(leafletMap);
    poiLayerGroup = L.layerGroup().addTo(leafletMap);
    leafletReady = true;
    var poiToggle = document.getElementById("poi-toggle");
    if (poiToggle){
      poiToggle.addEventListener("change", function(){
        showPois = poiToggle.checked;
        renderPois(state.city);
      });
    }
  }

  function renderPois(cityKey){
    if (!leafletReady) return;
    poiLayerGroup.clearLayers();
    if (!showPois) return;
    var list = POIS[cityKey];
    if (!list) return;
    list.forEach(function(p){
      var style = POI_STYLE[p.type] || {bg:"#666", icon:"•"};
      var icon = L.divIcon({
        className: "",
        html: '<div class="poi-marker" style="background:'+style.bg+';width:22px;height:22px;">'+style.icon+'</div>',
        iconSize: [22,22], iconAnchor: [11,11]
      });
      L.marker([p.lat, p.lon], {icon: icon}).bindTooltip(p.name).addTo(poiLayerGroup);
    });
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
    renderPois(state.city);
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
      if (l.details && l.details.duplicateOf) return false;
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
      var photos = l.details && l.details.photos;
      var photoHtml = (photos && photos.length)
        ? '<div class="listing-photos">' + photos.map(function(p, i){
            return '<img class="listing-photo" data-idx="' + i + '" src="' + p + '" alt="" loading="lazy" onerror="this.remove()">';
          }).join('') + '</div>'
        : "";
      var alsoOn = l.details && l.details.alsoOn;
      var alsoOnHtml = (alsoOn && alsoOn.length)
        ? '<p class="listing-also">Также встречается на: ' + alsoOn.map(function(a){
            var s = SOURCE_LABEL[a.source];
            return '<a href="' + a.url + '" target="_blank" rel="noopener">' + (s ? s.short : a.source) + '</a>';
          }).join(', ') + '</p>'
        : "";
      var priceHistory = l.details && l.details.priceHistory;
      var priceChangeHtml = "";
      if (priceHistory && priceHistory.length && l.price !== null){
        var prevPrice = priceHistory[priceHistory.length-1].price;
        if (prevPrice !== l.price){
          var down = l.price < prevPrice;
          priceChangeHtml = '<span class="price-change ' + (down?"down":"up") + '">' + (down?"↓":"↑") +
            ' было ' + fmtPrice(prevPrice) + ' ₫</span>';
        }
      }
      card.innerHTML =
        photoHtml +
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
        alsoOnHtml +
        detailsHtml(l) +
        '<div class="listing-bottom">' +
          '<span><span class="price">' + (l.price===null ? "цена по запросу" : (fmtPrice(l.price) + ' <small>₫ / мес</small>')) + '</span>' + priceChangeHtml + '</span>' +
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
      if (photos && photos.length){
        card.querySelectorAll(".listing-photo").forEach(function(img){
          img.addEventListener("click", function(){
            openLightbox(photos, Number(img.getAttribute("data-idx")));
          });
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

  var lightboxPhotos = [], lightboxIndex = 0;
  var lightboxEl = document.getElementById("lightbox");
  var lightboxMain = document.getElementById("lightbox-main");
  var lightboxThumbs = document.getElementById("lightbox-thumbs");

  function renderLightbox(){
    lightboxMain.src = lightboxPhotos[lightboxIndex];
    lightboxThumbs.innerHTML = "";
    if (lightboxPhotos.length > 1){
      lightboxPhotos.forEach(function(p, i){
        var t = document.createElement("img");
        t.src = p;
        t.loading = "lazy";
        t.className = (i === lightboxIndex) ? "active" : "";
        t.addEventListener("click", function(){ lightboxIndex = i; renderLightbox(); });
        lightboxThumbs.appendChild(t);
      });
    }
  }

  function openLightbox(photos, index){
    lightboxPhotos = photos; lightboxIndex = index;
    renderLightbox();
    lightboxEl.removeAttribute("hidden");
  }

  function closeLightbox(){ lightboxEl.setAttribute("hidden", ""); }

  function lightboxStep(delta){
    lightboxIndex = (lightboxIndex + delta + lightboxPhotos.length) % lightboxPhotos.length;
    renderLightbox();
  }

  document.getElementById("lightbox-close").addEventListener("click", closeLightbox);
  document.getElementById("lightbox-prev").addEventListener("click", function(){ lightboxStep(-1); });
  document.getElementById("lightbox-next").addEventListener("click", function(){ lightboxStep(1); });
  lightboxEl.addEventListener("click", function(e){ if (e.target === lightboxEl) closeLightbox(); });
  document.addEventListener("keydown", function(e){
    if (lightboxEl.hasAttribute("hidden")) return;
    if (e.key === "Escape") closeLightbox();
    else if (e.key === "ArrowLeft") lightboxStep(-1);
    else if (e.key === "ArrowRight") lightboxStep(1);
  });

  initLeafletMap();
  renderCityTabs(); renderCityMap(); setupBudgetSlider(); renderBudgetChips(); renderDaysChips(); renderSourceChips(); renderTypeChips(); applyFilters();
})();
</script>
"""

HTML = HTML.replace("__DATA_JSON__", DATA_JSON)
HTML = HTML.replace("__LISTING_COUNT__", str(len(LISTINGS)))
HTML = HTML.replace("__TODAY_DATE__", ru_today_stamp())

out_path = W + "/vietnam-rent-finder.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print("Wrote", out_path, "size", len(HTML))
