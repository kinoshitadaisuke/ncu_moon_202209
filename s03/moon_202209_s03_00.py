#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/29 12:08:23 (CST) daisuke>
#

# importing astropy module
import astropy
import astropy.coordinates
import astropy.time
import astropy.units

# setting for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('jpl')

# time t = 2022-09-29T12:00:00 (UTC) = 2022-09-30T20:00:00 (Taiwan)
t = astropy.time.Time ('2022-09-29T12:00:00', format='isot', scale='utc')


# getting positions of Sun, Earth, and Moon
sun     = astropy.coordinates.get_body_barycentric ('sun', t)
mercury = astropy.coordinates.get_body_barycentric ('mercury', t)
venus   = astropy.coordinates.get_body_barycentric ('venus', t)
earth   = astropy.coordinates.get_body_barycentric ('earth', t)
mars    = astropy.coordinates.get_body_barycentric ('mars', t)

# printing positions of the Sun and planets
print (f'Positions of the Sun and the planets at t = {t}')
print (f'  Sun     : {sun}')
print (f'  Mercury : {mercury}')
print (f'  Venus   : {venus}')
print (f'  Earth   : {earth}')
print (f'  Mars    : {mars}')
