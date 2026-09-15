# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 2 строки, 2026-09-15, город phu-quoc.

Партию собрал collect_batdongsan.py -- без модели в контуре. Район не выведен, а
взят у самого источника: портал печатает нынешний квартал в карточке («P. Bắc
Nha Trang mới») и прежний в адресе объявления («phuong-vinh-phuoc»); строка
заводится, только если один из них совпал с районом нашего сайта. Описание
собрано из полей объявления, рекламный текст не пересказан. Фотографии --
ссылками на batdongsan, у них же и хранятся.

Возраст -- от последней выкладки: более поздняя из даты карточки и даты страницы
объявления. Перевыложенное объявление (те же фотографии) заменяет строку сайта:
её номер -- в REPLACES, партия снимает её, вставив новую.

ЗАВЕДЕНО:
  * 45720427 -- ath, 10,000,000 ₫, 117 м²: квартал в адресе объявления: an thoi
  * 46279260 -- ath, 60,000,000 ₫: квартал в адресе объявления: an thoi

ОТСЕЯНО (41):
  * 46247914 -- старее 6 дней (Đăng 1 tuần trước)
  * 46247898 -- старее 6 дней (Đăng 1 tuần trước)
  * 45838612 -- старее 6 дней (Đăng 08/07/2026)
  * 45853038 -- старее 6 дней (Đăng 04/06/2026)
  * 45595055 -- старее 6 дней (Đăng 13/05/2026)
  * 37960506 -- старее 6 дней (Đăng 13/08/2026)
  * 46165692 -- старее 6 дней (Đăng 11/08/2026)
  * 46116067 -- старее 6 дней (Đăng 30/07/2026)
  * 46116036 -- старее 6 дней (Đăng 30/07/2026)
  * 46115504 -- старее 6 дней (Đăng 30/07/2026)
  * 46110389 -- старее 6 дней (Đăng 29/07/2026)
  * 46080674 -- старее 6 дней (Đăng 22/07/2026)
  * 46030370 -- старее 6 дней (Đăng 11/07/2026)
  * 42730896 -- старее 6 дней (Đăng 25/06/2026)
  * 45870719 -- старее 6 дней (Đăng 07/06/2026)
  * 38401464 -- старее 6 дней (Đăng 26/04/2026)
  * 43491588 -- старее 6 дней (Đăng 1 tuần trước)
  * 46225499 -- старее 6 дней (Đăng 1 tuần trước)
  * 45219765 -- старее 6 дней (Đăng 26/07/2026)
  * 45938398 -- старее 6 дней (Đăng 24/07/2026)
  * 45923428 -- старее 6 дней (Đăng 17/06/2026)
  * 46208759 -- старее 6 дней (Đăng 1 tuần trước)
  * 44873225 -- старее 6 дней (Đăng 29/04/2026)
  * 44807099 -- старее 6 дней (Đăng 1 tuần trước)
  * 46257202 -- старее 6 дней (Đăng 1 tuần trước)
  * 46258926 -- старее 6 дней (Đăng 1 tuần trước)
  * 46259525 -- старее 6 дней (Đăng 1 tuần trước)
  * 46265271 -- старее 6 дней (Đăng 1 tuần trước)
  * 46138338 -- старее 6 дней (Đăng 3 tuần trước)
  * 46147277 -- старее 6 дней (Đăng 06/08/2026)
  * 46079719 -- старее 6 дней (Đăng 22/07/2026)
  * 45938638 -- старее 6 дней (Đăng 01/07/2026)
  * 45826443 -- старее 6 дней (Đăng 22/06/2026)
  * 45816074 -- старее 6 дней (Đăng 13/06/2026)
  * 45874340 -- старее 6 дней (Đăng 08/06/2026)
  * 45816691 -- старее 6 дней (Đăng 28/05/2026)
  * 45815948 -- старее 6 дней (Đăng 28/05/2026)
  * 45796144 -- старее 6 дней (Đăng 25/05/2026)
  * 45727630 -- старее 6 дней (Đăng 14/05/2026)
  * 45723741 -- старее 6 дней (Đăng 13/05/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3000715, 3000716]
REPLACES = []

NEW_SRC = r'''
L(3000715,"phu-quoc","ath","Дом",10000000,117,
  "Дом, 117 м², An Thới.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-hong-mon-phuong-an-thoi_1-meyhomes-capital-phu-quoc/cho-3-5-tang-tho-nguyen-can-khu-quoc-pr45720427","вчера",1,source="batdongsan",postedOn="2026-09-14",
  descEn="House, 117 m², An Thới.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513084333-4424_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513084337-a6c3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513084340-08c5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513084341-9ec8_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/05/13/20260513084333-4424_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/05/13/20260513084337-a6c3_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000716,"phu-quoc","ath","Дом",60000000,None,
  "Дом, An Thới.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-nguyen-van-cu-1-phuong-an-thoi_1-360/cho-san-vuon-moi-vao-o-uong-phu-quoc-pr46279260","6 дней назад",6,source="batdongsan",postedOn="2026-09-09",
  descEn="House, An Thới.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194947-814e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194948-903d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194949-08eb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194951-7e7f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194952-8296_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194953-c001_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
