#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/15 12:26:27 (CST) daisuke>
#

# importing math modue
import math

# value of pi
pi = math.pi

# solar radius in km
radius_sun   = 6.96 * 10**5
diameter_sun = radius_sun * 2.0

# Sun-Earth distance (1 astronomical unit) in km
distance     = 1.496 * 10**8

# calculation of angular diameter of the Sun as seen from the Earth
a_rad    = diameter_sun / distance
a_deg    = a_rad * 180.0 / pi
a_arcmin = a_deg * 60.0

# printing result of calculation
print (f'Solar diameter is {diameter_sun:g} km.')
print (f'Sun-Earth distance is {distance:g} km.')
print (f'Angular size of Sun is {a_deg:4.2f} deg = {a_arcmin:2.0f} arcmin.')
