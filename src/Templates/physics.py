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


# def plotgraph


def getmean(l: list):
    return statistics.mean(l)


def exp_func(x, a, b):
    return a * np.exp(b * x)


def plot_normal(numbers, y=None, xerr=None, yerr=None):
    if y is None:
        y = range(1, len(numbers) + 1)
    plt.figure()
    plt.errorbar(
        y, numbers, xerr=xerr, yerr=yerr, capsize=5, linestyle="none", marker="o"
    )
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
    plt.errorbar(
        y, numbers, xerr=xerr, yerr=yerr, capsize=5, linestyle="none", marker="o"
    )

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
    plt.errorbar(
        y, numbers, xerr=xerr, yerr=yerr, capsize=5, linestyle="none", marker="o"
    )

    try:
        params, _ = curve_fit(exp_func, y, numbers, maxfev=5000)
        a, b = params
        x_smooth = np.linspace(min(y), max(y), 300)
        plt.plot(
            x_smooth,
            exp_func(x_smooth, a, b),
            color="green",
            label=f"y = {a:.2f}·e^({b:.2f}x)",
        )
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

def fit_linear(x, y):
    """y = a + bx"""
    X = sm.add_constant(x)
    return sm.WLS(y, X).fit()


def fit_polynomial(x, y, degree=2):
    """y = a + bx + cx^2 + ..."""
    X = np.vander(x, N=degree + 1, increasing=True)
    return sm.WLS(y, X).fit()


def fit_exponential(x, y):
    """y = a * e^(bx)"""
    log_y = np.log(y)
    X = sm.add_constant(x)
    return sm.WLS(log_y, X).fit()


def fit_log(x, y):
    """y = a + b*ln(x)"""
    log_x = np.log(x)
    X = sm.add_constant(log_x)
    return sm.WLS(y, X).fit()


def fit_power(x, y):
    """y = a * x^b"""
    log_y = np.log(y)
    log_x = np.log(x)
    X = sm.add_constant(log_x)
    return sm.WLS(log_y, X).fit()

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
y = np.array([2.3, 3.1, 4.8, 6.2, 8.5, 9.1, 11.3, 13.0])

fits = {
    "Linear      (y = a + bx)":         fit_linear(x, y),
    "Polynomial  (y = a + bx + cx²)":   fit_polynomial(x, y, degree=2),
    "Exponential (y = a * e^bx)":       fit_exponential(x, y),
    "Log         (y = a + b*ln(x))":    fit_log(x, y),
    "Power       (y = a * x^b)":        fit_power(x, y),
}

for name, result in fits.items():
    print(f"\n{'='*55}")
    print(f"  {name}")
    print(f"{'='*55}")
    for i, (coef, err) in enumerate(zip(result.params, result.bse)):
        print(f"  c{i} = {coef:.4f} ± {err:.4f}")
    print(f"  R² = {result.rsquared:.4f}")
