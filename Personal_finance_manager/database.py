import sqlite3
from user import User
from transaction import Transaction
from budget import Budget

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, username TEXT, amount REAL, category TEXT, type TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (username TEXT, category TEXT, budget_limit REAL)''')  # Renamed 'limit' to 'budget_limit'
        self.connection.commit()

    def add_user(self, user):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user.username, user.password))
        self.connection.commit()

    def authenticate_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = self.cursor.fetchone()
        return User(result[0], result[1]) if result else None

    def add_transaction(self, transaction):
        self.cursor.execute("INSERT INTO transactions (username, amount, category, type) VALUES (?, ?, ?, ?)",
                            (transaction.username, transaction.amount, transaction.category, transaction.type))
        self.connection.commit()

    def set_budget(self, budget):
        self.cursor.execute("INSERT INTO budgets (username, category, budget_limit) VALUES (?, ?, ?)",
                            (budget.username, budget.category, budget.budget_limit))  # Updated to use 'budget_limit'
        self.connection.commit()

    def close(self):
        self.connection.close()

