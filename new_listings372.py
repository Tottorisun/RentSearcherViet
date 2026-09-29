# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 1 строка, 2026-09-29, город quy-nhon.

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
  * 46093786 -- qn, 10,000,000 ₫, 65 м²: нынешний район назван в карточке: Quy Nhơn

ОТСЕЯНО (25):
  * 39050214 -- цена не читается: Giá thỏa thuận
  * 39050071 -- похоже на уже заведённое: id 3001419
  * 46343644 -- уже на сайте
  * 46340525 -- то же объявление, что id 3001420: общие фотографии, а та строка не старше
  * 44186366 -- цена не читается: Giá thỏa thuận
  * 44116108 -- уже на сайте
  * 42303849 -- уже на сайте
  * 42303705 -- уже на сайте
  * 44066604 -- похоже на уже заведённое: id 1010989
  * 37302356 -- уже на сайте
  * 45577841 -- старее 6 дней (Đăng 1 tuần trước)
  * 45577797 -- уже на сайте
  * 42954925 -- старее 6 дней (Đăng 1 tuần trước)
  * 43127816 -- старее 6 дней (Đăng 2 tuần trước)
  * 46273694 -- старее 6 дней (Đăng 3 tuần trước)
  * 44414389 -- старее 6 дней (Đăng 3 tuần trước)
  * 45797545 -- старее 6 дней (Đăng 25/05/2026)
  * 45557289 -- старее 6 дней (Đăng 15/04/2026)
  * 45408592 -- старее 6 дней (Đăng 2 tuần trước)
  * 46258739 -- старее 6 дней (Đăng 2 tuần trước)
  * 46083694 -- старее 6 дней (Đăng 05/08/2026)
  * 45308773 -- старее 6 дней (Đăng 15/07/2026)
  * 45636113 -- старее 6 дней (Đăng 27/05/2026)
  * 45486144 -- старее 6 дней (Đăng 06/04/2026)
  * 46095595 -- старее 6 дней (Đăng 31/07/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001706]
REPLACES = []

NEW_SRC = r'''
L(3001706,"quy-nhon","qn","Квартира",10000000,65,
  "2-спальная квартира, 65 м², Quy Nhơn — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-hai-cang-altara-residences/cho-nhieu-tang-cao-view-ep-1-2-3pn-quy-nhon-noi-that-cao-cap-dich-vu-4-sao-pr46093786","вчера",1,source="batdongsan",postedOn="2026-09-28",
  descEn="2-bedroom flat, 65 m², Quy Nhơn — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/07/25/20260725102343-9ca4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/25/20260725102342-2351_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/25/20260725102343-5d69_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/07/25/20260725102343-9ca4_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/07/25/20260725102342-2351_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/07/25/20260725102343-5d69_wm.jpg"], "am": ["w", "k"], "fl": 31, "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
