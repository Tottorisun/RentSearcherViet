# -*- coding: utf-8 -*-
import json, re
import datetime

RU_MONTHS_GENITIVE = ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]
def ru_today_stamp():
    d = datetime.date.today()
    return f"{d.day} {RU_MONTHS_GENITIVE[d.month-1]} {d.year}"

EN_MONTHS = ["January","February","March","April","May","June",
             "July","August","September","October","November","December"]

def en_today_stamp():
    d = datetime.date.today()
    return f"{d.day} {EN_MONTHS[d.month-1]} {d.year}"

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
        "name": "Нячанг", "nameEn": "Nha Trang",
        "districts": [
            {"key":"vh","name":"Vĩnh Hải","hint":"север, Хон Чонг","hintEn":"north, Hon Chong","color":"#4E79A7"},
            {"key":"vp","name":"Vĩnh Phước","hint":"север, Mường Thanh Viễn Triều","hintEn":"north, Muong Thanh Vien Trieu","color":"#F28E2B"},
            {"key":"vt2","name":"Vạn Thạnh","hint":"центр-север, старый город","hintEn":"centre-north, old town","color":"#B07AA1"},
            {"key":"ps","name":"Phương Sài","hint":"у ж/д вокзала","hintEn":"by the railway station","color":"#76B7B2"},
            {"key":"nh","name":"Ngọc Hiệp","hint":"запад, у реки Cái","hintEn":"west, by the Cai river","color":"#E15759"},
            {"key":"ph","name":"Phước Hải","hint":"рынок Chợ Đầm, Hà Quang 2","hintEn":"Cho Dam market, Ha Quang 2","color":"#EDC949"},
            {"key":"lt","name":"Lộc Thọ","hint":"центр, набережная Trần Phú","hintEn":"centre, Tran Phu seafront","color":"#9C755F"},
            {"key":"ph2","name":"Phước Hòa","hint":"центр-запад, Lam Sơn","hintEn":"centre-west, Lam Son","color":"#D37295"},
            {"key":"tl","name":"Tân Lập","hint":"центр, «русский квартал»","hintEn":"centre, the \"Russian quarter\"","color":"#86BCB6"},
            {"key":"pl","name":"Phước Long","hint":"запад, спальный район, HUD","hintEn":"west, residential, HUD","color":"#FF9DA7"},
            {"key":"vt","name":"Vĩnh Trường","hint":"юг, An Viên","hintEn":"south, An Vien","color":"#F1CE63"},
            {"key":"vn","name":"Vĩnh Nguyên","hint":"юг, паром на Хон Тре","hintEn":"south, ferry to Hon Tre","color":"#D4A6C8"},
            # Четыре укрупнённых района после реформы 2025 года. Chợ Tốt отдаёт
            # ТОЛЬКО их (ward_name_v3 = «Phường Bắc Nha Trang» и т.д.), поэтому без
            # них Нячанг не собирался программой вовсе. Двенадцать прежних оставлены
            # рядом: 61 заведённая строка стоит на них, а объявления из Телеграма и
            # Facebook по-прежнему называют привычные Лок Тхо и Тан Лап.
            #
            # ОНИ ГЕОГРАФИЧЕСКИ ПЕРЕКРЫВАЮТСЯ, и это осознанно (решение владельца
            # 9 сентября 2026: «и так и так ищи»). Состав каждого нового района из
            # прежних НЕ указан намеренно: попытка вывести его точкой-в-полигоне
            # дала явную чушь -- «Тэй» не получил ни одного, а южные Виньчыонг и
            # Виньнгуен попали в центральный, потому что координаты прежних
            # районов в NT_APPROX сами расставлены на глаз. Пишем только сторону
            # света, которая названа в самом имени района.
            {"key":"nt","name":"Phường Nha Trang","hint":"центр, укрупнённый район реформы 2025 года","hintEn":"centre, an enlarged ward from the 2025 reform","color":"#59A14F"},
            {"key":"btr","name":"Phường Bắc Nha Trang","hint":"север, укрупнённый район реформы 2025 года","hintEn":"north, an enlarged ward from the 2025 reform","color":"#499894"},
            {"key":"ttr","name":"Phường Tây Nha Trang","hint":"запад, укрупнённый район реформы 2025 года","hintEn":"west, an enlarged ward from the 2025 reform","color":"#B6992D"},
            {"key":"ntr","name":"Phường Nam Nha Trang","hint":"юг, укрупнённый район реформы 2025 года","hintEn":"south, an enlarged ward from the 2025 reform","color":"#79706E"}
        ]
    },
    "da-lat": {
        "name": "Далат", "nameEn": "Da Lat",
        "districts": [
            {"key":"xh","name":"Phường Xuân Hương - Đà Lạt","hint":"центр, озеро Xuân Hương","hintEn":"centre, Xuan Huong lake"},
            {"key":"lv","name":"Phường Lâm Viên - Đà Lạt","hint":"юго-восток, у университета","hintEn":"south-east, by the university"},
            {"key":"xt","name":"Phường Xuân Trường - Đà Lạt","hint":"восток, пригород","hintEn":"east, suburbs"},
            {"key":"cl","name":"Phường Cam Ly - Đà Lạt","hint":"запад","hintEn":"west"},
            {"key":"lb","name":"Phường Lang Biang - Đà Lạt","hint":"север, Măng Lin и гора Лангбианг","hintEn":"north, Mang Lin and Langbiang mountain"}
        ]
    },
    "da-nang": {
        "name": "Дананг", "nameEn": "Da Nang",
        "districts": [
            {"key":"hc","name":"Phường Hải Châu","hint":"центр","hintEn":"centre"},
            {"key":"hcg","name":"Phường Hòa Cường","hint":"центр-юг, много sleepbox/студий","hintEn":"centre-south, lots of sleepbox/studios"},
            {"key":"tk","name":"Phường Thanh Khê","hint":"центр-север","hintEn":"centre-north"},
            {"key":"ak","name":"Phường An Khê","hint":"запад-центр","hintEn":"west-central"},
            {"key":"cl2","name":"Phường Cẩm Lệ","hint":"юг","hintEn":"south"},
            {"key":"hx","name":"Phường Hòa Xuân","hint":"юг, за рекой","hintEn":"south, across the river"},
            {"key":"ns","name":"Phường Ngũ Hành Sơn","hint":"юго-восток, пляж Mỹ An, рядом FPT","hintEn":"south-east, My An beach, near FPT"},
            {"key":"st","name":"Phường Sơn Trà","hint":"полуостров, пляж Mỹ Khê","hintEn":"peninsula, My Khe beach"},
            {"key":"ah","name":"Phường An Hải","hint":"восток, у реки","hintEn":"east, riverside"},
            {"key":"lc","name":"Phường Liên Chiểu","hint":"север","hintEn":"north"},
            {"key":"hk","name":"Phường Hòa Khánh","hint":"северо-запад, студенческий район","hintEn":"north-west, student area"}
        ]
    },
    "vung-tau": {
        "name": "Вунгтау", "nameEn": "Vung Tau",
        "districts": [
            {"key":"vtp","name":"Phường Vũng Tàu","hint":"центр, все старые пляжи Bãi Trước/Bãi Sau","hintEn":"centre, the classic Bai Truoc/Bai Sau beaches"},
            {"key":"rd","name":"Phường Rạch Dừa","hint":"север, у залива Bãi Trước","hintEn":"north, by Bai Truoc bay"},
            {"key":"pth","name":"Phường Phước Thắng","hint":"юг, аэропорт, Bãi Sau на юге","hintEn":"south, airport, Bai Sau further south"},
            {"key":"tth","name":"Phường Tam Thắng","hint":"дальний север, Лонг Шон, промзона","hintEn":"far north, Long Son, industrial area"}
        ]
    },
    "quy-nhon": {
        "name": "Куинён", "nameEn": "Quy Nhon",
        "districts": [
            {"key":"qn","name":"Phường Quy Nhơn","hint":"центр, пляж Xuân Diệu","hintEn":"centre, Xuan Dieu beach"},
            {"key":"qnd","name":"Phường Quy Nhơn Đông","hint":"восток, полуостров Nhơn Lý/Nhơn Hải, Kỳ Co","hintEn":"east, Nhon Ly/Nhon Hai peninsula, Ky Co"},
            {"key":"qnt","name":"Phường Quy Nhơn Tây","hint":"запад, Bùi Thị Xuân","hintEn":"west, Bui Thi Xuan"},
            {"key":"qnn","name":"Phường Quy Nhơn Nam","hint":"юг, Ghềnh Ráng, Quy Hòa","hintEn":"south, Ghenh Rang, Quy Hoa"},
            {"key":"qnb","name":"Phường Quy Nhơn Bắc","hint":"север, Nhơn Phú","hintEn":"north, Nhon Phu"}
        ]
    },
    "hoi-an": {
        "name": "Хойан", "nameEn": "Hoi An",
        "districts": [
            {"key":"ha","name":"Phường Hội An","hint":"старый город, центр","hintEn":"old town, centre"},
            {"key":"had","name":"Phường Hội An Đông","hint":"восток, пляж Cửa Đại","hintEn":"east, Cua Dai beach"},
            {"key":"hat","name":"Phường Hội An Tây","hint":"запад, пляж An Bàng/Tân Thành","hintEn":"west, An Bang/Tan Thanh beach"}
        ]
    },
    "phan-thiet": {
        "name": "Фантьет / Муйне", "nameEn": "Phan Thiet / Mui Ne",
        "districts": [
            {"key":"mn","name":"Phường Mũi Né","hint":"курортная зона, Хам Тьен, пляж Мюйне","hintEn":"resort strip, Ham Tien, Mui Ne beach"},
            {"key":"pt","name":"Phường Phan Thiết","hint":"центр города","hintEn":"city centre"},
            {"key":"put","name":"Phường Phú Thủy","hint":"центр-восток, у моря","hintEn":"centre-east, by the sea"},
            {"key":"bt","name":"Phường Bình Thuận","hint":"запад, аэропорт","hintEn":"west, airport"},
            {"key":"tt","name":"Phường Tiến Thành","hint":"юг, пляж Đồi Dương","hintEn":"south, Doi Duong beach"},
            {"key":"hth","name":"Phường Hàm Thắng","hint":"северо-запад, вдали от моря","hintEn":"north-west, away from the sea"}
        ]
    },
    "ho-chi-minh": {
        "name": "Хошимин", "nameEn": "Ho Chi Minh City",
        "districts": [
            {"key":"tm","name":"Phường Tân Mỹ","hint":"Phú Mỹ Hưng, ЖК The Ascentia и рядом","hintEn":"Phu My Hung, The Ascentia and nearby"},
            {"key":"th","name":"Phường Tân Hưng","hint":"Phú Mỹ Hưng, ядро — Crescent Mall, Cầu Ánh Sao","hintEn":"Phu My Hung core — Crescent Mall, Cau Anh Sao"},
            {"key":"ak","name":"Phường An Khánh","hint":"Thảo Điền, экспат-район, Masteri Thảo Điền","hintEn":"Thao Dien, expat area, Masteri Thao Dien"},
            {"key":"btr","name":"Phường Bình Trưng","hint":"An Phú восточнее — Estella Heights, Palm Heights","hintEn":"An Phu, further east — Estella Heights, Palm Heights"},
            {"key":"bq","name":"Phường Bình Quới","hint":"полуостров Thanh Đa","hintEn":"Thanh Da peninsula"},
            {"key":"bth","name":"Phường Bến Thành","hint":"исторический центр, бывший Quận 1","hintEn":"historic centre, former District 1"},
            {"key":"kh","name":"Phường Khánh Hội","hint":"бывший Quận 4, рядом с центром, набирает популярность","hintEn":"former District 4, next to downtown, up-and-coming"}
        ]
    },
    "ha-noi": {
        "name": "Ханой", "nameEn": "Hanoi",
        "districts": [
            {"key":"tyh","name":"Tây Hồ","hint":"Западное озеро, главный экспат-район","hintEn":"West Lake, the main expat area","color":"#4E79A7"},
            {"key":"bd","name":"Ba Đình","hint":"правительственный квартал, посольства","hintEn":"government quarter, embassies","color":"#F28E2B"},
            {"key":"hkm","name":"Hoàn Kiếm","hint":"Старый квартал, озеро Хоанкьем","hintEn":"Old Quarter, Hoan Kiem lake","color":"#E15759"},
            {"key":"cg","name":"Cầu Giấy","hint":"запад, офисный кластер, Trung Hòa","hintEn":"west, office cluster, Trung Hoa","color":"#76B7B2"},
            {"key":"ntl","name":"Nam Từ Liêm","hint":"Mỹ Đình, корейский квартал, Vinhomes Smart City","hintEn":"My Dinh, Korean quarter, Vinhomes Smart City","color":"#B07AA1"},
            {"key":"dd","name":"Đống Đa","hint":"центр-запад, плотная старая застройка","hintEn":"centre-west, dense older housing","color":"#EDC949"},
            {"key":"hbt","name":"Hai Bà Trưng","hint":"юго-восток центра, Times City","hintEn":"south-east of the centre, Times City","color":"#9C755F"},
            {"key":"lbn","name":"Long Biên","hint":"за Красной рекой, Vinhomes Riverside","hintEn":"across the Red River, Vinhomes Riverside","color":"#D37295"},
            {"key":"tx","name":"Thanh Xuân","hint":"юго-запад, Royal City","hintEn":"south-west, Royal City","color":"#86BCB6"},
            {"key":"hm","name":"Hoàng Mai","hint":"юг, Linh Đàm, Gamuda City","hintEn":"south, Linh Dam, Gamuda City","color":"#FF9DA7"},
            {"key":"btl","name":"Bắc Từ Liêm","hint":"северо-запад, Ciputra, Xuân Đỉnh","hintEn":"north-west, Ciputra, Xuan Dinh","color":"#F1CE63"},
            {"key":"hd","name":"Hà Đông","hint":"дальний юго-запад, бюджетные новостройки","hintEn":"far south-west, budget new-builds","color":"#D4A6C8"}
        ]
    },
    "binh-duong": {
        "name": "Биньзыонг", "nameEn": "Binh Duong",
        "districts": [
            {"key":"ta","name":"Thuận An","hint":"вдоль шоссе 13, Lái Thiêu, промзоны VSIP I","hintEn":"along Highway 13, Lai Thieu, VSIP I industrial parks","color":"#4E79A7"},
            {"key":"da","name":"Dĩ An","hint":"граница с Тхудыком, ближе всего к Хошимину","hintEn":"borders Thu Duc, the closest part to HCMC","color":"#F28E2B"},
            {"key":"tdm","name":"Thủ Dầu Một","hint":"административный центр, Bình Dương New City","hintEn":"administrative centre, Binh Duong New City","color":"#E15759"},
            {"key":"bc","name":"Bến Cát","hint":"север, промышленный пояс Mỹ Phước","hintEn":"north, My Phuoc industrial belt","color":"#76B7B2"},
            {"key":"tu","name":"Tân Uyên","hint":"северо-восток, новые промзоны","hintEn":"north-east, newer industrial parks","color":"#B07AA1"}
        ]
    }

,
    "phu-quoc": {
        "name": "Фукуок", "nameEn": "Phu Quoc",
        "districts": [
            # Реформа 2025 года сделала весь остров одной единицей: Chợ Tốt отдаёт у
            # ВСЕХ объявлений Фукуока квартал «Đặc khu Phú Quốc», и пока его здесь
            # не было, каждое отбрасывалось как «чужой район» -- отсюда ноль строк
            # по острову при живых объявлениях. Прежние общины оставлены: они точнее
            # там, где община названа в самом объявлении.
            {"key":"pq","name":"Đặc khu Phú Quốc","hint":"весь остров, укрупнённая единица реформы 2025 года","hintEn":"the whole island, a single unit since the 2025 reform","color":"#59A14F"},
            {"key":"ddg","name":"Dương Đông","hint":"главный город острова, рынок, набережная, ночная жизнь","hintEn":"the island's main town, market, waterfront, nightlife","color":"#4E79A7"},
            {"key":"ath","name":"An Thới","hint":"юг острова, паромный порт, ночной рынок","hintEn":"south of the island, ferry port, night market","color":"#F28E2B"},
            {"key":"dto","name":"Dương Tơ","hint":"курортная полоса Bãi Trường (Long Beach), аэропорт","hintEn":"Bãi Trường / Long Beach resort strip, the airport","color":"#E15759"},
            {"key":"cc","name":"Cửa Cạn","hint":"пляж Ông Lang, тихие бутик-курорты","hintEn":"Ông Lang beach, quieter boutique resorts","color":"#76B7B2"},
            {"key":"gd","name":"Gành Dầu","hint":"север острова, Vinpearl Safari и Grand World","hintEn":"north of the island, Vinpearl Safari and Grand World","color":"#B07AA1"},
            {"key":"hn","name":"Hàm Ninh","hint":"восток, рыбацкая деревня, вид на материк","hintEn":"east coast, fishing village, views to the mainland","color":"#EDC949"},
            {"key":"cdbt","name":"Cửa Dương – Bãi Thơm","hint":"север-центр, малоосвоенная часть острова","hintEn":"north-central, the island's least developed part","color":"#9C755F"}
        ]
    },
    "dumaguete": {
        "name": "Думагете", "nameEn": "Dumaguete", "country": "ph",
        "districts": [
            {"key":"pob","name":"Poblacion","hint":"центр: набережная Rizal Boulevard, порт, рынок","hintEn":"the centre: Rizal Boulevard seafront, the pier, the market","color":"#4E79A7"},
            {"key":"pia","name":"Piapi","hint":"к северу от центра, ближе к морю, тихие улицы","hintEn":"north of the centre, closer to the sea, quiet streets","color":"#F28E2B"},
            {"key":"dar","name":"Daro","hint":"северная окраина, дома с садами","hintEn":"northern edge, houses with gardens","color":"#E15759"},
            {"key":"bgy","name":"Bagacay","hint":"север, тихие субдивизионы недалеко от моря","hintEn":"north, quiet subdivisions near the sea","color":"#76B7B2"},
            {"key":"cdy","name":"Candau-Ay","hint":"запад, по дороге на Валенсию, дома с участками","hintEn":"west, on the Valencia road, houses with plots","color":"#B07AA1"},
            {"key":"lok","name":"Looc","hint":"северо-восток у побережья","hintEn":"north-east, by the shore","color":"#EDC949"},
            {"key":"jnb","name":"Junob","hint":"юг города, ближе к аэропорту","hintEn":"south of the city, towards the airport","color":"#9C755F"},
            {"key":"btg","name":"Batinguel","hint":"запад, спальные кварталы","hintEn":"west, residential blocks","color":"#D37295"},
            {"key":"val","name":"Valencia","hint":"предгорья в 15 минутах, прохладнее, популярна у экспатов","hintEn":"the hills 15 minutes inland, cooler, popular with expats","color":"#86BCB6"},
            {"key":"bcg","name":"Bacong","hint":"юг вдоль побережья, 15 минут от города","hintEn":"south along the coast, 15 minutes from the city","color":"#FF9DA7"},
            {"key":"sib","name":"Sibulan","hint":"север, аэропорт и переправа на Себу","hintEn":"north, the airport and the Cebu ferry","color":"#F1CE63"},
            {"key":"dau","name":"Dauin","hint":"дайв-побережье южнее города","hintEn":"the dive coast south of the city","color":"#D4A6C8"},
            {"key":"zmb","name":"Zamboanguita","hint":"дальний юг побережья, тише и дешевле","hintEn":"the far south coast, quieter and cheaper","color":"#59A14F"},
            {"key":"pul","name":"Pulantubig","hint":"центр-запад, рядом NORECO и университеты","hintEn":"centre-west, near NORECO and the universities","color":"#59A14F"},
            {"key":"cdw","name":"Cadawinonan","hint":"запад у объездной, дешёвые комнаты","hintEn":"west by the diversion road, cheap rooms","color":"#B6992D"},
            {"key":"cmj","name":"Camanjac","hint":"северо-запад, вдоль дороги, тише центра","hintEn":"north-west, along the road, quieter than the centre","color":"#499894"},
            {"key":"bnd","name":"Банилад","hint":"север города вдоль объездной, дома с участками","hintEn":"north of the city along the diversion road, houses with plots","color":"#8CD17D"},
            {"key":"tly","name":"Талай","hint":"запад, между городом и Валенсией, тихо и просторно","hintEn":"west, between the city and Valencia, quiet and roomy","color":"#A0CBE8"},
        ]
    },
    "cebu": {
        "name": "Себу", "nameEn": "Cebu", "country": "ph",
        "districts": [
            {"key":"itp","name":"IT Park / Apas","hint":"деловой кластер, кондо и рестораны, жизнь круглосуточно","hintEn":"the BPO cluster, condos and restaurants, awake around the clock","color":"#4E79A7"},
            {"key":"lah","name":"Lahug","hint":"рядом с IT Park, зеленее, вид на город","hintEn":"next to IT Park, greener, city views","color":"#F28E2B"},
            {"key":"bnl","name":"Banilad","hint":"север центра, школы и торговые центры","hintEn":"north of the centre, schools and malls","color":"#E15759"},
            {"key":"mab","name":"Mabolo","hint":"между центром и портом, средний ценовой сегмент","hintEn":"between the centre and the port, mid-market","color":"#76B7B2"},
            {"key":"gua","name":"Guadalupe","hint":"запад, на холмах, доступное жильё","hintEn":"west, on the hills, affordable","color":"#B07AA1"},
            {"key":"tlm","name":"Talamban","hint":"северо-восток, университеты, тихие субдивизионы","hintEn":"north-east, universities, quiet subdivisions","color":"#EDC949"},
            {"key":"cap","name":"Capitol Site","hint":"исторический центр, Fuente Osmeña","hintEn":"the old centre, Fuente Osmeña","color":"#9C755F"},
            {"key":"mac","name":"Mactan","hint":"остров Мактан, Лапу-Лапу, курорты и аэропорт","hintEn":"Mactan island, Lapu-Lapu, the resorts and the airport","color":"#D37295"},
            {"key":"man","name":"Mandaue","hint":"промышленный сосед Себу, дешевле","hintEn":"Cebu's industrial neighbour, cheaper","color":"#86BCB6"},
            {"key":"tls","name":"Talisay","hint":"юг, побережье, спальный пригород","hintEn":"south, a coastal commuter suburb","color":"#FF9DA7"},
            {"key":"col","name":"Колон · центр","hint":"исторический центр: Колон, Сикатуна, C. Padilla, университеты USC и UC","hintEn":"the old centre: Colon, Sikatuna, C. Padilla, the USC and UC campuses","color":"#59A14F"},
            {"key":"lab","name":"Лабангон","hint":"юго-запад города, недорогие комнаты и квартиры вдоль Katipunan","hintEn":"south-west of the centre, cheap rooms and flats along Katipunan","color":"#B6992D"},
            {"key":"tis","name":"Тиса","hint":"за Лабангоном, дома и малоэтажные комплексы, дешевле центра","hintEn":"beyond Labangon, houses and low-rise blocks, cheaper than the centre","color":"#A0CBE8"},
            {"key":"prd","name":"Пардо","hint":"юго-запад Себу: Басак, Кинасанг-ан, Булакао -- дёшево и людно","hintEn":"south-west Cebu: Basak, Kinasang-an, Bulacao -- cheap and busy","color":"#FF9D9A"},
        ]
    },
    "manila": {
        "name": "Манила", "nameEn": "Manila", "country": "ph",
        "districts": [
            {"key":"mak","name":"Makati","hint":"деловой центр, посольства, классический экспат-район","hintEn":"the business district, embassies, the classic expat area","color":"#4E79A7"},
            {"key":"bgc","name":"BGC / Taguig","hint":"новый деловой район, самый дорогой","hintEn":"the new business district, the most expensive","color":"#F28E2B"},
            {"key":"ort","name":"Ortigas / Pasig","hint":"второй деловой центр, восточнее","hintEn":"the second business district, further east","color":"#E15759"},
            {"key":"mla","name":"Malate / Ermita","hint":"старая Манила, залив, дешевле","hintEn":"old Manila, the bay, cheaper","color":"#76B7B2"},
            {"key":"qzc","name":"Quezon City","hint":"самый большой город агломерации, университеты","hintEn":"the largest city in the metro, universities","color":"#B07AA1"},
            {"key":"mdl","name":"Mandaluyong","hint":"между Макати и Ортигасом, кондо среднего класса","hintEn":"between Makati and Ortigas, mid-range condos","color":"#EDC949"},
            {"key":"alb","name":"Alabang","hint":"юг, закрытые зелёные посёлки, семьи","hintEn":"south, green gated subdivisions, families","color":"#9C755F"},
            {"key":"psy","name":"Pasay / MOA","hint":"у аэропорта и Mall of Asia","hintEn":"by the airport and the Mall of Asia","color":"#D37295"},
            {"key":"prq","name":"Parañaque / BF Homes","hint":"юг, малоэтажная застройка, дома а не кондо","hintEn":"south, low-rise, houses rather than condos","color":"#86BCB6"},
        ]
    }
    ,
    "can-tho": {
        "name": "Кантхо", "nameEn": "Can Tho",
        "districts": [
            {"key":"nki","name":"Phường Ninh Kiều","hint":"центр, набережная и рынок","hintEn":"the centre, the waterfront and the market"},
            {"key":"tanc","name":"Phường Tân An","hint":"центр, у пристани Ninh Kiều","hintEn":"centre, by the Ninh Kieu pier"},
            {"key":"ckh","name":"Phường Cái Khế","hint":"центр-север, торговый район","hintEn":"centre-north, shopping"},
            {"key":"anb","name":"Phường An Bình","hint":"запад центра, университеты","hintEn":"west of the centre, universities"},
            {"key":"crg","name":"Phường Cái Răng","hint":"юг, плавучий рынок и мост Cần Thơ","hintEn":"south, the floating market and the Can Tho bridge"},
            {"key":"hpu","name":"Phường Hưng Phú","hint":"юг за рекой, новые кварталы","hintEn":"south across the river, new blocks"},
            {"key":"bth2","name":"Phường Bình Thủy","hint":"северо-запад, у аэропорта","hintEn":"north-west, by the airport"},
            {"key":"ltu","name":"Phường Long Tuyền","hint":"запад, сады и каналы","hintEn":"west, orchards and canals"},
        ]
    },
    "hai-phong": {
        "name": "Хайфон", "nameEn": "Hai Phong",
        "districts": [
            {"key":"hbg","name":"Phường Hồng Bàng","hint":"центр, вокзал и театр","hintEn":"the centre, the station and the opera house"},
            {"key":"anb2","name":"Phường An Biên","hint":"центр-юг, прежний Лэ Тян","hintEn":"centre-south, the former Le Chan"},
            {"key":"lch","name":"Phường Lê Chân","hint":"юг центра, жилые кварталы","hintEn":"south of the centre, residential"},
            {"key":"gvi","name":"Phường Gia Viên","hint":"восток, прежний Нго Куен","hintEn":"east, the former Ngo Quyen"},
            {"key":"nqu","name":"Phường Ngô Quyền","hint":"восток, порт","hintEn":"east, the port"},
            {"key":"kan","name":"Phường Kiến An","hint":"юго-запад, дешевле","hintEn":"south-west, cheaper"},
        ]
    },
    "hue": {
        "name": "Хюэ", "nameEn": "Hue",
        "districts": [
            {"key":"pxu","name":"Phường Phú Xuân","hint":"север, Цитадель","hintEn":"north, the Citadel"},
            {"key":"vyd","name":"Phường Vỹ Dạ","hint":"восток, вдоль реки Хыонг","hintEn":"east, along the Perfume river"},
            {"key":"acu","name":"Phường An Cựu","hint":"юг, университеты","hintEn":"south, universities"},
        ]
    },
    "buon-ma-thuot": {
        "name": "Буонметхуот", "nameEn": "Buon Ma Thuot",
        "districts": [
            {"key":"bmt","name":"Phường Buôn Ma Thuột","hint":"центр","hintEn":"the centre"},
            {"key":"tlp","name":"Phường Tân Lập","hint":"север центра","hintEn":"north of the centre"},
            {"key":"tanb","name":"Phường Tân An","hint":"север","hintEn":"north"},
            {"key":"eak","name":"Phường Ea Kao","hint":"юг, окраина и озеро","hintEn":"south, the outskirts and the lake"},
        ]
    }
}

# `label` is the filter-chip text and needs an English form; `short` is only
# ever a brand name, so it is language-neutral and has none.
SOURCES = [
    {"key":"chotot","label":"Chợ Tốt / Nhà Tốt","labelEn":"Chợ Tốt / Nhà Tốt","short":"Chợ Tốt","active":True,"color":"#C7452B"},
    {"key":"facebook","label":"Facebook-группы","labelEn":"Facebook groups","short":"Facebook","active":True,"color":"#3B5FA6"},
    {"key":"batdongsan","label":"Batdongsan.com.vn","labelEn":"Batdongsan.com.vn","short":"Batdongsan","active":True,"color":"#E0862B"},
    {"key":"telegram","label":"Telegram-каналы","labelEn":"Telegram channels","short":"Telegram","active":True,"color":"#1E9FE0"},
    {"key":"airbnb","label":"Airbnb (помесячно)","labelEn":"Airbnb (monthly)","short":"Airbnb","active":True,"color":"#FF385C"},
    {"key":"tripcom","label":"Trip.com (помесячно)","labelEn":"Trip.com (monthly)","short":"Trip.com","active":True,"color":"#1F6FD6"},
    {"key":"vrbo","label":"Vrbo (помесячно)","labelEn":"Vrbo (monthly)","short":"Vrbo","active":True,"color":"#0074E4"},
    {"key":"booking","label":"Booking.com (помесячно)","labelEn":"Booking.com (monthly)","short":"Booking","active":True,"color":"#003580"},
    {"key":"fbmarketplace","label":"Facebook Marketplace","labelEn":"Facebook Marketplace","short":"FB Marketplace","active":True,"color":"#2E7CF6"},
    {"key":"dotproperty","label":"Dotproperty.com.ph","labelEn":"Dotproperty.com.ph","short":"Dotproperty","active":True,"color":"#00A0B0"},
    {"key":"hoppler","label":"Hoppler.com.ph","labelEn":"Hoppler.com.ph","short":"Hoppler","active":True,"color":"#7B5EA7"},
    {"key":"fbgroup","label":"Facebook-группы","labelEn":"Facebook groups","short":"FB-группы","active":True,"color":"#4267B2"}
]

# --- Donation block (USDT TRC20) ---
# QR generated once with segno (v1.6.6, error correction H, 33x33 modules)
# and baked in as static path data on purpose: the daily automation runs
# unattended, so the build must stay stdlib-only, and the Artifact CSP
# blocks any external QR-generator API. Regenerate only if ADDRESS changes.
USDT_TRC20_ADDRESS = "TXmzW4xfA85YiqVXQZELnE2W8fv7us1AS7"
USDT_QR_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 37 37" role="img">'
    '<path fill="none" stroke="#111111" stroke-width="1" d="M2 2.5h7m6 0h1m2 0h3m3 0h2m2 0h7m-33 1h1m5 0h1m1 0h2m1 0h2m1 0h1m2 0h1m1 0h4m1 0h1m1 0h1m5 0h1m-33 1h1m1 0h3m1 0h1m2 0h2m1 0h6m1 0h1m1 0h4m1 0h1m1 0h3m1 0h1m-33 1h1m1 0h3m1 0h1m2 0h1m1 0h1m2 0h1m2 0h1m1 0h1m1 0h1m1 0h2m1 0h1m1 0h3m1 0h1m-33 1h1m1 0h3m1 0h1m2 0h1m3 0h1m1 0h3m1 0h1m2 0h1m3 0h1m1 0h3m1 0h1m-33 1h1m5 0h1m1 0h1m2 0h2m2 0h4m1 0h3m3 0h1m5 0h1m-33 1h7m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h7m-25 1h1m3 0h3m1 0h2m1 0h1m1 0h1m1 0h1m-20 1h4m1 0h1m4 0h2m1 0h1m3 0h1m4 0h2m3 0h1m-31 1h1m3 0h1m1 0h1m3 0h4m2 0h2m1 0h1m1 0h1m4 0h1m-26 1h1m1 0h1m1 0h1m1 0h1m2 0h1m3 0h2m3 0h1m1 0h2m2 0h1m1 0h3m-31 1h1m1 0h1m6 0h4m1 0h3m1 0h4m3 0h1m5 0h1m-32 1h2m2 0h4m3 0h2m3 0h1m1 0h2m1 0h1m4 0h3m1 0h3m-33 1h1m1 0h1m1 0h1m2 0h2m4 0h2m1 0h3m1 0h3m2 0h1m1 0h1m1 0h2m1 0h1m-30 1h2m1 0h2m2 0h5m2 0h1m1 0h8m1 0h4m-28 1h2m1 0h1m1 0h1m2 0h3m2 0h2m2 0h3m2 0h1m1 0h2m2 0h1m-32 1h1m2 0h3m1 0h2m1 0h4m3 0h2m1 0h2m3 0h1m1 0h2m1 0h2m-31 1h1m1 0h2m1 0h2m1 0h1m1 0h1m1 0h1m4 0h3m1 0h5m1 0h2m-31 1h4m1 0h2m1 0h1m2 0h2m1 0h3m3 0h5m2 0h3m1 0h1m-32 1h1m1 0h1m1 0h1m5 0h1m2 0h1m3 0h3m1 0h2m1 0h3m5 0h1m-33 1h4m2 0h1m1 0h1m1 0h2m1 0h1m2 0h2m4 0h1m1 0h4m1 0h2m1 0h1m-33 1h2m5 0h2m3 0h2m1 0h2m1 0h1m1 0h3m4 0h1m4 0h1m-31 1h1m1 0h4m1 0h1m2 0h1m1 0h1m1 0h1m1 0h2m1 0h4m1 0h1m1 0h2m1 0h1m-29 1h1m1 0h1m2 0h2m1 0h2m1 0h2m1 0h1m1 0h1m1 0h3m2 0h1m1 0h2m1 0h1m-32 1h2m2 0h1m1 0h1m1 0h2m4 0h1m2 0h2m2 0h2m1 0h6m1 0h2m-25 1h1m2 0h1m2 0h6m3 0h2m3 0h5m-33 1h7m1 0h1m1 0h2m1 0h1m1 0h1m2 0h3m3 0h1m1 0h1m1 0h1m2 0h1m-32 1h1m5 0h1m1 0h2m2 0h1m2 0h1m2 0h1m1 0h2m1 0h2m3 0h1m3 0h1m-33 1h1m1 0h3m1 0h1m1 0h6m3 0h4m3 0h5m1 0h1m1 0h1m-33 1h1m1 0h3m1 0h1m2 0h5m3 0h2m4 0h2m1 0h1m1 0h4m-32 1h1m1 0h3m1 0h1m2 0h3m2 0h2m3 0h4m2 0h1m2 0h1m1 0h1m-31 1h1m5 0h1m5 0h4m8 0h1m1 0h3m-29 1h7m2 0h1m2 0h2m4 0h2m1 0h1m1 0h2m1 0h1m1 0h2m2 0h1"/>'
    '</svg>'
)

# Курсы для показа цены в чужой валюте. Файл обновляется fetch_rates.py и
# лежит в репозитории с датой: курс, зашитый в исходник, через месяц врёт.
try:
    RATES = json.load(open("rates.json", encoding="utf-8"))
except FileNotFoundError:
    raise SystemExit("нет rates.json -- запустите: python fetch_rates.py")
_PER_USD = RATES["per_usd"]


def _to_base(amount, cur):
    """Цена в валюте объявления -> в базовой (донги). Нужна фильтру и сортировке:
    сравнивать 45 000 песо с 7 500 000 донгов напрямую нельзя."""
    if amount is None:
        return None
    if cur == RATES["base"]:
        return int(amount)
    return int(round(amount / _PER_USD[cur] * _PER_USD[RATES["base"]]))


N = "https://www.nhatot.com"

def L(id, city, district, type_, price, area, desc, url, posted, daysAgo, source="chotot", details=None, descEn=None, cur="VND", postedOn=None):
    # postedOn -- дата выкладки объявления (ГГГГ-ММ-ДД). Её читает только
    # purge_old_listings.py, в данные страницы она не идёт. Без неё чистка ставит
    # якорь в день, когда впервые встретила строку: «сегодня минус daysAgo». Строки
    # вечернего прогона ПК сервер впервые видит утром -- 14.09 у всех строк
    # вечернего прогона 13.09 якорь оказался на день позже, и неделя на сайте
    # становилась восемью днями.
    d = {"id":id,"city":city,"district":district,"type":type_,"price":price,"area":area,"desc":desc,
         "url":url,"posted":posted,"daysAgo":daysAgo,"source":source}
    # Optional English description. The site falls back to `desc` when absent,
    # so old listings keep working while new ones arrive bilingual.
    if descEn: d["descEn"] = descEn
    if details: d["details"] = details
    # Валюта пишется в строку только когда она не донг -- иначе полторы тысячи
    # вьетнамских объявлений выросли бы на одно поле каждое без всякой пользы.
    if cur != "VND": d["cur"] = cur
    return d

# Строки объявлений лежат в listings/<источник>/<город>.jsonl -- по объявлению на
# строку файла, словарями, которые строит L() выше (с 17.09.2026). До того они стояли
# здесь кодом L(...): 9.9 МБ на 5181 строку, и сборка компилировала их целиком, упираясь
# в предел памяти службы на сервере. Писать строки -- только через listing_lock
# (insert_listings, remove_listings, save_rows), порядок сайта -- поле seq.
from listing_lock import load_page_rows
LISTINGS = load_page_rows()


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
    ],
    "nha-trang": [
        {"type":"hospital","name":"Prestige international polyclinic","lat":12.2522561,"lon":109.1883141},
        {"type":"school","name":"EFI International School","lat":12.1987033,"lon":109.2069537},
        {"type":"hospital","name":"Bệnh viện Quân y 87","lat":12.2307449,"lon":109.1948779},
        {"type":"hospital","name":"Bệnh viện Đa khoa Khánh Hòa","lat":12.2485342,"lon":109.1919559},
        {"type":"hospital","name":"Bệnh viện Ung bướu tỉnh Khánh Hoà","lat":12.2781479,"lon":109.1814538},
        {"type":"hospital","name":"Bệnh viện Da liễu tỉnh Khánh Hoà","lat":12.2782202,"lon":109.1833407},
        {"type":"hospital","name":"Bệnh viện Lao và Bệnh phổi tỉnh Khánh Hoà","lat":12.2777146,"lon":109.1879165},
        {"type":"hospital","name":"Tam Tri Nha Trang","lat":12.2125735,"lon":109.1949415},
        {"type":"hospital","name":"Bệnh viện đa khoa Sài Gòn Nha Trang","lat":12.2583221,"lon":109.1694482},
        {"type":"hospital","name":"Bệnh viện đa khoa Yersin Nha Trang","lat":12.2382514,"lon":109.1650726},
    ],
    "da-lat": [
        {"type":"hospital","name":"Phòng Khám Đa Khoa Trung Tâm Y Tế Đà Lạt","lat":11.9398477,"lon":108.4329545},
        {"type":"hospital","name":"Bệnh viện Đa khoa tỉnh Lâm Đồng","lat":11.9464757,"lon":108.4308966},
        {"type":"hospital","name":"Bệnh viện Y học cổ truyền Phạm Ngọc Thạch","lat":11.9481144,"lon":108.4594477},
        {"type":"hospital","name":"Bệnh viện Sản - Nhi tỉnh Lâm Đồng","lat":11.9730232,"lon":108.4344153},
        {"type":"hospital","name":"Trung tâm Y tế khu vực Lạc Dương","lat":12.0082688,"lon":108.4074842},
        {"type":"hospital","name":"Bệnh viện Phục hồi chức năng tỉnh Lâm Đồng","lat":11.9460869,"lon":108.4640367},
    ],
    "da-nang": [
        {"type":"hospital","name":"Cong Ty CP Benh Vien Da Khoa Hoa Xuan","lat":16.0681938,"lon":108.2013645},
        {"type":"hospital","name":"Benh Vien Y Hoc Co Truyen Tp.Da Nang","lat":16.054196,"lon":108.2190335},
        {"type":"hospital","name":"Benh Vien Phu Nu Tp.Da Nang","lat":16.057147,"lon":108.2179094},
        {"type":"hospital","name":"Benh Vien Ngoai Khoa Nguyen Van Thai","lat":16.0541328,"lon":108.233067},
        {"type":"hospital","name":"Bệnh viện Hoàn Mỹ Đà Nẵng","lat":16.059401,"lon":108.2098753},
        {"type":"hospital","name":"Benh Vien Da Khoa Binh Dan","lat":16.0713797,"lon":108.2001187},
        {"type":"hospital","name":"Benh Vien Tu Binh Dan","lat":16.0686754,"lon":108.2189349},
        {"type":"hospital","name":"Trung Tam Phuc Hoi Co Nhi Suy Dinh Duong Da Nang","lat":16.0824806,"lon":108.2205999},
        {"type":"hospital","name":"Thien Nhan Hospital","lat":16.076597,"lon":108.2158614},
        {"type":"hospital","name":"Bệnh viện Quân y 17","lat":16.0542165,"lon":108.2073008},
        {"type":"hospital","name":"Bệnh viện Phụ sản - Nhi Đà Nẵng","lat":16.0226987,"lon":108.2493906},
        {"type":"hospital","name":"Bệnh viện Phổi Đà Nẵng","lat":16.0480325,"lon":108.1705537},
        {"type":"hospital","name":"Bệnh viện Đà Nẵng","lat":16.0729442,"lon":108.2154554},
        {"type":"hospital","name":"Bệnh viện C Đà Nẵng","lat":16.0731525,"lon":108.2168358},
        {"type":"hospital","name":"Bệnh viện Chỉnh hình & Phục hồi Chức năng Đà Nẵng","lat":16.0736863,"lon":108.2174517},
        {"type":"hospital","name":"Bệnh viện Đa khoa Quốc tế Vinmec Đà Nẵng","lat":16.0387507,"lon":108.2112279},
        {"type":"hospital","name":"Bệnh viện Mắt thành phố Đà Nẵng","lat":16.0374445,"lon":108.2196525},
        {"type":"hospital","name":"Bệnh viện 199 - Bộ Công an","lat":16.0657753,"lon":108.2359315},
        {"type":"hospital","name":"Bệnh viện Phục hồi chức năng thành phố Đà Nẵng","lat":16.0053318,"lon":108.2095449},
        {"type":"hospital","name":"Bệnh viện Y học cổ truyền thành phố Đà Nẵng","lat":16.0057641,"lon":108.2106405},
        {"type":"hospital","name":"Bệnh viện Ung bướu Đà Nẵng","lat":16.0697057,"lon":108.1639233},
        {"type":"hospital","name":"Bệnh viện Y học cổ truyền thành phố Đà Nẵng (cơ sở 2)","lat":16.0660463,"lon":108.2220718},
        {"type":"hospital","name":"Bệnh viện Tâm thần thành phố Đà Nẵng","lat":16.0795422,"lon":108.1459188},
        {"type":"hospital","name":"Bệnh viện Da liễu thành phố Đà Nẵng","lat":16.0737867,"lon":108.1762198},
        {"type":"hospital","name":"Bệnh viện Đa khoa Nam Liên Chiểu","lat":16.0557752,"lon":108.1621981},
        {"type":"hospital","name":"Trung tâm Y tế quận Hải Châu","lat":16.0765046,"lon":108.2142367},
        {"type":"hospital","name":"Trung tâm Y tế quận Thanh Khê","lat":16.0687125,"lon":108.1896135},
        {"type":"hospital","name":"Trung tâm Y tế quận Sơn Trà","lat":16.0579051,"lon":108.2346537},
        {"type":"hospital","name":"Trung tâm Y tế quận Ngũ Hành Sơn","lat":16.0083739,"lon":108.2571427},
        {"type":"hospital","name":"Trung tâm Y tế khu vực Cẩm Lệ","lat":16.0098564,"lon":108.1951896},
        {"type":"hospital","name":"Trung tâm Y tế quận Liên Chiểu","lat":16.0640276,"lon":108.1554429},
        {"type":"hospital","name":"Trung tâm Y tế huyện Hoà Vang","lat":16.009734,"lon":108.1516407},
        {"type":"hospital","name":"Bệnh viện Đa khoa Tâm Trí Đà Nẵng","lat":16.0229038,"lon":108.2142},
        {"type":"hospital","name":"Bệnh viện Răng - Hàm - Mặt thành phố Đà Nẵng","lat":16.0546601,"lon":108.2104648},
    ],
    "hoi-an": [
        {"type":"hospital","name":"Pacific Hospital","lat":15.8843233,"lon":108.3280358},
        {"type":"hospital","name":"Trung tâm Y tế khu vực Hội An","lat":15.8805848,"lon":108.332732},
    ],
    "vung-tau": [
        {"type":"hospital","name":"Raffles Internation Health Clinic","lat":10.3503097,"lon":107.0714235},
        {"type":"hospital","name":"Trung tâm y tế Vietsovpetro","lat":10.3602708,"lon":107.0838967},
        {"type":"hospital","name":"Bệnh viện Đa khoa Vũng Tàu","lat":10.3919211,"lon":107.1303597},
    ],
    "quy-nhon": [
        {"type":"hospital","name":"Trung Tam y te du phong tinh binh dinh (Vaccination center)","lat":13.7927447,"lon":109.2045626},
        {"type":"hospital","name":"Bệnh viện Quân y 13","lat":13.7505205,"lon":109.2138587},
        {"type":"hospital","name":"Bệnh viện Chỉnh hình và Phục hồi chức năng Quy Nhơn","lat":13.7580656,"lon":109.2093373},
        {"type":"hospital","name":"Trung tâm Y tế Quy Nhơn","lat":13.7747431,"lon":109.2374693},
        {"type":"hospital","name":"Bệnh viện Mắt tỉnh Gia Lai","lat":13.7736829,"lon":109.2402522},
    ],
    "phan-thiet": [
        {"type":"hospital","name":"BV Binh Thuan","lat":10.9176763,"lon":108.0847248},
        {"type":"hospital","name":"Trung tâm Y tế khu vực Phan Thiết","lat":10.9335495,"lon":108.0957972},
        {"type":"hospital","name":"Bệnh viện Đa khoa Bình Thuận","lat":10.9401633,"lon":108.089251},
        {"type":"hospital","name":"Bệnh viện Phổi Bình Thuận","lat":10.9343327,"lon":108.0961539},
        {"type":"hospital","name":"Bệnh viện Da liễu Bình Thuận","lat":10.9328823,"lon":108.0952084},
        {"type":"hospital","name":"Bệnh viện Y học cổ truyền - Phục hồi chức năng Bình Thuận","lat":10.9409376,"lon":108.1231309},
    ],
}

# ---------------- RESIDENTIAL COMPLEXES (ЖК) ----------------
# A building/complex name is only ever written inside the free-text description,
# so it is extracted here at build time and baked onto each listing as
# `complex`. Two passes, most specific first:
#   1. a curated dictionary, matched anywhere in the text. Every name below was
#      read off the real descriptions in LISTINGS -- nothing is invented -- and
#      each entry is pinned to the city the building physically stands in, so a
#      name can never leak into another city's filter.
#   2. a fallback "ЖК X" / "комплекс X" pattern over the Russian description
#      only, so a building that first appears tomorrow still gets a name
#      without a dictionary edit.
# Both passes ignore a mention preceded by a proximity word ("рядом с ЖК
# Monarchy"): being next to a complex is not living in it.
import unicodedata

COMPLEX_DICT = [
    # (canonical name, city, [aliases -- matched diacritics- and case-insensitively])
    # "ЖК Millennium" and "Masteri Millennium" are the same Q4 tower (132 Bến
    # Vân Đồn); the marketplaces use both names, so they share one entry.
    ("Masteri Millennium", "ho-chi-minh", ["masteri millennium", "millennium"]),
    ("Masteri Thảo Điền", "ho-chi-minh", ["masteri thao dien"]),
    ("Masteri An Phú", "ho-chi-minh", ["masteri an phu"]),
    ("Era Town", "ho-chi-minh", ["era town"]),
    ("Lavida Plus", "ho-chi-minh", ["lavida plus"]),
    ("Tresor", "ho-chi-minh", ["tresor"]),
    ("Sunshine Sky City", "ho-chi-minh", ["sunshine sky city"]),
    ("Sunshine City", "ho-chi-minh", ["sunshine city"]),
    ("M-One Nam Sài Gòn", "ho-chi-minh", ["m one nam sai gon", "m one"]),
    ("Belleza", "ho-chi-minh", ["belleza", "beleza"]),
    ("Q7 Boulevard", "ho-chi-minh", ["q7 boulevard"]),
    ("RiverGate Residence", "ho-chi-minh", ["rivergate residence", "rivergate", "river gate"]),
    ("Sunrise City View", "ho-chi-minh", ["sunrise city view", "sunrise cityview"]),
    ("Sunrise City", "ho-chi-minh", ["sunrise city"]),
    ("Sunrise Riverside", "ho-chi-minh", ["sunrise riverside"]),
    ("New City Thủ Thiêm", "ho-chi-minh", ["new city thu thiem", "new city"]),
    ("River Panorama", "ho-chi-minh", ["river panorama"]),
    ("Florita", "ho-chi-minh", ["florita"]),
    ("Kim Sơn", "ho-chi-minh", ["kim son"]),
    ("Hoàng Anh Gia Lai", "ho-chi-minh", ["hoang anh gia lai", "hagl"]),
    ("Hoàng Anh Thanh Bình", "ho-chi-minh", ["hoang anh thanh binh"]),
    ("Phú Hoàng Anh", "ho-chi-minh", ["phu hoang anh"]),
    ("Goldview", "ho-chi-minh", ["goldview"]),
    ("Midtown", "ho-chi-minh", ["midtown"]),
    ("Star Hill", "ho-chi-minh", ["star hill"]),
    ("Scenic Valley", "ho-chi-minh", ["scenic valley"]),
    ("Green Valley", "ho-chi-minh", ["green valley"]),
    ("Happy Valley", "ho-chi-minh", ["happy valley"]),
    ("Sky Garden", "ho-chi-minh", ["sky garden"]),
    ("Riverside Residence", "ho-chi-minh", ["riverside residence"]),
    ("Riverpark Premier", "ho-chi-minh", ["riverpark premier", "riverpark"]),
    ("Cardinal Court", "ho-chi-minh", ["cardinal court"]),
    ("Hưng Phúc", "ho-chi-minh", ["hung phuc"]),
    ("Him Lam Kênh Tẻ", "ho-chi-minh", ["him lam kenh te"]),
    ("Him Lam Tân Hưng", "ho-chi-minh", ["him lam tan hung"]),
    ("Cosmo City", "ho-chi-minh", ["cosmo city"]),
    ("De Capella", "ho-chi-minh", ["de capella"]),
    ("Docklands", "ho-chi-minh", ["docklands"]),
    ("Sadora", "ho-chi-minh", ["sadora"]),
    ("Green Star", "ho-chi-minh", ["green star"]),
    ("Paris Hoàng Kim", "ho-chi-minh", ["paris hoang kim"]),
    ("The Ascentia", "ho-chi-minh", ["the ascentia", "ascentia"]),
    ("The Antonia", "ho-chi-minh", ["the antonia", "antonia"]),
    ("Riviera Point", "ho-chi-minh", ["infiniti riviera point", "riviera point"]),
    ("Cantavil An Phú", "ho-chi-minh", ["cantavil an phu", "cantavil"]),
    ("The Metropole Thủ Thiêm", "ho-chi-minh", ["metropole thu thiem", "metropole"]),
    ("Thanh Đa View", "ho-chi-minh", ["thanh da view"]),
    ("CityNest Saigon", "ho-chi-minh", ["citynest"]),
    ("Mỹ Khánh", "ho-chi-minh", ["my khanh"]),
    ("Mỹ Phát", "ho-chi-minh", ["my phat"]),
    ("Mỹ Đức", "ho-chi-minh", ["my duc"]),
    ("Res 3", "ho-chi-minh", ["res iii", "res 3", "res3"]),
    ("H1 Hoàng Diệu", "ho-chi-minh", ["h1 hoang dieu"]),
    ("Hồng Lĩnh", "ho-chi-minh", ["hong linh"]),
    ("Minh Thành", "ho-chi-minh", ["minh thanh"]),
    ("Sky Thủ Thiêm", "ho-chi-minh", ["sky thu thiem"]),
    ("Sunrise North", "ho-chi-minh", ["sunrise north"]),
    ("Phú Mỹ Vạn Phát Hưng", "ho-chi-minh", ["phu my van phat hung"]),

    ("Mường Thanh Viễn Triều", "nha-trang", ["muong thanh vien trieu"]),
    ("Mường Thanh Khánh Hòa", "nha-trang", ["muong thanh khanh hoa"]),
    ("Mường Thanh", "nha-trang", ["muong thanh"]),
    ("Oceanus", "nha-trang", ["oceanus"]),
    ("CCU-01", "nha-trang", ["ccu 01", "ccu01"]),
    ("HUD Building", "nha-trang", ["hud building"]),
    ("VCN Phước Long", "nha-trang", ["vcn phuoc long"]),
    ("VCN Phước Hải", "nha-trang", ["vcn phuoc hai"]),
    ("Vega City", "nha-trang", ["vega city"]),
    ("Panorama", "nha-trang", ["panorama"]),
    ("Gold Coast", "nha-trang", ["gold coast", "goldcoast"]),
    ("Maple", "nha-trang", ["maple"]),
    ("Megas", "nha-trang", ["megas"]),
    ("Hoàng Quân", "nha-trang", ["hoang quan"]),
    ("Napoleon", "nha-trang", ["napoleon"]),
    ("Mipeco", "nha-trang", ["mipeco"]),
    ("Scenia Bay", "nha-trang", ["scenia bay"]),
    ("Sông Đà Nha Trang", "nha-trang", ["song da nha trang"]),
    ("Mỹ Gia", "nha-trang", ["my gia"]),
    ("Hà Quang 2", "nha-trang", ["ha quang 2"]),
    ("Hà Quang 1", "nha-trang", ["ha quang 1"]),
    ("CT4 HUD", "nha-trang", ["ct4 hud"]),
    ("Biển An Viên", "nha-trang", ["bien an vien"]),
    ("Vĩnh Điềm Trung", "nha-trang", ["vinh diem trung"]),

    ("Panoma", "da-nang", ["panoma"]),
    ("Monarchy", "da-nang", ["monarchy"]),
    ("Hiyori Garden Tower", "da-nang", ["hiyori garden tower", "hiyori"]),
    ("Golden Bay", "da-nang", ["golden bay"]),
    ("Euro Village", "da-nang", ["euro village"]),
    ("FPT Plaza", "da-nang", ["fpt plaza"]),
    ("Mường Thanh", "da-nang", ["muong thanh"]),
    ("Sơn Trà Ocean View", "da-nang", ["son tra ocean view"]),
    ("Lapaz Tower", "da-nang", ["lapaz"]),
    ("MIA Center Point", "da-nang", ["mia center point"]),
    ("F.Home", "da-nang", ["f home"]),
    ("Sam Towers", "da-nang", ["sam towers"]),
    ("Đà Nẵng Plaza", "da-nang", ["da nang plaza"]),
    ("HAGL Lake View Residence", "da-nang", ["hagl lake view"]),
    ("Wyndham Soleil", "da-nang", ["wyndham soleil", "soleil anh duong"]),
    ("Sun Cosmo", "da-nang", ["sun cosmo"]),
    ("Nam Việt Á", "da-nang", ["nam viet a"]),

    ("Vũng Tàu Melody", "vung-tau", ["vung tau melody", "melody"]),
    ("Gateway", "vung-tau", ["gateway"]),
    ("Sơn Thịnh", "vung-tau", ["son thinh"]),
    ("Silver Sea", "vung-tau", ["silver sea"]),
    ("DIC Phoenix", "vung-tau", ["dic phoenix"]),
    ("The Imperial", "vung-tau", ["the imperial", "imperial"]),
    ("Goldsea", "vung-tau", ["goldsea"]),
    ("La Vida Residences", "vung-tau", ["la vida residences"]),
    ("Vũng Tàu Center Point", "vung-tau", ["vung tau center point"]),

    ("FLC SeaTower", "quy-nhon", ["flc seatower", "flc sea tower"]),
    ("Altara Residences", "quy-nhon", ["altara"]),
    ("Ecolife Riverside", "quy-nhon", ["ecolife"]),
    ("TMS Quy Nhơn", "quy-nhon", ["tms quy nhon"]),

    ("Apec Mandala Mũi Né", "phan-thiet", ["apec mandala"]),
    ("Casamia", "hoi-an", ["casamia"]),
]

# Names that describe a whole quarter (khu đô thị / KDC) rather than one
# building. They are real and worth filtering by, but a listing that also names
# an actual building inside the quarter must be filed under the building, so
# these are only consulted once every other alias has missed.
COMPLEX_AREA_NAMES = {"Him Lam Tân Hưng", "Him Lam Kênh Tẻ", "Hà Quang 1", "Hà Quang 2",
                      "Mỹ Gia", "Nam Việt Á", "Vĩnh Điềm Trung", "Biển An Viên",
                      "VCN Phước Long", "VCN Phước Hải"}

# A mention behind one of these is a landmark, not the listing's own address.
COMPLEX_NEAR_WORDS = ("рядом", "недалеко", "близко", "напротив", "неподалеку",
                      "мин до", "минут до", "минуты до", "мин пешком", "мин ходьбы",
                      "моста", "мосту", "cau ", "bridge",
                      "near", "next to", "close to", "walk to", "walking distance",
                      "minutes to", "min to", "opposite", "steps from", "minutes from")

# Heads the ЖК-pattern must never turn into a name: generic Vietnamese/English
# nouns that introduce the real name rather than being part of it.
COMPLEX_STOPWORDS = {"chung", "khu", "can", "nha", "block", "toa", "the", "duong",
                     "phuong", "quan", "kdt", "kdc", "cc", "apartment", "apartments",
                     "building", "residence", "residences", "tower", "towers", "view",
                     "premium", "luxury", "new", "old"}


def _cx_norm(s):
    """Lowercase, strip Vietnamese diacritics, squash punctuation to single spaces."""
    s = s.lower().replace("đ", "d")
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = re.sub(r"[^a-z0-9а-яё]+", " ", s)
    return " " + re.sub(r"\s+", " ", s).strip() + " "


# Buildings before quarters, then longest alias first -- so "Sunrise City View"
# beats "Sunrise City", and "ЖК Megas, район Hà Quang 2" files under Megas.
_CX_ALIASES = sorted(
    [(_cx_norm(a), name, city)
     for name, city, aliases in COMPLEX_DICT for a in aliases],
    key=lambda t: (t[1] in COMPLEX_AREA_NAMES, -len(t[0])))

_CX_LEAD = re.compile(r'(?:ЖК|Ж/К|жило[мг]\s+комплексе?|комплекс[а-я]*|КДТ|КГТ)\s+')
# A complex name reads as Latin or Vietnamese and is always capitalised.
_CX_TOKEN = re.compile(
    r'^[A-ZĐÂÊÔƯĂÁÀẢÃẠÉÈẺẼẸÍÌỈĨỊÓÒỎÕỌÚÙỦŨỤÝỲỶỸỴ]'
    r"[A-Za-zĐđÂâÊêÔôƯưĂăáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ0-9'\-\.]*$")


def _cx_is_landmark(norm_text, pos):
    """True when the mention at `pos` is a nearby landmark rather than the address."""
    return any(w in norm_text[max(0, pos - 30):pos] for w in COMPLEX_NEAR_WORDS)


def _cx_text(l):
    # Only the listing's own headline text. `details.notice`/`contract` are full
    # of nearby landmarks ("рядом Lotte Mart, ЖК ..."), which cost more in wrong
    # names than they win in extra ones.
    return (l.get("desc") or "") + " " + (l.get("descEn") or "")


def detect_complex(l):
    norm = _cx_norm(_cx_text(l))
    for alias, name, city in _CX_ALIASES:
        if city != l["city"]:
            continue
        start = 0
        while True:
            pos = norm.find(alias, start)
            if pos == -1:
                break
            if not _cx_is_landmark(norm, pos):
                return name
            start = pos + 1
    # Fallback: "ЖК X" in the Russian description only. English prose uses
    # "complex" as an ordinary word ("the complex has a pool"), which yielded
    # nothing but junk, so descEn is deliberately not scanned here.
    ru = l.get("desc") or ""
    for m in _CX_LEAD.finditer(ru):
        head = _cx_norm(ru[:m.start()])
        if any(w in head[-30:] for w in COMPLEX_NEAR_WORDS):
            continue
        words = []
        for raw in re.split(r"\s+", ru[m.end():m.end() + 90].strip()):
            tk = raw.strip("«»\"'(),;:.—-")
            # A bare "2"/"1" right after the name belongs to it (Hoàng Anh 2).
            if words and re.match(r"^\d{1,2}$", tk):
                words.append(tk)
                break
            if not tk or not _CX_TOKEN.match(tk):
                break
            if _cx_norm(tk).strip() in COMPLEX_STOPWORDS:
                break
            words.append(tk)
            # A comma or bracket ends the name: "ЖК Hưng Vượng, Tân Phong" is
            # the Hưng Vượng complex in Tân Phong, not a four-word building.
            if raw != tk and re.search(r"[,;:()«»]", raw):
                break
            if len(words) == 4:
                break
        if not words:
            continue
        if len(words) == 1 and len(words[0]) < 4:
            continue
        return " ".join(words)
    return None


# Bake the detected name onto every listing (and only when one was found, so
# the JSON stays small and the JS can test `l.complex` directly).
_cx_total = 0
_cx_names = set()
for _l in LISTINGS:
    _cx = detect_complex(_l)
    if _cx:
        _l["complex"] = _cx
        _cx_total += 1
        _cx_names.add((_l["city"], _cx))
print("Complexes: %d listings named, %d distinct (city, name) pairs" % (_cx_total, len(_cx_names)))


# Photo URLs go into the page in a compact form. 94% of them are exactly
# "https://cdn.chotot.com/<token>/preset:view/plain/<tail>" -- 42 bytes of
# identical boilerplate each, carried ~9 000 times and growing with every
# photo backfilled. Stored as "~<token>/<tail>" -- a printable sentinel on
# purpose: a control character would be re-escaped as  and cost six
# bytes in the JSON, and no photo URL we store begins with "~". Expanded once on load
# by the page (and by site_data.expand_photo for every Python consumer), so
# nothing downstream ever sees the short form. rebuild_final.py's own
# LISTINGS keep the full URLs: this is a serialisation detail, not data.
_CDN, _MID = "https://cdn.chotot.com/", "/preset:view/plain/"


def _compact_photo(u):
    if u.startswith(_CDN):
        token, sep, tail = u[len(_CDN):].partition(_MID)
        if sep and "/" not in token:
            return "~" + token + "/" + tail
    return u


_photos_before = _photos_after = 0
for _l in LISTINGS:
    _d = _l.get("details")
    if _d and _d.get("photos"):
        _short = [_compact_photo(u) for u in _d["photos"]]
        _photos_before += sum(len(u) for u in _d["photos"])
        _photos_after += sum(len(u) for u in _short)
        _d = dict(_d); _d["photos"] = _short
        _l = _l  # keep the row object; only the serialised copy differs
        _l["details"] = _d

# Пометка об источнике -- один и тот же текст у тысяч строк: 16.09.2026 на 4389
# строках их было ШЕСТЬ разных, а весили они 2.2 МБ из 6.8 МБ всех данных страницы
# (треть). В страницу они идут списком NOTICES, в строке остаётся «~N».
# Разворачивается один раз при загрузке -- страницей (expandNotices) и
# site_data.load_data, поэтому ни остальной JS, ни питоновские программы короткой
# формы не видят. Номер хранится строкой, а не числом: «0» -- ложное значение, и
# проверки вида «if (l.details.notice)» потеряли бы пометку первой строки.
_NOTICES, _notice_ix, _notices_before = [], {}, 0


def _notice_ref(t):
    if t not in _notice_ix:
        _notice_ix[t] = "~%d" % len(_NOTICES)
        _NOTICES.append(t)
    return _notice_ix[t]


for _l in LISTINGS:
    _d = _l.get("details")
    if not _d:
        continue
    for _k in ("notice", "noticeEn"):
        if isinstance(_d.get(_k), str) and _d[_k]:
            _notices_before += len(_d[_k])
            _d[_k] = _notice_ref(_d[_k])

# Нормализованная цена: фильтр бюджета и сортировка сравнивают объявления из
# разных стран, а 45 000 песо и 7 500 000 донгов напрямую несопоставимы.
# Считается здесь, на сборке, а не в браузере -- в JS это была бы работа на
# каждый кадр фильтрации.
for _l in LISTINGS:
    _l["pv"] = _to_base(_l.get("price"), _l.get("cur", "VND"))

_RATES_PUBLIC = {"base": RATES["base"], "date": RATES["date"],
                 "show": RATES["show_currencies"], "perUsd": _PER_USD}

# Какие источники реально живут в каждом городе и разделе. Реестр SOURCES общий
# на весь сайт, и без этой карты фильтр предлагал бы вьетнамцу Dotproperty, а на
# филиппинской странице -- Chợ Tốt и Batdongsan: чипы, которые ничего не находят
# и только создают впечатление, что данные потерялись. Считается по фактическим
# строкам, поэтому карта не может разойтись с содержимым.
_SOURCES_BY_CITY = {}
for _l in LISTINGS:
    _k = "commercial" if _l["type"] in ("Офис", "Торговая площадь", "Склад") else "residential"
    _SOURCES_BY_CITY.setdefault(_l["city"], {}).setdefault(_k, set()).add(_l.get("source", "chotot"))
_SRC_ORDER = [s["key"] for s in SOURCES]
_SOURCES_BY_CITY = {c: {k: sorted(v, key=_SRC_ORDER.index) for k, v in kinds.items()}
                    for c, kinds in _SOURCES_BY_CITY.items()}

DATA = {
    "CITIES": CITIES, "SOURCES": SOURCES, "RATES": _RATES_PUBLIC,
    "SOURCES_BY_CITY": _SOURCES_BY_CITY,
    "LISTINGS": LISTINGS, "WARD_BOUNDARIES": WARD_BOUNDARIES, "POIS": POIS,
    "NOTICES": _NOTICES
}
DATA_JSON = json.dumps(DATA, ensure_ascii=False, separators=(",",":"))
print("Data JSON size: %d (photo URLs compacted: %.0f KB saved, %d notices shared: %.0f KB saved)"
      % (len(DATA_JSON), (_photos_before - _photos_after) / 1024, len(_NOTICES),
         (_notices_before - sum(len(t) for t in _NOTICES)) / 1024))

# ================== HTML TEMPLATE ==================
HTML = r"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Жильё во Вьетнаме и на Филиппинах — Хошимин · Ханой · Себу · Манила</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%8F%A0%3C/text%3E%3C/svg%3E">
<meta name="description" content="Более __LISTING_COUNT__ объявлений об аренде жилья во Вьетнаме (Хошимин, Ханой, Дананг, Нячанг, Далат, Хойан, Вунгтау, Куинён, Фантьет), собранных с Chợ Tốt, Batdongsan, Facebook и других источников в одном месте — с фото, картой и фильтрами.">
<meta property="og:type" content="website">
<meta property="og:title" content="Жильё во Вьетнаме и на Филиппинах — Хошимин · Ханой · Себу · Манила">
<meta property="og:description" content="Более __LISTING_COUNT__ объявлений об аренде жилья во Вьетнаме и на Филиппинах, собранных с разных площадок в одном месте — с фото, картой и фильтрами.">
<meta property="og:url" content="https://tottorisun.github.io/RentSearcherViet/">
<link rel="canonical" href="https://tottorisun.github.io/RentSearcherViet/">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Жильё во Вьетнаме и на Филиппинах — Хошимин · Ханой · Себу · Манила">
<meta name="twitter:description" content="Более __LISTING_COUNT__ объявлений об аренде жилья во Вьетнаме и на Филиппинах, собранных с разных площадок в одном месте.">
__LEAFLET_CSS__
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/leaflet.markercluster.js" integrity="sha256-Hk4dIpcqOSb0hZjgyvFOP+cEmDXUKKNE/tT542ZbNQg=" crossorigin=""></script>
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
  .lang-toggle{display:flex;border:1px solid var(--line-strong);border-radius:999px;overflow:hidden;flex:none;align-self:flex-start;margin-bottom:8px;}
  .lang-toggle button{appearance:none;border:none;background:var(--surface);color:var(--ink-dim);padding:6px 14px;font-size:0.82rem;font-weight:700;cursor:pointer;letter-spacing:0.03em;}
  .lang-toggle button + button{border-left:1px solid var(--line-strong);}
  .lang-toggle button.active{background:var(--accent);color:var(--accent-ink);}
  .kind-toggle{display:flex;border:1px solid var(--line-strong);border-radius:999px;overflow:hidden;}
  .kind-toggle button{appearance:none;border:none;background:var(--surface);color:var(--ink-dim);padding:9px 16px;font-size:0.88rem;font-weight:600;cursor:pointer;flex:1;}
  .kind-toggle button + button{border-left:1px solid var(--line-strong);}
  .kind-toggle button.active{background:var(--accent);color:var(--accent-ink);}
  /* On the per-city pages the city tabs are links to sibling pages. */
  a.city-tab{text-decoration:none;color:inherit;display:inline-block;}
  .city-tab.empty{opacity:.55;}
  .theme-toggle{display:flex;border:1px solid var(--line-strong);border-radius:999px;overflow:hidden;flex:none;align-self:flex-start;}
  .theme-toggle button{appearance:none;border:none;background:var(--surface);color:var(--ink-dim);padding:6px 12px;font-size:0.82rem;font-weight:600;cursor:pointer;}
  .theme-toggle button + button{border-left:1px solid var(--line-strong);}
  .theme-toggle button.active{background:var(--accent);color:var(--accent-ink);}
  .brand-mark{flex:none;width:46px;height:46px;border-radius:12px;background:var(--accent);display:flex;align-items:center;justify-content:center;box-shadow:var(--shadow-sm);}
  .brand-mark svg{width:26px;height:26px;}
  .brand h1{font-size:clamp(1.5rem,1.1rem + 1.3vw,2.05rem);letter-spacing:-0.01em;}
  .tagline{margin:4px 0 0;color:var(--ink-dim);font-size:0.98rem;max-width:60ch;}

  .city-tabs{display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
  .city-group{flex-basis:100%;font-size:0.78rem;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-faint);margin:8px 0 -2px;}
  .city-group:first-child{margin-top:0;}
  .city-tab{appearance:none;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink);padding:10px 18px;border-radius:999px;font-size:0.96rem;font-weight:600;cursor:pointer;transition:background .15s ease,color .15s ease,border-color .15s ease;}
  .city-tab .sub{display:block;font-weight:400;font-size:0.76rem;color:var(--ink-faint);margin-top:1px;}
  .city-tab[aria-selected="true"]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);}
  .city-tab[aria-selected="true"] .sub{color:var(--accent-ink);opacity:0.82;}
  .city-tab:hover{border-color:var(--accent);}

  .control-panel{display:grid;grid-template-columns:minmax(280px,1fr) minmax(300px,1.05fr);gap:18px;align-items:start;}
  .control-panel>*{min-width:0;}
  @media (max-width:860px){.control-panel{grid-template-columns:1fr;}}

  .card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:var(--shadow-sm);}

  .filters{padding:22px 22px 18px;display:flex;flex-direction:column;gap:18px;}
  .field{display:flex;flex-direction:column;gap:8px;}
  /* `display:flex` above beats the UA's [hidden]{display:none}, so the JS-hidden
     fields (#poi-sort-field, #complex-field) need this to actually disappear. */
  .field[hidden]{display:none;}
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
  /* 1rem = 16px on purpose: iOS Safari zooms the whole page in when a focused
     input is smaller than 16px, and there is no way to zoom back out cleanly. */
  .date-row input{flex:1;min-width:0;padding:9px 10px;border-radius:var(--radius-md);border:1px solid var(--line-strong);background:var(--surface-2);color:var(--ink-faint);font-size:1rem;}
  .date-row span{color:var(--ink-faint);font-size:0.85rem;}

  .autocomplete{position:relative;}
  .autocomplete input{width:100%;padding:11px 36px 11px 14px;border-radius:var(--radius-md);border:1px solid var(--line-strong);background:var(--paper);color:var(--ink);font-size:1rem;}
  .autocomplete .clear-btn{position:absolute;right:6px;top:6px;width:28px;height:28px;border:none;background:transparent;color:var(--ink-faint);font-size:1.1rem;cursor:pointer;border-radius:50%;display:flex;align-items:center;justify-content:center;}
  .autocomplete .clear-btn:hover{background:var(--surface-2);}
  #poi-sort-select,#complex-select{width:100%;max-width:100%;padding:11px 14px;border-radius:var(--radius-md);border:1px solid var(--line-strong);background:var(--paper);color:var(--ink);font-size:1rem;}
  .poi-dist-badge{font-size:0.78rem;color:var(--ink-dim);white-space:nowrap;}
  .complex-pill{display:inline-block;margin-top:4px;padding:2px 8px;border-radius:999px;background:var(--paper);border:1px solid var(--line-strong);font-size:0.78rem;color:var(--ink);}
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
  /* Спокойная подложка из обычных тайлов OSM: фильтр висит только на слое
     тайлов, пины и границы районов остаются своего цвета. В тёмной теме тайлы
     инвертируются, а поворот оттенка на 180° возвращает воде синеву. */
  .leaflet-map-el.tiles-light .leaflet-tile-pane{filter:grayscale(.92) brightness(1.05) contrast(.9);}
  .leaflet-map-el.tiles-dark .leaflet-tile-pane{filter:invert(1) hue-rotate(180deg) grayscale(.85) brightness(.9) contrast(.88);}
  /* Пин с ценой. Leaflet ставит в точку объявления левый верхний угол иконки;
     пилюля сдвинута на свою ширину и высоту, так что точке соответствует
     кончик хвостика снизу, а не угол. */
  .pin-wrap{background:none;border:none;}
  .price-pin{position:absolute;left:0;top:0;transform:translate(-50%,calc(-100% - 6px));
    background:var(--accent);color:var(--accent-ink);font:700 11.5px/1.15 var(--font-body);
    padding:4px 7px;border-radius:999px;white-space:nowrap;border:1.5px solid var(--surface);
    box-shadow:0 1px 4px rgba(0,0,0,.35);cursor:pointer;font-variant-numeric:tabular-nums;}
  .price-pin::after{content:"";position:absolute;left:50%;top:100%;transform:translateX(-50%);
    border:5px solid transparent;border-top-color:var(--accent);border-bottom:0;margin-top:1px;}
  /* Приблизительный пин -- контур пунктиром: место не из объявления, а центр района. */
  .price-pin.approx{background:var(--surface);color:var(--accent);border:1.5px dashed var(--accent);}
  .price-pin.active{background:var(--gold);color:#241701;border:1.5px solid var(--surface);}
  .price-pin.active::after{border-top-color:var(--gold);}
  .cluster-wrap{background:none;border:none;}
  .cluster-pin{display:flex;align-items:center;justify-content:center;border-radius:50%;
    background:var(--ink);color:var(--paper);font:700 12.5px/1 var(--font-body);
    box-shadow:0 0 0 5px rgba(30,122,76,.30),0 2px 6px rgba(0,0,0,.35);cursor:pointer;}
  .leaflet-cluster-anim .leaflet-marker-icon,.leaflet-cluster-anim .leaflet-marker-shadow{transition:transform .3s ease-out,opacity .3s ease-in;}
  .leaflet-cluster-spider-leg{transition:stroke-dashoffset .3s ease-out,stroke-opacity .3s ease-in;}
  .map-tools{display:flex;gap:6px;flex-wrap:wrap;}
  .map-filters{display:flex;flex-wrap:wrap;align-items:center;gap:8px 18px;padding:8px 10px;background:var(--paper);border:1px solid var(--line);border-radius:var(--radius-md);}
  .map-filter-group{display:flex;align-items:center;gap:8px;flex-wrap:wrap;min-width:0;}
  .map-filter-label{font-size:0.72rem;font-weight:700;color:var(--ink-dim);text-transform:uppercase;letter-spacing:0.04em;white-space:nowrap;}
  .map-filter-count{margin-left:auto;font-weight:700;font-size:0.9rem;color:var(--ink);white-space:nowrap;}
  @media (max-width:640px){.map-filter-count{margin-left:0;}}
  .map-tool{appearance:none;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink-dim);
    padding:6px 11px;border-radius:999px;font-size:0.8rem;font-weight:600;cursor:pointer;}
  .map-tool:hover{border-color:var(--accent);color:var(--accent);}
  .map-tool:disabled{opacity:.6;cursor:progress;}
  /* Карта на весь экран: карточка карты становится слоем поверх страницы. */
  .map.card.map-full{position:fixed;inset:0;z-index:900;border-radius:0;border:none;display:flex;flex-direction:column;}
  .map.card.map-full .leaflet-map-el{flex:1;height:auto;min-height:0;}
  body.map-full-open{overflow:hidden;}
  /* Кнопка «Посмотреть» в карточке на карте. У Leaflet есть правило
     «.leaflet-container a { color: #0078A8 }», и оно специфичнее, чем
     «.pt-view»: текст кнопки был синим на зелёном -- rgb(0,120,168) на
     rgb(30,122,76), то есть почти невидимым. Замечено 11 сентября 2026. */
  .leaflet-container a.pt-view{color:#fff;}
  /* Крестик закрытия стоит в правом верхнем углу и наезжал на цену на 15 px. */
  .leaflet-popup .pt-top{padding-right:18px;}
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
  /* The only way from a map card to the source: a real button-sized target,
     because on a phone the card is read first and tapped second. */
  .pt-view{display:block;margin-top:8px;padding:9px 12px;border-radius:8px;background:var(--accent);color:#fff;
    font-size:0.82rem;font-weight:700;text-align:center;text-decoration:none;letter-spacing:.01em;min-height:36px;line-height:18px;}
  .pt-view:hover{filter:brightness(1.08);text-decoration:none;}
  .pt-view:focus-visible{outline:2px solid var(--ink);outline-offset:2px;}
  .leaflet-container a.leaflet-popup-close-button{width:28px;height:28px;font-size:20px;line-height:28px;color:var(--ink-dim);}
  .pt-approx{margin-top:4px;color:var(--ink-faint);font-size:0.7rem;font-style:italic;}

  .map-legend{display:flex;gap:14px;flex-wrap:wrap;font-size:0.78rem;color:var(--ink-dim);}
  .map-legend span{display:inline-flex;align-items:center;gap:6px;}
  .poi-toggle-label{display:inline-flex;align-items:center;gap:6px;cursor:pointer;}
  .per-m2-toggle-label{display:inline-flex;align-items:center;gap:6px;cursor:pointer;font-size:0.86rem;color:var(--ink-dim);margin-top:8px;}
  .price-per-m2{font-size:0.8rem;color:var(--ink-faint);margin-left:4px;}
  .poi-marker{border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;box-shadow:0 1px 3px rgba(0,0,0,0.35);border:1.5px solid #fff;}
  .swatch{width:12px;height:12px;border-radius:4px;display:inline-block;border:1px solid var(--line-strong);}
  .swatch-selected{background:var(--accent);border-color:var(--accent);}
  .swatch-has{background:var(--grey-has);}
  .swatch-empty{background:var(--grey-empty);}
  /* Приблизительная точка -- пунктирный контур, ровно как её пин на карте. */
  .swatch-approx{background:var(--surface);border:1.5px dashed var(--accent);}
  .swatch-cluster{border-radius:50%;background:var(--ink);border-color:var(--ink);}
  .map-credit{font-size:0.72rem;color:var(--ink-faint);}

  .results-head{display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:12px;}
  .results-head h2{font-size:1.3rem;}
  .results-sub{margin:4px 0 0;color:var(--ink-dim);font-size:0.9rem;}
  .reset-btn{appearance:none;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink-dim);padding:8px 14px;border-radius:999px;font-size:0.84rem;font-weight:600;cursor:pointer;}
  .reset-btn:hover{border-color:var(--danger);color:var(--danger);}
  .results-head-actions{display:flex;gap:8px;align-items:center;}
  .fav-filter-btn{appearance:none;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink-dim);padding:8px 14px;border-radius:999px;font-size:0.84rem;font-weight:600;cursor:pointer;}
  .fav-filter-btn[aria-pressed="true"]{border-color:#D8A02A;color:#B9860E;background:rgba(216,160,42,0.12);}
  .listing-top-right{display:flex;align-items:center;gap:8px;}
  .fav-btn{appearance:none;background:none;border:none;padding:0;cursor:pointer;font-size:1.15rem;line-height:1;color:var(--ink-faint);}
  .fav-btn[aria-pressed="true"]{color:#D8A02A;}
  /* Touch screens: the same controls, finger-sized. Desktop keeps the compact
     sizes. Found on the owner's phone (2 Sep 2026): the favourite star was a
     15x18px target, chips 31px, the budget fields 24px, the clear buttons 28px. */
  @media (pointer: coarse){
    .chip{min-height:38px;padding:8px 14px;font-size:0.9rem;}
    .lang-toggle button,.theme-toggle button{min-height:38px;padding:8px 16px;}
    .autocomplete .clear-btn{width:36px;height:36px;right:3px;top:3px;font-size:1.3rem;}
    .range-cell input{padding:8px 0;font-size:1.05rem;}
    .range-thumb::-webkit-slider-thumb{width:26px;height:26px;margin-top:1px;}
    .range-thumb::-moz-range-thumb{width:26px;height:26px;}
    .fav-btn{font-size:1.4rem;padding:8px;margin:-8px;}
    .pt-view{min-height:40px;line-height:22px;}
  }

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
  /* Пересчёт в другие валюты -- справочная строка, не цена: обычный шрифт,
     без жирности, приглушённый цвет. Явно, чтобы не наследовать от .price. */
  .price-conv{display:block;font-family:var(--font-body);font-size:0.7rem;font-weight:400;color:var(--ink-faint);font-variant-numeric:tabular-nums;letter-spacing:0;margin-top:2px;}
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
  .support{display:flex;gap:20px;align-items:center;flex-wrap:wrap;padding:18px 20px;margin-bottom:18px;}
  .support-text{flex:1 1 320px;min-width:0;}
  .support-text h3{font-size:1.05rem;margin:0 0 6px;}
  .support-text p{margin:0 0 8px;font-size:0.86rem;color:var(--ink-dim);}
  .support-net{font-size:0.8rem !important;color:var(--warn-ink) !important;background:var(--warn-bg);padding:6px 10px;border-radius:var(--radius-sm);display:inline-block;}
  .support-addr{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:4px;}
  .support-addr code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:0.8rem;background:var(--surface-2);padding:7px 10px;border-radius:var(--radius-sm);word-break:break-all;color:var(--ink);}
  .copy-addr-btn{appearance:none;border:1px solid var(--line-strong);background:var(--surface);color:var(--ink-dim);padding:7px 12px;border-radius:999px;font-size:0.8rem;font-weight:600;cursor:pointer;flex:none;}
  .copy-addr-btn:hover{border-color:var(--accent);color:var(--accent);}
  .support-qr{flex:none;width:132px;height:132px;background:#fff;border-radius:var(--radius-sm);padding:6px;}
  .support-qr svg{width:100%;height:100%;display:block;}
</style>

<div class="page">

  <header class="hero">
    <div class="brand">
      <span class="brand-mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none"><path d="M4 11.5 12 4l8 7.5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M6 10.5V19a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-8.5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 20v-5h4v5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <div>
        <h1 data-i18n="h1Title">Жильё во Вьетнаме и на Филиппинах</h1>
        <p class="tagline" data-i18n="tagline">Комнаты, студии, квартиры и коммерческие помещения в Хошимине, Ханое, Дананге и Нячанге — из реальных объявлений, отсортированные по цене.</p>
      </div>
    </div>
    <div class="lang-toggle" id="lang-toggle" role="group" aria-label="Language">
      <button type="button" data-lang="ru">RU</button>
      <button type="button" data-lang="en">EN</button>
    </div>
    <div class="theme-toggle" id="theme-toggle" role="group" data-i18n-aria="themeGroup" aria-label="Тема оформления">
      <button type="button" data-theme-choice="auto" data-i18n="themeAuto">Авто</button>
      <button type="button" data-theme-choice="light" data-i18n="themeLight">Светлая</button>
      <button type="button" data-theme-choice="dark" data-i18n="themeDark">Тёмная</button>
    </div>
    <nav class="city-tabs" id="city-tabs" role="tablist" data-i18n-aria="cityGroup" aria-label="Город"></nav>
  </header>

  <section class="control-panel">
    <div class="filters card">
      <div class="field">
        <span class="field-label" data-i18n="kindLabel">Тип недвижимости</span>
        <div class="kind-toggle" id="kind-toggle" role="group" data-i18n-aria="kindLabel" aria-label="Тип недвижимости">
          <button type="button" data-kind="residential" class="active" data-i18n="kindResidential">Жильё</button>
          <button type="button" data-kind="commercial" data-i18n="kindCommercial">Коммерция</button>
        </div>
      </div>

      <div class="field">
        <label for="text-search-input" data-i18n="searchLabel">Поиск по описанию</label>
        <div class="autocomplete">
          <input id="text-search-input" type="text" autocomplete="off" data-i18n-ph="searchPlaceholder" placeholder="например: бассейн, метро, вид на море">
          <button class="clear-btn" id="text-search-clear" type="button" data-i18n-title="searchClear" data-i18n-aria="searchClear" title="Очистить поиск" aria-label="Очистить поиск">×</button>
        </div>
      </div>

      <div class="field">
        <label data-i18n="budgetLabel">Бюджет, млн ₫ / мес</label>
        <div class="range-cells">
          <div class="range-cell">
            <span class="range-cell-label" data-i18n="from">от</span>
            <input id="budget-min-input" type="number" min="0" max="45" step="0.5" inputmode="decimal">
          </div>
          <span class="range-cell-sep">—</span>
          <div class="range-cell">
            <span class="range-cell-label" data-i18n="to">до</span>
            <input id="budget-max-input" type="number" min="0" max="45" step="0.5" inputmode="decimal">
          </div>
          <span class="unit" data-i18n="mln">млн ₫</span>
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
        <label for="district-input" data-i18n="districtLabel">Район</label>
        <div class="autocomplete">
          <input id="district-input" type="text" autocomplete="off" data-i18n-ph="districtPlaceholder" placeholder="Начните вводить название района">
          <button class="clear-btn" id="district-clear" type="button" data-i18n-title="districtClear" data-i18n-aria="districtClear" title="Сбросить район" aria-label="Сбросить район">×</button>
          <ul class="suggest-list" id="district-suggest" hidden></ul>
        </div>
      </div>

      <div class="field" id="complex-field" hidden>
        <label for="complex-select" data-i18n="complexLabel">ЖК / жилой комплекс</label>
        <select id="complex-select"></select>
      </div>

      <div class="field">
        <span class="field-label" data-i18n="postedLabel">Когда опубликовано</span>
        <div class="chip-row" id="days-chips"></div>
      </div>

      <div class="field">
        <span class="field-label" data-i18n="sourcesLabel">Источники</span>
        <div class="chip-row" id="source-chips"></div>
      </div>

      <div class="field">
        <span class="field-label" data-i18n="datesLabel">Даты заезда (Airbnb / Agoda / Trip.com / CozyCozy)</span>
        <div class="date-row">
          <input type="text" placeholder="16.08.2026" disabled>
          <span>—</span>
          <input type="text" placeholder="16.09.2026" disabled>
        </div>
        <p class="field-hint" data-i18n="datesHint">Появится, когда подключим посуточные сервисы — там снимают на даты, а не на месяцы.</p>
      </div>

      <div class="field">
        <span class="field-label" data-i18n="typeLabel">Тип жилья</span>
        <div class="chip-row" id="type-chips"></div>
      </div>

      <div class="field">
        <span class="field-label" data-i18n="sortLabel">Сортировка</span>
        <div class="sort-toggle" id="sort-toggle">
          <button data-sort="asc" class="active" type="button" data-i18n="sortAsc">Дешевле</button>
          <button data-sort="desc" type="button" data-i18n="sortDesc">Дороже</button>
          <button data-sort="new" type="button" data-i18n="sortNew">Новые</button>
        </div>
        <label class="per-m2-toggle-label"><input type="checkbox" id="per-m2-toggle"> <span data-i18n="perM2">сортировать по цене за м²</span></label>
      </div>

      <div class="field" id="poi-sort-field" hidden>
        <label for="poi-sort-select" data-i18n="poiLabel">Ближе к...</label>
        <select id="poi-sort-select">
          <option value="" data-i18n="poiNone">не важно</option>
          <option value="metro" data-i18n="poiMetro">🚇 метро</option>
          <option value="school" data-i18n="poiSchool">🎓 школе</option>
          <option value="hospital" data-i18n="poiHospital">✚ больнице</option>
        </select>
      </div>
    </div>

    <div class="map card">
      <div class="map-head">
        <span class="map-title" id="map-title" data-i18n="mapTitle">Карта района</span>
        <span class="map-note" id="map-note" data-i18n="mapNote">реальные границы районов, OpenStreetMap</span>
        <div class="map-tools">
          <button type="button" class="map-tool" id="map-near-btn" data-i18n="mapNearMe">📍 Рядом со мной</button>
          <button type="button" class="map-tool" id="map-full-btn" data-i18n="mapFullscreen">⤢ На весь экран</button>
        </div>
      </div>
      <!-- Цена и тип прямо в карточке карты (решение владельца 14.09.2026: «ценники в
           самой карточке»): у RentHome они над картой, у нас в развёрнутой карте
           фильтров не было вовсе. Это не копия фильтров, а второй набор тех же
           кнопок: одно состояние, панель слева и карточка карты всегда совпадают. -->
      <div class="map-filters" id="map-filters">
        <div class="map-filter-group">
          <span class="map-filter-label" data-i18n="typeLabel">Тип жилья</span>
          <div class="chip-row" id="map-type-chips"></div>
        </div>
        <div class="map-filter-group">
          <span class="map-filter-label" data-i18n="budgetLabel">Бюджет, млн ₫ / мес</span>
          <div class="chip-row" id="map-budget-chips"></div>
        </div>
        <span class="map-filter-count" id="map-filter-count"></span>
      </div>
      <div id="leaflet-map" class="leaflet-map-el"></div>
      <div class="map-legend">
        <span><i class="swatch" style="background:var(--accent)" aria-hidden="true"></i><span data-i18n="mapLegendPin">цена — место из объявления</span></span>
        <span><i class="swatch swatch-approx" aria-hidden="true"></i><span data-i18n="mapLegendPinApprox">пунктир — приблизительно, центр района</span></span>
        <span><i class="swatch swatch-cluster" aria-hidden="true"></i><span data-i18n="mapLegendCluster">кружок с числом — несколько объявлений рядом</span></span>
        <span data-i18n="mapLegendClick">клик по району на карте — фильтр по нему</span>
        <label class="poi-toggle-label"><input type="checkbox" id="poi-toggle"><span data-i18n="poiToggle">метро / школы / госпитали</span></label>
      </div>
      <p class="map-credit" id="map-credit" data-i18n="mapCredit">Карта и адреса — © участники OpenStreetMap (ODbL). Границы районов актуальны после реформы административного деления 2025 года.</p>
    </div>
  </section>

  <section class="results">
    <div class="results-head">
      <div>
        <h2 id="results-count">— объявлений</h2>
        <p class="results-sub" id="results-context"></p>
      </div>
      <div class="results-head-actions">
        <button class="fav-filter-btn" id="fav-filter-toggle" type="button" aria-pressed="false">☆ <span data-i18n="favFilter">Избранное</span></button>
        <button class="reset-btn" id="reset-filters" type="button" data-i18n="reset">Сбросить фильтры</button>
      </div>
    </div>
    <div class="results-list" id="results-list"></div>
    <div class="empty-state" id="empty-state" hidden>
      <strong data-i18n="emptyTitle">По этим критериям пока пусто</strong>
      <span data-i18n="emptyBody">Попробуйте увеличить бюджет, выбрать другой район или снять фильтр по сроку публикации.</span>
    </div>
  </section>

  <footer class="footer">
    <div class="support card">
      <div class="support-text">
        <h3 data-i18n="supportTitle">Поддержать проект</h3>
        <p data-i18n="supportBody">Сайт бесплатный и без рекламы. Если он помог вам найти жильё — можно поддержать его развитие переводом USDT.</p>
        <p class="support-net"><span data-i18n="supportNetPrefix">Сеть:</span> <strong>TRON (TRC20)</strong> <span data-i18n="supportNetWarn">· отправляйте только USDT в этой сети, иначе перевод потеряется.</span></p>
        <div class="support-addr">
          <code id="usdt-addr">__USDT_ADDR__</code>
          <button type="button" id="copy-addr" class="copy-addr-btn" data-i18n="copy">Скопировать</button>
        </div>
      </div>
      <div class="support-qr" aria-label="QR-код адреса USDT TRC20">__USDT_QR__</div>
    </div>
    <p class="stamp" data-i18n="stamp">Данные актуальны на __TODAY_DATE__ · объявления старше 7 дней исключены из подборки · перед созвоном с хозяином всегда проверяйте цену и наличие по ссылке на объявление.</p>
  </footer>

</div>

<div id="lightbox" class="lightbox" hidden>
  <button type="button" class="lightbox-close" id="lightbox-close" data-i18n-aria="close" aria-label="Закрыть">✕</button>
  <button type="button" class="lightbox-nav lightbox-prev" id="lightbox-prev" data-i18n-aria="prevPhoto" aria-label="Предыдущее фото">‹</button>
  <img class="lightbox-main" id="lightbox-main" src="" alt="">
  <button type="button" class="lightbox-nav lightbox-next" id="lightbox-next" data-i18n-aria="nextPhoto" aria-label="Следующее фото">›</button>
  <div class="lightbox-thumbs" id="lightbox-thumbs"></div>
</div>

<script>
(function(){
  "use strict";

  // Two ways this script gets its data. The all-in-one page (vietnam-rent-finder.html)
  // inlines everything right here. The per-city pages (assets/app.js) get a
  // small inline <script> before this one that sets window.PAGE_DATA (that
  // city + kind only), window.PAGE_DEFAULT_LANG and window.PAGE = {city, kind};
  // in that mode city tabs and the kind toggle are links to sibling pages.
  // The DATA assignment below must stay one plain literal statement in the
  // all-in-one page: site_data.load_data() and check_js_undefined_calls()
  // locate the data by that exact shape (and this comment must not spell it
  // out, or the regex matches the comment first). The per-city override is
  // therefore a separate line.
  var DEFAULT_LANG = "__DEFAULT_LANG__";
  var DATA = __DATA_JSON__;
  if (typeof window.PAGE_DEFAULT_LANG !== "undefined") DEFAULT_LANG = window.PAGE_DEFAULT_LANG;
  if (typeof window.PAGE_DATA !== "undefined") DATA = window.PAGE_DATA;
  var PAGE = window.PAGE || null;
  var COUNTS = DATA.COUNTS || null;
  // Photo URLs arrive with their common prefix folded away (see the compaction
  // note in rebuild_final.py). Expand once, here, so every later use -- the
  // card strip, the lightbox, the map popup -- just reads l.details.photos.
  (function expandPhotos(){
    var CDN = "https://cdn.chotot.com/", MID = "/preset:view/plain/";
    (DATA.LISTINGS || []).forEach(function(l){
      var d = l.details;
      if (!d || !d.photos) return;
      d.photos = d.photos.map(function(u){
        if (u.charAt(0) !== "~") return u;
        var i = u.indexOf("/");
        return CDN + u.slice(1, i) + MID + u.slice(i + 1);
      });
    });
  })();
  // Пометка об источнике приходит номером «~N» в списке NOTICES (см. сжатие в
  // rebuild_final.py): у тысяч строк она одна и та же. Разворачивается здесь же,
  // один раз, поэтому карточка, поиск и панель подробностей читают обычный текст.
  (function expandNotices(){
    var N = DATA.NOTICES || [];
    if (!N.length) return;
    (DATA.LISTINGS || []).forEach(function(l){
      var d = l.details;
      if (!d) return;
      ["notice", "noticeEn"].forEach(function(k){
        var v = d[k];
        if (typeof v === "string" && v.charAt(0) === "~" && N[+v.slice(1)] != null) d[k] = N[+v.slice(1)];
      });
    });
  })();
  var CITIES = DATA.CITIES;
  var SOURCES = DATA.SOURCES;
  var LISTINGS = DATA.LISTINGS;
  function pageHref(city, kind){ return city + (kind === "commercial" ? "-commercial" : "") + ".html"; }

  var SOURCE_LABEL = {};
  SOURCES.forEach(function(s){ SOURCE_LABEL[s.key] = s; });
  var SOURCES_BY_CITY = DATA.SOURCES_BY_CITY || {};

  var DAY_OPTIONS = [1,3,7];
  var BUDGET_CHIPS = [3,5,10,15];
  var DETAIL_ORDER = ["deposit","electricity","water","internet","managementFee","contract","policy","amenities","notice"];

  // Listing `type` is stored in Russian in the data; this maps it for display.
  // The project covers two kinds of property. Listing `type` stays in Russian
  // in the data; TYPE_EN maps it for display, KIND_TYPES splits it by kind.
  var RESIDENTIAL_TYPES = ["Комната","Студия","Квартира","Дом","Другое"];
  var COMMERCIAL_TYPES  = ["Офис","Торговая площадь","Склад"];
  var TYPE_OPTIONS = RESIDENTIAL_TYPES.concat(COMMERCIAL_TYPES);
  var TYPE_EN = {
    "Комната":"Room","Студия":"Studio","Квартира":"Apartment","Дом":"House","Другое":"Other",
    "Офис":"Office","Торговая площадь":"Retail space","Склад":"Warehouse"
  };
  var COMMERCIAL_SET = {};
  COMMERCIAL_TYPES.forEach(function(t){ COMMERCIAL_SET[t] = true; });
  function kindOf(l){ return COMMERCIAL_SET[l.type] ? "commercial" : "residential"; }

  // The page's own language wins on load. index.html IS the Russian page and
  // en.html IS the English one, each with its own <title>, meta and hreflang,
  // so the URL already states which language the visitor asked for.
  //
  // A stored preference used to override this, and it produced exactly the
  // failure en.html exists to prevent: anyone who had once picked Russian --
  // including on the other page, since both share an origin -- then landed on
  // en.html from an English search and got Russian text. The page looked
  // broken to the half of the audience it was built for, and nothing errored.
  //
  // The toggle still switches instantly and keeps your filters, but the choice
  // is not persisted across a reload: the URL decides. Navigating between the
  // two pages on click would keep the address bar in step, but the Artifact
  // build is a single self-contained file with no en.html beside it, so a
  // link there would 404.
  var lang = (typeof DEFAULT_LANG !== "undefined") ? DEFAULT_LANG : "ru";

  var I18N = {
    ru: {
      h1Title:"Жильё во Вьетнаме и на Филиппинах",
      kindLabel:"Тип недвижимости", kindResidential:"Жильё", kindCommercial:"Коммерция",
      tagline:"Комнаты, студии, квартиры и коммерческие помещения в Хошимине, Ханое, Дананге и Нячанге — из реальных объявлений, отсортированные по цене.",
      themeGroup:"Тема оформления", themeAuto:"Авто", themeLight:"Светлая", themeDark:"Тёмная",
      cityGroup:"Город",
      ratesOn:"курс на",
      countryVn:"Вьетнам",
      countryPh:"Филиппины",
      searchLabel:"Поиск по описанию", searchPlaceholder:"например: бассейн, метро, вид на море", searchClear:"Очистить поиск",
      budgetLabel:"Бюджет, млн ₫ / мес", from:"от", to:"до", mln:"млн ₫",
      districtLabel:"Район", districtPlaceholder:"Начните вводить название района", districtClear:"Сбросить район",
      complexLabel:"ЖК / жилой комплекс", complexAny:"Любой ЖК", complexCtx:"ЖК",
      postedLabel:"Когда опубликовано", sourcesLabel:"Источники",
      datesLabel:"Даты заезда (Airbnb / Agoda / Trip.com / CozyCozy)",
      datesHint:"Появится, когда подключим посуточные сервисы — там снимают на даты, а не на месяцы.",
      typeLabel:"Тип жилья", sortLabel:"Сортировка",
      sortAsc:"Дешевле", sortDesc:"Дороже", sortNew:"Новые", perM2:"сортировать по цене за м²",
      poiLabel:"Ближе к...", poiNone:"не важно", poiMetro:"🚇 метро", poiSchool:"🎓 школе", poiHospital:"✚ больнице",
      mapTitle:"Карта района", mapNote:"реальные границы районов, OpenStreetMap",
      mapLegendPin:"цена — место из объявления", mapLegendPinApprox:"пунктир — приблизительно, центр района", mapLegendCluster:"кружок с числом — несколько объявлений рядом", mapFullscreen:"⤢ На весь экран", mapExitFullscreen:"✕ Свернуть карту", mapNearMe:"📍 Рядом со мной", nearMeHere:"Вы здесь", nearMeDenied:"Не удалось узнать, где вы: браузер не дал доступ к местоположению.", nearMeFar:"Рядом с вами нет объявлений этого города — выберите свой город вверху.", mapLegendClick:"клик по району на карте — фильтр по нему",
      poiToggle:"метро / школы / госпитали",
      mapCredit:"Карта и адреса — © участники OpenStreetMap (ODbL). Границы районов актуальны после реформы административного деления 2025 года.",
      mapNoBounds:"нет официальных границ районов — показаны только точки объявлений",
      mapCreditNoBounds:"После реформы 2025 года у Нячанга нет официальных границ на уровне районов, поэтому контуры не показаны — только примерные точки объявлений по районам. Карта — © участники OpenStreetMap (ODbL).",
      mapCreditBounds:"Карта и границы районов — © участники OpenStreetMap (ODbL), границы актуальны после реформы административного деления 2025 года.",
      mapCreditHistoric:"Карта и границы — © участники OpenStreetMap (ODbL). Показаны 12 городских районов Ханоя в границах до реформы 2025 года: именно так район называют арендодатели и агенты, а новые кварталы с теми же именами занимают лишь часть прежней территории.",
      mapUnavailable:"Карта недоступна в этом окне — внешние карты (OpenStreetMap) заблокированы политикой безопасности. Откройте страницу как локальный файл, чтобы увидеть интерактивную карту.",
      favFilter:"Избранное", reset:"Сбросить фильтры",
      emptyTitle:"По этим критериям пока пусто", emptyBody:"Попробуйте увеличить бюджет, выбрать другой район или снять фильтр по сроку публикации.",
      supportTitle:"Поддержать проект",
      supportBody:"Сайт бесплатный и без рекламы. Если он помог вам найти жильё — можно поддержать его развитие переводом USDT.",
      supportNetPrefix:"Сеть:", supportNetWarn:"· отправляйте только USDT в этой сети, иначе перевод потеряется.",
      copy:"Скопировать", copied:"Скопировано ✓", selected:"Выделено — скопируйте",
      close:"Закрыть", prevPhoto:"Предыдущее фото", nextPhoto:"Следующее фото",
      districtsWord:"районов", noDistricts:"Районы не найдены",
      any:"Любой", all:"Все", upTo:"до", soon:"· скоро",
      priceOnRequest:"цена по запросу", perMonth:"/ мес", wasPrice:"было",
      openListing:"Открыть объявление →", alsoOn:"Также встречается на:",
      popupView:"Посмотреть →",
      detailsToggle:"Подробнее (депозит, коммуналка, удобства)",
      approxPos:"📍 положение на карте приблизительное — центр района",
      exactPos:"📍 координаты из самого объявления",
      addFav:"В избранное",
      anyDistrict:"любой район", anyBudget:"любой бюджет", anyType:"любой тип",
      searchCtx:"поиск", forDays:"за", noAdsYet:"пока нет объявлений", adsShort:"объяв.",
      m2:"м²", thousandPerM2:"тыс ₫/м²", mlnShort:"млн", thouShort:"тыс", metres:"м", km:"км",
      detailLabels:{deposit:"Депозит", electricity:"Электричество", water:"Вода", internet:"Интернет/wifi",
        managementFee:"Управление", amenities:"Удобства", policy:"Правила", contract:"Договор", notice:"Важно"},
      stamp:"Данные актуальны на __TODAY_DATE__ · объявления старше 7 дней исключены из подборки · перед созвоном с хозяином всегда проверяйте цену и наличие по ссылке на объявление."
    },
    en: {
      h1Title:"Rental housing in Vietnam and the Philippines",
      kindLabel:"Property kind", kindResidential:"Housing", kindCommercial:"Commercial",
      tagline:"Rooms, studios, apartments and commercial space in Ho Chi Minh City, Hanoi, Da Nang and Nha Trang — from real listings, sorted by price.",
      themeGroup:"Colour theme", themeAuto:"Auto", themeLight:"Light", themeDark:"Dark",
      cityGroup:"City",
      ratesOn:"rates as of",
      countryVn:"Vietnam",
      countryPh:"Philippines",
      searchLabel:"Search descriptions", searchPlaceholder:"e.g. pool, metro, sea view", searchClear:"Clear search",
      budgetLabel:"Budget, million ₫ / month", from:"from", to:"to", mln:"mln ₫",
      districtLabel:"District", districtPlaceholder:"Start typing a district name", districtClear:"Clear district",
      complexLabel:"Residential complex", complexAny:"Any complex", complexCtx:"complex",
      postedLabel:"Posted within", sourcesLabel:"Sources",
      datesLabel:"Check-in dates (Airbnb / Agoda / Trip.com / CozyCozy)",
      datesHint:"Coming when per-night services are added — those are booked by date, not by month.",
      typeLabel:"Property type", sortLabel:"Sort by",
      sortAsc:"Cheaper", sortDesc:"Pricier", sortNew:"Newest", perM2:"sort by price per m²",
      poiLabel:"Closer to...", poiNone:"doesn't matter", poiMetro:"🚇 metro", poiSchool:"🎓 school", poiHospital:"✚ hospital",
      mapTitle:"District map", mapNote:"real district boundaries, OpenStreetMap",
      mapLegendPin:"price — the listing's own location", mapLegendPinApprox:"dashed — approximate, the district centre", mapLegendCluster:"a number in a circle — several listings nearby", mapFullscreen:"⤢ Full screen", mapExitFullscreen:"✕ Close full screen", mapNearMe:"📍 Near me", nearMeHere:"You are here", nearMeDenied:"Could not find your location: the browser did not allow access to it.", nearMeFar:"No listings of this city near you — pick your city above.", mapLegendClick:"click a district on the map to filter by it",
      poiToggle:"metro / schools / hospitals",
      mapCredit:"Map and addresses — © OpenStreetMap contributors (ODbL). District boundaries reflect the 2025 administrative reform.",
      mapNoBounds:"no official district boundaries — only listing points are shown",
      mapCreditNoBounds:"After the 2025 reform Nha Trang has no official district-level boundaries, so outlines are not shown — only approximate listing points by district. Map — © OpenStreetMap contributors (ODbL).",
      mapCreditBounds:"Map and district boundaries — © OpenStreetMap contributors (ODbL), boundaries reflect the 2025 administrative reform.",
      mapCreditHistoric:"Map and boundaries — © OpenStreetMap contributors (ODbL). Hanoi is shown as its 12 urban districts as they were before the 2025 reform: that is how landlords and agents still name an area, and the new wards that reuse those names cover only part of the old district.",
      mapUnavailable:"The map is unavailable in this window — external maps (OpenStreetMap) are blocked by the security policy. Open the page as a local file to see the interactive map.",
      favFilter:"Favourites", reset:"Reset filters",
      emptyTitle:"Nothing matches these filters yet", emptyBody:"Try raising the budget, picking another district, or clearing the posted-within filter.",
      supportTitle:"Support the project",
      supportBody:"This site is free and ad-free. If it helped you find a place, you can support it with a USDT transfer.",
      supportNetPrefix:"Network:", supportNetWarn:"· send USDT on this network only, otherwise the transfer is lost.",
      copy:"Copy", copied:"Copied ✓", selected:"Selected — copy it",
      close:"Close", prevPhoto:"Previous photo", nextPhoto:"Next photo",
      districtsWord:"districts", noDistricts:"No districts found",
      any:"Any", all:"All", upTo:"up to", soon:"· soon",
      priceOnRequest:"price on request", perMonth:"/ month", wasPrice:"was",
      openListing:"Open listing →", alsoOn:"Also listed on:",
      popupView:"View listing →",
      detailsToggle:"More details (deposit, utilities, amenities)",
      approxPos:"📍 approximate position — the district centre",
      exactPos:"📍 coordinates from the listing itself",
      addFav:"Add to favourites",
      anyDistrict:"any district", anyBudget:"any budget", anyType:"any type",
      searchCtx:"search", forDays:"within", noAdsYet:"no listings yet", adsShort:"listings",
      m2:"m²", thousandPerM2:"k ₫/m²", mlnShort:"mln", thouShort:"k", metres:"m", km:"km",
      detailLabels:{deposit:"Deposit", electricity:"Electricity", water:"Water", internet:"Internet/wifi",
        managementFee:"Management fee", amenities:"Amenities", policy:"House rules", contract:"Contract", notice:"Important"},
      stamp:"Data current as of __TODAY_DATE_EN__ · listings older than 7 days are excluded · always confirm price and availability via the original listing before calling the owner."
    }
  };

  function t(key){ return (I18N[lang] && I18N[lang][key] !== undefined) ? I18N[lang][key] : I18N.ru[key]; }
  // Russian uses a decimal comma, English a decimal point.
  function decSep(s){ return lang === "en" ? s : s.replace(".", ","); }

  function applyLang(next){
    lang = next;
    document.documentElement.setAttribute("lang", lang);
    var lt = document.getElementById("lang-toggle");
    if (lt){
      Array.prototype.forEach.call(lt.querySelectorAll("button"), function(b){
        b.classList.toggle("active", b.getAttribute("data-lang") === lang);
      });
    }
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n]"), function(node){
      var key = node.getAttribute("data-i18n");
      node.textContent = t(key);
    });
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n-ph]"), function(node){
      node.setAttribute("placeholder", t(node.getAttribute("data-i18n-ph")));
    });
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n-aria]"), function(node){
      node.setAttribute("aria-label", t(node.getAttribute("data-i18n-aria")));
    });
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n-title]"), function(node){
      node.setAttribute("title", t(node.getAttribute("data-i18n-title")));
    });
    // re-render everything that builds its own strings in JS
    renderCityTabs(); renderCityMap(); renderBudgetChips(); renderDaysChips();
    renderSourceChips(); renderTypeChips(); renderComplexFilter(); applyFilters();
    el.favFilterToggle.textContent = (state.showFavoritesOnly ? "★" : "☆") + " " + t("favFilter");
  }

  function initLang(){
    var lt = document.getElementById("lang-toggle");
    if (lt){
      lt.addEventListener("click", function(e){
        var btn = e.target.closest("button[data-lang]");
        if (!btn) return;
        applyLang(btn.getAttribute("data-lang"));
      });
    }
    applyLang(lang);
  }
  function cityName(c){ return (lang === "en" && c.nameEn) ? c.nameEn : c.name; }
  function districtHint(d){ return (lang === "en" && d.hintEn) ? d.hintEn : d.hint; }
  function typeName(tp){ return (lang === "en" && TYPE_EN[tp]) ? TYPE_EN[tp] : tp; }
  // Listings gain an English description over time (the daily checks write
  // descEn for every new listing, and the 7-day purge cycles the whole
  // dataset), so fall back to the Russian text until one exists.
  function descText(l){ return (lang === "en" && l.descEn) ? l.descEn : l.desc; }
  function sourceLabel(s){ return (lang === "en" && s.labelEn) ? s.labelEn : s.label; }
  function noticeText(d){ return (lang === "en" && d.noticeEn) ? d.noticeEn : d.notice; }
  function postedText(l){
    if (lang !== "en") return l.posted;
    if (l.daysAgo === 0) return "today";
    if (l.daysAgo === 1) return "yesterday";
    return l.daysAgo + " days ago";
  }

  var state = {
    city: PAGE ? PAGE.city : "nha-trang", district: null, complex: null, minBudget: null, maxBudget: null, maxDays: 7, sort: "asc", type: null, kind: PAGE ? PAGE.kind : "residential", poiSort: "", textSearch: "", showFavoritesOnly: false, perM2: false,
    sources: new Set(SOURCES.filter(function(s){ return s.active; }).map(function(s){ return s.key; })),
    openDetails: new Set()
  };

  var THEME_KEY = "rentSearcherTheme";
  function applyTheme(choice){
    var root = document.documentElement;
    if (choice === "light" || choice === "dark") root.setAttribute("data-theme", choice);
    else root.removeAttribute("data-theme");
    var toggle = document.getElementById("theme-toggle");
    if (toggle){
      Array.prototype.forEach.call(toggle.querySelectorAll("button"), function(b){
        b.classList.toggle("active", b.getAttribute("data-theme-choice") === choice);
      });
    }
    if (typeof setTiles === "function") setTiles();
  }
  function initTheme(){
    var saved = "auto";
    try { saved = localStorage.getItem(THEME_KEY) || "auto"; } catch (e) {}
    applyTheme(saved);
    var toggle = document.getElementById("theme-toggle");
    if (toggle){
      toggle.addEventListener("click", function(e){
        var btn = e.target.closest("button[data-theme-choice]");
        if (!btn) return;
        var choice = btn.getAttribute("data-theme-choice");
        applyTheme(choice);
        try { localStorage.setItem(THEME_KEY, choice); } catch (e2) {}
      });
    }
  }

  var FAVORITES_KEY = "rentSearcherFavorites";
  var favorites = (function(){
    try {
      var raw = localStorage.getItem(FAVORITES_KEY);
      return new Set(raw ? JSON.parse(raw) : []);
    } catch (e) { return new Set(); }
  })();
  function saveFavorites(){
    try { localStorage.setItem(FAVORITES_KEY, JSON.stringify(Array.from(favorites))); } catch (e) {}
  }
  function toggleFavorite(id){
    if (favorites.has(id)) favorites.delete(id); else favorites.add(id);
    saveFavorites();
  }

  // Commercial rents reach ~160M VND/month while almost all housing sits under
  // 45M. One shared ceiling cannot serve both: at 45 the commercial listings are
  // invisible, at 300 the residential slider is unusable because everything
  // bunches into its first sixth. So the ceiling follows the selected kind.
  var BUDGET_MIN = 0;
  var BUDGET_MAX_RESIDENTIAL = 45, BUDGET_MAX_COMMERCIAL = 300;
  var BUDGET_MAX = BUDGET_MAX_RESIDENTIAL;

  var el = {
    cityTabs: document.getElementById("city-tabs"),
    textSearchInput: document.getElementById("text-search-input"),
    textSearchClear: document.getElementById("text-search-clear"),
    budgetMinInput: document.getElementById("budget-min-input"),
    budgetMaxInput: document.getElementById("budget-max-input"),
    budgetMinRange: document.getElementById("budget-min-range"),
    budgetMaxRange: document.getElementById("budget-max-range"),
    budgetRangeFill: document.getElementById("budget-range-fill"),
    budgetChips: document.getElementById("budget-chips"),
    districtInput: document.getElementById("district-input"),
    districtClear: document.getElementById("district-clear"),
    districtSuggest: document.getElementById("district-suggest"),
    complexField: document.getElementById("complex-field"),
    complexSelect: document.getElementById("complex-select"),
    daysChips: document.getElementById("days-chips"),
    sourceChips: document.getElementById("source-chips"),
    typeChips: document.getElementById("type-chips"),
    sortToggle: document.getElementById("sort-toggle"),
    perM2Toggle: document.getElementById("per-m2-toggle"),
    poiSortField: document.getElementById("poi-sort-field"),
    poiSortSelect: document.getElementById("poi-sort-select"),
    mapTitle: document.getElementById("map-title"),
    mapSvgWrap: document.getElementById("leaflet-map"),
    resultsCount: document.getElementById("results-count"),
    mapTypeChips: document.getElementById("map-type-chips"),
    mapBudgetChips: document.getElementById("map-budget-chips"),
    mapFilterCount: document.getElementById("map-filter-count"),
    resultsContext: document.getElementById("results-context"),
    resultsList: document.getElementById("results-list"),
    favFilterToggle: document.getElementById("fav-filter-toggle"),
    emptyState: document.getElementById("empty-state"),
    resetBtn: document.getElementById("reset-filters")
  };

  function fmtPrice(v){
    var m = v/1000000;
    var s = (m % 1 === 0) ? String(m) : decSep(m.toFixed(1));
    return s + " " + t("mlnShort");
  }
  // Валюта объявления. Основная сумма всегда в ней: человек, который смотрит
  // жильё в Себу, должен видеть песо, а не наш пересчёт.
  var CUR_SYM = {VND:"₫", PHP:"₱", RUB:"₽", USD:"$", EUR:"€", CNY:"¥"};
  var RATES = DATA.RATES || null;
  function curOf(l){ return l.cur || (RATES ? RATES.base : "VND"); }
  function groupNum(n){
    return String(Math.round(n)).replace(/(\d)(?=(\d{3})+$)/g, "$1 ");
  }
  function fmtMoney(v, cur){
    // донг показываем миллионами, как и раньше; остальные валюты -- целым числом
    if (cur === "VND") return fmtPrice(v) + " ₫";
    return groupNum(v) + " " + (CUR_SYM[cur] || cur);
  }
  function convShort(n){
    if (n >= 1000000) return groupNum(n/1000000 * 10)/10 + " млн";
    if (n >= 1000) return groupNum(Math.round(n/100)*100);
    return groupNum(n);
  }
  // Пересчёт в скобках: рубли, доллары, евро, юани -- по курсу с датой.
  function convLine(v, cur){
    if (!RATES || v == null) return "";
    var usd = v / RATES.perUsd[cur];
    var out = [];
    for (var i = 0; i < RATES.show.length; i++){
      var c = RATES.show[i];
      if (c === cur) continue;
      out.push(convShort(usd * RATES.perUsd[c]) + " " + (CUR_SYM[c] || c));
    }
    return out.join(" · ");
  }
  // Считаем от НОРМАЛИЗОВАННОЙ цены (pv, приведена к донгам на сборке), а не от
  // l.price. Подпись у этой строки -- «тыс ₫/м²», и делить на площадь цену в
  // песо или долларах значило подписывать донгами чужую валюту: квартира за
  // 15 000 ₱ на 35 м² показывала «0 тыс ₫/м²» вместо ~178. Так было у всех
  // филиппинских строк с площадью, и так же ломалась сортировка по цене за метр
  // -- она уводила их в самый низ. Найдено 8 сентября 2026 на первой строке в
  // долларах, но задето было ещё 217 филиппинских.
  function pricePerM2(l){
    var base = (l.pv != null) ? l.pv : l.price;
    if (base == null || !l.area) return null;
    return base / l.area;
  }
  function fmtPricePerM2(v){
    return Math.round(v/1000) + " " + t("thousandPerM2");
  }
  function districtByKey(cityKey, distKey){
    var list = CITIES[cityKey].districts;
    for (var i=0;i<list.length;i++){ if (list[i].key===distKey) return list[i]; }
    return null;
  }
  function listingSearchText(l){
    if (l._searchText) return l._searchText;
    var d = districtByKey(l.city, l.district);
    var parts = [l.desc, l.descEn || "", l.type, d ? d.name : "", l.complex || ""];
    if (l.details){
      ["amenities","notice","contract","deposit"].forEach(function(k){ if (l.details[k]) parts.push(l.details[k]); });
    }
    l._searchText = parts.join(" ").toLowerCase();
    return l._searchText;
  }
  function countsForCity(cityKey){
    var counts = {};
    LISTINGS.forEach(function(l){ if (l.city !== cityKey) return; counts[l.district] = (counts[l.district]||0) + 1; });
    return counts;
  }

  // `complex` is filled in at build time (see the COMPLEX_DICT pass in
  // rebuild_final.py) and only a minority of listings carry one, so the whole
  // control hides itself in a city where nothing was detected.
  function complexesForCity(cityKey){
    var counts = {};
    LISTINGS.forEach(function(l){
      if (l.city !== cityKey || !l.complex) return;
      if (l.details && l.details.duplicateOf) return;
      counts[l.complex] = (counts[l.complex]||0) + 1;
    });
    return Object.keys(counts).sort(function(a,b){
      return counts[b]-counts[a] || a.localeCompare(b);
    }).map(function(n){ return {name:n, count:counts[n]}; });
  }

  function renderComplexFilter(){
    var items = complexesForCity(state.city);
    var stillThere = false;
    items.forEach(function(c){ if (c.name === state.complex) stillThere = true; });
    if (state.complex && !stillThere) state.complex = null;
    el.complexField.hidden = (items.length === 0);
    el.complexSelect.innerHTML = "";
    var any = document.createElement("option");
    any.value = ""; any.textContent = t("complexAny");
    el.complexSelect.appendChild(any);
    items.forEach(function(c){
      var o = document.createElement("option");
      o.value = c.name; o.textContent = c.name + " (" + c.count + ")";
      el.complexSelect.appendChild(o);
    });
    el.complexSelect.value = state.complex || "";
  }

  function renderCityTabs(){
    el.cityTabs.innerHTML = "";
    var lastCountry = null;
    Object.keys(CITIES).forEach(function(key){
      var c = CITIES[key];
      // Вторая страна появилась 4 сентября 2026. Без подписи Думагете стоял бы
      // вплотную к Далату и ничто не сказало бы, что это другая страна.
      var country = c.country || "vn";
      if (country !== lastCountry){
        var head = document.createElement("span");
        head.className = "city-group";
        head.textContent = t(country === "ph" ? "countryPh" : "countryVn");
        el.cityTabs.appendChild(head);
        lastCountry = country;
      }
      // Per-city pages: the tab is a real link to that city's page for the
      // same kind, with the listing count for the kind. All-in-one page: a
      // button that switches in place, with the district count as before.
      // Отсутствие записи в COUNTS означает «ноль», а не «неизвестно»: COUNTS
      // строится по объявлениям, и город без единого объявления в него просто
      // не попадает. Пока здесь стоял null, такой город показывал число районов
      // («Фукуок · 7 районов») и потому не получал пометку empty, хотя сосед с
      // одним коммерческим объявлением честно показывал «0 объяв.». Число
      // районов остаётся запасным вариантом только когда COUNTS нет вовсе.
      var n = COUNTS ? ((COUNTS[key] && COUNTS[key][state.kind]) || 0) : null;
      var sub = (n !== null) ? (n + " " + t("adsShort")) : (c.districts.length + " " + t("districtsWord"));
      var btn;
      if (PAGE){
        btn = document.createElement("a");
        btn.href = pageHref(key, state.kind);
      } else {
        btn = document.createElement("button");
        btn.type = "button";
        btn.addEventListener("click", function(){ selectCity(key); });
      }
      btn.className = "city-tab"; btn.setAttribute("role","tab");
      btn.setAttribute("aria-selected", state.city===key ? "true":"false");
      if (PAGE && n === 0) btn.classList.add("empty");
      btn.innerHTML = cityName(c) + '<span class="sub">' + sub + "</span>";
      el.cityTabs.appendChild(btn);
    });
  }

  function selectCity(key){
    if (PAGE){ location.href = pageHref(key, state.kind); return; }
    state.city = key; state.district = null; state.complex = null; el.districtInput.value = "";
    renderCityTabs(); renderCityMap(); updatePoiSortAvailability(); renderSourceChips(); renderComplexFilter(); applyFilters();
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

  function haversineKm(lat1, lon1, lat2, lon2){
    var R = 6371;
    var dLat = (lat2-lat1) * Math.PI/180;
    var dLon = (lon2-lon1) * Math.PI/180;
    var a = Math.sin(dLat/2)*Math.sin(dLat/2) +
      Math.cos(lat1*Math.PI/180)*Math.cos(lat2*Math.PI/180)*Math.sin(dLon/2)*Math.sin(dLon/2);
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  }

  function nearestPoiKm(l, poiType){
    var list = POIS[l.city];
    if (!list || l.lat == null || l.lon == null) return null;
    var best = null;
    list.forEach(function(p){
      if (p.type !== poiType) return;
      var km = haversineKm(l.lat, l.lon, p.lat, p.lon);
      if (best === null || km < best) best = km;
    });
    return best;
  }

  function fmtDist(km){
    if (km < 1) return Math.round(km*1000) + " " + t("metres");
    return decSep(km.toFixed(1)) + " " + t("km");
  }

  function updatePoiSortAvailability(){
    var list = POIS[state.city] || [];
    var typesPresent = new Set(list.map(function(p){ return p.type; }));
    var hasPois = list.length > 0;
    el.poiSortField.hidden = !hasPois;
    Array.prototype.forEach.call(el.poiSortSelect.querySelectorAll("option[value]"), function(opt){
      if (opt.value === "") return;
      opt.hidden = !typesPresent.has(opt.value);
    });
    if (state.poiSort && !typesPresent.has(state.poiSort)){
      state.poiSort = "";
      el.poiSortSelect.value = "";
    }
  }

  // ПОДЛОЖКА. Стандартный стиль OSM рисует всё сразу -- дороги цветом, парки,
  // вывески, -- и зелёные пины на нём теряются; в тёмной теме сайта он был
  // белым пятном посреди тёмной страницы. У renthome.pro спокойная подложка
  // CARTO, но она теперь только с ключом: 11 сентября 2026 CARTO без ключа
  // отдавал вместо карты водяной знак «API KEY REQUIRED» -- с кодом 200, так
  // что проверка по статусу ответа его пропускает (я на этом и попался). Их
  // ключ стоит в адресе каждого их тайла, но он их. Поэтому тайлы остаются
  // свои, OSM, а спокойными их делает CSS-фильтр на слое тайлов -- пины и
  // границы районов он не трогает. Ни стороннего сервиса, ни ключа.
  var TILE_URL = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
  var TILE_ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors';
  var meMarker = null;
  function isDarkTheme(){
    var th = document.documentElement.getAttribute("data-theme");
    if (th) return th === "dark";
    return !!(window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches);
  }
  function setTiles(){
    var box = document.getElementById("leaflet-map");
    if (!box) return;
    var dark = isDarkTheme();
    box.classList.toggle("tiles-dark", dark);
    box.classList.toggle("tiles-light", !dark);
  }

  function toggleMapFull(){
    var card = document.querySelector(".map.card");
    if (!card || !leafletMap) return;
    var on = !card.classList.contains("map-full");
    card.classList.toggle("map-full", on);
    document.body.classList.toggle("map-full-open", on);
    var btn = document.getElementById("map-full-btn");
    if (btn){
      // data-i18n меняется вместе с текстом: иначе переключение языка вернуло
      // бы на развёрнутой карте надпись «На весь экран».
      btn.setAttribute("data-i18n", on ? "mapExitFullscreen" : "mapFullscreen");
      btn.textContent = t(on ? "mapExitFullscreen" : "mapFullscreen");
    }
    setTimeout(function(){ leafletMap.invalidateSize(); }, 80);
  }

  function nearMe(){
    var note = document.getElementById("map-note");
    if (!leafletReady) return;
    if (!navigator.geolocation){ if (note) note.textContent = t("nearMeDenied"); return; }
    var btn = document.getElementById("map-near-btn");
    if (btn) btn.disabled = true;
    navigator.geolocation.getCurrentPosition(function(p){
      if (btn) btn.disabled = false;
      var here = [p.coords.latitude, p.coords.longitude];
      if (meMarker) leafletMap.removeLayer(meMarker);
      meMarker = L.circleMarker(here, {radius: 8, weight: 3, color: "#fff", fillColor: "#2F7CF6", fillOpacity: 1})
        .bindTooltip(t("nearMeHere")).addTo(leafletMap);
      // Ближайшее объявление ЭТОГО города. Дальше 30 км -- человек в другом
      // городе, и увести карту к нему значит показать пустоту; честнее сказать,
      // что выбрать.
      var best = null;
      LISTINGS.forEach(function(l){
        if (l.city !== state.city || typeof l.lat !== "number") return;
        var km = haversineKm(here[0], here[1], l.lat, l.lon);
        if (best === null || km < best) best = km;
      });
      if (best === null || best > 30){ if (note) note.textContent = t("nearMeFar"); return; }
      leafletMap.setView(here, 15);
    }, function(){
      if (btn) btn.disabled = false;
      if (note) note.textContent = t("nearMeDenied");
    }, {enableHighAccuracy: false, timeout: 10000, maximumAge: 300000});
  }

  function initLeafletMap(){
    if (leafletMap || typeof L === "undefined") return;
    leafletMap = L.map("leaflet-map", {scrollWheelZoom:true});
    L.tileLayer(TILE_URL, {maxZoom: 19, attribution: TILE_ATTR}).addTo(leafletMap);
    setTiles();
    if (window.matchMedia){
      var mq = window.matchMedia("(prefers-color-scheme: dark)");
      if (mq.addEventListener) mq.addEventListener("change", setTiles);
    }
    wardLayerGroup = L.layerGroup().addTo(leafletMap);
    // КЛАСТЕРЫ. Без них в Хошимине на экран ложилась тысяча точек, и выбрать
    // одну было нельзя; раньше это лечилось раздвиганием одинаковых точек по
    // спирали. Кластер решает то же честнее: «12» на месте двенадцати
    // объявлений, при нажатии -- приближение, а у точек в одном месте -- веер.
    // Не загрузилась библиотека -- карта работает по-старому, без кластеров.
    markerLayerGroup = (typeof L.markerClusterGroup === "function")
      ? L.markerClusterGroup({
          showCoverageOnHover: false, spiderfyOnMaxZoom: true, chunkedLoading: true,
          maxClusterRadius: 56,
          iconCreateFunction: function(c){
            var n = c.getChildCount(), px = n < 10 ? 34 : (n < 100 ? 40 : 48);
            return L.divIcon({html: '<div class="cluster-pin" style="width:' + px + 'px;height:' + px + 'px">' + n + '</div>',
                              className: "cluster-wrap", iconSize: [px, px]});
          }
        })
      : L.layerGroup();
    markerLayerGroup.addTo(leafletMap);
    poiLayerGroup = L.layerGroup().addTo(leafletMap);
    leafletReady = true;
    var fullBtn = document.getElementById("map-full-btn");
    if (fullBtn) fullBtn.addEventListener("click", toggleMapFull);
    var nearBtn = document.getElementById("map-near-btn");
    if (nearBtn) nearBtn.addEventListener("click", nearMe);
    document.addEventListener("keydown", function(e){
      if (e.key === "Escape" && document.body.classList.contains("map-full-open")) toggleMapFull();
    });
    // Карта, размеченная в контейнере без ширины (скрытая вкладка, ещё не
    // разложенная страница), запоминает этот размер: Leaflet подгоняет город
    // под 4 пикселя и ставит максимальное приближение -- пустой квадрат вместо
    // карты. Так было и до кластеров, просто точки тогда тоже были не видны.
    // Найдено 11 сентября 2026 в скрытой панели браузера. Когда у контейнера
    // появляется настоящая ширина, город подгоняется заново.
    if (window.ResizeObserver){
      var box = document.getElementById("leaflet-map");
      var lastW = box.offsetWidth;
      new ResizeObserver(function(){
        var w = box.offsetWidth;
        if (!w || w === lastW) return;
        leafletMap.invalidateSize();
        if (lastW < 50 && w >= 50) renderCityMap();
        lastW = w;
      }).observe(box);
    }
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
    el.mapTitle.textContent = t("mapTitle") + " — " + cityName(city);
    var noteEl = document.getElementById("map-note");
    var creditEl = document.getElementById("map-credit");
    var boundaries = WARD_BOUNDARIES[state.city];
    if (!boundaries){
      noteEl.textContent = t("mapNoBounds");
      creditEl.textContent = t("mapCreditNoBounds");
    } else {
      noteEl.textContent = t("mapNote");
      // Hanoi's outlines are the pre-2025 districts on purpose (see build_leaflet_data.py)
      creditEl.textContent = (state.city === "ha-noi") ? t("mapCreditHistoric") : t("mapCreditBounds");
    }
    if (!leafletReady){
      el.mapSvgWrap.innerHTML = '<div style="padding:32px 16px;text-align:center;color:var(--ink-dim);font-size:0.88rem;">' + t("mapUnavailable") + '</div>';
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
        poly.bindTooltip(d.name + (cnt ? (" — " + cnt + " " + t("adsShort")) : (" — " + t("noAdsYet"))));
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
    var dsc = descText(l);
    var desc = dsc.length > 100 ? dsc.slice(0,100) + "…" : dsc;
    var priceHtml = (l.price===null) ? t("priceOnRequest") : fmtMoney(l.price, curOf(l));
    return '<div class="pt-top"><span class="pt-src">' + src.short + '</span><span class="pt-price">' + priceHtml + '</span></div>' +
      '<div class="pt-meta">' + typeName(l.type) + ' · ' + d.name + (l.area ? (" · " + l.area + " " + t("m2")) : "") + '</div>' +
      '<div class="pt-desc">' + desc + '</div>' +
      // До 9 сентября 2026 эта строка стояла у КАЖДОГО пина. Тогда это была
      // правда: почти все точки были центроидами районов. Теперь 91% пинов --
      // это координаты из самого объявления, и называть их приблизительными
      // значит врать про собственные данные в обе стороны сразу.
      '<div class="pt-approx">' + t(l.geocoded ? "exactPos" : "approxPos") + '</div>' +
      '<a class="pt-view" href="' + l.url + '" target="_blank" rel="noopener">' + t("popupView") + '</a>';
  }

  // Listings that share one coordinate -- every ward-centroid fallback in a
  // district, or several units in one building -- used to stack on a single
  // pixel: only the top marker was clickable and the other 75 (the worst
  // HCMC case) were unreachable. Spread each such group on a sunflower
  // spiral a few metres across; stable per id, so pins don't jump between
  // renders. Precisely-geocoded singletons are left exactly where they are.
  function spreadStackedPins(list){
    var groups = {};
    list.forEach(function(l){
      if (typeof l.lat !== "number" || typeof l.lon !== "number") return;
      var key = l.lat.toFixed(5) + "," + l.lon.toFixed(5);
      (groups[key] = groups[key] || []).push(l);
    });
    var pos = {};
    Object.keys(groups).forEach(function(key){
      var g = groups[key];
      if (g.length === 1){ pos[g[0].id] = [g[0].lat, g[0].lon]; return; }
      g.sort(function(a, b){ return a.id - b.id; });
      var lat0 = g[0].lat, lon0 = g[0].lon;
      var mPerDegLat = 111320, mPerDegLon = 111320 * Math.cos(lat0 * Math.PI / 180);
      var spacing = g.length > 20 ? 7 : 9;                 // metres between neighbours
      g.forEach(function(l, i){
        var r = spacing * Math.sqrt(i + 1), a = i * 2.39996;   // golden angle
        pos[l.id] = [lat0 + (r * Math.sin(a)) / mPerDegLat, lon0 + (r * Math.cos(a)) / mPerDegLon];
      });
    });
    return pos;
  }

  // Подпись на пине -- цена коротко: «12,5 млн» для донгов (у вьетнамских
  // страниц валюта одна), «45 тыс ₱», «1 060 $». Пин с ценой отвечает на
  // главный вопрос прямо на карте; кружок-точку приходилось наводить по одному.
  function pinPrice(l){
    if (l.price === null) return "—";
    var cur = curOf(l), v = l.price;
    if (cur === "VND") return fmtPrice(v);
    var sym = CUR_SYM[cur] || cur;
    if (v >= 10000) return groupNum(v / 1000) + " " + t("thouShort") + " " + sym;
    return groupNum(v) + " " + sym;
  }

  function renderLeafletMarkers(list){
    if (!leafletReady) return;
    markerLayerGroup.clearLayers();
    var clustered = typeof markerLayerGroup.addLayers === "function";
    // Раздвигать одинаковые точки нужно только без кластеров: кластер сам
    // раскрывает их веером, а точки, раздвинутые на метры, он раскрыл бы лишь
    // на самом крупном масштабе, после пяти нажатий подряд.
    var pos = clustered ? {} : spreadStackedPins(list);
    var coarsePointer = !!(window.matchMedia && window.matchMedia("(pointer: coarse)").matches);
    var batch = [];
    list.forEach(function(l){
      if (typeof l.lat !== "number" || typeof l.lon !== "number") return;
      var icon = L.divIcon({
        className: "pin-wrap", iconSize: null, popupAnchor: [0, -32],
        html: '<div class="price-pin' + (l.geocoded ? "" : " approx") + '">' + pinPrice(l) + '</div>'
      });
      var marker = L.marker(pos[l.id] || [l.lat, l.lon], {icon: icon, keyboard: false});
      // A tap/click never navigates away: it opens the card and PINS it, so
      // the person can read it; the card's own "Посмотреть" link is the only
      // way to the source. Hover still previews on mouse devices; on touch
      // there is no hover, and emulated mouseout must not close a pinned card
      // before the link inside it can be tapped.
      marker.bindPopup(popupHtml(l), {closeButton:true, maxWidth:240, autoPanPadding:[24,24]});
      marker.off("click");                       // drop Leaflet's open/close toggle
      var pinned = false;
      function setActive(on){
        var node = marker.getElement();
        var pill = node && node.querySelector(".price-pin");
        if (pill) pill.classList.toggle("active", on);
        marker.setZIndexOffset(on ? 1000 : 0);
      }
      marker.on("click", function(){ pinned = true; marker.openPopup(); setActive(true); });
      marker.on("popupclose", function(){ pinned = false; setActive(false); });
      if (!coarsePointer){
        marker.on("mouseover", function(){ if (!pinned) marker.openPopup(); setActive(true); });
        marker.on("mouseout", function(){ if (!pinned){ marker.closePopup(); setActive(false); } });
      }
      batch.push(marker);
    });
    if (clustered) markerLayerGroup.addLayers(batch);
    else batch.forEach(function(m){ m.addTo(markerLayerGroup); });
  }

  function renderSuggestions(){
    var q = el.districtInput.value.trim().toLowerCase();
    var city = CITIES[state.city];
    var matches = city.districts.filter(function(d){
      return !q || d.name.toLowerCase().indexOf(q)!==-1 || districtHint(d).toLowerCase().indexOf(q)!==-1;
    });
    el.districtSuggest.innerHTML = "";
    if (matches.length===0){
      var li = document.createElement("li"); li.className = "suggest-empty"; li.textContent = t("noDistricts");
      el.districtSuggest.appendChild(li);
    } else {
      matches.forEach(function(d){
        var li = document.createElement("li");
        var b = document.createElement("button"); b.type = "button";
        b.innerHTML = "<span>"+d.name+"</span><span class='hint'>"+districtHint(d)+"</span>";
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

  el.textSearchInput.addEventListener("input", function(){
    state.textSearch = el.textSearchInput.value.trim().toLowerCase();
    applyFilters();
  });
  el.textSearchClear.addEventListener("click", function(){
    state.textSearch = ""; el.textSearchInput.value = ""; applyFilters(); el.textSearchInput.focus();
  });

  el.favFilterToggle.addEventListener("click", function(){
    state.showFavoritesOnly = !state.showFavoritesOnly;
    el.favFilterToggle.setAttribute("aria-pressed", state.showFavoritesOnly);
    el.favFilterToggle.textContent = (state.showFavoritesOnly ? "★" : "☆") + " " + t("favFilter");
    applyFilters();
  });

  function renderBudgetChips(){
    fillBudgetChips(el.budgetChips);
    if (el.mapBudgetChips) fillBudgetChips(el.mapBudgetChips);
  }

  function fillBudgetChips(box){
    box.innerHTML = "";
    var allBtn = document.createElement("button");
    allBtn.type="button"; allBtn.className="chip"; allBtn.textContent=t("any");
    allBtn.setAttribute("aria-pressed", (state.maxBudget===null && state.minBudget===null) ? "true":"false");
    allBtn.addEventListener("click", function(){ setBudgetRange(BUDGET_MIN, BUDGET_MAX); });
    box.appendChild(allBtn);
    BUDGET_CHIPS.forEach(function(v){
      var b = document.createElement("button");
      b.type="button"; b.className="chip"; b.textContent=t("upTo") + " " + v;
      b.setAttribute("aria-pressed", (state.maxBudget===v && state.minBudget===null) ? "true":"false");
      b.addEventListener("click", function(){ setBudgetRange(BUDGET_MIN, v); });
      box.appendChild(b);
    });
  }

  function clampBudget(v){
    if (isNaN(v)) return BUDGET_MIN;
    return Math.max(BUDGET_MIN, Math.min(BUDGET_MAX, v));
  }

  function setBudgetRange(lo, hi, opts){
    lo = clampBudget(lo); hi = clampBudget(hi);
    if (lo > hi){ var t=lo; lo=hi; hi=t; }
    state.minBudget = (lo <= BUDGET_MIN) ? null : lo;
    state.maxBudget = (hi >= BUDGET_MAX) ? null : hi;
    syncBudgetUI(opts);
    renderBudgetChips();
    applyFilters();
  }

  function syncBudgetUI(opts){
    // The bounds live here, not only in setupBudgetSlider: that runs once at
    // init, so when BUDGET_MAX moves (housing 45M -> commercial 300M) the
    // inputs kept the old ceiling and the wider range was unreachable.
    el.budgetMinRange.min = el.budgetMaxRange.min = el.budgetMinInput.min = el.budgetMaxInput.min = BUDGET_MIN;
    el.budgetMinRange.max = el.budgetMaxRange.max = el.budgetMinInput.max = el.budgetMaxInput.max = BUDGET_MAX;
    var lo = state.minBudget===null ? BUDGET_MIN : state.minBudget;
    var hi = state.maxBudget===null ? BUDGET_MAX : state.maxBudget;
    // While the user is typing in one of the number fields, leave BOTH text
    // fields alone: writing the normalised value back on every keystroke made
    // it impossible to clear a field or type "6" over "45" on a phone (the
    // empty field snapped straight back to 0 / 45). The fields are
    // normalised on "change" (blur / Enter) instead. Sliders and the fill
    // bar still follow every keystroke.
    if (!(opts && opts.skipInputs)){
      el.budgetMinInput.value = lo;
      el.budgetMaxInput.value = hi;
    }
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
    // Typed budget: read what is in the field, never write into it mid-edit.
    // An empty or half-typed field means "no bound for now"; the value is
    // only clamped/ordered in state, and the field itself is tidied on
    // "change" (blur or Enter). Without this, phones could not delete a digit.
    function typedBudget(inp, fallback){
      var raw = inp.value.trim().replace(",", ".");
      if (raw === "" || raw === "." || raw === "-") return fallback;
      var v = parseFloat(raw);
      return isNaN(v) ? fallback : v;
    }
    el.budgetMinInput.addEventListener("input", function(){
      var hi = state.maxBudget===null ? BUDGET_MAX : state.maxBudget;
      var lo = Math.min(typedBudget(el.budgetMinInput, BUDGET_MIN), hi);
      setBudgetRange(lo, hi, {skipInputs:true});
    });
    el.budgetMaxInput.addEventListener("input", function(){
      var lo = state.minBudget===null ? BUDGET_MIN : state.minBudget;
      var hi = Math.max(typedBudget(el.budgetMaxInput, BUDGET_MAX), lo);
      setBudgetRange(lo, hi, {skipInputs:true});
    });
    // Leaving the field (or pressing Enter) writes the normalised value back.
    el.budgetMinInput.addEventListener("change", function(){ syncBudgetUI(); });
    el.budgetMaxInput.addEventListener("change", function(){ syncBudgetUI(); });
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
    if (lang === "en") return n === 1 ? "day" : "days";
    if (n===1) return "день";
    if ([2,3,4].indexOf(n)!==-1) return "дня";
    return "дней";
  }

  // Только те источники, у которых в этом городе и разделе есть строки. Чип
  // «Chợ Tốt» на странице Себу ничего не находит и читается как поломка, а не
  // как пустой фильтр. Если карты почему-то нет -- показываем всё, как раньше.
  function sourcesForCity(){
    var byKind = SOURCES_BY_CITY[state.city];
    var keys = byKind && byKind[state.kind];
    if (!keys || !keys.length) return SOURCES;
    return SOURCES.filter(function(s){ return keys.indexOf(s.key) !== -1; });
  }

  function renderSourceChips(){
    el.sourceChips.innerHTML = "";
    sourcesForCity().forEach(function(s){
      var b = document.createElement("button");
      b.type="button"; b.className="chip"; b.disabled = !s.active;
      b.innerHTML = '<span class="dot" style="background:'+s.color+'"></span>' + sourceLabel(s) + (s.active ? "" : " " + t("soon"));
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
    fillTypeChips(el.typeChips);
    if (el.mapTypeChips) fillTypeChips(el.mapTypeChips);
  }

  function fillTypeChips(box){
    box.innerHTML = "";
    var allBtn = document.createElement("button");
    allBtn.type="button"; allBtn.className="chip"; allBtn.textContent=t("all");
    allBtn.setAttribute("aria-pressed", state.type===null ? "true":"false");
    allBtn.addEventListener("click", function(){ state.type=null; renderTypeChips(); applyFilters(); });
    box.appendChild(allBtn);
    // Only the types belonging to the selected kind: showing "Warehouse" while
    // the user is browsing housing is noise, and vice versa.
    var typesForKind = state.kind === "commercial" ? COMMERCIAL_TYPES
                     : state.kind === "residential" ? RESIDENTIAL_TYPES
                     : TYPE_OPTIONS;
    // NB: the loop variable must not be named `t` -- that would shadow the
    // t() translation helper inside this closure.
    typesForKind.forEach(function(tp){
      var b = document.createElement("button");
      b.type="button"; b.className="chip"; b.textContent=typeName(tp);
      b.setAttribute("aria-pressed", state.type===tp ? "true":"false");
      b.addEventListener("click", function(){ state.type = (state.type===tp) ? null : tp; renderTypeChips(); applyFilters(); });
      box.appendChild(b);
    });
  }

  function setKind(kind){
    if (state.kind === kind) return;
    state.kind = kind;
    // A type from the other kind would silently match nothing.
    if (state.type && kindOf({type: state.type}) !== kind) state.type = null;
    BUDGET_MAX = (kind === "commercial") ? BUDGET_MAX_COMMERCIAL : BUDGET_MAX_RESIDENTIAL;
    // Any ceiling-relative budget must be reinterpreted against the new range,
    // otherwise "up to 45" silently becomes a hard filter on a 300-wide scale.
    state.minBudget = null; state.maxBudget = null;
    var tg = document.getElementById("kind-toggle");
    if (tg){
      Array.prototype.forEach.call(tg.querySelectorAll("button"), function(b){
        b.classList.toggle("active", b.getAttribute("data-kind") === kind);
      });
    }
    syncBudgetUI(); renderBudgetChips(); renderSourceChips(); renderTypeChips(); renderComplexFilter(); applyFilters();
  }

  var kindToggleEl = document.getElementById("kind-toggle");
  if (kindToggleEl){
    kindToggleEl.addEventListener("click", function(e){
      var btn = e.target.closest("button[data-kind]");
      if (!btn) return;
      var kind = btn.getAttribute("data-kind");
      // Per-city pages hold one kind each: the other kind is a sibling page.
      if (PAGE){ if (kind !== PAGE.kind) location.href = pageHref(PAGE.city, kind); return; }
      setKind(kind);
    });
  }

  el.sortToggle.addEventListener("click", function(e){
    var btn = e.target.closest("button[data-sort]");
    if (!btn) return;
    state.sort = btn.getAttribute("data-sort");
    Array.prototype.forEach.call(el.sortToggle.querySelectorAll("button"), function(b){ b.classList.toggle("active", b===btn); });
    applyFilters();
  });

  el.perM2Toggle.addEventListener("change", function(){
    state.perM2 = el.perM2Toggle.checked;
    applyFilters();
  });

  el.poiSortSelect.addEventListener("change", function(){
    state.poiSort = el.poiSortSelect.value;
    applyFilters();
  });

  el.complexSelect.addEventListener("change", function(){
    state.complex = el.complexSelect.value || null;
    applyFilters();
  });

  function detailsHtml(l){
    if (!l.details) return "";
    var rows = DETAIL_ORDER.filter(function(k){ return l.details[k]; }).map(function(k){
      // Пометка -- единственная подробность с переводом. Панель печатала поле как
      // есть, и в английском режиме под подписью «Important» стоял русский текст,
      // хотя noticeEn есть у всех 4416 строк с пометкой (найдено 16.09.2026).
      var v = (k === "notice") ? noticeText(l.details) : l.details[k];
      return '<div class="details-row"><dt>' + t("detailLabels")[k] + '</dt><dd>' + v + '</dd></div>';
    }).join("");
    var open = state.openDetails.has(l.id);
    return '<button class="details-toggle" type="button" data-details-for="'+l.id+'" aria-expanded="'+open+'">' + t("detailsToggle") + ' <span class="arrow">▾</span></button>' +
      '<dl class="details-panel"' + (open ? "" : " hidden") + ' id="details-'+l.id+'">' + rows + '</dl>';
  }

  function applyFilters(){
    var city = CITIES[state.city];
    var list = LISTINGS.filter(function(l){
      if (l.city !== state.city) return false;
      if (l.details && l.details.duplicateOf) return false;
      if (!state.sources.has(l.source)) return false;
      if (state.district && l.district !== state.district) return false;
      if (state.complex && l.complex !== state.complex) return false;
      // pv -- цена, приведённая к базовой валюте на сборке. Сравнивать
      // 45 000 песо с 7 500 000 донгов напрямую нельзя.
      var pvv = (l.pv == null ? l.price : l.pv);
      if (state.minBudget !== null && pvv < state.minBudget*1000000) return false;
      if (state.maxBudget !== null && pvv > state.maxBudget*1000000) return false;
      if (l.daysAgo > state.maxDays) return false;
      if (state.kind && kindOf(l) !== state.kind) return false;
      if (state.type && l.type !== state.type) return false;
      if (state.textSearch && listingSearchText(l).indexOf(state.textSearch) === -1) return false;
      if (state.showFavoritesOnly && !favorites.has(l.id)) return false;
      return true;
    });
    if (state.poiSort){
      list.forEach(function(l){ l._poiDist = nearestPoiKm(l, state.poiSort); });
      list.sort(function(a,b){
        if (a._poiDist===null && b._poiDist===null) return 0;
        if (a._poiDist===null) return 1;
        if (b._poiDist===null) return -1;
        return a._poiDist - b._poiDist;
      });
    } else if (state.perM2 && state.sort !== "new"){
      list.forEach(function(l){ l._perM2 = pricePerM2(l); });
      list.sort(function(a,b){
        if (a._perM2===null && b._perM2===null) return 0;
        if (a._perM2===null) return 1;
        if (b._perM2===null) return -1;
        return state.sort==="asc" ? a._perM2-b._perM2 : b._perM2-a._perM2;
      });
    } else {
      list.sort(function(a,b){
        if (a.price===null && b.price===null) return 0;
        if (a.price===null) return 1;
        if (b.price===null) return -1;
        var ap = (a.pv == null ? a.price : a.pv), bp = (b.pv == null ? b.price : b.pv);
        if (state.sort==="new") return a.daysAgo-b.daysAgo || ap-bp;
        return state.sort==="asc" ? ap-bp : bp-ap;
      });
    }

    el.resultsCount.textContent = list.length + " " + declineObjav(list.length);
    if (el.mapFilterCount) el.mapFilterCount.textContent = el.resultsCount.textContent;
    var distLabel = state.district ? districtByKey(state.city, state.district).name : t("anyDistrict");
    var budgetLabel;
    if (state.minBudget===null && state.maxBudget===null) budgetLabel = t("anyBudget");
    else if (state.minBudget===null) budgetLabel = t("upTo") + " " + fmtPrice(state.maxBudget*1000000) + " " + t("perMonth");
    else if (state.maxBudget===null) budgetLabel = t("from") + " " + fmtPrice(state.minBudget*1000000) + " " + t("perMonth");
    else budgetLabel = t("from") + " " + fmtPrice(state.minBudget*1000000) + " " + t("to") + " " + fmtPrice(state.maxBudget*1000000) + " " + t("perMonth");
    var typeLabel = state.type ? typeName(state.type).toLowerCase() : t("anyType");
    var searchLabel = state.textSearch ? (' · ' + t("searchCtx") + ': "' + state.textSearch + '"') : "";
    var complexLabel = state.complex ? (" · " + t("complexCtx") + " " + state.complex) : "";
    el.resultsContext.textContent = cityName(city) + " · " + distLabel + complexLabel + " · " + typeLabel + " · " + budgetLabel + " · " + t("forDays") + " " + state.maxDays + " " + dayWord(state.maxDays) + searchLabel;

    el.resultsList.innerHTML = "";
    el.emptyState.hidden = list.length !== 0;

    list.forEach(function(l){
      var d = districtByKey(l.city, l.district);
      var src = SOURCE_LABEL[l.source];
      var card = document.createElement("article");
      card.className = "listing-card";
      var noticeHtml = (l.details && l.details.notice && l.details.notice.indexOf("⚠")===0)
        ? '<p class="listing-notice">' + noticeText(l.details) + '</p>' : "";
      var photos = l.details && l.details.photos;
      var photoHtml = (photos && photos.length)
        ? '<div class="listing-photos">' + photos.map(function(p, i){
            return '<img class="listing-photo" data-idx="' + i + '" src="' + p + '" alt="" loading="lazy" onerror="this.remove()">';
          }).join('') + '</div>'
        : "";
      var alsoOn = l.details && l.details.alsoOn;
      var alsoOnHtml = (alsoOn && alsoOn.length)
        ? '<p class="listing-also">' + t("alsoOn") + ' ' + alsoOn.map(function(a){
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
            ' ' + t("wasPrice") + ' ' + fmtPrice(prevPrice) + ' ₫</span>';
        }
      }
      var perM2Val = pricePerM2(l);
      var perM2Html = perM2Val ? ('<span class="price-per-m2">' + fmtPricePerM2(perM2Val) + '</span>') : "";
      card.innerHTML =
        photoHtml +
        '<div class="listing-top">' +
          '<span class="source-pill"><i style="background:'+src.color+'"></i>' + src.short + '</span>' +
          '<span class="listing-top-right">' +
            '<span class="posted">' + postedText(l) + '</span>' +
            '<button class="fav-btn" type="button" data-fav-id="' + l.id + '" aria-label="' + t("addFav") + '" aria-pressed="' + favorites.has(l.id) + '">' + (favorites.has(l.id) ? "★" : "☆") + '</button>' +
          '</span>' +
        '</div>' +
        '<div>' +
          '<div class="listing-type">' + typeName(l.type) + '</div>' +
          '<div class="listing-meta">' + d.name + (l.area ? (" · " + l.area + " " + t("m2")) : "") +
            (state.poiSort && l._poiDist!=null ? (' · <span class="poi-dist-badge">' + POI_STYLE[state.poiSort].icon + " " + fmtDist(l._poiDist) + '</span>') : "") +
            (l.complex ? ('<br><span class="complex-pill">🏢 ' + l.complex + '</span>') : "") +
          '</div>' +
        '</div>' +
        '<p class="listing-desc">' + descText(l) + '</p>' +
        noticeHtml +
        alsoOnHtml +
        detailsHtml(l) +
        '<div class="listing-bottom">' +
          '<span><span class="price">' + (l.price===null ? t("priceOnRequest") : (fmtMoney(l.price, curOf(l)) + ' <small>' + t("perMonth") + '</small>')) + '</span>'
          + (l.price===null ? '' : '<span class="price-conv" title="' + t("ratesOn") + ' ' + (RATES ? RATES.date : "") + '">≈ ' + convLine(l.price, curOf(l)) + '</span>') + perM2Html + priceChangeHtml + '</span>' +
          '<a class="open-link" href="' + l.url + '" target="_blank" rel="noopener">' + t("openListing") + '</a>' +
        '</div>';
      var favBtn = card.querySelector(".fav-btn");
      favBtn.addEventListener("click", function(){
        toggleFavorite(l.id);
        var isFav = favorites.has(l.id);
        favBtn.setAttribute("aria-pressed", isFav);
        favBtn.textContent = isFav ? "★" : "☆";
        if (state.showFavoritesOnly && !isFav) applyFilters();
      });
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
    if (lang === "en") return n === 1 ? "listing" : "listings";
    var mod10 = n%10, mod100 = n%100;
    if (mod10===1 && mod100!==11) return "объявление";
    if ([2,3,4].indexOf(mod10)!==-1 && (mod100<10 || mod100>=20)) return "объявления";
    return "объявлений";
  }

  el.resetBtn.addEventListener("click", function(){
    state.district = null; state.complex=null; state.minBudget=null; state.maxBudget=null; state.maxDays=7; state.sort="asc"; state.type=null; state.poiSort=""; state.textSearch=""; state.showFavoritesOnly=false; state.perM2=false
    // Reset returns to housing, so the budget ceiling must come back with it --
    // otherwise the slider keeps the 300M commercial scale on residential data.
    // On a per-city page the kind is the page itself and stays.
    state.kind = PAGE ? PAGE.kind : "residential";
    BUDGET_MAX = (state.kind === "commercial") ? BUDGET_MAX_COMMERCIAL : BUDGET_MAX_RESIDENTIAL;
    var kt = document.getElementById("kind-toggle");
    if (kt){ Array.prototype.forEach.call(kt.querySelectorAll("button"), function(b){
      b.classList.toggle("active", b.getAttribute("data-kind")===state.kind); }); }
    state.sources = new Set(SOURCES.filter(function(s){ return s.active; }).map(function(s){ return s.key; }));
    el.districtInput.value=""; el.poiSortSelect.value=""; el.textSearchInput.value=""; el.perM2Toggle.checked=false;
    el.favFilterToggle.setAttribute("aria-pressed","false"); el.favFilterToggle.textContent="☆ " + t("favFilter");
    Array.prototype.forEach.call(el.sortToggle.querySelectorAll("button"), function(b){ b.classList.toggle("active", b.getAttribute("data-sort")==="asc"); });
    syncBudgetUI(); renderBudgetChips(); renderDaysChips(); renderSourceChips(); renderTypeChips(); renderComplexFilter(); renderCityMap(); applyFilters();
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

  var copyAddrBtn = document.getElementById("copy-addr");
  if (copyAddrBtn){
    copyAddrBtn.addEventListener("click", function(){
      var addr = document.getElementById("usdt-addr").textContent.trim();
      var done = function(){
        copyAddrBtn.textContent = t("copied");
        setTimeout(function(){ copyAddrBtn.textContent = t("copy"); }, 1800);
      };
      // Copying a wallet address must never silently no-op. If the clipboard
      // API is unavailable, or its promise is rejected -- no user gesture,
      // permission denied, sandboxed frame -- fall back to execCommand, and
      // if that fails too, select the address so it can be copied by hand.
      var legacyCopy = function(){
        var ta = document.createElement("textarea");
        ta.value = addr; ta.setAttribute("readonly", "");
        ta.style.position = "fixed"; ta.style.opacity = "0";
        document.body.appendChild(ta); ta.select();
        var ok = false;
        try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
        document.body.removeChild(ta);
        if (ok) { done(); return; }
        var node = document.getElementById("usdt-addr");
        var sel = window.getSelection(), range = document.createRange();
        range.selectNodeContents(node); sel.removeAllRanges(); sel.addRange(range);
        copyAddrBtn.textContent = t("selected");
        setTimeout(function(){ copyAddrBtn.textContent = t("copy"); }, 2600);
      };
      if (navigator.clipboard && window.isSecureContext){
        navigator.clipboard.writeText(addr).then(done, legacyCopy);
      } else {
        legacyCopy();
      }
    });
  }

  if (PAGE && PAGE.kind === "commercial"){
    // A commercial page starts on the commercial budget scale and with the
    // toggle showing which page this is; setKind() is never called here.
    BUDGET_MAX = BUDGET_MAX_COMMERCIAL;
    if (kindToggleEl){ Array.prototype.forEach.call(kindToggleEl.querySelectorAll("button"), function(b){
      b.classList.toggle("active", b.getAttribute("data-kind") === "commercial"); }); }
  }
  initTheme();
  initLeafletMap();
  renderCityTabs(); renderCityMap(); updatePoiSortAvailability(); setupBudgetSlider(); renderBudgetChips(); renderDaysChips(); renderSourceChips(); renderTypeChips(); renderComplexFilter(); applyFilters();
  initLang();
})();
</script>
"""

def check_js_undefined_calls(html):
    """
    Cheap static guard against the exact bug class found 25 Aug 2026: a
    concurrent session's merge/stash resolution silently reintroduced a
    call to a function (renderFbGroups) that had been deleted, breaking
    city switching in production with no build-time signal. Not a real
    JS parser -- just flags bare `name(` call sites (dot-prefixed method
    calls like `.forEach(` are excluded via the lookbehind) that match
    neither a local function declaration nor a known browser/JS global.
    Heuristic and non-fatal by design: prints a warning to check by eye
    rather than failing the build on a false positive.
    """
    m = re.search(r'<script>\n\(function\(\)\{(.*?)\}\)\(\);\n</script>', html, re.S)
    if not m:
        print("WARNING: check_js_undefined_calls could not locate the main JS IIFE -- skipped")
        return
    js = m.group(1)
    # Blank out string literals AND comments before looking for call sites.
    # Prose in either ("Open listing", "maps (OpenStreetMap)", CSS "var(--x)",
    # a comment saying "over time (the daily checks...)") reads as `name(` to
    # the regex and produced a steady drip of false positives. A real call
    # site never lives inside a string or a comment, so dropping both removes
    # that whole class instead of accumulating per-word exceptions.
    js = re.sub(r'"(?:[^"\\\n]|\\.)*"', '""', js)
    js = re.sub(r"'(?:[^'\\\n]|\\.)*'", "''", js)
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.S)
    js = re.sub(r'//[^\n]*', '', js)
    declared = set(re.findall(r'\bfunction\s+([a-zA-Z_$][\w$]*)\s*\(', js))
    declared |= set(re.findall(r'\bvar\s+([a-zA-Z_$][\w$]*)\s*=\s*function\s*\(', js))
    known_globals = {
        "if", "for", "while", "switch", "catch", "function", "return", "typeof", "new", "in", "of",
        "instanceof", "else", "do", "void", "delete", "yield", "await",
        "document", "window", "console", "Array", "Object", "JSON", "Math", "Number", "String",
        "Boolean", "Set", "Map", "RegExp", "Promise", "Date", "Error", "Symbol",
        "parseInt", "parseFloat", "isNaN", "encodeURIComponent", "decodeURIComponent",
        "L", "fetch", "setTimeout", "setInterval", "clearTimeout", "clearInterval",
        "requestAnimationFrame", "alert", "confirm", "prompt", "localStorage", "sessionStorage",
        "ResizeObserver",
    }
    calls = set(re.findall(r'(?<![\w.$])([a-zA-Z_$][\w$]*)\s*\(', js))
    suspicious = sorted(calls - declared - known_globals)
    if suspicious:
        print("WARNING: possibly-undefined JS function calls, verify before shipping:", ", ".join(suspicious))
    else:
        print("JS undefined-call check: OK")

def check_listing_types(html, listings):
    """
    Fail the build on a listing whose type is not one the UI actually offers.

    Found 31 Aug 2026: 29 HCMC listings carried types like "2-спальная
    квартира", invented by a daily-check session. Nothing looked broken --
    the cards rendered normally -- but the type filter compares strictly
    (l.type !== state.type) and the UI draws one chip per allowed type, so
    those listings were unreachable for anyone who narrowed by type, and
    typeName() had no English form for them, so the English page showed the
    type in Russian. Silent by construction: the failure is visible only to
    a user who filters, never to whoever added the data.

    The allowed set is parsed out of the page's own JS instead of being
    duplicated here, so this check cannot drift from what the UI offers.

    Fatal on purpose. A warning would be ignored by the next automated
    session exactly as the previous one ignored the convention.
    """
    allowed = set()
    for name in ("RESIDENTIAL_TYPES", "COMMERCIAL_TYPES"):
        m = re.search(r"var\s+" + name + r"\s*=\s*\[(.*?)\];", html, re.S)
        if not m:
            raise SystemExit(
                "check_listing_types: could not find " + name + " in the page JS.\n"
                "The guard cannot verify listing types against a list it cannot\n"
                "read. Fix the parse rather than deleting the check."
            )
        allowed |= set(re.findall(r'"([^"]*)"', m.group(1)))

    first_id = {}
    for l in listings:
        if l["type"] not in allowed and l["type"] not in first_id:
            first_id[l["type"]] = l["id"]
    if first_id:
        offenders = "; ".join(
            '"' + t + '" (e.g. id ' + str(i) + ')' for t, i in sorted(first_id.items())
        )
        raise SystemExit(
            "Listing types the UI does not offer: " + offenders + "\n"
            "These listings render fine but are unreachable through the type\n"
            "filter, and have no English type name.\n"
            "Allowed: " + ", ".join(sorted(allowed)) + "\n"
            "Either use one of those, or add the new type to RESIDENTIAL_TYPES or\n"
            "COMMERCIAL_TYPES and to TYPE_EN in the page JS so the UI can show it."
        )
    print("Listing-type check: OK (" + str(len(allowed)) + " allowed types)")

check_listing_types(HTML, LISTINGS)


def _ru_days_label(n):
    """Метка «N дней назад». Одна на всех: её берут listing_lock.with_current_age
    (возраст строк на сегодня при сборке) и сборщики -- через template_function."""
    if n <= 0:
        return "сегодня"
    if n == 1:
        return "вчера"
    a = abs(n)
    word = "день" if (a % 10 == 1 and a % 100 != 11) else ("дня" if (2 <= a % 10 <= 4 and not 12 <= a % 100 <= 14) else "дней")
    return "%d %s назад" % (n, word)


_SOURCE_KEYS = {s["key"] for s in SOURCES}


def check_listings(listings, cities):
    """
    Fail the build on data that renders fine but is wrong -- invariants that
    until 2 Sep 2026 held only by convention (audit, MEDIUM: "build guards
    check only the listing type"):

      * ids unique -- every state file (posted_to_telegram.json,
        posted_dates.json, users' favourites) is keyed by id;
      * district exists for the city -- a bad key gives an empty district
        line on the card, no map pin, and the listing is unreachable by the
        district filter, all silently;
      * descEn present -- the EN page falls back to Russian without a word;
      * noticeEn present whenever there is a notice -- same silent fallback;
      * `posted` label agrees with `daysAgo` -- the RU page shows the label,
        the EN page computes from the number, so they disagreed for 24 rows.

    URL uniqueness is reported, not fatal: 39 legacy duplicate pairs are a
    known debt, and Telegram-sourced listings share a channel URL by design.

    Fatal on purpose, same reasoning as check_listing_types above.
    """
    valid = {(c, d["key"]) for c, cv in cities.items() for d in cv["districts"]}
    errors = []
    seen = set()
    for l in listings:
        i = l["id"]
        if i in seen:
            errors.append("duplicate id %s" % i)
        seen.add(i)
        if (l["city"], l["district"]) not in valid:
            errors.append("id %s: district %r is not defined for city %r" % (i, l["district"], l["city"]))
        if not l.get("descEn"):
            errors.append("id %s: no descEn (the EN page would silently show Russian)" % i)
        d = l.get("details") or {}
        if d.get("notice") and not d.get("noticeEn"):
            errors.append("id %s: notice without noticeEn" % i)
        # Источник обязан быть в SOURCES. Фильтр на странице стартует со списка
        # активных источников, поэтому объявление с незнакомым source просто
        # исчезает из выдачи -- при том что счётчик в заголовке считается здесь,
        # на Python, и продолжает его учитывать. Ровно это и случилось с первыми
        # восемнадцатью объявлениями Думагете 4 сентября 2026: страница написала
        # "17 объявлений" и не показала ни одного.
        if l.get("cur", "VND") not in _PER_USD:
            errors.append("id %s: unknown currency %r -- add it to rates.json "
                          "(known: %s)" % (i, l.get("cur"), ", ".join(sorted(_PER_USD))))
        if l.get("source") not in _SOURCE_KEYS:
            errors.append("id %s: unknown source %r -- add it to SOURCES or the "
                          "listing renders nowhere (allowed: %s)"
                          % (i, l.get("source"), ", ".join(sorted(_SOURCE_KEYS))))
        if isinstance(l.get("daysAgo"), int) and l.get("posted") != _ru_days_label(l["daysAgo"]):
            errors.append("id %s: posted label %r does not match daysAgo=%s (expected %r) -- run purge_old_listings.py"
                          % (i, l.get("posted"), l["daysAgo"], _ru_days_label(l["daysAgo"])))
    if errors:
        raise SystemExit("check_listings: %d problem(s), nothing written:\n  " % len(errors)
                         + "\n  ".join(errors[:40]) + ("\n  ... (%d more)" % (len(errors) - 40) if len(errors) > 40 else ""))
    by_url = {}
    for l in listings:
        by_url.setdefault(l["url"], []).append(l["id"])
    shared = sum(1 for ids in by_url.values() if len(ids) > 1)
    print("Listing check: OK (%d listings, %d URLs shared by several listings -- legacy duplicates / Telegram channel links)"
          % (len(listings), shared))


check_listings(LISTINGS, CITIES)

check_js_undefined_calls(HTML)

TEMPLATE_HTML = HTML      # the template with placeholders intact -- the per-city build below needs it
HTML = HTML.replace("__DATA_JSON__", DATA_JSON)
del DATA_JSON             # дальше не нужен; см. «ПАМЯТЬ» ниже, у записи полной страницы
# __LISTING_COUNT__ is deliberately NOT substituted here -- finalise() below
# matches the RU meta descriptions verbatim to swap in English ones, so the
# placeholder must survive until then. finalise() does the substitution.
# Стиль Leaflet встраивается, а не подключается ссылкой. Причина -- Артефакт:
# его политика безопасности пускает скрипты только с нескольких CDN (cdnjs в их
# числе, unpkg -- нет), а ВНЕШНИЕ СТИЛИ не пускает ниоткуда, кроме шрифтов Google.
# Пока обе части Leaflet грузились с unpkg, в Артефакте не загружалась ни одна, и
# карта была пустым местом. Файл лежит в vendor/ и совпадает по sha256 с тем, что
# отдаёт cdnjs. Ссылки на картинки внутри (marker-icon, layers) остаются, но не
# запрашиваются: сайт рисует кружки и полигоны, а не стандартные маркеры и не
# переключатель слоёв.
import os.path as _osp                      # _os появляется ниже, здесь его ещё нет
_LEAFLET_CSS = open(_osp.join(W, "vendor", "leaflet-1.9.4.css"), encoding="utf-8").read()
HTML = HTML.replace("__LEAFLET_CSS__", "<style>\n" + _LEAFLET_CSS + "\n</style>")
HTML = HTML.replace("__TODAY_DATE__", ru_today_stamp())
HTML = HTML.replace("__TODAY_DATE_EN__", en_today_stamp())
HTML = HTML.replace("__USDT_ADDR__", USDT_TRC20_ADDRESS)
HTML = HTML.replace("__USDT_QR__", USDT_QR_SVG)

SITE_ROOT = "https://tottorisun.github.io/RentSearcherViet/"
# The all-in-one English page. en.html itself is the English LANDING since the
# multi-page build (2 Sep 2026), mirroring index.html.
EN_PATH = "vietnam-rent-finder-en.html"

# Two real pages, one per language. A single page cannot rank for both
# languages: crawlers read the STATIC title/description/lang, and the
# in-page RU/EN switch is JS-only so they never see the other language.
# Each page therefore ships its own meta and its own DEFAULT_LANG, and
# both carry hreflang so search engines treat them as translations of
# one another rather than duplicates.
EN_TITLE = "Rental housing in Vietnam and the Philippines — Ho Chi Minh City, Hanoi, Cebu, Manila"
EN_DESC = ("Over __LISTING_COUNT__ rental listings across Vietnam (Ho Chi Minh City, Hanoi, Da Nang, "
           "Nha Trang, Da Lat, Hoi An, Vung Tau, Quy Nhon, Phan Thiet), gathered from Cho Tot, Batdongsan and "
           "other sources in one place — with photos, a map and filters.")
EN_DESC_SHORT = ("Over __LISTING_COUNT__ rental listings across Vietnam and the Philippines, gathered from several "
                 "marketplaces in one place — with photos, a map and filters.")

HREFLANG = (
    '<link rel="alternate" hreflang="ru" href="' + SITE_ROOT + '">\n'
    '<link rel="alternate" hreflang="en" href="' + SITE_ROOT + EN_PATH + '">\n'
    '<link rel="alternate" hreflang="x-default" href="' + SITE_ROOT + '">\n'
)


def finalise(html, lang):
    """Bake the per-language head + DEFAULT_LANG into one page."""
    html = html.replace('<meta charset="utf-8">',
                        '<meta charset="utf-8">\n' + HREFLANG, 1)
    html = html.replace("__DEFAULT_LANG__", lang)
    if lang == "en":
        html = html.replace(
            "<title>Жильё во Вьетнаме и на Филиппинах — Хошимин · Ханой · Себу · Манила</title>",
            "<title>" + EN_TITLE + "</title>", 1)
        html = html.replace(
            'content="Более __LISTING_COUNT__ объявлений об аренде жилья во Вьетнаме (Хошимин, Ханой, Дананг, Нячанг, Далат, Хойан, Вунгтау, Куинён, Фантьет), собранных с Chợ Tốt, Batdongsan, Facebook и других источников в одном месте — с фото, картой и фильтрами."',
            'content="' + EN_DESC + '"', 1)
        html = html.replace(
            'content="Жильё во Вьетнаме и на Филиппинах — Хошимин · Ханой · Себу · Манила"',
            'content="' + EN_TITLE + '"')
        html = html.replace(
            'content="Более __LISTING_COUNT__ объявлений об аренде жилья во Вьетнаме и на Филиппинах, собранных с разных площадок в одном месте — с фото, картой и фильтрами."',
            'content="' + EN_DESC_SHORT + '"', 1)
        html = html.replace(
            'content="Более __LISTING_COUNT__ объявлений об аренде жилья во Вьетнаме и на Филиппинах, собранных с разных площадок в одном месте."',
            'content="' + EN_DESC_SHORT + '"', 1)
        html = html.replace('<meta property="og:url" content="' + SITE_ROOT + '">',
                            '<meta property="og:url" content="' + SITE_ROOT + EN_PATH + '">', 1)
        html = html.replace('<link rel="canonical" href="' + SITE_ROOT + '">',
                            '<link rel="canonical" href="' + SITE_ROOT + EN_PATH + '">', 1)
    html = html.replace("__LISTING_COUNT__", str(len(LISTINGS)))
    return html


def _write_atomic(path, text):
    """Write through a temp file and rename, so a concurrent reader of the
    built HTML (build_pins_step2_geocode.py, build_leaflet_data.py,
    cleanup_telegram_posts.py, post_new_to_telegram.py -- all of which
    re.search `var DATA` and crash on a half-written file) sees either the
    old page or the new one, never a torn one. The PostToolUse hook rebuilds
    on every edit, so two sessions really do overlap here (2 Sep audit)."""
    import os
    tmp = "%s.tmp.%d" % (path, os.getpid())
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)


# The all-in-one pages. vietnam-rent-finder.html is what every pipeline script
# reads the complete DATA out of (site_data.load_data) and what the Artifact
# copy is; keep writing it first, before anything below can fail.
#
# ПАМЯТЬ. Полная страница -- семь миллионов символов, и в ней есть эмодзи, поэтому
# Python хранит её по 4 байта на символ: ~30 МБ на копию. Раньше общий HTML и обе
# языковые копии жили до конца сборки, ~90 МБ поверх постраничной части. У службы
# на сервере предел MemoryHigh=300M, и 19-21.09 все прогоны упирались в него ровно
# (300.0-300.2 МБ при 6200-6600 строках). Теперь копия пишется и сразу отпускается.
RU_HTML = finalise(HTML, "ru")
_write_atomic(W + "/vietnam-rent-finder.html", RU_HTML)
_RU_SIZE = len(RU_HTML)
del RU_HTML
EN_HTML = finalise(HTML, "en")
_write_atomic(W + "/" + EN_PATH, EN_HTML)
del EN_HTML, HTML
print("Wrote vietnam-rent-finder.html (ru) and " + EN_PATH + " (en), size", _RU_SIZE)


# ================== MULTI-PAGE BUILD (2 Sep 2026) ==================
# Why: the all-in-one page carries every listing inline -- 3.2 MB, 1 MB
# gzipped, parsed on every open, on a phone too. Each city now also gets a
# page per kind (nha-trang.html / nha-trang-commercial.html, ...) that shares
# one CSS and one JS file (cached after the first page) and inlines only its
# own slice of DATA; index.html is a light landing that links to them. The JS
# is the same file in both modes -- see the PAGE comment at the top of the
# script block: on a per-city page the city tabs and the kind toggle are
# links to sibling pages, everything else works on the slice it was given.
import hashlib as _hashlib
import os as _os
_os.makedirs(W + "/assets", exist_ok=True)


def _fill_common(tpl):
    return (tpl.replace("__TODAY_DATE__", ru_today_stamp()).replace("__TODAY_DATE_EN__", en_today_stamp())
               .replace("__USDT_ADDR__", USDT_TRC20_ADDRESS).replace("__USDT_QR__", USDT_QR_SVG))


_TPL = _fill_common(TEMPLATE_HTML)
_css_m = re.search(r"<style>\n(.*?)\n</style>", _TPL, re.S)
_js_m = re.search(r"<script>\n(\(function\(\)\{.*?\}\)\(\);)\n</script>", _TPL, re.S)
if not _css_m or not _js_m:
    raise SystemExit("multi-page build: could not locate the <style> or the app <script> block in the template")
# Стиль Leaflet едет и сюда: постраничные города берут его из assets/app.css
# (свой источник, ограничения Артефакта на них не распространяются). Без этой
# строки карта на них осталась бы вовсе без стилей -- поймано сразу после
# перевода полной страницы на встроенный стиль.
APP_CSS = _LEAFLET_CSS + "\n" + _css_m.group(1)
APP_JS = _js_m.group(1).replace("__DATA_JSON__", "null").replace('"__DEFAULT_LANG__"', '"ru"')
_write_atomic(W + "/assets/app.css", APP_CSS)
_write_atomic(W + "/assets/app.js", APP_JS)

# Ссылки на ассеты версионируются содержимым. Без этого правка в app.js не
# доходит до вернувшегося посетителя: браузер держит старую копию, а адрес не
# меняется. Поймано 9 сентября 2026 -- новая легенда карты уже лежала на
# сервере, а страница показывала прежнюю, потому что словарь переводов живёт
# в закэшированном app.js.
_ASSET_V = {
    "css": _hashlib.sha256(APP_CSS.encode("utf-8")).hexdigest()[:8],
    "js": _hashlib.sha256(APP_JS.encode("utf-8")).hexdigest()[:8],
}

# Page shell: the same markup with styles and script linked, and a hook for
# the page's own data script right before the app.
PAGE_SHELL = _TPL.replace(_css_m.group(0), '<link rel="stylesheet" href="assets/app.css?v=' + _ASSET_V["css"] + '">', 1)
# Плейсхолдер подставляется только в полной странице; здесь он лишний и без
# этой строки уезжал в разметку города видимым текстом.
PAGE_SHELL = PAGE_SHELL.replace("__LEAFLET_CSS__\n", "").replace("__LEAFLET_CSS__", "")
PAGE_SHELL = PAGE_SHELL.replace(
    _js_m.group(0),
    '__PAGE_DATA_SCRIPT__\n<script src="assets/app.js?v=' + _ASSET_V["js"] + '"></script>', 1)
if "__PAGE_DATA_SCRIPT__" not in PAGE_SHELL or "__DATA_JSON__" in PAGE_SHELL:
    raise SystemExit("multi-page build: page shell assembly went wrong")

COMMERCIAL_TYPES_PY = ("Офис", "Торговая площадь", "Склад")   # mirrors COMMERCIAL_TYPES in the JS


def _kind(l):
    return "commercial" if l["type"] in COMMERCIAL_TYPES_PY else "residential"


def _hidden(l):
    """Строка помечена как дубль другой: в списке, на карте и в счётчиках её нет.
    Считать её значит обещать в заголовке объявления, которых пользователь не
    увидит -- ровно так однажды страница Думагете обещала 17 и показывала ноль."""
    return bool((l.get("details") or {}).get("duplicateOf"))


COUNTS = {}
for _l in LISTINGS:
    if _hidden(_l):
        continue
    COUNTS.setdefault(_l["city"], {"residential": 0, "commercial": 0})[_kind(_l)] += 1


def ru_ads(n):
    if 11 <= n % 100 <= 14:
        return "%d объявлений" % n
    if n % 10 == 1:
        return "%d объявление" % n
    if n % 10 in (2, 3, 4):
        return "%d объявления" % n
    return "%d объявлений" % n


RU_TITLE_FULL = "Жильё во Вьетнаме и на Филиппинах — Хошимин · Ханой · Себу · Манила"
RU_DESC_LONG = ("Более __LISTING_COUNT__ объявлений об аренде жилья во Вьетнаме (Хошимин, Ханой, Дананг, Нячанг, Далат, "
                "Хойан, Вунгтау, Куинён, Фантьет), собранных с Chợ Tốt, Batdongsan, Facebook и других источников в одном "
                "месте — с фото, картой и фильтрами.")
RU_DESC_OG = "Более __LISTING_COUNT__ объявлений об аренде жилья во Вьетнаме и на Филиппинах, собранных с разных площадок в одном месте — с фото, картой и фильтрами."
RU_DESC_TW = "Более __LISTING_COUNT__ объявлений об аренде жилья во Вьетнаме и на Филиппинах, собранных с разных площадок в одном месте."


def page_name(city, kind):
    return city + ("-commercial" if kind == "commercial" else "") + ".html"


def city_page(city, kind):
    c = CITIES[city]
    rows = [l for l in LISTINGS if l["city"] == city and _kind(l) == kind and not _hidden(l)]
    n = len(rows)
    data = {"CITIES": CITIES, "SOURCES": SOURCES, "RATES": _RATES_PUBLIC,
            "SOURCES_BY_CITY": _SOURCES_BY_CITY, "LISTINGS": rows, "COUNTS": COUNTS,
            "WARD_BOUNDARIES": ({city: WARD_BOUNDARIES[city]} if city in WARD_BOUNDARIES else {}),
            "POIS": ({city: POIS[city]} if city in POIS else {}), "NOTICES": _NOTICES}
    if kind == "commercial":
        title = "Коммерческая аренда: %s — %s" % (c["name"], ru_ads(n))
        desc = ("Офисы, торговые площади и склады в аренду: %s. %s с Chợ Tốt, Batdongsan и других площадок — "
                "с фото, картой и фильтрами." % (c["name"], ru_ads(n)))
    else:
        title = "Аренда жилья: %s — %s" % (c["name"], ru_ads(n))
        desc = ("Комнаты, студии, квартиры и дома в аренду: %s. %s с Chợ Tốt, Batdongsan, Facebook и Telegram — "
                "с фото, картой и фильтрами." % (c["name"], ru_ads(n)))
    fname = page_name(city, kind)
    url = SITE_ROOT + fname
    html = PAGE_SHELL
    html = html.replace("<title>" + RU_TITLE_FULL + "</title>", "<title>" + title + "</title>", 1)
    html = html.replace('content="' + RU_TITLE_FULL + '"', 'content="' + title + '"')
    for old in (RU_DESC_LONG, RU_DESC_OG, RU_DESC_TW):
        html = html.replace(old, desc)
    html = html.replace('<meta property="og:url" content="' + SITE_ROOT + '">',
                        '<meta property="og:url" content="' + url + '">', 1)
    html = html.replace('<link rel="canonical" href="' + SITE_ROOT + '">',
                        '<link rel="canonical" href="' + url + '">', 1)
    page_script = ('<script>window.PAGE_DATA=' + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
                   + ';window.PAGE_DEFAULT_LANG="ru";window.PAGE=' + json.dumps({"city": city, "kind": kind})
                   + ';</script>')
    html = html.replace("__PAGE_DATA_SCRIPT__", page_script, 1)
    html = html.replace("__DEFAULT_LANG__", "ru").replace("__LISTING_COUNT__", str(n))
    _write_atomic(W + "/" + fname, html)
    return fname, n


CITY_PAGES = []
for _city in CITIES:
    for _k in ("residential", "commercial"):
        CITY_PAGES.append(city_page(_city, _k))
print("Wrote %d per-city pages (assets/app.css %d KB, assets/app.js %d KB); largest page: %s"
      % (len(CITY_PAGES), len(APP_CSS) // 1024, len(APP_JS) // 1024,
         max(CITY_PAGES, key=lambda p: _os.path.getsize(W + "/" + p[0]))[0]))


def landing(lang):
    en = (lang == "en")
    COUNTRY_TITLE = {"vn": ("Вьетнам", "Vietnam"), "ph": ("Филиппины", "Philippines")}
    by_country, order = {}, []
    for key, c in CITIES.items():
        n_r = COUNTS.get(key, {}).get("residential", 0)
        n_c = COUNTS.get(key, {}).get("commercial", 0)
        name = c["nameEn"] if en else c["name"]
        res_label = ("%d residential" % n_r) if en else ru_ads(n_r) + " · жильё"
        com_label = ("%d commercial" % n_c) if en else ru_ads(n_c) + " · коммерция"
        card = ('<div class="lc">'
                  '<h2>' + name + '</h2>'
                  # Пустой раздел не должен выглядеть ссылкой. Для коммерции это
                  # было учтено с самого начала, для жилья -- нет, и 9 сентября 2026
                  # лендинг предлагал «0 объявлений · жильё →» у Фантьета и Фукуока:
                  # обещание вело на пустую страницу. Та же беда, что когда-то
                  # обещала 17 объявлений в Думагете и показывала ноль.
                  + ('<a class="lc-link" href="' + page_name(key, "residential") + '"><span>' + res_label + '</span><span>→</span></a>' if n_r else
                     '<span class="lc-link lc-none">' + ("no residential listings yet" if en else "жилья пока нет") + '</span>')
                  + ('<a class="lc-link lc-com" href="' + page_name(key, "commercial") + '"><span>' + com_label + '</span><span>→</span></a>' if n_c else
                     '<span class="lc-link lc-none">' + ("no commercial listings yet" if en else "коммерции пока нет") + '</span>')
                  + '</div>')
        cc = c.get("country", "vn")
        if cc not in by_country:
            by_country[cc] = []
            order.append(cc)
        by_country[cc].append(card)
    # одна секция на страну, каждая со своим заголовком
    cards = ""
    for cc in order:
        cc_title = COUNTRY_TITLE.get(cc, (cc, cc))[1 if en else 0]
        cards += ('<h2 class="lgroup">' + cc_title + '</h2>'
                  '<section class="lgrid">' + "".join(by_country[cc]) + '</section>')
    total = len(LISTINGS)
    if en:
        title = "Rental housing in Vietnam and the Philippines — by city"
        desc = "Over %d rental listings across Vietnam, one page per city, residential and commercial apart: Ho Chi Minh City, Hanoi, Da Nang, Nha Trang, Da Lat, Vung Tau, Quy Nhon, Hoi An, Phan Thiet, Binh Duong, Phu Quoc." % total
        h1 = "Rental housing in Vietnam and the Philippines"
        tagline = "Pick a city: residential and commercial listings are separate pages, each loads only its own data."
        full_link = "All cities on one page"
        other = '<a href="./">Русская версия</a>'
        stamp = "Updated " + en_today_stamp()
    else:
        title = "Жильё во Вьетнаме и на Филиппинах — по городам"
        desc = "Более %d объявлений об аренде во Вьетнаме, отдельная страница на каждый город, жильё и коммерция врозь: Хошимин, Ханой, Дананг, Нячанг, Далат, Вунгтау, Куинён, Хойан, Фантьет, Биньзыонг, Фукуок." % total
        h1 = "Жильё во Вьетнаме и на Филиппинах"
        tagline = "Выберите город: жильё и коммерция — отдельные страницы, каждая грузит только свои объявления."
        full_link = "Все города на одной странице"
        other = '<a href="en.html">English</a>'
        stamp = "Обновлено " + ru_today_stamp()
    self_url = SITE_ROOT + ("en.html" if en else "")
    return ('<!doctype html>\n<html lang="' + lang + '">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>' + title + '</title>\n'
            '<meta name="description" content="' + desc + '">\n'
            '<link rel="canonical" href="' + self_url + '">\n'
            '<link rel="alternate" hreflang="ru" href="' + SITE_ROOT + '">\n'
            '<link rel="alternate" hreflang="en" href="' + SITE_ROOT + 'en.html">\n'
            '<link rel="alternate" hreflang="x-default" href="' + SITE_ROOT + '">\n'
            '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 100 100\'%3E%3Ctext y=\'.9em\' font-size=\'90\'%3E%F0%9F%8F%A0%3C/text%3E%3C/svg%3E">\n'
            '<link rel="stylesheet" href="assets/app.css?v=' + _ASSET_V["css"] + '">\n'
            '<style>\n'
            '.landing{max-width:1100px;margin:0 auto;padding:28px 18px 60px;}\n'
            '.landing .hero{margin-bottom:22px;}\n'
            '.lgrid{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));}\n'
            '.lgroup{margin:26px 0 10px;font-size:0.82rem;font-weight:700;letter-spacing:.05em;'
            'text-transform:uppercase;color:var(--ink-faint);}\n'
            '.lgroup:first-of-type{margin-top:6px;}\n'
            '.lc{background:var(--surface);border:1px solid var(--line-strong);border-radius:var(--radius-md);padding:16px 16px 12px;box-shadow:var(--shadow-md);}\n'
            '.lc h2{margin:0 0 10px;font-size:1.15rem;}\n'
            '.lc-link{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:10px 12px;margin-top:8px;border-radius:10px;background:var(--accent);color:var(--accent-ink);text-decoration:none;font-weight:700;font-size:0.95rem;min-height:40px;}\n'
            '.lc-link.lc-com{background:var(--surface-2);color:var(--ink);border:1px solid var(--line-strong);}\n'
            '.lc-none{background:transparent;border:1px dashed var(--line-strong);color:var(--ink-faint);font-weight:500;}\n'
            '.lfoot{margin-top:26px;color:var(--ink-dim);font-size:0.9rem;display:flex;flex-wrap:wrap;gap:10px 22px;}\n'
            '.lfoot a{color:var(--accent);}\n'
            '</style>\n</head>\n<body>\n'
            '<div class="page landing">\n'
            '<header class="hero"><div class="brand"><span class="brand-mark" aria-hidden="true">'
            '<svg viewBox="0 0 24 24" fill="none"><path d="M4 11.5 12 4l8 7.5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M6 10.5V19a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-8.5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 20v-5h4v5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            '</span><div><h1>' + h1 + '</h1><p class="tagline">' + tagline + '</p></div></div></header>\n'
            + cards + '\n'
            '<p class="lfoot"><a href="vietnam-rent-finder' + ("-en" if en else "") + '.html">' + full_link + ' →</a>'
            + other + '<span>' + stamp + '</span></p>\n'
            '</div>\n</body>\n</html>\n')


_write_atomic(W + "/index.html", landing("ru"))
_write_atomic(W + "/en.html", landing("en"))
print("Wrote index.html (ru landing) and en.html (en landing)")

with open(W + "/robots.txt", "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: " + SITE_ROOT + "sitemap.xml\n")
with open(W + "/sitemap.xml", "w", encoding="utf-8") as f:
    today = datetime.date.today().isoformat()
    urls = ""
    locs = [(SITE_ROOT, "1.0"), (SITE_ROOT + "en.html", "0.9"),
            (SITE_ROOT + "vietnam-rent-finder.html", "0.6"), (SITE_ROOT + EN_PATH, "0.5")]
    locs += [(SITE_ROOT + fname, "0.8" if n else "0.3") for fname, n in CITY_PAGES]
    for loc, prio in locs:
        urls += ('  <url>\n'
                 '    <loc>' + loc + '</loc>\n'
                 '    <lastmod>' + today + '</lastmod>\n'
                 '    <changefreq>daily</changefreq>\n'
                 '    <priority>' + prio + '</priority>\n'
                 '  </url>\n')
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + urls +
            '</urlset>\n')
print("Wrote robots.txt and sitemap.xml (%d URLs)" % len(locs))
