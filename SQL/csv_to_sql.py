import csv
import sqlite3
import os
from cs50 import get_string

def create_sample_csv():
    """Create sample CSV files for demonstration"""
    
    # Students CSV
    students_data = [
        ['name', 'house', 'year'],
        ['Harry Potter', 'Gryffindor', '3'],
        ['Hermione Granger', 'Gryffindor', '3'],
        ['Ron Weasley', 'Gryffindor', '3'],
        ['Draco Malfoy', 'Slytherin', '3'],
        ['Luna Lovegood', 'Ravenclaw', '2'],
        ['Cedric Diggory', 'Hufflepuff', '4']
    ]
    
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students_data)
    
    print("Created students.csv")
    
    # Shows CSV
    shows_data = [
        ['title', 'year', 'rating'],
        ['The Office', '2005', '8.7'],
        ['Breaking Bad', '2008', '9.4'],
        ['Friends', '1994', '8.9'],
        ['Game of Thrones', '2011', '9.2'],
        ['Stranger Things', '2016', '8.8']
    ]
    
    with open('shows.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(shows_data)
    
    print("Created shows.csv")

def csv_to_sqlite(csv_file, db_file, table_name):
    """Convert CSV file to SQLite table"""
    
    if not os.path.exists(csv_file):
        print(f"CSV file {csv_file} not found")
        return
    
    # Connect to database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    try:
        # Read CSV file
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Get column headers
            
            # Create table with columns from CSV headers
            columns = []
            for header in headers:
                # Simple type inference
                if header.lower() in ['year', 'rating', 'id', 'age']:
                    columns.append(f"{header} REAL")
                else:
                    columns.append(f"{header} TEXT")
            
            # Drop table if exists and create new one
            cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
            create_query = f"CREATE TABLE {table_name} ({', '.join(columns)})"
            cursor.execute(create_query)
            
            print(f"Created table: {table_name}")
            print(f"Columns: {', '.join(headers)}")
            
            # Insert data
            placeholders = ', '.join(['?' for _ in headers])
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            
            row_count = 0
            for row in csv_reader:
                cursor.execute(insert_query, row)
                row_count += 1
            
            conn.commit()
            print(f"Inserted {row_count} rows into {table_name}")
            
    except Exception as e:
        print(f"Error converting CSV: {e}")
        conn.rollback()
    finally:
        conn.close()

def analyze_csv_structure(csv_file):
    """Analyze CSV structure and suggest SQL schema"""
    
    if not os.path.exists(csv_file):
        print(f"CSV file {csv_file} not found")
        return
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        
        # Analyze first few rows to infer types
        sample_rows = []
        for i, row in enumerate(csv_reader):
            if i >= 10:  # Analyze first 10 rows
                break
            sample_rows.append(row)
    
    print(f"\n=== CSV Analysis: {csv_file} ===")
    print(f"Columns found: {len(headers)}")
    print(f"Sample rows: {len(sample_rows)}")
    
    # Suggest data types
    print("\nSuggested SQL schema:")
    print(f"CREATE TABLE {os.path.splitext(csv_file)[0]} (")
    
    for i, header in enumerate(headers):
        # Simple type inference based on sample data
        column_type = "TEXT"  # Default
        
        if sample_rows:
            sample_values = [row[i] for row in sample_rows if i < len(row)]
            
            # Check if all values are numeric
            try:
                numeric_values = [float(val) for val in sample_values if val]
                if all(val.is_integer() for val in numeric_values):
                    column_type = "INTEGER"
                else:
                    column_type = "REAL"
            except ValueError:
                column_type = "TEXT"
        
        comma = "," if i < len(headers) - 1 else ""
        print(f"    {header} {column_type}{comma}")
    
    print(");")

def export_sql_to_csv(db_file, table_name, output_csv):
    """Export SQL table back to CSV"""
    
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        # Get all data from table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [row[1] for row in cursor.fetchall()]
        
        # Write to CSV
        with open(output_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)  # Write headers
            writer.writerows(rows)    # Write data
        
        conn.close()
        print(f"Exported {table_name} to {output_csv}")
        print(f"Exported {len(rows)} rows with {len(columns)} columns")
        
    except Exception as e:
        print(f"Error exporting to CSV: {e}")

def main():
    """Main program for CSV/SQL conversion"""
    print("=== CSV ↔ SQL Converter ===")
    
    while True:
        print("\nOptions:")
        print("1. Create sample CSV files")
        print("2. Convert CSV to SQLite")
        print("3. Analyze CSV structure")
        print("4. Export SQL table to CSV")
        print("5. View table data")
        print("6. Exit")
        
        choice = get_string("Choose option: ")
        
        if choice == "1":
            create_sample_csv()
        
        elif choice == "2":
            csv_file = get_string("CSV file name: ")
            db_file = get_string("Database file name: ")
            table_name = get_string("Table name: ")
            csv_to_sqlite(csv_file, db_file, table_name)
        
        elif choice == "3":
            csv_file = get_string("CSV file name: ")
            analyze_csv_structure(csv_file)
        
        elif choice == "4":
            db_file = get_string("Database file name: ")
            table_name = get_string("Table name: ")
            output_csv = get_string("Output CSV file name: ")
            export_sql_to_csv(db_file, table_name, output_csv)
        
        elif choice == "5":
            db_file = get_string("Database file name: ")
            table_name = get_string("Table name: ")
            
            try:
                conn = sqlite3.connect(db_file)
                cursor = conn.cursor()
                
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 10")
                rows = cursor.fetchall()
                
                if rows:
                    # Get column names
                    cursor.execute(f"PRAGMA table_info({table_name})")
                    columns = [row[1] for row in cursor.fetchall()]
                    
                    print(f"\nFirst 10 rows from {table_name}:")
                    print(" | ".join(columns))
                    print("-" * (len(" | ".join(columns))))
                    
                    for row in rows:
                        print(" | ".join(str(cell) for cell in row))
                else:
                    print(f"No data found in {table_name}")
                
                conn.close()
                
            except Exception as e:
                print(f"Error viewing table: {e}")
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
