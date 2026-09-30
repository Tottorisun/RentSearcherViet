# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 5 строк, 2026-09-30, город da-lat.

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
  * 46175548 -- xt, 11,000,000 ₫, 61 м²: нынешний район назван в карточке: Xuân Trường-Đà Lạt
  * 46289856 -- xh, 35,000,000 ₫: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 45703872 -- lv, 3,000,000 ₫, 16 м²: нынешний район назван в карточке: Lâm Viên-Đà Lạt
  * 45070260 -- xt, 25,000,000 ₫, 350 м²: нынешний район назван в карточке: Xuân Trường-Đà Lạt; перевыложено -- заменяет id 3001481 (те же фотографии)
  * 45874487 -- xt, 120,000,000 ₫, 100 м²: нынешний район назван в карточке: Xuân Trường-Đà Lạt

ОТСЕЯНО (60):
  * 46333303 -- уже на сайте
  * 46175563 -- старее 6 дней (Đăng 2 tuần trước)
  * 42512173 -- старее 6 дней (Đăng 2 tuần trước)
  * 46290937 -- старее 6 дней (Đăng 2 tuần trước)
  * 46169987 -- старее 6 дней (Đăng 12/08/2026)
  * 45874200 -- старее 6 дней (Đăng 27/06/2026)
  * 44271365 -- старее 6 дней (Đăng 08/04/2026)
  * 45228785 -- старее 6 дней (Đăng 31/03/2026)
  * 46344572 -- уже на сайте
  * 46344479 -- уже на сайте
  * 46341902 -- уже на сайте
  * 46338497 -- уже на сайте
  * 46252039 -- старее 6 дней (Đăng 3 tuần trước)
  * 46252137 -- старее 6 дней (Đăng 3 tuần trước)
  * 46252168 -- старее 6 дней (Đăng 3 tuần trước)
  * 46252216 -- старее 6 дней (Đăng 3 tuần trước)
  * 46252239 -- старее 6 дней (Đăng 3 tuần trước)
  * 46140934 -- старее 6 дней (Đăng 05/08/2026)
  * 45962440 -- старее 6 дней (Đăng 25/06/2026)
  * 45576808 -- старее 6 дней (Đăng 18/04/2026)
  * 45436230 -- старее 6 дней (Đăng 30/03/2026)
  * 46157935 -- уже на сайте
  * 46291428 -- старее 6 дней (Đăng 2 tuần trước)
  * 46267523 -- старее 6 дней (Đăng 3 tuần trước)
  * 46181403 -- старее 6 дней (Đăng 14/08/2026)
  * 46159595 -- старее 6 дней (Đăng 10/08/2026)
  * 46155722 -- старее 6 дней (Đăng 08/08/2026)
  * 41472028 -- старее 6 дней (Đăng 3 tuần trước)
  * 45648318 -- старее 6 дней (Đăng 3 tuần trước)
  * 46185034 -- старее 6 дней (Đăng 3 tuần trước)
  * 46185083 -- старее 6 дней (Đăng 3 tuần trước)
  * 46185045 -- старее 6 дней (Đăng 3 tuần trước)
  * 46185068 -- старее 6 дней (Đăng 3 tuần trước)
  * 46217397 -- старее 6 дней (Đăng 24/08/2026)
  * 45985291 -- старее 6 дней (Đăng 01/07/2026)
  * 45698255 -- старее 6 дней (Đăng 09/05/2026)
  * 45648108 -- старее 6 дней (Đăng 29/04/2026)
  * 45529165 -- старее 6 дней (Đăng 11/04/2026)
  * 45513763 -- старее 6 дней (Đăng 09/04/2026)
  * 45420454 -- старее 6 дней (Đăng 28/03/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001751, 3001752, 3001753, 3001754, 3001755]
REPLACES = [3001481]

NEW_SRC = r'''
L(3001751,"da-lat","xt","Квартира",11000000,61,
  "2-спальная квартира, 61 м², Xuân Trường - Đà Lạt — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nam-ho-phuong-11_1-sun-garden-da-lat/cho-a-theo-ngay-hoac-thang-lien-he-xem-nha-pr46175548","2 дня назад",2,source="batdongsan",postedOn="2026-09-28",
  descEn="2-bedroom flat, 61 m², Xuân Trường - Đà Lạt — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813114112-f299_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813114111-d2fb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813114111-8268_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813114111-fd28_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813114111-5520_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813114111-c9c8_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001752,"da-lat","xh","Дом",35000000,None,
  "4-спальный дом, Xuân Hương - Đà Lạt — 5 санузлов, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-an-son-391/chinh-chu-cho-biet-thu-dic-mat-tien-uong-p-04-a-lat-456-7m2-hau-18-met-pr46289856","3 дня назад",3,source="batdongsan",postedOn="2026-09-27",
  descEn="4-bedroom house, Xuân Hương - Đà Lạt — 5 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912100055-7c2a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912100141-bbe5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912100141-5885_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912100141-20a7_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/12/20260912100055-7c2a_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/12/20260912100141-bbe5_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001753,"da-lat","lv","Комната",3000000,16,
  "Комната, 16 м², Lâm Viên - Đà Lạt — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-huu-canh-391/cho-1pn-16m2-gia-2-2-trieu-tai-1-8-p8-a-lat-pr45703872","вчера",1,source="batdongsan",postedOn="2026-09-29",
  descEn="Room, 16 m², Lâm Viên - Đà Lạt — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/05/10/20260510171536-e324_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/24/20260524071944-60f4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/18/20260618145114-9b75_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/29/20260929191308-4915_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/29/20260929191311-794d_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/05/10/20260510171536-e324_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001754,"da-lat","xt","Дом",25000000,350,
  "3-спальный дом, 350 м², Xuân Trường - Đà Lạt — 3 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-nam-ho-phuong-11_1-391/cho-villa-san-vuon-da-lat-25-trieu-thang-view-thong-pr45070260","2 дня назад",2,source="batdongsan",postedOn="2026-09-28",
  descEn="3-bedroom house, 350 m², Xuân Trường - Đà Lạt — 3 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-4f13_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-ec21_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-4b26_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-0382_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-5280_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-18b0_wm.jpg"], "am": ["k"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001755,"da-lat","xt","Дом",120000000,100,
  "2-спальный дом, 100 м², Xuân Trường - Đà Lạt — 3 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-hung-vuong-2-xa-xuan-truong-1-391/cho-villa-1100m2-uong-thich-hop-kinh-doanh-hang-cao-cap-hien-trang-moi-ep-pr45874487","4 дня назад",4,source="batdongsan",postedOn="2026-09-26",
  descEn="2-bedroom house, 100 m², Xuân Trường - Đà Lạt — 3 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608112934-7ec2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608112934-2b7a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608112934-1a2f_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/06/08/20260608112934-7ec2_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/06/08/20260608112934-2b7a_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/06/08/20260608112934-1a2f_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
