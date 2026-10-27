# -*- coding: utf-8 -*-
"""Минимальные тесты listing_lock.py: хранение строк, заведение и снятие партий,
блокировка записи. Все тесты -- во временном каталоге (фикстура ll)."""
import datetime
import json
import os
import time

import pytest


def row(i, city="nha-trang", source="chotot", seq=None, **extra):
    r = {"id": i, "city": city, "district": "vh", "type": "Квартира", "price": 1000000,
         "area": 30, "desc": "d", "url": "https://example.com/%d.htm" % i,
         "posted": "сегодня", "daysAgo": 0, "source": source}
    if seq is not None:
        r["seq"] = seq
    r.update(extra)
    return r


def batch_src(*ids, url="https://example.com/new/%d.htm", days_ago=0, source="chotot", extra=""):
    return "\n".join(
        'L(%d,"nha-trang","vh","Квартира",5000000,40,\n  "desc %d",\n  "%s","%s",%d,source="%s"%s),'
        % (i, i, url % i if "%d" in url else url, "сегодня" if days_ago == 0 else "вчера",
           days_ago, source, extra)
        for i in ids)


# --- хранение -----------------------------------------------------------------

def test_save_and_load_roundtrip_in_site_order(ll):
    rows = [row(3, seq=1), row(1, seq=2), row(2, city="da-nang", source="telegram", seq=0)]
    ll.save_rows(rows)
    assert os.path.exists("listings/chotot/nha-trang.jsonl")
    assert os.path.exists("listings/telegram/da-nang.jsonl")
    assert [r["id"] for r in ll.load_rows()] == [2, 3, 1]      # (seq, id)


def test_row_without_source_goes_to_chotot(ll):
    r = row(1)
    del r["source"]
    assert ll.row_path(r) == os.path.join("listings", "chotot", "nha-trang.jsonl")


def test_save_rows_refuses_duplicate_ids_and_writes_nothing(ll):
    with pytest.raises(SystemExit):
        ll.save_rows([row(1), row(1)])
    assert ll.load_rows() == []


def test_save_rows_deletes_emptied_file_and_keeps_unchanged_one(ll):
    ll.save_rows([row(1), row(2, city="da-nang")])
    keep = "listings/chotot/nha-trang.jsonl"
    before = os.stat(keep).st_mtime_ns
    time.sleep(0.01)
    ll.save_rows([row(1)])
    assert not os.path.exists("listings/chotot/da-nang.jsonl")
    assert os.stat(keep).st_mtime_ns == before                 # не переписан


def test_files_are_lf_one_json_object_per_line(ll):
    ll.save_rows([row(1, desc="Нячанг, đường Trần Phú")])
    raw = open("listings/chotot/nha-trang.jsonl", "rb").read()
    assert b"\r\n" not in raw and raw.endswith(b"\n")
    assert "Trần Phú" in raw.decode("utf-8")                    # ensure_ascii=False
    assert json.loads(raw)["id"] == 1


def test_load_rows_rejects_broken_line(ll):
    os.makedirs("listings/chotot")
    with open("listings/chotot/nha-trang.jsonl", "w", encoding="utf-8") as f:
        f.write(json.dumps(row(1)) + "\n{not json\n")
    with pytest.raises(SystemExit):
        ll.load_rows()


def test_load_page_rows_strips_store_fields_and_refuses_empty(ll):
    with pytest.raises(SystemExit):
        ll.load_page_rows()
    ll.save_rows([row(1, seq=0, postedOn=datetime.date.today().isoformat())])
    page = ll.load_page_rows()
    assert "seq" not in page[0] and "postedOn" not in page[0]


# --- возраст строк ---------------------------------------------------------------

def test_row_anchor_prefers_posted_dates_and_ignores_future_or_bad_dates(ll):
    today = datetime.date(2026, 10, 27)
    r = row(5, postedOn="2026-10-20")
    assert ll.row_anchor(r, {"5": "2026-10-25"}, today) == datetime.date(2026, 10, 25)
    assert ll.row_anchor(r, {}, today) == datetime.date(2026, 10, 20)
    assert ll.row_anchor(row(5, postedOn="2026-11-01"), {}, today) is None
    assert ll.row_anchor(row(5, postedOn="27.10.2026"), {}, today) is None
    assert ll.row_anchor(row(5), {}, today) is None


def test_with_current_age_recomputes_label(ll):
    today = datetime.date(2026, 10, 27)
    with open(ll.POSTED_DATES_FILE, "w", encoding="utf-8") as f:
        json.dump({"1": "2026-10-22"}, f)
    rows = ll.with_current_age([row(1), row(2), row(3, postedOn="2026-10-26")], today=today)
    assert (rows[0]["daysAgo"], rows[0]["posted"]) == (5, "5 дней назад")
    assert (rows[1]["daysAgo"], rows[1]["posted"]) == (0, "сегодня")   # якоря нет -- как было
    assert (rows[2]["daysAgo"], rows[2]["posted"]) == (1, "вчера")


# --- партии -----------------------------------------------------------------------

def test_insert_listings_appends_with_seq_and_postedOn(ll):
    ll.save_rows([row(1, seq=7)])
    assert ll.insert_listings(batch_src(10, 11, days_ago=1), [10, 11], owner="test") == 2
    rows = {r["id"]: r for r in ll.load_rows()}
    assert (rows[10]["seq"], rows[11]["seq"]) == (8, 9)
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    assert rows[10]["postedOn"] == yesterday
    assert not os.path.exists(ll.LOCK_FILE)


def test_insert_listings_keeps_explicit_postedOn(ll):
    ll.insert_listings(batch_src(10, extra=',postedOn="2026-10-01"'), [10])
    assert ll.load_rows()[0]["postedOn"] == "2026-10-01"


def test_insert_listings_refuses_rerun_of_same_batch(ll):
    ll.insert_listings(batch_src(10), [10])
    with pytest.raises(SystemExit):
        ll.insert_listings(batch_src(10), [10])
    assert [r["id"] for r in ll.load_rows()] == [10]


def test_insert_listings_refuses_known_url_even_with_query_string(ll):
    ll.save_rows([row(1, url="https://example.com/ad/5.htm")])
    with pytest.raises(SystemExit):
        ll.insert_listings(batch_src(10, url="https://example.com/ad/5.htm?utm=x"), [10])
    assert [r["id"] for r in ll.load_rows()] == [1]


def test_insert_listings_allows_shared_url_for_telegram(ll):
    ll.save_rows([row(1, source="telegram", url="https://t.me/channel")])
    ll.insert_listings(batch_src(10, url="https://t.me/channel", source="telegram"), [10])
    assert sorted(r["id"] for r in ll.load_rows()) == [1, 10]


def test_insert_listings_refuses_wrong_declared_ids(ll):
    with pytest.raises(SystemExit):
        ll.insert_listings(batch_src(10, 11), [10, 12])
    assert ll.load_rows() == []


@pytest.mark.parametrize("src", [
    'print("hi")',                                                      # не L(...)
    'L(10,"nha-trang","vh","Квартира",N+"/x",40,"d","u","сегодня",0),',  # не литерал
])
def test_rows_from_src_accepts_only_literal_L_rows(ll, src):
    with pytest.raises(SystemExit):
        ll.rows_from_src(src)


def test_listing_ids_counts_batch_rows(ll):
    assert ll.listing_ids(batch_src(3, 4, 5)) == [3, 4, 5]


def test_remove_listings(ll, capsys):
    ll.save_rows([row(1), row(2), row(3)])
    assert ll.remove_listings([2, 99, "3"], owner="test") == [2, 3]
    assert [r["id"] for r in ll.load_rows()] == [1]
    assert "99" in capsys.readouterr().out
    assert ll.remove_listings([]) == []


# --- блокировка -------------------------------------------------------------------

def test_lock_is_released_even_on_error(ll):
    with pytest.raises(RuntimeError):
        with ll.listings_write_lock("t"):
            assert os.path.exists(ll.LOCK_FILE)
            raise RuntimeError
    assert not os.path.exists(ll.LOCK_FILE)


def test_live_lock_times_out(ll, monkeypatch):
    monkeypatch.setattr(ll, "TIMEOUT_S", 0.3)
    open(ll.LOCK_FILE, "w").write("123 other session")
    with pytest.raises(SystemExit) as ex:
        ll.acquire("me")
    assert "other session" in str(ex.value)
    assert os.path.exists(ll.LOCK_FILE)                         # чужой замок не тронут


def test_stale_lock_is_taken_over(ll):
    open(ll.LOCK_FILE, "w").write("1 dead session")
    old = time.time() - ll.STALE_S - 60
    os.utime(ll.LOCK_FILE, (old, old))
    ll.acquire("me")
    try:
        assert open(ll.LOCK_FILE, encoding="utf-8").read().endswith(" me")
    finally:
        ll.release()
    assert not [f for f in os.listdir(".") if ".stale." in f]
