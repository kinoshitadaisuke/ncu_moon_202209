#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/15 12:31:25 (CST) daisuke>
#

# semimajor axis of the Moon orbit around the Earth in km
a = 384400

# eccentricity of the Moon orbit
e = 0.0549

# calculation of the least distance between Earth and Moon
q = (1.0 - e) * a

# printing result of calculation
print (f'Semimajor axis of Moon orbit is {a:g} km.')
print (f'Least distance between Earth and Moon is {q:g} km.')
