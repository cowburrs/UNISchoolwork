from math import cos, pi

import numpy as np

norm = np.linalg.norm
f_vec = np.array([-1.1, -1.7, 1.1 * 12 / 5])
f = 80 * f_vec / norm(f_vec)
print(f)
import numpy as np

fi = np.radians(25)
theta = np.radians(20)
a = 7750

A = np.array([[np.cos(fi), np.cos(theta)], [np.sin(fi), -np.sin(theta)]])
b = np.array([a, 0])

c, d = np.linalg.solve(A, b)
print(c, d)
from sympy import Eq, cos, nsolve, rad, sin, symbols, deg

F, theta = symbols("F theta")
eq1 = Eq(F + F * sin(rad(64)), 675 * sin(theta))
eq2 = Eq(F * cos(rad(64)), 675 * cos(theta))

sol = nsolve([eq1, eq2], [F, theta], [346, 1])  # [500,1] = initial guesses
print(sol[1])
a = sol[1]
print(np.degrees(float(a)))
print("EOL")
