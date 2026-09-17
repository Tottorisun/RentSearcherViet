# -*- coding: utf-8 -*-
"""
Сборка сайта -- то же, что `python rebuild_final.py`, но без компиляции всего
файла разом.

ЗАЧЕМ. rebuild_final.py -- шаблон страницы вместе со всеми строками объявлений,
записанными как код Python (L(...)). 17.09.2026 это 9.9 МБ и 5181 строка.
`python rebuild_final.py` компилирует файл целиком, и пик памяти сборки --
около 255 МБ, а у службы прогона на сервере предел MemoryHigh=300M (MemoryMax=400M,
выше -- ядро убивает процесс). Прогон 17.09 17:00 уже дошёл до 302 МБ, а при
недельном сроке жизни и 500 строках Chợ Tốt за прогон файл растёт к 14-15 МБ.
Днём раньше тот же предел уронил сборщики, разбиравшие файл целиком (см.
listing_lock.template_without_listings).

КАК. Шаблон до списка LISTINGS выполняется как есть; каждая строка L(...)
вычисляется отдельно (listing_lock.iter_listing_blocks); затем выполняется остаток
шаблона -- с прежними номерами строк, чтобы трассировка ошибки указывала на
настоящее место в rebuild_final.py. Результат совпадает побайтно: проверено
сравнением всех файлов, которые пишет сборка, с `python rebuild_final.py`.

`python rebuild_final.py` по-прежнему работает и остаётся запасным путём. Если
список строк в файле не нашёлся, эта сборка сама выполняет файл целиком.

    python build_site.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

from listing_lock import MARKER, SOURCE, iter_listing_blocks


def main():
    src = open(SOURCE, encoding="utf-8").read()
    ns = {"__name__": "__main__", "__file__": os.path.join(HERE, SOURCE)}
    start = src.find("\nLISTINGS = [")
    end = src.find(MARKER)
    blocks = iter_listing_blocks(src)
    if start < 0 or end < start or blocks is None:
        exec(compile(src, SOURCE, "exec"), ns)
        return
    head = src[:start]
    tail_lead = "\n" * src.count("\n", 0, end + 1)   # остаток на своих номерах строк
    tail = src[end + 1:]                              # после «]», закрывающей LISTINGS
    del src
    exec(compile(head, SOURCE, "exec"), ns)
    rows = []
    for block in blocks:
        rows.extend(eval(compile("[" + block + "]", SOURCE, "eval"), ns))
    del blocks
    ns["LISTINGS"] = rows
    exec(compile(tail_lead + tail, SOURCE, "exec"), ns)


if __name__ == "__main__":
    main()
