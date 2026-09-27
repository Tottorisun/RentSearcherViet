# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 10 строк, 2026-09-27, город can-tho.

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
  * 46348832 -- crg, 10,000,000 ₫, 37 м²: нынешний район назван в карточке: Cái Răng
  * 46307450 -- crg, 14,000,000 ₫, 53 м²: нынешний район назван в карточке: Cái Răng
  * 45457221 -- crg, 8,000,000 ₫, 70 м²: нынешний район назван в карточке: Cái Răng
  * 46343781 -- crg, 12,000,000 ₫, 69 м²: нынешний район назван в карточке: Cái Răng
  * 46346577 -- tanc, 9,000,000 ₫, 140 м²: нынешний район назван в карточке: Tân An
  * 46292031 -- hpu, 13,000,000 ₫, 72 м²: квартал в адресе объявления: hung phu
  * 46348240 -- ltu, 9,000,000 ₫, 39 м²: квартал в адресе объявления: long tuyen
  * 44385918 -- anb, 8,000,000 ₫, 33 м²: квартал в адресе объявления: an binh
  * 44385985 -- anb, 2,000,000 ₫, 33 м²: квартал в адресе объявления: an binh
  * 45920226 -- hpu, 16,000,000 ₫, 204 м²: нынешний район назван в карточке: Hưng Phú

ОТСЕЯНО (67):
  * 45655118 -- уже на сайте
  * 46325290 -- уже на сайте
  * 45614225 -- уже на сайте
  * 46343707 -- похоже на уже заведённое: id 3001145
  * 46343438 -- похоже на уже заведённое: id 3001143
  * 46342920 -- уже на сайте
  * 46340222 -- похоже на уже заведённое: id 1009466
  * 46339331 -- уже на сайте
  * 46338548 -- похоже на уже заведённое: id 1014562
  * 46336091 -- уже на сайте
  * 46335240 -- похоже на уже заведённое: id 3001374
  * 46307326 -- уже на сайте
  * 46305504 -- похоже на уже заведённое: id 3001373
  * 46211409 -- уже на сайте
  * 45987974 -- похоже на уже заведённое: id 1014562
  * 46324638 -- уже на сайте
  * 45948985 -- уже на сайте
  * 46328304 -- похоже на уже заведённое: id 1008950
  * 46324959 -- уже на сайте
  * 45892878 -- уже на сайте
  * 46323010 -- уже на сайте
  * 44540093 -- старее 6 дней (Đăng 1 tuần trước)
  * 46007565 -- старее 6 дней (Đăng 1 tuần trước)
  * 46295364 -- старее 6 дней (Đăng 1 tuần trước)
  * 46284490 -- старее 6 дней (Đăng 2 tuần trước)
  * 46243641 -- старее 6 дней (Đăng 2 tuần trước)
  * 45595974 -- старее 6 дней (Đăng 21/04/2026)
  * 46292636 -- старее 6 дней (Đăng 1 tuần trước)
  * 46303903 -- старее 6 дней (Đăng 1 tuần trước)
  * 46196000 -- старее 6 дней (Đăng 1 tuần trước)
  * 46304069 -- старее 6 дней (Đăng 1 tuần trước)
  * 46304057 -- старее 6 дней (Đăng 1 tuần trước)
  * 46299818 -- старее 6 дней (Đăng 1 tuần trước)
  * 46293464 -- старее 6 дней (Đăng 2 tuần trước)
  * 45651391 -- похоже на уже заведённое: id 1011864
  * 42375396 -- старее 6 дней (Đăng 1 tuần trước)
  * 39577249 -- старее 6 дней (Đăng 2 tuần trước)
  * 41138517 -- старее 6 дней (Đăng 2 tuần trước)
  * 45579525 -- старее 6 дней (Đăng 1 tuần trước)
  * 46306970 -- старее 6 дней (Đăng 1 tuần trước)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001559, 3001560, 3001561, 3001562, 3001563, 3001564, 3001565, 3001566, 3001567, 3001568]
REPLACES = []

NEW_SRC = r'''
L(3001559,"can-tho","crg","Квартира",10000000,37,
  "1-спальная квартира, 37 м², Cái Răng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/cho-1pn-park-pr46348832","вчера",1,source="batdongsan",postedOn="2026-09-26",
  descEn="1-bedroom flat, 37 m², Cái Răng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926171016-3bed_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926171016-244f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926171016-2887_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926171016-9eae_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926171016-559c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926171016-e496_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001560,"can-tho","crg","Квартира",14000000,53,
  "2-спальная квартира, 53 м², Cái Răng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/cho-2pn-noi-that-cao-cap-park-pr46307450","вчера",1,source="batdongsan",postedOn="2026-09-26",
  descEn="2-bedroom flat, 53 m², Cái Răng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916153134-8561_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916153133-ba53_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916153134-58ef_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916153134-aadc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916153134-202e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916153134-1335_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001561,"can-tho","crg","Квартира",8000000,70,
  "2-спальная квартира, 70 м², Cái Răng — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/chi-5-trieu-thang-don-vao-o-ngay-so-huu-view-truc-dien-cau-tho-song-hau-trung-tam-chill-pr45457221","2 дня назад",2,source="batdongsan",postedOn="2026-09-25",
  descEn="2-bedroom flat, 70 m², Cái Răng — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/04/02/20260402094657-0930_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/02/20260402094655-9074_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/02/20260402094655-33d3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/02/20260402094655-2626_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/02/20260402094655-6388_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/02/20260402094656-80e4_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001562,"can-tho","crg","Квартира",12000000,69,
  "3-спальная квартира, 69 м², Cái Răng — 3 санузла.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-3-phong-ngu-pr46343781","2 дня назад",2,source="batdongsan",postedOn="2026-09-25",
  descEn="3-bedroom flat, 69 m², Cái Răng — 3 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925112606-df8a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925112606-d461_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925112606-5aa0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925112606-cc55_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925112606-92d4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925112607-2393_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001563,"can-tho","tanc","Дом",9000000,140,
  "Дом, 140 м², Tân An.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-b10-phuong-an-khanh-1-83/cho-1-lau-kdc-91b-tien-van-phong-9-trieu-pr46346577","вчера",1,source="batdongsan",postedOn="2026-09-26",
  descEn="House, 140 m², Tân An.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926072436-0bf7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926072442-2ff7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926072447-79fd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926072447-8568_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926072447-c4b6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926072447-440b_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001564,"can-tho","hpu","Дом",13000000,72,
  "4-спальный дом, 72 м², Hưng Phú — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-b4-phuong-hung-phu-82/cho-1-tret-2-lau-kdc-phu-pr46292031","6 дней назад",6,source="batdongsan",postedOn="2026-09-21",
  descEn="4-bedroom house, 72 m², Hưng Phú — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912201920-728d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912201921-081a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912201922-ec6b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912201923-ad9a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912201924-2afd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912201925-8694_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001565,"can-tho","ltu","Комната",9000000,39,
  "Комната, 39 м², Long Tuyền — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-van-cu-1-phuong-long-tuyen-81/cho-can-ho-minihouse-khu-bv-nhi-ong-full-noi-that-gia-tot-pr46348240","вчера",1,source="batdongsan",postedOn="2026-09-26",
  descEn="Room, 39 m², Long Tuyền — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926144944-c9ac_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926144944-6571_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926144945-43b1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926144946-6507_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926144947-7209_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926144948-f855_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001566,"can-tho","anb","Комната",8000000,33,
  "Комната, 33 м², An Bình — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-van-cu-1-phuong-an-binh-2-83/cho-mini-house-moi-xay-can-co-gac-full-tien-nghi-cach-dai-hoc-nam-can-tho-800m-pr44385918","вчера",1,source="batdongsan",postedOn="2026-09-26",
  descEn="Room, 33 m², An Bình — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/11/05/20251105113207-9959_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/11/05/20251105113204-bb0c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/11/05/20251105113211-9994_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/11/05/20251105113220-6944_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/11/05/20251105113223-320d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/11/21/20251121133119-f37b_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001567,"can-tho","anb","Комната",2000000,33,
  "Комната, 33 м², An Bình — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-van-cu-1-phuong-an-binh-2-83/cho-mini-house-moi-xay-can-co-gac-full-tien-nghi-cach-dai-hoc-nam-can-tho-800m-pr44385985","вчера",1,source="batdongsan",postedOn="2026-09-26",
  descEn="Room, 33 m², An Bình — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/03/19/20260319095203-3cc3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/03/19/20260319095134-df7c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/03/19/20260319095137-732a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/03/19/20260319095139-9445_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/03/19/20260319095141-5565_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/03/19/20260319095142-9cca_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001568,"can-tho","hpu","Дом",16000000,204,
  "9-спальный дом, 204 м², Hưng Phú — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-lam-van-phan-phuong-phu-thu-khu-dan-cu-phu-an/cho-co-san-rong-gan-xe-ford-tien-phong-16-trieu-pr45920226","4 дня назад",4,source="batdongsan",postedOn="2026-09-23",
  descEn="9-bedroom house, 204 m², Hưng Phú — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201917-8ef6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201921-a485_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201927-ecc7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201927-de06_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201933-5915_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/16/20260616201933-8c86_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
