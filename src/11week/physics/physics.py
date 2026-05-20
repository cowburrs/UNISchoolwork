import matplotlib

matplotlib.use("TkAgg")
import math
import statistics

import matplotlib.pyplot as plt
import numpy as np  # imports not on the top nooo
import pandas as pd
import scipy as sp
import statsmodels.api as sm
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
tennisbounces1 = [ufloat(x[1], 5) / 1000 for x in bl]
tennisbounces2 = [ufloat(x[1], 5) / 1000 for x in b2l]
pingpongbounces1 = [ufloat(x[1], 5) / 1000 for x in blp]
pingpongbounces2 = [ufloat(x[1], 5) / 1000 for x in b2lp]


def dofunction(list, name, what):
    plt.errorbar(
        [x for x in range(len(list))],
        [math.log(x.n) for x in list],
        yerr=[x.s / x.n for x in list],
        capsize=5,
        color="black",
        ecolor="red",
    )
    plt.title("Bounce time vs #Bounce " + what)
    plt.xlabel("Bounce Number")
    plt.ylabel("ln(T) (ms)")
    plt.savefig(name, dpi=300)
    plt.clf()

    x = np.array([i + 1 for i in range(len(list))])
    y = np.array([math.log(b.n) for b in list])
    err_y = np.array([5 / x.n for x in list])
    print(y)

    x1 = sm.add_constant(x)
    w = 1.0 / (err_y**2)
    model = sm.WLS(y, x1, weights=w)
    result = model.fit()

    slope = result.params[1]
    slope_error = result.bse[1]
    slope_real = np.exp(slope)
    slope_error_real = np.exp(slope) * slope_error

    intercept = result.params[0]
    intercept_error = result.bse[0]
    intercept_real = np.exp(intercept)
    intercept_error_real = np.exp(intercept) * intercept_error

    print(f"intercept = {intercept_real:.4f} ± {intercept_error_real:.4f}")
    print(f"slope = {slope_real:.4f} ± {slope_error_real:.4f}")

    result.summary()
    return [
        ufloat(slope_real, slope_error_real),
        ufloat(intercept_real, intercept_error_real),
    ]


def compsigma(a, b):
    return abs((a.n - b.n) / ((((a.s**2) + (b.s**2)) ** (1 / 2))))

a = dofunction(tennisbounces1, "tenboun1", "on a tennis ball")
b = dofunction(tennisbounces2, "tenboun2", "on a tennis ball")
c = dofunction(pingpongbounces1, "pp1", "on a pingpong ball")
d = dofunction(pingpongbounces2, "pp2", "on a pingpong ball")

print(compsigma(a[0], b[0]))
print(compsigma(c[0], d[0]))





def getv0(x: ufloat):
    return 9.81 * (x) / 2

print(ufloat(math.sqrt(2 * 9.81 * 0.4), 0))
print(getv0(a[1]))
print(getv0(b[1]))
print(getv0(c[1]))
print(getv0(d[1]))
v0 = (ufloat(math.sqrt(2 * 9.81 * 0.4), 0))
print(compsigma((getv0(a[1])), v0))
print(compsigma((getv0(b[1])), v0))
print(compsigma((getv0(c[1])), v0))
print(compsigma((getv0(d[1])), v0))
