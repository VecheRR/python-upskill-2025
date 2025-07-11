import sqlite3

SQL = """
INSERT INTO expenses (title, amount, category, date)
VALUES (?, ?, ?, ?)
"""

def main() -> None:
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    data = ("Продукты", 1500.00, "Еда", "2025-07-09")

    # Вставляем данные в таблицу expenses
    cursor.execute(SQL, data)
    conn.commit()

    # Чтение
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    # for row in rows:
    #     print(row)

    # Пример использования функции для выборки по категории
    category = "Еда"
    expenses_by_category = select_by_category(category, cursor)
    print(f"Расходы в категории '{category}':")
    for expense in expenses_by_category:
        print(expense)

    conn.close()

def select_by_category(category: str, cursor) -> list:
    SQL = "SELECT * FROM expenses WHERE category = ?"
    cursor.execute(SQL, (category,))
    return cursor.fetchall()

if __name__ == "__main__":  # pragma: no cover
    main()