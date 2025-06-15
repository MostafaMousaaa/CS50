from cs50 import get_float

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return None  # Handle division by zero
    return x / y

def main():
    """Simple calculator program"""
    
    # Get input from user
    x = get_float("x: ")
    y = get_float("y: ")
    
    # Perform calculations
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    
    result = divide(x, y)
    if result is not None:
        print(f"{x} / {y} = {result}")
    else:
        print("Cannot divide by zero!")
    
    # Integer division and modulo
    if y != 0:
        print(f"{x} // {y} = {x // y}")  # Integer division
        print(f"{x} % {y} = {x % y}")    # Modulo

if __name__ == "__main__":
    main()
