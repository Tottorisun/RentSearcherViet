# -*- coding: utf-8 -*-
"""Весь суточный цикл проекта одной программой -- без модели в контуре.

ЗАЧЕМ ЭТО ПОЯВИЛОСЬ
===================
run_daily_check.ps1 запускает не программу, а сессию: `$prompt | claude.exe -p`.
Значит суточный цикл до сих пор существовал только как ТЕКСТ инструкции, и
каждый его шаг зависел от того, дошла ли сессия до конца и не устарел ли вход.
8 сентября 2026 стало видно, чем это плохо: партии копились, а порядок шагов
жил в голове у того, кто их выполнял.

Здесь порядок записан кодом. Программа не спрашивает и не додумывает: каждый
шаг -- отдельный существующий скрипт, который и так работал, а этот файл лишь
знает, в каком порядке их звать, когда остановиться и о чём сказать владельцу.

ЧТО ЗДЕСЬ АВТОНОМНО, А ЧТО НЕТ -- ЧЕСТНО
========================================
  * Chợ Tốt -- полностью. collect_chotot.py сам отбирает, сам пишет партию,
    сам вставляет: район берётся точным совпадением, описание собирается из
    полей объявления. Это главный источник сайта, и с 9 сентября 2026 он
    покрывает девять городов, а не один.
  * Facebook -- наполовину. fb_collect.py сам заходит в группы своим профилем
    и сам скачивает фотографии, но останавливается на файле кандидатов. Текст
    поста -- свободный, адрес в нём написан как попало, и превратить его в
    строку сайта пока может только человек или сессия. Программа не делает
    вид, что умеет: она собирает и отсеивает, а не сочиняет.
  * dotproperty.com.ph -- полностью, с 9 сентября 2026. У портала на каждой
    карточке лежит schema.org-разметка, а район ставится либо точным совпадением
    с CITIES, либо однозначным прецедентом, уже заведённым на сайте.
  * hoppler.com.ph -- полностью, с 10 сентября 2026. Метро Манила целиком:
    карточка списка несёт все поля сразу, а лимит тратится по кругу семи
    городов, чтобы самый крупный раздел не выбирал его в одиночку.
  * Telegram -- наполовину, ровно по той же причине, что и Facebook.
  * Обслуживание, сборка, карта, публикация -- полностью.

То есть после этого файла модель нужна ТОЛЬКО на разбор свободного текста двух
источников, а не на весь цикл, как раньше.

ЧЕГО ЗДЕСЬ НАМЕРЕННО НЕТ
========================
  * Публикации в телеграм-хабы. Отправка необратима: бот не может найти и
    удалить свой прошлый пост, а канал -- владельца. post_new_to_telegram.py
    и cleanup_telegram_posts.py вызываются отдельно и глазами.
  * Facebook на сервере. Профиль `_fb_profile/` -- это живой вход владельца в
    Facebook. Копировать его на VDS нельзя: личный аккаунт банят за вход с
    чужого адреса, и терять его ради расписания незачем. На машине без профиля
    шаг просто пропускается с объяснением, а не падает.

  python run_pipeline.py                    весь цикл без публикации
  python run_pipeline.py --publish          и закоммитить с пушем
  python run_pipeline.py --no-fb --no-tg    только Chợ Tốt и обслуживание
  python run_pipeline.py --dry-run          показать план и выйти
"""
import argparse
import datetime
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "daily_check_logs")
LOCK = os.path.join(HERE, ".pipeline.lock")
SAY = r"D:\MyDev\AI_CONTEXT\TASKS\gelios_say.py"
FB_PROFILE = os.path.join(HERE, "_fb_profile")


class Step:
    """Шаг цикла. `fatal` -- останавливает ли его провал весь прогон.

    Сбор не фатален намеренно: если Facebook не пустил, это не повод оставить
    сайт несобранным и без обновлённых курсов. Обслуживание и сборка -- фатальны:
    их провал означает, что публиковать нечего или нечестно."""

    def __init__(self, name, argv, fatal=True, timeout=1800, skip_if=None):
        self.name, self.argv, self.fatal = name, argv, fatal
        self.timeout, self.skip_if = int(timeout * TIMEOUT_SCALE), skip_if


# Пределы шагов рассчитаны на ПК во Вьетнаме. С сервера в Германии каждый из сотен
# последовательных запросов к вьетнамским и филиппинским сайтам идёт заметно
# дольше: 11 сентября 2026 шаг Chợ Tốt, занимающий на ПК 206-264 с, на Netcup
# шёл больше 480 с при пределе 900 -- упираясь не в процессор (занят на треть),
# а в расстояние. Множитель задаётся в окружении службы, на ПК он 1.
try:
    TIMEOUT_SCALE = max(1.0, float(os.environ.get("PIPELINE_TIMEOUT_SCALE") or 1))
except ValueError:
    TIMEOUT_SCALE = 1.0


def steps_for(a):
    py = sys.executable
    out = []
    if not a.no_chotot:
        out.append(Step("Chợ Tốt: сбор и вставка",
                        [py, "collect_chotot.py", "--days", str(a.days),
                         "--limit", str(a.limit), "--write", "--insert"],
                        fatal=False, timeout=900))
    if not a.no_fb:
        why = None if os.path.isdir(FB_PROFILE) else (
            "нет %s -- на этой машине вход в Facebook не заведён; "
            "профиль не переносится с чужой машины намеренно" % FB_PROFILE)
        for city in a.fb_cities.split(","):
            city = city.strip()
            if city:
                out.append(Step("Facebook: группы, %s" % city,
                                [py, "fb_collect.py", "--groups", "--city", city,
                                 "--max-groups", str(a.fb_groups)],
                                fatal=False, timeout=2400, skip_if=why))
    if not a.no_dotproperty:
        # Медленный по устройству: возраст записи виден только на её странице,
        # поэтому старые приходится открыть, чтобы отбросить. Отсюда и таймаут.
        out.append(Step("dotproperty: сбор и вставка",
                        [py, "collect_dotproperty.py", "--days", "14", "--pages", "3",
                         "--limit", "40", "--write", "--insert"],
                        fatal=False, timeout=2400))
    if not a.no_hoppler:
        # ОКНО 14 ДНЕЙ, А НЕ 30, хотя портал отдаёт и месячную давность:
        # hoppler не освобождён от чистки по возрасту, поэтому строка старше
        # двух недель была бы удалена тем же прогоном, что её завёл. Заводить и
        # тут же удалять -- это не сбор, а холостой ход по чужому сайту.
        # Практика показывает, что теряется при этом почти ничего: агенты
        # обновляют объявления постоянно, и у подавляющего большинства
        # «последнее изменение» -- сегодняшнее.
        out.append(Step("hoppler: сбор и вставка",
                        [py, "collect_hoppler.py", "--days", "14", "--pages", "2",
                         "--limit", "30", "--write", "--insert"],
                        fatal=False, timeout=2400))
    if not a.no_tg:
        out.append(Step("Telegram: каналы",
                        [py, "fetch_telegram_listings.py", "--pages", str(a.tg_pages)],
                        fatal=False, timeout=900))
    if not a.no_maintain:
        out += [
            Step("обслуживание: снятые с Chợ Tốt", [py, "remove_gone_listings.py"], timeout=2400),
            Step("обслуживание: снятые на порталах", [py, "remove_gone_web.py"], timeout=1800),
            Step("обслуживание: чистка по возрасту", [py, "purge_old_listings.py"]),
            Step("обслуживание: курсы валют", [py, "fetch_rates.py"], fatal=False, timeout=300),
            # Догоняет координаты у строк, заведённых до появления chotot_coords.json.
            # Порциями и не фатально: это улучшение карты, а не условие публикации.
            Step("обслуживание: координаты объявлений",
                 [py, "backfill_chotot_coords.py", "--limit", "150"], fatal=False, timeout=1800),
        ]
    # Порядок сборки не произволен: build_pins_step2_geocode.py читает DATA из
    # СОБРАННОЙ страницы, а не из rebuild_final.py, поэтому сборка идёт и до
    # карты, и после. step1 не зовём никогда: он переписывает pin_projections.json
    # целиком и стирает вручную добавленные Бинь Зыонг и Фукуок.
    out += [
        Step("сборка сайта", [py, "rebuild_final.py"], timeout=900),
        Step("карта: координаты", [py, "build_pins_step2_geocode.py"], timeout=3600),
        Step("карта: проекции пинов", [py, "build_pins_step3_project.py"]),
        Step("карта: данные Leaflet", [py, "build_leaflet_data.py"]),
        Step("сборка сайта (после карты)", [py, "rebuild_final.py"], timeout=900),
    ]
    if a.candidates_only:
        out = [st for st in out if st.name.startswith(("Facebook:", "Telegram:"))]
    return out


def run(step, log):
    if step.skip_if:
        say(log, "  ПРОПУЩЕН: %s" % step.skip_if)
        return "skipped", ""
    t0 = time.time()
    try:
        p = subprocess.run(step.argv, cwd=HERE, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=step.timeout)
    except subprocess.TimeoutExpired:
        say(log, "  ПРОВАЛ: не уложился в %d с" % step.timeout)
        return "timeout", ""
    # Хвост берём из ОБОИХ потоков. Сначала брался только stdout, и отказ
    # fb_collect.py («not logged in», stderr) в сводке выглядел пустым местом:
    # шаг провалился, а причина не показана -- ровно та беда, ради которой
    # сводка и заведена.
    merged = "\n".join(x for x in ((p.stdout or "").strip(), (p.stderr or "").strip()) if x)
    tail = "\n".join([ln for ln in merged.split("\n") if ln.strip()][-6:])
    log.write("$ %s\n%s\n%s\n" % (" ".join(step.argv), p.stdout or "", p.stderr or ""))
    log.flush()
    dt = time.time() - t0
    if p.returncode != 0:
        say(log, "  ПРОВАЛ (код %d, %.0f с). Последнее, что сказал:\n%s"
            % (p.returncode, dt, indent(tail)))
        return "failed", tail
    say(log, "  готово за %.0f с\n%s" % (dt, indent(tail)))
    return "ok", tail


NEEDS_LOGIN = "not logged in"
ALERT_MEMO = os.path.join(LOG_DIR, ".pipeline_last_alert.json")


def alert_once(text, key, hours=24):
    """Одна беда -- одно сообщение в сутки. Прогон может идти трижды в день, и
    три одинаковых сообщения про протухший вход делают незаметными настоящие."""
    try:
        memo = json.load(open(ALERT_MEMO, encoding="utf-8"))
    except Exception:
        memo = {}
    last = memo.get(key)
    if last and (time.time() - last) < hours * 3600:
        return "оповещение пропущено: то же самое сообщали %d ч назад" % ((time.time() - last) / 3600)
    res = alert_owner(text)
    memo[key] = time.time()
    try:
        json.dump(memo, open(ALERT_MEMO, "w", encoding="utf-8"))
    except Exception:
        pass
    return res


def indent(text):
    return "\n".join("    " + ln for ln in (text or "").split("\n") if ln.strip())


def say(log, line):
    print(line)
    log.write(line + "\n")
    log.flush()


def alert_owner(text):
    """Провал обязан быть слышен. Лог никто не открывает -- 3 сентября вход
    протух, и об этом узнали по устаревшим данным, а не от программы."""
    if not os.path.exists(SAY):
        return telegram_direct(text)
    try:
        p = subprocess.run([sys.executable, SAY, text], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=120)
        return (p.stdout or p.stderr or "").strip()
    except Exception as e:
        return "оповестить не удалось: %s" % e


def telegram_direct(text):
    """Оповещение там, где gelios_say.py нет, -- на сервере.

    Тот же бот и тот же чат, что у gelios_say.py: токен -- из файла
    GELIOS_TOKEN_FILE (или ~/.gelios/token), чат -- из переменной GELIOS_CHAT_ID.
    В репозитории нет ни того, ни другого: он публичный. До 11 сентября 2026 на
    машине без gelios_say.py оповещение молча пропускалось -- то есть на сервере
    о протухшем входе, упавшем шаге или несостоявшемся пуше не узнал бы никто."""
    tf = (os.environ.get("GELIOS_TOKEN_FILE")
          or os.path.join(os.path.expanduser("~"), ".gelios", "token"))
    chat = os.environ.get("GELIOS_CHAT_ID")
    if not chat or not os.path.exists(tf):
        return "оповещение пропущено: нет ни %s, ни токена с GELIOS_CHAT_ID" % SAY
    try:
        token = open(tf, encoding="utf-8").read().strip()
        data = urllib.parse.urlencode({"chat_id": chat, "text": "[сервер] " + text[:3990],
                                       "disable_web_page_preview": "true"}).encode()
        req = urllib.request.Request("https://api.telegram.org/bot%s/sendMessage" % token,
                                     data=data)
        with urllib.request.urlopen(req, timeout=25) as r:
            return ("отправлено в Telegram" if json.load(r).get("ok")
                    else "Telegram не принял сообщение")
    except Exception as e:
        # Текст исключения не печатается: в нём может оказаться адрес с токеном.
        return "оповестить не удалось (%s)" % type(e).__name__


def git(*args):
    p = subprocess.run(["git"] + list(args), cwd=HERE, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()


def dirty():
    return git("status", "--porcelain")[1]


def publish(log, note):
    rc, out, _ = git("status", "--porcelain")
    if not out:
        say(log, "публиковать нечего: рабочее дерево чистое")
        return True
    git("add", "-A")
    msg = ("Автоматический прогон %s\n\n%s\n\n"
           "Собрано run_pipeline.py без модели в контуре: Chợ Tốt вставлен\n"
           "программой, кандидаты Facebook и Telegram оставлены на разбор.\n"
           % (datetime.date.today().isoformat(), note))
    rc, _, err = git("commit", "-m", msg)
    if rc != 0:
        say(log, "коммит не прошёл: %s" % err)
        return False
    rc, _, err = git("push")
    if rc != 0:
        say(log, "пуш не прошёл: %s" % err)
        # Раньше провал пуша оставался только в логе, а прогон завершался с кодом 0:
        # данные собраны, сайт не обновлён, и никто об этом не знает.
        last = (err.strip().splitlines() or ["?"])[-1][:200]
        say(log, "оповещение владельцу: %s" % alert_once(
            "RentSearcher: прогон собрал данные, но не опубликовал их -- пуш не прошёл (%s)."
            % last, "push-failed", hours=12))
        return False
    say(log, "опубликовано: %s" % git("log", "--oneline", "-1")[1])
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=float, default=3.0, help="возраст объявлений Chợ Tốt")
    # 40 было рассчитано на один город. С девятью источник даёт больше тысячи
    # подходящих в сутки, и 40 означало бы отставать от него каждый день.
    ap.add_argument("--limit", type=int, default=150, help="максимум новых строк с Chợ Tốt")
    # Все города, по которым в реестре fb_collect.GROUPS есть группы. Вьетнамские
    # добавлены 11 сентября 2026: до этого их группы стояли в реестре, но ночной
    # прогон их не обходил -- что было незаметно, пока он не собирал вообще ничего.
    ap.add_argument("--fb-cities", default="dumaguete,cebu,manila,ho-chi-minh,nha-trang,da-nang")
    ap.add_argument("--fb-groups", type=int, default=2, help="групп на город за прогон")
    ap.add_argument("--tg-pages", type=int, default=2)
    ap.add_argument("--no-chotot", action="store_true")
    ap.add_argument("--no-fb", action="store_true")
    ap.add_argument("--no-dotproperty", action="store_true")
    ap.add_argument("--no-hoppler", action="store_true")
    ap.add_argument("--no-tg", action="store_true")
    ap.add_argument("--no-maintain", action="store_true")
    # С 11 сентября 2026 сайт собирает и публикует сервер (Netcup), а ПК владельца
    # собирает то, что может только он: Facebook -- из-за входа в личный аккаунт,
    # Telegram -- потому что его кандидатов разбирает сессия на этом же ПК.
    ap.add_argument("--candidates-only", action="store_true",
                    help="только кандидаты Facebook и Telegram: без сборки и публикации")
    ap.add_argument("--publish", action="store_true", help="закоммитить и запушить результат")
    ap.add_argument("--dirty-ok", action="store_true",
                    help="работать, даже если в дереве есть чужие правки")
    ap.add_argument("--dry-run", action="store_true", help="показать план и выйти")
    a = ap.parse_args()
    if a.candidates_only and a.publish:
        sys.exit("--candidates-only и --publish несовместимы: кандидатов не публикуют, "
                 "их разбирает сессия")

    plan = steps_for(a)
    if a.dry_run:
        print("план прогона (%d шагов):" % len(plan))
        for s in plan:
            print("  %-38s %s%s" % (s.name, " ".join(s.argv[1:]),
                                    "   [будет пропущен]" if s.skip_if else ""))
        print("публикация: %s" % ("да" if a.publish else "нет"))
        return 0

    # Чужие правки в дереве -- повод не начинать: параллельная сессия может
    # прямо сейчас держать наполовину сделанную партию, а --publish закоммитит
    # её вместе со своим.
    d = dirty()
    # Кандидаты пишутся только в игнорируемые файлы, так что состояние дерева им
    # безразлично, а сессия на ПК вполне может быть на середине своей партии.
    if d and not a.dirty_ok and not a.candidates_only:
        sys.exit("в рабочем дереве есть незакоммиченные правки (%d файлов) -- возможно, "
                 "работает другая сессия. Разберитесь или запустите с --dirty-ok:\n%s"
                 % (len(d.split("\n")), d[:800]))

    os.makedirs(LOG_DIR, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log_path = os.path.join(LOG_DIR, "pipeline_%s.log" % stamp)
    try:
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        age = time.time() - os.path.getmtime(LOCK)
        if age < 6 * 3600:
            sys.exit("другой прогон уже идёт (%s, начат %d мин назад)" % (LOCK, age / 60))
        os.unlink(LOCK)
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.write(fd, ("%d %s" % (os.getpid(), stamp)).encode())
    os.close(fd)

    results = []
    publish_failed = False
    try:
        with open(log_path, "w", encoding="utf-8") as log:
            say(log, "=== прогон %s ===" % stamp)
            for s in plan:
                say(log, "\n[%s]" % s.name)
                state, tail = run(s, log)
                results.append((s, state, tail))
                if state != "ok" and s.fatal:
                    break

            bad = [s.name for s, st, _t in results if st in ("failed", "timeout") and s.fatal]
            soft = [s.name for s, st, _t in results if st in ("failed", "timeout") and not s.fatal]
            skip = [s.name for s, st, _t in results if st == "skipped"]

            # Протухший вход в Facebook -- не сбой прогона, а работа для
            # владельца: только он может войти руками, и пока он этого не
            # сделает, источник просто молчит. Молчащий источник заметен
            # только если о нём сказать.
            if any(NEEDS_LOGIN in (t or "") for _s, _st, t in results):
                say(log, "Facebook: вход протух. %s" % alert_once(
                    "RentSearcher: сбор из групп Facebook остановлен -- вход в профиле "
                    "истёк. Нужен один вход руками: python fb_collect.py --login "
                    "(из D:\\MyDev\\Rent Searcher). До этого группы не собираются.",
                    "fb-login"))
            note = "шагов %d, из них не сделано: %s" % (
                len(results), ", ".join(bad + soft + skip) or "ничего")
            say(log, "\n=== итог ===\n%s" % note)

            if bad:
                say(log, "оповещение владельцу: %s" % alert_owner(
                    "RentSearcher: суточный прогон остановлен на шаге «%s». Лог: %s"
                    % (bad[0], os.path.basename(log_path))))
            elif a.publish:
                publish_failed = not publish(log, note)
            elif dirty():
                say(log, "результат не опубликован (--publish не задан); в дереве есть изменения")
        json.dump({"stamp": stamp, "steps": [(s.name, st) for s, st, _t in results]},
                  open(os.path.join(LOG_DIR, "pipeline_last.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
    finally:
        try:
            os.unlink(LOCK)
        except FileNotFoundError:
            pass
    return 1 if (publish_failed or any(st in ("failed", "timeout") and s.fatal
                                        for s, st, _t in results)) else 0


if __name__ == "__main__":
    sys.exit(main())
