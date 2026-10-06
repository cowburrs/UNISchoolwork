import warnings
from math import log, pi, sqrt

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


diffractoingrating = 600
uncertainty = 0.5 / 60
middle = umath.radians(  # pyright: ignore[reportAttributeAccessIssue]
    (ufloat(40 + 7 / 60, uncertainty) + ufloat(12 + 11 / 60, uncertainty)) / 2
)  
unknown1 = [41 + 49 / 60, 43 + 55 / 60, 47]
unknown2 = [48 + 55 / 60, 48, 47 + 15 / 60]
unknown3 = [47]

spectral_lines = [
    (706.5, "He"),
    (703.2, "Ne"),
    (670.8, "Li"),
    (667.8, "He"),
    (650.6, "Ne"),
    (643.8, "Cd"),
    (640.2, "Ne"),
    (636.2, "Zn"),
    (633.4, "Ne"),
    (610, "Eu"),
    (589.0, "Na"),
    (589.6, "Na"),
    (587.5, "He"),
    (579, "Hg"),
    (576.9, "Hg"),
    (546.1, "Hg"),
    (508.6, "Cd"),
    (501.5, "He"),
    (481, "Zn"),
    (480, "Cd"),
    (472, "Zn"),
    (467.8, "Cd"),
    (460.3, "Li"),
    (447.1, "He"),
    (435.8, "Hg"),
    (404.6, "Hg"),
    (388.8, "He"),
    (365.4, "Hg"),
    (360, "Cd"),
]


def calc_wavelength(x: UFloat):
    D = 1e-3 / 600
    return D * umath.sin(x)  # type: ignore


unknown1rad = [ufloat(np.deg2rad(x), np.deg2rad(uncertainty)) for x in unknown1]
unknown2rad = [ufloat(np.deg2rad(x), np.deg2rad(uncertainty)) for x in unknown2]
unknown3rad = [ufloat(np.deg2rad(x), np.deg2rad(uncertainty)) for x in unknown3]

unknown1waves = [calc_wavelength(x - middle) for x in unknown1rad]
unknown2waves = [calc_wavelength(x - middle) for x in unknown2rad]
unknown3waves = [calc_wavelength(x - middle) for x in unknown3rad]
print(unknown1waves)
print()
print(unknown2waves)
print()
print(unknown3waves)


# First is 53 degrees 37 mins
# faint purple 1  12 11
# faint purple 2 40 7
## UNKOWN 1
# first purple at 41 59
# some type of green 43 55
# SUPER STRONG ORANGE 47 0
## UNKNOWN 3
#  47 on the dot basically
# sodium easily cause its only one line
## UNKNOWN 2
# LOTS OF ORANGE AND RED ON A SPECTROM THINGY
# 48 55
# 48
# 47 15
# ERROR 5 minutes
