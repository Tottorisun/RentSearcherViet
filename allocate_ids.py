# -*- coding: utf-8 -*-
"""
Atomically reserve a block of listing ids.

WHY THIS EXISTS
Listing-id collisions have corrupted this dataset four times. Two fixes were
tried and each closed only part of the hole:

  1. "grep the max id and continue from there" -- races whenever two checks
     overlap in time: both read the same max, both start there.
  2. "give each check its own id range" (HCMC 1000000+, 7-city 2000000+) --
     fixes collisions BETWEEN the two checks, but two concurrent instances of
     the SAME check still share a range and still collide. That has happened
     here before (a duplicated HCMC run).

Even "re-read the max at write time" leaves two gaps:
  - the read->write window itself: two processes can still read the same max;
  - ids handed out but not yet written into rebuild_final.py are invisible to
    anyone grepping the file.

This closes both. An exclusive lock (atomic O_CREAT|O_EXCL, which is atomic on
Windows too) serialises allocation, and a reservation ledger records ids that
are spoken for but not yet written, so a concurrent caller cannot reuse them.

USAGE
  python allocate_ids.py --block 1000000 --count 12
      -> prints the reserved range, e.g.  1000042-1000053
         and a machine-readable last line: FIRST=1000042 LAST=1000053

  python allocate_ids.py --block 2000000 --count 5 --owner other-cities

  # a long job should refresh its reservation periodically so it cannot
  # expire while the job is still running:
  python allocate_ids.py --renew 1000042-1000053

  # after the listings are actually written into rebuild_final.py:
  python allocate_ids.py --release 1000042-1000053

Blocks: 1000000 = daily HCMC check, 2000000 = daily 7-city check.
Reservations older than --stale-hours (default 24) are ignored, so a crashed
run cannot wedge the allocator forever -- see the note on DEFAULT_STALE_HOURS
for why that threshold is deliberately generous rather than tight.
"""
import argparse
import json
import os
import re
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

LOCK_FILE = ".id_alloc.lock"
LEDGER_FILE = "id_reservations.json"
SOURCE = "rebuild_final.py"
LOCK_TIMEOUT_S = 30
LOCK_STALE_S = 120

# How long a reservation stays honoured. Deliberately generous, because the
# two ways of getting this wrong are NOT symmetric:
#   too long  -> a crashed run leaves a hole of unused ids. Harmless: each
#                block holds a million of them and nothing depends on ids
#                being contiguous.
#   too short -> a still-running job's reservation expires UNDERNEATH it, the
#                next caller is handed the same numbers, and we get duplicate
#                ids -- the exact data corruption this file exists to prevent.
# So it must comfortably exceed the longest realistic run (the 7-city sweep
# can take hours). A long job should also call --renew periodically, which
# refreshes its own entry and makes the threshold irrelevant for that run.
DEFAULT_STALE_HOURS = 24.0


def acquire_lock():
    """Atomic create-or-fail; retries until timeout, breaks a stale lock."""
    deadline = time.time() + LOCK_TIMEOUT_S
    while True:
        try:
            fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
            return
        except FileExistsError:
            try:
                age = time.time() - os.path.getmtime(LOCK_FILE)
                if age > LOCK_STALE_S:
                    os.unlink(LOCK_FILE)   # previous holder died
                    continue
            except FileNotFoundError:
                continue                    # holder released between our checks
            if time.time() > deadline:
                sys.exit("could not acquire %s within %ds -- another allocation "
                         "is in progress; retry shortly" % (LOCK_FILE, LOCK_TIMEOUT_S))
            time.sleep(0.3)


def release_lock():
    try:
        os.unlink(LOCK_FILE)
    except FileNotFoundError:
        pass


def load_ledger():
    try:
        return json.load(open(LEDGER_FILE, encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return {"reservations": []}


def save_ledger(led):
    json.dump(led, open(LEDGER_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def max_in_file(block):
    """Highest id already written into the source, within this block."""
    try:
        src = open(SOURCE, encoding="utf-8").read()
    except FileNotFoundError:
        sys.exit("%s not found -- run from the project directory" % SOURCE)
    ids = [int(x) for x in re.findall(r"^L\((\d+),", src, re.M)]
    in_block = [i for i in ids if block <= i < block + 1000000]
    return max(in_block) if in_block else block - 1


def cmd_allocate(args):
    acquire_lock()
    try:
        led = load_ledger()
        now = time.time()
        live = [r for r in led["reservations"]
                if now - r["ts"] < args.stale_hours * 3600]
        dropped = len(led["reservations"]) - len(live)
        if dropped:
            print("note: ignoring %d reservation(s) older than %.1fh" % (dropped, args.stale_hours))

        floor = max_in_file(args.block)
        for r in live:
            if r["block"] == args.block:
                floor = max(floor, r["last"])

        first = floor + 1
        last = first + args.count - 1
        live.append({"block": args.block, "first": first, "last": last,
                     "owner": args.owner, "ts": now, "pid": os.getpid()})
        led["reservations"] = live
        save_ledger(led)
    finally:
        release_lock()

    print("reserved %d id(s) in block %d for %s" % (args.count, args.block, args.owner))
    print("use exactly these ids and no others: %d..%d" % (first, last))
    print("FIRST=%d LAST=%d" % (first, last))


def cmd_renew(args):
    """Refresh a reservation's timestamp so a long-running job cannot have its
    own ids expire underneath it and be handed to someone else."""
    m = re.match(r"^(\d+)-(\d+)$", args.renew)
    if not m:
        sys.exit("--renew expects FIRST-LAST, e.g. 1000042-1000053")
    first, last = int(m.group(1)), int(m.group(2))
    acquire_lock()
    try:
        led = load_ledger()
        found = False
        for r in led["reservations"]:
            if r["first"] == first and r["last"] == last:
                r["ts"] = time.time()
                found = True
        save_ledger(led)
    finally:
        release_lock()
    if not found:
        sys.exit("no reservation %d..%d to renew -- it may already have expired "
                 "or been released; do NOT keep using those ids, allocate again"
                 % (first, last))
    print("renewed reservation %d..%d" % (first, last))


def cmd_release(args):
    m = re.match(r"^(\d+)-(\d+)$", args.release)
    if not m:
        sys.exit("--release expects FIRST-LAST, e.g. 1000042-1000053")
    first, last = int(m.group(1)), int(m.group(2))
    acquire_lock()
    try:
        led = load_ledger()
        before = len(led["reservations"])
        led["reservations"] = [r for r in led["reservations"]
                               if not (r["first"] == first and r["last"] == last)]
        save_ledger(led)
    finally:
        release_lock()
    print("released %d reservation(s) for %d..%d" % (before - len(led["reservations"]), first, last))


def cmd_status(_args):
    led = load_ledger()
    now = time.time()
    if not led["reservations"]:
        print("no outstanding reservations")
    for r in led["reservations"]:
        print("block %d | %d..%d | owner=%s | age=%.1fh"
              % (r["block"], r["first"], r["last"], r.get("owner", "?"),
                 (now - r["ts"]) / 3600))
    for block, name in ((1000000, "HCMC check"), (2000000, "7-city check")):
        print("max written in block %d (%s): %d" % (block, name, max_in_file(block)))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--block", type=int, help="1000000 (HCMC) or 2000000 (7-city)")
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--owner", default="unnamed")
    p.add_argument("--release", help="FIRST-LAST, after the ids are written to " + SOURCE)
    p.add_argument("--renew", help="FIRST-LAST, refresh a long-running job's reservation")
    p.add_argument("--status", action="store_true")
    p.add_argument("--stale-hours", type=float, default=DEFAULT_STALE_HOURS)
    args = p.parse_args()

    if args.status:
        cmd_status(args)
    elif args.renew:
        cmd_renew(args)
    elif args.release:
        cmd_release(args)
    elif args.block:
        if args.block not in (1000000, 2000000):
            sys.exit("--block must be 1000000 (HCMC) or 2000000 (7-city)")
        cmd_allocate(args)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
