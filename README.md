# Прокачка Python — 2025

> **Репозиторий-дневник моей Python-прокачки.** Каждый день — новая тема, ветка, проект или задачи. Цель — освежить и углубить знания, собрать pet-проекты для портфолио и показать прогресс в публичном виде.

---

## 🎯 Цели

1. **Повторить** ключевые концепции Python, ООП, SQL, API и т.д.
2. **Углубить** знания: тестирование, Docker, REST, ORM, CI.
3. **Разработать** полноценный pet-проект.
4. **Собрать опыт** для резюме, собеседований и стажировок.

---

## 🗓️ План

| День | Ветка (feature/…) | Темы                              | Статус |
| :--: | :---------------- | :-------------------------------- | :----: |
|  1   | `core-basics`     | Основы Python, исключения         |   ✅   |
|  2   | `oop-files`       | ООП, работа с файлами, JSON/CSV   |   ✅   |
|  3   | `api-requests`    | Git flow, `requests`, внешние API |   ✅   |
|  4   | `sql-orm`         | SQLite, SQL, SQLAlchemy ORM       |   ✅   |
|  5   | `tests-linters`   | pytest, flake8, black, типизация  |   ✅   |
|  6   | `flask-crud`      | Flask, REST API (ToDo-приложение) |   ⬜   |
|  7   | `docker-ci`       | Docker, GitHub Actions, CI        |   ⬜   |
|  8   | `url-shortener`   | Мини-сервис: укорачиватель ссылок |   ⬜   |

---

## 🗂 Структура репозитория

```
python-upskill-2025/
├─ day01_core/
│   ├─ calc.py
│   ├─ try_except.py
│   └─ test_calc.py
├─ day02_oop/
│   ├─ expression.py
│   ├─ expression_class.py
│   └─ test_expression.py
├─ day03_git_api/
│   └─ weather_api.py
├─ day04_sql_orm/
│   ├─ db_init.py
│   ├─ raw_sql.py
│   ├─ models.py
│   └─ orm_demo.py
├─ day05_tests/
│   ├─ test_core.py
│   ├─ test_utils.py
│   └─ ...
├─ requirements.txt
└─ README.md
```

---

## 🚀 Быстрый старт

```bash
# Клонировать и запустить (Python 3.11+)
git clone https://github.com/VecheRR/python-upskill-2025.git
cd python-upskill-2025
python day01_core/calc.py
```

### Docker (после дня 7)

```bash
docker build -t upskill .
docker run -p 8000:8000 upskill
```

---

## 🤝 Git Flow

- Ветка `main` защищена, мерж через Pull Request
- Новая тема → новая ветка `feature/<тема>`
- Коммиты по Conventional Commits: `feat:`, `fix:`, `docs:` и т.д.
- Использую squash merge — история проекта чистая и логичная

---

### 💡 Conventional Commits

**📌 Формат:**

```
<тип>(опционально: область): краткое описание изменений
```

**🔧 Примеры:**

- `feat: добавил форму авторизации`
- `fix(api): исправил баг с GET-запросом`
- `docs(readme): обновил инструкцию запуска`
- `style: форматирование кода по PEP8`
- `refactor: вынес бизнес-логику в отдельный модуль`
- `test: добавил юнит-тесты для функций`
- `chore: обновил зависимости и .gitignore`

**🔥 Основные типы:**

| Тип        | Назначение                                      |
| ---------- | ----------------------------------------------- |
| `feat`     | Добавление новой функциональности               |
| `fix`      | Исправление ошибок                              |
| `docs`     | Работа с документацией                          |
| `style`    | Изменения в форматировании кода, пробелы и т.п. |
| `refactor` | Рефакторинг кода (без изменений поведения)      |
| `test`     | Добавление или изменение тестов                 |
| `chore`    | Служебные изменения (CI, зависимости и т.д.)    |

---

## ✔️ Чек-лист качества

- [x] PEP 8 (`flake8`, `black`)
- [x] Статическая типизация (`mypy`)
- [x] Тесты (`pytest`)
- [ ] Докстроки (Google style)
- [ ] CI (GitHub Actions)

---

## 🔗 Полезные ссылки

- [Python 3.11 Docs](https://docs.python.org/3/)
- [PEP 8](https://peps.python.org/pep-0008/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Flask](https://flask.palletsprojects.com/)
- [pytest](https://docs.pytest.org/)
- [Docker](https://docs.docker.com/)

---

## 👤 Обо мне

**Влад @VecheRR** — Python-разработчик

- 🎓 Выпускник МТУСИ (2025), специальность «Прикладная информатика в экономике»
- 📍 Москва
- 🧠 Увлекаюсь backend-разработкой, автоматизацией, REST API, аналитикой и CI/CD
- 🛠 Опыт с Django, Flask, SQLAlchemy, PostgreSQL, Git, Docker и др.
- 🔎 Ищу стажировку / работу в области Python-разработки
- 💼 Этот репозиторий — часть моего карьерного трека. Здесь мой подход, дисциплина и реальный код, который можно использовать и расширять.
