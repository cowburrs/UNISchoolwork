import warnings
from math import pi

import matplotlib.pyplot as plt
import numpy as np
from scipy import odr
from uncertainties import UFloat, ufloat

warnings.filterwarnings("ignore", category=FutureWarning, module="uncertainties")
warnings.filterwarnings(
    "ignore", category=UserWarning, message="Using UFloat objects with std_dev==0"
)

print("bryce tabangcura")
print("haven bunter-gooley")


def fit_odr(x: list[UFloat], y: list[UFloat], zero_intercept: bool = False):
    x_nom, x_err = [v.n for v in x], [v.s for v in x]
    y_nom, y_err = [v.n for v in y], [v.s for v in y]
    data = odr.RealData(x_nom, y_nom, sx=x_err, sy=y_err)
    if zero_intercept:
        model, beta0 = odr.Model(lambda p, x: p[0] * x), [1]
    else:
        model, beta0 = odr.Model(lambda p, x: p[0] * x + p[1]), [1, 0]
    out = odr.ODR(data, model, beta0=beta0).run()
    slope = ufloat(out.beta[0], out.sd_beta[0])
    intercept = (
        ufloat(out.beta[1], out.sd_beta[1]) if not zero_intercept else ufloat(0, 0)
    )
    y_pred = model.fcn(out.beta, np.array(x_nom))
    ss_res = np.sum((np.array(y_nom) - y_pred) ** 2)
    ss_tot = np.sum(
        np.array(y_nom) ** 2
        if zero_intercept
        else (np.array(y_nom) - np.mean(y_nom)) ** 2
    )
    r_squared = 1 - ss_res / ss_tot
    return slope, intercept, r_squared


def compsigma(a, b):
    return abs((a.n - b.n) / ((((a.s**2) + (b.s**2)) ** (1 / 2))))


length = ufloat(60.5, 1) / 100  # m
total_time_swings_theta: list[tuple[float, float]] = [
    (23.56, 10),
    (23.44, 10),
    (23.9, 25),
    (23.78, 25),
    (24.1, 40),
    (24.29, 40),
]
total_period = [ufloat(x[0], 0.25) for x in total_time_swings_theta]
# time uncertainty of 0.25 methinks
periods = [x / 15 for x in total_period]
# A whole degree uncertainty measurement
thetas = [ufloat(np.deg2rad(x[1]), np.deg2rad(1)) for x in total_time_swings_theta]
fi = [1 + (1 / 16) * (x**2) for x in thetas]
print(periods[0])
print(fi[0])
print(length * 4 * (pi**2) * (fi[0] ** 2) / (periods[0] ** 2))

x = [T**2 for T in periods]
y = [length * 4 * (pi**2) * fi[n] for n in range(len(periods))]
a, b, c = fit_odr(x, y, zero_intercept=True)
print(a, b, c)

total_time_swings_length: list[tuple[float, float]] = [
    (23.47, 60.5),
    (20.38, 44.5),
    (16.39, 30.5),
    (10.97, 15),
]
periods = [ufloat(x[0], 0.25) / 15 for x in total_time_swings_length]
lengths = [ufloat(x[1], 0.25) / 100 for x in total_time_swings_length]
x = [x**2 for x in periods]
y = [4 * (pi**2) * x for x in lengths]
e, f, g = fit_odr(x, y, zero_intercept=True)
print(compsigma(a, e))
# Doing 5 degrees

print("EOL")
