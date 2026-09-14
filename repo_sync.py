# -*- coding: utf-8 -*-
"""Коммит строк, которые программа заводит на ПК: подтянуть сервер ДО вставки.

Порядок здесь и есть вся суть. `git pull --rebase` отказывает, пока в дереве
изменён хоть один отслеживаемый файл, а вставка строк сама меняет
rebuild_final.py. Шаги Facebook и batdongsan сначала вставляли и лишь потом
тянули -- и не могли закоммитить ни одной партии (прогон ПК 13.09.2026:
«cannot pull with rebase: You have unstaged changes»). Хуже того, брошенные
ими изменения срывали такой же коммит следующему прогону.

Подтянуть надо и до резервирования номеров: allocate_ids берёт наибольший id
из rebuild_final.py и свой журнал, а журналы у сервера и ПК разные. Блок
3000000 делят Facebook и batdongsan на ПК с hoppler и dotproperty на сервере:
не видя серверных строк, ПК выдал бы те же номера.

    why = repo_sync.prepare(["rebuild_final.py"])      # до allocate и вставки
    ...вставка партии path...
    err = repo_sync.commit_and_push([...свои файлы...], msg, path)
"""
import subprocess
import sys

SOURCE = "rebuild_final.py"


def git(*args):
    return subprocess.run(["git"] + list(args), capture_output=True, text=True, encoding="utf-8")


def _said(r, n=160):
    return ((r.stdout or "") + (r.stderr or "")).strip().replace("\n", " ")[:n]


def _pull():
    # --autostash: правка сессии в ДРУГОМ файле (скажем, в коде) не должна
    # останавливать сбор -- git уберёт её на время перебазирования и вернёт.
    # Свои файлы шага проверены раньше, в prepare().
    r = git("pull", "--rebase", "--autostash", "--quiet")
    if r.returncode:
        # Оборванное на конфликте перебазирование оставило бы репозиторий в
        # полусостоянии, и в нём споткнулся бы уже любой следующий шаг.
        git("rebase", "--abort")
    return r


def prepare(own_files):
    """До резервирования номеров и вставки. None -- можно заводить, иначе причина отложить."""
    dirty = (git("status", "--porcelain", "--", *own_files).stdout or "").strip()
    if dirty:
        # Изменения в своих файлах, сделанные не этим шагом, -- чужая работа:
        # `git add` унёс бы её в коммит программы.
        return "свои файлы уже изменены кем-то ещё, чтобы не смешать работу: %s" % dirty.replace("\n", "; ")
    r = _pull()
    if r.returncode:
        return "git pull --rebase не прошёл: %s" % _said(r)
    return None


def _commit(files, msg):
    r = git("add", "--", *files)
    if r.returncode:
        return "git add не прошёл: %s" % _said(r, 200)
    # Пути после «--» -- коммит только их, даже если в индексе лежит чужое.
    r = git("commit", "-q", "-m", msg, "--", *files)
    if r.returncode:
        return "git commit не прошёл: %s" % _said(r)
    return None


def commit_and_push(files, msg, batch=None, redo=None):
    """После правки rebuild_final.py. None -- в репозитории, иначе что не получилось.

    Повторить правку поверх серверной версии можно двумя способами: `batch` --
    файл партии, который вставляет строки заново; `redo` -- функция без
    аргументов, которая повторяет правку сама и возвращает None или причину
    неудачи (так снимает строки remove_gone_facebook.py: у снятия файла партии нет)."""
    err = _commit(files, msg)
    if err:
        return err
    if not git("push", "-q", "origin", "HEAD").returncode:
        return None
    # Отказ почти всегда значит, что сервер успел отправить свой прогон.
    # Перебазировать свой коммит бесполезно: insert_listings ставит и серверные,
    # и свои строки перед одной и той же меткой, так что git видит конфликт при
    # любом совпадении по времени. Коммит снимается, rebuild_final.py
    # возвращается к общему виду, а партия -- она лежит на диске отдельным
    # файлом -- вставляется заново поверх серверной версии. Застрявший
    # неотправленный коммит конфликтовал бы и у всех следующих прогонов.
    git("reset", "-q", "HEAD~1")
    git("checkout", "--", SOURCE)
    p = _pull()
    if p.returncode:
        return "push отклонён, а pull --rebase не прошёл -- партия не вставлена: %s" % _said(p)
    if batch:
        r = subprocess.run([sys.executable, batch], capture_output=True, text=True, encoding="utf-8")
        if r.returncode:
            # insert_listings отказывает сам, если сервер тем временем выдал те же
            # номера или завёл те же адреса.
            return "после подтягивания сервера партия не встала заново -- не отправлено: %s" % _said(r, 240)
        if (r.stdout or "").strip():
            print(r.stdout.strip())
    elif redo:
        why = redo()
        if why:
            return "после подтягивания сервера правка не повторилась -- не отправлено: %s" % why
    else:
        return "push отклонён, а повторить правку нечем (нет ни batch, ни redo) -- не отправлено"
    err = _commit(files, msg)
    if err:
        return err
    r = git("push", "-q", "origin", "HEAD")
    return ("закоммичено, но push не прошёл: %s" % _said(r)) if r.returncode else None
