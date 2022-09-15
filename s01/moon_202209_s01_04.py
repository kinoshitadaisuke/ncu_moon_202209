#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/15 12:22:45 (CST) daisuke>
#

# importing math modue
import math

# value of pi
pi = math.pi

# Moon size in km
diameter_moon = 3476

# Earth-Moon distance in km
distance      = 384400

# calculation of angular diameter of the Moon as seen from the Earth
a_rad    = diameter_moon / distance
a_deg    = a_rad * 180.0 / pi
a_arcmin = a_deg * 60.0

# printing result of calculation
print (f'Moon diameter is {diameter_moon} km.')
print (f'Earth-Moon distance is {distance} km.')
print (f'Angular size of Moon is {a_deg:4.2f} deg = {a_arcmin:2.0f} arcmin.')
