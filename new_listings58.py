# -*- coding: utf-8 -*-

with open("new_listings58_body.txt", encoding="utf-8") as f:
    NEW_SRC = f.read()

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()
marker = "]\n\n# Real lat/lon"
assert marker in content

new_content = content.replace(marker, NEW_SRC.strip() + "\n" + marker, 1)
assert new_content != content
open(path, "w", encoding="utf-8").write(new_content)
print("inserted", NEW_SRC.count("L("), "listings")
