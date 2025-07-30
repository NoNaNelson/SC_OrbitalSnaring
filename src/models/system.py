import json
from typing import List, Dict, Any, Optional
from enum import Enum
from pydantic import BaseModel, Field

from src.models.planet import Planet

class System(BaseModel):
    name: str
    model_config = {"extra": "ignore"}
    planets: List[Planet] 


    def _get(self, name: str) -> Optional[Planet]:
        """Returns a specific planet by name."""
        for item in self.planets:
            if item.name == name:
                return item
        return None
    
    def __getitem__(self, name: str) -> Planet:
        """Allows access to planets using the bracket notation."""
        _item = self._get(name)
        if _item is None:
            raise KeyError(f"Planet '{name}' not found in system '{self.name}'.")

        return _item


if  __name__ == "__main__":
    with open("../data/stanton.json", "r") as f:
            data = json.load(f)
    print(System(name="Stanton", planets=data).model_dump())