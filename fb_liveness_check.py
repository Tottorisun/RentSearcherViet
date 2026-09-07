# -*- coding: utf-8 -*-
"""Проверка живости фейсбучных объявлений — в два шага, через залогиненный браузер.

Почему не как у остальных источников. remove_gone_web.py опрашивает dotproperty и
hoppler обычным запросом из питона, но с Facebook так нельзя: на любой запрос без
сессии он отвечает HTTP 400 и одинаковой служебной страницей — на живое, на
снятое и на выдуманное (измерено 8 сентября 2026). Сигнала там нет вовсе.

А ВОТ ИЗНУТРИ залогиненной страницы сигнал есть, и чистый. `fetch` с
credentials:'include' на facebook.com отдаёт:
    живое   -> HTTP 200, ~1.07 МБ, маркера нет
    снятое  -> HTTP 200, ~1.04 МБ, есть «isn't available»
    выдуманное -> то же, что снятое
Проверено на заведомо снятом посте 28698912193035115 и на выдуманных id и для
Marketplace, и для групп.

Отсюда и порядок: питон готовит список, браузер его проверяет, питон удаляет.
Полностью автоматическим этот шаг быть не может — нужна сессия владельца,
то есть присутствие человека. Поэтому он и не в ночном прогоне.

  1. python fb_liveness_check.py --emit
     напишет _fb_liveness_run.js со списком текущих фейсбучных строк.
  2. Открыть любую страницу facebook.com в залогиненном браузере, вставить
     содержимое файла в консоль (javascript_tool), дождаться, пока
     `Object.keys(window.__R).length` дорастёт до общего числа, и забрать
     `window.__gone()` — строку с id снятых.
  3. python fb_liveness_check.py --apply 3000123,3000456
     удалит их из rebuild_final.py под блокировкой.

Ограничение по времени: одна страница весит около мегабайта и тянется ~2 с,
поэтому 87 строк идут около трёх минут. Вызов JS обрывается по таймауту раньше,
но цикл продолжает работать в фоне — запускать его надо БЕЗ await и опрашивать
счётчик. И не подменять тело страницы, пока он идёт: это его останавливает
(наступил на это 8 сентября, потерял 6 строк из 87).
"""
import io, json, sys

FB_SOURCES = ("fbmarketplace", "fbgroup")
OUT = "_fb_liveness_run.js"

JS_TEMPLATE = """// Сгенерировано fb_liveness_check.py -- вставить в консоль на facebook.com.
// Запускать БЕЗ await: window.__run(); потом опрашивать window.__R.
window.__T = %s;
window.__R = window.__R || {};
window.__url = t => t.k === 'm'
  ? 'https://www.facebook.com/marketplace/item/' + t.r + '/'
  : 'https://www.facebook.com/groups/' + t.r.split('/')[0] + '/posts/' + t.r.split('/')[1] + '/';
window.__run = async function () {
  const sl = ms => new Promise(r => setTimeout(r, ms));
  for (const t of window.__T) {
    if (window.__R[t.i]) continue;
    try {
      const res = await fetch(window.__url(t), { credentials: 'include' });
      const body = await res.text();
      // Единственный надёжный признак: Facebook отвечает 200 и на живое, и на
      // снятое, различает их только текст страницы.
      const gone = /isn.t available|content isn|not available right now/i.test(body);
      window.__R[t.i] = { s: res.status, n: body.length, v: gone ? 'GONE' : 'ALIVE' };
    } catch (e) {
      window.__R[t.i] = { s: 0, n: 0, v: 'ERR' };   // ошибка НИКОГДА не 'снято'
    }
    await sl(150);
  }
  return 'готово ' + Object.keys(window.__R).length + ' из ' + window.__T.length;
};
window.__gone = () => Object.keys(window.__R).filter(i => window.__R[i].v === 'GONE').join(',');
window.__stat = () => Object.entries(window.__R).reduce((a, [, v]) => (a[v.v] = (a[v.v] || 0) + 1, a), {});
'загружено целей: ' + window.__T.length;
"""


def targets():
    from site_data import load_listings
    out = []
    for l in load_listings():
        if l.get("source") not in FB_SOURCES:
            continue
        url = l["url"].rstrip("/")
        if "/marketplace/item/" in url:
            out.append({"i": str(l["id"]), "k": "m", "r": url.rsplit("/", 1)[-1]})
        else:
            p = url.split("/")
            out.append({"i": str(l["id"]), "k": "g", "r": "%s/%s" % (p[-3], p[-1])})
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if "--emit" in sys.argv:
        t = targets()
        io.open(OUT, "w", encoding="utf-8", newline="\n").write(
            JS_TEMPLATE % json.dumps(t, ensure_ascii=False))
        print("целей: %d (%s)" % (len(t), ", ".join(FB_SOURCES)))
        print("записано в %s — вставить в консоль на facebook.com" % OUT)
        return
    if "--apply" in sys.argv:
        raw = sys.argv[sys.argv.index("--apply") + 1]
        ids = [int(x) for x in raw.replace(" ", "").split(",") if x]
        if not ids:
            sys.exit("--apply без идентификаторов")
        known = {int(t["i"]) for t in targets()}
        alien = [i for i in ids if i not in known]
        if alien:
            sys.exit("это не фейсбучные строки текущего массива: %s — проверьте, "
                     "не перепутан ли список" % alien)
        from listing_lock import remove_listings
        removed = remove_listings(ids, owner=__file__)
        print("удалено: %d — %s" % (len(removed), removed))
        print("дальше: rebuild_final.py -> geocode -> leaflet -> rebuild_final.py")
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
