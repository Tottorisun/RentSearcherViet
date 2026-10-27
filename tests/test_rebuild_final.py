# -*- coding: utf-8 -*-
"""Минимальные тесты rebuild_final.py.

rebuild_final.py -- скрипт без main(): сборка идёт при импорте и пишет файлы в
текущий каталог. Поэтому чистые функции шаблона берутся так же, как их берут
сборщики (listing_lock.template_function), а сама сборка запускается отдельным
процессом во временной копии (фикстура build_dir)."""
import json
import os
import shutil
import subprocess
import sys

import pytest

from conftest import ROOT

import listing_lock


@pytest.fixture(scope="module")
def tpl():
    old = listing_lock.SOURCE
    listing_lock.SOURCE = os.path.join(ROOT, "rebuild_final.py")
    try:
        yield listing_lock.template_function
    finally:
        listing_lock.SOURCE = old


# --- чистые функции шаблона --------------------------------------------------------

@pytest.mark.parametrize("n, label", [
    (-1, "сегодня"), (0, "сегодня"), (1, "вчера"), (2, "2 дня назад"), (5, "5 дней назад"),
    (11, "11 дней назад"), (21, "21 день назад"), (22, "22 дня назад"), (112, "112 дней назад"),
])
def test_ru_days_label(tpl, n, label):
    assert tpl("_ru_days_label")(n) == label


def test_L_builds_page_row(tpl):
    L = tpl("L")
    r = L(1, "nha-trang", "vh", "Квартира", 5000000, 40, "d", "u", "сегодня", 0)
    assert r == {"id": 1, "city": "nha-trang", "district": "vh", "type": "Квартира", "price": 5000000,
                 "area": 40, "desc": "d", "url": "u", "posted": "сегодня", "daysAgo": 0, "source": "chotot"}
    r = L(2, "cebu", "x", "Студия", 20000, 25, "d", "u", "вчера", 1, source="dotproperty",
          descEn="e", details={"photos": ["p"]}, cur="PHP", postedOn="2026-10-01")
    assert (r["cur"], r["descEn"], r["details"]) == ("PHP", "e", {"photos": ["p"]})
    assert "postedOn" not in r                                   # только для хранения


# --- сборка целиком ----------------------------------------------------------------

def page_row(i, city, district_key, **over):
    r = {"id": i, "city": city, "district": district_key, "type": "Квартира", "price": 6000000 + i,
         "area": 40, "desc": "Тестовая квартира %d" % i, "descEn": "Test apartment %d" % i,
         "url": "https://www.nhatot.com/test/%d.htm" % i, "posted": "сегодня", "daysAgo": 0,
         "source": "chotot", "seq": i}
    r.update(over)
    return r


def write_rows(base, rows):
    for r in rows:
        d = os.path.join(base, "listings", r.get("source") or "chotot")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "%s.jsonl" % r["city"]), "a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def build(cwd):
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, "rebuild_final.py"], cwd=str(cwd), env=env,
                          capture_output=True, text=True, timeout=300)


def test_build_writes_site(build_dir, first_district):
    city, district = first_district
    write_rows(build_dir, [page_row(1, city, district), page_row(2, city, district, daysAgo=3,
                                                                  posted="3 дня назад")])
    p = build(build_dir)
    assert p.returncode == 0, p.stdout + p.stderr
    for name in ["vietnam-rent-finder.html", "vietnam-rent-finder-en.html", "index.html", "en.html",
                 "%s.html" % city, "assets/app.js", "assets/app.css", "robots.txt", "sitemap.xml"]:
        assert (build_dir / name).stat().st_size > 0, name
    page = (build_dir / "vietnam-rent-finder.html").read_text(encoding="utf-8")
    assert "Тестовая квартира 1" in page and "Test apartment 2" in page
    assert "__DATA_JSON__" not in page and "__TODAY_DATE__" not in page
    assert "Listing check: OK (2 listings" in p.stdout


@pytest.mark.parametrize("bad, message", [
    ({"district": "no-such-district"}, "is not defined for city"),
    ({"descEn": ""}, "no descEn"),
    # Незнакомые source и cur сборка тоже не пропускает, но падает раньше
    # check_listings -- KeyError в _to_base и ValueError в _SOURCES_BY_CITY, без
    # понятного сообщения (см. docs/repo-analysis-2026-10.md). Тест закрепляет
    # главное: страница не пишется.
    ({"source": "no-such-source"}, ""),
    ({"cur": "XXX"}, ""),
    ({"posted": "вчера"}, "does not match daysAgo"),
    ({"type": "2-спальная квартира"}, ""),                        # check_listing_types
])
def test_build_refuses_bad_row_and_writes_nothing(build_dir, first_district, bad, message):
    city, district = first_district
    rows = [page_row(1, city, district), page_row(2, city, district, **bad)]
    if bad.get("source"):
        rows[1]["url"] += "?other"
    write_rows(build_dir, rows)
    p = build(build_dir)
    assert p.returncode != 0
    assert message in p.stdout + p.stderr
    assert not (build_dir / "vietnam-rent-finder.html").exists()


def test_build_refuses_duplicate_id_across_files(build_dir, first_district):
    city, district = first_district
    write_rows(build_dir, [page_row(1, city, district),
                           page_row(1, city, district, source="telegram", url="https://t.me/c/1")])
    p = build(build_dir)
    assert p.returncode != 0 and "duplicate id 1" in p.stdout + p.stderr


def test_build_refuses_empty_listings(build_dir):
    os.makedirs(build_dir / "listings")
    p = build(build_dir)
    assert p.returncode != 0
    assert not (build_dir / "vietnam-rent-finder.html").exists()


def test_build_on_repository_data(build_dir):
    """Сборка на настоящих строках репозитория -- то же, что делает хук и прогон,
    но во временной копии: рабочие файлы проекта не меняются."""
    shutil.copytree(os.path.join(ROOT, "listings"), build_dir / "listings")
    for name in ["posted_dates.json", "leaflet_listing_latlon.json", "leaflet_ward_boundaries.json"]:
        if os.path.exists(os.path.join(ROOT, name)):
            shutil.copy(os.path.join(ROOT, name), build_dir / name)
    p = build(build_dir)
    assert p.returncode == 0, (p.stdout + p.stderr)[-3000:]
    assert "Listing check: OK" in p.stdout
