import json
from src.models.system import System
from build_data import load_data
from src.calcs import orbital_pos_verification

if  __name__ == "__main__":
    STANTON, PYRO = load_data()
    systems = {"Stanton": STANTON, "Pyro": PYRO}
    system = input("System (Stanton/Pyro): ")
    system_obj = systems[system]
    # x,y,z
    print("all units in meters please")
    print("Currenct location in local coordinates:")
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("z: "))

    planet_name = input("Planet name: ")
    planet = system_obj[planet_name]

    start = input("start at: ")
    end = input("end at: ")
    
    selected_start_om = planet.oms[int(start) + 1]
    selected_end_om = planet.oms[int(end) + 1]
    print("Start/End ", selected_start_om, selected_end_om)
    print("x, y, z: ", x, y, z)
    print("Planet: ", planet.name)

    orbital_pos_verification(x, y, z, planet, start_om=selected_start_om, end_om=selected_end_om)