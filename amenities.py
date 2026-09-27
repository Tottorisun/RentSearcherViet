# -*- coding: utf-8 -*-
"""
Удобства и этаж из текста объявления -- одним разбором для всех источников.

ЗАЧЕМ. До 27.09.2026 сборщик Chợ Tốt брал из текста до четырёх удобств и только
в описание («— кондиционер, балкон.»): по ним нельзя было отфильтровать, кухню и
этаж он не искал вовсе, а «стиральная машина» не отличала свою от общей. Владелец
подбирал квартиру «со своей стиральной машиной, кухней и не ниже 3-го этажа» -- и
это пришлось проверять по полным текстам 188 объявлений руками.

ЧТО ВОЗВРАЩАЕТ. extract(text) -> {"am": [...коды...], "fl": этаж или None, "flHigh": 1}
  w     своя стиральная машина          ws    стиральная машина общая или «в части квартир»
  k     кухня (можно готовить)          b     балкон
  win   окно                            lift  лифт
  pool  бассейн                         gym   спортзал
  free  свободный вход                  pet   можно с животными
  fl    этаж по-русски: 1 -- первый (у земли). «tầng trệt» -- 1; «lầu N» -- N+1
        (на юге Вьетнама lầu считают над первым этажом); «tầng N», «N floor» -- N.
  flHigh  «tầng cao», «high floor» -- высокий этаж без номера.

Ничего не выдумываем: нет в тексте -- нет кода. Отсутствие кода значит «в
объявлении не сказано», а не «нет». Слова ищутся в тексте без диакритики.
"""
import re
import unicodedata

_STYLED = re.compile("[\U0001D400-\U0001D7FF！-～]")


def fold(s):
    """Без диакритики, в нижнем регистре; «математические» буквы -- обычные."""
    s = _STYLED.sub(lambda m: unicodedata.normalize("NFKC", m.group(0)), s or "")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("đ", "d").replace("Đ", "D").lower()


WASHER = re.compile(r"may giat|washing machine|\bwasher\b|стиральн")
# «máy giặt chung», «dùng chung máy giặt», «một số căn có máy giặt», «máy giặt riêng
# tùy căn» -- не своя или не в каждой квартире.
WASHER_SHARED = re.compile(
    r"may giat (?:dung )?chung|chung may giat|dung chung may giat|khu (?:vuc )?giat|"
    r"mot so can co may giat|may giat rieng tuy can|tuy can co may giat|"
    r"shared washing|shared laundry|communal laundry|laundry room|общая стиральн")
KITCHEN = re.compile(r"\bbep\b|kitchen|nau an|nau nuong|кухн")
NO_COOK = re.compile(r"khong (?:duoc )?nau(?: an)?\b|cam nau|khong bep|no cooking|без кухни|готовить нельзя")
FEATURES = (
    ("b", re.compile(r"ban cong|bancol|bancon\b|balcony|балкон")),
    ("win", re.compile(r"cua so|window|окн[оа]")),
    ("lift", re.compile(r"thang may|elevator|\blift\b|лифт")),
    ("pool", re.compile(r"ho boi|swimming pool|\bpool\b|бассейн")),
    ("gym", re.compile(r"\bgym\b|phong tap|fitness|спортзал")),
    ("free", re.compile(r"gio giac tu do|khong chung chu|tu do gio giac|no curfew|свободный вход")),
    ("pet", re.compile(r"nuoi (?:thu cung|cho|meo|pet)|pet[- ]friendly|pets? allowed|thu cung|можно с животн")),
)
NO_PET = re.compile(r"khong (?:nhan |cho )?(?:nuoi )?(?:thu cung|pet)|no pets?\b|без животн")
# Этаж. «tầng 3 có hồ bơi», «gym tầng 5» -- этаж бассейна, а не квартиры: такие
# совпадения отбрасываются по соседним словам.
FLOOR = re.compile(r"\b(tang|lau)\s*(?:so\s*)?(\d{1,2})\b"
                   r"|\b(\d{1,2})(?:st|nd|rd|th)?\s*floor\b|\bfloor\s*(\d{1,2})\b"
                   r"|(\d{1,2})\s*(?:-?й)?\s*этаж|этаж\s*(\d{1,2})")
FLOOR_NOT_UNIT = re.compile(r"ho boi|pool|gym|cafe|san vuon|khuon vien|san thuong|rooftop|nha xe|ham xe|"
                            r"toa nha \d+ tang|\d+ tang lau|cao \d+ tang|gom \d+ tang|\d+ tang \d|nha \d+ tang")
FLOOR_HIGH = re.compile(r"tang cao|high floor|view cao|высокий этаж")
GROUND = re.compile(r"tang tret|ground floor|первый этаж|1-?й этаж")


def _floor(t):
    for m in FLOOR.finditer(t):
        ctx = t[max(0, m.start() - 30):m.end() + 25]
        if FLOOR_NOT_UNIT.search(ctx):
            continue
        if m.group(1):
            n = int(m.group(2))
            n = n + 1 if m.group(1) == "lau" else n
        else:
            n = int(next(g for g in m.groups()[2:] if g))
        # «tầng 1» -- у земли; нулевых и «90-го» этажей в съёмном жилье не бывает.
        if 1 <= n <= 60:
            return n
    if GROUND.search(t):
        return 1
    return None


def extract(text):
    t = fold(text)
    am = []
    if WASHER.search(t):
        am.append("ws" if WASHER_SHARED.search(t) else "w")
    if KITCHEN.search(t) and not NO_COOK.search(t):
        am.append("k")
    for code, rx in FEATURES:
        if code == "pet" and NO_PET.search(t):
            continue
        if rx.search(t):
            am.append(code)
    out = {"am": am}
    fl = _floor(t)
    if fl is not None:
        out["fl"] = fl
    if FLOOR_HIGH.search(t):
        # 1, а не True: collect_chotot пишет details через json.dumps в L(...), а
        # пакетный файл читается ast.literal_eval -- «true» там не литерал.
        out["flHigh"] = 1
    return out


def attach(details, text):
    """Положить найденное в details строки (на месте, и вернуть его же). Пустое не
    кладём: строка без удобств и этажа весит столько же, сколько раньше."""
    got = extract(text)
    if got["am"]:
        details["am"] = got["am"]
    for k in ("fl", "flHigh"):
        if k in got:
            details[k] = got[k]
    return details


def selftest():
    cases = [
        ("Căn hộ 1PN, máy giặt riêng, bếp riêng thoả sức nấu nướng, thang máy", {"w", "k", "lift"}),
        ("Máy giặt riêng tùy căn, khu vực bếp", {"ws", "k"}),
        ("Máy giặt chung ở sân thượng. Không nấu ăn trong phòng.", {"ws"}),
        ("𝐁𝐀𝐍 𝐂𝐎̂𝐍𝐆 rộng, cửa sổ lớn", {"b", "win"}),
        ("Không nhận thú cưng. Hồ bơi, gym tầng 5.", {"pool", "gym"}),
        ("Pet-friendly studio with a kitchen", {"pet", "k"}),
    ]
    fails = []
    for text, want in cases:
        got = set(extract(text)["am"])
        if got != want:
            fails.append("%r: %s != %s" % (text, sorted(got), sorted(want)))
    floors = [("ban công rộng thoáng lầu 3", 4), ("Căn hộ tầng 12, view sông", 12),
              ("tầng 3 có hồ bơi, yoga", None), ("2BR on the 7th floor", 7), ("Phòng tầng trệt", 1),
              ("Nhà 3 tầng, 4 phòng ngủ", None), ("квартира на 5 этаже", 5)]
    for text, want in floors:
        got = extract(text).get("fl")
        if got != want:
            fails.append("этаж %r: %s != %s" % (text, got, want))
    if not extract("Căn hộ tầng cao view sông").get("flHigh"):
        fails.append("tầng cao")
    if fails:
        raise SystemExit("amenities selftest:\n  " + "\n  ".join(fails))
    print("amenities selftest: ok")


if __name__ == "__main__":
    selftest()
