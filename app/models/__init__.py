"""
Models paket - innehåller data models för applikationen
"""

from .user import User
from .scooter import Scooter
from .trip import Trip

__all__ = ["User", "Scooter", "Trip"]