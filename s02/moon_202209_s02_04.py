#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/22 11:44:26 (CST) daisuke>
#

# importing astropy module
import astropy
import astropy.coordinates
import astropy.time
import astropy.units

# importing matplotlib module
import matplotlib.pyplot
import matplotlib.animation

# units
u_hr = astropy.units.hour
u_km = astropy.units.km

# setting for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('jpl')

# time to start the simulation: t0 = 2022-09-01T00:00:00 (UTC)
t0 = astropy.time.Time ('2022-09-01T00:00:00', format='isot', scale='utc')

# number of steps
n = 2400

# making an empty list for animation
frames = []

# making a fig object using matplot.pyplot.figure function
fig = matplotlib.pyplot.figure ()
    
# making an axes object using object-oriented interface
ax = fig.add_subplot (111)

for i in range (n):
    # time t
    t = t0 + i * u_hr

    # getting positions of Earth and Moon
    earth = astropy.coordinates.get_body_barycentric ('earth', t)
    moon  = astropy.coordinates.get_body_barycentric ('moon', t)

    # calculation of position of the Moon relative to the Earth
    moon_rel_x = (moon.x - earth.x) / u_km
    moon_rel_y = (moon.y - earth.y) / u_km

    # settings for plot
    ax.set_aspect ('equal')
    ax.set_xlim (-4.7*10**5, +4.7*10**5)
    ax.set_ylim (-4.7*10**5, +4.7*10**5)
    ax.set_xlabel ("X [km]")
    ax.set_ylabel ("Y [km]")
    ax.set_title ("Position of the Moon relative to the Earth")
    
    # plotting grid
    grid0, = ax.plot ([-10**6, +10**6], [0.0*10**5, 0.0*10**5], \
                      linestyle='--', color='gray', alpha=0.3)
    grid1, = ax.plot ([-10**6, +10**6], [-2.0*10**5, -2.0*10**5], \
                      linestyle='--', color='gray', alpha=0.3)
    grid2, = ax.plot ([-10**6, +10**6], [-4.0*10**5, -4.0*10**5], \
                      linestyle='--', color='gray', alpha=0.3)
    grid3, = ax.plot ([-10**6, +10**6], [+2.0*10**5, +2.0*10**5], \
                      linestyle='--', color='gray', alpha=0.3)
    grid4, = ax.plot ([-10**6, +10**6], [+4.0*10**5, +4.0*10**5], \
                      linestyle='--', color='gray', alpha=0.3)
    grid5, = ax.plot ([0.0*10**5, 0.0*10**5], [-10**6, +10**6], \
                      linestyle='--', color='gray', alpha=0.3)
    grid6, = ax.plot ([-2.0*10**5, -2.0*10**5], [-10**6, +10**6], \
                      linestyle='--', color='gray', alpha=0.3)
    grid7, = ax.plot ([-4.0*10**5, -4.0*10**5], [-10**6, +10**6], \
                      linestyle='--', color='gray', alpha=0.3)
    grid8, = ax.plot ([+2.0*10**5, +2.0*10**5], [-10**6, +10**6], \
                      linestyle='--', color='gray', alpha=0.3)
    grid9, = ax.plot ([+4.0*10**5, +4.0*10**5], [-10**6, +10**6], \
                      linestyle='--', color='gray', alpha=0.3)
    
    # plotting the Earth
    earth, = ax.plot (0.0, 0.0, marker='o', markersize=25, \
                      color='blue', label='Earth')
    text_earth = ax.text (0.0, -8.0*10**4, f'Earth')

    # plotting the Moon
    moon,  = ax.plot (moon_rel_x, moon_rel_y, marker='o', markersize=15, \
                      color='orange', label='Moon')
    text_moon = ax.text (moon_rel_x, moon_rel_y - 8.0*10**4, f'Moon')

    # plotting the time
    text_time  = ax.text (-4.55*10**5, -4.55*10**5, f'Date/Time: {t} (UTC)')

    # appending the plot to animation
    frames.append ([earth, text_earth, moon, text_moon, text_time, \
                    grid0, grid1, grid2, grid3, grid4, \
                    grid5, grid6, grid7, grid8, grid9])

# making animation
anim = matplotlib.animation.ArtistAnimation (fig, frames, interval=50)

# showing animation
#matplotlib.pyplot.show ()

# saving file
anim.save ('moon_motion.gif')
