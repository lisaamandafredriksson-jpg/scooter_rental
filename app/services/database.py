import psycopg2
import time
from models.user import User
from models.scooter import Scooter
from models.trip import Trip
from datetime import datetime
import os

class Database:
    def __init__(self):
        self.conn = None
        self._connect()
        self._create_tables()
        self.seed_data()  # Lägger till exempeldata direkt

    # Privata metoder
    def _connect(self):
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", 5432)
        user = os.getenv("DB_USER", "admin")
        password = os.getenv("DB_PASSWORD", "password123")
        database = os.getenv("DB_NAME", "scooter_app")

        print("Försöker ansluta till databasen...")
        for attempt in range(5):
            try:
                self.conn = psycopg2.connect(
                    host=host,
                    port=port,
                    user=user,
                    password=password,
                    database=database
                )
                print("Anslutning lyckades! ✅")
                return
            except psycopg2.OperationalError:
                print(f"Försök {attempt+1}/5 misslyckades. Väntar 2 sekunder...")
                time.sleep(2)
        raise Exception("Kunde inte ansluta till databasen :(")

    def load_sql(self, filename):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(base_dir, 'database', filename)
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def _create_tables(self):
        print("Skapar tabeller om de inte finns...")
        sql = self.load_sql('init.sql')
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        self.conn.commit()
        print("Tabeller klara!")

    # Tillgänglighet
    def execute(self, sql, params=None, fetch=False):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, params)
                if fetch:
                    return cursor.fetchall()
                self.conn.commit()
        except Exception as e:
            print(f"Databasfel: {e}")
            self.conn.rollback()
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            print("Anslutning stängd")

    # User
    def create_user(self, user: User):
        sql = """
            INSERT INTO users (name, email, phone, balance)
            VALUES (%s, %s, %s, %s) RETURNING id
        """
        row = self.execute(sql, (user.name, user.email, user.phone, user.balance), fetch=True)
        if row:
            user._id = row[0][0]
        return user

    def get_all_users(self):
        rows = self.execute("SELECT * FROM users", fetch=True)
        return [User(*row[:5]) for row in rows] if rows else []

    def get_user_by_id(self, user_id: int):
        rows = self.execute("SELECT * FROM users WHERE id=%s", (user_id,), fetch=True)
        return User(*rows[0][:5]) if rows else None

    def update_user_balance(self, user_id: int, new_balance: float):
        self.execute("UPDATE users SET balance=%s WHERE id=%s", (new_balance, user_id))

    # Scooter
    def create_scooter(self, scooter: Scooter):
        sql = """
            INSERT INTO scooters (scooter_code, location, price_per_min, battery_level, is_available)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
        """
        row = self.execute(sql, (scooter.scooter_code, scooter.location, scooter.price_per_min,
                                 scooter.battery_level, scooter.is_available), fetch=True)
        if row:
            scooter._id = row[0][0]
        return scooter

    def get_all_scooters(self):
        rows = self.execute("SELECT * FROM scooters", fetch=True)
        return [Scooter(*row[:6]) for row in rows] if rows else []

    def get_available_scooters(self):
        rows = self.execute("SELECT * FROM scooters WHERE is_available = TRUE", fetch=True)
        return [Scooter(*row[:6]) for row in rows] if rows else []

    def get_scooter_by_id(self, scooter_id: int):
        rows = self.execute("SELECT * FROM scooters WHERE id=%s", (scooter_id,), fetch=True)
        return Scooter(*rows[0][:6]) if rows else None

    def update_scooter_status(self, scooter_id: int, is_available: bool, location: str = None):
        sql = "UPDATE scooters SET is_available=%s"
        params = [is_available]
        if location:
            sql += ", location=%s"
            params.append(location)
        sql += " WHERE id=%s"
        params.append(scooter_id)
        self.execute(sql, tuple(params))

    # Trip
    def start_trip(self, trip: Trip):

        if isinstance(trip.scooter, int):
            trip._scooter = self.get_scooter_by_id(trip.scooter)

        sql = """
            INSERT INTO trips (user_id, scooter_id, start_time)
            VALUES (%s, %s, %s) RETURNING id
        """

        row = self.execute(
            sql,
            (trip.user_id, trip.scooter.id, trip.start_time),
            fetch=True
        )

        if row:
            trip._id = row[0][0]

        self.update_scooter_status(trip.scooter.id, False)
        return trip



    def end_trip(self, trip: Trip):
        trip.end_trip()
        sql = "UPDATE trips SET end_time=%s, cost=%s WHERE id=%s"
        self.execute(sql, (trip.end_time, trip.cost, trip.id))
        self.update_scooter_status(trip.scooter.id, True, trip.scooter.location)

    def get_trips_by_user(self, user_id: int):
        rows = self.execute(
            "SELECT id, user_id, scooter_id, start_time, end_time, cost FROM trips WHERE user_id=%s",
            (user_id,),
            fetch=True
        )

        trips = []
   
        for row in rows:
            trip_id, uid, scooter_id, start_time, end_time, cost = row

            scooter = self.get_scooter_by_id(scooter_id)

            trip = Trip(
                user_id=uid,
                scooter=scooter,
                start_time=start_time,
                trip_id=trip_id,
                end_time=end_time,
                cost=cost
        )

            trips.append(trip)
        return trips


    # Seed exempel data
    def seed_data(self):
        # Users
        result = self.execute("SELECT COUNT(*) FROM users", fetch=True)
        if result and result[0][0] == 0:
            self.execute("""
                INSERT INTO users (name, email, phone, balance)
                VALUES
                ('Erik Eriksson', 'erik@mail.com', '070-1234567', 100.00),
                ('Doris Eriksson', 'doran@mail.com', '070-1235566', 100.00),
                ('Lisa Fredriksson', 'lisa@mail.com', '070-7654321', 50.00)
            """)

        # Scooters
        result = self.execute("SELECT COUNT(*) FROM scooters", fetch=True)
        if result and result[0][0] == 0:
            self.execute("""
                INSERT INTO scooters (scooter_code, location, price_per_min, battery_level, is_available)
                VALUES
                ('VOI123', 'Stureplan', 3.00, 100, TRUE),
                ('VOI567', 'Hötorget', 3.00, 80, TRUE),
                ('LIME456', 'Odenplan', 4.50, 92, TRUE)
            """)
