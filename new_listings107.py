# -*- coding: utf-8 -*-
NEW_SRC = """\
L(1000305,"ho-chi-minh","tm","Торговая площадь",19000000,90,
  "Торговое помещение на фасаде ул. Huỳnh Tấn Phát, д. 1272, Tân Mỹ (Phú Mỹ), Q7. Площадь 90 м².",
  "https://www.nhatot.com/thue-van-phong-mat-bang-kinh-doanh-quan-7-tp-ho-chi-minh/134472677.htm","сегодня",0,source="chotot",
  details={"photos": ["https://cdn.chotot.com/zFQg4ml5PkPq-JcEIS4m5Zf-gP5O19LKNkzrrCwrrHI/preset:view/plain/1d2236d0bba5eac0f49aafb3c2e5def6-3000319966322488882.jpg", "https://cdn.chotot.com/tMBHMwXTpwHQDUOi0T8RKXGOTDJMu8vRhZhf4vX_9Zk/preset:view/plain/448d7321b1e5730e11a20e056f2700da-3000319966077976622.jpg", "https://cdn.chotot.com/-Gry11iN2j7nemXpLE6yNep3M8PTmZKChAgKJCEy0w0/preset:view/plain/97022f005f2eaf09f6538b3142b98dde-3000319968630297001.jpg"]},
  descEn="Street-front commercial unit on Huynh Tan Phat St, #1272, Tan My (Phu My), Q7. 90m2."),
L(1000306,"ho-chi-minh","kh","Квартира",12000000,70,
  "Квартира в доме H3, ул. Hoàng Diệu, Khánh Hội, Q4. 70 м², 2 спальни, 1 санузел, свежий ремонт, кондиционер и водонагреватель. 12 млн ₫/мес. Также доступны варианты: 70 м² без мебели за 9,5 млн ₫/мес (заезд с октября 2026), и 56 м² с мебелью, 1 спальня, за 11 млн ₫/мес.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-quan-4-tp-ho-chi-minh/134147662.htm","вчера",1,source="chotot",
  details={"photos": ["https://cdn.chotot.com/U1JePEL0RGvZPmxmR3d9QebZ-SopQ8QDB41n6BjBCZY/preset:property_project_small/plain/2011_overview_2.jpg", "https://cdn.chotot.com/6bG2BXAO0_Ss9n6IVpJ6_Ano4Wv95gHrEA0AM4dzeac/preset:property_project_small/plain/5a90444a-2f6b-4c7c-839c-dc756d86d594.jpg", "https://cdn.chotot.com/Rz0XBQGpD_0Qa783FjL82KOEaIlUiGTl2p82o7dDBMg/preset:property_project_small/plain/2011_floor_plan_project_6.jpg"]},
  descEn="Apartment in the H3 building, Hoang Dieu St, Khanh Hoi, Q4. 70m2, 2 bedrooms, 1 bathroom, freshly renovated, AC and water heater. 12M VND/month. Alternative options also available: 70m2 unfurnished for 9.5M VND/month (move-in from October 2026), or 56m2 furnished 1-bedroom for 11M VND/month."),
L(1000307,"ho-chi-minh","bq","Комната",1700000,16,
  "Отдельная комната 16 м² на первом этаже (без антресоли), отдельный вход, санузел и кухня в комнате, кровать в комплекте. Свободный доступ 24/7, отдельно от хозяев. Thanh Đa (Bình Quới), тихий район. Свободна для заезда сейчас.",
  "https://www.nhatot.com/thue-phong-tro-quan-binh-thanh-tp-ho-chi-minh/131424232.htm","вчера",1,source="chotot",
  details={"photos": ["https://cdn.chotot.com/IUWZS94Um_Gm6PUZbfqOQpCkwcAhHV6sgvNdRNvuBLk/preset:view/plain/399f4146791337d8b28b9a938afccc3b-2994927687360959344.jpg", "https://cdn.chotot.com/wLKuvbnGcEu-vQGd-_2bG5sVEFmA5tS7E5J-WirvoKU/preset:view/plain/c7239c8353fbedfa3ae2f0af6fe41fcb-2994927687494742569.jpg", "https://cdn.chotot.com/eNkBgGPOeV0DcHeF_z8XjhM6QxaPi2UwJemi3Y4j6fs/preset:view/plain/663acd3f9fd9d447b5f3081d70449dc4-2994927688787088240.jpg"]},
  descEn="Standalone ground-floor room, 16m2, no mezzanine, private entrance, own bathroom and kitchen, bed included. Free 24/7 access, fully separate from the landlord's living space. Thanh Da peninsula (Binh Quoi), quiet area. Available for immediate move-in."),
"""

with open("rebuild_final.py", encoding="utf-8") as f:
    content = f.read()

marker = "]\n\n# Real lat/lon"
idx = content.find(marker)
if idx == -1:
    raise SystemExit("marker not found")

new_content = content[:idx] + NEW_SRC + content[idx:]

with open("rebuild_final.py", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Inserted", NEW_SRC.count(chr(10)+"L("), "new listings")
