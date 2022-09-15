#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/15 12:05:36 (CST) daisuke>
#

# Earth size in km
diameter_earth = 12756

# Moon size in km
diameter_moon  = 3476

# comparison of Earth and Moon sizes
comparison = diameter_moon / diameter_earth * 100.0

# printing result of calculation
print (f'Earth diameter is {diameter_earth} km.')
print (f'Moon diameter is {diameter_moon} km.')
print (f'Moon size is {comparison:4.1f} percent of Earth size.')
