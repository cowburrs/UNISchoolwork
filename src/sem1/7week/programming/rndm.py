from vpython import *
import random

gc = graph(title="Atmosphere density", xtitle="height (m)", ytitle="density (kg/m^3)")

fig = gcurve(color=color.green)

# Define physical parameters and initial properties so they all have the same SI units

x = 0
dx = 1
# Set up a loop for the simulation

dices = list()
while x < 10000.0:
    dices.append(random.randint(0, 6))
    fig.plot(x, sum(dices) / len(dices))
    x += dx
