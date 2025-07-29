from src.models.vector import Vector3
from src.models.planet import Planet
from enum import Enum
from typing import List

class System(Enum):

    @classmethod
    def name(cls) -> str:
        """Return the name of the system."""
        return cls.__name__
    @classmethod
    def __iter__(cls):
        return iter(cls.__members__.values())
    
    @classmethod
    def default_planet(cls) -> Planet:
        """Return the first planet in the system, if available."""
        return cls.planets()[0]
    
    @classmethod
    def planets(cls) -> List[Planet]:
        return [member.value for member in cls.__members__.values() if isinstance(member.value, Planet)]
    

if  __name__ == "__main__":
    # Example usage
    sun = System(data={
        "name": "Sun",
        "x": 0,
        "y": 0,
        "z": 0,
        "rotation_speed": 1,
        "type": "Star"
    })