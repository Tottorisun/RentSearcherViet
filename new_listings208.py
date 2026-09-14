# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 13 строк, 2026-09-14, город da-lat.

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
  * 46246761 -- cl, 4,000,000 ₫, 75 м²: нынешний район назван в карточке: Cam Ly-Đà Lạt
  * 46252039 -- xh, 10,000,000 ₫, 50 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46252137 -- xh, 13,000,000 ₫, 150 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46252168 -- xh, 15,000,000 ₫, 100 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46252216 -- lv, 5,000,000 ₫, 110 м²: нынешний район назван в карточке: Lâm Viên-Đà Lạt
  * 46252239 -- xh, 12,000,000 ₫, 90 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46185034 -- xh, 5,000,000 ₫, 20 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 41472028 -- lv, 6,000,000 ₫, 12 м²: нынешний район назван в карточке: Lâm Viên-Đà Lạt
  * 45648318 -- xh, 8,000,000 ₫, 22 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46271442 -- xh, 60,000,000 ₫, 330 м²: нынешний район назван в карточке: Xuân Hương-Đà Lạt
  * 46188310 -- lv, 48,000,000 ₫, 880 м²: нынешний район назван в карточке: Lâm Viên-Đà Lạt
  * 45874487 -- xt, 120,000,000 ₫, 100 м²: нынешний район назван в карточке: Xuân Trường-Đà Lạt
  * 46251949 -- cl, 25,000,000 ₫: нынешний район назван в карточке: Cam Ly-Đà Lạt

ОТСЕЯНО (55):
  * 46175563 -- уже на сайте
  * 42512173 -- уже на сайте
  * 46175548 -- уже на сайте
  * 46290937 -- уже на сайте
  * 46169987 -- старее 6 дней (Đăng 12/08/2026)
  * 45874200 -- старее 6 дней (Đăng 27/06/2026)
  * 44271365 -- старее 6 дней (Đăng 08/04/2026)
  * 45228785 -- старее 6 дней (Đăng 31/03/2026)
  * 45347154 -- старее 6 дней (Đăng 19/03/2026)
  * 45334210 -- старее 6 дней (Đăng 17/03/2026)
  * 45317373 -- старее 6 дней (Đăng 16/03/2026)
  * 46157935 -- уже на сайте
  * 46291428 -- уже на сайте
  * 46289856 -- уже на сайте
  * 46267523 -- уже на сайте
  * 46140934 -- старее 6 дней (Đăng 05/08/2026)
  * 45962440 -- старее 6 дней (Đăng 25/06/2026)
  * 45576808 -- старее 6 дней (Đăng 18/04/2026)
  * 45436230 -- старее 6 дней (Đăng 30/03/2026)
  * 46181403 -- старее 6 дней (Đăng 14/08/2026)
  * 46159595 -- старее 6 дней (Đăng 10/08/2026)
  * 46155722 -- старее 6 дней (Đăng 08/08/2026)
  * 46144431 -- старее 6 дней (Đăng 06/08/2026)
  * 45572182 -- старее 6 дней (Đăng 29/07/2026)
  * 46068255 -- старее 6 дней (Đăng 20/07/2026)
  * 46185083 -- похоже на уже заведённое: id new:46185034
  * 46185045 -- похоже на уже заведённое: id new:46185034
  * 46185068 -- похоже на уже заведённое: id new:46185034
  * 45703872 -- старее 6 дней (Đăng 18/06/2026)
  * 46217397 -- старее 6 дней (Đăng 3 tuần trước)
  * 45985291 -- старее 6 дней (Đăng 01/07/2026)
  * 45698255 -- старее 6 дней (Đăng 09/05/2026)
  * 45648108 -- старее 6 дней (Đăng 29/04/2026)
  * 45529165 -- старее 6 дней (Đăng 11/04/2026)
  * 45513763 -- старее 6 дней (Đăng 09/04/2026)
  * 45420454 -- старее 6 дней (Đăng 28/03/2026)
  * 45389983 -- старее 6 дней (Đăng 24/03/2026)
  * 45359268 -- старее 6 дней (Đăng 20/03/2026)
  * 44848680 -- старее 6 дней (Đăng 02/03/2026)
  * 46156986 -- то же объявление, что id 3000662: общие фотографии, а та строка не старше
"""
from listing_lock import insert_listings, remove_listings

IDS = [3000694, 3000695, 3000696, 3000697, 3000698, 3000699, 3000700, 3000701, 3000702, 3000703, 3000704, 3000705, 3000706]
REPLACES = []

NEW_SRC = r'''
L(3000694,"da-lat","cl","Дом",4000000,75,
  "2-спальный дом, 75 м², Cam Ly - Đà Lạt — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-han-thuyen-phuong-5_3-391/cho-tai-7-5-4-trieu-vnd-75-m2-ep-nhieu-tien-ich-chinh-chu-pr46246761","6 дней назад",6,source="batdongsan",
  descEn="2-bedroom house, 75 m², Cam Ly - Đà Lạt — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131453-cc66_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131453-074a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131453-7f73_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131455-a16d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131459-2895_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/01/20260901131459-5881_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000695,"da-lat","xh","Дом",10000000,50,
  "2-спальный дом, 50 м², Xuân Hương - Đà Lạt — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-trung-truc-phuong-4_3-391/cho-tam-a-lat-2-phong-ngu-10-tr-thang-pr46252039","6 дней назад",6,source="batdongsan",
  descEn="2-bedroom house, 50 m², Xuân Hương - Đà Lạt — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903151355-e199_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903151355-4953_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903151355-6f38_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903151355-ddef_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903151355-503e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903151356-3af6_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000696,"da-lat","xh","Дом",13000000,150,
  "1-спальный дом, 150 м², Xuân Hương - Đà Lạt — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-ha-huy-tap-phuong-4_3-391/cho-trung-tam-a-lat-13-trieu-1-thang-pr46252137","6 дней назад",6,source="batdongsan",
  descEn="1-bedroom house, 150 m², Xuân Hương - Đà Lạt — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903152610-b342_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903152623-ba46_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903152623-e532_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903152623-6841_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903152624-3a35_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/09/03/20260903152610-b342_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000697,"da-lat","xh","Дом",15000000,100,
  "5-спальный дом, 100 м², Xuân Hương - Đà Lạt — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-van-troi-phuong-2_3-391/cho-ngay-trung-tam-a-lat-15-trieu-1-thang-ay-u-noi-that-pr46252168","6 дней назад",6,source="batdongsan",
  descEn="5-bedroom house, 100 m², Xuân Hương - Đà Lạt — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153044-79a9_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153052-86c7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153053-84c0_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153052-b164_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153053-df71_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153053-c06e_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000698,"da-lat","lv","Дом",5000000,110,
  "2-спальный дом, 110 м², Lâm Viên - Đà Lạt — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-xo-viet-nghe-tinh-phuong-8_2-391/cho-ngay-khu-quy-hoach-san-van-ong-a-lat-9-5-trieu-1-thang-pr46252216","6 дней назад",6,source="batdongsan",
  descEn="2-bedroom house, 110 m², Lâm Viên - Đà Lạt — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153608-3db2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153616-8c66_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153616-c995_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153616-9725_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153616-81fd_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153616-76e9_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000699,"da-lat","xh","Дом",12000000,90,
  "2-спальный дом, 90 м², Xuân Hương - Đà Lạt — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-khe-sanh-phuong-10_4-391/cho-a-lat-12-trieu-1-thang-pr46252239","6 дней назад",6,source="batdongsan",
  descEn="2-bedroom house, 90 m², Xuân Hương - Đà Lạt — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153852-ac29_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153858-5ea7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153858-5a73_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153858-7592_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153858-2023_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903153858-0888_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000700,"da-lat","xh","Комната",5000000,20,
  "Комната, 20 м², Xuân Hương - Đà Lạt — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-pham-ngu-lao-phuong-3_3-391/chinh-chu-cho-ks-theo-thang-co-thang-may-pr46185034","6 дней назад",6,source="batdongsan",
  descEn="Room, 20 m², Xuân Hương - Đà Lạt — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/15/20260815135846-6feb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/15/20260815135846-4664_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/15/20260815135846-37bf_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/15/20260815135847-f699_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/15/20260815135846-6feb_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/08/15/20260815135846-4664_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000701,"da-lat","lv","Комната",6000000,12,
  "Комната, 12 м², Lâm Viên - Đà Lạt — 1 санузел.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-yersin-phuong-9_2-391/cho-tai-9-da-lat-3x4-12m2-gia-1-6-trieu-thang-co-gac-lung-pr41472028","6 дней назад",6,source="batdongsan",
  descEn="Room, 12 m², Lâm Viên - Đà Lạt — 1 bathroom.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2024/11/08/20241108155313-c125_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/11/12/20241112155802-1fb6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/11/12/20241112155801-8d9e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/11/12/20241112155802-8f40_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/11/08/20241108155313-ada2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/11/08/20241108155313-85b0_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000702,"da-lat","xh","Комната",8000000,22,
  "Комната, 22 м², Xuân Hương - Đà Lạt — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-duong-nguyen-van-troi-phuong-2_3-391/cho-can-ho-full-noi-that-gia-re-pr45648318","6 дней назад",6,source="batdongsan",
  descEn="Room, 22 m², Xuân Hương - Đà Lạt — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/09/20260809172950-0a64_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/16/20260516123333-933a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/16/20260516123334-45f5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/16/20260516123455-6168_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/16/20260516123456-0c05_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/05/16/20260516123457-2b19_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000703,"da-lat","xh","Дом",60000000,330,
  "9-спальный дом, 330 м², Xuân Hương - Đà Lạt — 9 санузлов, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-dinh-tien-hoang-phuong-2_3-cong-vien-van-hoa-do-thi-da-lat-golf-valley/cho-villa-ep-kqh-a-1-tret-2-lau-9-phong-ngu-co-thang-may-pr46271442","6 дней назад",6,source="batdongsan",
  descEn="9-bedroom house, 330 m², Xuân Hương - Đà Lạt — 9 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908111304-e6a7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908111304-e52a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908111304-a3a6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908111304-c01d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908111304-29a2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/08/20260908111304-1607_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000704,"da-lat","lv","Дом",48000000,880,
  "11-спальный дом, 880 м², Lâm Viên - Đà Lạt.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-nguyen-huu-canh-phuong-8_2-391/chinh-chu-can-cho-gap-villa-o-b10-tp-a-lat-pr46188310","6 дней назад",6,source="batdongsan",
  descEn="11-bedroom house, 880 m², Lâm Viên - Đà Lạt.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/16/20260816164824-1192_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/16/20260816164825-850a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/16/20260816164825-a43c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/16/20260816164825-1912_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/16/20260816164825-e038_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/16/20260816164825-7680_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000705,"da-lat","xt","Дом",120000000,100,
  "2-спальный дом, 100 м², Xuân Trường - Đà Lạt — 3 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-hung-vuong-2-xa-xuan-truong-1-391/cho-villa-1100m2-uong-thich-hop-kinh-doanh-hang-cao-cap-hien-trang-moi-ep-pr45874487","6 дней назад",6,source="batdongsan",
  descEn="2-bedroom house, 100 m², Xuân Trường - Đà Lạt — 3 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608112934-7ec2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608112934-2b7a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/06/08/20260608112934-1a2f_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/06/08/20260608112934-7ec2_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/06/08/20260608112934-2b7a_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2026/06/08/20260608112934-1a2f_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
L(3000706,"da-lat","cl","Дом",25000000,None,
  "4-спальный дом, Cam Ly - Đà Lạt — 4 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-biet-thu-lien-ke-duong-nguyen-an-ninh-phuong-6_3-391/cho-villa-san-vuon-1000m2-a-lat-25tr-thang-pr46251949","6 дней назад",6,source="batdongsan",
  descEn="4-bedroom house, Cam Ly - Đà Lạt — 4 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903145952-95f7_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903145952-f63f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903145952-e883_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903145952-ef36_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903145952-0df1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/03/20260903145952-8789_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
