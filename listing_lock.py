# -*- coding: utf-8 -*-
"""
One lock for every script that rewrites rebuild_final.py, plus the only
sanctioned way to insert new L(...) rows into it.

WHY THIS EXISTS. allocate_ids.py serialises the hand-out of listing ids, but
not the write of the file itself. Two sessions could still each read
rebuild_final.py, each insert its own rows, and the second write silently
dropped the first one's listings -- while the first session had already
released its id reservation, so the same numbers were handed out again.
That is the class of failure allocate_ids.py's own header says has happened
four times; the id lock closed the hand-out, this closes the write
(2 Sep 2026 audit, HIGH-4).

USAGE
    from listing_lock import insert_listings
    insert_listings(NEW_SRC, ids, owner="hcmc batch 108")

  or, for any other read-modify-write of rebuild_final.py:

    from listing_lock import listings_write_lock, write_source_atomic
    with listings_write_lock("purge"):
        src = open("rebuild_final.py", encoding="utf-8").read()
        ...
        write_source_atomic(new_src)

insert_listings() is idempotent and self-checking: it refuses an id that is
already in the file (re-running a batch used to duplicate it), checks that
the batch declares exactly the ids it contains, verifies that exactly
len(ids) rows were added, re-parses the result with ast, and writes through
a temp file + os.replace so no reader ever sees a half-written file.
"""
import ast
import os
import re
import sys
import time
from contextlib import contextmanager

SOURCE = "rebuild_final.py"
LOCK_FILE = ".listings_write.lock"
MARKER = "]\n\n# Real lat/lon"
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
                         "(lock holder: %s). Retry shortly." % (SOURCE, TIMEOUT_S, holder))
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


def listing_ids(src):
    return [int(x) for x in re.findall(r"^L\((\d+),", src, re.M)]


def write_source_atomic(new_src):
    """Refuse to write anything that is not valid Python; then replace the
    file in one step so a concurrent reader gets old-or-new, never half."""
    ast.parse(new_src)
    tmp = "%s.tmp.%d" % (SOURCE, os.getpid())
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(new_src)
    os.replace(tmp, SOURCE)


def find_blocks(src):
    """{listing id: (first line, last line)} for every L(...) element of the
    LISTINGS list, via ast -- exact, never a regex guess. Lines are 1-based
    and inclusive, so `lines[a-1:b]` is the block."""
    tree = ast.parse(src)
    lists = [n for n in tree.body if isinstance(n, ast.Assign)
             and any(getattr(t, "id", None) == "LISTINGS" for t in n.targets)]
    if len(lists) != 1 or not isinstance(lists[0].value, ast.List):
        sys.exit("could not find exactly one `LISTINGS = [...]` list in %s" % SOURCE)
    out = {}
    for e in lists[0].value.elts:
        if isinstance(e, ast.Call) and e.args and isinstance(e.args[0], ast.Constant):
            out[int(e.args[0].value)] = (e.lineno, e.end_lineno)
    return out


def remove_listings(ids, owner="remove"):
    """Delete the L(...) blocks of `ids` under the write lock. Ids not in the
    file are reported and skipped; the rewrite is re-parsed and its block
    count checked before anything is written. Returns the ids removed."""
    ids = sorted({int(i) for i in ids})
    if not ids:
        return []
    with listings_write_lock(owner):
        src = open(SOURCE, encoding="utf-8").read()
        blocks = find_blocks(src)
        missing = [i for i in ids if i not in blocks]
        if missing:
            print("remove_listings: not in %s (already gone?): %s" % (SOURCE, missing))
        todo = [i for i in ids if i in blocks]
        if not todo:
            return []
        lines = src.split("\n")
        for i in sorted(todo, key=lambda i: blocks[i][0], reverse=True):
            a, b = blocks[i]
            start, end = a - 1, b
            if end < len(lines) and lines[end].strip() == "":
                end += 1                       # swallow one trailing blank line
            del lines[start:end]
        new_src = "\n".join(lines)
        if len(find_blocks(new_src)) != len(blocks) - len(todo):
            sys.exit("remove_listings: block count after rewrite is wrong -- nothing written")
        write_source_atomic(new_src)
    return todo


def insert_listings(new_src, ids, owner="batch"):
    """Insert NEW_SRC -- one or more complete `L(...),` rows, each starting at
    column 0 -- at the end of the LISTINGS list. Idempotent and self-checking."""
    ids = sorted(int(i) for i in ids)
    new_src = new_src.strip("\n") + "\n"
    in_new = sorted(listing_ids(new_src))
    if in_new != ids:
        sys.exit("NEW_SRC contains ids %s but the batch declares %s -- fix the batch file" % (in_new, ids))
    with listings_write_lock(owner):
        src = open(SOURCE, encoding="utf-8").read()
        present = set(listing_ids(src))
        clash = [i for i in ids if i in present]
        if clash:
            sys.exit("refusing to insert: id(s) already in %s: %s -- was this batch already "
                     "applied, or were the ids handed out twice? Nothing written." % (SOURCE, clash))
        if src.count(MARKER) != 1:
            sys.exit("marker %r found %d time(s) in %s, expected exactly 1 -- nothing written"
                     % (MARKER, src.count(MARKER), SOURCE))
        out = src.replace(MARKER, new_src + MARKER, 1)
        added = len(listing_ids(out)) - len(present)
        if added != len(ids):
            sys.exit("expected to add %d row(s) but the rewritten file has %d more -- nothing written"
                     % (len(ids), added))
        write_source_atomic(out)
    print("inserted %d listing(s) into %s: %d..%d" % (len(ids), SOURCE, ids[0], ids[-1]))
    return len(ids)
