# -*- coding: utf-8 -*-
"""Ловит перевыложенные объявления: тот же объект под новым идентификатором.

Зачем. Дедупликация в проекте построена на URL и id -- listing_lock не даст
завести дважды одну ссылку. Facebook этого не ловит: продавец снимает
объявление и выкладывает заново, Marketplace выдаёт НОВЫЙ item id, ссылка
другая, а квартира та же. 7 сентября 2026 из семи карточек по Думагете две
оказались уже заведёнными объектами: квартира в Sto. Rosario Heights (у нас
3000182) вышла под id 1081919054566506 с посимвольно тем же текстом, и
студия без адреса -- под 1060869616768429. По ссылке ни одна не отличима.

Как ищет. Сравнивать в лоб нельзя: в базе лежит НАШ пересказ объявления, а не
текст продавца, и лежит он сразу на двух языках (desc и descEn). Жаккар на
объединении обоих полей размывается ровно вдвое и не находит даже точную
перевыкладку -- проверено на паре 3000182 / 1081919054566506.

Первая попытка считала перекрытие по всем словам и дала 19 «совпадений» на 65
строк -- то есть шум. Причина в том, что описания пишем мы, и пишем по шаблону:
«полная меблировка», «месяц авансом и два месяца депозита», «договор от года».
Две совершенно разные студии делят этот канцелярит и набирают 0.69.

Значимо не любое общее слово, а РЕДКОЕ: название дома, улицы, посёлка, ориентир.
Поэтому по каждому городу считается частота слов, и всё, что встречается больше
чем в 12% его объявлений, выбрасывается как местный шаблон -- автоматически, без
ручного списка. Сравниваются только редкие слова, и требуется одновременно:
не меньше трёх общих редких слов и перекрытие по ним >= 0.45. Совпадение цены
снижает планку перекрытия до 0.34, но три общих редких слова нужны всё равно.

Сравнение идёт с каждым языком отдельно (в базе и desc, и descEn), а мерой
служит перекрытие |A∩B| / min(|A|,|B|), а не Жаккар: пересказ короче исходника,
и делить на объединение значило бы наказывать за краткость.

Три режима:
  python check_repost.py --audit                 весь массив, пары внутри города
  python check_repost.py --file new_listings99.py батч перед вставкой
  python check_repost.py --text "..." --city cebu одна строка
"""
import argparse, ast, functools, re, sys, unicodedata

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

THRESHOLD = 0.45
THRESHOLD_SAME_PRICE = 0.34
MIN_RARE_SHARED = 3      # меньше трёх редких слов -- это совпадение канцелярита
COMMON_DF = 0.12         # слово в >12% объявлений города считается местным шаблоном
# Слова, которые есть почти в каждом объявлении и потому ничего не различают.
STOP = set("""
for rent the a an and or of in on at to with is are be this that it its very
month monthly per only available now please pm dm message contact viewing
inquiries send me more details php peso pesos sqm ready near
для сдам аренда в на и с по за от до это что как рядом месяц можно есть
""".split())


@functools.lru_cache(maxsize=None)   # в режиме --audit norm() зовётся O(n^2) раз
def norm(text):
    if not text:
        return set()
    t = unicodedata.normalize("NFKD", str(text)).lower()
    t = re.sub(r"[^\w\s]", " ", t, flags=re.U)      # эмодзи и пунктуация
    t = re.sub(r"\d+", " ", t)                       # цифры: цена и площадь -- не смысл
    return {w for w in t.split() if len(w) > 2 and w not in STOP}


def similarity(a, b):
    """Перекрытие, а не Жаккар: пересказ короче исходника, и делить на
    объединение значило бы наказывать за краткость."""
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


def load_site():
    """Строки сайта как (id, city, price, source, текст-описание)."""
    from site_data import load_listings
    out = []
    for l in load_listings():
        out.append((l["id"], l["city"], l.get("price"), l.get("source", "chotot"),
                    [t for t in (l.get("desc"), l.get("descEn")) if t]))
    return out


def parse_batch(path):
    """Достаёт (id, city, price, source, desc+descEn) из файла партии, не запуская его."""
    src = open(path, encoding="utf-8").read()
    m = re.search(r"NEW_SRC\s*=\s*r?'''(.*?)'''", src, re.S)
    if not m:
        sys.exit("в %s не нашёлся блок NEW_SRC = '''...'''" % path)
    # Блок NEW_SRC -- это последовательность вызовов L(...) через запятую, то
    # есть готовое кортежное выражение. Разбирать его целиком надёжнее, чем
    # считать скобки вручную: ручной счётчик спотыкался о скобки внутри текстов
    # описания и возвращал Tuple вместо Call.
    body = m.group(1).strip().rstrip(",")
    try:
        node = ast.parse("[" + body + "]", mode="eval").body
    except SyntaxError as ex:
        sys.exit("не удалось разобрать NEW_SRC из %s: %s" % (path, ex))
    rows = []
    for call in node.elts:
        if not (isinstance(call, ast.Call) and getattr(call.func, "id", "") == "L"):
            continue
        args = [a.value if isinstance(a, ast.Constant) else None for a in call.args]
        kw = {k.arg: (k.value.value if isinstance(k.value, ast.Constant) else None)
              for k in call.keywords}
        if len(args) < 7:
            continue
        rows.append((args[0], args[1], args[4], kw.get("source", "chotot"),
                     [t for t in (args[6], kw.get("descEn")) if t]))
    return rows


def build_common(rows):
    """Слова-шаблоны считаются отдельно по каждому городу: в Себу шаблон свой,
    в Думагете свой, и общий список на всю страну смазал бы оба."""
    from collections import Counter
    per_city, total = {}, {}
    for _i, city, _p, _s, texts in rows:
        words = set()
        for t in texts:
            words |= norm(t)
        per_city.setdefault(city, Counter()).update(words)
        total[city] = total.get(city, 0) + 1
    return {city: {w for w, n in c.items() if n > max(2, COMMON_DF * total[city])}
            for city, c in per_city.items()}


def best_match(a_texts, b_texts, common):
    """Лучшая пара полей: русское с русским, английское с английским и накрест
    -- кандидат может прийти на одном языке. Возвращает (перекрытие, сколько
    редких слов совпало)."""
    best = (0.0, 0)
    for x in a_texts:
        ax = norm(x) - common
        if not ax:
            continue
        for y in b_texts:
            by = norm(y) - common
            if not by:
                continue
            # Очень короткое описание («подробностей владелец не приводит»)
            # даёт высокое перекрытие на пустом месте: трёх общих слов там
            # хватает, чтобы перекрыть всё, что вообще написано.
            if min(len(ax), len(by)) < 6:
                continue
            shared = len(ax & by)
            r = shared / min(len(ax), len(by))
            if (r, shared) > best:
                best = (r, shared)
    return best


def flagged(r, shared, same_price):
    if shared < MIN_RARE_SHARED:
        return False
    return r >= THRESHOLD or (same_price and r >= THRESHOLD_SAME_PRICE)


def report(candidates, existing, label, common):
    hits = 0
    for cid, ccity, cprice, csrc, ctexts in candidates:
        best = []
        for eid, ecity, eprice, esrc, etexts in existing:
            if eid == cid or ecity != ccity:
                continue
            r, shared = best_match(ctexts, etexts, common.get(ccity, set()))
            if flagged(r, shared, eprice == cprice):
                best.append((r, shared, eid, eprice, esrc))
        for r, shared, eid, eprice, esrc in sorted(best, reverse=True)[:3]:
            same = " ЦЕНА ТА ЖЕ" if eprice == cprice else " (цена %s против %s)" % (cprice, eprice)
            print("  %s ~ %s  перекрытие %.2f по %d редким словам  [%s]%s"
                  % (cid, eid, r, shared, esrc, same))
            hits += 1
    print("%s: подозрительных пар %d (порог %.2f, при равной цене %.2f)"
          % (label, hits, THRESHOLD, THRESHOLD_SAME_PRICE))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true", help="искать перевыкладки во всём массиве")
    ap.add_argument("--file", help="файл партии (new_listingsNNN.py) -- проверить перед вставкой")
    ap.add_argument("--text", help="одна строка описания")
    ap.add_argument("--city", help="город для --text")
    ap.add_argument("--source", help="ограничить сравнение одним источником, напр. fbmarketplace")
    a = ap.parse_args()

    site = load_site()
    if a.source:
        site = [r for r in site if r[3] == a.source]

    if a.file:
        cand = parse_batch(a.file)
        print("в партии %s строк: %d" % (a.file, len(cand)))
        sys.exit(1 if report(cand, site, a.file, build_common(site + cand)) else 0)

    if a.text:
        if not a.city:
            sys.exit("--text требует --city")
        one = [(0, a.city, None, "?", [a.text])]
        sys.exit(1 if report(one, site, "строка", build_common(site + one)) else 0)

    if a.audit:
        seen, hits = set(), 0
        common = build_common(site)
        norms = site
        for x in range(len(norms)):
            i1, c1, p1, s1, n1 = norms[x]
            for y in range(x + 1, len(norms)):
                i2, c2, p2, s2, n2 = norms[y]
                if c1 != c2:
                    continue
                r, shared = best_match(n1, n2, common.get(c1, set()))
                if flagged(r, shared, p1 == p2) and (i1, i2) not in seen:
                    seen.add((i1, i2)); hits += 1
                    print("  %s ~ %s  %.2f по %d редким  %s/%s  %s  цены %s / %s"
                          % (i1, i2, r, shared, s1, s2, c1, p1, p2))
        print("всего подозрительных пар: %d из %d строк" % (hits, len(norms)))
        sys.exit(0)

    ap.error("нужен один из режимов: --audit, --file или --text")


if __name__ == "__main__":
    main()
