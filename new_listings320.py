# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 9 строк, 2026-09-25, город can-tho.

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
  * 46342920 -- crg, 9,000,000 ₫, 57 м²: нынешний район назван в карточке: Cái Răng
  * 45655118 -- crg, 8,000,000 ₫, 75 м²: нынешний район назван в карточке: Cái Răng
  * 46010917 -- crg, 14,000,000 ₫, 70 м²: нынешний район назван в карточке: Cái Răng
  * 45614225 -- crg, 15,000,000 ₫, 74 м²: нынешний район назван в карточке: Cái Răng
  * 46339331 -- crg, 9,000,000 ₫, 66 м²: нынешний район назван в карточке: Cái Răng
  * 46336091 -- crg, 15,000,000 ₫, 31 м²: нынешний район назван в карточке: Cái Răng
  * 46307326 -- crg, 9,000,000 ₫, 70 м²: нынешний район назван в карточке: Cái Răng
  * 46211409 -- hpu, 5,000,000 ₫, 70 м²: квартал в адресе объявления: hung phu
  * 45948985 -- crg, 9,000,000 ₫, 85 м²: нынешний район назван в карточке: Cái Răng

ОТСЕЯНО (68):
  * 46343781 -- похоже на уже заведённое: id 3001148
  * 46343707 -- похоже на уже заведённое: id 3001145
  * 46343438 -- похоже на уже заведённое: id 3001143
  * 46340222 -- похоже на уже заведённое: id 1009466
  * 46325290 -- уже на сайте
  * 46338548 -- похоже на уже заведённое: id 1007541
  * 46335240 -- похоже на уже заведённое: id new:46339331
  * 46305504 -- похоже на уже заведённое: id new:45614225
  * 45987974 -- похоже на уже заведённое: id 1007541
  * 46324638 -- уже на сайте
  * 46321901 -- уже на сайте
  * 46323362 -- похоже на уже заведённое: id 1008516
  * 46328304 -- похоже на уже заведённое: id 1008950
  * 46324959 -- уже на сайте
  * 45892878 -- уже на сайте
  * 46323010 -- уже на сайте
  * 44540093 -- похоже на уже заведённое: id 1008112
  * 46007565 -- старее 6 дней (Đăng 1 tuần trước)
  * 46303903 -- старее 6 дней (Đăng 1 tuần trước)
  * 46196000 -- старее 6 дней (Đăng 1 tuần trước)
  * 46304069 -- старее 6 дней (Đăng 1 tuần trước)
  * 46304057 -- старее 6 дней (Đăng 1 tuần trước)
  * 46295364 -- старее 6 дней (Đăng 1 tuần trước)
  * 46284490 -- старее 6 дней (Đăng 2 tuần trước)
  * 46243641 -- старее 6 дней (Đăng 2 tuần trước)
  * 45595974 -- старее 6 дней (Đăng 21/04/2026)
  * 46292031 -- похоже на уже заведённое: id 1009536
  * 46292636 -- уже на сайте
  * 46299818 -- старее 6 дней (Đăng 1 tuần trước)
  * 46293464 -- старее 6 дней (Đăng 1 tuần trước)
  * 46050142 -- старее 6 дней (Đăng 1 tuần trước)
  * 45651391 -- похоже на уже заведённое: id 1011864
  * 46306970 -- старее 6 дней (Đăng 1 tuần trước)
  * 42375396 -- старее 6 дней (Đăng 1 tuần trước)
  * 39577249 -- старее 6 дней (Đăng 1 tuần trước)
  * 41138517 -- старее 6 дней (Đăng 2 tuần trước)
  * 45579525 -- старее 6 дней (Đăng 1 tuần trước)
  * 44385985 -- старее 6 дней (Đăng 2 tuần trước)
  * 39563308 -- старее 6 дней (Đăng 2 tuần trước)
  * 40290344 -- старее 6 дней (Đăng 2 tuần trước)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001370, 3001371, 3001372, 3001373, 3001374, 3001375, 3001376, 3001377, 3001378]
REPLACES = []

NEW_SRC = r'''
L(3001370,"can-tho","crg","Квартира",9000000,57,
  "2-спальная квартира, 57 м², Cái Răng — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-2-pn-khu-2-lake-pr46342920","сегодня",0,source="batdongsan",postedOn="2026-09-25",
  descEn="2-bedroom flat, 57 m², Cái Răng — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925093245-1916_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925093245-9927_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925093245-6049_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925093245-f929_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925093245-18f1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925093245-91ce_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001371,"can-tho","crg","Квартира",8000000,75,
  "2-спальная квартира, 75 м², Cái Răng — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/chinh-chu-cho-cao-cap-thong-minh-cho-ngay-tuan-thang-hoac-dai-han-pr45655118","сегодня",0,source="batdongsan",postedOn="2026-09-25",
  descEn="2-bedroom flat, 75 m², Cái Răng — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/05/02/20260502110134-ceb9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/02/20260502110133-00eb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/02/20260502110133-c62d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/02/20260502110133-08a9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/02/20260502110133-3a36_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/02/20260502110133-5b45_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001372,"can-tho","crg","Квартира",14000000,70,
  "2-спальная квартира, 70 м², Cái Răng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/chi-hon-10-ban-uoc-2pn-ngay-trung-tam-pr46010917","вчера",1,source="batdongsan",postedOn="2026-09-24",
  descEn="2-bedroom flat, 70 m², Cái Răng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083406-bdbe_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083406-7ecf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083406-2a85_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083406-bc6b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083406-0e14_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923083406-60b7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001373,"can-tho","crg","Квартира",15000000,74,
  "2-спальная квартира, 74 м², Cái Răng — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/chinh-chu-cho-2pn-chi-tu-7trieu-view-cuc-chill-truc-dien-cau-tho-pr45614225","вчера",1,source="batdongsan",postedOn="2026-09-24",
  descEn="2-bedroom flat, 74 m², Cái Răng — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914102918-1eb5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914102918-d072_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/23/20260423151455-5de6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/23/20260423151454-f172_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/23/20260423151454-abd8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/23/20260423151454-8e84_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001374,"can-tho","crg","Квартира",9000000,66,
  "2-спальная квартира, 66 м², Cái Răng — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-66m2-2pn-pr46339331","вчера",1,source="batdongsan",postedOn="2026-09-24",
  descEn="2-bedroom flat, 66 m², Cái Răng — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924110026-aab7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924110027-0fce_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924110028-0c09_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924110033-2198_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924110030-2cda_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924110026-e918_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001375,"can-tho","crg","Квартира",15000000,31,
  "2-спальная квартира, 31 м², Cái Răng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/cho-2pn-full-noi-that-pr46336091","2 дня назад",2,source="batdongsan",postedOn="2026-09-23",
  descEn="2-bedroom flat, 31 m², Cái Răng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923150842-5cbe_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923150842-c5b9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923150842-235e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923150842-2b8a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923150842-b1e7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923150842-e28a_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001376,"can-tho","crg","Квартира",9000000,70,
  "2-спальная квартира, 70 м², Cái Răng — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/chinh-chu-cho-2pn-9tr-thang-tai-don-vao-o-ngay-tam-view-cau-tho-pr46307326","3 дня назад",3,source="batdongsan",postedOn="2026-09-22",
  descEn="2-bedroom flat, 70 m², Cái Răng — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916151351-3949_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916151351-c34a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916151351-c085_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916151358-d959_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916151359-86ab_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916151409-8854_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001377,"can-tho","hpu","Квартира",5000000,70,
  "2-спальная квартира, 70 м², Hưng Phú — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-quang-trung-phuong-hung-phu-khu-do-thi-moi-hung-phu-can-tho/cho-phu-pr46211409","4 дня назад",4,source="batdongsan",postedOn="2026-09-21",
  descEn="2-bedroom flat, 70 m², Hưng Phú — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/21/20260821150931-4af7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/21/20260821150932-f171_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/21/20260821150932-1c0e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/21/20260821150932-584a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/21/20260821150932-4f25_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/21/20260821150931-4af7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001378,"can-tho","crg","Дом",9000000,85,
  "3-спальный дом, 85 м², Cái Răng — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-hung-thanh-khu-dan-cu-hong-loan/cho-1-tret-1-lau-kdc-6a-3-phong-ngu-3-may-lanh-full-ban-ghe-lam-viec-b-pr45948985","3 дня назад",3,source="batdongsan",postedOn="2026-09-22",
  descEn="3-bedroom house, 85 m², Cái Răng — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/06/23/20260623103610-4b59_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820182413-1faa_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820182416-0080_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820182418-86ee_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820182421-fbcf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820182424-ca3c_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
