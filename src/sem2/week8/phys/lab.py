import warnings
from math import log, pi, sqrt

import matplotlib.pyplot as plt
import numpy as np
from scipy import constants, odr
from uncertainties import UFloat, ufloat, umath

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


def plot(
    x,
    y,
    fitodr=None,
    title="default title",
    xlabel="default xlabel",
    ylabel="default ylabel",
    show=True,
):
    if fitodr is None:
        fitodr = fit_odr(x, y)
    slope, intercept, r_squared = fitodr
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

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    if show:
        plt.show()


def plot_residuals(
    x,
    y,
    fitodr=None,
    title="Residuals",
    xlabel="default xlabel",
    ylabel="Residual (y - fit)",
    show=True,
):
    if fitodr is None:
        fitodr = fit_odr(x, y)
    slope, intercept, r_squared = fitodr
    residuals = [yi - (slope * xi + intercept) for xi, yi in zip(x, y)]
    sigma_eff = [
        sqrt(yi.std_dev**2 + (slope.n * xi.std_dev) ** 2) for xi, yi in zip(x, y)
    ]
    chi2 = sum((r.nominal_value**2) / (s**2) for r, s in zip(residuals, sigma_eff))
    dof = len(y) - 1
    chi2_reduced = chi2 / dof
    zero_fit = (
        ufloat(0, 0),
        ufloat(0, 0),
        0.0,
    )  # was None — plot()'s label needs a float

    plot(
        x,
        residuals,
        fitodr=zero_fit,
        title=f"{title} ($\\chi^2_\\nu = {chi2_reduced:.3f}$)",
        xlabel=xlabel,
        ylabel=ylabel,
        show=show,
    )

    return chi2_reduced


# time difference is
L = ufloat(0.995, 0.0025)
a = ufloat(9, 0.5) / 100 / 2  # cm
openend = [161, 322, 480, 634, 805, 986, 1149, 1319]
openend2 = [157, 324, 487, 647, 815, 949, 1146, 1314]
closedend = [89, 262, 423, 602, 765, 927, 1101, 1282]
closedend2 = [104, 269, 426, 591, 759, 938, 1099, 1271]

openendavg = [
    (ufloat(openend[x], 10) + ufloat(openend2[x], 10)) / 2 for x in range(len(openend))
]
closedend2 = [
    (ufloat(closedend[x], 10) + ufloat(closedend2[x], 10)) / 2
    for x in range(len(openend))
]
openendx = [(n + 1) / (2 * (L + 1.2 * a)) for n in range(len(openendavg))]
closedendx = [(2 * (n + 1) - 1) / (4 * (L + 0.6 * a)) for n in range(len(openendavg))]
# plot(openendx, openendavg)
# plot_residuals(openendx, openendavg)

resonentfreqs = (85, 232, 422)  # hz
threepeaks = [
    (0, -12.9, -2.8),
    (-0.6, -12.3, -3.7),
    (-5.1, -17, -7),
    (-9, -24, -12.9),
    (-17, -30.8, -20.3),
]
resonance = [x for x in resonentfreqs]
t = [ufloat(x * 0.015, 0.001) for x in range(len(threepeaks))]
resy = [ufloat(x[0], 1) for x in threepeaks]
resy2 = [ufloat(x[1], 1) for x in threepeaks]
resy3 = [ufloat(x[2], 1) for x in threepeaks]
print(fit_odr(t, resy)[0])
print(fit_odr(t, resy2)[0])
print(fit_odr(t, resy3)[0])


def calcq(fr, slope):
    T12 = 3 / (-slope)
    return pi * fr * T12 / log(2)


print(calcq(resonentfreqs[0], fit_odr(t, resy)[0]))
print(calcq(resonentfreqs[1], fit_odr(t, resy2)[0]))
print(calcq(resonentfreqs[2], fit_odr(t, resy3)[0]))


plt.close()
