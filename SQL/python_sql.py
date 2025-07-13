import sqlite3
import csv
from cs50 import get_string, get_int

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Connect to the database"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Connected to {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
    
    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("Database connection closed")
    
    def create_tables(self):
        """Create tables for student management system"""
        try:
            # Students table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    house TEXT NOT NULL,
                    year INTEGER NOT NULL CHECK (year >= 1 AND year <= 4)
                )
            ''')
            
            # Courses table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL UNIQUE,
                    credits INTEGER NOT NULL DEFAULT 3
                )
            ''')
            
            # Enrollments table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS enrollments (
                    student_id INTEGER,
                    course_id INTEGER,
                    grade TEXT CHECK (grade IN ('A', 'B', 'C', 'D', 'F')),
                    PRIMARY KEY (student_id, course_id),
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (course_id) REFERENCES courses(id)
                )
            ''')
            
            self.connection.commit()
            print("Tables created successfully")
            
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
    
    def add_student(self, name, house, year):
        """Add a new student - demonstrates parameterized queries"""
        try:
            # Secure way using parameterized query
            self.cursor.execute(
                "INSERT INTO students (name, house, year) VALUES (?, ?, ?)",
                (name, house, year)
            )
            self.connection.commit()
            print(f"Added student: {name}")
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")
            return None
    
    def add_student_unsafe(self, name, house, year):
        """Demonstrates SQL injection vulnerability - DO NOT USE"""
        try:
            # DANGEROUS: Vulnerable to SQL injection
            query = f"INSERT INTO students (name, house, year) VALUES ('{name}', '{house}', {year})"
            print(f"Unsafe query: {query}")
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error in unsafe query: {e}")
    
    def search_students(self, house=None, year=None):
        """Search students with optional filters"""
        try:
            query = "SELECT id, name, house, year FROM students WHERE 1=1"
            params = []
            
            if house:
                query += " AND house = ?"
                params.append(house)
            
            if year:
                query += " AND year = ?"
                params.append(year)
            
            query += " ORDER BY name"
            
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
            
        except sqlite3.Error as e:
            print(f"Error searching students: {e}")
            return []
    
    def get_student_grades(self, student_id):
        """Get all grades for a student with course information"""
        try:
            self.cursor.execute('''
                SELECT c.title, e.grade, c.credits
                FROM enrollments e
                JOIN courses c ON e.course_id = c.id
                WHERE e.student_id = ?
                ORDER BY c.title
            ''', (student_id,))
            
            return self.cursor.fetchall()
            
        except sqlite3.Error as e:
            print(f"Error getting grades: {e}")
            return []
    
    def calculate_gpa(self, student_id):
        """Calculate GPA for a student"""
        try:
            self.cursor.execute('''
                SELECT 
                    CASE e.grade
                        WHEN 'A' THEN 4.0
                        WHEN 'B' THEN 3.0
                        WHEN 'C' THEN 2.0
                        WHEN 'D' THEN 1.0
                        WHEN 'F' THEN 0.0
                    END * c.credits as grade_points,
                    c.credits
                FROM enrollments e
                JOIN courses c ON e.course_id = c.id
                WHERE e.student_id = ?
            ''', (student_id,))
            
            results = self.cursor.fetchall()
            
            if not results:
                return None
            
            total_points = sum(row[0] for row in results)
            total_credits = sum(row[1] for row in results)
            
            return total_points / total_credits if total_credits > 0 else 0
            
        except sqlite3.Error as e:
            print(f"Error calculating GPA: {e}")
            return None
    
    def house_statistics(self):
        """Get statistics by house"""
        try:
            self.cursor.execute('''
                SELECT 
                    house,
                    COUNT(*) as student_count,
                    AVG(year) as avg_year
                FROM students
                GROUP BY house
                ORDER BY student_count DESC
            ''')
            
            return self.cursor.fetchall()
            
        except sqlite3.Error as e:
            print(f"Error getting house statistics: {e}")
            return []
    
    def import_from_csv(self, csv_file, table_name):
        """Import data from CSV file"""
        try:
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)
                
                for row in csv_reader:
                    if table_name == 'students':
                        self.add_student(row['name'], row['house'], int(row['year']))
                    # Add more table types as needed
                
                print(f"Imported data from {csv_file}")
                
        except FileNotFoundError:
            print(f"CSV file {csv_file} not found")
        except Exception as e:
            print(f"Error importing CSV: {e}")
    
    def demonstrate_transaction(self):
        """Demonstrate database transactions"""
        try:
            # Start transaction
            self.cursor.execute("BEGIN TRANSACTION")
            
            # Multiple operations
            self.cursor.execute("INSERT INTO students (name, house, year) VALUES (?, ?, ?)",
                              ("Test Student 1", "Gryffindor", 1))
            self.cursor.execute("INSERT INTO students (name, house, year) VALUES (?, ?, ?)",
                              ("Test Student 2", "Slytherin", 2))
            
            # Simulate an error condition
            should_rollback = get_string("Rollback transaction? (y/n): ").lower() == 'y'
            
            if should_rollback:
                self.cursor.execute("ROLLBACK")
                print("Transaction rolled back")
            else:
                self.cursor.execute("COMMIT")
                print("Transaction committed")
                
        except sqlite3.Error as e:
            print(f"Transaction error: {e}")
            self.cursor.execute("ROLLBACK")

def demonstrate_sql_injection():
    """Demonstrate SQL injection attack and prevention"""
    print("=== SQL Injection Demonstration ===")
    
    db = DatabaseManager("injection_demo.db")
    db.connect()
    db.create_tables()
    
    # Add some sample data
    db.add_student("Alice", "Gryffindor", 3)
    db.add_student("Bob", "Slytherin", 2)
    
    print("\n1. Normal search:")
    name = "Alice"
    try:
        db.cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        results = db.cursor.fetchall()
        print(f"Found: {results}")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    
    print("\n2. SQL Injection attempt:")
    malicious_input = "'; DROP TABLE students; --"
    print(f"Malicious input: {malicious_input}")
    
    # Safe version (parameterized query)
    try:
        db.cursor.execute("SELECT * FROM students WHERE name = ?", (malicious_input,))
        results = db.cursor.fetchall()
        print(f"Safe query result: {results}")
        print("✅ Parameterized query prevented injection!")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    
    # Verify table still exists
    try:
        db.cursor.execute("SELECT COUNT(*) FROM students")
        count = db.cursor.fetchone()[0]
        print(f"Students table still has {count} records")
    except sqlite3.Error as e:
        print(f"Table destroyed! {e}")
    
    db.disconnect()

def main():
    """Main program demonstrating database operations"""
    print("=== Python + SQL Database Demo ===")
    
    db = DatabaseManager("students.db")
    db.connect()
    db.create_tables()
    
    while True:
        print("\nOptions:")
        print("1. Add student")
        print("2. Search students")
        print("3. View house statistics")
        print("4. Student grades")
        print("5. Demonstrate transactions")
        print("6. SQL injection demo")
        print("7. Exit")
        
        choice = get_string("Choose option: ")
        
        if choice == "1":
            name = get_string("Student name: ")
            house = get_string("House: ")
            year = get_int("Year: ")
            db.add_student(name, house, year)
        
        elif choice == "2":
            house = get_string("Filter by house (optional): ")
            year_str = get_string("Filter by year (optional): ")
            year = int(year_str) if year_str else None
            
            students = db.search_students(house if house else None, year)
            
            if students:
                print("\nFound students:")
                print("ID | Name | House | Year")
                print("-" * 30)
                for student in students:
                    print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")
            else:
                print("No students found")
        
        elif choice == "3":
            stats = db.house_statistics()
            if stats:
                print("\nHouse Statistics:")
                print("House | Students | Avg Year")
                print("-" * 30)
                for stat in stats:
                    print(f"{stat[0]} | {stat[1]} | {stat[2]:.1f}")
        
        elif choice == "4":
            student_id = get_int("Student ID: ")
            grades = db.get_student_grades(student_id)
            gpa = db.calculate_gpa(student_id)
            
            if grades:
                print(f"\nGrades for student {student_id}:")
                print("Course | Grade | Credits")
                print("-" * 25)
                for grade in grades:
                    print(f"{grade[0]} | {grade[1]} | {grade[2]}")
                
                if gpa is not None:
                    print(f"\nGPA: {gpa:.2f}")
            else:
                print("No grades found for this student")
        
        elif choice == "5":
            db.demonstrate_transaction()
        
        elif choice == "6":
            demonstrate_sql_injection()
        
        elif choice == "7":
            db.disconnect()
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
