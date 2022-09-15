#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/15 12:15:52 (CST) daisuke>
#

# importing math module
import math

# value of pi
pi = math.pi

# Earth diameter in km
diameter_earth = 12756

# Moon diameter in km
diameter_moon  = 3476

# calculation of Earth volume
volume_earth = 4.0 / 3.0 * pi * (diameter_earth * 10**3 / 2.0)**3

# calculation of Moon volume
volume_moon = 4.0 / 3.0 * pi * (diameter_moon * 10**3 / 2.0)**3

# comparison of Earth and Moon volumes
comparison = volume_moon / volume_earth * 100.0

# printing result of calculation
print (f'Earth volume is {volume_earth:g} m^3.')
print (f'Moon volume is {volume_moon:g} m^3.')
print (f'Moon volume is {comparison:4.1f} percent of Earth volume.')
