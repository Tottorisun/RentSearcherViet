# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 1 строка, 2026-09-22, город buon-ma-thuot.

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
  * 46326704 -- bmt, 6,000,000 ₫, 135 м²: нынешний район назван в карточке: Buôn Ma Thuột

ОТСЕЯНО (8):
  * 46283625 -- старее 6 дней (Đăng 1 tuần trước)
  * 46261167 -- старее 6 дней (Đăng 2 tuần trước)
  * 46320131 -- уже на сайте
  * 46228157 -- старее 6 дней (Đăng 2 tuần trước)
  * 46048776 -- старее 6 дней (Đăng 15/07/2026)
  * 45856597 -- старее 6 дней (Đăng 04/06/2026)
  * 44948358 -- старее 6 дней (Đăng 28/03/2026)
  * 45783149 -- старее 6 дней (Đăng 23/06/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001180]
REPLACES = []

NEW_SRC = r'''
L(3001180,"buon-ma-thuot","bmt","Дом",6000000,135,
  "3-спальный дом, 135 м², Buôn Ma Thuột — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-duan-phuong-tan-thanh-27-218/cho-nguyen-can-trung-tam-tp-buon-ma-thuot-pr46326704","вчера",1,source="batdongsan",postedOn="2026-09-21",
  descEn="3-bedroom house, 135 m², Buôn Ma Thuột — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921154158-0cd3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921154157-c264_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921154158-cfa5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921154158-6864_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921154158-95e1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921154158-d8b7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
