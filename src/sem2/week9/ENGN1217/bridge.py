from sympy import Eq, linsolve, symbols, sqrt

w = symbols("w")
f1 = symbols("f1")
f2x = symbols("f2x")
f2y = symbols("f2y")
f3 = symbols("f3")
f4x = symbols("f4x")
f4y = symbols("f4y")
f5x = symbols("f5x")
f5y = symbols("f5y")
f6 = symbols("f6")
f7 = symbols("f7")
f8 = symbols("f8")
f9 = symbols("f9")
f10 = symbols("f10")
f11 = symbols("f11")

eqs = [
    Eq(f1, -w),
    Eq(f2y, -f1 / 2),
    Eq(f2y / 60, f2x / 45),
    # f2
    Eq(f3, -f2y),
    Eq(f4y, -f3),
    Eq(f4y / 60, f4x / 45),
    # f4
    Eq(f5y, -(1 / 4) * w),
    Eq(f5y / 60, f5x / 45),
    # f5
    Eq(f6, -f5y - f4y),
    Eq(f7, f5x - f4x),
    Eq(f8, f7 - f2x),
    Eq(f9, -f5x),
    Eq(f10, f9),
    Eq(f11, f4x + f10),
]

sol = linsolve(eqs, f1, f2x, f2y, f3, f4x, f4y, f5x, f5y, f6, f7, f8, f9, f10, f11)
print(sol)

names = [
    "f1",
    "f2x",
    "f2y",
    "f3",
    "f4x",
    "f4y",
    "f5x",
    "f5y",
    "f6",
    "f7",
    "f8",
    "f9",
    "f10",
    "f11",
]
values = dict()

for name, val in zip(names, list(sol)[0]):
    values[name] = val
    print(name, "=", val)


def mag(a, b):
    return sqrt(a**2 + b** 2)


print("f2x")
print(mag(values["f2x"], values["f2y"]))

print("f4x")
print(mag(values["f4x"], values["f4y"]))

print("f5x")
print(mag(values["f5x"], values["f5y"]))
