import unittest
from models.scooter import Scooter

class TestScooter(unittest.TestCase):

    def setUp(self):
        self.scooter = Scooter(1, "VOI123", "Stureplan", 3.0, 100, True)

    def test_rent_and_release(self):
        self.scooter.rent()
        self.assertFalse(self.scooter.is_available)
        self.scooter.release("Odenplan")
        self.assertTrue(self.scooter.is_available)
        self.assertEqual(self.scooter.location, "Odenplan")

    def test_rent_already_rented(self):
        self.scooter.rent()
        with self.assertRaises(ValueError):
            self.scooter.rent()

    def test_drain_battery(self):
        self.scooter.drain_battery(30)
        self.assertEqual(self.scooter.battery_level, 70)

    def test_drain_battery_negative(self):
        with self.assertRaises(ValueError):
            self.scooter.drain_battery(-10)

if __name__ == "__main__":
    unittest.main()