# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 7 строк, 2026-09-26, город da-lat.

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
  * 46333303 -- xh, 13,000,000 ₫, 88 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46157935 -- xt, 27,000,000 ₫, 450 м²: нынешний район назван в карточке: Xuân Trường-Đà Lạt
  * 46344572 -- xh, 80,000,000 ₫, 135 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46344479 -- xh, 25,000,000 ₫: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46341902 -- xt, 11,000,000 ₫, 168 м²: нынешний район назван в карточке: Xuân Trường-Đà Lạt
  * 46338497 -- cl, 7,000,000 ₫, 60 м²: нынешний район назван в карточке: Cam Ly-Đà Lạt
  * 46333317 -- xh, 60,000,000 ₫, 330 м²: квартал в адресе объявления: phuong 1

ОТСЕЯНО (62):
  * 46175563 -- старее 6 дней (Đăng 1 tuần trước)
  * 42512173 -- старее 6 дней (Đăng 1 tuần trước)
  * 46175548 -- старее 6 дней (Đăng 1 tuần trước)
  * 46290937 -- старее 6 дней (Đăng 2 tuần trước)
  * 46169987 -- старее 6 дней (Đăng 12/08/2026)
  * 45874200 -- старее 6 дней (Đăng 27/06/2026)
  * 44271365 -- старее 6 дней (Đăng 08/04/2026)
  * 45228785 -- старее 6 дней (Đăng 31/03/2026)
  * 45347154 -- старее 6 дней (Đăng 19/03/2026)
  * 45334210 -- старее 6 дней (Đăng 17/03/2026)
  * 45317373 -- старее 6 дней (Đăng 16/03/2026)
  * 46318499 -- уже на сайте
  * 46246761 -- старее 6 дней (Đăng 1 tuần trước)
  * 46291428 -- старее 6 дней (Đăng 2 tuần trước)
  * 46289856 -- старее 6 дней (Đăng 2 tuần trước)
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
  * 45703872 -- старее 6 дней (Đăng 18/06/2026)
  * 41472028 -- старее 6 дней (Đăng 2 tuần trước)
  * 45648318 -- старее 6 дней (Đăng 2 tuần trước)
  * 46185034 -- старее 6 дней (Đăng 2 tuần trước)
  * 46185083 -- старее 6 дней (Đăng 2 tuần trước)
  * 46185045 -- старее 6 дней (Đăng 2 tuần trước)
  * 46185068 -- старее 6 дней (Đăng 2 tuần trước)
  * 46217397 -- старее 6 дней (Đăng 24/08/2026)
  * 45985291 -- старее 6 дней (Đăng 01/07/2026)
  * 45698255 -- старее 6 дней (Đăng 09/05/2026)
  * 45648108 -- старее 6 дней (Đăng 29/04/2026)
  * 45529165 -- старее 6 дней (Đăng 11/04/2026)
  * 45513763 -- старее 6 дней (Đăng 09/04/2026)
  * 45420454 -- старее 6 дней (Đăng 28/03/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001480, 3001481, 3001482, 3001483, 3001484, 3001485, 3001486]
REPLACES = []

NEW_SRC = r'''
L(3001480,"da-lat","xh","Квартира",13000000,88,
  "2-спальная квартира, 88 м², Xuân Hương - Đà Lạt — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-10_4-the-panorama-da-lat/cao-cap-2-phong-trung-tam-a-ao-pr46333303","3 дня назад",3,source="batdongsan",postedOn="2026-09-23",
  descEn="2-bedroom flat, 88 m², Xuân Hương - Đà Lạt — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083116-b47e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083114-5e75_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083115-6991_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083114-73c7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083116-4c5a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083117-33c7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001481,"da-lat","xt","Дом",27000000,450,
  "5-спальный дом, 450 м², Xuân Trường - Đà Lạt — 6 санузлов, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-hung-vuong-2-phuong-11_1-391/villa-a-lat-view-thong-dt-450m2-3-phong-ngu-khach-bep-3-wc-st-pr46157935","вчера",1,source="batdongsan",postedOn="2026-09-25",
  descEn="5-bedroom house, 450 m², Xuân Trường - Đà Lạt — 6 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-4f13_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-4b26_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-0382_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095108-5280_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/01/21/20260121095109-5930_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/01/21/20260121095108-4f13_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001482,"da-lat","xh","Дом",80000000,135,
  "8-спальный дом, 135 м², Xuân Hương - Đà Lạt — 9 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-pham-hong-thai-phuong-10_4-391/can-goc-8pn-gan-ho-xuan-huong-pr46344572","вчера",1,source="batdongsan",postedOn="2026-09-25",
  descEn="8-bedroom house, 135 m², Xuân Hương - Đà Lạt — 9 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925142749-337d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925142740-ba42_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925142741-504b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925142742-82b2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925142744-dca4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925142747-8760_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001483,"da-lat","xh","Дом",25000000,None,
  "5-спальный дом, Xuân Hương - Đà Lạt — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-phan-dinh-phung-phuong-2_3-391/inh-5pn-moi-phu-hop-o-gia-inh-pr46344479","вчера",1,source="batdongsan",postedOn="2026-09-25",
  descEn="5-bedroom house, Xuân Hương - Đà Lạt — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925141550-ad90_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925141551-c929_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925141551-3265_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925141552-ebf1_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/25/20260925141550-ad90_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/25/20260925141551-c929_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001484,"da-lat","xt","Дом",11000000,168,
  "2-спальный дом, 168 м², Xuân Trường - Đà Lạt — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-trinh-hoai-duc-phuong-11_1-391/can-cho-ep-uong-uc-xuan-truong-a-lat-pr46341902","2 дня назад",2,source="batdongsan",postedOn="2026-09-24",
  descEn="2-bedroom house, 168 m², Xuân Trường - Đà Lạt — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924204842-fdcb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924204840-c6c7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924204840-2d11_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924204840-762d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924204841-a15c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924204841-8e22_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001485,"da-lat","cl","Дом",7000000,60,
  "1-спальный дом, 60 м², Cam Ly - Đà Lạt — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-mai-hac-de-phuong-5_3-391/cho-tai-cam-ly-a-lat-dt-60m2-san-rong-view-ep-gia-7tr-thang-pr46338497","2 дня назад",2,source="batdongsan",postedOn="2026-09-24",
  descEn="1-bedroom house, 60 m², Cam Ly - Đà Lạt — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093404-824d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093405-62ac_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093407-908f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093409-2bb5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093412-c453_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093415-e6e3_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001486,"da-lat","xh","Дом",60000000,330,
  "9-спальный дом, 330 м², Xuân Hương - Đà Lạt — 9 санузлов, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-bui-thi-xuan-phuong-phuong-1-5-391/villa-cao-cap-ngay-ho-huong-a-lat-pr46333317","3 дня назад",3,source="batdongsan",postedOn="2026-09-23",
  descEn="9-bedroom house, 330 m², Xuân Hương - Đà Lạt — 9 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083516-3da4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083517-3c06_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083518-eaf4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083519-ccb7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083519-428b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083520-fb84_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
