def show_menu() -> None:
    print("\n====== Elsparkcykel-uthyrning 🛴 ======")
    print("[1] Registrera ny användare")
    print("[2] Visa alla användare")
    print("[3] Ladda saldo")
    print("[4] Lägg till elsparkcykel")
    print("[5] Visa lediga elsparkcyklar")
    print("[6] Starta resa")
    print("[7] Avsluta resa")
    print("[8] Visa mina resor")
    print("[9] Avsluta programmet")
    print("=====================================\n")


def get_menu_choice() -> int:
    try:
        choice = int(input("Välj ett alternativ (1-9): \n"))
        if 1 <= choice <= 9:
            return choice
        else:
            print("❌ Ogiltigt val. Välj mellan 1 och 9.\n")
            return -1
    except ValueError:
        print("❌ Du måste skriva en siffra.\n")
        return -1