# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 7 строк, 2026-09-13, город ho-chi-minh.

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
  * 46287244 -- tm, 17,000,000 ₫, 75 м²: нынешний район назван в карточке: Tân Mỹ
  * 46285878 -- tm, 10,000,000 ₫, 161 м²: нынешний район назван в карточке: Tân Mỹ
  * 46278984 -- th, 5,000,000 ₫, 50 м²: нынешний район назван в карточке: Tân Hưng
  * 46268198 -- tm, 11,000,000 ₫, 57 м²: нынешний район назван в карточке: Tân Mỹ
  * 46271303 -- ak, 22,000,000 ₫, 64 м²: нынешний район назван в карточке: An Khánh
  * 46230148 -- ak, 21,000,000 ₫, 95 м²: квартал в адресе объявления: an phu
  * 46248047 -- ak, 28,000,000 ₫, 91 м²: нынешний район назван в карточке: An Khánh

ОТСЕЯНО (373):
  * 35670559 -- район не назван так, как его знает сайт (tan thuan tay, tan thuan)
  * 46123754 -- похоже на уже заведённое: id new:45168390
  * 34570335 -- район не назван так, как его знает сайт (phu thuan 3)
  * 46006351 -- похоже на уже заведённое: id 1002786
  * 46271795 -- похоже на уже заведённое: id 1002786
  * 35321899 -- район не назван так, как его знает сайт (tan thuan tay, tan thuan)
  * 41094428 -- район не назван так, как его знает сайт (phu thuan 3)
  * 46279407 -- район не назван так, как его знает сайт (phu thuan 3)
  * 39981691 -- похоже на уже заведённое: id 1000644
  * 35770675 -- район не назван так, как его знает сайт (phu thuan 3)
  * 45855261 -- район не назван так, как его знает сайт (phu thuan 3)
  * 45431382 -- район не назван так, как его знает сайт (tan thuan tay, tan thuan)
  * 46184498 -- район не назван так, как его знает сайт (thanh my loi, cat lai)
  * 46214995 -- район не назван так, как его знает сайт (thanh my loi, cat lai)
  * 46262441 -- район не назван так, как его знает сайт (thanh my loi, cat lai)
  * 36069231 -- похоже на уже заведённое: id 1000762
  * 46184235 -- район не назван так, как его знает сайт (thanh my loi, cat lai)
  * 45356269 -- лимит прогона выбран
  * 43184378 -- лимит прогона выбран
  * 39621891 -- лимит прогона выбран
  * 46291738 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 46158451 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 46247813 -- район не назван так, как его знает сайт (ben nghe vinhomes, sai gon)
  * 45540622 -- район не назван так, как его знает сайт (ben nghe vinhomes, sai gon)
  * 46019439 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 46268753 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 46255430 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 46258757 -- район не назван так, как его знает сайт (ben nghe vinhomes, sai gon)
  * 46272716 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 37806305 -- район не назван так, как его знает сайт (ben nghe vinhomes, sai gon)
  * 43854412 -- район не назван так, как его знает сайт (ben nghe vinhomes, sai gon)
  * 46158399 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 46249633 -- район не назван так, как его знает сайт (ben nghe vinhomes, sai gon)
  * 46132963 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 46268621 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 46136995 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 45181809 -- район не назван так, как его знает сайт (da kao the, sai gon)
  * 46243761 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 46247162 -- район не назван так, как его знает сайт (ben nghe grand, sai gon)
  * 43234315 -- район не назван так, как его знает сайт (ben nghe vinhomes, sai gon)
"""
from listing_lock import insert_listings

IDS = [3000580, 3000581, 3000582, 3000583, 3000584, 3000585, 3000586]

NEW_SRC = r'''
L(3000580,"ho-chi-minh","tm","Квартира",17000000,75,
  "Квартира, 75 м², Tân Mỹ.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-phu-thuan-phuong-tan-phu-19-sunshine-sky-city/em-sale-ong-gia-2pn-gia-chi-17-trieu-thang-pr46287244","2 дня назад",2,source="batdongsan",
  descEn="Flat, 75 m², Tân Mỹ.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911145314-b540_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911145314-2d0a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911145314-65b9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911145314-92a0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911145314-de18_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911145314-5b90_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000581,"ho-chi-minh","tm","Квартира",10000000,161,
  "4-спальная квартира, 161 м², Tân Mỹ — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-phu-my-9-the-era-town/a-dang-cac-cho-nha-moi-sach-ep-gia-10tr-lh-thu-hien-pr46285878","2 дня назад",2,source="batdongsan",
  descEn="4-bedroom flat, 161 m², Tân Mỹ — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911103548-8e91_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911103548-6b19_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911103548-f9b1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911103612-da7e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911103616-cafa_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/11/20260911103624-9ac7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000582,"ho-chi-minh","th","Квартира",5000000,50,
  "1-спальная квартира, 50 м², Tân Hưng — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-van-linh-phuong-tan-phong-9-lavida-plus/oc-quyen-quan-ly-cho-1pn-nha-ep-moi-y-hinh-hiem-co-gia-tot-hien-trong-o-ngay-pr46278984","4 дня назад",4,source="batdongsan",
  descEn="1-bedroom flat, 50 m², Tân Hưng — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/19/20260819152918-d0bd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/19/20260819152918-f7f3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/19/20260819152918-ee91_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/19/20260819152918-26be_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/19/20260819152918-67cf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/19/20260819152918-0b27_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000583,"ho-chi-minh","tm","Квартира",11000000,57,
  "2-спальная квартира, 57 м², Tân Mỹ — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-luong-bang-1-phuong-phu-my-9-q7-boulevard/chuyen-cho-cap-nhat-moi-nhat-t9-2026-2pn-1wc-gia-9-trieu-pr46268198","5 дней назад",5,source="batdongsan",
  descEn="2-bedroom flat, 57 m², Tân Mỹ — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162532-a78d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162531-ea59_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162532-1959_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162532-7d4c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162532-9fe2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162558-639d_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000584,"ho-chi-minh","ak","Квартира",22000000,64,
  "1-спальная квартира, 64 м², An Khánh — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-mai-chi-tho-phuong-thu-thiem-empire-city-thu-thiem/em-tu-vui-ve-a-o-hon-5-nam-ranh-rot-moi-tro-nhiet-tinh-chu-ao-khi-ve-o-pr46271303","5 дней назад",5,source="batdongsan",
  descEn="1-bedroom flat, 64 m², An Khánh — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/06/02/20260602130333-7455_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/02/20260602130355-eb01_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/11/20260411120838-dd5d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/11/20260411120838-e30b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/11/20260411120838-aec8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/11/20260411120838-4979_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000585,"ho-chi-minh","ak","Квартира",21000000,95,
  "2-спальная квартира, 95 м², An Khánh — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-an-phu-imperia-an-phu/cho-2-phong-ngu-95-m2-trong-khu-cao-cap-q2-gia-thuong-luong-pr46230148","2 дня назад",2,source="batdongsan",
  descEn="2-bedroom flat, 95 m², An Khánh — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826152552-ef5c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826152552-817d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826152553-0373_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826152553-f280_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826152554-42a6_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/26/20260826152552-ef5c_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000586,"ho-chi-minh","ak","Квартира",28000000,91,
  "2-спальная квартира, 91 м², An Khánh — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-mai-chi-tho-phuong-thu-thiem-empire-city-thu-thiem/top-2pn-gia-tot-t9-2026-nam-full-gio-hang-1pn-2pn-3pn-4pn-van-phong-tai-du-an-pr46248047","10 дней назад",10,source="batdongsan",
  descEn="2-bedroom flat, 91 m², An Khánh — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902111340-5f14_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902111343-26f2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902111346-0076_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902111345-9966_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902111345-b68e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/02/20260902111451-8c55_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
