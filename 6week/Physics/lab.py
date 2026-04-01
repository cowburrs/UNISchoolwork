from math import e
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import numpy as np  # imports not on the top nooo
import pandas as pd
from uncertainties import ufloat  # type:ignore

###
### PART 2
###
x = ufloat(10.34, 0.04)
y = ufloat(7.66, 0.03)
G = 6.67e-11


print(f"Equation1 is{ (x**2 + y**2) ** 0.5 }")
print(f"Equation2 is{ (4 * x) / (e**y) }")
print(f"Equation3 is{ (G * x) / y }") 


###
### PART 3
###
df = pd.read_excel("RawSupernovaData.ods", engine="odf")

x = df["Distance"]
y = df["Redshift"]
error = df["Uncertainty"]

plt.scatter(x, y)
xerror = error
plt.errorbar(
    x,
    y,
    xerr=xerror,
    fmt="o",
    color="black",
    ecolor="red",
    capsize=5,
    elinewidth=2,
    label="Data with Uncertainty",
)
plt.xlabel("Distance")
plt.ylabel("Redshift")
plt.title("Supernova Distance vs Redshift")
plt.savefig("supernova_plot.png", dpi=150, bbox_inches="tight")
# plt.show()
print()
print("Saved plot to supernova_plot.png")


###
### PART 4
###
fa = pd.read_csv("DataC.csv")
fb = pd.read_csv("DataD.csv")
a = ufloat(np.mean(fa["Strength"]), np.std(fa["Strength"]) / len(fa["Strength"]))
b = ufloat(np.mean(fb["Strength"]), np.std(fb["Strength"]) / len(fa["Strength"]))
print()
print(f"Alloy C Strength is {a}")
print(f"Alloy D Strength is {b}")
print(f"The difference between the two is {a - b}")
print(f"so D is around {(b/a)*100 - 100}% better than C")
print("which is marginal but still something")
print("it is comfortably very slightly better, only slightly")


###
### PART 5
###
plt.clf()
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
plt.savefig("xyplot.png", dpi=150, bbox_inches="tight")

print()
print("Saved plot to xyplot.png")
