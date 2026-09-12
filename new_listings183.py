# -*- coding: utf-8 -*-
"""Telegram, заведение по шаблонам агентств: 2 строки, 2026-09-13.

Партию собрал ingest_telegram.py -- без модели в контуре. Заведены только посты,
целиком совпавшие с шаблоном агентства. Район -- из слов поста, по улице (её
отрезки из OpenStreetMap в границах районов карты) или по жилому комплексу, все
строки которого на сайте стоят в одном районе; правила -- в начале
ingest_telegram.py.

ЗАВЕДЕНО:
  * DaNangRentAFlat/130234 -- da-nang/ah, Minhouse: улица Nguyễn Đình: 4 из 4 отрезков в ah; пост: Son Tra
  * DaNangRentAFlat/130253 -- da-nang/ah, Minhouse: улица Tô Hiến Thành: 4 из 4 отрезков в ah; пост: Son Tra

ПО ШАБЛОНУ, НО НЕ ЗАВЕДЕНО (21):
  * DaNangRentAFlat/130244 -- район не определяется: «#Sontra street»
  * DaNangRentAFlat/130206 -- в посте нет фотографий
  * DaNangRentAFlat/130207 -- Minhouse: цены нет или она не читается (диапазон, «от»)
  * vietnam_nedvijimost/23346 -- тот же текст уже заведён: id 2000622
  * vietnam_nedvijimost/23352 -- район не определяется: «Sam Towers, Hai Chau»
  * vietnam_nedvijimost/23362 -- тот же текст уже заведён: id 2000631
  * vietnam_nedvijimost/23317 -- похоже на уже заведённое: id 2000623 (та же цена)
  * vietnam_nedvijimost/23327 -- тот же текст уже заведён: id 2000624
  * nyachang_arenda/643313 -- район не определяется: пост не называет ни района, ни комплекса
  * nyachang_arenda/643318 -- район не определяется: пост не называет ни района, ни комплекса
  * nyachang_arenda/643323 -- район не определяется: прецедент расколот («Mường Thành 04»: lt 1)
  * nyachang_arenda/643329 -- район не определяется: пост не называет ни района, ни комплекса
  * nyachang_arenda/643283 -- район не определяется: пост не называет ни района, ни комплекса
  * nyachang_arenda/643303 -- Viet Life: в заголовке нет полей через «|»
  * Nhatranghomes/11563 -- квартира в «Oceanus» без площади, корпуса и номера каталога: от уже стоящих строк этого комплекса её не отличить
  * Nhatranghomes/11547 -- район не определяется: пост не называет района, а «Champa Island» на сайте не встречается
  * Viet_life_niachang/179215 -- квартира в «Oceanus» без площади, корпуса и номера каталога: от уже стоящих строк этого комплекса её не отличить
  * Viet_life_niachang/179225 -- Viet Life: в заголовке нет полей через «|»
  * Viet_life_niachang/179235 -- Viet Life: в заголовке нет полей через «|»
  * Viet_life_niachang/179185 -- квартира в «Oceanus» без площади, корпуса и номера каталога: от уже стоящих строк этого комплекса её не отличить
  * Arenda_Nyachang_Zhilye/27762 -- район не определяется: пост не называет района, а «Скения Бай» на сайте не встречается
"""
from listing_lock import insert_listings

IDS = [2000648, 2000649]

NEW_SRC = r'''
L(2000648,"da-nang","ah","Квартира",28000000,90,
  "2-спальная квартира, 90 м², ул. Nguyễn Đình, An Hải. Аренда от 1 месяца.",
  "https://t.me/DaNangRentAFlat/130234","вчера",1,source="telegram",
  descEn="2-bedroom flat, 90 m², Nguyễn Đình, An Hải. Minimum 1 month.",
  details={"photos": ["https://cdn5.telesco.pe/file/Ndq4P-U3p1G8pRqwGqMvGNWJT4yWCcu9KP4FLWfi0XIml5OicxqhqlF6kS4_bZS47dJU3VJJt2ogdf1ZqqP9yTMcmIw4FYLCqLznrarIjAW9jL6sjW6tUdplnrzQICj75q_d6U9fKjlV1sfBK6ffwZa0CNLbfxFJ97-MCR93zId9EyubH_xKHWiHZdvGDGTWBOWzr24X2o7Xb14fH-P8BxXSJs9Uv2KrFxjQV-X_ww3dsA2tRh6uZVMu5TJEfjS5IrkRPV5aDzF_5SnzlonqrLY65qm9lQB0sErPnulxmXsgK5CA1XqZBLurz0nD5x5lT2v_5Fz-4CfKFmypajJ7hQ.jpg", "https://cdn5.telesco.pe/file/eSWpjaC6KXFUPcg3OJr9TANHTu8UXc5QB-qiZFzaLCgJN1a_wCKiQgSsQ26eBCrU3DSUyUz07VUr_vtQyMsV5fG5I3Yw4D3DfQqfDQ6vT-ddSUx07vmqdckG2QXeqOPtEemmSj1QbxEQk5M6icR_PsTHzPKk-hW6-0vnZRyTGeVKesDiPHJUTGjmVVxJR3UnviuLMXgS3FYsVwntK_KPvjpMAvuEqbe1aPC_SBbIKTQKJ5tBVi9B7293U-fXeK3XIR7BTHFSvos377aJCs8uo0eEnq9d85ik5zgllrHmXYf8V5BN4MBJntUUWAVif3NxRfWfrfGgf0I8JI8iH-wiMg.jpg", "https://cdn5.telesco.pe/file/AOIDjQcDhi623LMzbOR_DUNVf9IBacBXZuSdmEJkuxXjBFlFlwDbk-OrbFpJ5xBQfJGA7lnHZUS564cY1SQJMzTBA09gM5Y5HfwMEXSfn2bSSh9e3UqEWm8KlbG8xreZ2hbHvYw6Ywz3YUlFPcHVHi5BovbZxNcQ20CztOYlwaRIloRuMvMx-M0bQq3fypnQkVKJzvOgAfaq0Qog4qY3RKI0ya_HRVwQoKuZt0SFjNalq6H4HlLZVNeO_J_5zczwe_IxR9gshmmpwAyxGRgaPc6hUC5mr6fBRJRsxJIWNmCHgHaX5aRDRsLgDnbVbPVOXjVOBsNxmRY5AXZ0H1Y0sg.jpg", "https://cdn5.telesco.pe/file/uxudeMr6kHR94zFY_T4Weh4AbfDA4O_6lNTDPMw6jK9F6iapTXzfPdrLlqmx4XGbqi8woHLDw3UQ96XL7DPEd6LjANKl1AOVH1C7dttFHOpL6f2MUUhu-HReCttl01L5RqQR3xCfT3Wtjr9P_rdSbDhtWmrEglza9E0pYmHdaTZF11Fo51pTyHwF5VUhm-jhXjMkO-AqgO1_69VuJrd-G2anRbkhKD7f-CJF-iPJXORVhQKyu6351Coki4Gr5vNcMKTqaDB29URzTb83dJ3Nq4WRL99wsXi1FpT1e6qgsSsZMD5OWCGtMMCUEmfDMSDVsYtF_KrMIEALnSxPF8XTfw.jpg", "https://cdn5.telesco.pe/file/mY36GV3pjL4l1K31tKk5T4uDaIsikD8WTrQuWYKWKEveKkZdMkmmC7gGh0V1ZsPWDdWDf8z2SGWBZ85d0x_ML5tbxjPsiUTTgDC6Mtsl61cUyaBS5ikCJAxb89pOuD2sp584Lry1Z_G7PWrdHUnMPeQLHLhXeA9_6JOVLhzdI8goSZ_LIBQzQexqQrTgJ9yfV9A16-eLlBGoU_QlPlvZXFpkoNOhMuMehj-wYnqYyDhLSAAnaquj69tRuSb4KA8r73W9NF0S1QEmclz2I9lhoW_tFpO6GGokhKQsBdsiPZCa99Uk_JAzZdOP03-A_p4lm8TRYgEfLsK1WhqTno59Dw.jpg", "https://cdn5.telesco.pe/file/j922pIArmp_QfusFcqv0CeIKiyVIrYzNDmir8uBf6y8pGMDzwZfjp6NazNNHGD-xv90E8_XAVI-NNS5G2i8r30E4RECdZ8MfTmL-92D-dxigogxZ44dk5uyQzSH7pEOApGvOA2GoUf3r6FPaCrTJM4MdhPr7XglAQO3fvgCDcf5cEG5x7oFSKC2N7TcAUkXjPHEeVyuMSStyj15N6thitKGl_tiZ-6S-Ds-IeguZHOXuMgII4sGtguqvj8-qKJgClu5OWOeWLgBnT8fREWNO_CKD_YJjNvrY4L9alMITUVb5fR7bILgyayYsUXLl8DP-1xrB_ic-5F_8FdU_SjWxOw.jpg"], "notice": "Описание собрано программой из полей телеграм-поста агентства — тип, спальни, санузлы, площадь, адрес и цена; рекламный текст не пересказан. Ссылка ведёт на сам пост, дата размещения взята из него. Фотографии из того же поста и лежат на серверах Telegram. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "This description was assembled by a program from the fields of an agency's Telegram post — type, bedrooms, bathrooms, size, address and price; the marketing text is not retold. The link points at the post itself and the posting date is taken from it. The photos come from the same post and are hosted by Telegram. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
L(2000649,"da-nang","ah","Квартира",25000000,80,
  "2-спальная квартира, 80 м², ул. Tô Hiến Thành, An Hải. Аренда от 1 месяца.",
  "https://t.me/DaNangRentAFlat/130253","вчера",1,source="telegram",
  descEn="2-bedroom flat, 80 m², Tô Hiến Thành, An Hải. Minimum 1 month.",
  details={"photos": ["https://cdn5.telesco.pe/file/Mecz1cywW6kj0L6csUEzm64cGCE9CLXQvIjZfuXSbvXGHzpo_UoVQB29xlv5sP8JCre3ceNKsR8eknOzojj5jH2sWjRE3exvgRwjQ1LC41tYSlbsDbIvIZj_L9b6_z3WXqHrQSS3g06-EMArOVJHJzb3Bp4gWQVRpGIn7Aq7g7AdO7S4K8Nq0KZIsT1tIJH0j-AIMa_PFhBcUUM5XtP_giPlMFtnhvEnGx79IiWDJx77fHUpk6yOfBxSYqlZ33Af6b4gbII_0-thu_hs28pFjG6ZuAbQmZLZmyjaViuyvXIrCpF-2qL-gjCy_krNVWmJze-zSTFI7YwHNE7KmL3YMQ.jpg", "https://cdn5.telesco.pe/file/nH4iRZAjbhhsZoP0ZSwI6_m8pgLLISByxAupXML5FTZELGMgPdDpb0qkEsOcO3XnI9z-rmczvKwRdes7UHtz3UdzDOfuStyvMmlN60V32fLXILw1Ry8DLF-ZgW78MFVe5m59-Z4hawxdeyXdpCNn2ilVsXifmrD3IzwaDb8Z8A-GjTtMuhCH7ybPI-ERYg9p2x8yL3sMfVFrRBV5DswtTJEWC2FYOU8rwA-6WuycS52R-f_RG_hFYBurXUcVk_56Jh25iUm1I2ZRtTPtq4HuwLcZLfqeYG0Gqcvhpf7IZ0gywYzqBNpzXMB103OaVFA2H2ffObnEvB3Po2U6G8xCaQ.jpg", "https://cdn5.telesco.pe/file/S9Gc-gcU5elQyg-tZCmXDv3Z9tcrlH6uhQWGYRbW6f4XIM4_9yXzpVGcjR_fwzFfhm2Y6mZ3fkX3cm_UtU7jWsgwRSbZsWf8JbEI6gqswuKoemO_d217RfJDhVcI-5ArN_RVu54018CIrI3JPlI4U4FeHKCTB79hk7no80VUkVH52rzGfumoXog6d8bAqDLqe_pZhk4RacN3IXujawjF7CrnxCV4RZERnTnDjqplrSkmoknViEz8VUxRA7oWA52nDhtlaBoZWPJ95TzCoI8ySEOFshwfAQPK7zc914alr61uN2qTIixKMQMVuFSRZK1ttSMbo8W36drRQwNeF8oj5g.jpg", "https://cdn5.telesco.pe/file/q8aOuqLgTqDWL0_O_Kb5sQN0Yc38KyZ1-VA9_JSFzuCgRRUwJPs5q8IImnUk807xxwgc4JAEn51EE4IXPlr5okyXoBkzBjVtynBIAl0kd3Tv6A-R0olagnEzb-GZQSZrimYgnj4HLWkUP6IKg-iRjEdIq3zWFMEYzCjbezojztId7Fe4R8d1_g6io_Ym7Jswf79Nrz7-0F6RLTA7GRAINOV9Obl4Dhvr3njtSlXMcARtXVF29x0APd7DPqXQS516BsAj5bLfiFywuuJPPc9MgPdJEGp4wdwOxkb2FdrnjSrVOcpY94FGa5MGdGZcOIDstsFlCxyX4ajqSbLpb_dkCA.jpg", "https://cdn5.telesco.pe/file/Hnhe3OJRyaLPXHrmxis1-22n-yQcqhpbN52d9fxbIlbkyeMfTA8s5jx8fPzfevhUA5Y3cZM5JVWrYJB4ADGwZojRM5iij_BXmqW41jOX1Vc9gux5uHnUhXa7Jp4cWx6Xan8sj9GkhhuTQ6014DTRV79wfiiD8EhnzNBXVcnkNSnaU-PxjdZ9OFkH5HP9Wywd3IOgJC5WsUCDjTvjIxcNxRnz40ZKSXb68G8MPPYTRFBVfQt4SS3XRLZyOyPh8cYRdGxS82kmIsr3W-bA-dlRS_2ZNCy0MjSBAguAQqStcXeJrkdjvBpM4F76uzKOTZcbb0NfWMrqvKvOJujRKehOog.jpg", "https://cdn5.telesco.pe/file/s4lfX6a95DzhoKxm71RX8ZuQFbUXTR8dlm9ggQt7QsQ836isNO5Fdwe-YkGKWB7GdZEiwmnNIXbqB2Z1uGmIcW-cjqwETuexNeT7-PxsU4Mce2F7jDEam1o9yNmk5ocpQxh8cciKpvfnlLbxb0HkDcBSyCZcUEfJ86-jc3-PG9sf3mBBUWYPWZQpeMLPlEm6R5rhJGCxQYvmruwYegmPnnSVDJRSXg4i7O6ApS2gWsMkDsjqTSzh-50xSaETyTdIa47S3Rq8BRm3YuNvnHwHjb8PB9TP8FlJGEh3-coKPVjYYY9jRb0QmVzgLXE2C7qQLprOE4TLcm0r_Axq09XGkQ.jpg"], "notice": "Описание собрано программой из полей телеграм-поста агентства — тип, спальни, санузлы, площадь, адрес и цена; рекламный текст не пересказан. Ссылка ведёт на сам пост, дата размещения взята из него. Фотографии из того же поста и лежат на серверах Telegram. Цену и условия подтверждайте у автора объявления. Район определён по улице: пост называет прежний район города, а после реформы 2025 года улица лежит в районе, указанном здесь.", "noticeEn": "This description was assembled by a program from the fields of an agency's Telegram post — type, bedrooms, bathrooms, size, address and price; the marketing text is not retold. The link points at the post itself and the posting date is taken from it. The photos come from the same post and are hosted by Telegram. Confirm the price and terms with the poster. The district comes from the street: the post names the city's former district, and since the 2025 reform the street lies in the district shown here."}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
