# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 5 строк, 2026-09-13, город hai-phong.

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
  * 46276526 -- lch, 5,000,000 ₫, 52 м²: нынешний район назван в карточке: Lê Chân
  * 46237029 -- gvi, 12,000,000 ₫, 72 м²: нынешний район назван в карточке: Gia Viên
  * 46292082 -- anb2, 20,000,000 ₫, 74 м²: нынешний район назван в карточке: An Biên
  * 46290828 -- anb2, 14,000,000 ₫, 74 м²: нынешний район назван в карточке: An Biên
  * 46276881 -- anb2, 12,000,000 ₫, 80 м²: нынешний район назван в карточке: An Biên

ОТСЕЯНО (68):
  * 46276155 -- похоже на уже заведённое: id 1002631
  * 46279137 -- похоже на уже заведённое: id new:46168778
  * 46162010 -- район не назван так, как его знает сайт (dang hai 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 46257128 -- район не назван так, как его знает сайт (dang lam 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 45138187 -- район не назван так, как его знает сайт (dang lam 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 45779742 -- район не назван так, как его знает сайт (dang lam 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 46030986 -- район не назван так, как его знает сайт (dang lam 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 46279722 -- район не назван так, как его знает сайт (dang lam 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 46274687 -- район не назван так, как его знает сайт (dong hai 3, dong hai; в карточке «Q. Hải An (P. Đông Hải mới)»)
  * 45555007 -- район не назван так, как его знает сайт (dang lam 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 46190712 -- лимит прогона выбран
  * 41308722 -- лимит прогона выбран
  * 41856213 -- район не назван так, как его знает сайт (dang lam 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 44995480 -- район не назван так, как его знает сайт (dang lam 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 46140634 -- лимит прогона выбран
  * 46200716 -- район не назван так, как его знает сайт (dong hai 3, dong hai; в карточке «Q. Hải An (P. Đông Hải mới)»)
  * 46241217 -- лимит прогона выбран
  * 46241223 -- район не назван так, как его знает сайт (cat bi 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 46253351 -- лимит прогона выбран
  * 46253358 -- лимит прогона выбран
  * 45919952 -- район не назван так, как его знает сайт (dang lam 32, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 46181795 -- район не назван так, как его знает сайт (luu phuong dang, hai an; в карточке «Q. Hải An (P. Hải An mới)»)
  * 46234815 -- район не назван так, как его знает сайт (nam hai 32, dong hai; в карточке «Q. Hải An (P. Đông Hải mới)»)
  * 46160104 -- старее 13 дней (Đăng 10/08/2026)
  * 45981486 -- старее 13 дней (Đăng 03/07/2026)
  * 45981441 -- старее 13 дней (Đăng 30/06/2026)
  * 45485324 -- старее 13 дней (Đăng 27/06/2026)
  * 43402763 -- старее 13 дней (Đăng 16/06/2026)
  * 45852098 -- старее 13 дней (Đăng 10/06/2026)
  * 45868983 -- старее 13 дней (Đăng 08/06/2026)
  * 42759870 -- старее 13 дней (Đăng 08/04/2026)
  * 45134849 -- старее 13 дней (Đăng 06/04/2026)
  * 45248234 -- старее 13 дней (Đăng 06/03/2026)
  * 46278634 -- район не назван так, как его знает сайт (thuy ha vinhomes, hoa binh; в карточке «TP. Thủy Nguyên (P. Hòa Bình mới)»)
  * 46000092 -- район не назван так, как его знает сайт (an lu belhomes, thuy nguyen; в карточке «TP. Thủy Nguyên (P. Thủy Nguyên mới)»)
  * 46291147 -- лимит прогона выбран
  * 46162864 -- район не назван так, как его знает сайт (duong quan centa, thuy nguyen; в карточке «TP. Thủy Nguyên (P. Thủy Nguyên mới)»)
  * 46228497 -- район не назван так, как его знает сайт (duong quan centa, thuy nguyen; в карточке «TP. Thủy Nguyên (P. Thủy Nguyên mới)»)
  * 46184633 -- район не назван так, как его знает сайт (duong quan centa, thuy nguyen; в карточке «TP. Thủy Nguyên (P. Thủy Nguyên mới)»)
  * 40889598 -- район не назван так, как его знает сайт (duong quan centa, thuy nguyen; в карточке «TP. Thủy Nguyên (P. Thủy Nguyên mới)»)
"""
from listing_lock import insert_listings

IDS = [3000635, 3000636, 3000637, 3000638, 3000639]

NEW_SRC = r'''
L(3000635,"hai-phong","lch","Квартира",5000000,52,
  "2-спальная квартира, 52 м², Lê Chân — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-dai-lo-vo-nguyen-giap-phuong-kenh-duong-sentosa-sky-park-hai-phong/cho-1-5-ngu-hiem-pr46276526","4 дня назад",4,source="batdongsan",
  descEn="2-bedroom flat, 52 m², Lê Chân — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909110358-ba3d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909110359-449c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909110359-97a8_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909110400-d965_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909110401-4fb5_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909110401-0021_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000636,"hai-phong","gvi","Квартира",12000000,72,
  "2-спальная квартира, 72 м², Gia Viên — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-le-hong-phong-phuong-dang-giang-diamond-crown-hai-phong/daimond-2-ngu-full-o-12-trieu-pr46237029","сегодня",0,source="batdongsan",
  descEn="2-bedroom flat, 72 m², Gia Viên — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828140314-c6ab_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828140315-bcc1_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828140316-2a80_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828140316-8ca6_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828140317-0a9b_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/08/28/20260828140318-e9db_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000637,"hai-phong","anb2","Квартира",20000000,74,
  "2-спальная квартира, 74 м², An Biên — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-phuong-vinh-niem-the-minato-residence/cho-2pn-toa-ct1-74-m2-full-noi-that-cao-cap-view-ep-gia-20-tr-th-o-ngay-pr46292082","вчера",1,source="batdongsan",
  descEn="2-bedroom flat, 74 m², An Biên — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912203801-41a4_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912203801-fa4f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912203801-4b11_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912203801-86b2_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912203801-451c_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912203801-5b06_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000638,"hai-phong","anb2","Квартира",14000000,74,
  "2-спальная квартира, 74 м², An Biên — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-vo-nguyen-giap-phuong-vinh-niem-the-minato-residence/cho-tai-2pn-2wc-13-trieu-thang-74-m2-pr46290828","вчера",1,source="batdongsan",
  descEn="2-bedroom flat, 74 m², An Biên — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912141115-39ab_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912141115-07eb_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912141115-3198_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912141115-c65f_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912141115-2e01_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/12/20260912141115-4cf7_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
L(3000639,"hai-phong","anb2","Дом",12000000,80,
  "2-спальный дом, 80 м², An Biên — 2 санузла, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-pho-hai-ba-trung-phuong-cat-dai-35/cho-ngo-cut-to-nong-gan-mat-uong-vua-o-vua-kinh-doanh-uoc-pr46276881","4 дня назад",4,source="batdongsan",
  descEn="2-bedroom house, 80 m², An Biên — 2 bathrooms, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909115334-a86d_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909115336-3b55_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909115338-1d93_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909115340-8089_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909115341-3326_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/09/09/20260909115343-1aa4_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется, поэтому свежесть проверена ещё и по номеру объявления.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, so freshness is checked against the ad's number as well."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
