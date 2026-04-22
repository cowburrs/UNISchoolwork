import helpers
import matplotlib
import pandas as pd

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import math

# plt.title("AnneTemp")
# at = pd.read_csv("AnneTemp.csv")
# x = at.Minutes[60:]
# y = at.Temperature[60:]
# plt.plot(x, y, ".b", label="T2")
# helpers.expfit(x, y)
# plt.xlabel("Minutes")
# plt.ylabel("Temperature")

# plt.title("FredTemp")
# at = pd.read_csv("FredTemp.csv")
# x = at["Minutes"][60:]
# y = at.Temperature[60:]
# plt.plot(x, y, ".b", label="T2")
# helpers.expfit(x, y)
# plt.xlabel("Minutes")
# plt.ylabel("Temperature")

# # NOTE: IRSENSOR
# plt.title("IRsensor")
# at = pd.read_csv("IRsensor.csv")
# x = at["Minutes"][90:-80]
# print(len(x))
# y = at.Signal[90:-80]
# plt.plot(x, y, ".b", label="T2")
# helpers.expfit(x, y)
# plt.xlabel("Minutes")
# plt.ylabel("Temperature")

# NOTE: anne phone
# plt.title("Annephone")
# at = pd.read_csv("Annephone.csv")
# x = at["Minutes"]
# y = at.T2
# plt.plot(x, y, ".b", label="T2")
# helpers.linefit(x, y)
# x = at["Minutes"]
# y = at.T1
# plt.plot(x, y, ".b", label="T2")
# helpers.linefit(x, y)
# 4370 from t2, 2341 from t1

# # NOTE: fredphone
# plt.title("Fredphone")
# at = pd.read_csv("Fredphone.csv")
# rangex = 250
# rangey = -300
# x = at["Minutes"][rangex:rangey]
# y = at.T2[rangex:rangey]
# plt.plot(x, y, ".b", label="T2")
# helpers.expfit(x, y)
# 4356

# x = at["Minutes"][0:150]
# y = at.T2[0:150]
# plt.plot(x, y, ".b", label="T2")
# helpers.expfit(x, y)
# plt.xlabel("Minutes")
# plt.ylabel("T2 distance")
# 4371

# at["Minutes"][0:150]
# y = at.T1[0:150]
# plt.plot(x, y, ".b", label="T1")
# helpers.expfit(x, y)
# plt.xlabel("Minutes")
# plt.ylabel("T1 distance")
# 2331

# x = at["Minutes"]
# y = at.T1
# plt.plot(x, y, ".r", label="T2")


# # NOTE: LOUSAPHONEDATA
# 4383, fred is 4371, they not doing the uhh....
# plt.title("Louisaphone")
# at = pd.read_csv("Louisaphone.csv")
# x = at["Minutes"][:510]
# y = at.T1[:510]
# print(y.std()) # NOTE: 5
# c = y.std()
# plt.plot(x, y, ".b", label="T1")
# helpers.linefit(x, y)
# plt.xlabel("Minutes")
# plt.ylabel("Distance")

at = pd.read_csv("Louisaphone.csv")
x = at["Minutes"][513:540]
y = at.T1[513:540]
mean = sum(y) / len(y)
print(mean)
print(y.std())
print(y.std()/math.sqrt(28))
plt.plot(x, y, ".b", label="T1")
helpers.linefit(x, y)
plt.xlabel("Minutes")
plt.ylabel("Distance")


# NOTE: helpers
# helpers.linefit(x, y)
# helpers.powfit(x, y)
# plt.xlabel("Minutes")
# plt.ylabel("Temperature")
plt.legend()
plt.show()
