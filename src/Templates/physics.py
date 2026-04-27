import matplotlib

matplotlib.use("TkAgg")
import math
import statistics

import matplotlib.pyplot as plt
import numpy as np  # imports not on the top nooo
import pandas as pd
import scipy as sp
from scipy.optimize import curve_fit
from uncertainties import ufloat


def uprint(x):
    print(f"{(x ** 0.5).n:.5f}")  # print number
    print(f"{(x ** 0.5).s:.5f}")  # print uncertainty


numbers = list(range(1, 17))
mean = statistics.mean(numbers)
std = statistics.pstdev(numbers)
n = len(numbers)
se = std / (n**0.5)


def exp_func(x, a, b):
    return a * np.exp(b * x)


params, _ = curve_fit(exp_func, numbers, numbers)
a, b = params
exp_line = [exp_func(i, a, b) for i in numbers]
plt.plot(numbers, exp_line, color="green", label=f"y = {a:.2f}e^({b:.2f}x)")

degree = 2
coeffs = np.polyfit(numbers, numbers, degree) # change 1 to change degree polynomial
poly = np.poly1d(coeffs)
line = [poly(i) for i in numbers]
plt.plot(numbers, line, color='purple', label=f'poly deg {degree}')

plt.bar(range(1, 17), numbers, yerr=se, capsize=5)
plt.title("Numbers with Standard Error")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

# pop_std = statistics.pstdev(numbers)
# sam_std = statistics.stdev(numbers)
# mean = statistics.mean(numbers)
# right_tail = 1 - stats.norm.cdf(1)
# left_tail = stats.norm.cdf(1)
# two_tail = 1 - (2 * (1 - stats.norm.cdf(1)))
#
# x = ufloat(10, 3)
# uprint(x)
#
