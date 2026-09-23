# -*- coding: utf-8 -*-
"""
Ежедневная подборка лучших свежих объявлений одного города -- текст поста для
публичного канала города.

ЗАЧЕМ. Хабы в Телеграме -- закрытые группы: 21.09.2026 в них 4 и 2 участника, и
с 7.09 туда ничего не уходило. Ленту в 900 объявлений в сутки никто читать не
станет; читают короткую подборку «что появилось выгодного», и из неё идут на сайт
и к боту. Первый город -- Нячанг (решение владельца 21.09.2026): там больше всего
русскоязычных, а у нас ~50 новых объявлений в сутки из четырёх источников.

КАК ВЫБИРАЕТСЯ. Жильё (квартира, студия, дом, комната) не старше --days дней, с
ценой, площадью и не меньше чем тремя настоящими фотографиями. Выгодность -- цена
за м² против медианы того же типа по городу за неделю; подозрительно дешёвые
(меньше --floor медианы -- обычно опечатка в цене или площади) не берутся. Не больше
--per-district объявлений из одного района, чтобы подборка не состояла из одной улицы.

ЧТО НЕ ДЕЛАЕТ. Не отправляет ничего: публикация в публичный канал необратима и
идёт только после того, как владелец посмотрел подборку. Пишет текст поста (HTML
для Телеграма) в stdout и в _digest_<город>.html.

    python city_digest.py --city nha-trang
    python city_digest.py --city nha-trang --top 8 --days 1
"""
import argparse
import html
import re
import statistics
import sys

sys.stdout.reconfigure(encoding="utf-8")

from listing_lock import load_rows, template_cities, with_current_age

SITE_URL = "https://tottorisun.github.io/RentSearcherViet/"
BOT = "@RentVietnamBot"
RESIDENTIAL = ("Квартира", "Студия", "Дом", "Комната")
TYPE_EMOJI = {"Квартира": "🏢", "Студия": "🏙", "Дом": "🏠", "Комната": "🛏"}
MESSAGE_LIMIT = 4096        # предел текста одного сообщения Телеграма
BEDROOMS = re.compile(r"(\d+)-спальн")


def esc(s):
    return html.escape(str(s), quote=False)


def real_photos(r):
    """Фотографии строки: ссылки на источник и снимки, которые лежат на самом
    сайте (assets/fb_photos/... у строк из групп Facebook -- ссылки Facebook
    живут четыре дня, и фото хранятся у нас)."""
    return [u for u in ((r.get("details") or {}).get("photos") or [])
            if isinstance(u, str) and u.startswith(("http://", "https://", "assets/"))]


def mln(v):
    m = v / 1000000
    return (str(int(m)) if m == int(m) else ("%.1f" % m)).replace(".", ",")


def clip(text, limit):
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    cut = text[:limit]
    space = cut.rfind(" ")
    if space > limit * 0.6:
        cut = cut[:space]
    return cut.rstrip(" ,.;:—-") + "…"


def plural(n, one, few, many):
    if n % 10 == 1 and n % 100 != 11:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


def bedrooms(r):
    m = BEDROOMS.search(r.get("desc") or "")
    return int(m.group(1)) if m else None


def pick(rows, city, days, top, per_district, floor, max_houses):
    """(выбранные, число свежих, медианы). Каждая выбранная строка получает _ratio."""
    mine = [r for r in rows if r["city"] == city and r["type"] in RESIDENTIAL
            and (r.get("cur") or "VND") == "VND"]
    ppm = {}
    for r in mine:
        if r.get("price") and r.get("area") and 15 <= r["area"] <= 500:
            ppm.setdefault(r["type"], []).append(r["price"] / r["area"])
    everyone = [v for vs in ppm.values() for v in vs]
    if not everyone:
        return [], 0, {}
    med_all = statistics.median(everyone)
    # Медиана по типу -- если у типа хватает строк; иначе по всему жилью города.
    medians = {t: (statistics.median(vs) if len(vs) >= 8 else med_all) for t, vs in ppm.items()}
    fresh = [r for r in mine if isinstance(r.get("daysAgo"), int) and r["daysAgo"] <= days]
    cands, seen = [], set()
    for r in sorted(fresh, key=lambda r: (r["daysAgo"], -r["id"])):
        if not (r.get("price") and r.get("area") and 15 <= r["area"] <= 500):
            continue
        photos = real_photos(r)
        if len(photos) < 3:
            continue
        # Одно объявление, выложенное дважды (разные площадки, та же первая фотография
        # или та же ссылка), в подборке один раз.
        keys = {r["url"].split("?")[0], photos[0].rsplit("/", 1)[-1]}
        if keys & seen:
            continue
        seen |= keys
        ratio = (r["price"] / r["area"]) / medians.get(r["type"], med_all)
        if ratio < floor:
            continue
        cands.append(dict(r, _ratio=ratio))
    cands.sort(key=lambda r: (r["_ratio"], r["daysAgo"], -r["id"]))
    # Дома -- не больше max_houses: у дома в площадь часто входит участок, и цена за
    # м² у него ниже, чем у квартиры того же уровня; без предела подборка Нячанга
    # 21.09 вышла из пяти домов на восемь мест.
    out, per, houses = [], {}, 0
    for r in cands:
        if per.get(r["district"], 0) >= per_district:
            continue
        if r["type"] == "Дом" and houses >= max_houses:
            continue
        houses += r["type"] == "Дом"
        per[r["district"]] = per.get(r["district"], 0) + 1
        out.append(r)
        if len(out) >= top:
            break
    return out, len(fresh), medians


def render(city, city_info, picked, n_fresh, n_total, days):
    names = {d["key"]: d["name"] for d in city_info["districts"]}
    when = "за сутки" if days <= 1 else "за %d дня" % days if days < 5 else "за %d дней" % days
    lines = ["🏝 <b>%s: %d выгодных из %d новых объявлений %s</b>"
             % (esc(city_info["name"]), len(picked), n_fresh, when),
             "<i>Отобраны по цене за м² — ниже обычной для того же типа жилья в городе.</i>", ""]
    for i, r in enumerate(picked, 1):
        # Процент -- к медиане цены за м² того же типа по городу. Больше 60% --
        # скорее особенность строки (участок, общая площадь), чем находка: не кричим.
        cheaper = round((1 - r["_ratio"]) * 100)
        br = bedrooms(r)
        rooms = (" · %d сп." % br) if br else ""
        lines.append("%d. %s <b>%s</b>%s · %s м² · <b>%s млн ₫/мес</b>"
                     % (i, TYPE_EMOJI.get(r["type"], "🏠"), esc(r["type"]), rooms, r["area"], mln(r["price"])))
        # Описание -- только если в нём есть что-то сверх типа, площади и района
        # (у строк batdongsan оно часто ровно «Квартира, 73 м², Tây Nha Trang.»).
        extra = r["desc"].split("—", 1)[1].strip() if "—" in r["desc"] else ""
        place = names.get(r["district"], r["district"])
        lines.append("📍 %s%s" % (esc(place), (" · " + esc(clip(extra, 90))) if extra else ""))
        if 5 <= cheaper <= 60:
            lines.append("💰 цена за м² на %d%% ниже, чем обычно по городу" % cheaper)
        lines.append('<a href="%s">Открыть объявление →</a>' % html.escape(r["url"], quote=True))
        lines.append("")
    lines.append('🗺 Все %d %s города на карте: <a href="%s%s.html">%s</a>'
                 % (n_total, plural(n_total, "объявление", "объявления", "объявлений"),
                    SITE_URL, city, esc(city_info["name"])))
    lines.append("🔔 Свои фильтры и оповещения о новых — %s" % BOT)
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--city", default="nha-trang")
    ap.add_argument("--days", type=int, default=1, help="не старше стольких дней")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--per-district", type=int, default=2)
    ap.add_argument("--max-houses", type=int, default=3)
    ap.add_argument("--floor", type=float, default=0.35,
                    help="дешевле этой доли медианы за м² -- скорее ошибка, чем находка")
    a = ap.parse_args()
    cities = template_cities()
    if a.city not in cities:
        sys.exit("нет такого города: %s" % a.city)
    rows = with_current_age(load_rows())
    picked, n_fresh, _med = pick(rows, a.city, a.days, a.top, a.per_district, a.floor, a.max_houses)
    if not picked:
        sys.exit("для %s не нашлось ни одного подходящего свежего объявления -- подборки нет" % a.city)
    n_total = sum(1 for r in rows if r["city"] == a.city)
    text = render(a.city, cities[a.city], picked, n_fresh, n_total, a.days)
    while len(text) > MESSAGE_LIMIT and len(picked) > 3:
        picked = picked[:-1]
        text = render(a.city, cities[a.city], picked, n_fresh, n_total, a.days)
    out = "_digest_%s.html" % a.city
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print("\n-- %d символов из %d; записано в %s; ничего не отправлено" % (len(text), MESSAGE_LIMIT, out))


if __name__ == "__main__":
    main()
