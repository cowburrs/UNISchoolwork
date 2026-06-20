import matplotlib

matplotlib.use("TkAgg")
import math
import random

import matplotlib.pyplot as plt


# Set up a couple of lists which will store the values to plot
x = 1
xlist = []
ylist = []
dices = list()
size = 20000
dicesize = 6
# Set up a loop
while x < size:
    dices.append(random.randint(1, dicesize))
    xlist.append(x ** .5)
    # xlist.append(x)
    ylist.append((sum(dices) / len(dices)) - (0.5 + dicesize / 2))
    x += 1
# import numpy as np
# plt.xticks(xlist[::10])
plt.xticks([x**0.5 for x in range(0, size, size//10)])
# Plot the two lists as a red line.
plt.plot(xlist, ylist, "-b")
plt.xlabel("#rolls")
plt.ylabel("Mean(Rolls)")

plt.plot(
    [0, size ** .5], [0, 0], color="red", linestyle="-"
)
# plt.plot(
#     [0, size], [0, 0], color="red", linestyle="-"
# )
plt.show()
