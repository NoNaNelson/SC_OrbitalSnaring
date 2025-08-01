# Orbital Snaring

Ever wanted to snare from an OM > OM marler but arnt sure if you are still on route?
No Worries, my orbital snaring tool got you covered!

## Installation

### Python

    Version 3.13.5

### Clone the repo

    git clone https://github.com/NoNaNelson/SC_OrbitalSnaring.git

### (Optional) Create a virtual enviroment

    python3 -m venv venv
    source venv/bin/activate

### Install dependencies

    pip install -r requirements.txt
    

## Usage

    ./main.py -x <x coord> -y <y coord> -z <z coord> -p <planet> -s <start OM> -e <end OM>
    

* `-x` : X coordinate of your current position
* `-y` : Y coordinate of your current position
* `-z` : Z coordinate of your current position
* `-p` : Name of the planet (e.g., Yela)
* `-s` : Starting Orbital Marker (OM) number
* `-e` : Ending Orbital Marker (OM) number

## Examples

1.

    ./main.py -x 6699 -y -8000  -z 440000 -p Yela -s 1 -e 3


2.

> Distance to selected route: 5289.16m

    ./main.py -x 14050 -y -50  -z -220 -p Yela -s 3 -e 4

> 
