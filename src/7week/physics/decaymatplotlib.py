import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

p = 0.01
dt = 1

# Set up loop

n = 100000
t = 0.0
tlist = []
nlist = []


while t < 500:

    # print(t,n)
    n += -n * p * dt
    t += dt
    nlist.append(n)
    tlist.append(t)

# plot our graph

plt.plot(tlist, nlist, "-r")
plt.xlabel("Time (s)")
plt.ylabel("Number")
# plt.savefig("decay.png", dpi=300)
plt.show()
