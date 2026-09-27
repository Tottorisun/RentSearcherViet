# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 1 строка, 2026-09-27, город phan-thiet.

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
  * 46264011 -- tt, 20,000,000 ₫, 240 м²: нынешний район назван в карточке: Tiến Thành

ОТСЕЯНО (31):
  * 46210314 -- старее 6 дней (Đăng 21/08/2026)
  * 45077848 -- старее 6 дней (Đăng 2 tuần trước)
  * 35968857 -- старее 6 дней (Đăng 10/08/2026)
  * 45827525 -- старее 6 дней (Đăng 23/07/2026)
  * 44918985 -- старее 6 дней (Đăng 19/06/2026)
  * 44132087 -- старее 6 дней (Đăng 15/05/2026)
  * 45906376 -- цена не читается: Giá thỏa thuận
  * 46288454 -- старее 6 дней (Đăng 1 tuần trước)
  * 46110925 -- старее 6 дней (Đăng 29/07/2026)
  * 46011362 -- старее 6 дней (Đăng 07/07/2026)
  * 45779256 -- старее 6 дней (Đăng 22/05/2026)
  * 44918598 -- уже на сайте
  * 46257234 -- старее 6 дней (Đăng 2 tuần trước)
  * 45655262 -- старее 6 дней (Đăng 29/07/2026)
  * 45729634 -- старее 6 дней (Đăng 29/07/2026)
  * 44918855 -- старее 6 дней (Đăng 17/06/2026)
  * 46152912 -- цена не читается: Giá thỏa thuận
  * 46001702 -- цена не читается: Giá thỏa thuận
  * 46321416 -- уже на сайте
  * 14169716 -- старее 6 дней (Đăng 1 tuần trước)
  * 46317503 -- старее 6 дней (Đăng 1 tuần trước)
  * 46237691 -- старее 6 дней (Đăng 1 tuần trước)
  * 45807447 -- старее 6 дней (Đăng 27/05/2026)
  * 46279257 -- старее 6 дней (Đăng 2 tuần trước)
  * 46271443 -- старее 6 дней (Đăng 2 tuần trước)
  * 41158969 -- старее 6 дней (Đăng 10/08/2026)
  * 43959690 -- старее 6 дней (Đăng 10/08/2026)
  * 46155529 -- старее 6 дней (Đăng 08/08/2026)
  * 45489372 -- старее 6 дней (Đăng 06/04/2026)
  * 45451129 -- старее 6 дней (Đăng 01/04/2026)
  * 43926337 -- старее 6 дней (Đăng 23/03/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001558]
REPLACES = []

NEW_SRC = r'''
L(3001558,"phan-thiet","tt","Дом",20000000,240,
  "3-спальный дом, 240 м², Tiến Thành — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-lac-long-quan-xa-tien-thanh-1-181/cho-on-lap-1024-ngan-ngay-tung-ngay-hang-tuan-hoac-pr46264011","3 дня назад",3,source="batdongsan",postedOn="2026-09-24",
  descEn="3-bedroom house, 240 m², Tiến Thành — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/06/20260906201944-812d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/06/20260906201947-3fd0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/06/20260906201951-629d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/06/20260906201955-cf91_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/06/20260906201959-f040_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/06/20260906201944-812d_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
