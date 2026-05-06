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


# NOTE: percentage uncertainty is 1.2%
v1v2list = [
    (0, 0),
    (3.02, 0.71),
    (6.03, 0.73),
    (9.06, 0.74),
    (12.00, 0.75),
    (15.05, 0.76),
    (18.03, 0.76),
    (20.9, 0.77),
    (24.0, 0.77),
    (26.9, 0.77),
    (29.9, 0.78),
    (-3.0, -2.99),
    (-6.0, -4.23),
    (-9.0, -4.54),
    (-12.0, -4.68),
    (-15.0, -4.77),
    (-18.0, -4.83),
    (-21.0, -4.87),
    (-24.0, -4.90),
    (-27.0, -4.93),
    (-30.0, -4.95),
    (1.5, 0.68),
    (1.0, 0.66),
]
v1v2list.sort(key=lambda x: x[0])
v1list = [x[0] for x in v1v2list]
v2list = [x[1] for x in v1v2list]
currentlist = [(x[0] - x[1]) / 3900 for x in v1v2list]
# print(currentlist)
# print(v1list)
# print(v2list)
# [print(x) for x in zip(currentlist, v1list, v2list)]

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.plot(v2list, currentlist)
# plt.axvline(0.67, color="black", linewidth=0.8)
plt.title("Voltage(Zener) over Voltage(Total)")
plt.xlabel("Voltage Through Diode")
plt.ylabel("Current Through Diode")
plt.savefig("currentvoltage", dpi=300)
plt.clf()

plt.plot(v1list, v2list)
plt.title("Voltage vs Current over Zener diode")
plt.xlabel("V1 (Volts)")
plt.ylabel("V2 (Volts)")
plt.savefig("volts vs volts", dpi=300)
plt.clf()

part2vlist = [
    (0, 0),
    (1.5, 0.67),
    (3, 0.73),
    (4.4, 0.75),
    (6, 0.76),
    (7.4, 0.77),
    (9, 0.78),
    (10.5, 0.78),
    (12.0, 0.79),
    (13.4, 0.79),
    (15, 0.79),
    (-1.52, -0.76),
    (-3.02, -1.51),
    (-4.50, -2.25),
    (-6.03, -3.01),
    (-7.46, -3.70),
    (-9.07, -4.25),
    (-10.56, -4.49),
    (-12.02, -4.75),
    (-13.54, -4.85),
    (-15, -4.91),
    (-16.54, -4.96),
    (-18.04, -4.99),
    (-18.04, -4.99),
    (-18.46, -5.02),
    (-21.0, -5.04),
    (-22.5, -5.05),
]

part2vlist.sort(key=lambda x: x[0])

v1list = [x[0] for x in part2vlist]
v2list = [x[1] for x in part2vlist]

plt.plot(v1list, v2list)
plt.savefig("part2", dpi=300)
plt.title("part2")
# plt.xlabel("Voltage Through Diode")
# plt.ylabel("Current Through Diode")


def exp_func(x, a, b):
    return a * np.exp(b * x)


# params, _ = curve_fit(exp_func, v1list, v2list)
# a, b = params
# exp_line = [exp_func(i, a, b) for i in v1list]
# plt.plot(v1list, exp_line, color="green", label=f"y = {a:.2f}e^({b:.2f}x)")

# numbers = list(range(1, 17))
# mean = statistics.mean(numbers)
# std = statistics.pstdev(numbers)
# n = len(numbers)
# se = std / (n**0.5)
#
#
#
# degree = 2
# coeffs = np.polyfit(numbers, numbers, degree) # change 1 to change degree polynomial
# poly = np.poly1d(coeffs)
# line = [poly(i) for i in numbers]
# NOTE: Oscilloscope uncertainty is +- 1 of the last digit

# plt.plot(numbers, line, color='purple', label=f'poly deg {degree}')
#

# pop_std = statistics.pstdev(numbers)
# sam_std = statistics.stdev(numbers)
# mean = statistics.mean(numbers)
# right_tail = 1 - stats.norm.cdf(1)
# left_tail = stats.norm.cdf(1)
# two_tail = 1 - (2 * (1 - stats.norm.cdf(1)))
#
# x = ufloat(10, 3)
# uprint(x)
