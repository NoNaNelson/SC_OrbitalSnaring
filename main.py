#!/usr/bin/env python3
import argparse
from build_data import load_data
from src.calcs import orbital_pos_verification

parser = argparse.ArgumentParser()
STANTON, PYRO = load_data()

# #-db DATABASE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-x", "--xcoord", help="Local X Coordinate", type=float)
parser.add_argument("-y", "--ycoord", help="Local Y Coordinate", type=float)
parser.add_argument("-z", "--zcoord", help="Local Z Coordinate", type=float)
parser.add_argument("-p", "--planet", help="Selected Planet", type=str)
parser.add_argument("-s", "--start", help="Start OM (1-6)", type=int)
parser.add_argument("-e", "--end", help="End OM (1-6)", type=int)



def main():
    args = parser.parse_args()
    for system in load_data():
        if args.planet in system:
            planet = system[args.planet]    
            print(f"Selected Planet: {planet.name}")
            orbital_pos_verification( x=args.xcoord, y=args.ycoord, z=args.zcoord, start_om=planet.oms[args.start - 1], end_om=planet.oms[args.end - 1])


if  __name__ == "__main__":
    main()
