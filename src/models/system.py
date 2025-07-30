import json
from typing import List
from pydantic import BaseModel, Field

from src.models.planet import Planet

class System(BaseModel):
    name: str
    
    planets: List[Planet]



        
    
    


if  __name__ == "__main__":
    with open("../data/stanton.json", "r") as f:
            data = json.load(f)
    print(System(name="Stanton", planets=data).model_dump())