class Expression:
    def __init__(self, expression: str):
        self.expression = expression.strip()

    def evaluate(self) -> float:
        try:
            return eval(self.expression, {"__builtins__": None}, {})
        except Exception as e:
            raise ValueError(f"Invalid expression: {self.expression}") from e

    def __str__(self):
        return f"Expression({self.expression})"
    
expr = Expression("2 + 3 * 4")
print(expr)
print(f"Result: {expr.evaluate()}")