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


# mean std
# NOTE: BASE
# 120 counts and per second
# 0.574 0.3
# 0.549 0.274
# 0.607 0.376

# NOTE:
# Brown white black grey
# Copper lead acrylic pvc
# Base only
# 1.300 1.213
# PVC depth 9.36 or 9.36 Since we both had the same caliper measurement
# Instead of choosing standard error as half of our difference, we choose
# Half the calipers increent as our sstandard deviation. which is 0.01 mm

# NOTE: PVC
# PVC 1 layer
# 0.892 0.968
# 0.800 0.885
# PVC 2 layer
# 0.875 0.975
# 0.883 0.852
# PVC 3 layer
# 0.725 0.860
# 0.717 0.842

# NOTE: Second experiment with closer.
# nothing
# 0.325 0.663
# 0.408 0.628
# Base
# 2.225 1.399
# 2.425 1.459
# PVC 1 layer
# 1.433 1.207
# 1.467 1.223
# PVC 2 layer
# 1.242 1.045
# 1.5 1.23
# PVC 3 layer
# 1.317 1.123
# 1.150 1.001
exp2data: list[tuple[int, float, float]] = [
    (-1, 0.325, 0.663),
    (-1, 0.408, 0.628),
    (0, 2.225, 1.399),
    (0, 2.425, 1.459),
    (1, 1.433, 1.207),
    (1, 1.467, 1.223),
    (2, 1.242, 1.045),
    (2, 1.5, 1.23),
    (3, 1.317, 1.123),
    (3, 1.150, 1.001),
]
exp1data: list[tuple[int, float, float]] = [
    (-1, 0.574, 0.3),
    (-1, 0.549, 0.274),
    (-1, 0.607, 0.376),
    (0, 1.300, 1.213),
    (1, 0.892, 0.968),
    (1, 0.800, 0.885),
    (2, 0.875, 0.975),
    (2, 0.883, 0.852),
    (1, 0.725, 0.860),
    (1, 0.717, 0.842),
]
# 1.300 1.213
# PVC depth 9.36 or 9.36 Since we both had the same caliper measurement
# Instead of choosing standard error as half of our difference, we choose
# Half the calipers increent as our sstandard deviation. which is 0.01 mm
lengthpvc = ufloat(9.36, 0.01) / 1000


def databetter(data: list[tuple[int, float, float]]):
    ufloats = [(x[0], ufloat(x[1], x[2] / sqrt(120))) for x in data]
    numbers = set([x[0] for x in ufloats])
    combinedufloats = [list(filter(lambda y: y[0] == x, ufloats)) for x in numbers]
    values = [(x[0][0], sum([y[1] for y in x]) / len(x)) for x in combinedufloats]
    sortedvalues = sorted(values, key=lambda x: x[0])
    out = [(x[0], x[1] - sortedvalues[0][1]) for x in sortedvalues[1:]]
    return out


def datainterpolate(data: list[tuple]):
    xdata = [-x[0] * lengthpvc for x in data[1:]]
    ydata = [umath.log(x[1] / data[0][1]) for x in data[1:]]
    out = fit_odr(xdata, ydata)
    return out


mu2 = datainterpolate(databetter(exp2data))[0]
print(compsigma(mu2, ufloat(14, 0.5)))

mu1 = datainterpolate(databetter(exp1data))[0]
print(compsigma(mu1, ufloat(1.4, 0.05)*10))
