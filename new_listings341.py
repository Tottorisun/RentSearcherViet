# -*- coding: utf-8 -*-
"""batdongsan.com.vn, автоматический сбор: 1 строка, 2026-09-26, город hoi-an.

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
  * 38338118 -- hat, 25,000,000 ₫, 500 м²: нынешний район назван в карточке: Hội An Tây

ОТСЕЯНО (23):
  * 35898029 -- цена не читается: Giá thỏa thuận
  * 46325872 -- уже на сайте
  * 45631159 -- старее 6 дней (Đăng 11/08/2026)
  * 45978499 -- старее 6 дней (Đăng 12/07/2026)
  * 45790325 -- старее 6 дней (Đăng 07/07/2026)
  * 45840173 -- старее 6 дней (Đăng 08/06/2026)
  * 45763264 -- старее 6 дней (Đăng 20/05/2026)
  * 45703294 -- старее 6 дней (Đăng 11/05/2026)
  * 45258202 -- старее 6 дней (Đăng 08/03/2026)
  * 46335349 -- похоже на уже заведённое: id 1010986
  * 45240276 -- старее 6 дней (Đăng 2 tuần trước)
  * 46180369 -- старее 6 дней (Đăng 24/08/2026)
  * 46185585 -- старее 6 дней (Đăng 15/08/2026)
  * 46170907 -- старее 6 дней (Đăng 12/08/2026)
  * 46147035 -- старее 6 дней (Đăng 06/08/2026)
  * 44627123 -- старее 6 дней (Đăng 24/05/2026)
  * 44533134 -- старее 6 дней (Đăng 24/05/2026)
  * 45624048 -- старее 6 дней (Đăng 09/05/2026)
  * 42989229 -- старее 6 дней (Đăng 08/05/2026)
  * 45685235 -- старее 6 дней (Đăng 07/05/2026)
  * 45584028 -- старее 6 дней (Đăng 20/04/2026)
  * 45448767 -- старее 6 дней (Đăng 14/04/2026)
  * 45332949 -- старее 6 дней (Đăng 23/03/2026)
"""
from listing_lock import insert_listings, remove_listings

IDS = [3001501]
REPLACES = []

NEW_SRC = r'''
L(3001501,"hoi-an","hat","Дом",25000000,500,
  "3-спальный дом, 500 м², Hội An Tây — 4 санузла.",
  "https://batdongsan.com.vn/cho-thue-nha-rieng-duong-nguyen-phan-vinh-xa-cam-ha-1-520/cho-nhieu-villa-dep-cach-bien-an-bang-chi-1-phut-cach-trung-pho-co-hoi-an-dien-tich-da-dang-pr38338118","2 дня назад",2,source="batdongsan",postedOn="2026-09-24",
  descEn="3-bedroom house, 500 m², Hội An Tây — 4 bathrooms.",
  details={"photos": ["https://file4.batdongsan.com.vn/resize/1275x717/2023/10/05/20231005073447-2343_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/10/05/20231005073448-49ae_wm.webp", "https://file4.batdongsan.com.vn/resize/1275x717/2023/10/05/20231005073448-25ff_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/10/05/20231005073448-e35a_wm.jpg", "https://file4.batdongsan.com.vn/resize/1275x717/2023/10/05/20231005073448-a7c3_wm.jpg", "https://file4.batdongsan.com.vn/resize/200x200/2023/10/05/20231005073447-2343_wm.jpg"], "notice": "Описание собрано программой из полей объявления на batdongsan.com.vn — тип, комнаты, санузлы, площадь, район и цена. Рекламный текст продавца не пересказан. Район назван самим источником: портал печатает и нынешний квартал, и прежний. Фотографии показаны ссылками на batdongsan и хранятся у них. Дата — «Ngày đăng» объявления; при перевыкладке продавцом она обновляется: перевыложенное объявление показывается ещё 7 дней.", "noticeEn": "This description was assembled by a program from the ad's own fields on batdongsan.com.vn — type, rooms, bathrooms, size, ward and price. The seller's marketing copy is not retold. The district comes from the source itself: the portal prints both the current ward and the former one. The photos are shown as links to batdongsan and stay hosted there. The date is the ad's own posting date; sellers reset it when they repost, and a reposted ad is shown for another 7 days."}),
'''

if __name__ == "__main__":
    # Сначала вставка, потом снятие: откажет вставка -- файл строк не тронут.
    insert_listings(NEW_SRC, IDS, owner=__file__)
    if REPLACES:
        remove_listings(REPLACES, owner=__file__)
