# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 6 строк, 2026-09-13, город da-nang.

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
  * 46277539 -- hx, 11,000,000 ₫, 100 м²: квартал в адресе объявления: hoa xuan
  * 46276820 -- hcg, 30,000,000 ₫, 70 м²: квартал в адресе объявления: hoa cuong
  * 46274032 -- hc, 5,000,000 ₫, 20 м²: квартал в адресе объявления: hai chau
  * 46242805 -- hc, 5,000,000 ₫, 30 м²: квартал в адресе объявления: hai chau
  * 46248996 -- ns, 5,000,000 ₫, 36 м²: квартал в адресе объявления: ngu hanh son
  * 46256877 -- tk, 6,000,000 ₫, 25 м²: квартал в адресе объявления: thanh khe

ОТСЕЯНО (74):
  * 46275818 -- уже на сайте
  * 46269354 -- уже на сайте
  * 46278150 -- уже на сайте
  * 46263637 -- похоже на уже заведённое: id 3000542
  * 46273841 -- уже на сайте
  * 46273790 -- уже на сайте
  * 46203271 -- цена не читается: Giá thỏa thuận
  * 46232561 -- уже на сайте
  * 46267353 -- уже на сайте
  * 46292997 -- похоже на уже заведённое: id 3000542
  * 46256739 -- уже на сайте
  * 37014826 -- похоже на уже заведённое: id 2000401
  * 46268102 -- похоже на уже заведённое: id 2000401
  * 46262116 -- уже на сайте
  * 46292125 -- цена не читается: Giá thỏa thuận
  * 46291484 -- район не назван так, как его знает сайт (phuong hoa xuan)
  * 46291438 -- уже на сайте
  * 46289960 -- уже на сайте
  * 46287668 -- цена не читается: Giá thỏa thuận
  * 46287883 -- цена не читается: Giá thỏa thuận
  * 46287548 -- цена не читается: Giá thỏa thuận
  * 46287425 -- цена не читается: Giá thỏa thuận
  * 46287402 -- цена не читается: Giá thỏa thuận
  * 46283988 -- уже на сайте
  * 46280179 -- похоже на уже заведённое: id 1001040
  * 46279801 -- похоже на уже заведённое: id 1001149
  * 46277457 -- похоже на уже заведённое: id 1001190
  * 46277421 -- похоже на уже заведённое: id 1001190
  * 46275218 -- похоже на уже заведённое: id 1001013
  * 46274519 -- похоже на уже заведённое: id 1000994
  * 42261329 -- район не назван так, как его знает сайт (1 phuong hoa)
  * 46234113 -- район не назван так, как его знает сайт (ban thach tp)
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

IDS = [3000596, 3000597, 3000598, 3000599, 3000600, 3000601]

NEW_SRC = r'''
L(3000596,"da-nang","hx","Дом",11000000,100,
  "1-спальный дом, 100 м², Hòa Xuân — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-quang-chi-phuong-hoa-xuan-tp-da-nang/cho-cap-4-kinh-doanh-buon-ban-tap-nap-truc-uong-lon-10m5-co-gac-mai-pr46277539","4 дня назад",4,source="batdongsan",
  descEn="1-bedroom house, 100 m², Hòa Xuân — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909142454-144d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909142456-fc67_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909142457-66eb_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/09/20260909142454-144d_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/09/20260909142456-fc67_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/09/20260909142457-66eb_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000597,"da-nang","hcg","Дом",30000000,70,
  "3-спальный дом, 70 м², Hòa Cường — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-dinh-ly-phuong-hoa-cuong-tp-da-nang/cho-4-tang-inh-3-phong-ngu-3wc-san-bbq-gara-o-to-u-noi-that-pr46276820","4 дня назад",4,source="batdongsan",
  descEn="3-bedroom house, 70 m², Hòa Cường — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909114451-e685_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909114452-b3d6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909114453-e301_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909114454-fa40_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909114455-d623_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909114456-cc83_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000598,"da-nang","hc","Комната",5000000,20,
  "Комната, 20 м², Hải Châu — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-hai-son-phuong-hai-chau-tp-da-nang/khu-38-a-gan-cho-ong-a-a-nang-pr46274032","5 дней назад",5,source="batdongsan",
  descEn="Room, 20 m², Hải Châu — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908175527-7bc7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908175530-ff33_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908175533-c226_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908175536-b699_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908175539-0381_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908175541-afdd_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000599,"da-nang","hc","Комната",5000000,30,
  "Комната, 30 м², Hải Châu — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-phuong-hai-chau-tp-da-nang/cho-trung-tam-a-nang-pr46242805","14 дней назад",14,source="batdongsan",
  descEn="Room, 30 m², Hải Châu — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/30/20260830132337-dd9e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/30/20260830132337-ee36_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/30/20260830132337-4e2d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/30/20260830132337-4129_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/30/20260830132337-5673_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/30/20260830132337-dd9e_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000600,"da-nang","ns","Комната",5000000,36,
  "Комната, 36 м², Ngũ Hành Sơn — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-pham-noi-phuong-ngu-hanh-son-tp-da-nang/cho-o-lau-dai-a-nang-pr46248996","10 дней назад",10,source="batdongsan",
  descEn="Room, 36 m², Ngũ Hành Sơn — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212820-49a7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212820-14df_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212820-bc3a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212820-8073_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212820-b012_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902212820-7aed_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000601,"da-nang","tk","Комната",6000000,25,
  "Комната, 25 м², Thanh Khê.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-dao-duy-tu-phuong-thanh-khe-tp-da-nang/cho-moi-100-trung-tam-vi-tri-giao-uong-ong-ich-khiem-gan-cho-con-sieu-thi-go-pr46256877","8 дней назад",8,source="batdongsan",
  descEn="Room, 25 m², Thanh Khê.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904152826-00c8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904152826-baff_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904152826-40f2_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/04/20260904152826-00c8_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/04/20260904152826-baff_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/04/20260904152826-40f2_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
