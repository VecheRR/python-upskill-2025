import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from day04_sql_orm.models import Expense, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import date

# 🔧 Создаем тестовую in-memory SQLite базу
engine = create_engine('sqlite:///:memory:', echo=False)
Base.metadata.create_all(engine)  # 🧱 Создаем таблицы

def test_create_expense():
    Session = sessionmaker(bind=engine)
    session = Session()

    new_expenses = [
        Expense(title="Кино", amount=800.0, category="Развлечения", date=date.today()),
        Expense(title="Проезд", amount=55.0, category="Транспорт", date=date.today()),
        Expense(title="Кофе", amount=320.0, category="Еда", date=date.today()),
    ]

    session.add_all(new_expenses)
    session.commit()

    expenses = session.query(Expense).all()
    assert len(expenses) == 3

    # отобрать только "Еда"
    expenses = session.query(Expense).filter_by(category="Еда").all()
    assert len(expenses) == 1

    expenses = session.query(Expense).order_by(Expense.amount.desc()).all()
    assert expenses[0].amount == 800.0

    coffee = session.query(Expense).filter_by(title="Кофе").first()
    coffee.amount = 999.0
    session.commit()
    assert session.query(Expense).filter_by(title="Кофе").first().amount == 999.0

    session.query(Expense).filter_by(category="Транспорт").delete()
    session.commit()
    assert session.query(Expense).filter_by(category="Транспорт").count() == 0