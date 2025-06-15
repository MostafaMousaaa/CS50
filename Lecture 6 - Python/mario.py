from cs50 import get_int

def print_pyramid(height):
    """Print a pyramid of given height"""
    for i in range(height):
        # Print spaces
        print(" " * (height - i - 1), end="")
        # Print hashes
        print("#" * (i + 1))

def print_double_pyramid(height):
    """Print a double pyramid of given height"""
    for i in range(height):
        # Left side
        print(" " * (height - i - 1), end="")
        print("#" * (i + 1), end="")
        
        # Gap
        print("  ", end="")
        
        # Right side
        print("#" * (i + 1))

def main():
    """Get height and print pyramids"""
    
    # Get valid height (1-8)
    while True:
        height = get_int("Height: ")
        if 1 <= height <= 8:
            break
        print("Height must be between 1 and 8")
    
    print("\nSingle pyramid:")
    print_pyramid(height)
    
    print("\nDouble pyramid:")
    print_double_pyramid(height)
    
    # Alternative using string multiplication
    print("\nAlternative single pyramid:")
    for i in range(1, height + 1):
        print(" " * (height - i) + "#" * i)

if __name__ == "__main__":
    main()
