# -*- coding: utf-8 -*-
"""
The one place that knows how to read the built site's data back out.

rebuild_final.py bakes every listing into vietnam-rent-finder.html as
`var DATA = {...};`. Eight maintenance scripts used to carry their own copy
of the regex that digs it back out, most of them calling .group(1) on the
match without checking it -- so when another session's rebuild happened
to be mid-write, they died with a bare AttributeError halfway through the
pipeline (2 Sep 2026 audit). rebuild_final.py now writes the page
atomically, and every reader goes through load_data() below, which says
what is wrong instead of crashing on None.

    from site_data import load_data
    data = load_data()            # dict with LISTINGS, CITIES, SOURCES, POIS, ...
    listings = data["LISTINGS"]
"""
import json
import re

BUILT_HTML = "vietnam-rent-finder.html"   # index.html is a byte-identical copy
_DATA_RE = re.compile(r"var DATA = (\{.*?\});\s*\n", re.S)


def load_data(path=BUILT_HTML):
    try:
        html = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        raise SystemExit("%s not found -- run `python rebuild_final.py` first (from the project directory)" % path)
    m = _DATA_RE.search(html)
    if not m:
        raise SystemExit("%s has no `var DATA = {...};` block -- the build is incomplete or another "
                         "session is rewriting the file right now; run rebuild_final.py again" % path)
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        raise SystemExit("`var DATA` in %s is not valid JSON (%s) -- rebuild the site" % (path, e))


def load_listings(path=BUILT_HTML):
    return load_data(path)["LISTINGS"]
