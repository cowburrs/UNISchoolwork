import statistics

from uncertainties import ufloat

V = ufloat(1.5, 0.1)
R = ufloat(3, 0.1)
x = (V / R)
print(x)
a = ufloat(5,1)
t = ufloat(1.5,0.1)
print((1/2)*a*(t**2))
print(2.5*1.5*1.5)
polls = [51, 51, 52, 51, 52, 51, 51, 52, 51.5, 51, 51, 51.5]
print(sum(polls)/len(polls))
print(statistics.stdev([51, 51, 52, 51, 52, 51, 51, 52, 51.5, 51, 51, 51.5]))
temp19 = [13.96, 14.04, 13.83, 13.99, 13.99, 14.23, 13.90, 14.39, 14.09, 13.95]
temp20 = [14.22, 14.11, 14.16, 14.03, 14.03, 14.46, 14.48, 14.10, 14.04, 14.00]
print(sum(temp19)/len(temp19))
print(sum(temp20)/len(temp20))
print()
print(statistics.stdev(temp19))
print(statistics.stdev(temp20))
print(statistics.stdev(temp19) / (10 ** 0.5))
print(statistics.stdev(temp20) / (10 ** 0.5))
