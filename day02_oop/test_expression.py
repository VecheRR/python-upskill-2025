import pytest
from expression_class import Expression

@pytest.mark.parametrize("expr, result", [
    ("2+2", 4),
    ("3 * (4 - 1)", 9),
])
def test_evaluate(expr, result):
    assert Expression(expr).evaluate() == result

@pytest.mark.parametrize("expr", ["2++2", "hello", "5//2"])
def test_invalid(expr):
    assert not Expression.is_valid(expr)

def test_from_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2+3")
    exp = Expression.from_input()
    assert isinstance(exp, Expression)
    assert exp.text == "2+3"