# Анализ репозитория RentSearcherViet — октябрь 2026

Ветка `analysis-2026-10`, состояние `main` на коммит `e77f4c6` (26.10.2026).
Ничего не удалено и не перенесено. В этой ветке добавлены только этот отчёт,
`tests/`, `pytest.ini`, `requirements-dev.txt` и job `tests` в `.github/workflows/ci.yml`.

Как считались цифры: регулярными выражениями по `git ls-files` (скрипт в отчёт не
вошёл). Персональные данные в отчёт не скопированы: только файл, тип и количество.
Совпадения внутри URL фотографий (hex-хэши) отфильтрованы, телефоны проверены
выборочно по контексту. Клон мелкий (`--depth 50`, 07.10–26.10.2026), поэтому всё,
что сказано про историю, оценено по последним 50 коммитам. Полную историю нужно
перепроверить на полном клоне.

---

## 0. Главное

| # | Что | Насколько срочно |
|---|---|---|
| 1 | `assets/fb_photos/`: 129 МБ, 1 709 фото из постов частных лиц в группах Facebook, перезалитых в публичный репозиторий. **Ни одна текущая строка сайта на них не ссылается** (0 из 352 каталогов) | высокая: авторские права и ПДн, половина веса checkout |
| 2 | В архивных партиях `new_listingsN.py` лежат контакты частных лиц: поле `contact` (48 файлов), 45 телефонов, ссылки на 483 поста в FB-группах | высокая: файлы публичны и есть в истории |
| 3 | Сгенерированные HTML (32 МБ на tip) коммитятся дважды в сутки, по оценке это около 4 МБ сжатых данных в день в `.git` | средняя: репозиторий растёт примерно на 1,4 ГБ в год |
| 4 | 550 партий `new_listingsN.py` (58 МБ) — уже применённая история, но сборщики нумеруют новые партии через `glob("new_listings*.py")` в корне. **Просто перенести их в `archive/` нельзя**: нумерация начнётся заново | блокирует уборку |
| 5 | Тестов не было, CI делал только `compileall`. Добавлено 42 теста (≈4 с), включая полную сборку на реальных `listings/` | сделано в этой ветке |

---

## 1. Риски публичности

### 1.1 Персональные данные

**Живой сайт** (`listings/**/*.jsonl`, все 40 сгенерированных `*.html`, `assets/app.*`):
телефонов, Zalo, e-mail и ссылок на профили не найдено. Есть 138 ссылок на посты
Telegram (`t.me/<канал>/<id>`, `listings/telegram/da-nang.jsonl` — 111 и
`nha-trang.jsonl` — 27), и они продублированы во всех HTML. Это посты каналов
агентств, сделанные для публикации, так что риск низкий. Но через ссылку виден автор
поста, и если среди каналов окажется канал частного лица, правило должно это учитывать.

**Остальное содержимое репозитория:**

| Файл / группа | Тип данных | Количество |
|---|---|---|
| `new_listings*.py` (48 партий, № 14–120) | поле `contact` (имя или обращение плюс телефон/Zalo/WhatsApp) | 903 вхождения, 49 уникальных значений |
| `new_listings*.py` | телефоны VN в `contact`/описаниях | 45 вхождений, 40 уникальных |
| `new_listings*.py` (55 партий) | ссылки на посты в группах Facebook (`facebook.com/groups/<g>/posts/<id>`): по ним открывается профиль автора, частного лица | 483 |
| `new_listings*.py` | ссылки на страницы Facebook (не группы) | 131 вхождение, 11 уникальных |
| `new_listings*.py` | упоминания Zalo / @-хэндлы Telegram | 22 (10 уник.) / 18 (5 уник.) |
| `new_listings*.py` | ссылки на посты Telegram | 872 |
| `facebook_ingest_state.json` | ссылки на посты в FB-группах (ключи состояния) | 102 |
| `telegram_ingest_state.json` | ссылки на посты Telegram с категорией решения и датой проверки | 866 |
| `Nha_Trang_6_9mln.pdf`, `Nha_Trang_6_9mln_checkboxes.pdf`, `Nha_Trang_apartments_do_10mln.pdf` | телефоны и Zalo в тексте PDF | 5–6 телефонов в каждом (3 уникальных), 6–8 упоминаний Zalo |
| `legacy/build_pdf.py`, `legacy/build_pdf2.py` | то же, исходники этих PDF | 6 / 5 телефонов (по 3 уникальных), Zalo |
| `airbnb_listings.json` (54 записи) | имена хозяев в `host_or_terms` | ≥ 15 по шаблону «Хозяин: Имя», реально, вероятно, больше |
| `dl_*_full.txt`, `nt_room_full.txt`, `dn_room_full.txt` | сырые выгрузки страниц batdongsan: e-mail и ссылки на соцсети самой площадки | по 4 e-mail (1 уникальный, корпоративный) — риск низкий |
| `assets/fb_photos/` | фотографии из постов частных лиц (на части могут быть люди, номера домов, документы) | 1 709 файлов |

Секретов не найдено: шаблоны Telegram-токенов `\d{8,10}:[\w-]{35}` и
`api_key/secret/password/token = "…"` дали 0 совпадений. `run_pipeline.py` читает
токен из файла вне репозитория. Это сделано правильно и задокументировано.

Инфраструктура: публичные IP серверов (Netcup, Selectel) указаны в
`docs/servercontrol/RENTSEARCHER_NETCUP_PIPELINE.md`,
`server/rentsearcher-pipeline.service` и `run_pipeline.py`. Риск низкий, но эти
адреса в публичном репо не нужны. Ещё есть локальные пути владельца
(`D:\MyDev\…`) в `.claude/launch.json` и `run_pipeline.py`.

### 1.2 Внутренний стейт

- `telegram_ingest_state.json` (139 КБ, 866 записей `{id, cat, hash, checked}`) и
  `facebook_ingest_state.json` (19 КБ, 102 записи). Из них видно, какие посты
  рассматривались и почему отклонены, а у Facebook они ведут на посты частных лиц.
  По `.gitignore` они лежат в репо сознательно: состояние нужно серверу между
  прогонами.
- `posted_dates.json`, `liveness_*cache.json`, `geocode_cache.json`,
  `photos_backfill_cache.json` — кэши. Чувствительного в них нет, но это шум в диффах.
- `server.log` (477 байт, лог локального `http.server`) и
  `daily_*_check_prompt.txt`, `facebook_check_prompt.txt` (инструкции сессий,
  в одной есть ссылка на профиль) тоже лежат в репо.

**Рекомендация:** держать стейт вне публичного репо. Варианты:
(а) каталог `/opt/rentsearcher/state` на сервере плюс резервная копия;
(б) приватный репозиторий или приватная ветка-хранилище;
(в) как минимум хранить вместо URL поста хэш (`sha256(url)`). Для дедупликации
этого достаточно.

### 1.3 Авторские права на фото

| Источник | Как хранится | Риск |
|---|---|---|
| Chợ Tốt (`cdn.chotot.com`, 38 269 URL) | хотлинк, файлов в репо нет | средний: показ чужих фото на своём сайте, условия Chợ Tốt это запрещают. Ссылки, а не копии |
| Telegram (`cdn*.telesco.pe`, 732 URL) | хотлинк | средний: URL временные, в notice прямо сказано, что фото «лежат на серверах Telegram» |
| dotproperty / hoppler (CloudFront, 576 URL) | хотлинк | средний, по тем же причинам |
| **Facebook (`assets/fb_photos/`)** | **копии в публичном репо, 129 МБ** | **высокий**: перепубликация фото частных лиц без разрешения, и это навсегда остаётся в истории git |
| Airbnb (`airbnb_listings.json`) | только текст и URL | низкий для фото, но в тексте есть имена хозяев (см. выше). Живой код файл не читает |

### 1.4 Что сделать (решение за владельцем)

1. Сразу (обычные коммиты, без переписывания истории): убрать из tip
   `assets/fb_photos/` (на фото ничего не ссылается), три PDF, `airbnb_listings.json`,
   `legacy/build_pdf*.py`, сырые выгрузки `*_full.txt`, `*_out.txt`, `*_p1.txt`,
   `server.log`. Партии с `contact` и ссылками на FB перенести в приватное хранилище
   (см. § 2 — сначала исправить нумерацию).
2. Удаление из tip не убирает данные из истории и из форков. Полная очистка: `git
   filter-repo --path assets/fb_photos --path-glob '*.pdf' … --invert-paths`, затем
   force-push (правило `deny` в `.claude/settings.json` запрещает его сессиям Claude,
   делать руками), затем перезапуск клонов на сервере и ПК (`run_on_server.sh` и так
   делает `reset --hard origin/main`) и запрос в GitHub Support на очистку кэшированных
   представлений. Это необратимо, а SHA всех коммитов изменятся.
3. Сборщикам: не сохранять поле `contact` и телефоны в партиях. С № 120 этого уже нет,
   и в листинги поле не попадает. Стоит закрепить это тестом.

---

## 2. Структура: что живое, что архив

### 2.1 Живой пайплайн

Прослежен от `run_pipeline.py` (его запускают `server/run_on_server.sh` и
`run_daily_program.ps1`) и `rebuild_final.py`: транзитивное замыкание по `import`
и по вызовам `[py, "x.py"]`. Получился **31 скрипт**:

- **Ядро / данные:** `rebuild_final.py`, `listing_lock.py`, `allocate_ids.py`,
  `site_data.py`, `amenities.py`
- **Сбор:** `collect_chotot.py`, `collect_batdongsan.py`, `collect_dotproperty.py`,
  `collect_hoppler.py`, `fb_collect.py`, `fetch_telegram_listings.py`,
  `ingest_facebook.py`, `ingest_telegram.py`, `check_repost.py`
- **Обслуживание:** `remove_gone_listings.py`, `remove_gone_web.py`,
  `remove_gone_facebook.py`, `remove_gone_telegram.py`, `fb_liveness_check.py`,
  `purge_old_listings.py`, `check_freshness.py`, `clean_fb_photos.py`,
  `backfill_chotot_coords.py`, `fetch_rates.py`, `repo_sync.py`
- **Карта:** `build_pins_step2_geocode.py`, `build_pins_step3_project.py`,
  `build_leaflet_data.py`
- **Публикация в Telegram (руками):** `post_new_to_telegram.py`,
  `cleanup_telegram_posts.py`
- **Оркестратор:** `run_pipeline.py`

### 2.2 Не вызываются пайплайном, но это инструменты, а не мусор (6)

`backfill_amenities.py`, `backfill_photos.py` (разовые дозаполнения, могут
понадобиться снова), `build_pins_step1_projections.py`, `build_pins_nhatrang.py`
(пересборка проекций и мозаики Нячанга при смене границ), `city_digest.py`,
`find_chat_id.py`. Место им в `tools/`.

### 2.3 Одноразовые, кандидаты в `archive/` (554 файла, ≈58 МБ)

- `new_listings2.py` … `new_listings556.py`: 550 файлов (6 пропусков в нумерации).
  Это уже применённые партии: `insert_listings()` отказывается применять их повторно.
  Код их не читает, кроме двух мест: подсчёта номера следующей партии и
  `check_repost.py --file` для новой партии.
- `new_listings.py` (самая первая партия, ещё на `L(...)` в шаблоне),
  `new_listings9_data.py`, `new_listings10_data.py`.
- `new_listings_template.py` **остаётся**: это шаблон, на него ссылается его
  собственная документация.

**Блокер:** шесть сборщиков (`collect_chotot.py:528`, `collect_batdongsan.py:560`,
`collect_dotproperty.py:347`, `collect_hoppler.py:401`, `ingest_facebook.py:815`,
`ingest_telegram.py:1380`) одинаково считают
`max(glob("new_listings*.py")) + 1`. Если перенести партии, следующая получит
№ 1 и т. д. Ничего не сломается (защита от повторов в `insert_listings` по id и URL),
но имена файлов начнут совпадать с архивными. Прежде чем переносить, нужно вынести
эту логику в одну функцию (например, `listing_lock.next_batch_path()`), которая
смотрит и в `archive/batches/`, или хранит счётчик в файле. Заодно уйдут шесть
копий одного кода.

### 2.4 Данные в корне

| Группа | Размер | Читает живой код? | Куда |
|---|---|---|---|
| `*_overpass.json`, `osm_streets_*.json`, `leaflet_*.json`, `pin_*.json`, `final_pins.json`, `chotot_coords.json`, `geocode_cache.json`, `maps_data.json`, `nt_realtor_map.json` | 19 МБ | да | `data/geo/` |
| `posted_dates.json`, `liveness_*cache.json`, `*_ingest_state.json`, `rates.json` | ≈0,6 МБ | да | `data/state/` (лучше вне репо, § 1.2) |
| `*_full.txt`, `*_out.txt`, `*_p1.txt`, `py_check*.txt`, `raw_batch5.txt`, `dalat_geocode*.txt`, `*_query.txt`, `wards_*.txt`, `new_listings58_body.txt`, `date_check_out.txt` | 1,3 МБ | нет | `archive/raw/` или удалить |
| `nt_realtor_preview*.html`, `map_preview.html`, PDF, `airbnb_listings.json`, `final_data.json`, `nt_old_wards.json`, `nt_neighborhood_geocode*.json`, `photos_backfill_cache.json` | 1,2 МБ | нет (последний читает только `backfill_photos.py`) | `archive/` (PDF и airbnb — вне публичного репо, § 1) |
| 40 сгенерированных `*.html`, `assets/app.*`, `robots.txt`, `sitemap.xml` | 32 МБ | `vietnam-rent-finder.html` читают через `site_data.load_data()` 25 скриптов | `site/` / вне `main` (§ 3) |

### 2.5 Целевая структура

```
rentsearcher/              # пакет (src-раскладка: src/rentsearcher/)
  core/      listing_lock.py, allocate_ids.py, site_data.py, amenities.py, paths.py
  build/     rebuild_final.py (+ шаблон HTML/JS отдельными файлами), build_leaflet_data.py,
             build_pins_step2_geocode.py, build_pins_step3_project.py
  collect/   collect_*.py, fb_collect.py, fetch_telegram_listings.py, ingest_*.py, check_repost.py
  maintain/  remove_gone_*.py, fb_liveness_check.py, purge_old_listings.py, check_freshness.py,
             clean_fb_photos.py, backfill_chotot_coords.py, fetch_rates.py, repo_sync.py
  publish/   post_new_to_telegram.py, cleanup_telegram_posts.py
scripts/     run_pipeline.py, run_daily_*.ps1, server/ (unit, timer, run_on_server.sh)
tools/       backfill_*.py, build_pins_step1_projections.py, build_pins_nhatrang.py,
             city_digest.py, find_chat_id.py, new_listings_template.py
data/
  listings/<source>/<city>.jsonl
  geo/       overpass, osm_streets, leaflet_*, pins, maps_data, nt_realtor_map
  state/     posted_dates, liveness caches, rates  (ingest-состояния — вне публичного репо)
site/        результат сборки — не в main (§ 3)
archive/
  batches/   new_listingsN.py (или приватное хранилище, § 1)
  raw/       сырые выгрузки
legacy/      как сейчас
tests/
docs/
```

**Порядок миграции.** Всё сейчас работает относительно cwd и запускает соседей по
имени файла, так что переносить за один раз нельзя:

1. `next_batch_path()` (§ 2.3), затем `git mv new_listings[0-9]*.py archive/batches/`.
   Риск минимальный, корень уменьшится с 735 до ≈180 записей.
2. `archive/raw/` для сырых выгрузок и превью (код их не читает).
3. Модуль `paths.py` с константами (`DATA_DIR`, `GEO_DIR`, `STATE_DIR`, `SITE_DIR`).
   Каждый скрипт переводится на него отдельным коммитом, и после каждого шага
   прогоняется `pytest` плюс `run_pipeline.py --dry-run`.
4. Только после этого — пакет, `python -m rentsearcher.…` в `run_pipeline.py` и
   в хуке `.claude/hooks/rebuild-on-listings-change.sh` (он сейчас смотрит на имена
   `rebuild_final.py` и `new_listings*.py`).

---

## 3. Размер репозитория

### 3.1 Что занимает место

На tip (рабочее дерево — 256 МБ, `.git` мелкого клона — 286 МБ):

| Что | На tip | В `.git` за 50 коммитов (20 дней), сжато |
|---|---|---|
| `assets/fb_photos/` (webp) | 129 МБ | 126 МБ (webp не сжимается и не дельтуется) |
| сгенерированные `*.html` | 32 МБ | 81 МБ (1 643 блоба; ≈4 МБ/день) |
| `listings/*.jsonl` | 16 МБ | 66 МБ (719 блобов) |
| `new_listings*.py` | 58 МБ | 19 МБ |
| `*.json` (гео, кэши, стейт) | 20 МБ | 6 МБ |

Рост ≈7 МБ в сутки при двух прогонах: HTML плюс jsonl. Это около 2,5 ГБ в год,
а мягкий лимит GitHub на репозиторий — 1–5 ГБ. jsonl растут быстрее, чем можно
было бы ожидать. Стоит проверить на полном клоне (`git count-objects -vH` после
`git gc --aggressive`), не переписываются ли файлы городов целиком на каждый
прогон.

### 3.2 Варианты

Сайт публикуется через GitHub Pages из `main` (`SITE_ROOT =
https://tottorisun.github.io/RentSearcherViet/`), поэтому HTML и `assets/` сейчас
обязаны лежать в git.

| Вариант | Экономия | Цена / подводные камни |
|---|---|---|
| **A. Удалить `assets/fb_photos/` из tip** (фото не используются) | −129 МБ checkout сразу; история — только с `filter-repo` | Прежде проверить, что FB-строки не вернутся. Если вернутся — см. C |
| **B. Сборка сайта в GitHub Actions + `actions/deploy-pages`**: `main` хранит только `listings/` и код, HTML не коммитится | −32 МБ на tip, −≈4 МБ/день роста (≈1,4 ГБ/год) | 25 скриптов читают данные из `vietnam-rent-finder.html` через `site_data.load_data()`. Её нужно перевести на `listing_lock.load_page_rows()` плюс `template_cities()` (или писать рядом `site/data.json`). Шаги карты (`build_pins_*`, `build_leaflet_data`) нужно перенести в CI или коммитить только их json |
| **B′. Ветка `gh-pages` с одним коммитом** (orphan, `push --force` после каждой сборки) | те же −≈4 МБ/день; история `main` чистая | Скрипты по-прежнему читают HTML локально (без изменений в коде). Нужен force-push из серверного прогона, и запрет `git push --force*` в `.claude/settings.json` должен остаться только для сессий |
| **C. Фото — во внешнее хранилище** (Cloudflare R2 / Backblaze B2 + CDN, или вообще не перезаливать, а ссылаться, как с Chợ Tốt) | −129 МБ и весь будущий рост фото | Нужен ключ хранилища на ПК/сервере. Юридически вариант «не хранить» лучше любого хостинга |
| **D. Git LFS для фото** | checkout меньше | **Не подходит:** GitHub Pages не отдаёт LFS-объекты (на сайт попадут файлы-указатели), бесплатная квота — 1 ГБ хранения и 1 ГБ трафика в месяц. Права и ПДн LFS не решает |
| **E. `archive/batches` вне репо** (release-ассет / приватный репо) | −58 МБ на tip | Сначала § 2.3 |
| **F. Переписать историю** (`git filter-repo` для fb_photos, PDF, старых HTML) | `.git` уменьшится в разы | Необратимо, force-push, пересоздание клонов на сервере и ПК, форки сохранят старое |

**Рекомендуемый порядок:** A + C (решение по фото), затем B′ как быстрый способ
остановить рост, затем B, когда `site_data` перестанет зависеть от HTML, затем F
(разово, после A–B, вместе с очисткой ПДн из § 1).

---

## 4. Пайплайн: тесты и CI (сделано в этой ветке)

### 4.1 Что добавлено

- `tests/conftest.py`: фикстуры. Каждый тест работает во временном каталоге и
  в рабочие файлы проекта не пишет. Шаблон `rebuild_final.py` читается по
  абсолютному пути.
- `tests/test_listing_lock.py`, 22 теста:
  - хранение: раскладка по `<source>/<city>.jsonl`, порядок `(seq, id)`, LF, UTF-8 без экранирования;
  - `save_rows`: отказ на повторных id, удаление опустевшего файла, неизменный файл не переписывается;
  - `load_rows`: битая строка; `load_page_rows` убирает `seq`/`postedOn` и отказывается собирать пустой сайт;
  - `row_anchor` и `with_current_age` (приоритет `posted_dates.json`, даты из будущего);
  - `insert_listings`: `seq` в конец, `postedOn` по `daysAgo`, отказ на повторной партии, на известном URL (в том числе с `?query`), на расхождении объявленных id, на не-литералах; исключение для общих URL Telegram;
  - `remove_listings`;
  - блокировка: снимается при исключении, таймаут при живом чужом замке, перехват протухшего.
- `tests/test_rebuild_final.py`, 20 тестов:
  - `_ru_days_label` (9 случаев склонения) и `L()`;
  - сборка в изолированной копии: все выходные файлы, плейсхолдеры подставлены, строки на странице;
  - сборка отказывает и ничего не пишет при неизвестном районе, источнике, валюте, при пустом `descEn`, несовпадении `posted`/`daysAgo`, недопустимом типе, повторном id в разных файлах, пустом `listings/`;
  - **полная сборка на настоящих `listings/` репозитория** (≈3 с). Это та же проверка, что делает PostToolUse-хук, только теперь она идёт и в CI.
- `pytest.ini` (`testpaths = tests`: импорт любого скрипта из корня уже является действием), `requirements-dev.txt` (`pytest==8.3.5`).
- `.github/workflows/ci.yml`: новый job `tests` рядом с `compile-check`.

Локально: `python -m pip install -r requirements-dev.txt && python -m pytest`,
42 passed за ≈4 с (Python 3.13). CI использует 3.11.

### 4.2 Что нашли тесты

- **Неизвестные `cur` и `source` не доходят до `check_listings`.** Сборка падает
  раньше: `KeyError` в `_to_base()` (`rebuild_final.py:346`) и `ValueError` при
  сортировке `_SOURCES_BY_CITY` (`rebuild_final.py:838`). Это сырой traceback вместо
  подготовленного сообщения «add it to rates.json / SOURCES», так что эти две ветки
  `check_listings` фактически мёртвые. Сайт при этом не пишется, то есть отказ
  безопасный. Исправление: вызывать `check_listings(LISTINGS, CITIES)` сразу после
  `load_page_rows()`. Тесты закрепляют текущее поведение («не пишется») и после
  исправления сообщения проверять не мешают.
- `rebuild_final.py` — скрипт без `main()`: сборка идёт при импорте. Чтобы тестировать
  дешевле, стоит обернуть хвост в `main()`. Тогда функции импортировались бы
  напрямую, а не через `ast`.

### 4.3 Следующие шаги

1. Тест для `allocate_ids.py` (параллельная выдача id) и для `next_batch_path()` (§ 2.3).
2. Тест-«сторож» ПДн: ни в одной строке `listings/` нет телефона, `contact`,
   `zalo.me`, `facebook.com/…/posts`.
3. Обновить README: сейчас там 9 строк и написано «тестов нет». Нужен раздел
   «как запустить тесты» и карта пайплайна из § 2.1.
4. Хук `.claude/hooks/rebuild-on-listings-change.sh` пересобирает сайт в рабочем
   каталоге. Можно добавить в него `pytest -q tests/test_listing_lock.py` (< 1 с).
