import sqlite3

# Connect to database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL NOT NULL
)
""")
conn.commit()


def create account():
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))
    
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, balance))
    conn.commit()
    print("✅ Account Created Successfully!")


def deposit():
    acc no = int(input("Enter Account Number: "))
    amount = float(input("Enter Deposit Amount: "))
    
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no = ?", (amount, acc_no))
    conn.commit()
    print("✅ Amount Deposited Successfully!")


def withdraw():
    acc no = int(input("Enter Account Number: "))
    amount = float(input("Enter Withdraw Amount: "))
    
    cursor.execute("SELECT balance FROM accounts WHERE acc_no = ?", (acc_no,))
    result = cursor.fetchone()
    
    if result and result[0] >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no = ?", (amount, acc_no))
        conn.commit()
        print("✅ Withdrawal Successful!")
    else:
        print("❌ Insufficient Balance or Invalid Account!")


def check_balance():
    acc_no = int(input("Enter Account Number: "))
    cursor.execute("SELECT * FROM accounts WHERE acc_no = ?", (acc_no,))
    result = cursor.fetchone()
    
    if result:
        print(f"Account No: {result[0]}")
        print(f"Name: {result[1]}")
        print(f"Balance: ₹{result[2]}")
    else:
        print("❌ Account Not Found!")


def view_all():
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    
    for acc in accounts:
        print(f"Acc No: {acc[0]} | Name: {acc[1]} | Balance: ₹{acc[2]}")


# Main Menu
while True:
    print("\n--- BANK MANAGEMENT SYSTEM ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        view_all()
    elif choice == "6":
        print("Thank You for Using Bank System")
        break
    else:
        print("Invalid Choice!")
