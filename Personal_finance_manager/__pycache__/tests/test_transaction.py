import unittest
from transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        transaction = Transaction(username="testuser", amount=100.0, category="Salary", type="income")
        self.assertEqual(transaction.username, "testuser")
        self.assertEqual(transaction.amount, 100.0)
        self.assertEqual(transaction.category, "Salary")
        self.assertEqual(transaction.type, "income")

    def test_transaction_negative_amount(self):
        transaction = Transaction(username="testuser", amount=-50.0, category="Food", type="expense")
        self.assertEqual(transaction.amount, -50.0)
        self.assertEqual(transaction.type, "expense")

if __name__ == "__main__":
    unittest.main()

