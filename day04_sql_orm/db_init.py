import sqlite3

SQL = """
CREATE TABLE IF NOT EXISTS expenses (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    title    TEXT    NOT NULL,
    amount   REAL    NOT NULL,
    category TEXT,
    date     TEXT    NOT NULL   -- ISO-строка 2025-07-08
);
"""

def main() -> None:
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute(SQL)
    conn.commit()
    conn.close()
    print("База данных expenses.db и таблица expenses созданы.")

if __name__ == "__main__":  # pragma: no cover
    main()
    
# Этот файл создаёт базу данных expenses.db и таблицу expenses.
# Запустите его один раз перед началом работы с приложением.
# После этого база данных будет использоваться в других модулях.