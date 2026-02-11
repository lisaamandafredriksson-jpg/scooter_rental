from datetime import datetime
from math import ceil
from models.scooter import Scooter

class Trip:
    def __init__(
        self,
        user_id: int,
        scooter: Scooter,
        start_time: datetime | None = None,
        trip_id: int | None = None,
        end_time: datetime | None = None,
        cost: float | None = None
    ):
        self._id = trip_id
        self._user_id = user_id
        self._scooter = scooter
        self._start_time = start_time or datetime.now()
        self._end_time = end_time
        self._cost = cost

    # Getters
    @property
    def id(self) -> int | None:
        return self._id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def scooter(self) -> Scooter:
        return self._scooter

    @property
    def start_time(self) -> datetime:
        return self._start_time

    @property
    def end_time(self) -> datetime | None:
        return self._end_time

    @property
    def cost(self) -> float | None:
        return self._cost

    # Affärslogik
    def end_trip(self) -> float:
        if self._end_time is not None:
            raise ValueError("Resan är redan avslutad")

        self._end_time = datetime.now()
        duration_minutes = ceil(
            (self._end_time - self._start_time).total_seconds() / 60
        )

        self._cost = duration_minutes * self._scooter.price_per_min
        return self._cost

    # Tillgänglighet
    def __str__(self) -> str:
        end_time = self._end_time.strftime("%Y-%m-%d %H:%M") if self._end_time else "Pågår"
        cost = f"{self._cost:.2f} kr" if self._cost is not None else "-"
        return (
            f"Trip(id={self._id}, "
            f"user_id={self._user_id}, "
            f"scooter={self._scooter.scooter_code}, "
            f"start={self._start_time.strftime('%Y-%m-%d %H:%M')}, "
            f"end={end_time}, "
            f"cost={cost})"
        )

