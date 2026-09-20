# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 4 строки, 2026-09-20, город da-lat.

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
  * 46318499 -- xh, 50,000,000 ₫, 100 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46246761 -- cl, 4,000,000 ₫, 75 м²: нынешний район назван в карточке: Cam Ly-Đà Lạt
  * 45874487 -- xt, 120,000,000 ₫, 100 м²: нынешний район назван в карточке: Xuân Trường-Đà Lạt
  * 46302621 -- xh, 35,000,000 ₫, 456 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt

ОТСЕЯНО (64):
  * 46175563 -- уже на сайте
  * 42512173 -- уже на сайте
  * 46175548 -- уже на сайте
  * 46290937 -- старее 6 дней (Đăng 1 tuần trước)
  * 46169987 -- старее 6 дней (Đăng 12/08/2026)
  * 45874200 -- старее 6 дней (Đăng 27/06/2026)
  * 44271365 -- старее 6 дней (Đăng 08/04/2026)
  * 45228785 -- старее 6 дней (Đăng 31/03/2026)
  * 45347154 -- старее 6 дней (Đăng 19/03/2026)
  * 45334210 -- старее 6 дней (Đăng 17/03/2026)
  * 45317373 -- старее 6 дней (Đăng 16/03/2026)
  * 46157935 -- уже на сайте
  * 46291428 -- старее 6 дней (Đăng 1 tuần trước)
  * 46289856 -- старее 6 дней (Đăng 1 tuần trước)
  * 46252039 -- старее 6 дней (Đăng 1 tuần trước)
  * 46252137 -- старее 6 дней (Đăng 1 tuần trước)
  * 46252168 -- старее 6 дней (Đăng 1 tuần trước)
  * 46252216 -- старее 6 дней (Đăng 1 tuần trước)
  * 46252239 -- старее 6 дней (Đăng 1 tuần trước)
  * 46140934 -- старее 6 дней (Đăng 05/08/2026)
  * 45962440 -- старее 6 дней (Đăng 25/06/2026)
  * 45576808 -- старее 6 дней (Đăng 18/04/2026)
  * 45436230 -- старее 6 дней (Đăng 30/03/2026)
  * 46267523 -- старее 6 дней (Đăng 1 tuần trước)
  * 46181403 -- старее 6 дней (Đăng 14/08/2026)
  * 46159595 -- старее 6 дней (Đăng 10/08/2026)
  * 46155722 -- старее 6 дней (Đăng 08/08/2026)
  * 46144431 -- старее 6 дней (Đăng 06/08/2026)
  * 45572182 -- старее 6 дней (Đăng 29/07/2026)
  * 45703872 -- старее 6 дней (Đăng 18/06/2026)
  * 41472028 -- старее 6 дней (Đăng 1 tuần trước)
  * 45648318 -- старее 6 дней (Đăng 1 tuần trước)
  * 46185034 -- старее 6 дней (Đăng 1 tuần trước)
  * 46185083 -- старее 6 дней (Đăng 1 tuần trước)
  * 46185045 -- старее 6 дней (Đăng 1 tuần trước)
  * 46185068 -- старее 6 дней (Đăng 1 tuần trước)
  * 46217397 -- старее 6 дней (Đăng 3 tuần trước)
  * 45985291 -- старее 6 дней (Đăng 01/07/2026)
  * 45698255 -- старее 6 дней (Đăng 09/05/2026)
  * 45648108 -- старее 6 дней (Đăng 29/04/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001038, 3001039, 3001040, 3001041]
REPLACES = []

NEW_SRC = r'''
L(3001038,"da-lat","xh","Дом",50000000,100,
  "12-спальный дом, 100 м², Xuân Hương - Đà Lạt — 12 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ngo-thi-sy-phuong-4_3-391/cho-nguyen-can-12-phong-dang-can-ho-tai-hem-xe-hoi-uong-a-lat-pr46318499","вчера",1,source="batdongsan",postedOn="2026-09-19",
  descEn="12-bedroom house, 100 m², Xuân Hương - Đà Lạt — 12 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/19/20260919081612-a090_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/19/20260919081613-dc19_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/19/20260919081614-b1d8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/19/20260919081615-1f39_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/19/20260919081615-5cf7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/19/20260919081616-747f_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001039,"da-lat","cl","Дом",4000000,75,
  "2-спальный дом, 75 м², Cam Ly - Đà Lạt — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-han-thuyen-phuong-5_3-391/cho-tai-7-5-4-trieu-vnd-75-m2-ep-nhieu-tien-ich-chinh-chu-pr46246761","4 дня назад",4,source="batdongsan",postedOn="2026-09-16",
  descEn="2-bedroom house, 75 m², Cam Ly - Đà Lạt — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131453-cc66_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131453-074a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131453-7f73_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131455-a16d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131459-2895_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131459-5881_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001040,"da-lat","xt","Дом",120000000,100,
  "2-спальный дом, 100 м², Xuân Trường - Đà Lạt — 3 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-hung-vuong-2-xa-xuan-truong-1-391/cho-villa-1100m2-uong-thich-hop-kinh-doanh-hang-cao-cap-hien-trang-moi-ep-pr45874487","4 дня назад",4,source="batdongsan",postedOn="2026-09-16",
  descEn="2-bedroom house, 100 m², Xuân Trường - Đà Lạt — 3 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608112934-7ec2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608112934-2b7a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608112934-1a2f_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/06/08/20260608112934-7ec2_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/06/08/20260608112934-2b7a_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/06/08/20260608112934-1a2f_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001041,"da-lat","xh","Дом",35000000,456,
  "4-спальный дом, 456 м², Xuân Hương - Đà Lạt — 5 санузлов, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-an-son-phuong-4_3-391/cho-villa-rieng-khu-dic-son-pr46302621","5 дней назад",5,source="batdongsan",postedOn="2026-09-15",
  descEn="4-bedroom house, 456 m², Xuân Hương - Đà Lạt — 5 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/15/20260915152005-2f07_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/15/20260915152005-acc5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/15/20260915152156-61bd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/15/20260915152215-dd35_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/15/20260915152215-7c4d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/15/20260915152215-b571_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
