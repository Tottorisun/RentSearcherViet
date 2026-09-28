# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 1 строка, 2026-09-28, город hue.

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
  * 45805693 -- vyd, 18,000,000 ₫, 160 м²: нынешний район назван в карточке: Vỹ Dạ

ОТСЕЯНО (22):
  * 46288555 -- старее 6 дней (Đăng 2 tuần trước)
  * 46213971 -- старее 6 дней (Đăng 28/08/2026)
  * 45741873 -- старее 6 дней (Đăng 29/05/2026)
  * 45764720 -- старее 6 дней (Đăng 20/05/2026)
  * 45743221 -- старее 6 дней (Đăng 16/05/2026)
  * 45611683 -- старее 6 дней (Đăng 23/04/2026)
  * 45510139 -- старее 6 дней (Đăng 09/04/2026)
  * 46296381 -- старее 6 дней (Đăng 2 tuần trước)
  * 45997282 -- старее 6 дней (Đăng 03/07/2026)
  * 45611057 -- старее 6 дней (Đăng 23/04/2026)
  * 46146668 -- старее 6 дней (Đăng 06/08/2026)
  * 45694373 -- старее 6 дней (Đăng 14/05/2026)
  * 45660334 -- старее 6 дней (Đăng 04/05/2026)
  * 45450244 -- старее 6 дней (Đăng 01/04/2026)
  * 41136905 -- старее 6 дней (Đăng 15/08/2026)
  * 45702315 -- старее 6 дней (Đăng 11/05/2026)
  * 46307247 -- старее 6 дней (Đăng 1 tuần trước)
  * 46250772 -- старее 6 дней (Đăng 2 tuần trước)
  * 45815018 -- старее 6 дней (Đăng 2 tuần trước)
  * 45393399 -- старее 6 дней (Đăng 13/07/2026)
  * 45602505 -- старее 6 дней (Đăng 22/04/2026)
  * 45421004 -- старее 6 дней (Đăng 28/03/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001635]
REPLACES = []

NEW_SRC = r'''
L(3001635,"hue","vyd","Дом",18000000,160,
  "2-спальный дом, 160 м², Vỹ Dạ — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-le-duc-anh-phuong-thuy-van-eco-garden-hue/cho-full-noi-that-ecogarden-chi-18-trieu-thang-pr45805693","сегодня",0,source="batdongsan",postedOn="2026-09-28",
  descEn="2-bedroom house, 160 m², Vỹ Dạ — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/05/27/20260527083121-8caa_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/27/20260527083122-47d6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/27/20260527083123-029a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/27/20260527083123-4d40_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/27/20260527083124-7283_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/27/20260527083125-22b8_wm.jpg"], "am": ["k"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
