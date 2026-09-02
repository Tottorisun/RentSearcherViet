# -*- coding: utf-8 -*-
"""
TEMPLATE for a daily-check batch file. Copy to new_listings<N>.py, fill in
IDS (exactly the range allocate_ids.py handed you) and NEW_SRC (one complete
`L(...),` row per listing, each starting at column 0, ids in the same
range), then run it: `python new_listings<N>.py`.

Everything that used to be copy-pasted boilerplate at the bottom of every
batch file (read rebuild_final.py, find the marker, replace, write) now
lives in listing_lock.insert_listings(), which also:
  * takes the write lock, so two sessions can no longer overwrite each
    other's rows in rebuild_final.py;
  * refuses ids that are already in the file (re-running a batch used to
    insert duplicates);
  * checks that NEW_SRC declares exactly IDS and that exactly len(IDS)
    rows were added;
  * re-parses the result and writes it atomically.

Do NOT open or write rebuild_final.py yourself in a batch file.
"""
from listing_lock import insert_listings

IDS = [1000999]          # <- the FIRST..LAST range from allocate_ids.py, expanded

NEW_SRC = '''
L(1000999,"ho-chi-minh","tm","Квартира",9000000,60,
  "2-спальная квартира, 60 м², ЖК Example, ул. Nguyễn Lương Bằng, Tân Mỹ. Полная меблировка.",
  "https://www.nhatot.com/example/123456.htm","сегодня",0,source="chotot",
  descEn="2-bedroom apartment, 60m², Example complex, Nguyễn Lương Bằng St, Tân Mỹ. Fully furnished.",
  details={'photos': ['https://cdn.chotot.com/example-1.jpg', 'https://cdn.chotot.com/example-2.jpg', 'https://cdn.chotot.com/example-3.jpg']}),
'''

if __name__ == "__main__":
    if IDS == [1000999]:
        raise SystemExit("this is the template -- copy it to new_listings<N>.py and fill in IDS and NEW_SRC first")
    insert_listings(NEW_SRC, IDS, owner=__file__)
