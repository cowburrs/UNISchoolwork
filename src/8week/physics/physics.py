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
    print(f"{(x ** 0.5).n:.5f}")  # print number
    print(f"{(x ** 0.5).s:.5f}")  # print uncertainty


numbers = list(range(1, 17))
mean = statistics.mean(numbers)
std = statistics.pstdev(numbers)
n = len(numbers)
se = std / (n**0.5)

pop_std = statistics.pstdev(numbers)
sam_std = statistics.stdev(numbers)
mean = statistics.mean(numbers)
right_tail = 1 - stats.norm.cdf(1)
left_tail = stats.norm.cdf(1)
two_tail = 1 - (2 * (1 - stats.norm.cdf(1)))

x = ufloat(10, 3)
uprint(x)
