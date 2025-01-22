from dataclasses import dataclass, field
from typing import List


@dataclass
class Coordinate:
    x: float
    y: float

    def to_dict(self):
        return {"x": self.x, "y": self.y}


@dataclass
class Room:
    """Represents a room with dimensions and light positions.

    Attributes:
        length: Room length in meters
        width: Room width in meters
        coordinates: List of coordinates defining room shape
        lights: List of light positions, defaults to empty list
    """

    length: float
    width: float
    coordinates: List[Coordinate]
    lights: List[Coordinate] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert room to dictionary representation."""
        return {
            "length": self.length,
            "width": self.width,
            "coordinates": [coord.to_dict() for coord in self.coordinates],
            "lights": [coord.to_dict() for coord in self.lights] if self.lights else [],
        }
