# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 14 строк, 2026-09-21, город can-tho.

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
  * 46325290 -- crg, 15,000,000 ₫, 49 м²: нынешний район назван в карточке: Cái Răng
  * 46248987 -- hpu, 6,000,000 ₫, 50 м²: квартал в адресе объявления: hung phu
  * 46324638 -- crg, 12,000,000 ₫: нынешний район назван в карточке: Cái Răng
  * 46321901 -- crg, 4,000,000 ₫, 38 м²: нынешний район назван в карточке: Cái Răng
  * 46321419 -- crg, 5,000,000 ₫, 44 м²: нынешний район назван в карточке: Cái Răng
  * 46315918 -- crg, 6,000,000 ₫, 38 м²: нынешний район назван в карточке: Cái Răng
  * 46137015 -- hpu, 5,000,000 ₫, 66 м²: квартал в адресе объявления: hung phu
  * 46269381 -- crg, 12,000,000 ₫, 69 м²: нынешний район назван в карточке: Cái Răng
  * 46324959 -- crg, 15,000,000 ₫, 350 м²: нынешний район назван в карточке: Cái Răng
  * 45892878 -- hpu, 20,000,000 ₫, 480 м²: квартал в адресе объявления: hung phu
  * 46323010 -- crg, 5,000,000 ₫, 80 м²: нынешний район назван в карточке: Cái Răng
  * 46292636 -- tanc, 16,000,000 ₫, 90 м²: квартал в адресе объявления: tan an
  * 42375396 -- crg, 8,000,000 ₫, 28 м²: нынешний район назван в карточке: Cái Răng
  * 45920226 -- hpu, 16,000,000 ₫, 204 м²: нынешний район назван в карточке: Hưng Phú

ОТСЕЯНО (64):
  * 46307326 -- уже на сайте
  * 45655118 -- уже на сайте
  * 45614225 -- похоже на уже заведённое: id 3000920
  * 46211409 -- уже на сайте
  * 45987974 -- похоже на уже заведённое: id 1007541
  * 45988341 -- похоже на уже заведённое: id 1007541
  * 46323362 -- похоже на уже заведённое: id 1008516
  * 45457221 -- уже на сайте
  * 46318246 -- похоже на уже заведённое: id 1005143
  * 46320410 -- похоже на уже заведённое: id 1008516
  * 46111709 -- уже на сайте
  * 46044677 -- похоже на уже заведённое: id 1005148
  * 46292031 -- похоже на уже заведённое: id 1006205
  * 44540093 -- похоже на уже заведённое: id 1008112
  * 46007565 -- похоже на уже заведённое: id 1004501
  * 46303903 -- уже на сайте
  * 46196000 -- похоже на уже заведённое: id 1004609
  * 46304069 -- похоже на уже заведённое: id 1005178
  * 46304057 -- уже на сайте
  * 46299818 -- уже на сайте
  * 46295364 -- уже на сайте
  * 46293464 -- старее 6 дней (Đăng 1 tuần trước)
  * 46289836 -- старее 6 дней (Đăng 1 tuần trước)
  * 46284490 -- старее 6 дней (Đăng 1 tuần trước)
  * 46282502 -- старее 6 дней (Đăng 1 tuần trước)
  * 46216136 -- старее 6 дней (Đăng 1 tuần trước)
  * 46243641 -- старее 6 дней (Đăng 1 tuần trước)
  * 45595974 -- старее 6 дней (Đăng 21/04/2026)
  * 45579525 -- уже на сайте
  * 46306970 -- уже на сайте
  * 39577249 -- старее 6 дней (Đăng 1 tuần trước)
  * 44385985 -- старее 6 дней (Đăng 1 tuần trước)
  * 41138517 -- старее 6 дней (Đăng 1 tuần trước)
  * 44385918 -- старее 6 дней (Đăng 1 tuần trước)
  * 39563308 -- старее 6 дней (Đăng 1 tuần trước)
  * 40290344 -- старее 6 дней (Đăng 1 tuần trước)
  * 40290347 -- старее 6 дней (Đăng 1 tuần trước)
  * 42096008 -- старее 6 дней (Đăng 1 tuần trước)
  * 45651391 -- старее 6 дней (Đăng 3 tuần trước)
  * 46217775 -- старее 6 дней (Đăng 1 tháng trước)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001141, 3001142, 3001143, 3001144, 3001145, 3001146, 3001147, 3001148, 3001149, 3001150, 3001151, 3001152, 3001153, 3001154]
REPLACES = []

NEW_SRC = r'''
L(3001141,"can-tho","crg","Квартира",15000000,49,
  "2-спальная квартира, 49 м², Cái Răng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/cho-2pn-49m-noi-that-cao-cap-sang-trong-park-pr46325290","сегодня",0,source="batdongsan",postedOn="2026-09-21",
  descEn="2-bedroom flat, 49 m², Cái Răng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921113623-8c5e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921113623-805f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921113623-b3e5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921113623-e1b2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921113623-b7ce_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921113623-3107_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001142,"can-tho","hpu","Квартира",6000000,50,
  "2-спальная квартира, 50 м², Hưng Phú — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-phu/cho-lo-a-lau-1-50m2-2pn-full-noi-that-pr46248987","сегодня",0,source="batdongsan",postedOn="2026-09-21",
  descEn="2-bedroom flat, 50 m², Hưng Phú — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212746-42e7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212745-d627_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212745-e549_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212746-0dca_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212747-b8a6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212747-eea3_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001143,"can-tho","crg","Квартира",12000000,None,
  "2-спальная квартира, Cái Răng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/cho-2pn-1-wc-tp-tho-pr46324638","сегодня",0,source="batdongsan",postedOn="2026-09-21",
  descEn="2-bedroom flat, Cái Răng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921102519-febc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921102520-77b9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921102521-817f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921102522-2b5e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921102522-6afd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921102523-2497_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001144,"can-tho","crg","Квартира",4000000,38,
  "1-спальная квартира, 38 м², Cái Răng — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-2-38m2-moi-100-tang-6-thang-may-boi-san-pickleball-pr46321901","сегодня",0,source="batdongsan",postedOn="2026-09-21",
  descEn="1-bedroom flat, 38 m², Cái Răng — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920104034-0683_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920104036-4b49_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920104038-6924_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920104040-1c9e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920104041-79bd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920104043-e089_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001145,"can-tho","crg","Квартира",5000000,44,
  "Квартира, 44 м², Cái Răng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-lake-pr46321419","вчера",1,source="batdongsan",postedOn="2026-09-20",
  descEn="Flat, 44 m², Cái Răng.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920045425-56d4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920045425-295b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920045425-4373_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920045425-d3cf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920045425-adde_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920045425-4244_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001146,"can-tho","crg","Квартира",6000000,38,
  "1-спальная квартира, 38 м², Cái Răng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-2-38m2-full-noi-that-moi-100-thang-may-ep-gia-re-pr46315918","3 дня назад",3,source="batdongsan",postedOn="2026-09-18",
  descEn="1-bedroom flat, 38 m², Cái Răng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918132048-9a59_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918132049-2b3b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918132050-dbf7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918132051-13e0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918132051-ed9e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918132052-87ab_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001147,"can-tho","hpu","Квартира",5000000,66,
  "2-спальная квартира, 66 м², Hưng Phú — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-quang-trung-phuong-hung-phu-khu-do-thi-moi-hung-phu-can-tho/cho-70m2-2-phong-ngu-2-may-lanh-thang-may-son-sua-bai-xe-pr46137015","3 дня назад",3,source="batdongsan",postedOn="2026-09-18",
  descEn="2-bedroom flat, 66 m², Hưng Phú — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913170429-ba70_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913170430-a182_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913170430-9305_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913170431-f9b3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913170432-1ab6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913170433-5824_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001148,"can-tho","crg","Квартира",12000000,69,
  "3-спальная квартира, 69 м², Cái Răng — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-2-69m2-3-phong-ngu-2wc-full-noi-that-canh-quan-pr46269381","3 дня назад",3,source="batdongsan",postedOn="2026-09-18",
  descEn="3-bedroom flat, 69 m², Cái Răng — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907225138-f64d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907225138-8338_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907225140-006d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907225141-bbaa_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907225142-0cdf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907225142-aa4d_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001149,"can-tho","crg","Дом",15000000,350,
  "5-спальный дом, 350 м², Cái Răng — 4 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-hung-thanh-khu-dan-cu-hong-loan/cho-tret-3-lau-moi-ep-san-noi-that-kdc-5c-can-tho-15-trieu-pr46324959","сегодня",0,source="batdongsan",postedOn="2026-09-21",
  descEn="5-bedroom house, 350 m², Cái Răng — 4 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921110046-e24e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921110045-1cbd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921110046-70e2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921110046-da23_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921110046-248c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/21/20260921110045-0cd6_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001150,"can-tho","hpu","Дом",20000000,480,
  "5-спальный дом, 480 м², Hưng Phú — 5 санузлов, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ly-thai-to-phuong-hung-phu-82/cho-tret-3-lau-moi-ep-vi-tri-au-khu-truc-chinh-kdc-can-tho-30-trieu-pr45892878","сегодня",0,source="batdongsan",postedOn="2026-09-21",
  descEn="5-bedroom house, 480 m², Hưng Phú — 5 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/06/11/20260611104031-7165_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/11/20260611104032-bc77_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/11/20260611104032-c4c0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/11/20260611104031-235b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/11/20260611104032-ec52_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/11/20260611104032-3cda_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001151,"can-tho","crg","Дом",5000000,80,
  "3-спальный дом, 80 м², Cái Răng — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-hung-thanh-khu-dan-cu-hong-loan/cho-1-tret-1-lau-rong-thuan-tien-o-kinh-doanh-vp-cong-ty-ngay-kdc-loan-pr46323010","вчера",1,source="batdongsan",postedOn="2026-09-20",
  descEn="3-bedroom house, 80 m², Cái Răng — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920191420-143a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920191419-3076_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920191418-70d5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920191420-7fb9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920191421-855f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920191421-0cb9_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001152,"can-tho","tanc","Дом",16000000,90,
  "4-спальный дом, 90 м², Tân An — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-tan-an-1/nha1-tret-2-lau-vi-tri-kinh-doanh-vp-cong-ty-lo-20m-co-4-p-ngu-rong-cach-truong-h-y-duoc-900m-pr46292636","3 дня назад",3,source="batdongsan",postedOn="2026-09-18",
  descEn="4-bedroom house, 90 m², Tân An — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/18/20260918142308-5c5f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085048-7025_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085051-6ce3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085053-3236_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085055-88a8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914150711-bfe5_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001153,"can-tho","crg","Комната",8000000,28,
  "Комната, 28 м², Cái Răng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-so-20-phuong-hung-thanh-82/cho-co-gac-moi-100-full-noi-that-co-san-vuon-pr42375396","6 дней назад",6,source="batdongsan",postedOn="2026-09-15",
  descEn="Room, 28 m², Cái Răng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/03/09/20250309144544-d201_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/09/20250309144543-45b8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/09/20250309144544-c0d8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/09/20250309144543-c8c5_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2025/03/09/20250309144544-d201_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2025/03/09/20250309144543-45b8_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001154,"can-tho","hpu","Дом",16000000,204,
  "9-спальный дом, 204 м², Hưng Phú — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-lam-van-phan-phuong-phu-thu-khu-dan-cu-phu-an/cho-co-san-rong-gan-xe-ford-tien-phong-16-trieu-pr45920226","3 дня назад",3,source="batdongsan",postedOn="2026-09-18",
  descEn="9-bedroom house, 204 m², Hưng Phú — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201917-8ef6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201921-a485_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201927-ecc7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201927-de06_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201933-5915_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201933-8c86_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
