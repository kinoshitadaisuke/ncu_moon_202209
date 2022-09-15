#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/15 12:30:06 (CST) daisuke>
#

# semimajor axis of the Moon orbit around the Earth in km
a = 384400

# eccentricity of the Moon orbit
e = 0.0549

# calculation of the greatest distance between Earth and Moon
Q = (1.0 + e) * a

# printing result of calculation
print (f'Semimajor axis of Moon orbit is {a:g} km.')
print (f'Greatest distance between Earth and Moon is {Q:g} km.')
