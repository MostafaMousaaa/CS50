import csv
import sys
from cs50 import get_string

def longest_match(sequence, subsequence):
    """Return length of longest run of subsequence in sequence"""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs
    for i in range(sequence_length):
        count = 0
        
        # Check for a subsequence match starting at position i
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        
        longest_run = max(longest_run, count)

    return longest_run

def load_database(filename):
    """Load DNA database from CSV file"""
    database = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)
    
    return database

def analyze_dna(sequence, strs):
    """Analyze DNA sequence for STR counts"""
    profile = {}
    
    for str_sequence in strs:
        profile[str_sequence] = longest_match(sequence, str_sequence)
    
    return profile

def find_match(database, profile):
    """Find matching person in database"""
    for person in database:
        match = True
        for str_sequence in profile:
            if int(person[str_sequence]) != profile[str_sequence]:
                match = False
                break
        
        if match:
            return person['name']
    
    return "No match"

def main():
    """DNA analysis program"""
    
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        return
    
    database_file = sys.argv[1]
    sequence_file = sys.argv[2]
    
    # Load database
    try:
        database = load_database(database_file)
    except FileNotFoundError:
        print(f"Error: {database_file} not found")
        return
    
    # Get STR sequences from database header
    strs = list(database[0].keys())[1:]  # Skip 'name' column
    
    # Load DNA sequence
    try:
        with open(sequence_file, 'r') as file:
            sequence = file.read().strip()
    except FileNotFoundError:
        print(f"Error: {sequence_file} not found")
        return
    
    # Analyze DNA
    profile = analyze_dna(sequence, strs)
    
    # Display results
    print("STR Analysis:")
    for str_sequence, count in profile.items():
        print(f"{str_sequence}: {count}")
    
    # Find match
    match = find_match(database, profile)
    print(f"\nResult: {match}")

if __name__ == "__main__":
    main()
