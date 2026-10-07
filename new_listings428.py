# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 2 строки, 2026-10-07, город hue.

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
  * 46383671 -- vyd, 9,000,000 ₫, 65 м²: нынешний район назван в карточке: Vỹ Dạ
  * 46366841 -- acu, 4,000,000 ₫, 70 м²: нынешний район назван в карточке: An Cựu

ОТСЕЯНО (25):
  * 46376349 -- похоже на уже заведённое: id 1023102
  * 46288555 -- старее 6 дней (Đăng 3 tuần trước)
  * 46213971 -- старее 6 дней (Đăng 28/08/2026)
  * 45741873 -- старее 6 дней (Đăng 29/05/2026)
  * 45764720 -- старее 6 дней (Đăng 20/05/2026)
  * 45743221 -- старее 6 дней (Đăng 16/05/2026)
  * 45611683 -- старее 6 дней (Đăng 23/04/2026)
  * 45510139 -- старее 6 дней (Đăng 09/04/2026)
  * 46296381 -- район не назван так, как его знает сайт (нет данных; в карточке «P. An Cựu»)
  * 46364249 -- старее 6 дней (Đăng 1 tuần trước)
  * 45997282 -- старее 6 дней (Đăng 03/07/2026)
  * 45611057 -- старее 6 дней (Đăng 23/04/2026)
  * 46146668 -- старее 6 дней (Đăng 06/08/2026)
  * 45694373 -- старее 6 дней (Đăng 14/05/2026)
  * 45660334 -- старее 6 дней (Đăng 04/05/2026)
  * 45450244 -- старее 6 дней (Đăng 01/04/2026)
  * 46370331 -- район не назван так, как его знает сайт (нет данных; в карточке «P. An Cựu»)
  * 41136905 -- старее 6 дней (Đăng 15/08/2026)
  * 45702315 -- старее 6 дней (Đăng 11/05/2026)
  * 45805693 -- старее 6 дней (Đăng 1 tuần trước)
  * 46307247 -- старее 6 дней (Đăng 3 tuần trước)
  * 45815018 -- старее 6 дней (Đăng 1 tháng trước)
  * 46250772 -- старее 6 дней (Đăng 1 tháng trước)
  * 45393399 -- старее 6 дней (Đăng 13/07/2026)
  * 45602505 -- старее 6 дней (Đăng 22/04/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3002060, 3002061]
REPLACES = []

NEW_SRC = r'''
L(3002060,"hue","vyd","Квартира",9000000,65,
  "2-спальная квартира, 65 м², Vỹ Dạ — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-to-huu-the-manor-crown-hue/cho-62-uong-sieu-hien-ai-sang-trong-pr46383671","2 дня назад",2,source="batdongsan",postedOn="2026-10-05",
  descEn="2-bedroom flat, 65 m², Vỹ Dạ — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005162336-1249_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005162336-2b25_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005162336-380c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005162336-c6e7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005162336-ff8f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005162336-2705_wm.jpg"], "am": ["k", "b"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3002061,"hue","acu","Квартира",4000000,70,
  "2-спальная квартира, 70 м², An Cựu — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-to-huu-nera-garden/cho-hue-bo-pho-ve-vuon-nhung-van-tron-ven-tien-nghi-pr46366841","6 дней назад",6,source="batdongsan",postedOn="2026-10-01",
  descEn="2-bedroom flat, 70 m², An Cựu — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/10/01/20261001101758-d23c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/01/20261001101805-1992_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/01/20261001101805-7c0b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/01/20261001101812-bc1f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/01/20261001101813-22d9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/01/20261001101813-ec0c_wm.jpg"], "am": ["w", "pool", "gym"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
