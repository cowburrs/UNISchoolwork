import matplotlib.pyplot as plt
import numpy as np  # imports not on the top nooo
import pandas as pd
from uncertainties import ufloat  # type:ignore

df = pd.read_csv("linedata.csv")

x = df["x"]
y = df["y"]
yerror = df["yerr"]

plt.errorbar(
    x,
    y,
    yerr=yerror,
    fmt="o",
    color="black",
    ecolor="red",
    capsize=2,
    elinewidth=2,
    label="Data with Uncertainty",
)
m, b = np.polyfit(x, y, 1)

plt.plot(x, m*x + b, color='blue', label='Line of Best Fit')

# plt.xlabel("x")
# plt.ylabel("y")
plt.title("x vs y")

plt.text(7, 1, f"y = {m}x + {b}")
plt.show()
plt.savefig("xyplot.png", dpi=150, bbox_inches="tight")

