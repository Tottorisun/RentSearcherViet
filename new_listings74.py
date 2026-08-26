# -*- coding: utf-8 -*-
NEW_SRC = '''
L(1718,"ho-chi-minh","ak","Студия",5500000,30,
  "Мини-квартира (студия), 30м², ул. Trần Não, An Khánh (бывший Q2) — есть окно (не глухая комната), полная меблировка, свободный график (вход по отпечатку пальца), тихий охраняемый квартал, просторная парковка с камерами 24/7, пожарная сигнализация; рядом рынок, супермаркет, кафе, удобно до Q1/Q3/Q7/Bình Thạnh.",
  "https://www.nhatot.com/thue-can-ho-chung-cu-thanh-pho-thu-duc-tp-ho-chi-minh/132639692.htm","1 день назад",1,source="chotot",
  details={"photos": ["https://cdn.chotot.com/ExjuBaQDCsst6iHWxwC181pW5Ab5xAwvHrBS7Dvy5-Y/preset:view/plain/6686c8815f72141f27999cf834351200-2986159418735567699.jpg", "https://cdn.chotot.com/AxKELD5tKisXTn9mAmLAK8DJf90_sHcr7Yc4_F8o7ho/preset:view/plain/8dff81237795f424e92c632fbc2d2469-2986159418711897291.jpg", "https://cdn.chotot.com/BktrXvCKUuVxz3pLiRasrh92Yp-VhqHUAFSXDooKyMQ/preset:view/plain/094d1001e647daf583a8c521c2be7bcd-2986159421392499870.jpg"]}),
'''

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content

new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
assert new_content != content
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", NEW_SRC.count("L("), "listings")
