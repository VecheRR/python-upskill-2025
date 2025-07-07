# Прокачка Python — 2025

> **Репозиторий-дневник моей недельной прокачки навыков Python.** Каждый день — одна тема, отдельная ветка и мини-проект или задачи. Цель — освежить знания, закрыть пробелы и оставить публичный трек, который ляжет в резюме и pet-проекты.

---

## 🎯 Цели

1. **Повторить** ключевые основы Python и инструменты.
2. **Углубить** знания: Git flow, requests, SQL и ORM, Flask, тесты, Docker.
3. **Зафиксировать** прогресс публично: коммиты, pull request’ы, чек-листы.
4. **Подготовить базу** для pet-проектов и блока «Опыт» в резюме.

---

## 🗓️ План на неделю

| День | Ветка (feature/…) | Темы                              | Статус |
| :--: | :---------------- | :-------------------------------- | :----: |
|  1   | `core-basics`     | Основы Python, исключения         |   ✅   |
|  2   | `oop-files`       | ООП, работа с файлами, JSON/CSV   |   ✅   |
|  3   | `api-requests`    | Git flow, `requests`, внешние API |   ✅   |
|  4   | `sql-orm`         | SQL, SQLite, SQLAlchemy ORM       |   ⬜   |
|  5   | `flask-todo`      | Flask, REST API (CRUD ToDo)       |   ⬜   |
|  6   | `tests-docker`    | pytest, линтеры, Docker           |   ⬜   |
|  7   | `final-review`    | Финал: CI, рефактор, README       |   ⬜   |

_Статусы обновляются после слияния PR в `main`._

---

## 🗂 Структура репозитория

```text
python-upskill-2025/
├─ day01_core/
│   ├─ calc.py
│   ├─ test_calc.py
│   └─ try_except.py
├─ day02_oop/
│   ├─ expression_class.py
│   ├─ expression.py
│   └─ test_expression.py
├─ day03_git_api/
│   └─ weather_api.py
├─ requirements.txt
└─ README.md
```

Каждый день → отдельная папка, отдельная ветка, отдельный pull-request.

---

## 🚀 Быстрый старт

```bash
# Клонировать и запустить пример (Python 3.11+)
$ git clone https://github.com/VecheRR/python-upskill-2025.git
$ cd python-upskill-2025
$ python day01_core/calc.py
```

### Docker (после дня 6)

```bash
$ docker build -t upskill .
$ docker run -p 8000:8000 upskill
```

---

## 🤝 Git flow

1. Ветка `main` защищена — мерж только через PR
2. Одна фича-ветка на одну тему (`feature/<тема>`)
3. Коммиты в стиле Conventional commits (`feat:`, `fix:`, `docs:` ...)
4. Шаблон PR появится в `.github` после дня 2
5. Использую squash merge — история чистая

---

## ✔️ Чек-лист качества

- [ ] PEP 8 (`flake8`, `black`)
- [ ] Статическая типизация (`mypy`)
- [x] Тесты (`pytest`)
- [ ] Докстроки (Google style)
- [ ] CI — GitHub Actions (на 6 день)

---

## 🔗 Полезные ссылки

- [Документация Python 3.11](https://docs.python.org/3/)
- [PEP 8 (стилистика кода)](https://peps.python.org/pep-0008/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [pytest](https://docs.pytest.org/)

---

## 👤 Автор

| Влад @VecheRR          | Junior Python разработчик |
| :--------------------- | :------------------------ |
| Москва · студент МТУСИ | Качаю железо и пишу код   |

> «Качаю мышцы и код одновременно» 💪🐍
