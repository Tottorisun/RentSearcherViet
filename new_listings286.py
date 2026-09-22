# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 1 строка, 2026-09-22, город quy-nhon.

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
  * 42954925 -- qn, 5,000,000 ₫, 65 м²: нынешний район назван в карточке: Quy Nhơn

ОТСЕЯНО (25):
  * 43127816 -- старее 6 дней (Đăng 1 tuần trước)
  * 39050214 -- старее 6 дней (Đăng 1 tuần trước)
  * 39050071 -- старее 6 дней (Đăng 1 tuần trước)
  * 45408592 -- старее 6 дней (Đăng 1 tuần trước)
  * 45408563 -- старее 6 дней (Đăng 1 tuần trước)
  * 46286935 -- старее 6 дней (Đăng 1 tuần trước)
  * 46273694 -- старее 6 дней (Đăng 2 tuần trước)
  * 44414389 -- старее 6 дней (Đăng 2 tuần trước)
  * 36709073 -- старее 6 дней (Đăng 2 tuần trước)
  * 44032246 -- старее 6 дней (Đăng 2 tuần trước)
  * 45172456 -- старее 6 дней (Đăng 2 tuần trước)
  * 46093786 -- старее 6 дней (Đăng 2 tuần trước)
  * 45797545 -- старее 6 дней (Đăng 25/05/2026)
  * 45557289 -- старее 6 дней (Đăng 15/04/2026)
  * 44164379 -- старее 6 дней (Đăng 2 tuần trước)
  * 45411022 -- старее 6 дней (Đăng 2 tuần trước)
  * 46208522 -- старее 6 дней (Đăng 2 tuần trước)
  * 46208549 -- старее 6 дней (Đăng 2 tuần trước)
  * 46208542 -- старее 6 дней (Đăng 2 tuần trước)
  * 46258739 -- старее 6 дней (Đăng 1 tuần trước)
  * 46083694 -- старее 6 дней (Đăng 05/08/2026)
  * 45308773 -- старее 6 дней (Đăng 15/07/2026)
  * 45636113 -- старее 6 дней (Đăng 27/05/2026)
  * 45486144 -- старее 6 дней (Đăng 06/04/2026)
  * 46095595 -- старее 6 дней (Đăng 31/07/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001179]
REPLACES = []

NEW_SRC = r'''
L(3001179,"quy-nhon","qn","Квартира",5000000,65,
  "2-спальная квартира, 65 м², Quy Nhơn — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-hai-cang-altara-residences/quy-cho-residence-6-5tr-7-5tr-th-2pn-2wc-tang-trung-cao-view-bien-pr42954925","вчера",1,source="batdongsan",postedOn="2026-09-21",
  descEn="2-bedroom flat, 65 m², Quy Nhơn — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-923b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-2c51_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-7801_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-5c3c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-ddf7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-673d_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
