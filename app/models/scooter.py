class Scooter:
    def __init__(
        self,
        scooter_id: int,
        scooter_code: str,
        location: str,
        price_per_min: float,
        battery_level: int = 100,
        is_available: bool = True
    ):
        self._id = scooter_id
        self._scooter_code = scooter_code
        self._location = location
        self._price_per_min = price_per_min
        self._battery_level = battery_level
        self._is_available = is_available

    # Getters
    @property
    def id(self) -> int:
        return self._id

    @property
    def scooter_code(self) -> str:
        return self._scooter_code

    @property
    def location(self) -> str:
        return self._location

    @property
    def price_per_min(self) -> float:
        return self._price_per_min

    @property
    def battery_level(self) -> int:
        return self._battery_level

    @property
    def is_available(self) -> bool:
        return self._is_available

    # Affärslogik
    def rent(self) -> None:
        if not self._is_available:
            raise ValueError("Scootern är redan uthyrd")
        self._is_available = False

    def release(self, new_location: str) -> None:
        self._is_available = True
        self._location = new_location

    def drain_battery(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Batteriförbrukning kan inte vara negativ")
        self._battery_level = max(0, self._battery_level - amount)

    # Tillgänglighet
    def __str__(self) -> str:
        status = "Ledig" if self._is_available else "Uthyrd"
        return (
            f"Scooter(id={self._id}, "
            f"code='{self._scooter_code}', "
            f"location='{self._location}', "
            f"status={status}, "
            f"price={self._price_per_min} kr/min)"
        )