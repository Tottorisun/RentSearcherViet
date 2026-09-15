# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 3 строки, 2026-09-15, город phan-thiet.

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
  * 46288454 -- mn, 5,000,000 ₫, 35 м²: нынешний район назван в карточке: Mũi Né
  * 46237691 -- tt, 12,000,000 ₫, 160 м²: нынешний район назван в карточке: Tiến Thành
  * 46279257 -- tt, 10,000,000 ₫, 120 м²: нынешний район назван в карточке: Tiến Thành

ОТСЕЯНО (28):
  * 45077848 -- старее 6 дней (Đăng 1 tuần trước)
  * 46210314 -- старее 6 дней (Đăng 3 tuần trước)
  * 35968857 -- старее 6 дней (Đăng 10/08/2026)
  * 45827525 -- старее 6 дней (Đăng 23/07/2026)
  * 44918985 -- старее 6 дней (Đăng 19/06/2026)
  * 44132087 -- старее 6 дней (Đăng 15/05/2026)
  * 45339296 -- старее 6 дней (Đăng 18/03/2026)
  * 46110925 -- старее 6 дней (Đăng 29/07/2026)
  * 46011362 -- старее 6 дней (Đăng 07/07/2026)
  * 45906376 -- старее 6 дней (Đăng 13/06/2026)
  * 45779256 -- старее 6 дней (Đăng 22/05/2026)
  * 46257234 -- старее 6 дней (Đăng 1 tuần trước)
  * 44918598 -- старее 6 дней (Đăng 12/06/2026)
  * 45655262 -- старее 6 дней (Đăng 29/07/2026)
  * 45729634 -- старее 6 дней (Đăng 29/07/2026)
  * 44918855 -- старее 6 дней (Đăng 17/06/2026)
  * 46152912 -- старее 6 дней (Đăng 1 tuần trước)
  * 46001702 -- старее 6 дней (Đăng 1 tuần trước)
  * 46264011 -- старее 6 дней (Đăng 1 tuần trước)
  * 46271443 -- старее 6 дней (Đăng 1 tuần trước)
  * 45807447 -- старее 6 дней (Đăng 27/05/2026)
  * 41158969 -- старее 6 дней (Đăng 10/08/2026)
  * 43959690 -- старее 6 дней (Đăng 10/08/2026)
  * 46155529 -- старее 6 дней (Đăng 08/08/2026)
  * 14169716 -- старее 6 дней (Đăng 10/06/2026)
  * 45489372 -- старее 6 дней (Đăng 06/04/2026)
  * 45451129 -- старее 6 дней (Đăng 01/04/2026)
  * 43926337 -- старее 6 дней (Đăng 23/03/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3000717, 3000718, 3000719]
REPLACES = []

NEW_SRC = r'''
L(3000717,"phan-thiet","mn","Дом",5000000,35,
  "1-спальный дом, 35 м², Mũi Né — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-dinh-chieu-phuong-ham-tien-181/cho-phong-homestay-inh-gan-bien-cho-truong-sieu-thi-pr46288454","вчера",1,source="batdongsan",postedOn="2026-09-14",
  descEn="1-bedroom house, 35 m², Mũi Né — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911184743-ab8c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911184742-ebe0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911184743-febd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911184743-c7cf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911184742-b3a6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911184743-86f2_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000718,"phan-thiet","tt","Дом",12000000,160,
  "3-спальный дом, 160 м², Tiến Thành — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-lac-long-quan-xa-tien-thanh-1-novaworld-phan-thiet/cho-villa-theo-thang-tu-10-trieu-thang-pr46237691","вчера",1,source="batdongsan",postedOn="2026-09-14",
  descEn="3-bedroom house, 160 m², Tiến Thành — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828160259-92f6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828160257-715e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828160258-4215_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828160259-e55d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828160256-ef07_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828160300-4780_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000719,"phan-thiet","tt","Дом",10000000,120,
  "4-спальный дом, 120 м², Tiến Thành — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-lac-long-quan-xa-tien-thanh-1-novaworld-phan-thiet/chu-can-cho-nguyen-can-4-phong-ngu-gia-10tr-thang-lh-pr46279257","6 дней назад",6,source="batdongsan",postedOn="2026-09-09",
  descEn="4-bedroom house, 120 m², Tiến Thành — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194835-c0c0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194835-020b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194834-5ba3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194834-fc91_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194835-9e11_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909194835-9348_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
