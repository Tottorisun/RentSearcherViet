# -*- coding: utf-8 -*-
import requests, json, time, sys
# reconfigure, not `sys.stdout = io.TextIOWrapper(sys.stdout.buffer, ...)`:
# the replaced wrapper closes the underlying stream when it is collected,
# and every later print then dies with "I/O operation on closed file" --
# which in a background run looks like a hang, not an error.
sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

ids = [133359508, 134056333, 133613805, 134377788, 130008809, 133769363, 134367086, 134366877, 133735024, 133064208, 134348579]

details = {}
for i in ids:
    url = f"https://gateway.chotot.com/v1/public/ad-listing/{i}"
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
            d = r.json()
            details[i] = d
            break
        except Exception as e:
            print("ERR", i, "attempt", attempt, e)
            time.sleep(2)
    time.sleep(0.3)

with open("today_details.json", "w", encoding="utf-8") as f:
    json.dump(details, f, ensure_ascii=False, indent=1)

for i, d in details.items():
    ad = d.get("ad", d)
    print("====", i)
    print("subject:", ad.get("subject"))
    print("price:", ad.get("price"), "size:", ad.get("size"))
    print("ward:", ad.get("ward_name_v3"), "street:", ad.get("street_name"))
    print("area:", ad.get("area"))
    print("images:", (ad.get("images") or [])[:3])
    print("body:", (ad.get("body") or "")[:400])
    print()
