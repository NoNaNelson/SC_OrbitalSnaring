import os, json
from src.models.planet import Planet
from src.models.system import System

# iterate through files in the "data/" directory
for file in os.listdir("src/data/"):
    l=[]
    data = None
    if file.endswith(".json") and file.startswith("raw_"):
        with open(os.path.join("src/data/", file), "r") as f:
            data = json.load(f)
    if not data:
        continue
    print(data)

    for obj in data["structured"][0]["objects"]:
        if obj["type"] == "Planet" or obj["type"] == "Moon":
            print(obj)
            l.append(Planet(**obj).model_dump())
            for moon_obj in obj["objects"]:
                if moon_obj["type"] == "Moon" or moon_obj["type"] == "Planet":
                    l.append(Planet(**moon_obj).model_dump())
                for sub_obj in obj["objects"]:
                    if sub_obj["type"] == "Moon" or sub_obj["type"] == "Planet":
                        l.append(Planet(**sub_obj).model_dump())
                        # write to file
    with open(os.path.join("src/data/", file.replace("raw_", '')), "w") as f:
        json.dump(l, f, indent=4)