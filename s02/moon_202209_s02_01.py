#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/22 10:47:41 (CST) daisuke>
#

# importing astropy module
import astropy
import astropy.coordinates
import astropy.time
import astropy.units

# units
u_hr = astropy.units.hour

# setting for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('jpl')

# time t = 2022-09-01T00:00:00 (UTC)
t = astropy.time.Time ('2022-09-22T12:00:00', format='isot', scale='utc')


# getting positions of Sun, Earth, and Moon
earth = astropy.coordinates.get_body_barycentric ('earth', t)
moon  = astropy.coordinates.get_body_barycentric ('moon', t)

# calculation of position of the Moon relative to the Earth
moon_rel_x = moon.x - earth.x
moon_rel_y = moon.y - earth.y

# printing positions of Earth and Moon
print (f'Positions of the Earth and the Moon at t = {t}')
print (f'  Earth : {earth}')
print (f'  Moon  : {moon}')

print (f'')

print (f'Positions of the Moon relative to the Earth at X-Y plane')
print (f'  Moon  : ({moon_rel_x}, {moon_rel_y})')
