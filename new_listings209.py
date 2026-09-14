# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 8 строк, 2026-09-14, город quy-nhon.

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
  * 36709073 -- qnd, 5,000,000 ₫, 64 м²: нынешний район назван в карточке: Quy Nhơn Đông
  * 42954925 -- qn, 5,000,000 ₫, 65 м²: нынешний район назван в карточке: Quy Nhơn
  * 44164379 -- qn, 8,000,000 ₫, 60 м²: нынешний район назван в карточке: Quy Nhơn
  * 45172456 -- qn, 8,000,000 ₫, 65 м²: нынешний район назван в карточке: Quy Nhơn
  * 46093786 -- qn, 5,000,000 ₫, 61 м²: нынешний район назван в карточке: Quy Nhơn
  * 46208522 -- qn, 7,000,000 ₫, 46 м²: нынешний район назван в карточке: Quy Nhơn
  * 46258739 -- qnn, 5,000,000 ₫, 87 м²: нынешний район назван в карточке: Quy Nhơn Nam
  * 46260204 -- qn, 16,000,000 ₫, 120 м²: нынешний район назван в карточке: Quy Nhơn

ОТСЕЯНО (20):
  * 43127816 -- уже на сайте
  * 39050214 -- цена не читается: Giá thỏa thuận
  * 39050071 -- уже на сайте
  * 45408592 -- цена не читается: Giá thỏa thuận
  * 45408563 -- цена не читается: Giá thỏa thuận
  * 46286935 -- уже на сайте
  * 46273694 -- уже на сайте
  * 44414389 -- уже на сайте
  * 44032246 -- уже на сайте
  * 45411022 -- цена не читается: Giá thỏa thuận
  * 46208549 -- похоже на уже заведённое: id new:46208522
  * 46208542 -- похоже на уже заведённое: id new:42954925
  * 46208591 -- нет фотографий
  * 46208660 -- нет фотографий
  * 46083694 -- старее 6 дней (Đăng 05/08/2026)
  * 45308773 -- старее 6 дней (Đăng 15/07/2026)
  * 45636113 -- старее 6 дней (Đăng 27/05/2026)
  * 45486144 -- старее 6 дней (Đăng 06/04/2026)
  * 45193295 -- старее 6 дней (Đăng 14/03/2026)
  * 46095595 -- старее 6 дней (Đăng 31/07/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3000707, 3000708, 3000709, 3000710, 3000711, 3000712, 3000713, 3000714]
REPLACES = []

NEW_SRC = r'''
L(3000707,"quy-nhon","qnd","Квартира",5000000,64,
  "2-спальная квартира, 64 м², Quy Nhơn Đông — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-dien-bien-phu-phuong-nhon-binh-ecolife-riverside/cho-gia-chi-tu-3-6-trieu-nha-moi-pr36709073","6 дней назад",6,source="batdongsan",
  descEn="2-bedroom flat, 64 m², Quy Nhơn Đông — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2023/03/12/20230312143222-8769_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/03/12/20230312143253-ccdb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/03/12/20230312143253-321b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/03/12/20230312143253-f3a3_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/03/12/20230312143253-68b4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/03/12/20230312143253-ff01_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000708,"quy-nhon","qn","Квартира",5000000,65,
  "2-спальная квартира, 65 м², Quy Nhơn — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-hai-cang-altara-residences/quy-cho-residence-6-5tr-7-5tr-th-2pn-2wc-tang-trung-cao-view-bien-pr42954925","6 дней назад",6,source="batdongsan",
  descEn="2-bedroom flat, 65 m², Quy Nhơn — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-923b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-2c51_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-7801_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-5c3c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-ddf7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2025/03/06/20250306104506-673d_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000709,"quy-nhon","qn","Квартира",8000000,60,
  "1-спальная квартира, 60 м², Quy Nhơn — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-hue-phuong-tran-phu-4-tms-luxury-hotel-residences/cho-quy-nhon-view-bien-gia-tot-pr44164379","6 дней назад",6,source="batdongsan",
  descEn="1-bedroom flat, 60 m², Quy Nhơn — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2025/10/02/20251002085113-9390_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820213406-e91f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820213408-6f83_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820213408-6070_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820213408-3843_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820213410-3491_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000710,"quy-nhon","qn","Квартира",8000000,65,
  "2-спальная квартира, 65 м², Quy Nhơn — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-hai-cang-altara-residences/quy-cho-residence-1pn-2pn-2wc-2pn-goc-tang-trung-cao-view-bien-full-nt-pr45172456","6 дней назад",6,source="batdongsan",
  descEn="2-bedroom flat, 65 m², Quy Nhơn — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/07/20260807142931-622e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/02/23/20260223165943-524e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/02/23/20260223165949-fb68_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/02/23/20260223165949-bf64_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/02/23/20260223165950-09e4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/02/23/20260223165950-9ce9_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000711,"quy-nhon","qn","Квартира",5000000,61,
  "2-спальная квартира, 61 м², Quy Nhơn — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-tran-hung-dao-phuong-hai-cang-altara-residences/cho-nhieu-tang-cao-view-ep-1-2-3pn-quy-nhon-noi-that-cao-cap-dich-vu-4-sao-pr46093786","6 дней назад",6,source="batdongsan",
  descEn="2-bedroom flat, 61 m², Quy Nhơn — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/07/25/20260725102343-9ca4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/25/20260725102342-2351_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/07/25/20260725102343-5d69_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/07/25/20260725102343-9ca4_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/07/25/20260725102342-2351_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/07/25/20260725102343-5d69_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000712,"quy-nhon","qn","Квартира",7000000,46,
  "Квартира, 46 м², Quy Nhơn — полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-nguyen-hue-phuong-tran-phu-4-tms-luxury-hotel-residences/cho-gia-tot-cach-bien-200m-pr46208522","6 дней назад",6,source="batdongsan",
  descEn="Flat, 46 m², Quy Nhơn — fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820221415-9782_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820221415-fab4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820221415-a401_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820221415-f2fe_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820221415-51ed_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/20/20260820221415-2bc7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000713,"quy-nhon","qnn","Дом",5000000,87,
  "1-спальный дом, 87 м², Quy Nhơn Nam — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-dang-van-chan-1-phuong-nguyen-van-cu-155/cho-can-mat-tien-tp-quy-nhon-pr46258739","3 дня назад",3,source="batdongsan",
  descEn="1-bedroom house, 87 m², Quy Nhơn Nam — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905075711-541b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905075711-7be7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905075711-b3e7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905075711-1d4d_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/05/20260905075711-541b_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/05/20260905075711-7be7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000714,"quy-nhon","qn","Дом",16000000,120,
  "Дом, 120 м², Quy Nhơn.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-tran-hung-dao-phuong-tran-hung-dao-4-155/cho-mat-tien-tret-lau-1-uong-ao-trung-tam-quy-nhon-pr46260204","6 дней назад",6,source="batdongsan",
  descEn="House, 120 m², Quy Nhơn.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905121027-e176_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905121030-f9aa_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/05/20260905122635-bf04_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/05/20260905121027-e176_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/05/20260905121030-f9aa_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/05/20260905122635-bf04_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
