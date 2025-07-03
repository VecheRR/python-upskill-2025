from __future__ import annotations

class Expression:
    def __init__(self, text: str):
        self.text = text.strip()

    # Simple method
    def evaluate(self) -> float:
        try:
            return eval(self.text, {"__builtins__": None}, {})
        except Exception as e:
            raise ValueError(f"Invalid expression: {self.text}") from e
        
    # Classmethod
    @classmethod
    def from_input(cls) -> Expression:
        user_text = input("Enter a mathematical expression: ")
        return cls(user_text)
    
    @staticmethod
    def is_valid(expr: str) -> bool:
        import re
        _invalid_ops = re.compile(r"[+\-*/]{2,}") # два и более операторов подряд
        _allowed = re.compile(r"^[0-9+\-*/(). ]+$") # только допустимые символы
        expr = expr.strip()
        return bool(_allowed.match(expr) and not _invalid_ops.search(expr))
    
    # Dunder for string representation
    def __str__(self) -> str:
        return f"Expression({self.text})"

    def __repr__(self) -> str:
        return f"Expression(text={self.text!r})"
        

if __name__ == "__main__":  # pragma: no cover
    expr = Expression.from_input()
    if not Expression.is_valid(expr.text):
        print("Недопустимое выражение 😔")
    else:
        print("Результат:", expr.evaluate())