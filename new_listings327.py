# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 7 строк, 2026-09-25, город quy-nhon.

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
  * 46343644 -- qnn, 5,000,000 ₫, 46 м²: нынешний район назван в карточке: Quy Nhơn Nam
  * 46340525 -- qn, 5,000,000 ₫, 46 м²: нынешний район назван в карточке: Quy Nhơn
  * 44116108 -- qn, 8,000,000 ₫, 72 м²: нынешний район назван в карточке: Quy Nhơn
  * 42303849 -- qn, 7,000,000 ₫, 52 м²: нынешний район назван в карточке: Quy Nhơn
  * 42303705 -- qn, 12,000,000 ₫, 96 м²: нынешний район назван в карточке: Quy Nhơn
  * 37302356 -- qnd, 5,000,000 ₫, 64 м²: нынешний район назван в карточке: Quy Nhơn Đông
  * 45577797 -- qnn, 6,000,000 ₫, 46 м²: нынешний район назван в карточке: Quy Nhơn Nam

ОТСЕЯНО (19):
  * 44186366 -- цена не читается: Giá thỏa thuận
  * 44066604 -- похоже на уже заведённое: id 1010989
  * 39050071 -- похоже на уже заведённое: id new:46343644
  * 45577841 -- цена не читается: Giá thỏa thuận
  * 42954925 -- уже на сайте
  * 43127816 -- старее 6 дней (Đăng 1 tuần trước)
  * 39050214 -- старее 6 дней (Đăng 1 tuần trước)
  * 45408592 -- старее 6 дней (Đăng 1 tuần trước)
  * 45408563 -- старее 6 дней (Đăng 1 tuần trước)
  * 46286935 -- старее 6 дней (Đăng 2 tuần trước)
  * 46273694 -- старее 6 дней (Đăng 2 tuần trước)
  * 44414389 -- старее 6 дней (Đăng 2 tuần trước)
  * 45797545 -- старее 6 дней (Đăng 25/05/2026)
  * 46258739 -- старее 6 дней (Đăng 2 tuần trước)
  * 46083694 -- старее 6 дней (Đăng 05/08/2026)
  * 45308773 -- старее 6 дней (Đăng 15/07/2026)
  * 45636113 -- старее 6 дней (Đăng 27/05/2026)
  * 45486144 -- старее 6 дней (Đăng 06/04/2026)
  * 46095595 -- старее 6 дней (Đăng 31/07/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001419, 3001420, 3001421, 3001422, 3001423, 3001424, 3001425]
REPLACES = []

NEW_SRC = r'''
L(3001419,"quy-nhon","qnn","Квартира",5000000,46,
  "1-спальная квартира, 46 м², Quy Nhơn Nam — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-an-duong-vuong-phuong-nguyen-van-cu-flc-seatower/cho-cao-cap-ay-u-tien-nghi-gia-tot-pr46343644","сегодня",0,source="batdongsan",postedOn="2026-09-25",
  descEn="1-bedroom flat, 46 m², Quy Nhơn Nam — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925110711-d671_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925110711-4561_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925110711-f54e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925110711-26e0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925110711-14cb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/25/20260925110711-605f_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001420,"quy-nhon","qn","Квартира",5000000,46,
  "1-спальная квартира, 46 м², Quy Nhơn — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-hue-phuong-tran-phu-4-tms-luxury-hotel-residences/cho-cao-cap-pullman-truc-bien-pr46340525","вчера",1,source="batdongsan",postedOn="2026-09-24",
  descEn="1-bedroom flat, 46 m², Quy Nhơn — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924145108-44a7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924145108-fb2a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924145108-9596_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924145108-c468_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924145108-2464_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/24/20260924145108-402f_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001421,"quy-nhon","qn","Квартира",8000000,72,
  "2-спальная квартира, 72 м², Quy Nhơn — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-le-duc-tho-phuong-hai-cang-phu-tai-residence/cho-2pn-full-nt-6-5-trieu-thang-pr44116108","вчера",1,source="batdongsan",postedOn="2026-09-24",
  descEn="2-bedroom flat, 72 m², Quy Nhơn — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/09/26/20250926105050-1719_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/09/26/20250926105052-4467_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/09/26/20250926105053-7ea3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/09/26/20250926105055-6c85_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/09/26/20250926105056-0953_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/09/26/20250926105058-a1f7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001422,"quy-nhon","qn","Квартира",7000000,52,
  "1-спальная квартира, 52 м², Quy Nhơn — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-hai-cang-altara-residences/cho-cao-cap-1pn-residence-quy-nhon-tang-cao-full-noi-that-xin-dep-pr42303849","вчера",1,source="batdongsan",postedOn="2026-09-24",
  descEn="1-bedroom flat, 52 m², Quy Nhơn — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301105329-c0aa_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301105259-6f28_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301105259-f281_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301105259-f8b6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301105259-cb82_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301105302-2cc8_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001423,"quy-nhon","qn","Квартира",12000000,96,
  "3-спальная квартира, 96 м², Quy Nhơn — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-le-duc-tho-phuong-hai-cang-phu-tai-residence/cho-cao-cap-3-phong-ngu-o-residence-pr42303705","вчера",1,source="batdongsan",postedOn="2026-09-24",
  descEn="3-bedroom flat, 96 m², Quy Nhơn — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301104151-3427_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301104151-a092_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301104151-7909_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301104151-80a7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301104151-176e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/01/20250301104151-57b4_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001424,"quy-nhon","qnd","Квартира",5000000,64,
  "2-спальная квартира, 64 м², Quy Nhơn Đông — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-dien-bien-phu-phuong-nhon-binh-ecolife-riverside/gio-hang-cho-da-dang-gia-tu-3trieu-pr37302356","2 дня назад",2,source="batdongsan",postedOn="2026-09-23",
  descEn="2-bedroom flat, 64 m², Quy Nhơn Đông — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2023/05/25/20230525082646-8eea_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/05/25/20230525082646-595a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/05/25/20230525082646-762a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/05/25/20230525082646-aea0_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2023/05/25/20230525082646-8eea_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2023/05/25/20230525082646-595a_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3001425,"quy-nhon","qnn","Квартира",6000000,46,
  "1-спальная квартира, 46 м², Quy Nhơn Nam — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-an-duong-vuong-phuong-nguyen-van-cu-flc-seatower/cho-ch-1pn-46m2-quy-nhon-gia-500k-em-pr45577797","3 дня назад",3,source="batdongsan",postedOn="2026-09-22",
  descEn="1-bedroom flat, 46 m², Quy Nhơn Nam — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/12/04/20251204084249-11ff_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/12/04/20251204084251-5ca2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/12/04/20251204084253-4c3f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/12/04/20251204084255-3e83_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/12/04/20251204084256-69bd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/12/04/20251204084258-6212_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
