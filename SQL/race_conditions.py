import sqlite3
import threading
import time
import random
from cs50 import get_string

class BankAccount:
    def __init__(self, db_name="bank.db"):
        self.db_name = db_name
        self.setup_database()
    
    def setup_database(self):
        """Create bank account table"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                balance REAL NOT NULL DEFAULT 0.0
            )
        ''')
        
        # Create sample account if not exists
        cursor.execute("SELECT COUNT(*) FROM accounts WHERE id = 1")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO accounts (id, name, balance) VALUES (1, 'Shared Account', 1000.0)")
        
        conn.commit()
        conn.close()
    
    def get_balance(self, account_id):
        """Get current balance"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
        result = cursor.fetchone()
        
        conn.close()
        return result[0] if result else 0.0
    
    def withdraw_unsafe(self, account_id, amount, user_name):
        """Unsafe withdrawal - demonstrates race condition"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            # Step 1: Read current balance
            cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
            current_balance = cursor.fetchone()[0]
            
            print(f"{user_name}: Read balance: ${current_balance:.2f}")
            
            # Simulate processing time
            time.sleep(random.uniform(0.1, 0.5))
            
            # Step 2: Check if sufficient funds
            if current_balance >= amount:
                # Step 3: Calculate new balance
                new_balance = current_balance - amount
                
                print(f"{user_name}: Withdrawing ${amount:.2f}, new balance will be ${new_balance:.2f}")
                
                # Simulate more processing time
                time.sleep(random.uniform(0.1, 0.3))
                
                # Step 4: Update balance
                cursor.execute("UPDATE accounts SET balance = ? WHERE id = ?", 
                             (new_balance, account_id))
                conn.commit()
                
                print(f"✅ {user_name}: Successfully withdrew ${amount:.2f}")
            else:
                print(f"❌ {user_name}: Insufficient funds (${current_balance:.2f})")
        
        except sqlite3.Error as e:
            print(f"❌ {user_name}: Database error: {e}")
        finally:
            conn.close()
    
    def withdraw_safe(self, account_id, amount, user_name):
        """Safe withdrawal using database transaction"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            # Start transaction
            cursor.execute("BEGIN IMMEDIATE TRANSACTION")
            
            # Read and update in single transaction
            cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
            current_balance = cursor.fetchone()[0]
            
            print(f"{user_name}: Read balance: ${current_balance:.2f}")
            
            if current_balance >= amount:
                new_balance = current_balance - amount
                
                # Simulate processing time
                time.sleep(random.uniform(0.1, 0.3))
                
                cursor.execute("UPDATE accounts SET balance = ? WHERE id = ?", 
                             (new_balance, account_id))
                
                # Commit transaction
                cursor.execute("COMMIT")
                print(f"✅ {user_name}: Successfully withdrew ${amount:.2f}")
            else:
                cursor.execute("ROLLBACK")
                print(f"❌ {user_name}: Insufficient funds (${current_balance:.2f})")
        
        except sqlite3.Error as e:
            cursor.execute("ROLLBACK")
            print(f"❌ {user_name}: Database error: {e}")
        finally:
            conn.close()
    
    def reset_account(self, account_id, balance=1000.0):
        """Reset account balance"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("UPDATE accounts SET balance = ? WHERE id = ?", (balance, account_id))
        conn.commit()
        conn.close()
        
        print(f"Account {account_id} reset to ${balance:.2f}")

def demonstrate_race_condition():
    """Demonstrate race condition with multiple threads"""
    print("=== Race Condition Demonstration ===")
    
    bank = BankAccount()
    account_id = 1
    
    # Reset account
    bank.reset_account(account_id, 1000.0)
    initial_balance = bank.get_balance(account_id)
    print(f"Initial balance: ${initial_balance:.2f}")
    
    # Create multiple threads trying to withdraw simultaneously
    threads = []
    users = ["Alice", "Bob", "Charlie", "Diana"]
    amounts = [300, 400, 500, 250]
    
    print(f"\nStarting unsafe withdrawals...")
    print(f"Expected final balance if all succeed: ${initial_balance - sum(amounts):.2f}")
    print("(But this should go negative, indicating a problem)")
    
    for user, amount in zip(users, amounts):
        thread = threading.Thread(
            target=bank.withdraw_unsafe,
            args=(account_id, amount, user)
        )
        threads.append(thread)
    
    # Start all threads simultaneously
    for thread in threads:
        thread.start()
    
    # Wait for all to complete
    for thread in threads:
        thread.join()
    
    final_balance = bank.get_balance(account_id)
    print(f"\n🔍 Final balance: ${final_balance:.2f}")
    
    if final_balance < 0:
        print("❌ RACE CONDITION DETECTED: Balance went negative!")
    else:
        print("✅ No race condition detected this time")

def demonstrate_safe_transactions():
    """Demonstrate safe transactions"""
    print("\n=== Safe Transaction Demonstration ===")
    
    bank = BankAccount()
    account_id = 1
    
    # Reset account
    bank.reset_account(account_id, 1000.0)
    initial_balance = bank.get_balance(account_id)
    print(f"Initial balance: ${initial_balance:.2f}")
    
    # Create multiple threads with safe withdrawals
    threads = []
    users = ["Alice", "Bob", "Charlie", "Diana"]
    amounts = [300, 400, 500, 250]
    
    print(f"\nStarting safe withdrawals...")
    
    for user, amount in zip(users, amounts):
        thread = threading.Thread(
            target=bank.withdraw_safe,
            args=(account_id, amount, user)
        )
        threads.append(thread)
    
    # Start all threads simultaneously
    for thread in threads:
        thread.start()
    
    # Wait for all to complete
    for thread in threads:
        thread.join()
    
    final_balance = bank.get_balance(account_id)
    print(f"\n🔍 Final balance: ${final_balance:.2f}")
    
    if final_balance >= 0:
        print("✅ Safe transactions prevented overdraft!")
    else:
        print("❌ Something went wrong with safe transactions")

def demonstrate_deadlock():
    """Demonstrate potential deadlock scenario"""
    print("\n=== Deadlock Demonstration ===")
    
    def transfer_money(from_account, to_account, amount, user_name):
        """Transfer money between accounts - potential deadlock"""
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        
        try:
            print(f"{user_name}: Starting transfer ${amount} from {from_account} to {to_account}")
            
            # Lock accounts in different orders - can cause deadlock
            cursor.execute("BEGIN IMMEDIATE TRANSACTION")
            
            # Get balance from source account
            cursor.execute("SELECT balance FROM accounts WHERE id = ?", (from_account,))
            balance = cursor.fetchone()[0]
            
            if balance >= amount:
                time.sleep(0.1)  # Simulate processing
                
                # Update both accounts
                cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", 
                             (amount, from_account))
                cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", 
                             (amount, to_account))
                
                cursor.execute("COMMIT")
                print(f"✅ {user_name}: Transfer completed")
            else:
                cursor.execute("ROLLBACK")
                print(f"❌ {user_name}: Insufficient funds")
                
        except sqlite3.Error as e:
            cursor.execute("ROLLBACK")
            print(f"❌ {user_name}: Error: {e}")
        finally:
            conn.close()
    
    # Setup two accounts
    bank = BankAccount()
    
    # Create account 2 if it doesn't exist
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO accounts (id, name, balance) VALUES (2, 'Account 2', 500.0)")
    conn.commit()
    conn.close()
    
    # Two threads transferring in opposite directions
    thread1 = threading.Thread(target=transfer_money, args=(1, 2, 100, "User1"))
    thread2 = threading.Thread(target=transfer_money, args=(2, 1, 150, "User2"))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

def main():
    """Main program"""
    print("=== Database Race Conditions and Concurrency ===")
    
    while True:
        print("\nOptions:")
        print("1. Demonstrate race condition")
        print("2. Demonstrate safe transactions")
        print("3. Demonstrate potential deadlock")
        print("4. Check account balance")
        print("5. Reset account")
        print("6. Exit")
        
        choice = get_string("Choose option: ")
        
        if choice == "1":
            demonstrate_race_condition()
        elif choice == "2":
            demonstrate_safe_transactions()
        elif choice == "3":
            demonstrate_deadlock()
        elif choice == "4":
            bank = BankAccount()
            balance1 = bank.get_balance(1)
            balance2 = bank.get_balance(2)
            print(f"Account 1 balance: ${balance1:.2f}")
            print(f"Account 2 balance: ${balance2:.2f}")
        elif choice == "5":
            bank = BankAccount()
            bank.reset_account(1, 1000.0)
            bank.reset_account(2, 500.0)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
