#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/29 12:38:40 (CST) daisuke>
#

# importing sys module
import sys

# importing astropy module
import astropy
import astropy.coordinates
import astropy.time
import astropy.units

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# units
u_au = astropy.units.au

# setting for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('jpl')

# asking the user to type year, month, day, hour, minute, second
try:
    YYYY = int (input ('Year in UTC: '))
except:
    print (f'Type an integer for Year.')
    sys.exit (1)
try:
    MM   = int (input ('Month in UTC: '))
except:
    print (f'Type an integer for Month.')
    sys.exit (1)
try:
    DD   = int (input ('Day in UTC: '))
except:
    print (f'Type an integer for Day.')
    sys.exit (1)
try:
    hh   = int (input ('hour in UTC: '))
except:
    print (f'Type an integer for hour.')
    sys.exit (1)
try:
    mm   = int (input ('minute in UTC: '))
except:
    print (f'Type an integer for minute.')
    sys.exit (1)
try:
    ss   = int (input ('second in UTC: '))
except:
    print (f'Type an integer for second.')
    sys.exit (1)

# date/time
t_str = f'{YYYY:04d}-{MM:02d}-{DD:02d}T{hh:02d}:{mm:02d}:{ss:02d}'
    
# time t = 2023-01-01T12:00:00 (UTC) = 2023-01-01T20:00:00 (Taiwan)
t = astropy.time.Time (t_str, format='isot', scale='utc')

# getting positions of Sun, Earth, and Moon
sun     = astropy.coordinates.get_body_barycentric ('sun', t)
mercury = astropy.coordinates.get_body_barycentric ('mercury', t)
venus   = astropy.coordinates.get_body_barycentric ('venus', t)
earth   = astropy.coordinates.get_body_barycentric ('earth', t)
mars    = astropy.coordinates.get_body_barycentric ('mars', t)

# printing positions of the Sun and planets
print (f'Positions of the Sun and the planets at t = {t}')
print (f'  Sun:')
print (f'    X = {sun.x} = {sun.x.to (u_au)}')
print (f'    Y = {sun.y} = {sun.y.to (u_au)}')
print (f'    Z = {sun.z} = {sun.z.to (u_au)}')
print (f'  Mercury:')
print (f'    X = {mercury.x} = {mercury.x.to (u_au)}')
print (f'    Y = {mercury.y} = {mercury.y.to (u_au)}')
print (f'    Z = {mercury.z} = {mercury.z.to (u_au)}')
print (f'  Venus:')
print (f'    X = {venus.x} = {venus.x.to (u_au)}')
print (f'    Y = {venus.y} = {venus.y.to (u_au)}')
print (f'    Z = {venus.z} = {venus.z.to (u_au)}')
print (f'  Earth:')
print (f'    X = {earth.x} = {earth.x.to (u_au)}')
print (f'    Y = {earth.y} = {earth.y.to (u_au)}')
print (f'    Z = {earth.z} = {earth.z.to (u_au)}')
print (f'  Mars:')
print (f'    X = {mars.x} = {mars.x.to (u_au)}')
print (f'    Y = {mars.y} = {mars.y.to (u_au)}')
print (f'    Z = {mars.z} = {mars.z.to (u_au)}')

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# settings for plot
ax.set_aspect ('equal')
ax.set_xlim (-2.0, +2.0)
ax.set_ylim (-2.0, +2.0)
ax.set_xlabel ("X [au]")
ax.set_ylabel ("Y [au]")
ax.set_title ("Positions of the Sun and planets")

# plotting the Sun
ax.plot (sun.x.to (u_au) / u_au, sun.y.to (u_au) / u_au, \
         marker='o', markersize=25, color='yellow', label='Sun')
ax.text (sun.x.to (u_au) / u_au + 0.1, sun.y.to (u_au) / u_au - 0.3, \
         f'Sun')

# plotting Mercury
ax.plot (mercury.x.to (u_au) / u_au, mercury.y.to (u_au) / u_au, \
         marker='o', markersize=5, color='orange', label='Mercury')
ax.text (mercury.x.to (u_au) / u_au + 0.1, mercury.y.to (u_au) / u_au - 0.3, \
         f'Mercury')

# plotting Venus
ax.plot (venus.x.to (u_au) / u_au, venus.y.to (u_au) / u_au, \
         marker='o', markersize=15, color='green', label='Venus')
ax.text (venus.x.to (u_au) / u_au + 0.1, venus.y.to (u_au) / u_au - 0.3, \
         f'Venus')

# plotting Earth
ax.plot (earth.x.to (u_au) / u_au, earth.y.to (u_au) / u_au, \
         marker='o', markersize=15, color='blue', label='Earth')
ax.text (earth.x.to (u_au) / u_au + 0.1, earth.y.to (u_au) / u_au - 0.3, \
         f'Earth')

# plotting Mars
ax.plot (mars.x.to (u_au) / u_au, mars.y.to (u_au) / u_au, \
         marker='o', markersize=10, color='red', label='Mars')
ax.text (mars.x.to (u_au) / u_au + 0.1, mars.y.to (u_au) / u_au - 0.3, \
         f'Mars')

# plotting the time
ax.text (-1.9, -1.9, f'Date/Time: {t} (UTC)')

# grid
ax.grid ()

# saving plot
fig.savefig ('solsys_iss.png', dpi=225)
