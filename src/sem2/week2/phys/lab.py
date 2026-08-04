import warnings

import matplotlib.pyplot as plt
from uncertainties import ufloat
import numpy as np
from scipy import odr

warnings.filterwarnings("ignore", category=FutureWarning, module="uncertainties")

print("bryce tabangcura")
print("haven bunter-gooley")

g = 9.796

def fit_odr(x, y):
    x_nom = [v.nominal_value for v in x]
    x_err = [v.std_dev for v in x]
    y_nom = [v.nominal_value for v in y]
    y_err = [v.std_dev for v in y]
    model = odr.Model(lambda p, x: p[0] * x + p[1])
    data = odr.RealData(x_nom, y_nom, sx=x_err, sy=y_err)
    out = odr.ODR(data, model, beta0=[1, 0]).run()
    slope = ufloat(out.beta[0], out.sd_beta[0])
    intercept = ufloat(out.beta[1], out.sd_beta[1])

    y_pred = out.beta[0] * np.array(x_nom) + out.beta[1]
    ss_res = np.sum((np.array(y_nom) - y_pred) ** 2)
    ss_tot = np.sum((np.array(y_nom) - np.mean(y_nom)) ** 2)
    r_squared = 1 - ss_res / ss_tot

    return slope, intercept, r_squared

# print(spring_weight)
spring_length_uncompressed = ufloat(30, 0.25)
milligrams_over_weight = (232 + 140 + 173 + 154) / 8
weight_to_total_spring_length = [
    (1, 33.5),
    (2, 35.5),
    (3, 38),
    (4, 40.5),
    (5, 43),
    (6, 45.5),
    (7, 48),
    (8, 50.5),
]
# uncertainty in mass will be 0.1g, and uncertainty in length is 0.25cm
mass_then_displacement = [
    (
        x[0] * ufloat(50, 0.1) / 1000,
        (ufloat(x[1], 0.25)) / 100,
    )
    for x in weight_to_total_spring_length
]
mg = [g * x[0] for x in mass_then_displacement]
delta_displacement = [
    x[1] - spring_length_uncompressed / 100 for x in mass_then_displacement
]





slope, intercept, r_squared = fit_odr(delta_displacement, mg)
intercept_static = intercept

x = delta_displacement
y = mg

plt.figure()
first = x[0].n
last = x[-1].n

plt.plot(
    [first, last],
    [first * slope.n + intercept.n, last * slope.n + intercept.n],
    "r-",
    label=f"Fit: $y = ({slope.n:.4g})x + ({intercept.n:.4g}),R^2 = {r_squared:.4f}$",
)

plt.errorbar(
    [v.nominal_value for v in x],
    [v.nominal_value for v in y],
    xerr=[v.std_dev for v in x],
    yerr=[v.std_dev for v in y],
    capsize=5,
    linestyle="none",
    marker="o",
    markersize=3,
    label="Data",
)

plt.title("Static Method: mg vs. displacement")
plt.xlabel("$x_0-x (m)$")
plt.ylabel("$mg (kgm/s^2)$")
plt.legend()
plt.savefig("StaticGraph")
plt.clf()

spring_weight = ufloat(43.627, 0.001) / 1000
period_to_weight = [
    (1, 7.17),
    (2, 9.61),
    (3, 11.57),
    (4, 13.14),
    (5, 14.78),
    (6, 15.89),
    (7, 17.16),
    (8, 18.29),
]
period = [ufloat(x[1], 0.1) / 20 for x in period_to_weight]
from numpy import pi
x = [((x / (2 * pi)) ** 2) for x in period]
mass_for_period = [x[0] for x in mass_then_displacement]
y = [m + (spring_weight / 3) for m in mass_for_period]
slope, intercept, r_squared = fit_odr(x, y)
print(f"y = {slope}x + {intercept}")



plt.figure()
first = x[0].n
last = x[-1].n

plt.plot(
    [first, last],
    [first * slope.n + intercept.n, last * slope.n + intercept.n],
    "r-",
    label=f"Fit: $y = ({slope.n:.4g})x + ({intercept.n:.4g}),R^2 = {r_squared:.4f}$",
)

plt.errorbar(
    [v.nominal_value for v in x],
    [v.nominal_value for v in y],
    xerr=[v.std_dev for v in x],
    yerr=[v.std_dev for v in y],
    capsize=5,
    linestyle="none",
    marker="o",
    markersize=3,
    label="Data",
)

plt.title("Period Method: f(t) vs. displacement")
plt.xlabel(r"$\frac{T}{2\pi}^2(t)$")
plt.ylabel(r"$m + \frac{m_3}{3}(m)$")
plt.legend()
plt.savefig("PeriodGraph")
plt.clf()


def compsigma(a, b):
    return abs((a.n - b.n) / ((((a.s**2) + (b.s**2)) ** (1 / 2))))
print(compsigma(intercept, intercept_static))
print("EOL")
