# RentSearcher: суточный прогон на Netcup

Статус: `COMPLETE` — с 11.09.2026 сайт собирает и публикует Netcup; ПК собирает
только кандидатов Facebook и Telegram.
Owner-проект: Rent Searcher. Исполнено сессией Claude (основной инженер) по
прямой команде владельца 11.09.2026: «у нас есть неткап и селектал, выбирай сам,
посмотри что да как». Запись для ServerControl — источника правды по серверам.

## Зачем

Компьютер владельца ночью выключен, а суточный прогон шёл только на нём
(планировщик Windows, 09:00 и 21:00, с догоном пропущенного). Сайт обновлялся,
лишь когда компьютер включён.

## Выбор: Netcup, не Selectel

Проверено 11.09.2026 запросами с обоих серверов (коды ответа):

| | Netcup 188.68.56.188 (DE) | Selectel 135.106.161.64 (RU) |
|---|---|---|
| gateway.chotot.com | 200 | 200 |
| t.me (каналы) | 200 | таймаут 25 с |
| dotproperty.com.ph | 200 | 403 |
| hoppler.com.ph | 200 | 200 |
| nominatim.openstreetmap.org | 200 | 200 |
| github.com | 200 | 200 |
| api.telegram.org (оповещения) | 302 | таймаут 25 с |

Selectel отпадает сразу по трём пунктам. К тому же это общий клиентский продакшн,
где сборки запрещены правилами (`AI_CONTEXT/INFRASTRUCTURE/SERVERS.md`), а
прогон по сути и есть сборка сайта.

Риск Netcup — теснота: 1 vCPU, 967 МБ памяти, свободно ~430 МБ, подкачка 2 ГБ,
давление на память 0. На нём VPN владельца (Xray за nginx stream на 443) и сайты
apart/book/softapk.sunarrow.ru и sunarrow.ru. Пик памяти прогона измерен
локально по счётчику Windows PeakWorkingSetSize: `rebuild_final.py` 182 МБ,
`build_leaflet_data.py` 108 МБ, `build_pins_step2_geocode.py` 61 МБ,
`build_pins_step3_project.py` 57 МБ. Шаги идут по очереди.

## Что где идёт

- **Сервер:** Chợ Tốt, dotproperty, hoppler, обслуживание (снятые, чистка по
  возрасту, курсы, координаты), карта, сборка, публикация (git push).
- **ПК владельца** (`run_pipeline.py --candidates-only`): группы Facebook — только
  там, потому что программа ходит под личным аккаунтом владельца, а вход с адреса
  дата-центра — типичный повод для проверки личности или блокировки; и каналы
  Telegram — их кандидатов разбирает сессия на том же ПК. Ничего не публикует.

## Что создано на Netcup

- системный пользователь `rentsearcher` (uid 995), shell `/usr/sbin/nologin`,
  домашний каталог `/opt/rentsearcher` (права 750);
- `/opt/rentsearcher/app` — клон `Tottorisun/RentSearcherViet`;
- `/opt/rentsearcher/.ssh/id_ed25519` — ключ этого сервера для деплоя
  (`SHA256:5bYfgPlXy47oEmR0xj9ylInDfHScY39A968VLzojwro`), права 600;
  `known_hosts` — ключ github.com, отпечаток сверен с опубликованным GitHub;
- `/opt/rentsearcher/.gelios/token` — токен бота оповещений, права 600,
  перенесён с ПК через stdin, нигде не напечатан;
- `/opt/rentsearcher/pipeline.env` — `GELIOS_TOKEN_FILE`, `GELIOS_CHAT_ID`
  (права 640, root:rentsearcher);
- `PIPELINE_TIMEOUT_SCALE=2` в том же файле — множитель пределов шагов;
- `/etc/systemd/system/rentsearcher-pipeline.service` и `.timer` — копии из
  `server/` репозитория, таймер включён;
- на GitHub — deploy key «Netcup rentsearcher pipeline (write)», id 162986509,
  только для репозитория RentSearcherViet.

Ничего не изменено в nginx, Xray, UFW, SSH, DNS, чужих каталогах и службах.

## Пределы службы

`MemoryHigh=300M`, `MemoryMax=400M`, `MemorySwapMax=200M`, `CPUQuota=60%`,
`Nice=19`, `IOSchedulingClass=idle`, `TimeoutStartSec=2h`. Если прогон
когда-нибудь разрастётся, ядро остановит его, а не Xray.

## Откат

```sh
systemctl disable --now rentsearcher-pipeline.timer
rm -f /etc/systemd/system/rentsearcher-pipeline.service /etc/systemd/system/rentsearcher-pipeline.timer
systemctl daemon-reload
userdel -r rentsearcher          # удаляет /opt/rentsearcher целиком
gh repo deploy-key delete <id> --repo Tottorisun/RentSearcherViet
```
На ПК вернуть `run_daily_program.ps1` к `run_pipeline.py --publish`.

## Evidence (11.09.2026)

- **Пробный прогон без публикации** (временная служба `rentsearcher-dryrun` с
  теми же пределами): 14:37–15:15 CEST, 14 шагов из 14, сбоев нет. CPU 4 мин
  32 с. Пик памяти группы 300,2 МБ — ровно `MemoryHigh`: на нём ядро придержало
  кэш файлов, подкачки ушло 3,6 МБ, до `MemoryMax` не дошло. Длительности
  (предел): Chợ Tốt 485 с (900), dotproperty 787 с (2400), hoppler 433 с (2400),
  Telegram 131 с (900), снятые с Chợ Tốt 217 с (2400), снятые на порталах 173 с
  (1800); сборка и карта — меньше 30 с. На ПК те же шаги идут в 1,8–2 раза
  быстрее: сервер в Германии, источники во Вьетнаме и на Филиппинах. Отсюда
  `PIPELINE_TIMEOUT_SCALE=2`.
- **Первый прогон с публикацией** (`rentsearcher-pipeline.service`):
  15:19–15:55 CEST, 13 шагов из 13 (Telegram на сервере не идёт), опубликован
  `168454b` «Автоматический прогон 2026-09-11» от «RentSearcher (Netcup)». CPU
  4 мин 22 с, пик 300,2 МБ, подкачка 17,4 МБ. GitHub Pages после выкладки:
  «Более 2864 объявлений» (до прогона было 2687).
- **Ключ деплоя**: отпечаток на GitHub совпадает с ключом сервера
  (`SHA256:5bYf…`); `git push --dry-run` — «Everything up-to-date», затем
  настоящий пуш `168454b`.
- **Оповещение с сервера** (`run_pipeline.telegram_direct`): «отправлено в
  Telegram» — владельцу пришло одно тестовое сообщение с пометкой «[сервер]».
- **Соседи во время прогона**: xray, nginx, sunarrow-cms — `active`;
  sunarrow.ru 200, book.sunarrow.ru 200, apart.sunarrow.ru/health/live 200
  (голый корень apart отдаёт 404 — это норма, см.
  `ServerControl/operations/taskboard/infraStatus.mjs`); давление на память 0;
  fail2ban забанил только постороннего сканера.
- **Таймер**: включён, ближайший запуск 00:06 CEST (05:06 по Вьетнаму, разброс
  до 10 минут).
- **Обрыв SSH** на время ожидания («Connection reset by peer») — не сервер: ПК
  владельца ушёл в сон в 20:20 по Вьетнаму и проснулся в 21:28 (Kernel-Power
  id 42, Power-Troubleshooter id 1). Тем же сном пропущена задача ПК в 21:00 —
  ровно та причина, ради которой прогон и переехал на сервер.
