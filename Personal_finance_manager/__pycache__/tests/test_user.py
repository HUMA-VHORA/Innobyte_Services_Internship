import unittest
from user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("testuser", "password123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "password123")

if __name__ == '__main__':
    unittest.main()
