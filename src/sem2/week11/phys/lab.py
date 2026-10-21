import warnings
from math import e, log, pi, sqrt

import matplotlib.pyplot as plt
import numpy as np
from scipy import constants, odr
from scipy.stats import norm
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


def two_tailed_p(diff: float):
    z = abs(diff)
    return 2 * norm.sf(z)


# Width tape = 1.79
# Width tape = 420 +/- 10
# single slit
# 120 697 pm 10 This was distance between two peaks, not including middle peak
# Length to slit is 76.5 pm 0.25
# second twoslit size between in 585
# 304 298. Considering our uncertainty is 10,. they are within 3 sigma
# hair is 273

width_tape = ufloat(1.79, 0.02) / 100
tape_pixels = ufloat(420, 10)
distance_slit_screen = ufloat(76.5, 0.25) / 100

single_slit = ufloat(697, 10) - ufloat(120, 10)

light_frequency = (0.04e-3 * width_tape * (single_slit / tape_pixels)) / (
    2 * distance_slit_screen
)
print(light_frequency)
print(compsigma(light_frequency, ufloat(642e-9, 2e-9)))

double_slit = ufloat(585, 10)

# I'm remarkably confident we chose a double slit spacing of somewhere in the range of 0.04, and we did the experiment wrong
print(2 * distance_slit_screen * light_frequency / (0.25e-3))
print(double_slit * width_tape / tape_pixels)
print(
    compsigma(
        double_slit * width_tape / tape_pixels,
        2 * distance_slit_screen * light_frequency / (0.25e-3),
    )
)

# Compsigma
print(compsigma(ufloat(304, 10), ufloat(298, 10)))

hair_px = ufloat(273, 10)

hair_width = (
    light_frequency * distance_slit_screen * 2 / (hair_px / tape_pixels * width_tape)
)

print(compsigma(ufloat(80e-6, 5e-6), hair_width))
