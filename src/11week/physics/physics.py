import matplotlib

matplotlib.use("TkAgg")
import math
import statistics

import matplotlib.pyplot as plt
import numpy as np  # imports not on the top nooo
import pandas as pd
import scipy as sp
from scipy import stats
from scipy.optimize import curve_fit
from uncertainties import ufloat


def uprint(x):
    print(f"{(x).n:.5f}")  # print number
    print(f"{(x).s:.5f}")  # print uncertainty


numbers = list(range(1, 17))
mean = statistics.mean(numbers)
std = statistics.pstdev(numbers)
n = len(numbers)
se = std / (n**0.5)


def exp_func(x, a, b):
    return a * np.exp(b * x)


bl = [  # nth bounce, milliseconds ERROR += 5 ms due to thats the yeah whatever
    (1, 440),
    (2, 310),
    (3, 260),
    (4, 190),
    (5, 150),
    (6, 120),
]

b2l = [  # nth bounce, milliseconds
    (1, 420),
    (2, 320),
    (3, 240),
    (4, 190),
    (5, 140),
    (6, 120),
]

blp = [  # nth bounce, milliseconds
    (1, 500),
    (2, 460),
    (3, 440),
    (4, 420),
    (5, 370),
    (6, 350),
    (7, 340),
    (8, 300),
    (9, 280),
    (10, 280),
    (11, 260),
    (12, 230),
]

b2lp = [  # nth bounce, milliseconds
    (1, 500),
    (2, 480),
    (3, 460),
    (4, 410),
    (5, 380),
    (6, 350),
    (7, 330),
    (8, 320),
    (9, 280),
    (10, 260),
    (11, 240),
    (12, 230),
]
tennisbounces = [
    (ufloat(bl[x][1], 5) + ufloat(b2l[x][1], 5)) / 2 for x in range(len(bl))
]
pingpongbounces = [
    (ufloat(blp[x][1], 5) + ufloat(b2lp[x][1], 5)) / 2 for x in range(len(blp))
]
plt.errorbar(
    [x for x in range(len(tennisbounces))],
    [x.n for x in tennisbounces],
    yerr=[x.s for x in tennisbounces],
    capsize=5,
    color="black",
    ecolor="red",
)
plt.title("Bounce time vs #Bounce on a tennis ball")
plt.xlabel("Bounce Number")
plt.ylabel("T (ms)")
# plt.semilogx()
plt.semilogy()
plt.savefig("tennball", dpi=300)
plt.clf()

plt.errorbar(
    [x for x in range(len(pingpongbounces))],
    [x.n for x in pingpongbounces],
    yerr=[x.s for x in pingpongbounces],
    capsize=5,
    color="black",
    ecolor="red",
)
plt.title("Bounce time vs #Bounce on a pongping ball")
plt.xlabel("Bounce Number")
plt.ylabel("T (ms)")
# plt.semilogx()
plt.semilogy()
plt.savefig("PinPon", dpi=300)
plt.show()
plt.clf()
