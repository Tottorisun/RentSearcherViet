# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 1 строка, 2026-10-04, город hoi-an.

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
  * 45240276 -- had, 55,000,000 ₫, 207 м²: нынешний район назван в карточке: Hội An Đông

ОТСЕЯНО (22):
  * 46365885 -- цена не читается: Giá thỏa thuận
  * 46325872 -- старее 6 дней (Đăng 1 tuần trước)
  * 38338118 -- старее 6 дней (Đăng 1 tuần trước)
  * 35898029 -- старее 6 дней (Đăng 1 tuần trước)
  * 45631159 -- старее 6 дней (Đăng 11/08/2026)
  * 45978499 -- старее 6 дней (Đăng 12/07/2026)
  * 45790325 -- старее 6 дней (Đăng 07/07/2026)
  * 45840173 -- старее 6 дней (Đăng 08/06/2026)
  * 45763264 -- старее 6 дней (Đăng 20/05/2026)
  * 45703294 -- старее 6 дней (Đăng 11/05/2026)
  * 46372703 -- похоже на уже заведённое: id 1019192
  * 46180369 -- старее 6 дней (Đăng 24/08/2026)
  * 46185585 -- старее 6 дней (Đăng 15/08/2026)
  * 46170907 -- старее 6 дней (Đăng 12/08/2026)
  * 46147035 -- старее 6 дней (Đăng 06/08/2026)
  * 44627123 -- старее 6 дней (Đăng 24/05/2026)
  * 44533134 -- старее 6 дней (Đăng 24/05/2026)
  * 45624048 -- старее 6 дней (Đăng 09/05/2026)
  * 42989229 -- старее 6 дней (Đăng 08/05/2026)
  * 45685235 -- старее 6 дней (Đăng 07/05/2026)
  * 45584028 -- старее 6 дней (Đăng 20/04/2026)
  * 45448767 -- старее 6 дней (Đăng 14/04/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001849]
REPLACES = []

NEW_SRC = r'''
L(3001849,"hoi-an","had","Дом",55000000,207,
  "5-спальный дом, 207 м², Hội An Đông — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-xa-cam-thanh-3-casamia-hoi-an/villa-3-tang-5pn-vip-khu-an-pr45240276","5 дней назад",5,source="batdongsan",postedOn="2026-09-29",
  descEn="5-bedroom house, 207 m², Hội An Đông — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/05/16/20250516094454-1041_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/16/20250516094454-ddb7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/16/20250516094454-bb69_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/16/20250516094455-dd4c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/16/20250516094455-2434_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/16/20250516094455-6b6a_wm.jpg"], "am": ["pool"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
