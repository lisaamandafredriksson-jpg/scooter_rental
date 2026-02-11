# main.py
from services.database import Database
from models.user import User
from models.scooter import Scooter
from models.trip import Trip
from ui.menu import show_menu, get_menu_choice
from datetime import datetime
import sys

def main():
    db = Database()
    trips_in_progress = {}  # user_id -> Trip

    while True:
        show_menu()
        choice = get_menu_choice()
        if choice == -1:
            continue

        # -------------------- 1. Registrera ny användare --------------------
        if choice == 1:
            name = input("Namn: ")
            email = input("Email: ")
            phone = input("Telefon: ")
            user = User(None, name, email, phone, 0)
            db.create_user(user)
            print(f"Användare registrerad: {user}")

        # -------------------- 2. Visa alla användare --------------------
        elif choice == 2:
            users = db.get_all_users()
            if not users:
                print("Inga användare registrerade.")
                continue
            for user in users:
                print(f"{user.id}: {user.name} - saldo {user.balance:.2f} kr")

        # -------------------- 3. Ladda saldo --------------------
        elif choice == 3:
            users = db.get_all_users()
            if not users:
                print("Inga användare registrerade.")
                continue
            for user in users:
                print(f"{user.id}: {user.name} - saldo {user.balance:.2f} kr")
            user_id = int(input("Välj user_id för att ladda saldo: "))
            user = db.get_user_by_id(user_id)
            if not user:
                print("Felaktigt user_id")
                continue
            amount = float(input("Belopp att ladda: "))
            try:
                user.add_balance(amount)
                db.update_user_balance(user.id, user.balance)
                print(f"Nytt saldo: {user.balance:.2f} kr")
            except ValueError as e:
                print(e)

        # -------------------- 4. Lägg till elsparkcykel --------------------
        elif choice == 4:
            code = input("Scooter code: ")
            location = input("Plats: ")
            price = float(input("Pris per minut: "))
            scooter = Scooter(None, code, location, price)
            db.create_scooter(scooter)
            print(f"Scooter tillagd: {scooter}")

        # -------------------- 5. Visa lediga scooters --------------------
        elif choice == 5:
            scooters = db.get_available_scooters()
            if not scooters:
                print("Inga lediga scooters.")
                continue
            for s in scooters:
                print(f"{s.id}: {s.scooter_code} - plats {s.location} - {s.price_per_min} kr/min")

        # -------------------- 6. Starta resa --------------------
        elif choice == 6:
            users = db.get_all_users()
            if not users:
                print("Inga användare registrerade.")
                continue
            for user in users:
                print(f"{user.id}: {user.name}")
            user_id = int(input("Välj user_id: "))
            user = db.get_user_by_id(user_id)
            if not user:
                print("Felaktigt user_id")
                continue

            scooters = db.get_available_scooters()
            if not scooters:
                print("Inga lediga scooters")
                continue
            for s in scooters:
                print(f"{s.id}: {s.scooter_code} - plats {s.location} - {s.price_per_min} kr/min")
            scooter_id = int(input("Välj scooter_id: "))
            scooter = db.get_scooter_by_id(scooter_id)
            if not scooter or not scooter.is_available:
                print("Scootern är inte tillgänglig")
                continue


            trip = Trip(
                user_id=user.id,
                scooter=scooter
            )

            db.start_trip(trip)
            trips_in_progress[user.id] = trip
            print(f"Resan startad: {trip}")

        # -------------------- 7. Avsluta resa --------------------
        elif choice == 7:
            if not trips_in_progress:
                print("Inga pågående resor")
                continue
            for uid, trip in trips_in_progress.items():
                print(f"{uid}: {trip.scooter.scooter_code} start {trip.start_time}")
            user_id = int(input("Välj user_id för att avsluta resa: "))
            if user_id not in trips_in_progress:
                print("Felaktigt user_id")
                continue

            trip = trips_in_progress.pop(user_id)
            db.end_trip(trip)
            user = db.get_user_by_id(user_id)
            try:
                user.deduct_balance(trip.cost)
                db.update_user_balance(user.id, user.balance)
                print(f"Resan avslutad. Kostnad: {trip.cost:.2f} kr. Nytt saldo: {user.balance:.2f} kr")
            except ValueError as e:
                print(e)

        # -------------------- 8. Visa mina resor --------------------
        elif choice == 8:
            users = db.get_all_users()
            if not users:
                print("Inga användare registrerade.")
                continue
            for user in users:
                print(f"{user.id}: {user.name}")
            user_id = int(input("Välj user_id för att se resor: "))
            trips = db.get_trips_by_user(user_id)
            if not trips:
                print("Inga resor")
                continue
            for trip in trips:
                scooter_code = trip.scooter.scooter_code if trip.scooter else "Okänd"
                start_time = trip.start_time
                end_time = trip.end_time if trip.end_time else "Pågår"
                cost = f"{trip.cost:.2f}" if trip.cost is not None else "-"
                print(f"Trip(id={trip.id}, user_id={trip.user_id}, scooter={scooter_code}, start={start_time}, end={end_time}, cost={cost})")

        # -------------------- 9. Avsluta program --------------------
        elif choice == 9:
            print("Avslutar programmet...")
            db.close()
            sys.exit()


if __name__ == "__main__":
    main()
