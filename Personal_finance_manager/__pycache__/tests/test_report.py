import unittest
from report import Report

class MockDB:
    def __init__(self):
        # Mock data storage for the cursor calls
        self.income_sum = 0
        self.expense_sum = 0
        self.called_queries = []

    def cursor(self):
        # Return self as cursor object
        return self

    def execute(self, query, params):
        self.called_queries.append((query, params))
        # This method does nothing but records calls for verification

    def fetchone(self):
        # Return sums based on the last query executed
        last_query, _ = self.called_queries[-1]
        if "type='income'" in last_query:
            return (self.income_sum,)
        elif "type='expense'" in last_query:
            return (self.expense_sum,)
        else:
            return (0,)

class TestReport(unittest.TestCase):
    def test_generate_report(self):
        mock_db = MockDB()
        # Set mock sums for income and expenses
        mock_db.income_sum = 1000.0
        mock_db.expense_sum = -300.0

        report = Report(username="testuser", db=mock_db)
        # Redirect print to capture output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        report.generate_report()

        sys.stdout = sys.__stdout__  # Reset redirect

        output = captured_output.getvalue()
        self.assertIn("Total Income: 1000.0", output)
        self.assertIn("Total Expenses: -300.0", output)
        self.assertIn("Total Savings: 700.0", output)

if __name__ == "__main__":
    unittest.main()

