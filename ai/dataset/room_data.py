from dataclasses import dataclass
from typing import List


@dataclass
class Coordinate:
    x: float
    y: float

    def __dict__(self):
        return {"x": self.x, "y": self.y}


@dataclass
class Room:
    length: float
    width: float
    coordinates: List[Coordinate]
