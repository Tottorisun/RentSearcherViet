# -*- coding: utf-8 -*-
# Ежедневная проверка HCMC 19 авг 2026 (4-й прогон в тот же день, ~18:08, через ~1ч после
# 3-го прогона в 17:10/коммит b5c35da) — 1 новое объявление (ID 938).
#
# Chợ Tốt: собран свежий срез по всем 5 районам (Q1/Q4/Q7/Bình Thạnh/Thủ Đức) x 3 категориям
# (căn hộ/nhà/phòng trọ), 400 объявлений всего, 114 в целевых районах, 19 с честным
# orig_list_time <=3.5 дня. Из них 16 уже были добавлены 2-м/3-м прогонами сегодня (проверено
# по URL grep в rebuild_final.py — не дубли по факту, просто ранее найдены). Из оставшихся 3:
#   - 133129867 (принято, см. ниже).
#   - 134189578 ("Chuỗi căn hộ Studio-Duplex-1PN-2PN Quận 7, Quận 4 đa dạng các loại giá") —
#     явный посреднический "chuỗi" (сеть/цепочка) объявлений на разные юниты/цены, не конкретный
#     объект — отклонён по тому же принципу, что и в прошлых прогонах.
#   - 134174047 ("Hỗ trợ 2k8 Tìm trọ Quận 7") — это не объявление о конкретном жилье, а реклама
#     брокерской услуги поиска комнаты для студентов ("giỏ hàng có 100% phòng ở Q7", "nhắn anh
#     gửi full") — отклонено, не объект недвижимости.
#
# Batdongsan.com.vn: СЕГОДНЯ доступен для apartment-страниц (Q1/Q4/Q7/Bình Thạnh/Thủ Đức, все
# 200 OK) — house-страницы всех районов заблокированы Cloudflare (Cf-Mitigated: challenge).
# В целевых районах на apartment-страницах найдено 7 карточек в Tân Hưng (ward slug совпал),
# ВСЕ — посреднические "rổ hàng"/"chuỗi"/"hệ thống" объявления на комплексы Sunrise City(view)/
# Hoàng Anh Gia Lai II/Him Lam Riverside с несколькими ценами на разные юниты или прямой
# рекламой бесплатного поиска комнаты — ни одно не описывает конкретный проверяемый объект,
# все отклонены по тому же принципу, что и всегда в этом проекте. 0 добавлено с Batdongsan.
#
# Facebook Marketplace/группы: как обычно недоступен в headless-окружении (редирект на логин).
NEW_SRC = r'''
L(938,"ho-chi-minh","th","Квартира",9000000,50,
  "1-спальная квартира (1 с/у) с новой полной меблировкой, ул. Đường Số 79, Tân Hưng, Q7, рядом Lotte Mart. Светлая, отдельная кухня, естественная вентиляция.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133129867.htm","сегодня",0,source="chotot",
  details={"contact":"Trịnh Hoàng Tâm"}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content
new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
open(path, "w", encoding="utf-8").write(new_content)
print("inserted daily HCMC check 19 aug 2026 (4th pass): 1 listing (chotot); "
      "batdongsan accessible for apartments but only broker/chain ads in target wards (rejected); "
      "facebook inaccessible as usual")
