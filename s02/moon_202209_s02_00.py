#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/22 10:47:26 (CST) daisuke>
#

# importing math module
import math

# value of pi
pi = math.pi

# mean distance between the Earth and the Moon in km
r_km = 384400.0

# mean distance between the Earth and the Moon in m
r    = r_km * 10**3

# Earth mass in kg
M_earth = 5.974 * 10**24

# gravitational constant
G = 6.674 * 10**-11

# calculation of orbital period of the Moon
T = math.sqrt ( (4.0 * pi**2 * r**3) / (G * M_earth) )

# orbital period of the Moon in hr
T_hr = T / 3600.0

# orbital period of the Moon in day
T_day = T_hr / 24.0

# printing result of calculation
print (f'orbital period of the Moon:')
print (f'  T = {T:g} sec')
print (f'    = {T_hr:g} hr')
print (f'    = {T_day:g} day')
