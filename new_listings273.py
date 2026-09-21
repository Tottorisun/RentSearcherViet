# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 2 строки, 2026-09-21, город phan-thiet.

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
  * 46321416 -- tt, 14,000,000 ₫, 160 м²: нынешний район назван в карточке: Tiến Thành
  * 46317503 -- tt, 20,000,000 ₫, 200 м²: нынешний район назван в карточке: Tiến Thành

ОТСЕЯНО (31):
  * 46210314 -- старее 6 дней (Đăng 21/08/2026)
  * 45077848 -- старее 6 дней (Đăng 1 tuần trước)
  * 35968857 -- старее 6 дней (Đăng 10/08/2026)
  * 45827525 -- старее 6 дней (Đăng 23/07/2026)
  * 44918985 -- старее 6 дней (Đăng 19/06/2026)
  * 44132087 -- старее 6 дней (Đăng 15/05/2026)
  * 46288454 -- уже на сайте
  * 45339296 -- старее 6 дней (Đăng 18/03/2026)
  * 46110925 -- старее 6 дней (Đăng 29/07/2026)
  * 46011362 -- старее 6 дней (Đăng 07/07/2026)
  * 45906376 -- старее 6 дней (Đăng 13/06/2026)
  * 45779256 -- старее 6 дней (Đăng 22/05/2026)
  * 44918598 -- старее 6 дней (Đăng 12/06/2026)
  * 46257234 -- старее 6 дней (Đăng 1 tuần trước)
  * 45655262 -- старее 6 дней (Đăng 29/07/2026)
  * 45729634 -- старее 6 дней (Đăng 29/07/2026)
  * 44918855 -- старее 6 дней (Đăng 17/06/2026)
  * 14169716 -- цена не читается: Giá thỏa thuận
  * 46001702 -- цена не читается: Giá thỏa thuận
  * 46237691 -- уже на сайте
  * 46152912 -- старее 6 дней (Đăng 1 tuần trước)
  * 46271443 -- старее 6 дней (Đăng 1 tuần trước)
  * 45807447 -- старее 6 дней (Đăng 27/05/2026)
  * 46279257 -- старее 6 дней (Đăng 1 tuần trước)
  * 46264011 -- старее 6 дней (Đăng 1 tuần trước)
  * 41158969 -- старее 6 дней (Đăng 10/08/2026)
  * 43959690 -- старее 6 дней (Đăng 10/08/2026)
  * 46155529 -- старее 6 дней (Đăng 08/08/2026)
  * 45489372 -- старее 6 дней (Đăng 06/04/2026)
  * 45451129 -- старее 6 дней (Đăng 01/04/2026)
  * 43926337 -- старее 6 дней (Đăng 23/03/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001088, 3001089]
REPLACES = []

NEW_SRC = r'''
L(3001088,"phan-thiet","tt","Дом",14000000,160,
  "3-спальный дом, 160 м², Tiến Thành — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-lac-long-quan-xa-tien-thanh-1-novaworld-phan-thiet/cho-thang-villa-tu-14-trieu-thang-pr46321416","сегодня",0,source="batdongsan",postedOn="2026-09-21",
  descEn="3-bedroom house, 160 m², Tiến Thành — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920031449-9a6b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920031451-70f8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920031452-94d9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920031454-dda8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920031456-dbc3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920031457-5b3a_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001089,"phan-thiet","tt","Дом",20000000,200,
  "3-спальный дом, 200 м², Tiến Thành — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-lac-long-quan-xa-tien-thanh-1-novaworld-phan-thiet/winter-escape-villa-vietnam-pr46317503","3 дня назад",3,source="batdongsan",postedOn="2026-09-18",
  descEn="3-bedroom house, 200 m², Tiến Thành — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918172234-a4fb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918172231-967f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918172232-69da_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918172233-e275_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918172233-67d4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918172231-374c_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
