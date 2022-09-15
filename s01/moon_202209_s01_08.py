#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/15 12:35:30 (CST) daisuke>
#

# apparent magnitude of the Sun
mag_sun  = -26.7

# apparent magnitude of the full Moon
mag_moon = -12.7

# comparison of brightness of the Sun and the full Moon
comparison = 10**(-0.4 * (mag_moon - mag_sun))

# printing result of calculation
print (f'Brightness of the full Moon is {comparison:g} of that of the Sun.')
