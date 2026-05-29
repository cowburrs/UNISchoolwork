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


# def plotgraph


def getmean(l: list):
    return statistics.mean(l)


def exp_func(x, a, b):
    return a * np.exp(b * x)


def plot_normal(numbers, y=None, xerr=None, yerr=None):
    if y is None:
        y = range(1, len(numbers) + 1)
    plt.figure()
    plt.errorbar(y, numbers, xerr=xerr, yerr=yerr, capsize=5, linestyle='none', marker='o')
    plt.title("Numbers with Standard Error")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.show()
    plt.clf()

def plot_poly_fit(numbers, y=None, xerr=None, yerr=None, degree=2):
    if y is None:
        y = range(1, len(numbers) + 1)
    plt.figure()
    plt.errorbar(y, numbers, xerr=xerr, yerr=yerr, capsize=5, linestyle='none', marker='o')

    coeffs = np.polyfit(list(y), numbers, degree)
    poly = np.poly1d(coeffs)
    x_smooth = np.linspace(min(y), max(y), 300)
    plt.plot(x_smooth, poly(x_smooth), color="purple", label=f"poly deg {degree}")

    plt.title(f"Polynomial Fit (degree {degree})")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.show()
    plt.clf()

def plot_exp_fit(numbers, y=None, xerr=None, yerr=None):
    if y is None:
        y = np.array(range(1, len(numbers) + 1), dtype=float)
    y = np.array(y, dtype=float)
    numbers = np.array(numbers, dtype=float)
    plt.figure()
    plt.errorbar(y, numbers, xerr=xerr, yerr=yerr, capsize=5, linestyle='none', marker='o')

    try:
        params, _ = curve_fit(exp_func, y, numbers, maxfev=5000)
        a, b = params
        x_smooth = np.linspace(min(y), max(y), 300)
        plt.plot(x_smooth, exp_func(x_smooth, a, b), color="green",
                 label=f"y = {a:.2f}·e^({b:.2f}x)")
    except RuntimeError:
        print("Exponential fit did not converge.")

    plt.title("Exponential Fit")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.show()
    plt.clf()



def compsigma(a, b):
    return abs((a.n - b.n) / ((((a.s**2) + (b.s**2)) ** (1 / 2))))


def getpopstd(numbers: list):
    return statistics.pstdev(numbers)


def getsamstd(numbers: list):
    return statistics.stdev(numbers)


def getrighttail(stds):
    return 1 - stats.norm.cdf(stds)


def getlefttail(stds):
    return stats.norm.cdf(stds)


def gettwotail(stds):
    return 1 - (2 * (1 - stats.norm.cdf(stds)))
