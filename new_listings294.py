# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 1 строка, 2026-09-22, город da-lat.

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
  * 46325410 -- cl, 35,000,000 ₫, 400 м²: нынешний район назван в карточке: Cam Ly-Đà Lạt

ОТСЕЯНО (67):
  * 46175563 -- старее 6 дней (Đăng 1 tuần trước)
  * 42512173 -- старее 6 дней (Đăng 1 tuần trước)
  * 46175548 -- старее 6 дней (Đăng 1 tuần trước)
  * 46290937 -- старее 6 дней (Đăng 1 tuần trước)
  * 46169987 -- старее 6 дней (Đăng 12/08/2026)
  * 45874200 -- старее 6 дней (Đăng 27/06/2026)
  * 44271365 -- старее 6 дней (Đăng 08/04/2026)
  * 45228785 -- старее 6 дней (Đăng 31/03/2026)
  * 45347154 -- старее 6 дней (Đăng 19/03/2026)
  * 45334210 -- старее 6 дней (Đăng 17/03/2026)
  * 45317373 -- старее 6 дней (Đăng 16/03/2026)
  * 46318499 -- уже на сайте
  * 46246761 -- уже на сайте
  * 46157935 -- старее 6 дней (Đăng 1 tuần trước)
  * 46291428 -- старее 6 дней (Đăng 1 tuần trước)
  * 46289856 -- старее 6 дней (Đăng 1 tuần trước)
  * 46252039 -- старее 6 дней (Đăng 2 tuần trước)
  * 46252137 -- старее 6 дней (Đăng 2 tuần trước)
  * 46252168 -- старее 6 дней (Đăng 2 tuần trước)
  * 46252216 -- старее 6 дней (Đăng 2 tuần trước)
  * 46252239 -- старее 6 дней (Đăng 2 tuần trước)
  * 46140934 -- старее 6 дней (Đăng 05/08/2026)
  * 45962440 -- старее 6 дней (Đăng 25/06/2026)
  * 45576808 -- старее 6 дней (Đăng 18/04/2026)
  * 45436230 -- старее 6 дней (Đăng 30/03/2026)
  * 46267523 -- старее 6 дней (Đăng 2 tuần trước)
  * 46181403 -- старее 6 дней (Đăng 14/08/2026)
  * 46159595 -- старее 6 дней (Đăng 10/08/2026)
  * 46155722 -- старее 6 дней (Đăng 08/08/2026)
  * 46144431 -- старее 6 дней (Đăng 06/08/2026)
  * 45572182 -- старее 6 дней (Đăng 29/07/2026)
  * 45703872 -- старее 6 дней (Đăng 18/06/2026)
  * 41472028 -- старее 6 дней (Đăng 2 tuần trước)
  * 45648318 -- старее 6 дней (Đăng 2 tuần trước)
  * 46185034 -- старее 6 дней (Đăng 2 tuần trước)
  * 46185083 -- старее 6 дней (Đăng 2 tuần trước)
  * 46185045 -- старее 6 дней (Đăng 2 tuần trước)
  * 46185068 -- старее 6 дней (Đăng 2 tuần trước)
  * 46217397 -- старее 6 дней (Đăng 1 tháng trước)
  * 45985291 -- старее 6 дней (Đăng 01/07/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001219]
REPLACES = []

NEW_SRC = r'''
L(3001219,"da-lat","cl","Дом",35000000,400,
  "15-спальный дом, 400 м², Cam Ly - Đà Lạt — 14 санузлов, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-hoang-van-thu-phuong-5_3-391/ban-cong-viec-tai-sai-gon-nen-sang-nhuong-lai-khach-san-villa-hoa-chuong-a-lat-pr46325410","вчера",1,source="batdongsan",postedOn="2026-09-21",
  descEn="15-bedroom house, 400 m², Cam Ly - Đà Lạt — 14 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921115558-0392_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921115600-60e4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921115601-39e9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921115602-e68d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921115604-8a3e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921115605-9f04_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
