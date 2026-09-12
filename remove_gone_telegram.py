# -*- coding: utf-8 -*-
"""Проверка «жив ли пост» для телеграм-строк сайта.

ЗАЧЕМ. Живость проверяют два скрипта, и телеграма нет ни в одном:
remove_gone_listings.py смотрит только Chợ Tốt (`if l.get("source") != "chotot"`),
remove_gone_web.py -- dotproperty и hoppler. Строки с source="telegram" не
проверял никто. 12 сентября 2026 это нашлось случайно: пост
DaNangRentAFlat/129863 был удалён, а строка 2000590 висела на сайте как живая
(снята вручную). Сколько таких же висит ещё -- никто не считал, потому что
считать было нечем.

ПОЧЕМУ ССЫЛКА НА ПОСТ, А НЕ ЛЕНТА КАНАЛА. Похожая проверка есть внутри
ingest_telegram.seed_state, но она читает ленту t.me/s/<канал> и судит только
те номера, что попали на скачанные страницы, то есть верхушку. Пропадают же
как раз старые посты, до которых лента не достаёт. Здесь спрашивается каждый
пост по своему адресу, поэтому возраст строки роли не играет.

ЧТО СЧИТАЕТСЯ ПРОПАЖЕЙ. Только явное «Post not found» в
`tgme_widget_message_error`. Измерено 12 сентября 2026 на самом t.me:
  удалённый пост  DaNangRentAFlat/129863   -> error-div, «Post not found»
  живой пост      DaNangRentAFlat/128821   -> есть tgme_widget_message_text
  выдуманный канал                         -> тот же error-div, но
                                              «Channel with username @... not found»
Последнее -- НЕ пропажа поста: канал могли переименовать или закрыть, и целый
канал надо разбирать руками, а не выкашивать пачкой. Всё остальное -- таймаут,
обрыв, 429, незнакомая разметка -- тоже не повод удалять: строка просто
остаётся непроверенной до следующего прогона.

ПОТОЛОК НА УДАЛЕНИЕ. Если t.me начнёт отдавать заглушку или разметка поедет,
«пропавшими» окажутся сразу все проверенные, и один прогон снёс бы с сайта
весь телеграм. Поэтому при MAX_GONE и больше пропаж (или больше четверти
проверенных) не удаляется ничего -- это разбирает человек.

ЦЕНА -- ТОЛЬКО ОТЧЁТОМ. У живого поста берётся текст из того же ответа и
разбирается шаблонами ingest_telegram: пост агентства пишет цену в
предсказуемой строке. Расхождение печатается и НИЧЕГО не меняет: 12 сентября
у строки 2000557 на сайте стояло 60 млн, а в посте уже 70 млн, но цену в
rebuild_final.py правят руками -- разбор шаблона для этого недостаточно надёжен.

    python remove_gone_telegram.py                 отчёт, ничего не трогает
    python remove_gone_telegram.py --limit 15      отчёт по 15 строкам
    python remove_gone_telegram.py --apply         удалить пропавшие
    python remove_gone_telegram.py --apply --all   весь список за один прогон
"""
import sys

# Консоль этой машины -- cp1251 и не печатает ни вьетнамский, ни эмодзи из постов.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

import json
import os
import re
import time

import fetch_telegram_listings as ftl          # http_get: свой User-Agent и повторы
from listing_lock import remove_listings
from site_data import load_listings

# Разбор цены -- необязательное дополнение к проверке живости, и падать из-за
# него проверка не должна: ingest_telegram тянет за собой выгрузку улиц и прочее.
try:
    import ingest_telegram
except Exception as _ex:                       # noqa: BLE001 -- любая беда при импорте
    ingest_telegram = None
    INGEST_ERROR = _ex
else:
    INGEST_ERROR = None

CACHE_FILE = "liveness_telegram_cache.json"
# Ссылка вида https://t.me/<канал>/<номер>. Строки, ссылающиеся на канал целиком
# (без номера), проверить нечем -- в канале живы другие посты, а про этот объект
# ответа нет.
POST_URL = re.compile(r"^https?://t\.me/([A-Za-z0-9_]+)/(\d+)\b")
ERROR_DIV = re.compile(r'tgme_widget_message_error[^>]*>(.*?)</div>', re.S)
GONE_TEXT = "post not found"

# 61 проверяемая строка на 12 сентября 2026: с паузой в секунду весь список
# проходится примерно за минуту. Когда строк станет заметно больше, прогон
# будет доходить до остальных на следующий день -- порядок задаёт кэш, первыми
# идут те, кого дольше всех не проверяли.
DEFAULT_LIMIT = 60
PAUSE = 1.0                                    # t.me не любит частых запросов
MAX_GONE = 20
MAX_GONE_SHARE = 0.25


def load_json(path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return default


def save_json(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def money(n):
    return format(int(n), ",").replace(",", " ") if isinstance(n, (int, float)) else str(n)


def check(channel, msg_id):
    """('gone'|'alive'|'unclear', пояснение, текст поста).

    Ошибка транспорта и незнакомый ответ -- НИКОГДА не 'gone'."""
    url = "https://t.me/%s/%d?embed=1&mode=tme" % (channel, msg_id)
    try:
        html = ftl.http_get(url)
    except Exception as ex:                    # http_get уже сделал свои повторы
        return "unclear", "запрос не удался (%s)" % type(ex).__name__, ""
    err = ERROR_DIV.search(html)
    if err:
        # Текст ошибки разбираем дословно: «Channel ... not found» -- это про
        # канал, а не про пост, и удалять по нему строки нельзя.
        plain = re.sub(r"<[^>]+>", "", err.group(1)).strip()
        if GONE_TEXT in plain.lower():
            return "gone", plain, ""
        return "unclear", "t.me отвечает «%s» — это не про пост" % plain[:80], ""
    if "tgme_widget_message_text" not in html:
        # Пост без текста (одни фото) тоже сюда попадёт -- и это правильно:
        # такой ответ мы не умеем толковать, а гадать нельзя.
        return "unclear", "ответ без текста поста и без ошибки (%d байт)" % len(html), ""
    posts, _ = ftl.parse_page(html, channel)
    return "alive", "пост на месте", (posts[0]["text"] if posts else "")


def post_price(text):
    """(цена, валюта) по шаблону агентства или (None, None). Только для отчёта."""
    if ingest_telegram is None or not text:
        return None, None
    try:
        p = ingest_telegram.parse_post(text)
    except ingest_telegram.Skip:               # шаблон свой, но пост с изъяном
        return None, None
    except Exception:                          # разбор -- дополнение, а не проверка
        return None, None
    if not p or not p.get("price"):
        return None, None
    return p["price"], p.get("cur")


def main():
    argv = sys.argv[1:]
    unknown = [a for a in argv if a.startswith("-") and a not in ("--apply", "--dry-run",
                                                                  "--all", "--limit")]
    if unknown:
        sys.exit("неизвестный ключ: %s (есть --apply, --dry-run, --all, --limit N)"
                 % " ".join(unknown))
    # Удаление -- только по явному --apply. Опечатка в ключе оставляет прогон
    # отчётом, а не наоборот.
    apply_mode = "--apply" in argv and "--dry-run" not in argv
    limit = DEFAULT_LIMIT
    if "--limit" in argv:
        limit = int(argv[argv.index("--limit") + 1])

    listings = load_listings()
    tg = [l for l in listings if l.get("source") == "telegram"]
    rows, channel_only = [], []
    for l in tg:
        m = POST_URL.match(l.get("url") or "")
        if m:
            rows.append((l["id"], l.get("city"), m.group(1), int(m.group(2)),
                         l.get("price"), l.get("cur") or "VND"))
        else:
            channel_only.append(l)

    cache = load_json(CACHE_FILE, {})
    rows.sort(key=lambda r: cache.get(str(r[0]), {}).get("checked", 0))
    todo = rows if "--all" in argv else rows[:limit]

    print("телеграм-строк на сайте: %d, со ссылкой на конкретный пост: %d, проверяю %d%s"
          % (len(tg), len(rows), len(todo),
             "" if apply_mode else " — режим отчёта, ничего не удаляю"))
    if channel_only:
        print("НЕ проверяется: %d строк ссылаются на канал без номера поста (%s) — "
              "по такой ссылке не видно, что стало с самим объявлением"
              % (len(channel_only), ", ".join(str(l["id"]) for l in channel_only)))
    if INGEST_ERROR is not None:
        print("цены не сверяются: ingest_telegram не импортировался (%s)" % INGEST_ERROR)

    gone, alive, unclear, price_diff = [], 0, 0, []
    now = int(time.time())
    t0 = time.time()
    for lid, city, channel, msg_id, price, cur in todo:
        link = "https://t.me/%s/%d" % (channel, msg_id)
        verdict, why, text = check(channel, msg_id)
        if verdict == "gone":
            gone.append((lid, city, link, why))
            cache[str(lid)] = {"checked": now, "gone": True}
        elif verdict == "alive":
            alive += 1
            cache[str(lid)] = {"checked": now}
            ppr, pcur = post_price(text)
            if ppr and price and pcur == cur and ppr != price:
                price_diff.append((lid, city, link, price, ppr, cur))
        else:
            unclear += 1
            print("  %s (%s): %s — пропавшим НЕ считаю" % (lid, link, why))
            # t.me лёг или закрылся целиком -- выходим, а не выкашиваем список.
            if unclear >= 10 and alive == 0 and not gone:
                sys.exit("10 непонятных ответов подряд и ни одного живого поста — "
                         "t.me недоступен, выхожу без изменений")
        time.sleep(PAUSE)

    print("проверено %d за %.0f с: живых %d, пропало %d, неясных %d"
          % (len(todo), time.time() - t0, alive, len(gone), unclear))
    for lid, city, link, why in gone:
        print("  ПРОПАЛ  %s  (%s, %s): %s" % (lid, city, link, why))
    if price_diff:
        print("цена разошлась с постом (только отчёт, ничего не меняю — правится руками):")
        for lid, city, link, was, now_price, cur in price_diff:
            print("  %s  (%s, %s): на сайте %s %s, в посте %s %s"
                  % (lid, city, link, money(was), cur, money(now_price), cur))

    if not apply_mode:
        print("режим отчёта — ничего не удалено; удалить: python remove_gone_telegram.py --apply")
        return
    if gone:
        # Столько пропаж разом -- это не удалённые посты, а сломанный разбор
        # или блокировка со стороны t.me. Такое разбирает человек.
        if len(gone) >= MAX_GONE or len(gone) > len(todo) * MAX_GONE_SHARE:
            sys.exit("пропавших %d из %d проверенных — на удаление постов это не похоже "
                     "(потолок: %d штук или четверть проверенных); ничего не удалено, "
                     "разберитесь глазами" % (len(gone), len(todo), MAX_GONE))
        # Блокировку берёт сама remove_listings (listing_lock.py:142). Обёртка
        # снаружи была бы самозахватом: тот же процесс ждал бы замок, который
        # держит он сам.
        removed = remove_listings([g[0] for g in gone], owner=__file__)
        print("удалено из rebuild_final.py: %d" % len(removed))
        for lid, _city, _link, _why in gone:
            cache.pop(str(lid), None)
    save_json(CACHE_FILE, cache)


if __name__ == "__main__":
    main()
