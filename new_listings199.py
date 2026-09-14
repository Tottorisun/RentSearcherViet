# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 3 строки, 2026-09-14, город hue.

Партию собрал collect_batdongsan.py -- без модели в контуре. Район не выведен, а
взят у самого источника: портал печатает нынешний квартал в карточке («P. Bắc
Nha Trang mới») и прежний в адресе объявления («phuong-vinh-phuoc»); строка
заводится, только если один из них совпал с районом нашего сайта. Описание
собрано из полей объявления, рекламный текст не пересказан. Фотографии --
ссылками на batdongsan, у них же и хранятся.

Свежесть проверена дважды: по дате объявления и по его номеру. Номер сквозной по
стране, поэтому старый номер со свежей датой -- это перевыкладка, а не новое
объявление, и такие отброшены.

ЗАВЕДЕНО:
  * 46288555 -- vyd, 5,000,000 ₫, 53 м²: нынешний район назван в карточке: Vỹ Dạ
  * 46296381 -- acu, 30,000,000 ₫, 150 м²: квартал в адресе объявления: an cuu
  * 46250772 -- acu, 30,000,000 ₫, 242 м²: нынешний район назван в карточке: An Cựu

ОТСЕЯНО (23):
  * 46213971 -- номер объявления старый при свежей дате -- перевыкладка
  * 45741873 -- номер объявления старый при свежей дате -- перевыкладка
  * 45764720 -- номер объявления старый при свежей дате -- перевыкладка
  * 45743221 -- номер объявления старый при свежей дате -- перевыкладка
  * 45611683 -- номер объявления старый при свежей дате -- перевыкладка
  * 45510139 -- номер объявления старый при свежей дате -- перевыкладка
  * 45231649 -- номер объявления старый при свежей дате -- перевыкладка
  * 46249509 -- цена не читается: 7,8 tỷ/tháng
  * 45997282 -- номер объявления старый при свежей дате -- перевыкладка
  * 45611057 -- номер объявления старый при свежей дате -- перевыкладка
  * 46146668 -- номер объявления старый при свежей дате -- перевыкладка
  * 45694373 -- номер объявления старый при свежей дате -- перевыкладка
  * 45660334 -- номер объявления старый при свежей дате -- перевыкладка
  * 45450244 -- номер объявления старый при свежей дате -- перевыкладка
  * 45316455 -- номер объявления старый при свежей дате -- перевыкладка
  * 45227320 -- номер объявления старый при свежей дате -- перевыкладка
  * 41136905 -- номер объявления старый при свежей дате -- перевыкладка
  * 45702315 -- номер объявления старый при свежей дате -- перевыкладка
  * 45805693 -- номер объявления старый при свежей дате -- перевыкладка
  * 45815018 -- номер объявления старый при свежей дате -- перевыкладка
  * 45393399 -- номер объявления старый при свежей дате -- перевыкладка
  * 45602505 -- номер объявления старый при свежей дате -- перевыкладка
  * 45421004 -- номер объявления старый при свежей дате -- перевыкладка
"""
from listing_lock import insert_listings

IDS = [3000641, 3000642, 3000643]

NEW_SRC = r'''
L(3000641,"hue","vyd","Квартира",5000000,53,
  "2-спальная квартира, 53 м², Vỹ Dạ — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-lo-trach-phuong-xuan-phu-5-chung-cu-aranya-hue/cho-910-tang-9-7-5-trieu-53-m2-hang-hiem-tai-view-ep-pr46288555","вчера",1,source="batdongsan",
  descEn="2-bedroom flat, 53 m², Vỹ Dạ — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911195124-7b20_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911195124-0d9c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911195124-2f78_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911195124-4a87_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/11/20260911195124-7b20_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/11/20260911195124-0d9c_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000642,"hue","acu","Дом",30000000,150,
  "5-спальный дом, 150 м², An Cựu — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-dang-van-ngu-phuong-an-cuu-641/cho-nr-5pn-3wc-150m2-tai-35b-kiet-135-ang-hue-30-trieu-vnd-pr46296381","сегодня",0,source="batdongsan",
  descEn="5-bedroom house, 150 m², An Cựu — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914113400-e0ba_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914113408-7567_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914113408-0d54_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914113408-e1f5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914113408-1fe9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914113408-ec3a_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000643,"hue","acu","Дом",30000000,242,
  "9-спальный дом, 242 м², An Cựu — 7 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-vo-nguyen-giap-phuong-an-dong-phu-xuan-city/cho-don-vao-o-ngay-pr46250772","11 дней назад",11,source="batdongsan",
  descEn="9-bedroom house, 242 m², An Cựu — 7 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903110618-0496_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903110618-a96c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903110618-e479_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903110618-ca5c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903110618-4edf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903110618-3bb8_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
