import sys
from database import Database
from user import User
from transaction import Transaction
from report import Report
from budget import Budget

def main():
    db = Database('finance.db')
    db.create_tables()

    while True:
        print("Welcome to Personal Finance Manager")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            db.add_user(user)
            print("User  registered successfully!")

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = db.authenticate_user(username, password)
            if user:
                print("Login successful!")
                user_menu(user, db)
            else:
                print("Invalid credentials!")

        elif choice == '3':
            print("Exiting...")
            sys.exit()

def user_menu(user, db):
    while True:
        print(f"\nWelcome {user.username}")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Report")
        print("4. Set Budget")
        print("5. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter category: ")
            transaction = Transaction(user.username, amount, category, 'income')
            db.add_transaction(transaction)
            print("Income added successfully!")

        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter category: ")
            transaction = Transaction(user.username, -amount, category, 'expense')
            db.add_transaction(transaction)
            print("Expense added successfully!")

        elif choice == '3':
            report = Report(user.username, db)
            report.generate_report()

        elif choice == '4':
            category = input("Enter budget category: ")
            limit = float(input("Enter budget limit: "))
            budget = Budget(user.username, category, limit)
            db.set_budget(budget)
            print("Budget set successfully!")

        elif choice == '5':
            print("Logging out...")
            break

if __name__ == "__main__":
    main()
