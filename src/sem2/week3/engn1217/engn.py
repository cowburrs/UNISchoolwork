from math import cos, sin, tan

from sympy import Matrix, linsolve, rad, symbols
#
# x1 = Matrix([1.48, 0, 0])
# x2 = Matrix([0.53, 0, 0])
# y1 = Matrix([0, 0.44, 0])
# y2 = Matrix([0, 1.372, 0])
# z1 = Matrix([0, 0, 0.837])
# z2 = Matrix([0, 0, 0.911])
#
#
# A = x1 + z1
# B = x2
# C = y2 + z2
# D = x2 + y1
# mg = 9.8 * 11.5
# mg_vec = mg * Matrix([0, 0, 1])
# DA = (A - D) / (A - D).norm()
# DB = (B - D) / (B - D).norm()
# DC = (C - D) / (C - D).norm()
# # HOW DO I SOLVE x * DA + y*DB + z*DC + mg_vec = 0
# M = DA.row_join(DB).row_join(DC)
# rhs = mg_vec
# x, y, z = symbols("x y z")
# sol = linsolve((M, rhs), (x, y, z))
# print("EOL")

h = Matrix([0, 7.33, 0])
l = Matrix([0, 0, 0.929])
x = Matrix([2.47, 0, 0])
theta = rad(39)
fi = rad(13)
mg = -Matrix([0, 224 * 9.81, 0])
CA_vec = Matrix([cos(theta), -sin(theta), 0]).normalized()
CD_vec = (h - x).normalized()
CE_vec = (l - h).normalized()
CF_vec = (-l - h).normalized()
print(CE_vec)
CA_mag = mg.norm() / (tan(fi) * cos(theta) + sin(theta))
print(CA_mag)

M = CD_vec.row_join(CE_vec).row_join(CF_vec)
rhs = -CA_vec * CA_mag
x, y, z = symbols("x y z")
sol = linsolve((M, rhs), (x, y, z))
print(sol)
print("EOL2")
