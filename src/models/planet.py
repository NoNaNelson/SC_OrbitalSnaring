from src.models.vector import Vector3
from pydantic import BaseModel, Field
from typing import Optional, Literal, List

class Planet(BaseModel):
    model_config = {"extra": "ignore"}

    type: Literal['Planet', 'Moon']
    name: str
    designation: str
    grid_range: float
    om_range: float
    min_qt_range: float
    dropout_distance: float
    rotation_speed: float
    x: float
    y: float
    z: float

    parent: Optional[str] = None  # Optional parent Planet name, if exists
    # name: str
    # x: float
    # y: float
    # z: float
    # rotation_speed: float
    # parent: Optional['Planet'] = None  # Reference to the parent Planet if exists
    # type: Literal['Planet', 'Moon']

    @property
    def has_parent(self) -> bool:
        return self.parent is not None
    
    def __init__(self, *args, **kwargs):
        super(Planet, self).__init__(*args, **kwargs)
        if self.has_parent:
            # update x, y, z to be relative to global
            self.x += self.parent.x #type: ignore
            self.y += self.parent.y #type: ignore
            self.z += self.parent.z #type: ignore
    @property
    def vector(self) -> Vector3:
        return Vector3(x=self.x, y=self.y, z=self.z)

    @property
    def oms(self) -> List[Vector3]:
        return [self.OM1, self.OM2, self.OM3, self.OM4, self.OM5, self.OM6]
    
    @property
    def OM1(self) -> Vector3:
        return Vector3(0, 0, self.om_range)
    @property
    def OM2(self) -> Vector3:
        return Vector3(0, 0, -self.om_range)
    @property
    def OM3(self) -> Vector3:
        return Vector3(0, self.om_range, 0)
    @property
    def OM4(self) -> Vector3:
        return Vector3(0, -self.om_range, 0)
    @property
    def OM5(self) -> Vector3:
        return Vector3(self.om_range, 0, 0)
    @property
    def OM6(self) -> Vector3:
        return Vector3(-self.om_range, 0, 0)