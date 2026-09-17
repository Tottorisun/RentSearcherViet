# -*- coding: utf-8 -*-
# Remove specific L(id, ...) entries (multi-line) from rebuild_final.py by id.
import re

REMOVE_IDS = [571, 572, 575, 590, 591, 593, 595, 596]

path = "rebuild_final.py"
content = open(path, encoding="utf-8").read()

for _id in REMOVE_IDS:
    # Match from "L(<id>," through the closing "),\n" right before the next "\nL(" or "\n]"
    pattern = re.compile(r'\nL\(' + str(_id) + r',.*?\}\),\n', re.S)
    new_content, n = pattern.subn('\n', content, count=1)
    if n != 1:
        print(f"WARNING: id {_id} matched {n} times, expected 1")
    else:
        content = new_content
        print(f"removed id {_id}")

open(path, "w", encoding="utf-8").write(content)
