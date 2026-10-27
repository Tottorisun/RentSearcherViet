# -*- coding: utf-8 -*-
"""
Общие фикстуры. Ни один тест не пишет в рабочий каталог проекта: listing_lock и
rebuild_final.py работают с путями относительно текущего каталога (listings/,
.listings_write.lock, posted_dates.json, выходные *.html), поэтому каждый тест
переходит во временный каталог, а шаблон rebuild_final.py читается из корня
репозитория по абсолютному пути.
"""
import os
import shutil
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import listing_lock  # noqa: E402


@pytest.fixture
def ll(tmp_path, monkeypatch):
    """listing_lock, переведённый во временный каталог с пустым listings/."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(listing_lock, "SOURCE", os.path.join(ROOT, "rebuild_final.py"))
    (tmp_path / listing_lock.DATA_DIR).mkdir()
    return listing_lock


@pytest.fixture(scope="session")
def first_district():
    """(город, район), который точно есть в CITIES шаблона."""
    old = listing_lock.SOURCE
    listing_lock.SOURCE = os.path.join(ROOT, "rebuild_final.py")
    try:
        cities = listing_lock.template_cities()
    finally:
        listing_lock.SOURCE = old
    city = next(iter(cities))
    return city, cities[city]["districts"][0]["key"]


# Что rebuild_final.py читает при сборке. leaflet_*.json и posted_dates.json
# необязательны (сборка без них идёт), остальное -- обязательно.
BUILD_INPUTS = ["rebuild_final.py", "listing_lock.py", "maps_data.json", "nt_realtor_map.json",
                "rates.json", "vendor"]


@pytest.fixture
def build_dir(tmp_path, monkeypatch):
    """Временная копия ровно того, что нужно сборке, -- без listings/."""
    for name in BUILD_INPUTS:
        src = os.path.join(ROOT, name)
        if os.path.isdir(src):
            shutil.copytree(src, tmp_path / name)
        else:
            shutil.copy(src, tmp_path / name)
    monkeypatch.chdir(tmp_path)
    return tmp_path
