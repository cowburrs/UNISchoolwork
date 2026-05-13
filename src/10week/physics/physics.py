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


R = ufloat(4600, 4600 * 0.012)
C = ufloat(0.1e-6, 0.1e-6 * 0.01)
TCalculated = R * C
print(TCalculated)
TMeasured = ufloat(440e-6, 20e-6)
Sigma = (TCalculated.n - TMeasured.n) / (TCalculated + TMeasured).s
print(Sigma)
print(1/(2 * math.pi * R * C))
FCalculated = 1/(2 * math.pi * R * C)
FMeasured = ufloat(1e2, (10 ** 0.5) * 1e2)
print(FMeasured)
Sigma = (FCalculated.n - FMeasured.n) / (FCalculated + FMeasured).s
print(Sigma)
Vclist = [
    (1, 3920),
    (5, 3920),
    (10, 3920),
    (50, 3920),
    (100, 3760),
    (200, 3400),
    (500, 2200),
    (1000, 1240),
    (2000, 648),
    (5000, 276),
    (10000, 148),
]
Flist = [x[0] for x in Vclist]
Vlist = [x[1] for x in Vclist]
Errorx = [x * 0.01 for x in Flist]
Errory = [2 * 10 ** (math.floor(math.log(x, 10)) - 2) for x in Vlist]
# [print(f"{Errory[x]} {Vlist[x]}") for x in range(len(Flist))]

# plt.plot(Flist, Vlist)
plt.errorbar(
    Flist,
    Vlist,
    xerr=Errorx,
    yerr=Errory,
    capsize=5,
    color="black",
    ecolor="red",
)
plt.title("Frequency vs Amplitude over Capacitor")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Voltage Amplitude (mV)")
plt.semilogx()
plt.semilogy()
plt.savefig("FreqAmpCap", dpi=300)
plt.clf()

Vclist = [
    (1, 15),
    (5, 60),
    (10, 120),
    (50, 576),
    (100, 1140),
    (200, 1960),
    (500, 3240),
    (1000, 3680),
    (2000, 3920),
    (5000, 4000),
    (10000, 4000),
]

Flist = [x[0] for x in Vclist]
Vlist = [x[1] for x in Vclist]
Errorx = [x * 0.01 for x in Flist]
Errory = [2 * 10 ** (math.floor(math.log(x, 10)) - 2) for x in Vlist]
# [print(f"{Errory[x]} {Vlist[x]}") for x in range(len(Flist))]

# plt.plot(Flist, Vlist)
plt.errorbar(
    Flist,
    Vlist,
    xerr=Errorx,
    yerr=Errory,
    capsize=5,
    color="black",
    ecolor="red",
)

plt.title("Frequency vs Amplitude over Resistor")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Voltage Amplitude (v)")
plt.semilogx()
plt.semilogy()
plt.savefig("FreqAmplRes", dpi=300)
