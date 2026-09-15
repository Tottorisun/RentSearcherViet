# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 10 строк, 2026-09-15, город ha-noi.

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
  * 46230430 -- dd, 14,000,000 ₫, 110 м²: нынешний район назван в карточке: Đống Đa
  * 46257466 -- dd, 22,000,000 ₫, 80 м²: нынешний район назван в карточке: Đống Đa
  * 46297883 -- hkm, 10,000,000 ₫, 40 м²: нынешний район назван в карточке: Hoàn Kiếm
  * 46298932 -- cg, 35,000,000 ₫, 20 м²: нынешний район назван в карточке: Cầu Giấy
  * 46096329 -- tx, 3,000,000 ₫, 20 м²: нынешний район назван в карточке: Thanh Xuân
  * 46260834 -- hd, 21,000,000 ₫, 98 м²: нынешний район назван в карточке: Hà Đông
  * 39921757 -- hm, 14,000,000 ₫, 95 м²: нынешний район назван в карточке: Hoàng Mai
  * 46281386 -- hm, 14,000,000 ₫, 100 м²: нынешний район назван в карточке: Hoàng Mai
  * 45726825 -- tyh, 92,000,000 ₫, 200 м²: нынешний район назван в карточке: Tây Hồ
  * 45455222 -- tyh, 120,000,000 ₫, 300 м²: нынешний район назван в карточке: Tây Hồ

ОТСЕЯНО (70):
  * 46303995 -- карточка без квартала -- из общего списка, а не города
  * 46302744 -- карточка без квартала -- из общего списка, а не города
  * 46105341 -- карточка без квартала -- из общего списка, а не города
  * 46255588 -- карточка без квартала -- из общего списка, а не города
  * 45312749 -- карточка без квартала -- из общего списка, а не города
  * 46126554 -- карточка без квартала -- из общего списка, а не города
  * 46009006 -- карточка без квартала -- из общего списка, а не города
  * 46086956 -- карточка без квартала -- из общего списка, а не города
  * 46277180 -- карточка без квартала -- из общего списка, а не города
  * 45989538 -- карточка без квартала -- из общего списка, а не города
  * 46170734 -- карточка без квартала -- из общего списка, а не города
  * 46275958 -- карточка без квартала -- из общего списка, а не города
  * 42961364 -- карточка без квартала -- из общего списка, а не города
  * 46273608 -- карточка без квартала -- из общего списка, а не города
  * 46297069 -- район не назван так, как его знает сайт (phu thuong 1, phu thuong; в карточке «Q. Tây Hồ (P. Phú Thượng mới)»)
  * 42363013 -- цена не читается: Giá thỏa thuận
  * 46301102 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 44051734 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 44542130 -- район не назван так, как его знает сайт (giang bien 1, viet hung; в карточке «Q. Long Biên (P. Việt Hưng mới)»)
  * 45895812 -- цена не читается: Giá thỏa thuận
  * 45913572 -- район не назван так, как его знает сайт (quan hoa 7, nghia do; в карточке «Q. Cầu Giấy (P. Nghĩa Đô mới)»)
  * 46297749 -- район не назван так, как его знает сайт (minh khai 4, tuong mai; в карточке «Q. Hai Bà Trưng (P. Tương Mai mới)»)
  * 46290354 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 38992140 -- район не назван так, как его знает сайт (bach mai 4, bach mai; в карточке «Q. Hai Bà Trưng (P. Bạch Mai mới)»)
  * 46285359 -- район не назван так, как его знает сайт (o cho dua, o cho dua; в карточке «Q. Đống Đa (P. Ô Chợ Dừa mới)»)
  * 46190525 -- район не назван так, как его знает сайт (yen hoa 2, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 46267180 -- уже на сайте
  * 46303972 -- район не назван так, как его знает сайт (giang vo 2, giang vo; в карточке «Q. Ba Đình (P. Giảng Võ mới)»)
  * 46299938 -- район не назван так, как его знает сайт (my dinh 1, pr46299938, tu liem; в карточке «Q. Nam Từ Liêm (P. Từ Liêm mới)»)
  * 45930803 -- район не назван так, как его знает сайт (phuc xa 2, hong ha; в карточке «Q. Ba Đình (P. Hồng Hà mới)»)
  * 46297747 -- район не назван так, как его знает сайт (lang ha 3, lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46136025 -- район не назван так, как его знает сайт (viet hung 2, viet hung; в карточке «Q. Long Biên (P. Việt Hưng mới)»)
  * 40284543 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 37657063 -- район не назван так, как его знает сайт (dai kim 8, dinh cong; в карточке «Q. Hoàng Mai (P. Định Công mới)»)
  * 46293208 -- район не назван так, как его знает сайт (thuong thanh 1, viet hung; в карточке «Q. Long Biên (P. Việt Hưng mới)»)
  * 46122526 -- район не назван так, как его знает сайт (tu lien 6, hong ha; в карточке «Q. Tây Hồ (P. Hồng Hà mới)»)
  * 46291782 -- район не назван так, как его знает сайт (my dinh 2, tu liem; в карточке «Q. Nam Từ Liêm (P. Từ Liêm mới)»)
  * 45830490 -- старее 6 дней (Đăng 1 tuần trước)
  * 46254882 -- старее 6 дней (Đăng 1 tuần trước)
  * 46300778 -- цена не читается: Giá thỏa thuận
"""
from listing_lock import insert_listings, remove_listings

IDS = [3000760, 3000761, 3000762, 3000763, 3000764, 3000765, 3000766, 3000767, 3000768, 3000769]
REPLACES = []

NEW_SRC = r'''
L(3000760,"ha-noi","dd","Дом",14000000,110,
  "3-спальный дом, 110 м², Đống Đa — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-hao-nam-phuong-o-cho-dua-3/nr-3pn-2wc-110m2-gia-uu-ai-14-trieu-tai-ngach-127-28-ha-noi-pr46230430","6 дней назад",6,source="batdongsan",postedOn="2026-09-09",
  descEn="3-bedroom house, 110 m², Đống Đa — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163500-513d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163501-88c7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163502-6286_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163504-255a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163505-5afc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163505-5093_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000761,"ha-noi","dd","Дом",22000000,80,
  "Дом, 80 м², Đống Đa.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-thai-ha-phuong-o-cho-dua-3/ong-a-80m2-4-5-tang-2-mat-thoang-rong-rai-hop-vp-lop-hoc-22tr-th-pr46257466","сегодня",0,source="batdongsan",postedOn="2026-09-15",
  descEn="House, 80 m², Đống Đa.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904165331-2ef0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904165331-10a9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904165331-022c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904165331-4949_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/04/20260904165331-5dab_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/04/20260904165331-2ef0_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000762,"ha-noi","hkm","Дом",10000000,40,
  "Дом, 40 м², Hoàn Kiếm.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ly-nam-de-phuong-hang-ma-1/chinh-chu-cho-pho-e-hoan-kiem-ha-noi-pr46297883","вчера",1,source="batdongsan",postedOn="2026-09-14",
  descEn="House, 40 m², Hoàn Kiếm.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914153512-1ca2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914153512-2444_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914153513-cf31_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/14/20260914153512-1ca2_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/14/20260914153512-2444_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/14/20260914153513-cf31_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000763,"ha-noi","cg","Комната",35000000,20,
  "Комната, 20 м², Cầu Giấy — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-mieu-dam-phuong-my-dinh-1-14/sieu-pham-am-o-luon-ngay-trung-tam-hoi-nghi-quoc-gia-big-c-thang-long-pr46298932","сегодня",0,source="batdongsan",postedOn="2026-09-15",
  descEn="Room, 20 m², Cầu Giấy — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914195536-9098_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914195537-de8f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914195538-7055_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914195539-c49e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914195539-1b9e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/14/20260914195540-fefd_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000764,"ha-noi","tx","Комната",3000000,20,
  "Комната, 20 м², Thanh Xuân.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-pho-chinh-kinh-phuong-nhan-chinh-5/chi-3tr-nga-tu-so-gia-re-sinh-vien-pr46096329","сегодня",0,source="batdongsan",postedOn="2026-09-15",
  descEn="Room, 20 m², Thanh Xuân.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100824-fbb9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100831-1594_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100829-4cb1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100822-8ae0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100834-81f5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100827-280d_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000765,"ha-noi","hd","Дом",21000000,98,
  "1-спальный дом, 98 м², Hà Đông — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-to-huu-phuong-van-phuc-1-him-lam-van-phuc/cho-bt-tai-gia-cuc-tot-21-trieu-san-phu-hop-phong-lh-pr46260834","вчера",1,source="batdongsan",postedOn="2026-09-14",
  descEn="1-bedroom house, 98 m², Hà Đông — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905145507-36fb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905145507-a6f9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905145508-de5a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905145508-94a1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905145508-0a07_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905145508-3877_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000766,"ha-noi","hm","Дом",14000000,95,
  "8-спальный дом, 95 м², Hoàng Mai — 8 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-tan-mai-phuong-hoang-van-thu-4-louis-city-hoang-mai/can-cho-5-can-tai-du-an-dia-chi-54-ha-noi-pr39921757","2 дня назад",2,source="batdongsan",postedOn="2026-09-13",
  descEn="8-bedroom house, 95 m², Hoàng Mai — 8 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/07/10/20260710132551-2fbe_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231802-ea5f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231804-9473_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231805-7071_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231807-a429_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/10/20260710132550-2a56_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000767,"ha-noi","hm","Дом",14000000,100,
  "Дом, 100 м², Hoàng Mai.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-tan-mai-phuong-hoang-van-thu-4-louis-city-hoang-mai/cho-tai-k-t-mai-pr46281386","5 дней назад",5,source="batdongsan",postedOn="2026-09-10",
  descEn="House, 100 m², Hoàng Mai.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910104539-ba3b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910104539-cd03_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910104539-e242_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910104539-0066_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910104539-b625_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/10/20260910104539-b7d5_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000768,"ha-noi","tyh","Дом",92000000,200,
  "5-спальный дом, 200 м², Tây Hồ — 6 санузлов, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-tay-ho-phuong-quang-an-2-6/ngoi-5-phong-ngu-san-vuon-u-o-o-cho-e-o-cty-shop-vv-pr45726825","вчера",1,source="batdongsan",postedOn="2026-09-14",
  descEn="5-bedroom house, 200 m², Tây Hồ — 6 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513215756-13fb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513215757-6e12_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513215758-395d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513215800-e0e9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513215800-6111_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/13/20260513215801-323f_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000769,"ha-noi","tyh","Дом",120000000,300,
  "4-спальный дом, 300 м², Tây Hồ — 5 санузлов, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-to-ngoc-van-phuong-quang-an-2-6/4-phong-ngu-rong-rai-san-vuon-tuyet-ep-tai-tay-ho-cho-thue-pr45455222","вчера",1,source="batdongsan",postedOn="2026-09-14",
  descEn="4-bedroom house, 300 m², Tây Hồ — 5 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/04/01/20260401230411-cee7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/01/20260401230412-2cee_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/01/20260401230413-8088_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/01/20260401230414-d5ce_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/01/20260401230415-14d6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/04/01/20260401230416-6177_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
