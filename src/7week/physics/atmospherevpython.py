from vpython import *
# Set up the scene and the objects in it

gc = graph(title='Atmosphere density', xtitle='height (m)', ytitle='density (kg/m^3)')

fig = gcurve(color=color.green)

# Define physical parameters and initial properties so they all have the same SI units 

g = 9.8     # gravity in m/s^2

 

p = 101000.0  # pressure at ground level 

h = 0.0     # initial height = ground level

dh = 100.0  # m 

# Set up a loop for the simulation

 

while h < 10000.0: 

    density = p/84000.0

    dp = -density*g*dh  # pressure change 

    fig.plot(h,density)

    p = p+dp

    h = h+dh
