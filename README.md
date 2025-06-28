# Python Upskill 2025

Python Upskill 2025

Коротко: репозиторий-дневник моего недельного апгрейда навыков Python. Каждый день — новая тема, отдельная ветка и мини-проект/задачи. Итог — готовые примеры кода, тесты, Docker-сборки и база для pet-проектов и резюме.

⸻

🎯 Цели 1. Повторить основы Python и смежные инструменты без «пролётов» в знаниях. 2. Подтянуть пробелы (Git-flow, тесты, Docker, ORM, Flask). 3. Зафиксировать прогресс публично: коммиты, PR, ревью, чек-листы. 4. Подготовить базу для последующих pet-проектов и раздела «Опыт» в резюме.

⸻

🗓️ План на неделю

День Ветка Темы Статус
1 feature/core-basics Core Python, исключения, задачи 🔄
2 feature/oop-files ООП, работа с файлами, JSON/CSV ⏳
3 feature/api-requests Git-flow, requests, внешние API ⏳
4 feature/sql-orm SQL, SQLite, SQLAlchemy ORM ⏳
5 feature/flask-todo Flask, REST API (CRUD ToDo) ⏳
6 feature/tests-docker pytest, линтеры, Docker images ⏳
7 feature/final-review Рефакторинг, итоги, README update ⏳

Обновляю таблицу чек-марками после слияния каждого PR.

⸻

🗂️ Структура репозитория

python-upskill-2025/
├─ day01_core/ # упражнения и мини-проекты Дня 1
│ ├─ calc.py
│ └─ exceptions_demo.py
├─ day02_oop/
│ └─ ...
├─ day03_git_api/
│ └─ ...
├─ requirements.txt # (появится после Дня 5)
└─ README.md

Каждый день — своя папка, своя ветка, отдельный PR.

⸻

🚀 Быстрый старт

# Клонировать репо

$ git clone https://github.com/<username>/python-upskill-2025.git
$ cd python-upskill-2025

# Запустить любой пример (Python 3.11+)

$ python day01_core/calc.py

Docker

После Дня 6 будет доступен образ для беглого запуска Flask-API и тестов.

$ docker build -t upskill .
$ docker run -p 8000:8000 upskill

⸻

🤝 Git-flow & PR 1. main — защищённая ветка, только через PR. 2. Фича-ветка = тема дня (feature/<topic>). 3. Коммиты в стиле Conventional Commits (feat:, fix:, docs: …). 4. PR-шаблон автоматически предлагает чек-лист (добавлю в .github после Дня 2). 5. После ревью — squash merge, чтобы история была чистой.

⸻

📋 Чек-лист качества кода
• PEP 8 (flake8, black).
• Типизация (mypy).
• Тесты (pytest).
• Док-строки (Google style).
• CI — GitHub Actions (после Дня 6).

⸻

💡 Полезные ссылки
• Python Docs 3.11 → https://docs.python.org/3/
• PEP 8 → https://peps.python.org/pep-0008/
• Flask → https://flask.palletsprojects.com/
• SQLAlchemy → https://docs.sqlalchemy.org/
• pytest → https://docs.pytest.org/

⸻

Автор

Влад (21 y.o.) Junior Python Enthusiast
Из Москвы, учусь в МТУСИ. Люблю pet-проекты и тяжёлую штангу.

«Качаю мышцы и код одновременно» 💪🐍
