# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 7 строк, 2026-09-24, город ha-noi.

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
  * 46235874 -- tx, 19,000,000 ₫, 96 м²: нынешний район назван в карточке: Thanh Xuân
  * 45875769 -- tx, 13,000,000 ₫, 35 м²: нынешний район назван в карточке: Thanh Xuân
  * 46267180 -- tx, 48,000,000 ₫, 100 м²: нынешний район назван в карточке: Thanh Xuân
  * 46333971 -- tx, 60,000,000 ₫, 110 м²: квартал в адресе объявления: thanh xuan
  * 46332519 -- hbt, 5,000,000 ₫, 27 м²: нынешний район назван в карточке: Hai Bà Trưng
  * 46300808 -- tx, 3,000,000 ₫, 20 м²: нынешний район назван в карточке: Thanh Xuân; перевыложено -- заменяет id 3001084 (те же фотографии)
  * 46338523 -- hd, 40,000,000 ₫, 500 м²: нынешний район назван в карточке: Hà Đông

ОТСЕЯНО (73):
  * 46255588 -- карточка без квартала -- из общего списка, а не города
  * 46126554 -- карточка без квартала -- из общего списка, а не города
  * 46086956 -- карточка без квартала -- из общего списка, а не города
  * 46335362 -- карточка без квартала -- из общего списка, а не города
  * 46105341 -- карточка без квартала -- из общего списка, а не города
  * 46328985 -- карточка без квартала -- из общего списка, а не города
  * 46328587 -- карточка без квартала -- из общего списка, а не города
  * 46326427 -- карточка без квартала -- из общего списка, а не города
  * 46307166 -- карточка без квартала -- из общего списка, а не города
  * 46317251 -- карточка без квартала -- из общего списка, а не города
  * 45323490 -- карточка без квартала -- из общего списка, а не города
  * 46309306 -- карточка без квартала -- из общего списка, а не города
  * 46305932 -- карточка без квартала -- из общего списка, а не города
  * 46303995 -- карточка без квартала -- из общего списка, а не города
  * 46301102 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 46277849 -- район не назван так, как его знает сайт (vinh tuy green, vinh tuy; в карточке «Q. Hai Bà Trưng (P. Vĩnh Tuy mới)»)
  * 37686751 -- район не назван так, как его знает сайт (phu thuong 1, hong ha; в карточке «Q. Tây Hồ (P. Hồng Hà mới)»)
  * 46335396 -- район не назван так, как его знает сайт (me tri vov, dai mo; в карточке «Q. Nam Từ Liêm (P. Đại Mỗ mới)»)
  * 46334851 -- район не назван так, как его знает сайт (lang thuong lancaster, lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46228920 -- карточка без квартала -- из общего списка, а не города
  * 46335148 -- район не назван так, как его знает сайт (yen hoa 2, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 46334480 -- район не назван так, как его знает сайт (lang ha 3, lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46329171 -- район не назван так, как его знает сайт (trung van 14, dai mo; в карточке «Q. Nam Từ Liêm (P. Đại Mỗ mới)»)
  * 46325788 -- район не назван так, как его знает сайт (gia lam; в карточке «H. Gia Lâm (X. Gia Lâm mới)»)
  * 45167230 -- уже на сайте
  * 46132432 -- район не назван так, как его знает сайт (thanh nhan 4, bach mai; в карточке «Q. Hai Bà Trưng (P. Bạch Mai mới)»)
  * 46311988 -- уже на сайте
  * 46197980 -- старее 6 дней (Đăng 1 tuần trước)
  * 46297749 -- старее 6 дней (Đăng 1 tuần trước)
  * 46290354 -- старее 6 дней (Đăng 1 tuần trước)
  * 38992140 -- старее 6 дней (Đăng 1 tuần trước)
  * 46285359 -- старее 6 дней (Đăng 1 tuần trước)
  * 44622428 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 40284543 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 46331907 -- район не назван так, как его знает сайт (dai thanh; в карточке «H. Thanh Trì (X. Đại Thanh mới)»)
  * 45830490 -- район не назван так, как его знает сайт (dai kim, dinh cong; в карточке «Q. Hoàng Mai (P. Định Công mới)»)
  * 46313549 -- старее 6 дней (Đăng 1 tuần trước)
  * 32573231 -- район не назван так, как его знает сайт (bach dang 4, hong ha; в карточке «Q. Hai Bà Trưng (P. Hồng Hà mới)»)
  * 46331617 -- район не назван так, как его знает сайт (phuc tan 1, hong ha; в карточке «Q. Hoàn Kiếm (P. Hồng Hà mới)»)
  * 46250253 -- район не назван так, как его знает сайт (duong noi khu, duong noi; в карточке «Q. Hà Đông (P. Dương Nội mới)»)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001285, 3001286, 3001287, 3001288, 3001289, 3001290, 3001291]
REPLACES = [3001084]

NEW_SRC = r'''
L(3001285,"ha-noi","tx","Квартира",19000000,96,
  "2-спальная квартира, 96 м², Thanh Xuân — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-le-van-luong-phuong-nhan-chinh-star-city-le-van-luong-28171/hot-sieu-tiet-kiem-sieu-tien-cho-2pn-96m2-tai-19-trieu-vnd-pr46235874","вчера",1,source="batdongsan",postedOn="2026-09-23",
  descEn="2-bedroom flat, 96 m², Thanh Xuân — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828095953-0e6b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828095954-893c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828095955-33e2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828095956-6cc1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828095956-d213_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828095958-b776_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001286,"ha-noi","tx","Дом",13000000,35,
  "4-спальный дом, 35 м², Thanh Xuân — 5 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-le-van-luong-phuong-nhan-chinh-5/cho-ca-toa-ngo-21-uong-6-tang-moi-tang-la-1-phong-khep-kin-pr45875769","2 дня назад",2,source="batdongsan",postedOn="2026-09-22",
  descEn="4-bedroom house, 35 m², Thanh Xuân — 5 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608143421-5a8b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608143419-72f1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608143419-2c38_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608143420-d1ee_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608143419-d72a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608143419-c232_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001287,"ha-noi","tx","Дом",48000000,100,
  "Дом, 100 м², Thanh Xuân — 2 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-nguy-nhu-kon-tum_1-phuong-nhan-chinh-5/chu-cho-2-tang-kinh-doanh-tai-so-6-ngo-68-tum-pr46267180","3 дня назад",3,source="batdongsan",postedOn="2026-09-21",
  descEn="House, 100 m², Thanh Xuân — 2 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142601-3e9f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142602-41ee_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142604-803a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142605-4f1d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142606-4acc_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/07/20260907142608-87ae_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001288,"ha-noi","tx","Дом",60000000,110,
  "Дом, 110 м², Thanh Xuân.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-truong-chinh-phuong-thanh-xuan-trung-5/chu-can-cho-vuong-thua-vu-dt-110m2-xay-6t-1-thang-may-cuoi-pr46333971","вчера",1,source="batdongsan",postedOn="2026-09-23",
  descEn="House, 110 m², Thanh Xuân.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923095214-4287_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923095214-b027_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923095214-f799_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/23/20260923095214-48c8_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/23/20260923095214-4287_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/23/20260923095214-b027_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001289,"ha-noi","hbt","Дом",5000000,27,
  "1-спальный дом, 27 м², Hai Bà Trưng — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-van-ho-3-phuong-le-dai-hanh-4/dien-tich-27m-mat-tien-2m-xay-2-5-tang-pr46332519","вчера",1,source="batdongsan",postedOn="2026-09-23",
  descEn="1-bedroom house, 27 m², Hai Bà Trưng — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/22/20260922194339-65c3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/22/20260922194339-bdff_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/22/20260922194339-cf30_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/22/20260922194339-4997_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/22/20260922194339-680d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/22/20260922194340-5ca7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001290,"ha-noi","tx","Комната",3000000,20,
  "Комната, 20 м², Thanh Xuân.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-pho-chinh-kinh-phuong-nhan-chinh-5/chi-3tr-nga-tu-so-gia-re-sinh-vien-pr46300808","сегодня",0,source="batdongsan",postedOn="2026-09-24",
  descEn="Room, 20 m², Thanh Xuân.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100824-fbb9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100831-1594_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100829-4cb1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100822-8ae0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100834-81f5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/08/19/20250819100827-280d_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001291,"ha-noi","hd","Дом",40000000,500,
  "Дом, 500 м², Hà Đông — 7 санузлов.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-to-huu-phuong-van-phuc-1-him-lam-van-phuc/toi-can-cho-khu-o-thi-hoan-thien-ay-u-ieu-hoa-thang-may-pr46338523","сегодня",0,source="batdongsan",postedOn="2026-09-24",
  descEn="House, 500 m², Hà Đông — 7 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093745-a0b4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093707-a32f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093813-109a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093813-2b36_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924093813-96ce_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/24/20260924093745-a0b4_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
