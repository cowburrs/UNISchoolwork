
import statistics
from scipy import stats
from uncertainties import ufloat


def uprint(x):
    print(f"{(x).n:.5f}")  # print number
    print(f"{(x).s:.5f}")  # print uncertainty


numbers = list(range(1, 17))
mean = statistics.mean(numbers)
std = statistics.pstdev(numbers)
n = len(numbers)
se = std / (n**0.5)

pop_std = statistics.pstdev(numbers)
sam_std = statistics.stdev(numbers)
mean = statistics.mean(numbers)
right_tail = 1 - stats.norm.cdf(1)
left_tail = stats.norm.cdf(1)
two_tail = 1 - (2 * (1 - stats.norm.cdf(1)))

h1 = ufloat(45, 1)
h2 = ufloat(93, 0.5)
d1 = 2 * ((h1 * h2) ** 0.5)
d2 = 2 * ((5 / 7 * h1 * h2) ** 0.5)
print(d1)
print(d2)
listred = [
    14.3,
    14.5,
    15.1,
    12.5,
    13.2,
    13.2,
    13.9,
    13.9,
    12.4,
    10.8,
    10.5,
    13.4,
    13.3,
    14.0,
    15.4,
]
listblack = [
    14.5,
    14.4,
    12.6,
    13.8,
    14.2,
    14.5,
    12.8,
    13.3,
    13.3,
    13.4,
    12.5,
    16.0,
    17.8,
    15.5,
    13.3,
]
listred = list(map(lambda x: x + 72, listred))
listblack = list(map(lambda x: x + 72, listblack))
print(sum(listred) / len(listred))
print(statistics.stdev(listred))
print(statistics.stdev(listred) / len(listred))
print(sum(listblack) / len(listblack))
print(statistics.stdev(listblack))
print(statistics.stdev(listblack) / len(listblack))
