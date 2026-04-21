from vpython import *

x = 0.0
I = 1000.0
N = 2.0e6
sigma = 1.0e-8

# Pick the time step
dx = 0.1

# Set up a loop
fig = gcurve(color=color.green)
doprint = True
while x < 500.0:  # You should tinker with this condition
    I -= N * sigma * I * dx
    x += dx
    if I < 10 and doprint == True:
        doprint = False
        print(x)

    fig.plot(x, I)
