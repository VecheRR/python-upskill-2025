from models import Expense, engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from sqlalchemy import desc

Session = sessionmaker(bind=engine)
session = Session()

new_expenses = [
    Expense(title="Кино", amount=800.0, category="Развлечения", date=date(2025, 7, 10)),
    Expense(title="Проезд", amount=55.0, category="Транспорт", date=date(2025, 7, 10)),
    Expense(title="Кофе", amount=320.0, category="Еда", date=date(2025, 7, 11)),
]

session.add_all(new_expenses)
session.commit()

expenses = session.query(Expense).all()

for expense in expenses:
    print(f"ID: {expense.id}, Title: {expense.title}, Amount: {expense.amount}, "
          f"Category: {expense.category}, Date: {expense.date}")
    
# 1. Все расходы в категории "Еда"
print("\n🍏 Расходы в категории 'Еда':")
food_expenses = session.query(Expense).filter(Expense.category == "Еда").all()
for e in food_expenses:
    print(f"- {e.title}: {e.amount} руб. на {e.date}")

# 2. Все траты больше 1000 рублей, отсортированные по убыванию суммы
print("\n💸 Расходы дороже 1000 руб:")
big_expenses = session.query(Expense).filter(Expense.amount > 1000).order_by(desc(Expense.amount)).all()
for e in big_expenses:
    print(f"- {e.title}: {e.amount} руб. ({e.category})")

# 3. Обновление суммы для "Кофе"
print("\n🔄 Обновление суммы для 'Кофе'")
coffee_expense = session.query(Expense).filter_by(title="Кофе").first()
if coffee_expense:
    coffee_expense.amount = 450.0
    session.commit()
    print(f"Обновлено: {coffee_expense.title} теперь {coffee_expense.amount} руб.")
else:
    print("Не найдено")

print("\n🗑 Удаляем все 'Развлечения'")
deleted = session.query(Expense).filter_by(category="Развлечения").delete()
session.commit()
print(f"Удалено {deleted} записей.")

expenses = session.query(Expense).all()

for expense in expenses:
    print(f"ID: {expense.id}, Title: {expense.title}, Amount: {expense.amount}, "
          f"Category: {expense.category}, Date: {expense.date}")

session.close()

