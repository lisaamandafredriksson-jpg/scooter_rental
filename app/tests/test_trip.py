import unittest
from datetime import datetime, timedelta
from models.trip import Trip
from models.scooter import Scooter

class TestTrip(unittest.TestCase):

    def setUp(self):
        # Skapa scooter korrekt med scooter_id först
        self.scooter = Scooter(
            1,              # scooter_id
            "VOI123",       # scooter_code
            "Stureplan",    # location
            3.0,            # price_per_min
            100,            # battery_level
            True            # is_available
        )

        # Skapa Trip
        self.trip = Trip(
            user_id=1,
            scooter=self.scooter,
            start_time=datetime.now()
        )

    def test_end_trip_calculates_cost(self):
        # Simulera att resan startade
        self.trip._start_time = datetime.now() - timedelta(seconds=50)

        cost = self.trip.end_trip()

        # 1 minut * 3 kr/min
        self.assertEqual(cost, 3.0)
        self.assertIsNotNone(self.trip.end_time)

    def test_end_trip_twice_raises_error(self):
        self.trip._start_time = datetime.now() - timedelta(seconds=50)
        self.trip.end_trip()

        # Om man försöker avsluta resan igen ska ValueError kastas
        with self.assertRaises(ValueError):
            self.trip.end_trip()


if __name__ == "__main__":
    unittest.main()
