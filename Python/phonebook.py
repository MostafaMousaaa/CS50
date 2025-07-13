import csv
from cs50 import get_string

def load_phonebook(filename):
    """Load phonebook from CSV file"""
    phonebook = {}
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                phonebook[row['name']] = row['number']
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty phonebook.")
    
    return phonebook

def save_phonebook(phonebook, filename):
    """Save phonebook to CSV file"""
    with open(filename, 'w', newline='') as file:
        fieldnames = ['name', 'number']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for name, number in phonebook.items():
            writer.writerow({'name': name, 'number': number})

def add_contact(phonebook):
    """Add a new contact to phonebook"""
    name = get_string("Name: ")
    number = get_string("Number: ")
    phonebook[name] = number
    print(f"Added {name}: {number}")

def search_contact(phonebook):
    """Search for a contact in phonebook"""
    name = get_string("Search for: ")
    
    if name in phonebook:
        print(f"Found: {name} -> {phonebook[name]}")
    else:
        print(f"{name} not found")

def list_contacts(phonebook):
    """List all contacts in phonebook"""
    if not phonebook:
        print("Phonebook is empty")
        return
    
    print("\nPhonebook:")
    print("-" * 30)
    for name in sorted(phonebook.keys()):
        print(f"{name}: {phonebook[name]}")

def main():
    """Main phonebook program"""
    filename = "phonebook.csv"
    phonebook = load_phonebook(filename)
    
    while True:
        print("\n=== Phonebook ===")
        print("1. Add contact")
        print("2. Search contact")
        print("3. List all contacts")
        print("4. Save and quit")
        
        choice = get_string("Choose an option: ")
        
        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            list_contacts(phonebook)
        elif choice == "4":
            save_phonebook(phonebook, filename)
            print("Phonebook saved. Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
