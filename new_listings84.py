# -*- coding: utf-8 -*-
# Daily 7-city check (non-HCMC): Nha Trang, Da Lat, Da Nang, Vung Tau, Quy Nhon.
# Note: this was originally written to new_listings83.py using ids 1981-2007,
# but a concurrent HCMC daily-check session overwrote that filename with its
# own ~46-listing batch (also starting at id 1981, running to 2026) while
# this one was mid-pipeline. Per this project's established collision
# precedent (see commit 7cb8105's note on the same situation), this batch's
# ids were bumped by +46 (to 2027-2053) to sit after the true max id, and
# descEn (bilingual RU/EN, added mid-run by the same concurrent activity)
# was appended to each entry. This file was renamed to 84 and is a record
# of what's actually in rebuild_final.py -- do not re-run it, the insert
# already happened.
import json

data = {r["list_id"]: r for r in json.load(open("daily7_details.json", encoding="utf-8"))}

# (new_id, list_id, city, district, type, price, area, description_ru, url, posted, daysAgo)
ROWS = [
    (2027, 134400894, "nha-trang", "vp", "Квартира", 15000000, 71,
     "ЖК Mường Thanh Viễn Triều (блок 2B1730), 2 спальни, 2 с/у, 71м², полная меблировка по фото, без животных. У пляжа Hòn Chồng, вся инфраструктура рядом. Ул. Phạm Văn Đồng, Vĩnh Phước.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134400894.htm", "1 день назад", 1),
    (2028, 134383381, "nha-trang", "vp", "Квартира", 12000000, 60,
     "ЖК Oceanus (блок OC1B), 2 спальни, 2 с/у, 60м², аренда от 3/6/12 месяцев. Ул. Phạm Văn Đồng, Vĩnh Phước.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134383381.htm", "2 дня назад", 2),
    (2029, 134379092, "nha-trang", "vt", "Квартира", 6500000, 40,
     "1-спальная квартира с балконом на 1 этаже, 40м², полная меблировка, отдельная стиральная машина, свободна с 1 сентября. Рядом ЖК PH, южная часть Нячанга. Ул. Trường Sơn, Vĩnh Trường.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134379092.htm", "2 дня назад", 2),
    (2030, 134377726, "nha-trang", "tl", "Квартира", 10000000, 55,
     "Квартира в доме 60 Nguyễn Thiện Thuật, 2 спальни, 1 с/у, 55м², полная меблировка, до моря ~300м. Тан Лап.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134377726.htm", "2 дня назад", 2),
    (2031, 134360941, "nha-trang", "pl", "Квартира", 18000000, 88,
     "Угловая 3-спальная квартира (CH-3489), 2 с/у, 88м², полная меблировка, вид на реку и горы, есть место для авто, балкон на восток. Ул. Võ Văn Kiệt, Phước Long.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-nha-trang-khanh-hoa/134360941.htm", "3 дня назад", 3),
    (2032, 134406512, "nha-trang", "ph", "Дом", 30000000, 60,
     "Дом целиком, 4 спальни, 3 с/у, 3 этажа + техэтаж; площадь застройки 60м² (участок 80м², по объявлению также заявлена общая используемая площадь ~200м²). Рядом море, рынок, школы, супермаркет. Ул. Lê Hiến Mai, Phước Hải.",
     "https://www.nhatot.com/thue-nha-dat-thanh-pho-nha-trang-khanh-hoa/134406512.htm", "сегодня", 0),

    (2033, 134391269, "da-lat", "cl", "Квартира", 5500000, 35,
     "1-спальная квартира (CH-2), 35м², 3 этаж (лестница), полная меблировка, своя стиральная машина, место для мото и авто. Рядом больница, рынок, ~5 мин до ночного рынка Đà Lạt. Ул. Trần Nhật Duật, Cam Ly (быв. Phường 5).",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134391269.htm", "1 день назад", 1),
    (2034, 134385733, "da-lat", "lv", "Квартира", 6000000, 65,
     "1-спальная квартира (CH-86) с балконом, 65м², полная меблировка (ТВ, холодильник, стиральная машина, диван), просторная парковка для мото. ~4 мин до озера Xuân Hương. Ул. Lý Nam Đế, Lâm Viên (быв. Phường 8).",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134385733.htm", "1 день назад", 1),
    (2035, 134385088, "da-lat", "xh", "Квартира", 11000000, 55,
     "2-спальная квартира (CH-181), 2 с/у, 55м², 2 балкона, мансарда, коммунальные услуги включены, охрана 24/7. Ул. Hoàng Hoa Thám, Xuân Hương (быв. Phường 10).",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134385088.htm", "1 день назад", 1),
    (2036, 134372126, "da-lat", "cl", "Студия", 11000000, 40,
     "Дуплекс-студия (STU-133) с балконом, 40м², полная меблировка, стиральная машина в прачечной здания. Рядом Bách Hóa Xanh, школа Lam Sơn, областная больница. Ул. Nguyễn An Ninh, Cam Ly (быв. Phường 6).",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-da-lat-lam-dong/134372126.htm", "2 дня назад", 2),
    (2037, 134385560, "da-lat", "xh", "Дом", 16000000, 100,
     "Дом целиком (NNC-69), 5 спален, 4 с/у, цоколь + 2 этажа; площадь застройки 100м² (используемая ~300м²), комната для алтаря и караоке, заезд на авто через переулок. Рядом школа Thăng Long, GO!. Ул. Khởi Nghĩa Bắc Sơn, Xuân Hương (быв. Phường 10).",
     "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134385560.htm", "1 день назад", 1),
    (2038, 134380462, "da-lat", "xh", "Дом", 10000000, 50,
     "Новый дом, 2 спальни, 1 этаж + 1, крыша в тайском стиле; площадь застройки 50м² (используемая ~100м²), готов к заезду. Рядом рынок Đồng Tâm, Xuân Hương (быв. Phường 4).",
     "https://www.nhatot.com/thue-nha-dat-thanh-pho-da-lat-lam-dong/134380462.htm", "2 дня назад", 2),

    (2039, 134387513, "da-nang", "hcg", "Квартира", 25000000, 80,
     "ЖК Vista, новая квартира (первая сдача), 2 спальни, 2 с/у, 80м², полная меблировка, можно с животными, бесплатный Wi-Fi; коммуналка по гостарифу, сервис-сбор 17 тыс донг/м²/мес. Ул. Xô Viết Nghệ Tĩnh, Hòa Cường.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-quan-hai-chau-da-nang/134387513.htm", "1 день назад", 1),
    (2040, 134404762, "da-nang", "hx", "Квартира", 8000000, 40,
     "1-спальная квартира, новая (первая сдача), 40м², премиум-меблировка (диван, ТВ), отдельный Wi-Fi в каждой комнате; без животных и электротранспорта. Ул. Cồn Dầu 19, Hòa Xuân.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134404762.htm", "сегодня", 0),
    (2041, 134412959, "da-nang", "ah", "Квартира", 22999999, 63,
     "ЖК Hiyori Garden Tower, 2 спальни, 2 с/у, 63м², вид на море и город, бассейн и тренажёрный зал в комплексе, полная меблировка. Ул. Võ Văn Kiệt, An Hải (Sơn Trà).",
     "https://www.nhatot.com/thue-can-ho-chung-cu-quan-son-tra-da-nang/134412959.htm", "сегодня", 0),
    (2042, 134412945, "da-nang", "lc", "Квартира", 8500000, 63,
     "ЖК Mia Center Point, новая квартира (первая сдача), 2 спальни, 63м², высокий этаж с видом на море. Ул. Ngô Thì Nhậm, Liên Chiểu.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-quan-lien-chieu-da-nang/134412945.htm", "сегодня", 0),
    (2043, 134399572, "da-nang", "cl2", "Квартира", 6000000, 45,
     "1-спальная квартира, 45м², премиум-меблировка (кондиционер, ТВ, холодильник, стиральная машина, водонагреватель), широкая улица (10.5м), рядом школа, детсад, рынок, больница. Ул. Đinh Châu, Cẩm Lệ.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-quan-cam-le-da-nang/134399572.htm", "сегодня", 0),
    (2044, 133425328, "da-nang", "hk", "Дом", 18000000, 114,
     "Дом целиком, фасад, 3 этажа, 114м² (участок 350м²), 5 спален, 3 с/у, полная меблировка (кондиционеры, стиральная машина, холодильник), отдельные балкон и место для сушки. Подходит для семьи, специалистов, офиса или бизнеса. Ул. Trần Đình Tri, Hòa Khánh.",
     "https://www.nhatot.com/thue-nha-dat-quan-lien-chieu-da-nang/133425328.htm", "сегодня", 0),
    (2045, 134412977, "da-nang", "tk", "Дом", 16000000, 65,
     "Дом 2 этажа в переулке, 65м² (участок 52м², используемая площадь 104м²), 3 спальни, 2 с/у, полная меблировка, место для мото; рядом рынок морепродуктов и школы. Ул. Dũng Sĩ Thanh Khê, Thanh Khê.",
     "https://www.nhatot.com/thue-nha-dat-quan-thanh-khe-da-nang/134412977.htm", "сегодня", 0),
    (2046, 134412706, "da-nang", "ns", "Дом", 30000000, 100,
     "Дом целиком, 3 этажа, 100м², 4 спальни, 3 с/у, свободная планировка на 3-м этаже (можно под кабинет), просторная терраса для сушки. Ул. Hoài Thanh, Ngũ Hành Sơn (Mỹ An).",
     "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134412706.htm", "сегодня", 0),
    (2047, 134412459, "da-nang", "hcg", "Дом", 40000000, 95,
     "Дом 5 этажей, 95м² (фасад 5м), 8 спален, 5 с/у — подходит под мини-отель/общежитие или крупную семью. Ул. Phan Đăng Lưu, Hòa Cường (Hải Châu).",
     "https://www.nhatot.com/thue-nha-dat-quan-hai-chau-da-nang/134412459.htm", "сегодня", 0),
    (2048, 134377857, "da-nang", "ns", "Дом", 120000000, 325,
     "Вилла с бассейном, 2 этажа, 325м², 5 спален, 6 с/у — жильё премиум-класса рядом с пляжем Mỹ Khê. Ул. Chế Lan Viên, Ngũ Hành Sơn (Mỹ An).",
     "https://www.nhatot.com/thue-nha-dat-quan-ngu-hanh-son-da-nang/134377857.htm", "2 дня назад", 2),

    (2049, 134410367, "vung-tau", "vtp", "Квартира", 8500000, 110,
     "ЖК Silver Sea (Bãi Trước/Bàcu), 2 спальни, 2 с/у, 110м² (в объявлении также встречается 114м²), полная меблировка, вид на море, договор от 6 месяцев.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134410367.htm", "сегодня", 0),
    (2050, 134385793, "vung-tau", "vtp", "Квартира", 8000000, 108,
     "ЖК Sơn Thịnh 1 у пляжа Thùy Vân, 2 спальни, 3 с/у, 108м² (в тексте объявления также указано 105м²), премиум-меблировка, высокий этаж с диагональным видом на море и город.",
     "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-vung-tau-ba-ria-vung-tau/134385793.htm", "1 день назад", 1),
    (2051, 134385686, "vung-tau", "pth", "Дом", 18000000, 80,
     "Таунхаус в комплексе La Vida Residences, 4 спальни, 5 с/у, 80м², современная полная меблировка.",
     "https://www.nhatot.com/thue-nha-dat-thanh-pho-vung-tau-ba-ria-vung-tau/134385686.htm", "1 день назад", 1),
    (2052, 134372495, "vung-tau", "tth", "Дом", 3800000, 75,
     "Дом целиком, 2 спальни, 1 с/у, 75м², в переулке ул. Nguyễn An Ninh, тихий район, свет ~3-3.5 тыс/кВт, вода 14 тыс/м³.",
     "https://www.nhatot.com/thue-nha-dat-thanh-pho-vung-tau-ba-ria-vung-tau/134372495.htm", "2 дня назад", 2),

    (2053, 134377572, "quy-nhon", "qnn", "Дом", 4000000, 50,
     "Дом целиком: гостиная, 1 спальня, кухня, с/у, 50м², свет и вода по гостарифу, парковка у дома; рядом рынок, кожно-венерологическая больница, школы. Квартал Hưng Thịnh, Quy Nhơn Nam (Ghềnh Ráng).",
     "https://www.nhatot.com/thue-nha-dat-thanh-pho-qui-nhon-binh-dinh/134377572.htm", "2 дня назад", 2),
]

if __name__ == "__main__":
    print("This is a record of an already-applied batch (see module docstring). Not re-running.")
