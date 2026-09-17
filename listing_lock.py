# -*- coding: utf-8 -*-
"""
One lock for every script that changes the listing rows, plus the only
sanctioned way to insert and remove them.

WHY THIS EXISTS. allocate_ids.py serialises the hand-out of listing ids, but
not the write of the file itself. Two sessions could still each read
rebuild_final.py, each insert its own rows, and the second write silently
dropped the first one's listings -- while the first session had already
released its id reservation, so the same numbers were handed out again.
That is the class of failure allocate_ids.py's own header says has happened
four times; the id lock closed the hand-out, this closes the write
(2 Sep 2026 audit, HIGH-4).

WHERE THE ROWS LIVE. Since 17 Sep 2026 in listings/<source>/<city>.jsonl, one
JSON object per line -- the dict rebuild_final.py's L() builds, plus postedOn and
seq (see DATA_DIR below). rebuild_final.py is the page template and loads them.

USAGE
    from listing_lock import insert_listings, remove_listings
    insert_listings(NEW_SRC, ids, owner="hcmc batch 108")
    remove_listings([...ids...], owner="remove_gone")

  or, for any other read-modify-write of the rows:

    from listing_lock import listings_write_lock, load_rows, save_rows
    with listings_write_lock("purge"):
        rows = load_rows()
        ...
        save_rows(rows)

insert_listings() is idempotent and self-checking: it refuses an id or a URL
that is already on the site (re-running a batch used to duplicate it), checks
that the batch declares exactly the ids it contains, and save_rows() writes
every changed file through a temp file + os.replace so no reader ever sees a
half-written file.
"""
import ast
import collections
import json
import os
import re
import sys
import time
from contextlib import contextmanager

SOURCE = "rebuild_final.py"
LOCK_FILE = ".listings_write.lock"
TIMEOUT_S = 180      # a purge or a batch insert takes seconds; 3 minutes of waiting is plenty
STALE_S = 900        # a holder silent for 15 minutes is dead, not slow


def _take_over_stale_lock():
    """Only ONE waiter may remove a stale lock. Rename is atomic, so the process
    whose os.replace succeeds owns the corpse and deletes it; every other
    waiter's rename fails and they simply keep waiting. (Plain unlink lets
    two waiters both 'break' the lock and both proceed.)"""
    corpse = "%s.stale.%d" % (LOCK_FILE, os.getpid())
    try:
        os.replace(LOCK_FILE, corpse)
    except FileNotFoundError:
        return
    try:
        os.unlink(corpse)
    except FileNotFoundError:
        pass


def acquire(owner=""):
    deadline = time.time() + TIMEOUT_S
    while True:
        try:
            fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, ("%d %s %s" % (os.getpid(), time.strftime("%Y-%m-%d %H:%M:%S"), owner)).encode("utf-8"))
            os.close(fd)
            return
        except FileExistsError:
            try:
                age = time.time() - os.path.getmtime(LOCK_FILE)
            except FileNotFoundError:
                continue                      # released between our two checks
            if age > STALE_S:
                _take_over_stale_lock()
                continue
            if time.time() > deadline:
                try:
                    holder = open(LOCK_FILE, encoding="utf-8").read().strip()
                except OSError:
                    holder = "?"
                sys.exit("could not lock %s within %ds -- another session is writing it "
                         "(lock holder: %s). Retry shortly." % (DATA_DIR, TIMEOUT_S, holder))
            time.sleep(0.5)


def release():
    try:
        os.unlink(LOCK_FILE)
    except FileNotFoundError:
        pass


@contextmanager
def listings_write_lock(owner=""):
    acquire(owner)
    try:
        yield
    finally:
        release()


def listing_ids(src=None):
    """id строк: без аргумента -- всех строк в listings/; с текстом -- вызовов L(...)
    в нём (так их считает партия)."""
    if src is None:
        return [r["id"] for r in load_rows()]
    return [int(x) for x in re.findall(r"^L\((\d+),", src, re.M)]


# ---------------------------------------------------------------------------
# Функции и CITIES шаблона -- для сборщиков; каждая разбирается один раз на
# процесс. 17.09.2026 collect_chotot разбирал весь rebuild_final.py (тогда ещё со
# строками, 164 МБ на разбор) на КАЖДУЮ строку партии -- 500 раз за прогон, и два
# прогона подряд не уложился в таймаут при пределе службы MemoryHigh=300M.

_TEMPLATE_CACHE = {}


def _template_tree():
    with open(SOURCE, encoding="utf-8") as f:
        return ast.parse(f.read())


def template_function(name):
    """Функция шаблона (например _ru_days_label или L), разобранная один раз на процесс."""
    key = ("fn", name)
    if key not in _TEMPLATE_CACHE:
        fn = next(x for x in ast.walk(_template_tree()) if isinstance(x, ast.FunctionDef) and x.name == name)
        ns = {}
        exec(ast.unparse(fn), ns)
        _TEMPLATE_CACHE[key] = ns[name]
    return _TEMPLATE_CACHE[key]


def template_cities():
    """CITIES шаблона. Возвращается новая копия: вызывающие вправе её менять."""
    key = ("cities",)
    if key not in _TEMPLATE_CACHE:
        node = next(n for n in ast.walk(_template_tree())
                    if isinstance(n, ast.Assign) and any(getattr(t, "id", None) == "CITIES" for t in n.targets))
        _TEMPLATE_CACHE[key] = ast.unparse(node.value)
    return ast.literal_eval(_TEMPLATE_CACHE[key])


# ---------------------------------------------------------------------------
# Строки объявлений -- в listings/<источник>/<город>.jsonl, по одной на строку
# файла (с 17.09.2026). До того они стояли в rebuild_final.py кодом L(...): 9.9 МБ
# на 5181 строку, и всякий, кто их читал или правил, разбирал этот код -- при
# пределе памяти службы на сервере (MemoryHigh=300M, прогон 17.09 17:00 дошёл до
# 302 МБ). Строка файла -- словарь, который строит L() шаблона, плюс поля только
# для хранения: postedOn (дата выкладки, нужна чистке) и seq (порядок строк на
# сайте). Файлы -- по источникам и городам: сервер и ПК пишут в основном разные
# файлы, а git сравнивает построчно.

DATA_DIR = "listings"
STORE_ONLY = ("postedOn", "seq")


def row_path(row, data_dir=None):
    return os.path.join(data_dir or DATA_DIR, row.get("source") or "chotot", "%s.jsonl" % row["city"])


def _row_files(data_dir=None):
    base = data_dir or DATA_DIR
    if not os.path.isdir(base):
        sys.exit("нет каталога %s/ со строками объявлений -- запускайте из каталога проекта" % base)
    out = []
    for source in sorted(os.listdir(base)):
        d = os.path.join(base, source)
        if os.path.isdir(d):
            out.extend(os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".jsonl"))
    return out


def _site_order(row):
    return (row.get("seq", 0), row["id"])


def load_rows(data_dir=None):
    """Все строки -- словарями, в порядке сайта (seq, id)."""
    rows = []
    for path in _row_files(data_dir):
        with open(path, encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except ValueError as ex:
                    sys.exit("%s, строка %d: не JSON (%s) -- файл строк испорчен, ничего не сделано"
                             % (path, n, ex))
    rows.sort(key=_site_order)
    return rows


def load_page_rows(data_dir=None):
    """Строки для страницы -- без полей хранения. Ни одной строки -- отказ, а не пустой сайт."""
    rows = load_rows(data_dir)
    if not rows:
        sys.exit("в %s/ нет ни одной строки объявления -- пустой сайт не собирается" % (data_dir or DATA_DIR))
    return [{k: v for k, v in r.items() if k not in STORE_ONLY} for r in rows]


def _dump(row):
    return json.dumps(row, ensure_ascii=False, separators=(",", ":"))


def save_rows(rows, data_dir=None):
    """Записать ПОЛНЫЙ набор строк. Переписывается только файл, чьё содержимое
    изменилось (временный файл + os.replace); опустевший файл удаляется.
    Вызывать под listings_write_lock."""
    ids = [r["id"] for r in rows]
    if len(set(ids)) != len(ids):
        dup = [i for i, n in collections.Counter(ids).items() if n > 1]
        sys.exit("save_rows: повторяющиеся id %s -- ничего не записано" % dup[:10])
    by_path = collections.defaultdict(list)
    for r in rows:
        by_path[row_path(r, data_dir)].append(r)
    existing = set(_row_files(data_dir))
    for path in sorted(set(by_path) | existing):
        text = "".join(_dump(r) + "\n" for r in sorted(by_path.get(path, []), key=_site_order))
        if path in existing:
            with open(path, encoding="utf-8", newline="") as f:
                if f.read() == text:
                    continue
        if not text:
            os.remove(path)
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = "%s.tmp.%d" % (path, os.getpid())
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        os.replace(tmp, path)


def remove_listings(ids, owner="remove"):
    """Снять строки с этими id под блокировкой. Отсутствующие id называются и
    пропускаются. Возвращает снятые id."""
    ids = sorted({int(i) for i in ids})
    if not ids:
        return []
    with listings_write_lock(owner):
        rows = load_rows()
        present = {r["id"] for r in rows}
        missing = [i for i in ids if i not in present]
        if missing:
            print("remove_listings: not in %s (already gone?): %s" % (DATA_DIR, missing))
        todo = [i for i in ids if i in present]
        if not todo:
            return []
        drop = set(todo)
        save_rows([r for r in rows if r["id"] not in drop])
    return todo


# Источники, у которых одна ссылка на несколько объявлений -- норма, а не ошибка:
# телеграм-строки ссылаются на канал, а не на конкретный пост.
SHARED_URL_SOURCES = {"telegram", "facebook"}


def _listing_urls(rows):
    """{нормализованный url: id} -- кроме источников с общей ссылкой; при повторе -- первый."""
    out = {}
    for r in rows:
        if (r.get("source") or "chotot") in SHARED_URL_SOURCES:
            continue
        url = r.get("url")
        if isinstance(url, str):
            out.setdefault(url.split("?")[0].rstrip("/"), r["id"])
    return out


def rows_from_src(new_src):
    """Текст партии -- строки `L(...),` -- в словари, как их строит L() шаблона.
    Аргументы -- только литералы (так написаны все партии: 8694 вызова на
    17.09.2026). postedOn L() в данные страницы не кладёт; здесь он сохраняется."""
    L = template_function("L")
    try:
        tree = ast.parse(new_src.strip("\n") + "\n")
    except SyntaxError as ex:
        sys.exit("NEW_SRC is not valid Python (%s) -- fix the batch file, nothing written" % ex)
    rows = []
    for stmt in tree.body:
        value = stmt.value if isinstance(stmt, ast.Expr) else None
        for call in (value.elts if isinstance(value, ast.Tuple) else [value]):
            if not (isinstance(call, ast.Call) and getattr(call.func, "id", "") == "L"):
                sys.exit("NEW_SRC, line %d: only `L(...),` rows are allowed -- nothing written" % stmt.lineno)
            try:
                args = [ast.literal_eval(a) for a in call.args]
                kw = {k.arg: ast.literal_eval(k.value) for k in call.keywords}
            except ValueError:
                sys.exit("NEW_SRC, line %d: L(...) arguments must be literals -- nothing written" % call.lineno)
            row = L(*args, **kw)
            if kw.get("postedOn") is not None:
                row["postedOn"] = kw["postedOn"]
            rows.append(row)
    return rows


def insert_listings(new_src, ids, owner="batch"):
    """Завести строки партии -- NEW_SRC из строк `L(...),` -- в listings/. Партия
    объявляет ровно свои id; ни id, ни ссылки ещё не должно быть на сайте. Новые
    строки встают в конец порядка сайта (seq)."""
    ids = sorted(int(i) for i in ids)
    in_new = sorted(listing_ids(new_src))
    if in_new != ids:
        sys.exit("NEW_SRC contains ids %s but the batch declares %s -- fix the batch file" % (in_new, ids))
    new_rows = rows_from_src(new_src)
    if sorted(r["id"] for r in new_rows) != ids:
        sys.exit("NEW_SRC rows carry ids %s but the batch declares %s -- fix the batch file"
                 % (sorted(r["id"] for r in new_rows), ids))
    with listings_write_lock(owner):
        rows = load_rows()
        present = {r["id"] for r in rows}
        clash = [i for i in ids if i in present]
        if clash:
            sys.exit("refusing to insert: id(s) already in %s: %s -- was this batch already "
                     "applied, or were the ids handed out twice? Nothing written." % (DATA_DIR, clash))
        have = _listing_urls(rows)
        dup_urls = [(u, have[u]) for u in _listing_urls(new_rows) if u in have]
        if dup_urls:
            sys.exit("refusing to insert: %d listing(s) whose URL is already in %s.\n%s\n"
                     "Один и тот же URL -- это одно и то же объявление. Проверка по id этого "
                     "не ловит: две сессии одного дня берут с Chợ Tốt один ад и получают разные "
                     "id. 8 сентября 2026 так набралось 49 задвоенных ссылок, 13 из них за одни "
                     "сутки. Уберите повтор из партии; если это осознанное исключение (ссылка на "
                     "канал, а не на объявление) -- добавьте источник в SHARED_URL_SOURCES."
                     % (len(dup_urls), DATA_DIR,
                        "\n".join("  %s уже заведён как id %s" % (u, i) for u, i in dup_urls)))
        seq = max((r.get("seq", 0) for r in rows), default=-1) + 1
        for n, r in enumerate(new_rows):
            r["seq"] = seq + n
        save_rows(rows + new_rows)
    print("inserted %d listing(s) into %s: %d..%d" % (len(ids), DATA_DIR, ids[0], ids[-1]))
    return len(ids)
