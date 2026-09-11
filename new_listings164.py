# -*- coding: utf-8 -*-
"""Telegram, заведение по шаблонам агентств: 1 строка, 2026-09-12.

Партию собрал ingest_telegram.py -- без модели в контуре. Заведены только посты,
целиком совпавшие с шаблоном агентства. Район -- из слов поста, по улице (её
отрезки из OpenStreetMap в границах районов карты) или по жилому комплексу, все
строки которого на сайте стоят в одном районе; правила -- в начале
ingest_telegram.py.

ЗАВЕДЕНО:
  * DaNangRentAFlat/129843 -- da-nang/ah, Minhouse: улица Cao Bá Quát: 2 из 2 отрезков в ah

ПО ШАБЛОНУ, НО НЕ ЗАВЕДЕНО (23):
  * vietnam_nedvijimost/23168 -- район tk не входит в прежний район Hai Chau из поста
  * Danang_House/21381 -- уже на сайте: id 2000604
  * Danang_House/21391 -- уже на сайте: id 2000605
  * Danang_House/21401 -- похоже на уже заведённое: id 2000573 (цена на сайте 35000000, в посте 40000000 VND)
  * Danang_House/21361 -- уже на сайте: id 2000606
  * Danang_House/21371 -- уже на сайте: id 2000607
  * nyachang_arenda/641283 -- район не определяется: пост не называет ни района, ни комплекса
  * nyachang_arenda/641293 -- район не определяется: пост не называет района, а «Champa Island» на сайте не встречается
  * nyachang_arenda/641301 -- уже на сайте: id 2000608
  * nyachang_arenda/641262 -- квартира в «Oceanus» без площади, корпуса и номера каталога: от уже стоящих строк этого комплекса её не отличить
  * nyachang_arenda/641268 -- Viet Life: в заголовке нет полей через «|»
  * nyachang_arenda/641278 -- район не определяется: пост не называет ни района, ни комплекса
  * Nhatranghomes/11563 -- квартира в «Oceanus» без площади, корпуса и номера каталога: от уже стоящих строк этого комплекса её не отличить
  * Nhatranghomes/11573 -- район не определяется: прецедент расколот («My Gia»: ntr 2, vt 1)
  * Nhatranghomes/11547 -- район не определяется: пост не называет района, а «Champa Island» на сайте не встречается
  * Nhatranghomes/11555 -- район не определяется: прецедент расколот («My Gia»: ntr 2, vt 1)
  * Viet_life_niachang/178438 -- квартира в «Oceanus» без площади, корпуса и номера каталога: от уже стоящих строк этого комплекса её не отличить
  * Viet_life_niachang/178417 -- квартира в «Oceanus» без площади, корпуса и номера каталога: от уже стоящих строк этого комплекса её не отличить
  * Viet_life_niachang/178427 -- район не определяется: прецедент расколот («MƯỜNG THANH BA LÀNG»: vp 2, lt 2, vt2 1)
  * Arenda_Nyachang_Zhilye/27742 -- уже на сайте: id 2000609
  * Arenda_Nyachang_Zhilye/27752 -- уже на сайте: id 2000610
  * Arenda_Nyachang_Zhilye/27722 -- уже на сайте: id 2000611
  * Arenda_Nyachang_Zhilye/27732 -- уже на сайте: id 2000612
"""
from listing_lock import insert_listings

IDS = [2000613]

NEW_SRC = r'''
L(2000613,"da-nang","ah","Квартира",12000000,50,
  "2-спальная квартира, 50 м², ул. Cao Bá Quát, An Hải. Аренда от 3 месяцев.",
  "https://t.me/DaNangRentAFlat/129843","вчера",1,source="telegram",
  descEn="2-bedroom flat, 50 m², Cao Bá Quát, An Hải. Minimum 3 months.",
  details={"photos": ["https://cdn5.telesco.pe/file/KjaHkq6kZSUIvaIyQk_-XXCpEtztWwAHut8AKwL7iq9UGyVlNP9FsCSzABNldq18jC0CNlhpAQlvFel-O6l5uQXuJwU9VbSQGhIZbs6vdESTAqvIW90oDNxnDHPZs6czt45pYNTUgykHIDOCI4lJv675CImKsox5ZtucEtlzcZSUvZeyPmqRQXPqGjDZULOpbIqpMW2kN0qhBxNIXNO3CcwesLeet4bNbCDRew7A0i5sSrlKR9DHn3pMetedZ3BcQzV4rq9MZBx_ok7a-htOfny5MfTBzXOGdCs3Obx7MTs9VVEWDUBjVEgKMGyYBPT7ObpwNd3QdwYnLI1CQOpkwg.jpg", "https://cdn5.telesco.pe/file/HfGqSB70J6TjgPyN5CHuJa7D0iZqNnOoOjTl2La7wcOsOS8MJJxYwYKXSleuodB713hqtVs6q-vosxWEOnAmwt50mHxThEWahB1g9YMNSHar5k0KLbqGWwFROr3QWcr3tj4V_EWnQk9CQtVRWw4INbUKQ3y-vmm1gy-nQN0gevNTck8Xh8yl7LGPYIi4drZXMosNT3CiWc69hfmzTe0WFIWJFNIEiYucwy0sPTverm0aP3sdOx5EyaQ612zuTgdjcMiNmZT51j5l_Vvkl8eb_ciLK23qcM6ca66BRbxJUSxHGPVR3AIMw94CXOtGtaFoVJB3FdLV5qxwAWpHzVzoyg.jpg", "https://cdn5.telesco.pe/file/DArrYdSJxY0JYXrCJA6Pdm9LfGmXEHoMmg9-hmoq3WisXPORdINm9kDdjs5yINtpMPiEg2EyriBJ8CtyUen8ey37QBRH1sDvac1ppGENu20nts-JTSWvr3u_PkyO5NkX-U_zD3zvUKrEVgsdpTfYdjXPQQTCn9d3Ay6zTzRwIuC4jVbJ2pKUNXiyW6LUh5PsseroV34YCpIoAPHvVaKyXlMRrWEx7MzofDKapcYlFCkQJF5XdqHNbPBtdUk4mO6olZrie1uAWo3_j8qOptaJwjpVC5agInBR2b-tgWbHC1ADuKYGArZU__PJGzlEtlgbbxUvtv3uekB97bsWjgJacw.jpg", "https://cdn5.telesco.pe/file/l20sT0wrccUdjAHdSMOuKA2JAJYCdjAI1WzvYB1C7H44H59BEn8gFlRlgTZ-RVW7W3HUQbVsGqsGL9fEXLPj1gfaw7dkWj-dbawym2kwJT7avZ4SyTSyMisX-gkPij72tg_sk2a_j7wfVbJhtMMvEl3gjimtzEnzGhJMOhk5ZQ-k8qD_wHuYMBzIy0Xol_s8m6fy1RQXtrV-K9697ZiHytOJwbxChE-Ebay9v1HuUS4vU9RSWvSfhMFyctBuAmSiq9IOXPMwV9L6q5xTSiyVFmX-dVYXOxR6LDjkE3_u4qRVHQU4IP-etCCmMHjCz7gZiR2fCSk3zR3djPslwFv4dQ.jpg", "https://cdn5.telesco.pe/file/X2yyAZAQmQIq-2wWaSz27B7Dzw9M3ptkc9_2uY0eX3NTcHzVMYaD2Z3gFzbCj1Qt4nqY0Rck1iRBYhMICfV7e9NKCbyrKdFI6Nog1MQ_nK1J7AAQiMBDlElaMVgLBcyVfvGqJtlsJnnnDnogWJ1QbRP9cSMisPx6L9etlADt0ofMjxLLnbc_ajXKdKzNm46_QlVynQnXwDMcMIxsf14WblFcBQ8Z_G8i7qYxa2upPhKgXDI-jFaFS9e80txqzPIMxZr22HE7baEq02Iqbx3h0iILMmE7wxhh5aJrlqYUw2B37dQd7r6KdGqmQsdSB566D8zNPP116yI_OGm72iKtNA.jpg", "https://cdn5.telesco.pe/file/SBfC13ZU_fYA5TOL1m8lxlwaNIDGboGTD0t0rEz5kXhKUXWLkdP6NWHLDy4sJaXhPk9Zy24WKzldj3TZ6BgKWOE1wVcfeVxGJc-Pvwr0z9yj39uBdZCm4g91Mj3Vzw_z4P0gP-cUfi9I7bJmusX6B2i9c0J5FECXvp145NhOcxWOxpNxvP5-TDtp2VDAyh4bwYJlwyeZfxYnxdNRxwlwngEkowKlUB-sp5ciNE3ZgaMRfjfrpnG--aB8tdhBikoXMypUTyy1Y9gl6u5uODDvSXMnh01R5P1pZCjnWz4HgmDakMVpLUf4dPAh5Xd_ZjI-aC_zrkpxmJiFI7XB6Snq5g.jpg"], "notice": "Описание собрано программой из полей телеграм-поста агентства — тип, спальни, санузлы, площадь, адрес и цена; рекламный текст не пересказан. Ссылка ведёт на сам пост, дата размещения взята из него. Фотографии из того же поста и лежат на серверах Telegram. Цену и условия подтверждайте у автора объявления. Район определён по улице и границам районов на карте.", "noticeEn": "This description was assembled by a program from the fields of an agency's Telegram post — type, bedrooms, bathrooms, size, address and price; the marketing text is not retold. The link points at the post itself and the posting date is taken from it. The photos come from the same post and are hosted by Telegram. Confirm the price and terms with the poster. The district comes from the street and the district borders on the map."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
