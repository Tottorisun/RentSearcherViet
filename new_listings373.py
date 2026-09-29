# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 10 строк, 2026-09-29, город ha-noi.

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
  * 46349520 -- cg, 20,000,000 ₫, 120 м²: нынешний район назван в карточке: Cầu Giấy
  * 46347524 -- hbt, 5,000,000 ₫, 32 м²: нынешний район назван в карточке: Hai Bà Trưng
  * 46357501 -- tyh, 25,000,000 ₫, 95 м²: нынешний район назван в карточке: Tây Hồ
  * 46354068 -- lbn, 14,000,000 ₫, 58 м²: квартал в адресе объявления: long bien
  * 46201051 -- hkm, 5,000,000 ₫, 25 м²: нынешний район назван в карточке: Hoàn Kiếm
  * 46195997 -- hkm, 16,000,000 ₫, 50 м²: нынешний район назван в карточке: Hoàn Kiếm
  * 46168871 -- hd, 5,000,000 ₫, 35 м²: нынешний район назван в карточке: Hà Đông
  * 46352520 -- cg, 75,000,000 ₫, 50 м²: нынешний район назван в карточке: Cầu Giấy
  * 39921757 -- hm, 14,000,000 ₫, 95 м²: нынешний район назван в карточке: Hoàng Mai

ОТСЕЯНО (70):
  * 46277180 -- карточка без квартала -- из общего списка, а не города
  * 46357881 -- карточка без квартала -- из общего списка, а не города
  * 46086956 -- карточка без квартала -- из общего списка, а не города
  * 46177299 -- карточка без квартала -- из общего списка, а не города
  * 41111280 -- карточка без квартала -- из общего списка, а не города
  * 45628119 -- карточка без квартала -- из общего списка, а не города
  * 46009006 -- карточка без квартала -- из общего списка, а не города
  * 46335362 -- карточка без квартала -- из общего списка, а не города
  * 46328985 -- карточка без квартала -- из общего списка, а не города
  * 46326427 -- карточка без квартала -- из общего списка, а не города
  * 46307166 -- карточка без квартала -- из общего списка, а не города
  * 46305932 -- карточка без квартала -- из общего списка, а не города
  * 46303995 -- карточка без квартала -- из общего списка, а не города
  * 46360432 -- цена не читается: Giá thỏa thuận
  * 46161033 -- район не назван так, как его знает сайт (tay mo vinhomes, tay mo; в карточке «Q. Nam Từ Liêm (P. Tây Mỗ mới)»)
  * 42363013 -- цена не читается: Giá thỏa thuận
  * 46273608 -- район не назван так, как его знает сайт (vinh tuy; в карточке «Q. Hai Bà Trưng (P. Vĩnh Tuy mới)»)
  * 46357764 -- район не назван так, как его знает сайт (dong ngac sunshine, phu thuong; в карточке «Q. Bắc Từ Liêm (P. Phú Thượng mới)»)
  * 46357747 -- район не назван так, как его знает сайт (dong ngac sunshine, phu thuong; в карточке «Q. Bắc Từ Liêm (P. Phú Thượng mới)»)
  * 45768043 -- район не назван так, как его знает сайт (bach mai 4, bach mai; в карточке «Q. Hai Bà Trưng (P. Bạch Mai mới)»)
  * 46345563 -- район не назван так, как его знает сайт (kien hung 15, kien hung; в карточке «Q. Hà Đông (P. Kiến Hưng mới)»)
  * 46335148 -- район не назван так, как его знает сайт (yen hoa 2, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 46334480 -- район не назван так, как его знает сайт (lang ha 3, lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46329171 -- старее 6 дней (Đăng 1 tuần trước)
  * 46325788 -- старее 6 дней (Đăng 1 tuần trước)
  * 45167230 -- старее 6 дней (Đăng 1 tuần trước)
  * 46197980 -- старее 6 дней (Đăng 1 tuần trước)
  * 46359415 -- район не назван так, как его знает сайт (nghia do; в карточке «Q. Bắc Từ Liêm (P. Nghĩa Đô mới)»)
  * 46314656 -- район не назван так, как его знает сайт (gia lam; в карточке «H. Gia Lâm (X. Gia Lâm mới)»)
  * 44671493 -- район не назван так, как его знает сайт (tuong mai, tuong mai; в карточке «Q. Hoàng Mai (P. Tương Mai mới)»)
  * 46209036 -- район не назван так, как его знает сайт (dinh cong 8, dinh cong; в карточке «Q. Hoàng Mai (P. Định Công mới)»)
  * 46254252 -- район не назван так, как его знает сайт (khuong dinh 5, khuong dinh; в карточке «Q. Thanh Xuân (P. Khương Đình mới)»)
  * 45830490 -- район не назван так, как его знает сайт (dai kim, dinh cong; в карточке «Q. Hoàng Mai (P. Định Công mới)»)
  * 46355053 -- район не назван так, как его знает сайт (dinh cong; в карточке «Q. Hoàng Mai (P. Định Công mới)»)
  * 46032566 -- район не назван так, как его знает сайт (me tri 14, tu liem; в карточке «Q. Nam Từ Liêm (P. Từ Liêm mới)»)
  * 46182139 -- район не назван так, как его знает сайт (hoang liet 8, hoang liet; в карточке «Q. Hoàng Mai (P. Hoàng Liệt mới)»)
  * 46216050 -- район не назван так, как его знает сайт (cau dien 14, tu liem; в карточке «Q. Nam Từ Liêm (P. Từ Liêm mới)»)
  * 32573231 -- район не назван так, как его знает сайт (bach dang 4, hong ha; в карточке «Q. Hai Bà Trưng (P. Hồng Hà mới)»)
  * 45591297 -- старее 6 дней (Đăng 1 tuần trước)
  * 46354780 -- район не назван так, как его знает сайт (me tri, tu liem; в карточке «Q. Nam Từ Liêm (P. Từ Liêm mới)»)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001707, 3001708, 3001709, 3001710, 3001711, 3001712, 3001713, 3001714, 3001715, 3001716]
REPLACES = []

NEW_SRC = r'''
L(3001707,"ha-noi","tyh","Квартира",25000000,87,
  "2-спальная квартира, 87 м², Tây Hồ — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-lac-long-quan-d-el-dorado/chinh-chu-cho-gap-659a-tay-ha-noi-pr37721099","сегодня",0,source="batdongsan",postedOn="2026-09-29",
  descEn="2-bedroom flat, 87 m², Tây Hồ — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162936-04e9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162940-1ad7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162936-5a20_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162939-011c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162939-f2a4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/07/21/20230721162941-19c5_wm.jpg"], "am": ["gym"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001708,"ha-noi","cg","Дом",20000000,120,
  "6-спальный дом, 120 м², Cầu Giấy — 6 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-thien-hien-phuong-my-dinh-1-14/cho-san-hoac-ca-toa-gia-re-pr46349520","3 дня назад",3,source="batdongsan",postedOn="2026-09-26",
  descEn="6-bedroom house, 120 m², Cầu Giấy — 6 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926230359-730d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926230408-576a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926230421-598f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926230432-441c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926230443-55e3_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/26/20260926230359-730d_wm.jpg"], "am": ["lift"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001709,"ha-noi","hbt","Дом",5000000,32,
  "2-спальный дом, 32 м², Hai Bà Trưng — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-lo-duc-phuong-dong-nhan-4/can-cho-1-tang-tai-quan-hai-ba-trung-ha-noi-pr46347524","3 дня назад",3,source="batdongsan",postedOn="2026-09-26",
  descEn="2-bedroom house, 32 m², Hai Bà Trưng — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926110647-08e2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926110647-3e66_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/26/20260926110647-6735_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/26/20260926110647-08e2_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/26/20260926110647-3e66_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/26/20260926110647-6735_wm.jpg"], "am": ["k"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001710,"ha-noi","tyh","Дом",25000000,95,
  "3-спальный дом, 95 м², Tây Hồ — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-hoang-hoa-tham-6/cho-uong-p-tay-ho-ha-noi-pr46357501","сегодня",0,source="batdongsan",postedOn="2026-09-29",
  descEn="3-bedroom house, 95 m², Tây Hồ — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/29/20260929103711-def5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/29/20260929103711-6cb5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/29/20260929103711-50ef_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/29/20260929103711-d9a9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/29/20260929103711-bf21_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/29/20260929103711-4861_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001711,"ha-noi","lbn","Дом",14000000,58,
  "Дом, 58 м², Long Biên — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-bat-khoi-phuong-long-bien-9/chinh-chu-cho-5-tang-nguyen-can-dt-58m2-mat-tien-rong-phu-hop-o-ket-hop-kinh-doanh-pr46354068","вчера",1,source="batdongsan",postedOn="2026-09-28",
  descEn="House, 58 m², Long Biên — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153515-cb8a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153516-5dd8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153517-2f24_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153515-efe0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153517-ab89_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/17/20260717153517-de28_wm.jpg"], "am": ["k"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001712,"ha-noi","hkm","Дом",5000000,25,
  "1-спальный дом, 25 м², Hoàn Kiếm — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-hang-bac-phuong-hang-bac-1/cho-1-ngu-bep-ve-sinh-khep-kin-pr46201051","вчера",1,source="batdongsan",postedOn="2026-09-28",
  descEn="1-bedroom house, 25 m², Hoàn Kiếm — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/19/20260819114503-f4ce_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/19/20260819114503-9760_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/19/20260819114504-8afd_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/19/20260819114503-f4ce_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/19/20260819114503-9760_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/19/20260819114504-8afd_wm.jpg"], "am": ["k"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001713,"ha-noi","hkm","Дом",16000000,50,
  "4-спальный дом, 50 м², Hoàn Kiếm — 3 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ly-thai-to-phuong-ly-thai-to-1/cho-pho-hoan-kiem-dt-55m2-x-4t-thang-9-don-vao-chi-cho-gia-inh-pr46195997","вчера",1,source="batdongsan",postedOn="2026-09-28",
  descEn="4-bedroom house, 50 m², Hoàn Kiếm — 3 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/18/20260818112905-2301_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/18/20260818112905-6733_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/18/20260818112905-adb1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/18/20260818112905-6e80_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/18/20260818112905-2301_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/18/20260818112905-6733_wm.jpg"], "am": ["k"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001714,"ha-noi","hd","Дом",5000000,35,
  "2-спальный дом, 35 м², Hà Đông — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-tan-xa-phuong-phuc-la-15/nguyen-can-2-5-tang-35m2-ha-ong-canh-hv-quan-y-103-pr46168871","2 дня назад",2,source="batdongsan",postedOn="2026-09-27",
  descEn="2-bedroom house, 35 m², Hà Đông — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/11/20260811214957-c216_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/11/20260811214957-83e7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/11/20260811214957-2c08_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/11/20260811214957-8228_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/11/20260811214957-29f8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/27/20260927165424-7213_wm.jpg"], "am": ["k"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001715,"ha-noi","cg","Комната",75000000,50,
  "Комната, 50 м², Cầu Giấy — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-com-vong-7/chinh-chu-cho-ktx-giuong-tang-cao-cap-gia-uu-ai-1-750k-thang-tron-goi-khong-phat-sinh-pr46352520","вчера",1,source="batdongsan",postedOn="2026-09-28",
  descEn="Room, 50 m², Cầu Giấy — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/02/24/20250224102124-09e5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/02/24/20250224102123-648a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/02/24/20250224102123-bda4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/02/24/20250224102123-c177_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/02/24/20250224102123-c830_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/02/24/20250224102123-d15f_wm.jpg"], "am": ["lift"], "flHigh": 1, "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001716,"ha-noi","hm","Дом",14000000,95,
  "8-спальный дом, 95 м², Hoàng Mai — 8 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-tan-mai-phuong-hoang-van-thu-4-louis-city-hoang-mai/can-cho-5-can-tai-du-an-dia-chi-54-ha-noi-pr39921757","2 дня назад",2,source="batdongsan",postedOn="2026-09-27",
  descEn="8-bedroom house, 95 m², Hoàng Mai — 8 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/07/10/20260710132551-2fbe_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231802-ea5f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231804-9473_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231805-7071_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231807-a429_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/10/20260710132550-2a56_wm.jpg"], "am": ["lift"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
