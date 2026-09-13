# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 9 строк, 2026-09-13, город ha-noi.

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
  * 46267180 -- tx, 48,000,000 ₫, 100 м²: нынешний район назван в карточке: Thanh Xuân
  * 46282680 -- lbn, 14,000,000 ₫, 58 м²: квартал в адресе объявления: long bien
  * 46282182 -- dd, 5,000,000 ₫, 60 м²: нынешний район назван в карточке: Đống Đa
  * 46275435 -- cg, 75,000,000 ₫, 50 м²: нынешний район назван в карточке: Cầu Giấy
  * 46268230 -- hd, 5,000,000 ₫, 25 м²: нынешний район назван в карточке: Hà Đông
  * 46271167 -- tyh, 8,000,000 ₫, 30 м²: нынешний район назван в карточке: Tây Hồ
  * 46275994 -- tx, 50,000,000 ₫, 70 м²: квартал в адресе объявления: thanh xuan
  * 46282581 -- hd, 60,000,000 ₫, 120 м²: нынешний район назван в карточке: Hà Đông
  * 46282443 -- hd, 20,000,000 ₫, 75 м²: нынешний район назван в карточке: Hà Đông

ОТСЕЯНО (71):
  * 46086956 -- район не назван так, как его знает сайт (gia lam)
  * 46126554 -- район не назван так, как его знает сайт (gia lam)
  * 45938799 -- район не назван так, как его знает сайт (vinh tuy times, vinh tuy)
  * 46177299 -- район не назван так, как его знает сайт (gia lam)
  * 46277180 -- район не назван так, как его знает сайт (gia lam)
  * 46105341 -- район не назван так, как его знает сайт (gia lam)
  * 45989538 -- район не назван так, как его знает сайт (vinh tuy times, vinh tuy)
  * 46255588 -- район не назван так, как его знает сайт (gia lam)
  * 46170734 -- район не назван так, как его знает сайт (tay mo vinhomes, tay mo)
  * 46275958 -- район не назван так, как его знает сайт (tay mo the, tay mo)
  * 42961364 -- район не назван так, как его знает сайт (gia lam)
  * 46273608 -- район не назван так, как его знает сайт (vinh tuy times, vinh tuy)
  * 45170128 -- район не назван так, как его знает сайт (tay mo vinhomes, tay mo)
  * 45323490 -- район не назван так, как его знает сайт (tay mo vinhomes, tay mo)
  * 46262020 -- цена не читается: Giá thỏa thuận
  * 46283509 -- район не назван так, как его знает сайт (dong ngac sunshine, phu thuong)
  * 45679716 -- район не назван так, как его знает сайт (vinh tuy times, vinh tuy)
  * 44254074 -- район не назван так, как его знает сайт (me tri vinhomes, dai mo)
  * 36391599 -- район не назван так, как его знает сайт (vinh tuy imperia, vinh tuy)
  * 46228920 -- район не назван так, как его знает сайт (xuan dinh 718, xuan dinh)
  * 46262387 -- район не назван так, как его знает сайт (thanh nhan 4, bach mai)
  * 46290354 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa)
  * 38992140 -- район не назван так, как его знает сайт (bach mai 4, bach mai)
  * 46285359 -- район не назван так, как его знает сайт (o cho dua, o cho dua)
  * 46190525 -- район не назван так, как его знает сайт (yen hoa 2, yen hoa)
  * 46230430 -- район не назван так, как его знает сайт (o cho dua, o cho dua)
  * 45930803 -- район не назван так, как его знает сайт (phuc xa 2, hong ha)
  * 46268148 -- похоже на уже заведённое: id 1001869
  * 46122526 -- район не назван так, как его знает сайт (tu lien 6, hong ha)
  * 46291782 -- район не назван так, как его знает сайт (my dinh 2, tu liem)
  * 46263854 -- район не назван так, как его знает сайт (my dinh 1, tu liem)
  * 46290074 -- район не назван так, как его знает сайт (xuan la 6, xuan dinh)
  * 46286806 -- район не назван так, как его знает сайт (phuc loi 9, phuc loi)
  * 46278483 -- район не назван так, как его знает сайт (nghia do 1, nghia do)
  * 46187476 -- район не назван так, как его знает сайт (yen hoa 2, yen hoa)
  * 45830490 -- район не назван так, как его знает сайт (dai kim, dinh cong)
  * 46254882 -- район не назван так, как его знает сайт (thanh luong 4, linh nam)
  * 46292948 -- район не назван так, как его знает сайт (yen hoa 2, yen hoa)
  * 45690790 -- район не назван так, как его знает сайт (thuong cat, thuong cat)
  * 46192410 -- район не назван так, как его знает сайт (la khe the, duong noi)
"""
from listing_lock import insert_listings

IDS = [3000587, 3000588, 3000589, 3000590, 3000591, 3000592, 3000593, 3000594, 3000595]

NEW_SRC = r'''
L(3000587,"ha-noi","tx","Дом",48000000,100,
  "Дом, 100 м², Thanh Xuân — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-nguy-nhu-kon-tum_1-phuong-nhan-chinh-5/chu-cho-2-tang-kinh-doanh-tai-so-6-ngo-68-tum-pr46267180","5 дней назад",5,source="batdongsan",
  descEn="House, 100 m², Thanh Xuân — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142601-3e9f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142602-41ee_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142604-803a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142605-4f1d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142606-4acc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142608-87ae_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000588,"ha-noi","lbn","Дом",14000000,58,
  "Дом, 58 м², Long Biên — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-bat-khoi-phuong-long-bien-9/chinh-chu-cho-5-tang-nguyen-can-dt-58m2-mat-tien-rong-phu-hop-o-ket-hop-kinh-doanh-pr46282680","3 дня назад",3,source="batdongsan",
  descEn="House, 58 m², Long Biên — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153515-cb8a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153516-5dd8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153517-2f24_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153515-efe0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153517-ab89_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153517-de28_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000589,"ha-noi","dd","Дом",5000000,60,
  "Дом, 60 м², Đống Đa.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-thinh-quang-phuong-thinh-quang-3/cho-nguyen-can-ha-noi-5-ngu-tang-nao-eu-co-toilet-full-ieu-hoa-nong-lanh-pr46282182","3 дня назад",3,source="batdongsan",
  descEn="House, 60 m², Đống Đa.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/29/20260829213457-831b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/29/20260829213457-a864_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/29/20260829213457-51c0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/29/20260829213457-8f04_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/29/20260829213457-831b_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/29/20260829213457-a864_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000590,"ha-noi","cg","Комната",75000000,50,
  "Комната, 50 м², Cầu Giấy — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-com-vong-phuong-dich-vong-hau-7/mua-nhap-hoc-2026-san-slot-ky-tuc-xa-thang-long-pr46275435","4 дня назад",4,source="batdongsan",
  descEn="Room, 50 m², Cầu Giấy — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813150236-eb44_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813150236-aa8d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813150236-db6c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813150237-e717_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813150237-8397_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/13/20260813150238-026d_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000591,"ha-noi","hd","Комната",5000000,25,
  "Комната, 25 м², Hà Đông.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-yen-xa-xa-tan-trieu-13/chinh-chu-cho-tai-gia-chi-tu-3-5tr-gac-xep-full-o-pr46268230","5 дней назад",5,source="batdongsan",
  descEn="Room, 25 m², Hà Đông.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162002-7812_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162002-c437_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162002-aa5a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162957-e682_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162957-0a31_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907162958-711e_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000592,"ha-noi","tyh","Комната",8000000,30,
  "Комната, 30 м², Tây Hồ — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-lac-long-quan-phuong-buoi-6/cho-sieu-ep-tai-569-ngay-gan-ho-tay-sieu-thoang-pr46271167","5 дней назад",5,source="batdongsan",
  descEn="Room, 30 m², Tây Hồ — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908104514-a0bf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908104515-4b3d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908104515-5203_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908104516-f7ed_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908104516-7f8d_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/08/20260908104514-a0bf_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000593,"ha-noi","tx","Дом",50000000,70,
  "Дом, 70 м², Thanh Xuân.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-nguyen-huy-tuong-phuong-thanh-xuan-trung-lien-ke-96-nguyen-huy-tuong/cho-lam-van-phong-ia-iem-kinh-doanh-pr46275994","4 дня назад",4,source="batdongsan",
  descEn="House, 70 m², Thanh Xuân.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909101137-8f00_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909101137-882e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909101233-76d9_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/09/20260909101137-8f00_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/09/20260909101137-882e_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/09/20260909101233-76d9_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000594,"ha-noi","hd","Дом",60000000,120,
  "Дом, 120 м², Hà Đông.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-nguyen-van-loc-phuong-mo-lao-lang-viet-kieu-chau-au-euroland/cho-mat-bang-kinh-doanh-sam-uat-pho-ha-ong-pr46282581","2 дня назад",2,source="batdongsan",
  descEn="House, 120 m², Hà Đông.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910143520-3719_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910143421-04c7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910143520-539f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910143520-429e_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/10/20260910143520-3719_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/10/20260910143421-04c7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000595,"ha-noi","hd","Дом",20000000,75,
  "4-спальный дом, 75 м², Hà Đông — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-nguyen-khuyen-phuong-phuc-la-khu-do-thi-moi-van-quan/cho-4pn-3wc-75m2-20-trieu-vnd-tai-ha-ong-pr46282443","3 дня назад",3,source="batdongsan",
  descEn="4-bedroom house, 75 m², Hà Đông — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910142403-d71b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910142403-dc25_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910142403-9aaf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910142403-2d13_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910142403-7319_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910142404-eaff_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
