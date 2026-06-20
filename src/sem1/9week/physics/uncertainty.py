from uncertainties import ufloat

amplitude = ufloat(12, 0.1)
print(amplitude / 2)
vforwardbias = ufloat(5, 0.1)
vnegativebias = ufloat(0.6, 0.1)
print(vforwardbias + vnegativebias)
