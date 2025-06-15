def list_examples():
    """Demonstrate Python lists"""
    print("=== Lists ===")
    
    # Creating lists
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    empty = []
    
    print(f"Numbers: {numbers}")
    print(f"Mixed types: {mixed}")
    
    # List operations
    numbers.append(6)
    print(f"After append(6): {numbers}")
    
    numbers.insert(0, 0)
    print(f"After insert(0, 0): {numbers}")
    
    numbers.remove(3)
    print(f"After remove(3): {numbers}")
    
    # List slicing
    print(f"First 3 elements: {numbers[:3]}")
    print(f"Last 3 elements: {numbers[-3:]}")
    print(f"Every 2nd element: {numbers[::2]}")
    
    # List comprehensions
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")
    
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers: {evens}")

def dict_examples():
    """Demonstrate Python dictionaries"""
    print("\n=== Dictionaries ===")
    
    # Creating dictionaries
    person = {
        "name": "Alice",
        "age": 30,
        "city": "Boston"
    }
    
    print(f"Person: {person}")
    
    # Accessing values
    print(f"Name: {person['name']}")
    print(f"Age: {person.get('age', 'Unknown')}")
    
    # Adding/updating
    person["email"] = "alice@example.com"
    person["age"] = 31
    print(f"Updated person: {person}")
    
    # Dictionary methods
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    print(f"Items: {list(person.items())}")
    
    # Dictionary comprehension
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"Squares dict: {squares_dict}")

def set_examples():
    """Demonstrate Python sets"""
    print("\n=== Sets ===")
    
    # Creating sets
    numbers = {1, 2, 3, 4, 5}
    duplicates = {1, 2, 2, 3, 3, 4}
    
    print(f"Numbers set: {numbers}")
    print(f"Set from duplicates: {duplicates}")
    
    # Set operations
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")

def tuple_examples():
    """Demonstrate Python tuples"""
    print("\n=== Tuples ===")
    
    # Creating tuples
    coordinates = (10, 20)
    rgb = (255, 128, 0)
    single = (42,)  # Note the comma for single-element tuple
    
    print(f"Coordinates: {coordinates}")
    print(f"RGB color: {rgb}")
    print(f"Single element tuple: {single}")
    
    # Tuple unpacking
    x, y = coordinates
    print(f"x = {x}, y = {y}")
    
    # Tuples are immutable
    try:
        coordinates[0] = 15
    except TypeError as e:
        print(f"Error: {e}")

def main():
    """Demonstrate various Python data structures"""
    list_examples()
    dict_examples()
    set_examples()
    tuple_examples()
    
    print("\n=== Comparison with C ===")
    print("Python lists vs C arrays:")
    print("  - Dynamic size vs fixed size")
    print("  - Mixed types vs single type")
    print("  - Built-in methods vs manual implementation")
    
    print("\nPython dicts vs C hash tables:")
    print("  - Built-in vs manual implementation")
    print("  - Automatic resizing vs manual management")
    print("  - Easy syntax vs complex pointer operations")

if __name__ == "__main__":
    main()
