from sympy.vector import CoordSys3D
from sympy import rad, cos, sin

C = CoordSys3D("C")
x = C.i
y = C.j
z = C.k

beta = rad(29)
m1 = 16
m2 = 15
f1 = m1*cos(beta)*y - m1*sin(beta)*z
f2 = 5/13*m2*z-12/13*m2*x
print((-f2-f1).magnitude().evalf())
f3 = 13.8*x - 14*y + 1.99*z
from sympy import acos, deg

def angle_between(v1, v2, degrees=True):
    cos_theta = v1.dot(v2) / (v1.magnitude() * v2.magnitude())
    theta = acos(cos_theta)
    return deg(theta).evalf() if degrees else theta.evalf()

print(angle_between(f3, x))
print(angle_between(f3, y))
print(angle_between(f3, z))
print("EOL")
