import csv
import json
from cs50 import get_string

def text_file_examples():
    """Demonstrate text file operations"""
    print("=== Text File Operations ===")
    
    filename = "sample.txt"
    
    # Writing to file
    with open(filename, 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("Python makes file I/O easy!\n")
    
    print(f"Created {filename}")
    
    # Reading entire file
    with open(filename, 'r') as file:
        content = file.read()
        print("File contents:")
        print(content)
    
    # Reading line by line
    print("Reading line by line:")
    with open(filename, 'r') as file:
        for i, line in enumerate(file, 1):
            print(f"Line {i}: {line.strip()}")
    
    # Appending to file
    with open(filename, 'a') as file:
        file.write("This line was appended.\n")
    
    print("Appended a line to the file")

def csv_examples():
    """Demonstrate CSV file operations"""
    print("\n=== CSV File Operations ===")
    
    filename = "students.csv"
    
    # Sample data
    students = [
        {"name": "Alice", "house": "Gryffindor", "year": 3},
        {"name": "Bob", "house": "Hufflepuff", "year": 2},
        {"name": "Charlie", "house": "Ravenclaw", "year": 4}
    ]
    
    # Writing CSV
    with open(filename, 'w', newline='') as file:
        fieldnames = ["name", "house", "year"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for student in students:
            writer.writerow(student)
    
    print(f"Created {filename}")
    
    # Reading CSV
    print("Reading CSV file:")
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['name']} from {row['house']}, Year {row['year']}")

def json_examples():
    """Demonstrate JSON file operations"""
    print("\n=== JSON File Operations ===")
    
    filename = "data.json"
    
    # Sample data
    data = {
        "course": "CS50",
        "instructor": "David Malan",
        "topics": ["C", "Python", "SQL", "Web Development"],
        "students": 800,
        "online": True
    }
    
    # Writing JSON
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"Created {filename}")
    
    # Reading JSON
    with open(filename, 'r') as file:
        loaded_data = json.load(file)
    
    print("Loaded JSON data:")
    for key, value in loaded_data.items():
        print(f"{key}: {value}")

def file_statistics(filename):
    """Calculate file statistics"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            
            stats = {
                "characters": len(content),
                "words": len(content.split()),
                "lines": len(lines),
                "non_empty_lines": len([line for line in lines if line.strip()])
            }
            
            return stats
    
    except FileNotFoundError:
        return None

def main():
    """Demonstrate file I/O operations"""
    text_file_examples()
    csv_examples()
    json_examples()
    
    # File statistics example
    print("\n=== File Statistics ===")
    filename = get_string("Enter filename to analyze: ")
    
    stats = file_statistics(filename)
    if stats:
        print(f"Statistics for {filename}:")
        for key, value in stats.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print(f"File {filename} not found")
    
    print("\n=== Error Handling ===")
    # Demonstrate exception handling
    try:
        with open("nonexistent.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("Handled FileNotFoundError gracefully")
    except PermissionError:
        print("Handled PermissionError gracefully")
    except Exception as e:
        print(f"Handled unexpected error: {e}")

if __name__ == "__main__":
    main()
