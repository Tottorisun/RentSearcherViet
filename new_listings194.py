# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 12 строк, 2026-09-13, город can-tho.

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
  * 46246561 -- hpu, 6,000,000 ₫, 74 м²: нынешний район назван в карточке: Hưng Phú
  * 46292492 -- crg, 10,000,000 ₫, 69 м²: нынешний район назван в карточке: Cái Răng
  * 46282686 -- crg, 12,000,000 ₫, 53 м²: нынешний район назван в карточке: Cái Răng
  * 46277487 -- crg, 21,000,000 ₫, 86 м²: нынешний район назван в карточке: Cái Răng
  * 46276635 -- crg, 9,000,000 ₫, 57 м²: нынешний район назван в карточке: Cái Răng
  * 46275381 -- crg, 12,000,000 ₫, 62 м²: нынешний район назван в карточке: Cái Răng
  * 46293464 -- ckh, 5,000,000 ₫, 52 м²: нынешний район назван в карточке: Cái Khế
  * 46292636 -- tanc, 16,000,000 ₫, 90 м²: квартал в адресе объявления: tan an
  * 46289836 -- tanc, 8,000,000 ₫, 40 м²: нынешний район назван в карточке: Tân An
  * 46287191 -- tanc, 12,000,000 ₫, 72 м²: нынешний район назван в карточке: Tân An
  * 46284490 -- hpu, 9,000,000 ₫, 81 м²: квартал в адресе объявления: hung phu
  * 46283882 -- hpu, 13,000,000 ₫, 216 м²: квартал в адресе объявления: hung phu

ОТСЕЯНО (67):
  * 46207028 -- похоже на уже заведённое: id 1002520
  * 45457221 -- похоже на уже заведённое: id 1002520
  * 46284907 -- похоже на уже заведённое: id 1002933
  * 46213657 -- похоже на уже заведённое: id new:46276635
  * 45987974 -- похоже на уже заведённое: id 1002965
  * 45988341 -- похоже на уже заведённое: id 1002965
  * 46292031 -- похоже на уже заведённое: id 1002599
  * 46287446 -- похоже на уже заведённое: id 1002599
  * 46282502 -- лимит прогона выбран
  * 46279844 -- лимит прогона выбран
  * 46275618 -- лимит прогона выбран
  * 46215954 -- лимит прогона выбран
  * 46216136 -- лимит прогона выбран
  * 46274154 -- лимит прогона выбран
  * 45948985 -- лимит прогона выбран
  * 46007565 -- лимит прогона выбран
  * 46193738 -- лимит прогона выбран
  * 46196000 -- лимит прогона выбран
  * 46243641 -- лимит прогона выбран
  * 46256691 -- лимит прогона выбран
  * 39577249 -- район не назван так, как его знает сайт (phuoc thoi, phuoc thoi; в карточке «Q. Ô Môn (P. Phước Thới mới)»)
  * 44385985 -- лимит прогона выбран
  * 39563308 -- лимит прогона выбран
  * 40290344 -- лимит прогона выбран
  * 40290347 -- цена не читается: 1,1 triệu/tháng
  * 41138517 -- цена не читается: 1 triệu/tháng
  * 42096008 -- лимит прогона выбран
  * 44385918 -- лимит прогона выбран
  * 45579525 -- старее 13 дней (Đăng 12/08/2026)
  * 42375396 -- лимит прогона выбран
  * 45651391 -- старее 13 дней (Đăng 2 tuần trước)
  * 46217775 -- старее 13 дней (Đăng 3 tuần trước)
  * 40061981 -- старее 13 дней (Đăng 1 tháng trước)
  * 39078034 -- старее 13 дней (Đăng 14/08/2026)
  * 46177187 -- старее 13 дней (Đăng 13/08/2026)
  * 46165561 -- старее 13 дней (Đăng 11/08/2026)
  * 45372423 -- старее 13 дней (Đăng 13/07/2026)
  * 46033037 -- старее 13 дней (Đăng 11/07/2026)
  * 46005094 -- старее 13 дней (Đăng 05/07/2026)
  * 45983521 -- старее 13 дней (Đăng 01/07/2026)
"""
from listing_lock import insert_listings

IDS = [3000623, 3000624, 3000625, 3000626, 3000627, 3000628, 3000629, 3000630, 3000631, 3000632, 3000633, 3000634]

NEW_SRC = r'''
L(3000623,"can-tho","hpu","Квартира",6000000,74,
  "2-спальная квартира, 74 м², Hưng Phú — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-quang-trung-phuong-phu-thu-tay-nguyen-plaza/cho-74m2-2pn-full-noi-that-view-uong-pho-cau-tho-thang-may-pr46246561","сегодня",0,source="batdongsan",
  descEn="2-bedroom flat, 74 m², Hưng Phú — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901111330-b483_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901111331-e124_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901111331-4099_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901111332-c510_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901111332-9dfe_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901111333-c100_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000624,"can-tho","crg","Квартира",10000000,69,
  "3-спальная квартира, 69 м², Cái Răng — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-3pn-u-noi-that-ii-pr46292492","сегодня",0,source="batdongsan",
  descEn="3-bedroom flat, 69 m², Cái Răng — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913061735-a043_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913061736-cbe5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913061736-5059_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913061737-41d8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913061738-dacb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913061738-f271_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000625,"can-tho","crg","Квартира",12000000,53,
  "2-спальная квартира, 53 м², Cái Răng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/cho-cao-cap-full-noi-that-don-vao-o-ngay-y-nhu-hinh-tai-trung-tam-tho-pr46282686","3 дня назад",3,source="batdongsan",
  descEn="2-bedroom flat, 53 m², Cái Răng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910145025-c1b5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910145025-2534_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910145026-4b29_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910145026-c810_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910145027-326a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910145027-8c47_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000626,"can-tho","crg","Квартира",21000000,86,
  "3-спальная квартира, 86 м², Cái Răng.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vu-dinh-lieu-phuong-hung-thanh-cara-river-park/cho-3pn-86m2-full-noi-that-park-pr46277487","4 дня назад",4,source="batdongsan",
  descEn="3-bedroom flat, 86 m², Cái Răng.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909141740-c0a4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909141741-4dc9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909141742-d190_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909141743-7f82_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909141743-51d9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909141744-3847_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000627,"can-tho","crg","Квартира",9000000,57,
  "2-спальная квартира, 57 м², Cái Răng — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-2-2pn-full-noi-that-pr46276635","4 дня назад",4,source="batdongsan",
  descEn="2-bedroom flat, 57 m², Cái Răng — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909111928-5848_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909111929-4742_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909111930-b3db_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909111931-3d61_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909111933-c8ca_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909111933-d26e_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000628,"can-tho","crg","Квартира",12000000,62,
  "3-спальная квартира, 62 м², Cái Răng — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-hung-thanh-nam-long-ii-central-lake/cho-62m2-gom-3-phong-ngu-cai-rang-tho-pr46275381","4 дня назад",4,source="batdongsan",
  descEn="3-bedroom flat, 62 m², Cái Răng — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909091228-135c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909091229-2f43_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909091229-124f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909091230-c8c5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909091231-e827_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909091231-23f9_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000629,"can-tho","ckh","Дом",5000000,52,
  "2-спальный дом, 52 м², Cái Khế — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-mau-than-phuong-an-hoa-2-83/cho-lau-co-noi-that-gan-cao-ang-y-te-sieu-thi-lotte-mart-tp-can-tho-pr46293464","сегодня",0,source="batdongsan",
  descEn="2-bedroom house, 52 m², Cái Khế — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913143804-3a62_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913143805-99dd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913143805-7f8a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913143806-6c12_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913143806-03bc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913143807-0868_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000630,"can-tho","tanc","Дом",16000000,90,
  "4-спальный дом, 90 м², Tân An — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-tan-an-1/nha1-tret-2-lau-vi-tri-kinh-doanh-vp-cong-ty-lo-20m-co-4-p-ngu-rong-cach-truong-h-y-duoc-900m-pr46292636","сегодня",0,source="batdongsan",
  descEn="4-bedroom house, 90 m², Tân An — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085031-0dfb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085034-1fad_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085036-9b73_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085038-031c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085040-1492_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/13/20260913085043-a849_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000631,"can-tho","tanc","Дом",8000000,40,
  "2-спальный дом, 40 м², Tân An — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-an-khanh-1/lau-ep-co-2-phong-ngu-gan-h-y-duoc-cho-tret-lau-kdc-thoi-nhut-p-tan-can-tho-pr46289836","вчера",1,source="batdongsan",
  descEn="2-bedroom house, 40 m², Tân An — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912095951-a521_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912095952-7a35_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912095953-8b6e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912095954-e566_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912095954-bfc0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912095955-8c37_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000632,"can-tho","tanc","Дом",12000000,72,
  "3-спальный дом, 72 м², Tân An — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-phuong-an-khanh-1/cho-tret-lau-san-thuong-mat-tien-kinh-doanh-vp-cong-ty-ngay-kdc-91b-pr46287191","2 дня назад",2,source="batdongsan",
  descEn="3-bedroom house, 72 m², Tân An — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911144947-e00a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911144947-0431_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911144948-99cf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911144948-b77d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911144949-aa3b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911144949-339b_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000633,"can-tho","hpu","Дом",9000000,81,
  "2-спальный дом, 81 м², Hưng Phú — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-quang-trung-phuong-hung-phu-khu-do-thi-moi-hung-phu-can-tho/9tr-2pn-tret-lung-au-kdc-lo-16m-vi-tri-ep-ko-ngap-pr46284490","3 дня назад",3,source="batdongsan",
  descEn="2-bedroom house, 81 m², Hưng Phú — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910214936-6973_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910214959-6ac1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910214959-7c29_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910215000-b24f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910215000-51ff_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910215000-6103_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000634,"can-tho","hpu","Дом",13000000,216,
  "4-спальный дом, 216 м², Hưng Phú — 4 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-vo-nguyen-giap-phuong-hung-phu-1-82/cho-1-tret-2-lau-kdc-1-4pn-nt-y-hinh-pr46283882","3 дня назад",3,source="batdongsan",
  descEn="4-bedroom house, 216 m², Hưng Phú — 4 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910174327-0fe0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910174328-bb25_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910174328-f447_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910174329-a4dc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910174330-2df2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910174330-6250_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
