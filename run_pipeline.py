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
    полей объявления. 1275 из 1617 строк сайта -- этот источник.
  * Facebook -- наполовину. fb_collect.py сам заходит в группы своим профилем
    и сам скачивает фотографии, но останавливается на файле кандидатов. Текст
    поста -- свободный, адрес в нём написан как попало, и превратить его в
    строку сайта пока может только человек или сессия. Программа не делает
    вид, что умеет: она собирает и отсеивает, а не сочиняет.
  * Telegram -- наполовину, ровно по той же причине.
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
        self.timeout, self.skip_if = timeout, skip_if


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
    tail = "\n".join((p.stdout or "").strip().split("\n")[-6:])
    log.write("$ %s\n%s\n%s\n" % (" ".join(step.argv), p.stdout or "", p.stderr or ""))
    log.flush()
    dt = time.time() - t0
    if p.returncode != 0:
        say(log, "  ПРОВАЛ (код %d, %.0f с). Последнее, что сказал:\n%s"
            % (p.returncode, dt, indent(tail or (p.stderr or "").strip()[-500:])))
        return "failed", tail
    say(log, "  готово за %.0f с\n%s" % (dt, indent(tail)))
    return "ok", tail


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
        return "оповещение пропущено: нет %s" % SAY
    try:
        p = subprocess.run([sys.executable, SAY, text], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=120)
        return (p.stdout or p.stderr or "").strip()
    except Exception as e:
        return "оповестить не удалось: %s" % e


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
        return False
    say(log, "опубликовано: %s" % git("log", "--oneline", "-1")[1])
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=float, default=3.0, help="возраст объявлений Chợ Tốt")
    ap.add_argument("--limit", type=int, default=40, help="максимум новых строк с Chợ Tốt")
    ap.add_argument("--fb-cities", default="dumaguete,cebu,manila")
    ap.add_argument("--fb-groups", type=int, default=2, help="групп на город за прогон")
    ap.add_argument("--tg-pages", type=int, default=2)
    ap.add_argument("--no-chotot", action="store_true")
    ap.add_argument("--no-fb", action="store_true")
    ap.add_argument("--no-tg", action="store_true")
    ap.add_argument("--no-maintain", action="store_true")
    ap.add_argument("--publish", action="store_true", help="закоммитить и запушить результат")
    ap.add_argument("--dirty-ok", action="store_true",
                    help="работать, даже если в дереве есть чужие правки")
    ap.add_argument("--dry-run", action="store_true", help="показать план и выйти")
    a = ap.parse_args()

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
    if d and not a.dirty_ok:
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
    try:
        with open(log_path, "w", encoding="utf-8") as log:
            say(log, "=== прогон %s ===" % stamp)
            for s in plan:
                say(log, "\n[%s]" % s.name)
                state, _tail = run(s, log)
                results.append((s, state))
                if state != "ok" and s.fatal:
                    break

            bad = [s.name for s, st in results if st in ("failed", "timeout") and s.fatal]
            soft = [s.name for s, st in results if st in ("failed", "timeout") and not s.fatal]
            skip = [s.name for s, st in results if st == "skipped"]
            note = "шагов %d, из них не сделано: %s" % (
                len(results), ", ".join(bad + soft + skip) or "ничего")
            say(log, "\n=== итог ===\n%s" % note)

            if bad:
                say(log, "оповещение владельцу: %s" % alert_owner(
                    "RentSearcher: суточный прогон остановлен на шаге «%s». Лог: %s"
                    % (bad[0], os.path.basename(log_path))))
            elif a.publish:
                publish(log, note)
            elif dirty():
                say(log, "результат не опубликован (--publish не задан); в дереве есть изменения")
        json.dump({"stamp": stamp, "steps": [(s.name, st) for s, st in results]},
                  open(os.path.join(LOG_DIR, "pipeline_last.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
    finally:
        try:
            os.unlink(LOCK)
        except FileNotFoundError:
            pass
    return 1 if any(st in ("failed", "timeout") and s.fatal for s, st in results) else 0


if __name__ == "__main__":
    sys.exit(main())
