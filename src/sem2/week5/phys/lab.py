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


z_cm_small = [10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5, 3]
B_small_mT = [
    0.234,
    0.267,
    0.309,
    0.345,
    0.402,
    0.493,
    0.542,
    0.663,
    0.791,
    0.98,
    1.19,
    1.52,
    2.05,
    2.73,
    4.16,
]
mu_0 = constants.mu_0
zsmall = [mu_0 / ((ufloat(x / 100, 1e-100) ** 3) * 2 * pi) for x in z_cm_small]
bsmall = [ufloat(x, 1e-100) * 1e-3 for x in B_small_mT]
# m = fit_odr(zsmall, bsmall)[0].n
plot(zsmall, bsmall)
# plot_residuals(zsmall, bsmall)

# initdiameter = ufloat(2.5, 0.05)  # cm
# coils30delta = ufloat(1.5, 0)
heightvoltagetuples: list[tuple[int, int]] = [
    (5, 94),
    (10, 134),
    (15, 160),
    (20, 194),
    (25, 206),
    (30, 212),
]
radius_base = ufloat(2.525, 0.0125) / 100
n_base = 30
height_base = ufloat(20, 1.2) / 100
g = 9.79
heights = [
    25 * mu_0 * m * n_base * sqrt(2 * g) / ((5 ** (5 / 2)) * (radius_base**2)) * v
    for v in [ufloat(i[0], 1.5) / 100 for i in heightvoltagetuples]
]  # m
voltages = [ufloat(i[1], 2) * 1e3 for i in heightvoltagetuples]  # V
# plot(heights, voltages,xlab="")
# print(plot_residuals(heights, voltages))
del heightvoltagetuples, heights, voltages
ncoilvoltagetuples: list[tuple[int, int]] = [
    (5, 38),
    (10, 68),
    (15, 96),
    (20, 130),
    (25, 144),
    (30, 172),
]
ncoils = [
    24
    * mu_0
    * m
    * ((2 * g * height_base) ** (1 / 2))
    / (5 ** (5 / 2) * (radius_base**2))
    * n
    for n in [ufloat(x[0], 0.5) for x in ncoilvoltagetuples]
]
voltages = [ufloat(i[1], 2) * 1e3 for i in ncoilvoltagetuples]  # V
# plot(ncoils, voltages)
# print(plot_residuals(ncoils, voltages, show=False))
del ncoilvoltagetuples, ncoils, voltages
diametervoltagetuples: list[tuple[float, float]] = [
    (9.0, 27),
    (5.75, 47.2),
    (4.85, 57),
    (3.95, 121),  # pm 0.025
    (2.525, 220),
    (1.4, 268),
]
diameters = [
    # 1 / (((ufloat(i[0], 0.05) * 1e-2)) ** (1/2)) for i in diametervoltagetuples
    24
    * mu_0
    * m
    * n_base
    * ((2 * g * height_base) ** (1 / 2))
    / (5 ** (5 / 2) * (r**2))
    for r in [ufloat(i[0], 0.0125) for i in diametervoltagetuples]
]  # m
voltages = [(ufloat(i[1], 2) * 1e3) for i in diametervoltagetuples]  # V
plot(diameters, voltages)
print(
    plot_residuals(
        diameters,
        voltages,
        fitodr=fit_odr(diameters, voltages, zero_intercept=True),
        # show=False,
    )
)
