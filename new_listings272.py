# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 7 строк, 2026-09-21, город ha-noi.

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
  * 45167230 -- dd, 38,000,000 ₫, 67 м²: нынешний район назван в карточке: Đống Đa
  * 46230430 -- dd, 14,000,000 ₫, 110 м²: нынешний район назван в карточке: Đống Đa
  * 46322063 -- tyh, 12,000,000 ₫, 43 м²: нынешний район назван в карточке: Tây Hồ
  * 46098564 -- tx, 3,000,000 ₫, 20 м²: нынешний район назван в карточке: Thanh Xuân; перевыложено -- заменяет id 3000764 (те же фотографии)
  * 45668501 -- hkm, 2,000,000 ₫, 15 м²: нынешний район назван в карточке: Hoàn Kiếm
  * 39921757 -- hm, 14,000,000 ₫, 95 м²: нынешний район назван в карточке: Hoàng Mai
  * 46322418 -- hm, 50,000,000 ₫, 218 м²: нынешний район назван в карточке: Hoàng Mai

ОТСЕЯНО (73):
  * 46255588 -- карточка без квартала -- из общего списка, а не города
  * 46105341 -- карточка без квартала -- из общего списка, а не города
  * 46126554 -- карточка без квартала -- из общего списка, а не города
  * 46307166 -- карточка без квартала -- из общего списка, а не города
  * 46317251 -- карточка без квартала -- из общего списка, а не города
  * 45323490 -- карточка без квартала -- из общего списка, а не города
  * 46086956 -- карточка без квартала -- из общего списка, а не города
  * 46309306 -- карточка без квартала -- из общего списка, а не города
  * 45938799 -- карточка без квартала -- из общего списка, а не города
  * 46277180 -- карточка без квартала -- из общего списка, а не города
  * 46305932 -- карточка без квартала -- из общего списка, а не города
  * 46104079 -- карточка без квартала -- из общего списка, а не города
  * 46303995 -- карточка без квартала -- из общего списка, а не города
  * 46302744 -- карточка без квартала -- из общего списка, а не города
  * 45312749 -- карточка без квартала -- из общего списка, а не города
  * 46283509 -- район не назван так, как его знает сайт (dong ngac sunshine, phu thuong; в карточке «Q. Bắc Từ Liêm (P. Phú Thượng mới)»)
  * 46277849 -- район не назван так, как его знает сайт (vinh tuy green, vinh tuy; в карточке «Q. Hai Bà Trưng (P. Vĩnh Tuy mới)»)
  * 44254074 -- район не назван так, как его знает сайт (me tri vinhomes, dai mo; в карточке «Q. Nam Từ Liêm (P. Đại Mỗ mới)»)
  * 45301933 -- район не назван так, как его знает сайт (ngoc khanh vinhomes, ngoc ha; в карточке «Q. Ba Đình (P. Ngọc Hà mới)»)
  * 44804267 -- район не назван так, как его знает сайт (me tri vinhomes, dai mo; в карточке «Q. Nam Từ Liêm (P. Đại Mỗ mới)»)
  * 46228920 -- карточка без квартала -- из общего списка, а не города
  * 46132432 -- район не назван так, как его знает сайт (thanh nhan 4, bach mai; в карточке «Q. Hai Bà Trưng (P. Bạch Mai mới)»)
  * 46311988 -- уже на сайте
  * 46197980 -- район не назван так, как его знает сайт (bo de 9, bo de; в карточке «Q. Long Biên (P. Bồ Đề mới)»)
  * 45913572 -- район не назван так, как его знает сайт (quan hoa 7, nghia do; в карточке «Q. Cầu Giấy (P. Nghĩa Đô mới)»)
  * 46297749 -- старее 6 дней (Đăng 1 tuần trước)
  * 46290354 -- старее 6 дней (Đăng 1 tuần trước)
  * 38992140 -- старее 6 дней (Đăng 1 tuần trước)
  * 46285359 -- старее 6 дней (Đăng 1 tuần trước)
  * 46009685 -- район не назван так, как его знает сайт (lang thuong 3, lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46282222 -- район не назван так, как его знает сайт (phu do, tu liem; в карточке «Q. Nam Từ Liêm (P. Từ Liêm mới)»)
  * 46323844 -- район не назван так, как его знает сайт (o cho dua, o cho dua; в карточке «Q. Đống Đa (P. Ô Chợ Dừa mới)»)
  * 46323494 -- район не назван так, как его знает сайт (lien mac 718, thuong cat; в карточке «Q. Bắc Từ Liêm (P. Thượng Cát mới)»)
  * 46245240 -- похоже на уже заведённое: id 1006142
  * 46271331 -- район не назван так, как его знает сайт (lang thuong 3, lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46318432 -- район не назван так, как его знает сайт (khuong dinh 5, khuong dinh; в карточке «Q. Thanh Xuân (P. Khương Đình mới)»)
  * 46317343 -- район не назван так, как его знает сайт (linh nam 8, vinh hung; в карточке «Q. Hoàng Mai (P. Vĩnh Hưng mới)»)
  * 46313549 -- район не назван так, как его знает сайт (giap bat 8, tuong mai; в карточке «Q. Hoàng Mai (P. Tương Mai mới)»)
  * 45830490 -- старее 6 дней (Đăng 1 tuần trước)
  * 46199714 -- район не назван так, как его знает сайт (phu dong; в карточке «H. Gia Lâm (X. Phù Đổng mới)»)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001081, 3001082, 3001083, 3001084, 3001085, 3001086, 3001087]
REPLACES = [3000764]

NEW_SRC = r'''
L(3001081,"ha-noi","dd","Дом",38000000,67,
  "Дом, 67 м², Đống Đa.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-thai-ha-phuong-trung-liet-3/cho-ha-pr45167230","вчера",1,source="batdongsan",postedOn="2026-09-20",
  descEn="House, 67 m², Đống Đa.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/03/24/20260324183232-5a8c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/03/24/20260324183232-80f2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/03/24/20260324183232-1705_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/03/24/20260324183232-5a8c_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/03/24/20260324183232-80f2_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/03/24/20260324183232-1705_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001082,"ha-noi","dd","Дом",14000000,110,
  "3-спальный дом, 110 м², Đống Đa — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-hao-nam-phuong-o-cho-dua-3/nr-3pn-2wc-110m2-gia-uu-ai-14-trieu-tai-ngach-127-28-ha-noi-pr46230430","вчера",1,source="batdongsan",postedOn="2026-09-20",
  descEn="3-bedroom house, 110 m², Đống Đa — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163500-513d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163501-88c7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163502-6286_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163504-255a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163505-5afc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826163505-5093_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001083,"ha-noi","tyh","Дом",12000000,43,
  "3-спальный дом, 43 м², Tây Hồ — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-au-co-phuong-quang-an-2-6/cho-nguyen-can-tai-39-co-pr46322063","вчера",1,source="batdongsan",postedOn="2026-09-20",
  descEn="3-bedroom house, 43 m², Tây Hồ — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920113252-20f8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920113252-6521_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920113250-ee61_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920113250-ac76_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920113250-c811_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920113251-8991_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001084,"ha-noi","tx","Комната",3000000,20,
  "Комната, 20 м², Thanh Xuân.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-pho-chinh-kinh-phuong-nhan-chinh-5/chi-3tr-nga-tu-so-gia-re-sinh-vien-pr46098564","сегодня",0,source="batdongsan",postedOn="2026-09-21",
  descEn="Room, 20 m², Thanh Xuân.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100836-e4e2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100824-fbb9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100829-4cb1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100831-1594_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100827-280d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100822-8ae0_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001085,"ha-noi","hkm","Комната",2000000,15,
  "Комната, 15 м², Hoàn Kiếm — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-pho-hang-khay-phuong-trang-tien-1/cho-giuong-homestay-so-29-ay-u-nghi-sat-ho-guom-view-trieu-o-pr45668501","сегодня",0,source="batdongsan",postedOn="2026-09-21",
  descEn="Room, 15 m², Hoàn Kiếm — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/11/20260811102908-b54a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/05/20260505093554-a4f8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/05/20260505093555-9e3a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/05/20260505093553-4596_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/05/20260505093555-8901_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/05/20260505093557-dce8_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001086,"ha-noi","hm","Дом",14000000,95,
  "8-спальный дом, 95 м², Hoàng Mai — 8 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-tan-mai-phuong-hoang-van-thu-4-louis-city-hoang-mai/can-cho-5-can-tai-du-an-dia-chi-54-ha-noi-pr39921757","вчера",1,source="batdongsan",postedOn="2026-09-20",
  descEn="8-bedroom house, 95 m², Hoàng Mai — 8 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/07/10/20260710132551-2fbe_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231802-ea5f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231804-9473_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231805-7071_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/05/19/20250519231807-a429_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/10/20260710132550-2a56_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001087,"ha-noi","hm","Дом",50000000,218,
  "4-спальный дом, 218 м², Hoàng Mai — 4 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-nguyen-tam-trinh-phuong-tran-phu-7-gamuda-gardens/cho-218m-3-5-tang-full-noi-that-pr46322418","вчера",1,source="batdongsan",postedOn="2026-09-20",
  descEn="4-bedroom house, 218 m², Hoàng Mai — 4 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920142713-2afa_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920142748-bf85_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920142835-1d77_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920142903-7c74_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920142917-df8d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/20/20260920142934-ea9b_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
