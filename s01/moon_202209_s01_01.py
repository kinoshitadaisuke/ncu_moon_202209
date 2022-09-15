#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/15 12:11:53 (CST) daisuke>
#

# Jupiter size in km
diameter_jupiter  = 142984

# Ganymede size in km
diameter_ganymede = 5268

# comparison of Jupiter and Ganymede sizes
comparison = diameter_ganymede / diameter_jupiter * 100.0

# printing result of calculation
print (f'Jupiter diameter is {diameter_jupiter} km.')
print (f'Ganymede diameter is {diameter_ganymede} km.')
print (f'Ganymede size is {comparison:4.1f} percent of Jupiter size.')
