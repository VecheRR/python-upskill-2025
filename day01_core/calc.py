def string_calc(expression: str) -> float:
    """
    Evaluate a mathematical expression given as a string.
    
    Args:
        expression (str): A string containing a mathematical expression.
        
    Returns:
        float: The result of the evaluated expression.
        
    Raises:
        ValueError: If the expression is invalid.
    """
    try:
        return eval(expression, {"__builtins__": None}, {})
    except Exception as e:
        raise ValueError(f"Invalid expression: {expression}") from e
    
if __name__ == "__main__": # pragma: no cover    
    expr = input("Enter a mathematical expression: ")
    try:
        result = string_calc(expr)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")