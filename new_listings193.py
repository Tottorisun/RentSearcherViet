# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 10 строк, 2026-09-13, город nha-trang.

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
  * 46269065 -- btr, 16,000,000 ₫, 50 м²: квартал в адресе объявления: vinh hoa
  * 46248208 -- lt, 25,000,000 ₫: квартал в адресе объявления: loc tho
  * 46293053 -- pl, 11,000,000 ₫, 68 м²: квартал в адресе объявления: phuoc long
  * 46293031 -- ttr, 10,000,000 ₫, 70 м²: нынешний район назван в карточке: Tây Nha Trang
  * 46288910 -- ph, 8,000,000 ₫, 70 м²: квартал в адресе объявления: phuoc hai
  * 46288474 -- ph, 7,000,000 ₫, 58 м²: квартал в адресе объявления: phuoc hai
  * 46288195 -- lt, 22,000,000 ₫, 70 м²: квартал в адресе объявления: loc tho
  * 46292987 -- ph, 18,000,000 ₫, 85 м²: квартал в адресе объявления: phuoc hai
  * 46290661 -- ph, 25,000,000 ₫, 100 м²: квартал в адресе объявления: phuoc hai
  * 46288332 -- pl, 30,000,000 ₫, 150 м²: квартал в адресе объявления: phuoc long

ОТСЕЯНО (70):
  * 46288179 -- уже на сайте
  * 46280519 -- уже на сайте
  * 46072068 -- похоже на уже заведённое: id new:45311980
  * 46281273 -- уже на сайте
  * 44799071 -- цена не читается: Giá thỏa thuận
  * 46277948 -- уже на сайте
  * 36305984 -- похоже на уже заведённое: id new:45311987
  * 46245334 -- уже на сайте
  * 46290772 -- уже на сайте
  * 46290679 -- похоже на уже заведённое: id 1001734
  * 46232767 -- уже на сайте
  * 46270804 -- уже на сайте
  * 46287941 -- уже на сайте
  * 46126836 -- похоже на уже заведённое: id 2000641
  * 46285356 -- уже на сайте
  * 46265325 -- уже на сайте
  * 46282096 -- уже на сайте
  * 46281577 -- похоже на уже заведённое: id 1001734
  * 46279408 -- похоже на уже заведённое: id 1001732
  * 46220785 -- похоже на уже заведённое: id 2000646
  * 45790525 -- лимит прогона выбран
  * 46162044 -- лимит прогона выбран
  * 41253160 -- лимит прогона выбран
  * 45114842 -- старее 13 дней (Đăng 07/08/2026)
  * 45165973 -- старее 13 дней (Đăng 02/08/2026)
  * 46071290 -- старее 13 дней (Đăng 20/07/2026)
  * 45028767 -- старее 13 дней (Đăng 08/07/2026)
  * 45979935 -- старее 13 дней (Đăng 30/06/2026)
  * 43211408 -- старее 13 дней (Đăng 17/06/2026)
  * 45859601 -- старее 13 дней (Đăng 16/06/2026)
  * 45835871 -- старее 13 дней (Đăng 15/06/2026)
  * 45895261 -- старее 13 дней (Đăng 14/06/2026)
  * 45201513 -- старее 13 дней (Đăng 06/06/2026)
  * 45857308 -- старее 13 дней (Đăng 04/06/2026)
  * 45050388 -- старее 13 дней (Đăng 29/05/2026)
  * 45769899 -- старее 13 дней (Đăng 20/05/2026)
  * 45169268 -- старее 13 дней (Đăng 14/05/2026)
  * 39101985 -- старее 13 дней (Đăng 03/05/2026)
  * 45633287 -- старее 13 дней (Đăng 27/04/2026)
  * 44435718 -- старее 13 дней (Đăng 16/04/2026)
"""
from listing_lock import insert_listings

IDS = [3000613, 3000614, 3000615, 3000616, 3000617, 3000618, 3000619, 3000620, 3000621, 3000622]

NEW_SRC = r'''
L(3000613,"nha-trang","btr","Квартира",16000000,50,
  "1-спальная квартира, 50 м², Bắc Nha Trang — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-pham-van-dong-phuong-vinh-hoa-2-libera-nha-trang/cho-1pn-the-paramount-16-trieu-pr46269065","5 дней назад",5,source="batdongsan",
  descEn="1-bedroom flat, 50 m², Bắc Nha Trang — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907203932-d923_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907203933-6277_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907203933-9af5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907203934-7f07_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907203934-322f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907203935-d751_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000614,"nha-trang","lt","Квартира",25000000,None,
  "2-спальная квартира, Lộc Thọ — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-ton-dan-phuong-loc-tho-maple-nha-trang/cho-an-view-bien-full-noi-that-ep-vao-o-ngay-pr46248208","сегодня",0,source="batdongsan",
  descEn="2-bedroom flat, Lộc Thọ — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902124710-abbc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902124710-0b56_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902124711-70f0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902124712-8256_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902124713-3c22_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902130702-323f_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000615,"nha-trang","pl","Квартира",11000000,68,
  "Квартира, 68 м², Phước Long.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-van-kiet-phuong-phuoc-long-chung-cu-ccu-01-phuoc-long/cho-2pn-ccu01-dien-tich-68-27m-cong-nang-2-phong-ngu-2-wc-pho-pr46293053","сегодня",0,source="batdongsan",
  descEn="Flat, 68 m², Phước Long.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913111353-b7a6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913111354-5c17_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913111354-5672_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913111355-4754_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/13/20260913111353-b7a6_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/13/20260913111354-5c17_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000616,"nha-trang","ttr","Квартира",10000000,70,
  "2-спальная квартира, 70 м², Tây Nha Trang — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-19-5-1-xa-vinh-hiep-1-khu-do-thi-vinh-diem-trung/cho-2-phong-ngu-ay-u-noi-that-tai-ct2-iem-gan-sieu-go-pr46293031","сегодня",0,source="batdongsan",
  descEn="2-bedroom flat, 70 m², Tây Nha Trang — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913110502-eceb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913110502-ecd2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913110502-e466_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913110503-43d6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913110503-24b6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913110503-75ed_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000617,"nha-trang","ph","Квартира",8000000,70,
  "Квартира, 70 м², Phước Hải.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-phuoc-hai/cho-ssh-03-phong-ngu-8trieu-dien-tich-70m2-thiet-ke-3-phong-ngu-2wc-pr46288910","2 дня назад",2,source="batdongsan",
  descEn="Flat, 70 m², Phước Hải.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911222959-22aa_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911222957-f6f9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911222958-698d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911222956-31a8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911222959-46ed_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/11/20260911222959-22aa_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000618,"nha-trang","ph","Квартира",7000000,58,
  "Квартира, 58 м², Phước Hải.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-phuoc-hai/cho-ssh0-ha-quang-1-dt-58m2-2pn-2wc-trong-ko-noi-that-gia-7tr-thang-pr46288474","2 дня назад",2,source="batdongsan",
  descEn="Flat, 58 m², Phước Hải.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911190134-b0eb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911190135-1b46_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911190136-843d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911190136-5a88_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911190137-b97e_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/11/20260911190134-b0eb_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000619,"nha-trang","lt","Квартира",22000000,70,
  "2-спальная квартира, 70 м², Lộc Thọ — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-loc-tho-gold-coast-nha-trang/cho-full-noi-that-sin-70m-2-ngu-view-bien-vao-o-ngay-pr46288195","2 дня назад",2,source="batdongsan",
  descEn="2-bedroom flat, 70 m², Lộc Thọ — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911171944-e148_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911171947-e139_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911171949-532c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911171950-bf5c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911171951-ee8b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911171953-9da6_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000620,"nha-trang","ph","Дом",18000000,85,
  "4-спальный дом, 85 м², Phước Hải — 4 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-hong-phong-phuong-phuoc-hai-khu-do-thi-le-hong-phong-i/cho-k-t-ha-quang-gia-18-trieu-pr46292987","сегодня",0,source="batdongsan",
  descEn="4-bedroom house, 85 m², Phước Hải — 4 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913104631-03dd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913104639-de7e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913104648-c046_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913104707-e5f8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913104710-fcf3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913104714-9ca5_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000621,"nha-trang","ph","Дом",25000000,100,
  "4-спальный дом, 100 м², Phước Hải — 4 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-phuoc-hai-khu-do-thi-vcn-phuoc-hai/o-kinh-doanh-4-phong-ngu-full-noi-that-pr46290661","вчера",1,source="batdongsan",
  descEn="4-bedroom house, 100 m², Phước Hải — 4 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912132241-e4fc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912132241-c04a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912132241-bfbc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912132241-fcde_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912132241-9b32_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912132241-2efd_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000622,"nha-trang","pl","Дом",30000000,150,
  "6-спальный дом, 150 м², Phước Long — 4 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-phuoc-long-khu-do-thi-an-binh-tan/cho-150m2-k-t-gia-30trieu-pr46288332","вчера",1,source="batdongsan",
  descEn="6-bedroom house, 150 m², Phước Long — 4 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911175644-ba5d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911175646-117d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911175647-e6a3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911175647-ec66_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911175648-9f5a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911175649-dccf_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
