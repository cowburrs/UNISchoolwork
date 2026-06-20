import matplotlib.pyplot as plt
import numpy as np
def linefit(xdata, ydata):
    xdata = np.array(xdata, dtype=float)
    ydata = np.array(ydata, dtype=float)
    m, b = np.polyfit(xdata, ydata, 1)
    x_fit = np.linspace(min(xdata), max(xdata), 200)
    plt.plot(x_fit, m * x_fit + b, "-b", label=f"Linear: {m:.2f}x + {b:.2f}")
    return m, b


def expfit(xdata, ydata):
    xdata = np.array(xdata, dtype=float)
    ydata = np.array(ydata, dtype=float)
    k, logA = np.polyfit(xdata, np.log(ydata), 1)
    A = np.exp(logA)
    x_fit = np.linspace(min(xdata), max(xdata), 200)
    plt.plot(x_fit, A * np.exp(k * x_fit), "-g", label=f"Exp: {A:.2f}e^({k:.2f}x)")
    return A, k


def powfit(xdata, ydata):
    xdata = np.array(xdata, dtype=float)
    ydata = np.array(ydata, dtype=float)
    n, logA = np.polyfit(np.log(xdata), np.log(ydata), 1)
    A = np.exp(logA)
    x_fit = np.linspace(min(xdata), max(xdata), 200)
    plt.plot(x_fit, A * x_fit**n, "-m", label=f"Power: {A:.2f}x^({n:.2f})")
    return A, n
