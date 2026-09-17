# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 3 строки, 2026-09-17, город ha-noi.

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
  * 46311988 -- hbt, 30,000,000 ₫, 43 м²: нынешний район назван в карточке: Hai Bà Trưng
  * 46304610 -- tyh, 5,000,000 ₫, 70 м²: нынешний район назван в карточке: Tây Hồ
  * 46310255 -- tyh, 5,000,000 ₫, 45 м²: нынешний район назван в карточке: Tây Hồ

ОТСЕЯНО (77):
  * 46086956 -- карточка без квартала -- из общего списка, а не города
  * 46309306 -- карточка без квартала -- из общего списка, а не города
  * 45938799 -- карточка без квартала -- из общего списка, а не города
  * 46126554 -- карточка без квартала -- из общего списка, а не города
  * 46105341 -- карточка без квартала -- из общего списка, а не города
  * 46307166 -- карточка без квартала -- из общего списка, а не города
  * 46277180 -- карточка без квартала -- из общего списка, а не города
  * 46305932 -- карточка без квартала -- из общего списка, а не города
  * 46104079 -- карточка без квартала -- из общего списка, а не города
  * 46303995 -- карточка без квартала -- из общего списка, а не города
  * 46302744 -- карточка без квартала -- из общего списка, а не города
  * 46255588 -- карточка без квартала -- из общего списка, а не города
  * 45312749 -- карточка без квартала -- из общего списка, а не города
  * 46009006 -- карточка без квартала -- из общего списка, а не города
  * 46170734 -- карточка без квартала -- из общего списка, а не города
  * 46273608 -- карточка без квартала -- из общего списка, а не города
  * 42941555 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 42363013 -- цена не читается: Giá thỏa thuận
  * 45679716 -- район не назван так, как его знает сайт (vinh tuy times, vinh tuy; в карточке «Q. Hai Bà Trưng (P. Vĩnh Tuy mới)»)
  * 46301102 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 46228920 -- карточка без квартала -- из общего списка, а не города
  * 46197980 -- район не назван так, как его знает сайт (bo de 9, bo de; в карточке «Q. Long Biên (P. Bồ Đề mới)»)
  * 45913572 -- район не назван так, как его знает сайт (quan hoa 7, nghia do; в карточке «Q. Cầu Giấy (P. Nghĩa Đô mới)»)
  * 46297749 -- район не назван так, как его знает сайт (minh khai 4, tuong mai; в карточке «Q. Hai Bà Trưng (P. Tương Mai mới)»)
  * 46290354 -- район не назван так, как его знает сайт (trung hoa 4, yen hoa; в карточке «Q. Cầu Giấy (P. Yên Hòa mới)»)
  * 38992140 -- район не назван так, как его знает сайт (bach mai 4, bach mai; в карточке «Q. Hai Bà Trưng (P. Bạch Mai mới)»)
  * 46285359 -- район не назван так, как его знает сайт (o cho dua, o cho dua; в карточке «Q. Đống Đa (P. Ô Chợ Dừa mới)»)
  * 46267180 -- старее 6 дней (Đăng 1 tuần trước)
  * 46245240 -- похоже на уже заведённое: id 1002286
  * 46271331 -- район не назван так, как его знает сайт (lang thuong 3, lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46307644 -- цена не читается: Giá thỏa thuận
  * 46303972 -- район не назван так, как его знает сайт (giang vo 2, giang vo; в карточке «Q. Ba Đình (P. Giảng Võ mới)»)
  * 46299938 -- район не назван так, как его знает сайт (my dinh 1, pr46299938, tu liem; в карточке «Q. Nam Từ Liêm (P. Từ Liêm mới)»)
  * 46257466 -- уже на сайте
  * 45930803 -- район не назван так, как его знает сайт (phuc xa 2, hong ha; в карточке «Q. Ba Đình (P. Hồng Hà mới)»)
  * 46297883 -- уже на сайте
  * 46297747 -- район не назван так, как его знает сайт (lang ha 3, lang; в карточке «Q. Đống Đa (P. Láng mới)»)
  * 46136025 -- район не назван так, как его знает сайт (viet hung 2, viet hung; в карточке «Q. Long Biên (P. Việt Hưng mới)»)
  * 45830490 -- старее 6 дней (Đăng 1 tuần trước)
  * 46254882 -- старее 6 дней (Đăng 1 tuần trước)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3000861, 3000862, 3000863]
REPLACES = []

NEW_SRC = r'''
L(3000861,"ha-noi","hbt","Дом",30000000,43,
  "Дом, 43 м², Hai Bà Trưng.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-dinh-chieu-phuong-le-dai-hanh-4/cho-6-tang-ven-ho-cong-vien-thong-nhat-inh-o-to-thang-may-phu-hop-lam-spa-pr46311988","сегодня",0,source="batdongsan",postedOn="2026-09-17",
  descEn="House, 43 m², Hai Bà Trưng.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826134913-ecd6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826134919-e328_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826134932-9396_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826134947-acca_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826135015-2b84_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/26/20260826135015-3fb2_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000862,"ha-noi","tyh","Дом",5000000,70,
  "6-спальный дом, 70 м², Tây Hồ.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-lac-long-quan-phuong-nhat-tan-2-6/cho-4-tang-ngo-47-view-ho-tay-o-to-o-ca-2-chieu-pr46304610","вчера",1,source="batdongsan",postedOn="2026-09-16",
  descEn="6-bedroom house, 70 m², Tây Hồ.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916083755-7bb0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916083755-a316_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916083755-b32e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/16/20260916083755-3910_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/16/20260916083755-7bb0_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/16/20260916083755-a316_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000863,"ha-noi","tyh","Комната",5000000,45,
  "Комната, 45 м², Tây Hồ.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-phuong-thuy-khue/chinh-chu-cho-tang-1-va-tang-2-dt-50-45m2-ien-nuoc-gia-binh-dan-lh-cc-07746451-pr46310255","сегодня",0,source="batdongsan",postedOn="2026-09-17",
  descEn="Room, 45 m², Tây Hồ.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/17/20260917090857-f22c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/17/20260917090857-232b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/17/20260917090857-fb3b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/17/20260917090857-112f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/17/20260917090858-5e6b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/17/20260917090858-7455_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
