from pydantic import BaseModel, Field
import math


class Vector3(BaseModel):
    model_config = {"extra": "ignore"}
    """
    All Coordinate must be in meters (m)
    Local Grid Coordinates might be in KM, convert before
    """
    model_config = {"extra": "ignore"}
    x: float = Field(..., description="X component")
    y: float = Field(..., description="Y component")
    z: float = Field(..., description="Z component")

    def __init__(self, x: float, y: float, z: float, *args, **kwargs):
        super(Vector3, self).__init__(x=x, y=y, z=z)
    def __add__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)
    def __sub__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)
    def __mul__(self, scalar: float) -> 'Vector3':
        return Vector3(x=self.x * scalar, y=self.y * scalar, z=self.z * scalar)
    def __truediv__(self, scalar: float) -> 'Vector3':
        if scalar == 0:
            raise ValueError("Division by zero")
        return Vector3(x=self.x / scalar, y=self.y / scalar, z=self.z / scalar)
    def __len__(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)) 
    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}"
    def cross(self, other: 'Vector3') -> 'Vector3':
        """Cross product of two vectors."""
        return Vector3(
            x=self.y * other.z - self.z * other.y,
            y=self.z * other.x - self.x * other.z,
            z=self.x * other.y - self.y * other.x
        )
    def dot(self, other: 'Vector3') -> float:
        """Dot product of two vectors."""
        return self.x * other.x + self.y * other.y + self.z * other.z
    def normalize(self) -> 'Vector3':
        """Returns a normalized vector (unit vector)."""
        length = self.__len__()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return self / length
    @property
    def values(self):
        return (self.x, self.y, self.z)
    @property
    def len(self):
        return self.__len__()
    @property
    def unitvector(self) -> 'Vector3':
        """Returns the unit vector of this vector."""
        return self.normalize()