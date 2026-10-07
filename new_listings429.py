# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 9 строк, 2026-10-07, город ha-noi.

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
  * 37721099 -- tyh, 25,000,000 ₫, 87 м²: нынешний район назван в карточке: Tây Hồ
  * 46389346 -- tx, 8,000,000 ₫, 90 м²: нынешний район назван в карточке: Thanh Xuân
  * 46384200 -- hm, 5,000,000 ₫, 35 м²: нынешний район назван в карточке: Hoàng Mai
  * 46391710 -- tx, 15,000,000 ₫, 50 м²: нынешний район назван в карточке: Thanh Xuân
  * 46391703 -- tx, 15,000,000 ₫, 45 м²: нынешний район назван в карточке: Thanh Xuân
  * 46230277 -- cg, 6,000,000 ₫, 15 м²: нынешний район назван в карточке: Cầu Giấy
  * 38933633 -- cg, 8,000,000 ₫, 25 м²: нынешний район назван в карточке: Cầu Giấy
  * 39921757 -- hm, 14,000,000 ₫, 95 м²: нынешний район назван в карточке: Hoàng Mai
  * 46036902 -- hd, 50,000,000 ₫, 250 м²: нынешний район назван в карточке: Hà Đông

ОТСЕЯНО (71):
  * 46126554 -- карточка без квартала -- из общего списка, а не города
  * 46255588 -- карточка без квартала -- из общего списка, а не города
  * 46177299 -- карточка без квартала -- из общего списка, а не города
  * 46086956 -- карточка без квартала -- из общего списка, а не города
  * 46385215 -- карточка без квартала -- из общего списка, а не города
  * 46277180 -- карточка без квартала -- из общего списка, а не города
  * 46334851 -- карточка без квартала -- из общего списка, а не города
  * 45170128 -- карточка без квартала -- из общего списка, а не города
  * 46014467 -- карточка без квартала -- из общего списка, а не города
  * 46365565 -- карточка без квартала -- из общего списка, а не города
  * 46365562 -- карточка без квартала -- из общего списка, а не города
  * 46365511 -- карточка без квартала -- из общего списка, а не города
  * 46365459 -- карточка без квартала -- из общего списка, а не города
  * 45628119 -- карточка без квартала -- из общего списка, а не города
  * 46119973 -- район не назван так, как его знает сайт (phu thuong 1, phu thuong; в карточке «Q. Tây Hồ (P. Phú Thượng mới)»)
  * 42817138 -- район не назван так, как его знает сайт (dai mo; в карточке «Q. Nam Từ Liêm (P. Đại Mỗ mới)»)
  * 45895812 -- цена не читается: Giá thỏa thuận
  * 30125458 -- район не назван так, как его знает сайт (dai mo; в карточке «Q. Nam Từ Liêm (P. Đại Mỗ mới)»)
  * 42941555 -- район не назван так, как его знает сайт (yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 46311988 -- карточка без квартала -- из общего списка, а не города
  * 45466132 -- район не назван так, как его знает сайт (an khanh; в карточке «H. Hoài Đức (X. An Khánh mới)»)
  * 46334480 -- район не назван так, как его знает сайт (lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46369770 -- похоже на уже заведённое: id 1018560
  * 43839348 -- район не назван так, как его знает сайт (dong anh; в карточке «H. Đông Anh (X. Đông Anh mới)»)
  * 46365719 -- район не назван так, как его знает сайт (tuong mai; в карточке «Q. Hoàng Mai (P. Tương Mai mới)»)
  * 46364459 -- старее 6 дней (Đăng 1 tuần trước)
  * 46345563 -- старее 6 дней (Đăng 1 tuần trước)
  * 46386403 -- район не назван так, как его знает сайт (lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46391352 -- район не назван так, как его знает сайт (giang vo; в карточке «Q. Ba Đình (P. Giảng Võ mới)»)
  * 46170205 -- похоже на уже заведённое: id 1018749
  * 46383131 -- район не назван так, как его знает сайт (phu luong; в карточке «Q. Hà Đông (P. Phú Lương mới)»)
  * 46381891 -- район не назван так, как его знает сайт (tu liem; в карточке «Q. Nam Từ Liêm (P. Từ Liêm mới)»)
  * 45704507 -- район не назван так, как его знает сайт (ngoc ha; в карточке «Q. Ba Đình (P. Ngọc Hà mới)»)
  * 46380430 -- район не назван так, как его знает сайт (yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 46379905 -- район не назван так, как его знает сайт (yen nghia; в карточке «Q. Hà Đông (P. Yên Nghĩa mới)»)
  * 46262567 -- район не назван так, как его знает сайт (vinh hung; в карточке «Q. Hoàng Mai (P. Vĩnh Hưng mới)»)
  * 46377996 -- район не назван так, как его знает сайт (cua nam; в карточке «Q. Hoàn Kiếm (P. Cửa Nam mới)»)
  * 46313549 -- карточка без квартала -- из общего списка, а не города
  * 46199714 -- район не назван так, как его знает сайт (phu dong; в карточке «H. Gia Lâm (X. Phù Đổng mới)»)
  * 45687326 -- район не назван так, как его знает сайт (thanh liet; в карточке «Q. Thanh Xuân (P. Thanh Liệt mới)»)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3002062, 3002063, 3002064, 3002065, 3002066, 3002067, 3002068, 3002069, 3002070]
REPLACES = []

NEW_SRC = r'''
L(3002062,"ha-noi","tyh","Квартира",25000000,87,
  "2-спальная квартира, 87 м², Tây Hồ — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-lac-long-quan-d-el-dorado/chinh-chu-cho-gap-659a-tay-ha-noi-pr37721099","вчера",1,source="batdongsan",postedOn="2026-10-06",
  descEn="2-bedroom flat, 87 m², Tây Hồ — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162936-04e9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162940-1ad7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162936-5a20_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162939-011c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162939-f2a4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162941-19c5_wm.jpg"], "am": ["gym"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3002063,"ha-noi","tx","Дом",8000000,90,
  "4-спальный дом, 90 м², Thanh Xuân — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-quy-duc-5/cho-tap-the-e7-uc-4pn-2wc-pr46389346","вчера",1,source="batdongsan",postedOn="2026-10-06",
  descEn="4-bedroom house, 90 m², Thanh Xuân — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/10/06/20261006202050-5e9c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/06/20261006202053-33ed_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/06/20261006202055-8c48_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/06/20261006202057-a4c0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/06/20261006202059-e7a1_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/10/06/20261006202050-5e9c_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3002064,"ha-noi","hm","Дом",5000000,35,
  "Дом, 35 м², Hoàng Mai — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-chinh-khu-chuc-nang-do-thi-ao-sao/cho-2-tang-co-the-kinh-doanh-pr46384200","2 дня назад",2,source="batdongsan",postedOn="2026-10-05",
  descEn="House, 35 m², Hoàng Mai — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005185454-d201_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005185508-9a06_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005185512-02be_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005185603-c691_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005185619-fc5b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/05/20261005185738-0321_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3002065,"ha-noi","tx","Комната",15000000,50,
  "Комната, 50 м², Thanh Xuân — 3 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-pho-quan-nhan-5/cho-trung-tam-thanh-xuan-ngo-3-gac-thong-tu-tung-pr46391710","сегодня",0,source="batdongsan",postedOn="2026-10-07",
  descEn="Room, 50 m², Thanh Xuân — 3 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113028-47d5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113130-1d3c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113132-f396_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113133-8f4f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113134-ff66_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113136-bb47_wm.jpg"], "am": ["k", "b"], "fl": 1, "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3002066,"ha-noi","tx","Комната",15000000,45,
  "Комната, 45 м², Thanh Xuân — 3 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-trai-5/cho-quan-nhan-thanh-xuan-gan-cac-truong-h-lon-dan-cu-tap-nap-tien-ich-xung-quanh-pr46391703","сегодня",0,source="batdongsan",postedOn="2026-10-07",
  descEn="Room, 45 m², Thanh Xuân — 3 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113017-8b0a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113018-be2e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113019-e815_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113019-33e0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113020-c9a3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/10/07/20261007113021-ca46_wm.jpg"], "am": ["k", "b"], "fl": 1, "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3002067,"ha-noi","cg","Комната",6000000,15,
  "Комната, 15 м², Cầu Giấy.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-cau-giay-7/cho-ep-xuat-sac-tai-so-23-ngach-40-ngo-79-2-6-trieu-15m2-pr46230277","сегодня",0,source="batdongsan",postedOn="2026-10-07",
  descEn="Room, 15 m², Cầu Giấy.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923164709-9011_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923164707-9f1f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923164708-ad67_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923164708-e8a1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923164709-0327_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923164706-c91a_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3002068,"ha-noi","cg","Комната",8000000,25,
  "Комната, 25 м², Cầu Giấy — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-tran-thai-tong-phuong-dich-vong-hau-7/cho-ccmn-tai-44-da-day-du-noi-that-chi-can-mang-quan-ao-vao-o-pr38933633","сегодня",0,source="batdongsan",postedOn="2026-10-07",
  descEn="Room, 25 m², Cầu Giấy — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2024/01/03/20240103153139-439a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/01/03/20240103153155-0d10_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/01/03/20240103153208-cb9a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/01/03/20240103153223-04dc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/01/03/20240103153244-81a8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/01/03/20240103153259-6471_wm.jpg"], "am": ["k", "lift", "free"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3002069,"ha-noi","hm","Дом",14000000,95,
  "8-спальный дом, 95 м², Hoàng Mai — 8 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-tan-mai-louis-city-hoang-mai/can-cho-5-can-tai-du-an-dia-chi-54-ha-noi-pr39921757","3 дня назад",3,source="batdongsan",postedOn="2026-10-04",
  descEn="8-bedroom house, 95 m², Hoàng Mai — 8 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/07/10/20260710132551-2fbe_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231802-ea5f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231804-9473_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231805-7071_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231807-a429_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/10/20260710132550-2a56_wm.jpg"], "am": ["lift"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3002070,"ha-noi","hd","Дом",50000000,250,
  "Дом, 250 м², Hà Đông — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-phuong-mo-lao-khu-do-thi-mo-lao/chinh-chu-can-cho-on-lap-o-dien-tich-250m2-pr46036902","5 дней назад",5,source="batdongsan",postedOn="2026-10-02",
  descEn="House, 250 m², Hà Đông — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/07/13/20260713064622-9cf9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/13/20260713064623-57da_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/13/20260713064623-3e27_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/13/20260713064624-0951_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/13/20260713064625-ae18_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/07/13/20260713064622-9cf9_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
