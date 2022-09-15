#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/15 12:18:15 (CST) daisuke>
#

# Earth mass in kg
mass_earth = 5.974 * 10**24

# Moon mass in kg
mass_moon  = 7.349 * 10**22

# comparison of Earth and Moon masses
comparison = mass_moon / mass_earth * 100.0

# printing result of calculation
print (f'Earth mass is {mass_earth} kg.')
print (f'Moon mass is {mass_moon} kg.')
print (f'Moon mass is {comparison:4.1f} percent of Earth mass.')
