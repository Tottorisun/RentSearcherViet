# -*- coding: utf-8 -*-
"""Daily HCMC check, 4 Sep 2026 evening (3rd sweep of the day; previous
sweeps already committed at 09:xx/13:xx/18:28 local -- f853b24, 43fd726,
ebf28e0, 07cc426). Chợ Tốt sweep across tm/th/ak/btr/bq/bth/kh
(area_v2=13102 Q7, 13119 Thủ Đức, 13109 Bình Thạnh, 13096 Q1, 13099 Q4;
cg=1010/1020/1050/1030) matched 604 ads with a ward in scope; 77 had
orig_list_time <=3.5 days old, and after deduping list_id against every
URL already in rebuild_final.py (the other 73 were already added by
today's earlier sweeps), 4 were genuinely new: tm 1 (room), th 2 (studio +
commercial), ak 1 (apartment). All 4 verified FRESH by check_freshness.py.
Nothing new in btr/bq/bth/kh this sweep.

Batdongsan and Facebook not re-checked this sweep (Batdongsan was swept
twice already today per prior batches; Facebook is not reachable headless,
see facebook_check_prompt.txt for the attended pass)."""
from listing_lock import insert_listings

IDS = [1000475, 1000476, 1000477, 1000478]

NEW_SRC = '''
L(1000475,"ho-chi-minh","tm","Комната",3000000,20,
  "Комната, 20 м², ул. Huỳnh Tấn Phát, 672B/34, Tân Mỹ (Q7), рядом промзона и супермаркеты. Свободный график, отдельный счётчик электричества по гостарифу, вода 25 тыс.₫/м³, охраняемый район.",
  "https://www.nhatot.com/thue-phong-tro-quan-7-tp-ho-chi-minh/133468272.htm","сегодня",0,source="chotot",
  descEn="Room, 20m², Huỳnh Tấn Phát St, 672B/34, Tân Mỹ (Q7), near an industrial zone and supermarkets. No curfew, own electricity meter at the state rate, water 25,000₫/m³, secure area.",
  details={"photos": ["https://cdn.chotot.com/MMUg0JQt2g3jaSuLSReyXGofdzPtMF48uV7Fa-ShOlo/preset:view/plain/41b39f225bf17c740d499033e8dcf5a4-2992497990684404119.jpg", "https://cdn.chotot.com/bkQHVlfH8MHHVOpaQ8JVQfICiwqeFJvnN5oYfL73IIg/preset:view/plain/dc0aa5584eafed7092dd4fd20ef49d75-2992497990416201229.jpg", "https://cdn.chotot.com/o5mVr8V0Ad5SYl66clKRKHJRbxwhI1JcGvHJ3oIw8PA/preset:view/plain/a82219357c40ad8c4e2102831ed7c056-2992497991927720447.jpg", "https://cdn.chotot.com/71GmRCNto3IJxXoQKaeyGan-R1vWkQhMZEdcyfU_KWw/preset:view/plain/f9cc7c92559da5ca85d49abc01e16869-2992497990585496381.jpg", "https://cdn.chotot.com/NEN3rAief9IJeP4oeBxOl9SoTKA-fynQpPiB-p1Lhzk/preset:view/plain/1358c644c05ae5a9e3fd8455531b1145-2992497992551933925.jpg", "https://cdn.chotot.com/0UllgMVvv_3Mo027TF3k6Nw315Ab3paziLBvC7eu8rU/preset:view/plain/21c9050dfce050a2ce53967dd0b1a584-2992497991123820652.jpg"]}),
L(1000476,"ho-chi-minh","th","Студия",6000000,30,
  "Студия, 30 м², ул. Nguyễn Thị Thập, Tân Hưng (Q7), рядом RMIT, ĐH Tôn Đức Thắng, Lotte, Him Lam. Полностью новая меблировка, балкон/окно.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-7-tp-ho-chi-minh/133874177.htm","2 дня назад",2,source="chotot",
  descEn="Studio, 30m², Nguyễn Thị Thập St, Tân Hưng (Q7), near RMIT, Tôn Đức Thắng University, Lotte, Him Lam. Fully new furnishings, balcony/window.",
  details={"notice": "Объявление агентства с несколькими вариантами по системе апартаментов в этом районе Q7 — уточняйте конкретную планировку и этаж при звонке.", "noticeEn": "Agency listing covering several unit options in this Q7 apartment-management system — confirm the exact layout and floor when calling.", "photos": ["https://cdn.chotot.com/kchHLl-xWLZoCoOF-jiNwZEpx360nZMPAzFqGvaGNLY/preset:view/plain/404210d2f3737a81c27c8c577aaa2438-2995578430725745662.jpg", "https://cdn.chotot.com/e_PD04zGIKfV482Cik2fxzBAPgI8XQNiW4IeFcjHOMg/preset:view/plain/9d3547a079e305001cb4a512b77f2561-2995578430940102335.jpg", "https://cdn.chotot.com/raME5M4XKZuFd-q3VYvVhQli00RDyX41PoJ6AIw79Ns/preset:view/plain/56f8ad10b2d031d9090f5f4373228426-2995578430619934605.jpg", "https://cdn.chotot.com/tcq3mXfGUKbGv48DLY9ZK5dnltO9j-EVamjWhXQSAUs/preset:view/plain/812e6c6544ecad825660e2970034af6c-2995578430544748382.jpg", "https://cdn.chotot.com/wAtJj3lhvWMwX-boI70dtraZOCZJw5-UXfNYTdC2Ids/preset:view/plain/8ade547de3b95dc10f250813485d9118-2995578430391973263.jpg", "https://cdn.chotot.com/r_CaHDMPELTIaJs2I01o_jawcSggTKeOtUwYidLDui0/preset:view/plain/93b296b1c5c3703aae9b4e569d234d9a-2995578430208417650.jpg"]}),
L(1000477,"ho-chi-minh","ak","Квартира",6500000,40,
  "Квартира с балконом, 40 м², ул. Trần Não, An Khánh, у подножия моста Sài Gòn. Полная меблировка, просторный балкон, вход по отпечатку пальца, охрана 24/7, вместительная парковка.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/134090849.htm","3 дня назад",3,source="chotot",
  descEn="Apartment with a balcony, 40m², Trần Não St, An Khánh, at the foot of the Sài Gòn Bridge. Fully furnished, spacious balcony, fingerprint entry, 24/7 security, ample parking.",
  details={"photos": ["https://cdn.chotot.com/JJ9IfyUSYdFFT82Pian00TPFb0zVqlappYGMKguq1Uo/preset:view/plain/4f082077cd173efe6205edac0e5e01c6-2997259035764166214.jpg", "https://cdn.chotot.com/pBfXga_pT6snvWhpUJQlb-P0NjS4KJLe1BgFd2syhd0/preset:view/plain/d9b7860efb8920a71d164bd9de294ca8-2997259035744950661.jpg", "https://cdn.chotot.com/-ih0fT2F6XCWxD07qAQAXtpRpK2ZdUaeefAerAY7cHM/preset:view/plain/a5b3de7853f48ed87c98e15edd6e6ca4-2997259038321910036.jpg", "https://cdn.chotot.com/shEQV0JCJm5fCg-eyGMcI3rrYa-BP6MnWSrkpHqM3zg/preset:view/plain/1ab0ede1cab72afdb9c456b2628f0b33-2997259038279828568.jpg", "https://cdn.chotot.com/Jly-H5wp48rYr9ftpAJqaZQVZNlQg7a_42FpquPYxsI/preset:view/plain/d09c36bbb2bdb16b5d0465a0c0e4e0f8-2997259040423713737.jpg", "https://cdn.chotot.com/OOjzBM_jtj1KPhSgK86k-TWVVqguubyXoQa1-Kqgrq4/preset:view/plain/cfd630b30f5ed66734bdacf24f60deee-2997259040492523931.jpg"]}),
L(1000478,"ho-chi-minh","th","Торговая площадь",70000000,350,
  "Торговая площадь на первой линии, ул. số 10, Tân Kiểng, Tân Hưng (Q7). 8×30 м, 1 этаж + антресоль, оживлённый район, удобный выезд в Q4/Q1/Q8. Подходит под шоурум, мини-маркет, ресторан/кафе, склад с офисом, бильярдную, спортзал.",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-quan-7-tp-ho-chi-minh/134458428.htm","3 дня назад",3,source="chotot",
  descEn="Street-front commercial space, số 10 St, Tân Kiểng, Tân Hưng (Q7). 8x30m, ground floor + mezzanine, busy area, easy access to Q4/Q1/Q8. Suits a showroom, mini-mart, restaurant/cafe, warehouse with office, billiards hall, or gym.",
  details={"photos": ["https://cdn.chotot.com/P07r2dM0PNt4yyS7qmAHEysAvR0c31FFCPgdma38TPw/preset:view/plain/f80520f0e51bd1c872c1d0ec60c69c2a-3000161196025298513.jpg", "https://cdn.chotot.com/WH_rtQJt89DR7gSGRPjYVWvtZWNHjqck2-DAbkrXIOs/preset:view/plain/86845ec36f802ef064a7f2a85c92e006-3000161196418344327.jpg", "https://cdn.chotot.com/UCYJoudClbSqzn4xorJz9yubJFgw_jN9I6RGWXM2BDs/preset:view/plain/f5c07acbba4b7742ca449c2968793077-3000161199377219630.jpg"]}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
