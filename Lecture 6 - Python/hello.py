from cs50 import get_string

def main():
    """Basic Python hello world program"""
    
    # Simple print statement
    print("Hello, world!")
    
    # Get user input
    name = get_string("What's your name? ")
    print(f"Hello, {name}!")
    
    # String methods
    print(f"Uppercase: {name.upper()}")
    print(f"Lowercase: {name.lower()}")
    print(f"Length: {len(name)}")
    
    # Different ways to format strings
    print("Hello, " + name + "!")
    print("Hello, %s!" % name)
    print("Hello, {}!".format(name))
    print(f"Hello, {name}!")  # f-strings (preferred)

if __name__ == "__main__":
    main()
