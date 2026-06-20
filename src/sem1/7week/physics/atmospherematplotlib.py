import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import math

# Pick the starting conditions
p = 101000
h = 0.0
g = 9.8

# Pick the length step
dh = 100.0

# Set up a couple of lists which will store the values to plot
xlist = []
ylist = []

# Set up a loop
while h < 10000.0:
    density = p / 84000.0

    dp = -density * g * dh  # Calculate the pressure change

    # Store whatever you want to plot in the lists.
    xlist.append(h)
    ylist.append(density)

    print(h, density, p)

    # Updates
    h += dh
    p += dp

# Plot the two lists as a red line.
plt.plot(xlist, ylist, '-b')
plt.xlabel("Height (m)")
plt.ylabel(r"Density ($kg\, m^{-3}$)")
plt.show()
