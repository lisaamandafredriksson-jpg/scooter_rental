import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(1, "Anna Andersson", "anna@mail.com", "070-1234567", 100.0)

    def test_add_balance(self):
        self.user.add_balance(50)
        self.assertEqual(self.user.balance, 150.0)

    def test_add_balance_invalid(self):
        with self.assertRaises(ValueError):
            self.user.add_balance(0)
        with self.assertRaises(ValueError):
            self.user.add_balance(-10)

    def test_deduct_balance(self):
        self.user.deduct_balance(30)
        self.assertEqual(self.user.balance, 70.0)

    def test_deduct_balance_insufficient(self):
        with self.assertRaises(ValueError):
            self.user.deduct_balance(200)

if __name__ == "__main__":
    unittest.main()