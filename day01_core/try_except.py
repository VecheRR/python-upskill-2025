class MyDivisionError(Exception):
    """Custom exception for zero division error."""
    pass

def safe_div(a, b):
    """Safely divide two numbers, raising MyDivisionError if division by zero is attempted."""
    if b == 0:
        raise MyDivisionError("Division by zero is not allowed.")
    return a / b

a = int(input())
b = int(input())

try:
    result = safe_div(a, b)
    print(f"Result: {result}")
except MyDivisionError as e:
    print(f"Error: {e}")