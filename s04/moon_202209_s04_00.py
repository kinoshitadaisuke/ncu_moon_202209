#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/06 13:31:31 (CST) daisuke>
#

# importing sys module
import sys

# importing numpy module
import numpy

# importing astropy module
import astropy
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.animation
import matplotlib.backends.backend_agg
import matplotlib.figure

# file prefix
file_prefix = 'moon_3d'

# file extension
file_ext = 'png'

# definition of a function for making a sphere
def make_sphere (x_c, y_c, z_c, radius, colour):
    u = numpy.linspace (0, 2 * numpy.pi, 1000)
    v = numpy.linspace (0, numpy.pi, 1000)
    x = radius * numpy.outer (numpy.cos(u), numpy.sin(v)) + x_c
    y = radius * numpy.outer (numpy.sin(u), numpy.sin(v)) + y_c
    z = radius * numpy.outer (numpy.ones(numpy.size(u)), numpy.cos(v)) + z_c
    # plotting the surface
    sphere = ax.plot_surface (x, y, z, color=colour, antialiased=False, \
                               shade=True, rcount=100, ccount=100)
    return (sphere)

# units
u_au = astropy.units.au
u_km = astropy.units.kilometer
u_hr = astropy.units.hour

# number of animation frames to generate
n_steps = 3000

# step size in hr
step_hr  = 3
step_str = f'{step_hr}h'
step     = step_hr * u_hr

# date/time to start the simulation
t_start_str = f'2022-07-01T00:00:00.000'
    
# time to start the simulation in astropy.time object
t_start = astropy.time.Time (t_start_str, format='isot', scale='utc')

# time to stop the simulation in astropy.time object
t_stop  = t_start + step * n_steps

# an empty list to store positions of the Earth and the Moon
list_obj = []

# getting positions of the Earth from JPL/Horizons
print (f'Now, getting positions of the Earth...')
query = astroquery.jplhorizons.Horizons (id_type=None, id=f'399', \
                                         location='@0', \
                                         epochs={'start': t_start.iso, \
                                                 'stop': t_stop.iso, \
                                                 'step': step_str})
vec_earth = query.vectors ()
print (vec_earth.info)
print (vec_earth)
print (f'Finished getting positions of the Earth!')

# getting positions of the Moon from JPL/Horizons
print (f'Now, getting positions of the Moon...')
query = astroquery.jplhorizons.Horizons (id_type=None, id=f'301', \
                                         location='@0', \
                                         epochs={'start': t_start.iso, \
                                                 'stop': t_stop.iso, \
                                                 'step': step_str})
vec_moon = query.vectors ()
print (vec_moon.info)
print (vec_moon)
print (f'Finished getting positions of the Moon!')

print (f'Earth positions:')
for i in range ( len (vec_earth) ):
    print (f'  {vec_earth["datetime_str"][i]}', \
           f'{vec_earth["x"][i]:+12.9f}', \
           f'{vec_earth["y"][i]:+12.9f}', \
           f'{vec_earth["z"][i]:+12.9f}', \
           )
    
print (f'Moon positions:')
for i in range ( len (vec_moon) ):
    if (i % 100 != 0):
        continue
    print (f'  {vec_moon["datetime_str"][i]}', \
           f'{vec_moon["x"][i]:+12.9f}', \
           f'{vec_moon["y"][i]:+12.9f}', \
           f'{vec_moon["z"][i]:+12.9f}', \
           )
    
# relative positions of the Moon with respect to the Earth
moon_rel_x = (vec_moon['x'] - vec_earth['x']) * u_au
moon_rel_y = (vec_moon['y'] - vec_earth['y']) * u_au
moon_rel_z = (vec_moon['z'] - vec_earth['z']) * u_au

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure (figsize=[15.36, 8.64])
fig.subplots_adjust (left=0.0, right=1.0, bottom=0.0, top=1.0, \
                     wspace=0.0, hspace=0.0)

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
#ax = fig.add_subplot (111, projection='3d')
ax = fig.add_axes ( (0, 0, 1, 1), projection='3d')

# an empty list of frames for animation
list_frame = []

# initial value of 'elev' angle
el0 = 90.0

# initial value of 'azim' angle
az0 = -90.0

# initial value of 'dist'
dist0 = 10.0

for i in range (n_steps):
    # printing status
    print (f'Now, making the frame ID {i:06d}...')
    
    # empty list for orbital path
    list_orb_x = []
    list_orb_y = []
    list_orb_z = []

    # orbital path of Moon
    if (i < 219):
        for j in range (i + 1):
            list_orb_x.append (moon_rel_x[j].to (u_km) / u_km)
            list_orb_y.append (moon_rel_y[j].to (u_km) / u_km)
            list_orb_z.append (moon_rel_z[j].to (u_km) / u_km)
    else:
        for j in range (i - 219, i + 1):
            list_orb_x.append (moon_rel_x[j].to (u_km) / u_km)
            list_orb_y.append (moon_rel_y[j].to (u_km) / u_km)
            list_orb_z.append (moon_rel_z[j].to (u_km) / u_km)

    # elevation, azimuth, and distance of camera
    if (i < 300):
        el   = el0
        az   = az0
        dist = dist0
    elif ( (i >= 300) and (i < 750) ):
        el   = el0 - (i - 300) * 0.2
        az   = az0
        dist = dist0
    elif ( (i >= 750) and (i < 1050) ):
        el   = el0 - 90.0
        az   = az0
        dist = dist0
    elif ( (i >= 1050) and (i < 1350) ):
        el   = el0 - 90.0 + (i - 1050) * 0.15
        az   = az0
        dist = dist0
    elif ( (i >= 1350) and (i < 1650) ):
        el   = el0 - 45.0
        az   = az0
        dist = dist0 - (i - 1350) * 0.01
    elif ( (i >= 1650) and (i < 1950) ):
        el   = el0 - 45.0
        az   = az0
        dist = dist0 - 3.0
    elif ( (i >= 1950) and (i < 2250) ):
        el   = el0 - 45.0 - (i - 1950) * 0.1
        az   = az0
        dist = dist0 - 3.0 - (i - 1950) * 0.005
    elif ( (i >= 2250) and (i < 2550) ):
        el   = el0 - 75.0
        az   = az0
        dist = dist0 - 4.5
    elif ( (i >= 2550) and (i < 2850) ):
        el   = el0 - 75.0 + (i - 2550) * 0.2
        az   = az0
        dist = dist0 - 4.5 + (i - 2550) * 0.01
    elif ( (i >= 2850) and (i < 3000) ):
        el   = el0 - 15.0
        az   = az0
        dist = dist0 - 1.5
    
    # clearing previous axes
    ax.cla ()
    
    # time t
    t = t_start + i * step

    # settings for plot
    ax.set_xlim3d (-6.0*10**5, +6.0*10**5)
    ax.set_ylim3d (-6.0*10**5, +6.0*10**5)
    ax.set_zlim3d (-1.0*10**5, +1.0*10**5)
    ax.set_box_aspect ( (6.0, 6.0, 1.0) )

    # projection
    ax.set_proj_type ('persp')

    # using black background colour
    #fig.set_facecolor ('black')
    fig.set_facecolor ('white')
    ax.set_facecolor ('black')
    ax.grid (False)
    ax.w_xaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))
    ax.w_yaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))
    ax.w_zaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))

    # Earth
    earth = make_sphere (0.0, 0.0, 0.0, 6371.0 * 7.0, 'dodgerblue')

    # Moon
    moon = make_sphere (moon_rel_x[i].to (u_km) / u_km, \
                        moon_rel_y[i].to (u_km) / u_km, \
                        moon_rel_z[i].to (u_km) / u_km, \
                        1737.0 * 10.0, 'lemonchiffon')

    # plotting orbital path
    orb_x = numpy.array (list_orb_x)
    orb_y = numpy.array (list_orb_y)
    orb_z = numpy.array (list_orb_z)
    orb = ax.plot (orb_x, orb_y, orb_z, \
                   linestyle='-', linewidth=1.0, color='white')
    
    # title
    title = ax.text2D (0.20, 0.75, \
                       f'Orbital Motion of the Moon around the Earth', \
                       color='white', \
                       horizontalalignment='center', \
                       transform=ax.transAxes)

    # plotting the time
    time = ax.text2D (0.20, 0.23, f'Date/Time: {t} (UTC)', \
                      color='white', \
                      horizontalalignment='center', \
                      transform=ax.transAxes)

    # plotting the author name
    author = ax.text2D (0.85, 0.23, f'animation generated by Daisuke', \
                        color='white', \
                        horizontalalignment='center', \
                        transform=ax.transAxes)

    # viewing angles of camera
    ax.view_init (elev=el, azim=az)
    ax.dist = dist

    # image file
    file_image = f'{file_prefix}_{i:06d}.{file_ext}'
    fig.savefig (file_image, dpi=225)
