# Rent Searcher Viet

Агрегатор объявлений об аренде жилья во Вьетнаме (Нячанг, Далат, Дананг, Хойан, Вунгтау, Куинён, Фантьет/Муйне, Хошимин) — единая статическая страница `vietnam-rent-finder.html`, собираемая шаблоном `rebuild_final.py` из строк объявлений в `listings/<источник>/<город>.jsonl` (с 17.09.2026; заводятся и снимаются только через `listing_lock.py`).

Опубликовано: https://claude.ai/code/artifact/be6f5e7f-84a1-466a-8444-ffac55d827cf

## Автоматизация Claude Code

24.08.2026: добавлен PostToolUse-хук (`.claude/settings.json`) — после правки `rebuild_final.py` или любого `new_listingsN.py` он сам запускает `python rebuild_final.py` и показывает успех/ошибку. Пока это единственная страховка для пайплайна, тестов нет.
