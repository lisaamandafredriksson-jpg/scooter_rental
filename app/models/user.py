from decimal import Decimal

class User:
    def __init__(self, user_id: int | None, name: str, email: str, phone: str, balance: float = 0):
        self._id = user_id
        self._name = name
        self._email = email
        self._phone = phone
        self._balance = Decimal(balance)  

    # Getters 
    @property
    def id(self) -> int | None:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def balance(self) -> Decimal:
        return self._balance

    # Affärslogik
    def add_balance(self, amount: float | Decimal) -> None:
        """Ladda saldo. Belopp måste vara större än 0"""
        amount = Decimal(amount)
        if amount <= 0:
            raise ValueError("Beloppet måste vara större än 0")
        self._balance += amount

    def deduct_balance(self, amount: float | Decimal) -> None:
        """Dra pengar från saldo. Fel om inte tillräckligt saldo"""
        amount = Decimal(amount)
        if amount <= 0:
            raise ValueError("Beloppet måste vara större än 0")
        if self._balance < amount:
            raise ValueError("Otillräckligt saldo")
        self._balance -= amount

    # Tillgänglighet
    def __str__(self) -> str:
        return f"{self._id}: {self._name} - saldo {self._balance:.2f} kr"
