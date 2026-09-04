# -*- coding: utf-8 -*-
"""Daily HCMC check, 4 Sep 2026 ~21:07 (continuation of the 3rd sweep whose
new_listings127.py batch had already inserted 4 rows but the pipeline never
finished -- picked up here, remove_gone_listings.py found 7 already-removed
GONE ids and 0 new removals, purge did not trigger). Chợ Tốt sweep across
tm/th/ak/btr/bq/bth/kh (area_v2=13096 Q1, 13099 Q4, 13102 Q7, 13109 Bình
Thạnh, 13119 Thủ Đức; cg=1010/1020/1050/1030) matched 1211 ads with a ward
in scope; after filtering to orig_list_time <=3.2 days and deduping list_id
against every URL already in rebuild_final.py, exactly 1 was genuinely new:
btr 1 (room). Verified FRESH (1.07d) by check_freshness.py. Batdongsan
Cloudflare-blocked most of this run (one probe got through with an empty
results page, most 403'd with a challenge page) -- not usable today.
Facebook not reachable headless as usual."""
from listing_lock import insert_listings

IDS = [1000479]

NEW_SRC = '''
L(1000479,"ho-chi-minh","btr","Комната",4500000,30,
  "Комната, 30 м², ул. Nguyễn Hoàng, Bình Trưng (Thủ Đức), рядом супермаркет Mega Market. Балкон, большое окно, кондиционер-инвертор, водонагреватель на солнечных батареях. Электричество 4 тыс.₫/кВт·ч, вода 100 тыс.₫/чел.",
  "https://www.nhatot.com/thue-phong-tro-thanh-pho-thu-duc-tp-ho-chi-minh/134493514.htm","вчера",1,source="chotot",
  descEn="Room, 30m², Nguyễn Hoàng St, Bình Trưng (Thủ Đức), near Mega Market supermarket. Balcony, large window, inverter AC, solar water heater. Electricity 4,000₫/kWh, water 100,000₫/person.",
  details={"photos": ["https://cdn.chotot.com/rPlWDJkUdafxjO7U5Q4NYFgIkkle6elJ-QcmIQPa6c4/preset:view/plain/807b97520a1378d44158f3af69952ac0-3000501288858550318.jpg", "https://cdn.chotot.com/UeA0WA1wqQkoycMqGb6XQ8RFKMn5YwxOdCH8IXRmr_g/preset:view/plain/d6cff8f746ce9fc542e6462c133bc6fd-3000501288704786272.jpg", "https://cdn.chotot.com/qJT2UW63pXfbI0y0HMFFFuu8inRmUTl6KvTj4Aup5d8/preset:view/plain/9c37678ccd794778e47119c38baa324e-3000501290136709512.jpg", "https://cdn.chotot.com/Bjjy5QJpYKur_3iwGdx4EJW_KWvbTwSNad42awev2jI/preset:view/plain/eb28e6ac516723483a19b90c43aee5fd-3000501290160034366.jpg", "https://cdn.chotot.com/cqn84GAnOCN36zyrsqxZZLE4IYCUdywql9wnPHit0jw/preset:view/plain/b8eee9998bed4ff632f6d8282ebb568b-3000501291842191200.jpg", "https://cdn.chotot.com/oWGoQQiHpXqcm4L_ttM7jKKj4n5UI2WOgjpNDRLWeXE/preset:view/plain/7a9332bda3d4a0937692489b025587ea-3000501291844960302.jpg"]}),
'''

if __name__ == "__main__":
    insert_listings(NEW_SRC, IDS, owner=__file__)
