# legacy/

Scripts nothing in the live pipeline calls any more (moved here 2 Sep 2026
after the project audit; history preserved via `git mv`). Kept because two of
them produced artifacts that are still read at build time:

- `build_maps.py`, `build_maps2.py`, `build_maps_hcmc.py` — generated the
  early SVG map data (`maps_data.json`, still loaded by `rebuild_final.py`).
  Superseded by `build_pins_step1_projections.py` for every city that has real
  OSM ward polygons.
- `build_nt_realtor_map.py` — generated `nt_realtor_map.json` (the Nha Trang
  "mosaic" grid that `build_pins_nhatrang.py` reads). Its `W` path points at a
  dead scratchpad; fix that before re-running.
- `build_pdf.py`, `build_pdf2.py`, `render_pdf.py`, `render_pdf2.py`,
  `render_pdf3.py` — a PDF export of the listings (needs `reportlab`, not
  stdlib). The `render_*` files `exec()` the `build_*` ones by relative path,
  so run them from inside this directory.
- `extract.py`, `parse_listings.py` — one-off parsers for early `*_out.txt`
  dumps.
- `fetch_today_details.py` — hardcoded ids, needs `requests`.
- `integrate_batch5.py` — an early batch inserter that bypassed
  `allocate_ids.py` and wrote `rebuild_final.py` without a lock. Do NOT use as
  a template; use `new_listings_template.py` in the project root.

Run nothing here as part of a daily check.
