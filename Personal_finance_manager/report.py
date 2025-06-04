class Report:
    def __init__(self, username, db):
        self.username = username
        self.db = db

    def generate_report(self):
        self.db.cursor.execute("SELECT SUM(amount) FROM transactions WHERE username=? AND type='income'", (self.username,))
        total_income = self.db.cursor.fetchone()[0] or 0

        self.db.cursor.execute("SELECT SUM(amount) FROM transactions WHERE username=? AND type='expense'", (self.username,))
        total_expenses = self.db.cursor.fetchone()[0] or 0

        savings = total_income + total_expenses  # Expenses are negative

        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Total Savings: {savings}")
