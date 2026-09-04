# -*- coding: utf-8 -*-
"""Обновляет rates.json -- курсы валют для показа цены в карточке.

Зачем файл, а не константа в коде: курс, зашитый в исходник, через месяц врёт,
а через год врёт заметно. Здесь он лежит с датой, сборка эту дату показывает
рядом с пересчитанными суммами, и любому видно, насколько цифры свежие.

    python fetch_rates.py          # обновить
    python fetch_rates.py --show   # показать текущие, ничего не запрашивая

Источник -- open.er-api.com, бесплатный и без ключа. Если он недоступен,
скрипт НЕ трогает существующий файл: лучше показать вчерашний курс с честной
датой, чем обнулить его.

BASE -- валюта, в которой хранится нормализованная цена (pv) для фильтра и
сортировки: у площадки исторически всё во вьетнамских донгах, и бюджетный
фильтр подписан в миллионах донгов.
"""
import json, os, sys, urllib.request, datetime

OUT = "rates.json"
BASE = "VND"
# валюты, в которых объявления хранятся
LISTING = ["VND", "PHP"]
# валюты, которые показываем в скобках рядом с основной ценой
SHOW = ["RUB", "USD", "EUR", "CNY"]
API = "https://open.er-api.com/v6/latest/USD"


def fetch():
    req = urllib.request.Request(API, headers={"User-Agent": "RentSearcher/1.0 (currency display)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.loads(r.read().decode("utf-8"))
    if d.get("result") != "success":
        raise SystemExit("курсы: ответ без result=success -- файл не тронут")
    rates = d["rates"]
    need = set(LISTING) | set(SHOW) | {BASE, "USD"}
    missing = sorted(n for n in need if not rates.get(n))
    if missing:
        raise SystemExit("курсы: в ответе нет %s -- файл не тронут" % ", ".join(missing))
    return {n: float(rates[n]) for n in sorted(need)}, d.get("time_last_update_utc", "")


def main():
    if "--show" in sys.argv:
        if not os.path.exists(OUT):
            print("rates.json ещё нет")
            return
        d = json.load(open(OUT, encoding="utf-8"))
        print("дата: %s (источник обновил: %s)" % (d.get("date"), d.get("source_updated", "?")))
        for k, v in sorted(d["per_usd"].items()):
            print("   1 USD = %s %s" % (v, k))
        return

    try:
        per_usd, upd = fetch()
    except SystemExit:
        raise
    except Exception as ex:
        # существующий файл ценнее пустого: сборка покажет вчерашний курс с датой
        print("курсы недоступны (%s) -- rates.json оставлен как есть" % type(ex).__name__)
        return

    out = {
        "date": datetime.date.today().isoformat(),
        "source": API,
        "source_updated": upd,
        "base": BASE,
        "listing_currencies": LISTING,
        "show_currencies": SHOW,
        "per_usd": per_usd,
    }
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=False)
    os.replace(tmp, OUT)
    print("rates.json обновлён на %s" % out["date"])
    one_php_vnd = per_usd["VND"] / per_usd["PHP"]
    print("   1 USD = %.2f ₫ = %.2f ₱   (1 ₱ = %.1f ₫)" % (per_usd["VND"], per_usd["PHP"], one_php_vnd))


if __name__ == "__main__":
    main()
