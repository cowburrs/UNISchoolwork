from vpython import *

# Set up a plot

gc = graph(title="Number of atoms vs time", xtitle="Time (s)", ytitle="Number")

fig = gcurve(color=color.red)


# Define physical parameters and initial values so they all have the same SI units

n = 1e5  # initial number of atoms

t = 0.0  # start time

dt = 1.0  # time step

p = 0.01  # decay probability within 1 sec.

# Set up a loop for the simulation


while t < 500:

    fig.plot(t, n)

    n = n - n * p * dt

    t = t + dt
