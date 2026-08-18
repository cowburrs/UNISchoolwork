import warnings
from math import pi, sqrt

import matplotlib.pyplot as plt
import numpy as np
from scipy import constants, odr
from uncertainties import UFloat, ufloat

warnings.filterwarnings("ignore", category=FutureWarning, module="uncertainties")
warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    message=r"AffineScalarFunc\.__abs__\(\) is deprecated",
)
warnings.filterwarnings(
    "ignore", category=UserWarning, message="Using UFloat objects with std_dev==0"
)


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


length_solanoid = ufloat(15, 0.25) / 100  # cm
loops = 700
radius_outer = ufloat(5.5, 0.25) / 2 / 100  # cm
radius_inner = ufloat(4, 0.05) / 2 / 100  # cm
radius = radius_outer
current = ufloat(2, 2 * 0.01)  # amps
total_length = ufloat(15.5, 0.25) / 100  # cm
voltage_0 = ufloat(2.53, 2.53 * (1.2 / 100) + 0.01)  # 1.2% plus last digit
# north is facing the positive, and south is facing the negative
current_to_length = [
    (0, 2.17),
    (1, 2.19),
    (2, 2.22),
    (3, 2.25),
    (4, 2.27),
    (5, 2.28),
    (6, 2.33),
    (7, 2.42),
    (8, 2.46),
    (9, 2.49),
    (10, 2.51),
]

def a(d):
    val = d + total_length / 2
    return (val) / ((val**2 + radius**2) ** 0.5)


def b(d):
    val = d - total_length / 2
    return (val) / ((val**2 + radius**2) ** 0.5)
lengths = [ufloat(x[0], 0.25) / 100 for x in current_to_length]
delta_voltages = [
    abs(ufloat(x[1], x[1] * (1.2 / 100) + 0.01) - voltage_0) for x in current_to_length
]
A = (constants.mu_0 * current * loops) / (2 * length_solanoid)
y = [delta_voltages[x] / A for x in range(len(lengths))]
x = [a(n) - b(n) for n in lengths]
S = fit_odr(x, y)[0] / 10
print(compsigma(ufloat(3.13, 0.09), S))
# uncertainty cm is 0.25
# uncertainty v is 1.2% plus last digit.
# roughly 19 centimeters away it still worked
slope, intercept, r_squared = fit_odr(x, y)

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

plt.title("Hall Probe Calibration: ΔV/A vs. Geometric Factor")
plt.xlabel("$a(d) - b(d)$ (dimensionless)")
plt.ylabel(r"$\Delta V / A$ (V/T)")
plt.legend()
plt.show()
