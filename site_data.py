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

BUILT_HTML = "vietnam-rent-finder.html"   # the complete page; the per-city pages hold slices of it
_DATA_RE = re.compile(r"var DATA = (\{.*?\});\s*\n", re.S)

# Photo URLs are stored compactly in the built pages: 5 448 of the 5 771 Chợ
# Tốt URLs are exactly "https://cdn.chotot.com/<token>/preset:view/plain/<tail>",
# i.e. 42 bytes of identical boilerplate each, which the page would otherwise
# carry ~9 000 times. rebuild_final.py writes them as "~<token>/<tail>" and
# the page expands them in JS; this does the same for every Python consumer,
# so nothing outside those two places ever sees the short form.
PHOTO_PREFIXES = {
    "~": ("https://cdn.chotot.com/", "/preset:view/plain/"),
}


def expand_photo(u):
    p = PHOTO_PREFIXES.get(u[:1])
    if not p:
        return u
    head, mid = p
    token, _, tail = u[1:].partition("/")
    return head + token + mid + tail


def _expand_all(data):
    for l in data.get("LISTINGS", []):
        d = l.get("details")
        if d and d.get("photos"):
            d["photos"] = [expand_photo(u) for u in d["photos"]]
    return data


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
        return _expand_all(json.loads(m.group(1)))
    except json.JSONDecodeError as e:
        raise SystemExit("`var DATA` in %s is not valid JSON (%s) -- rebuild the site" % (path, e))


def load_listings(path=BUILT_HTML):
    return load_data(path)["LISTINGS"]
