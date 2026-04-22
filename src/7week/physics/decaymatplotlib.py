import matplotlib
import numpy as np

matplotlib.use("TkAgg")
import random

import matplotlib.pyplot as plt


def linefit(xdata, ydata):
    xdata = np.array(xdata, dtype=float)
    ydata = np.array(ydata, dtype=float)
    m, b = np.polyfit(xdata, ydata, 1)
    x_fit = np.linspace(min(xdata), max(xdata), 200)
    plt.plot(x_fit, m * x_fit + b, "-b", label=f"Linear: {m:.2f}x + {b:.2f}")
    return m, b


def expfit(xdata, ydata):
    xdata = np.array(xdata, dtype=float)
    ydata = np.array(ydata, dtype=float)
    k, logA = np.polyfit(xdata, np.log(ydata), 1)
    A = np.exp(logA)
    x_fit = np.linspace(min(xdata), max(xdata), 200)
    plt.plot(x_fit, A * np.exp(k * x_fit), "-g", label=f"Exp: {A:.2f}e^({k:.2f}x)")
    return A, k


def powfit(xdata, ydata):
    xdata = np.array(xdata, dtype=float)
    ydata = np.array(ydata, dtype=float)
    n, logA = np.polyfit(np.log(xdata), np.log(ydata), 1)
    A = np.exp(logA)
    x_fit = np.linspace(min(xdata), max(xdata), 200)
    plt.plot(x_fit, A * x_fit**n, "-m", label=f"Power: {A:.2f}x^({n:.2f})")
    return A, n


p = 0.01
dt = 1

# Set up loop

n = 100000
t = 0.0
tlist = []
nlist = []


while t < 500:

    # print(t,n)
    n += -n * p * dt
    t += dt
    nlist.append(n + random.randint(-10000, 10000))
    tlist.append(t)

# plot our graph
m, b = linefit(tlist, nlist)
A, k = expfit(tlist, nlist)
A, n = powfit(tlist, nlist)

plt.plot(tlist, nlist, ".r")
plt.xlabel("Time (s)")
plt.ylabel("Number")
# plt.savefig("decay.png", dpi=300)
plt.show()
