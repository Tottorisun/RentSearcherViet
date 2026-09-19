# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 1 строка, 2026-09-19, город quy-nhon.

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
  * 39050071 -- qnn, 5,000,000 ₫, 45 м²: нынешний район назван в карточке: Quy Nhơn Nam

ОТСЕЯНО (27):
  * 43127816 -- уже на сайте
  * 39050214 -- цена не читается: Giá thỏa thuận
  * 45408592 -- старее 6 дней (Đăng 1 tuần trước)
  * 45408563 -- старее 6 дней (Đăng 1 tuần trước)
  * 46286935 -- старее 6 дней (Đăng 1 tuần trước)
  * 46273694 -- старее 6 дней (Đăng 1 tuần trước)
  * 44414389 -- старее 6 дней (Đăng 1 tuần trước)
  * 36709073 -- старее 6 дней (Đăng 1 tuần trước)
  * 44032246 -- старее 6 дней (Đăng 1 tuần trước)
  * 44164379 -- старее 6 дней (Đăng 1 tuần trước)
  * 45172456 -- старее 6 дней (Đăng 1 tuần trước)
  * 46093786 -- старее 6 дней (Đăng 1 tuần trước)
  * 46208522 -- старее 6 дней (Đăng 1 tuần trước)
  * 46208549 -- старее 6 дней (Đăng 1 tuần trước)
  * 46208542 -- старее 6 дней (Đăng 1 tuần trước)
  * 46208591 -- старее 6 дней (Đăng 1 tuần trước)
  * 46208660 -- старее 6 дней (Đăng 1 tuần trước)
  * 46208628 -- старее 6 дней (Đăng 1 tuần trước)
  * 46208672 -- старее 6 дней (Đăng 1 tuần trước)
  * 46258739 -- старее 6 дней (Đăng 1 tuần trước)
  * 46260204 -- старее 6 дней (Đăng 1 tuần trước)
  * 46083694 -- старее 6 дней (Đăng 05/08/2026)
  * 45308773 -- старее 6 дней (Đăng 15/07/2026)
  * 45636113 -- старее 6 дней (Đăng 27/05/2026)
  * 45486144 -- старее 6 дней (Đăng 06/04/2026)
  * 45193295 -- старее 6 дней (Đăng 14/03/2026)
  * 46095595 -- старее 6 дней (Đăng 31/07/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3000985]
REPLACES = []

NEW_SRC = r'''
L(3000985,"quy-nhon","qnn","Квартира",5000000,45,
  "1-спальная квартира, 45 м², Quy Nhơn Nam — 1 санузел, полная меблировка.",
  "https://batdongsan.com.vn/cho-thue-can-ho-chung-cu-duong-an-duong-vuong-phuong-nguyen-van-cu-flc-seatower/cho-ngan-han-va-dai-han-lien-he-pr39050071","6 дней назад",6,source="batdongsan",postedOn="2026-09-13",
  descEn="1-bedroom flat, 45 m², Quy Nhơn Nam — 1 bathroom, fully furnished.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2024/04/17/20240417211209-608e_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2024/04/17/20240417211110-85af_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/02/11/20260211162459-a9da_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/02/12/20260212151846-3995_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/02/12/20260212151852-f702_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2026/02/12/20260212151859-3394_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
