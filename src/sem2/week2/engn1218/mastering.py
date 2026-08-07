from math import e

from sympy import diff, simplify, solve, symbols, integrate, oo

t = symbols("t")
v = (10000 * t + 5) * (e ** (-400 * t))
i = (40 * t + 0.05) * (e ** (-400 * t))
t_max = solve(diff(v * i))[0]
w_max = (v * i).subs(t, t_max)
p = i*v
p_int = integrate(p, (t, 0, 10))
print(p_int*1e6)
print(19*5*1e-3)
print("EOL")
