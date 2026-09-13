# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 12 строк, 2026-09-13, город da-nang.

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
  * 46275818 -- hcg, 25,000,000 ₫, 76 м²: квартал в адресе объявления: hoa cuong
  * 46269354 -- ns, 15,000,000 ₫, 68 м²: квартал в адресе объявления: ngu hanh son
  * 46278150 -- ah, 20,000,000 ₫, 29 м²: квартал в адресе объявления: an hai
  * 46273841 -- ah, 35,000,000 ₫, 50 м²: квартал в адресе объявления: an hai
  * 46273790 -- hc, 25,000,000 ₫, 130 м²: квартал в адресе объявления: hai chau
  * 46232561 -- ah, 26,000,000 ₫, 32 м²: квартал в адресе объявления: an hai
  * 46267353 -- ah, 30,000,000 ₫: квартал в адресе объявления: an hai
  * 46256739 -- ah, 22,000,000 ₫, 65 м²: квартал в адресе объявления: an hai
  * 46262116 -- tk, 12,000,000 ₫, 60 м²: квартал в адресе объявления: thanh khe
  * 46291438 -- ns, 33,000,000 ₫, 150 м²: квартал в адресе объявления: ngu hanh son
  * 46289960 -- ns, 40,000,000 ₫, 100 м²: квартал в адресе объявления: ngu hanh son
  * 46283988 -- tk, 13,000,000 ₫, 70 м²: квартал в адресе объявления: thanh khe

ОТСЕЯНО (68):
  * 46263637 -- похоже на уже заведённое: id 3000542
  * 46203271 -- цена не читается: Giá thỏa thuận
  * 46292997 -- похоже на уже заведённое: id 3000542
  * 37014826 -- похоже на уже заведённое: id 2000401
  * 46268102 -- похоже на уже заведённое: id 2000401
  * 46292125 -- цена не читается: Giá thỏa thuận
  * 46291484 -- район не назван так, как его знает сайт (phuong hoa xuan)
  * 46287668 -- цена не читается: Giá thỏa thuận
  * 46287883 -- цена не читается: Giá thỏa thuận
  * 46287548 -- цена не читается: Giá thỏa thuận
  * 46287425 -- цена не читается: Giá thỏa thuận
  * 46287402 -- цена не читается: Giá thỏa thuận
  * 46280179 -- лимит прогона выбран
  * 46279801 -- лимит прогона выбран
  * 46277539 -- лимит прогона выбран
  * 46277457 -- лимит прогона выбран
  * 46277421 -- лимит прогона выбран
  * 46276820 -- лимит прогона выбран
  * 46275218 -- лимит прогона выбран
  * 46274519 -- лимит прогона выбран
  * 45293230 -- лимит прогона выбран
  * 43941497 -- лимит прогона выбран
  * 35819466 -- лимит прогона выбран
  * 46080387 -- лимит прогона выбран
  * 46274032 -- лимит прогона выбран
  * 37012702 -- лимит прогона выбран
  * 42261329 -- район не назван так, как его знает сайт (1 phuong hoa)
  * 42511574 -- лимит прогона выбран
  * 46234113 -- район не назван так, как его знает сайт (ban thach tp)
  * 46242805 -- лимит прогона выбран
  * 46248996 -- лимит прогона выбран
  * 46256877 -- лимит прогона выбран
  * 46259323 -- лимит прогона выбран
  * 46261665 -- район не назван так, как его знает сайт (dien ban dong)
  * 46268422 -- лимит прогона выбран
  * 46124797 -- старее 13 дней (Đăng 01/08/2026)
  * 46138175 -- старее 13 дней (Đăng 04/08/2026)
  * 46117954 -- старее 13 дней (Đăng 30/07/2026)
  * 45730353 -- старее 13 дней (Đăng 14/05/2026)
  * 45656085 -- старее 13 дней (Đăng 02/05/2026)
"""
from listing_lock import insert_listings

IDS = [3000566, 3000567, 3000568, 3000569, 3000570, 3000571, 3000572, 3000573, 3000574, 3000575, 3000576, 3000577]

NEW_SRC = r'''
L(3000566,"da-nang","hcg","Квартира",25000000,76,
  "2-спальная квартира, 76 м², Hòa Cường — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-vista-residence-da-nang-phuong-hoa-cuong-tp-da-nang/cho-2pn-moi-100-ay-u-noi-that-vao-o-ngay-pr46275818","4 дня назад",4,source="batdongsan",
  descEn="2-bedroom flat, 76 m², Hòa Cường — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909095204-d362_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909095204-7e68_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909095204-2505_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909095204-ac4e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909095204-8e5b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909095204-2ec3_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000567,"da-nang","ns","Квартира",15000000,68,
  "2-спальная квартира, 68 м², Ngũ Hành Sơn — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-fpt-plaza-2-phuong-ngu-hanh-son-tp-da-nang/cho-2-pr46269354","5 дней назад",5,source="batdongsan",
  descEn="2-bedroom flat, 68 m², Ngũ Hành Sơn — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907222721-8fa5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907222724-21cf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907222727-7d6d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907222730-6634_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907222733-0f11_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907222736-7a2b_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000568,"da-nang","ah","Квартира",20000000,29,
  "1-спальная квартира, 29 м², An Hải — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-sun-ponte-residence-da-nang-phuong-an-hai-tp-da-nang/cho-ngay-cau-rong-view-song-han-tran-hung-ao-son-tra-a-nang-pr46278150","4 дня назад",4,source="batdongsan",
  descEn="1-bedroom flat, 29 m², An Hải — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909152749-1f8e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909152750-2a39_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909152750-47a4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909152751-e75a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909152751-3fe6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909152752-7e21_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000569,"da-nang","ah","Квартира",35000000,50,
  "1-спальная квартира, 50 м², An Hải — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-an-hai-tp-da-nang/trai-nghiem-su-sang-trong-tien-nghi-va-ang-cap-voi-chi-3-phut-i-bo-ra-bien-pr46273841","5 дней назад",5,source="batdongsan",
  descEn="1-bedroom flat, 50 m², An Hải — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908170810-ca0f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908170818-c98d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908170832-c236_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/08/20260908170810-ca0f_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/08/20260908170818-c98d_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/08/20260908170832-c236_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000570,"da-nang","hc","Квартира",25000000,130,
  "2-спальная квартира, 130 м², Hải Châu — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-da-nang-plaza-phuong-hai-chau-tp-da-nang/cho-3pn-cai-tao-thanh-2pn-dt-130m2-toa-a-voi-goi-nt-ban-moi-90-pr46273790","5 дней назад",5,source="batdongsan",
  descEn="2-bedroom flat, 130 m², Hải Châu — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908170123-1533_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908170123-469a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908170123-7be6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908170123-6d5c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908170123-f10a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908170123-9412_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000571,"da-nang","ah","Квартира",26000000,32,
  "1-спальная квартира, 32 м², An Hải — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-sun-ponte-residence-da-nang-phuong-an-hai-tp-da-nang/cho-1pn-a-full-noi-that-ngay-song-han-gia-tu-53-32-trieu-m-pr46232561","5 дней назад",5,source="batdongsan",
  descEn="1-bedroom flat, 32 m², An Hải — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/27/20260827110825-058c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/27/20260827110834-8918_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/27/20260827110842-b23d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/27/20260827110851-8a6d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/27/20260827110904-7359_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/27/20260827110916-d2ab_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000572,"da-nang","ah","Квартира",30000000,None,
  "2-спальная квартира, An Hải — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-sun-ponte-residence-da-nang-phuong-an-hai-tp-da-nang/cho-2pn-tai-a-vi-tri-ngay-cau-rong-view-song-bien-pr46267353","5 дней назад",5,source="batdongsan",
  descEn="2-bedroom flat, An Hải — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907144151-3f5f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907144151-af5e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907144149-6dd2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907144151-cf1b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907144151-19b7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907144149-dbcd_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000573,"da-nang","ah","Квартира",22000000,65,
  "2-спальная квартира, 65 м², An Hải — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-hiyori-garden-tower-phuong-an-hai-tp-da-nang/cho-2pn-65m2-full-noi-that-cao-cap-trung-tam-son-tra-ngay-cau-rong-gia-tot-t9-pr46256739","8 дней назад",8,source="batdongsan",
  descEn="2-bedroom flat, 65 m², An Hải — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904151008-d1d7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904151008-842d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904151008-85a2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904151008-c83f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904151008-9f79_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904151008-bfe5_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000574,"da-nang","tk","Дом",12000000,60,
  "3-спальный дом, 60 м², Thanh Khê — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-dinh-ly-phuong-thanh-khe-tp-da-nang/cho-3-tang-2-mat-kiet-o-to-uong-inh-3-phong-12-trieu-pr46262116","7 дней назад",7,source="batdongsan",
  descEn="3-bedroom house, 60 m², Thanh Khê — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905222737-6a20_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905222738-34dc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905222812-bcc1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905222813-e53f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905222815-9e01_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905222816-610e_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000575,"da-nang","ns","Дом",33000000,150,
  "3-спальный дом, 150 м², Ngũ Hành Sơn — 4 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-vung-trung-3-phuong-ngu-hanh-son-tp-da-nang/cho-ep-3pn-kieu-villa-co-san-gan-khu-fpt-pr46291438","вчера",1,source="batdongsan",
  descEn="3-bedroom house, 150 m², Ngũ Hành Sơn — 4 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912161537-661c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912161549-2f91_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912161549-8dbb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912161549-93ad_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912161549-f687_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912161549-7004_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000576,"da-nang","ns","Дом",40000000,100,
  "4-спальный дом, 100 м², Ngũ Hành Sơn — 4 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-my-da-tay-5-phuong-ngu-hanh-son-tp-da-nang/cho-ep-4pn-4wc-uong-a-khu-nam-viet-a-pr46289960","вчера",1,source="batdongsan",
  descEn="4-bedroom house, 100 m², Ngũ Hành Sơn — 4 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912102034-9e77_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912102035-2a2c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912102035-4fa8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912102035-52d3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912102035-ed9b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912102035-84b7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000577,"da-nang","tk","Дом",13000000,70,
  "3-спальный дом, 70 м², Thanh Khê — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-dien-bien-phu-phuong-thanh-khe-tp-da-nang/cho-3-tang-moi-ep-uong-ien-3-phong-ngu-u-noi-that-pr46283988","3 дня назад",3,source="batdongsan",
  descEn="3-bedroom house, 70 m², Thanh Khê — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910182159-0aa0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910182200-c98c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910182201-aac1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910182202-2900_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910182204-516e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910182205-cfe3_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
