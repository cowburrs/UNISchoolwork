#!/usr/bin/env python3
from math import erf, sqrt

def oneTailProbability(stdev):
    return 1/2*(1-erf(stdev/sqrt(2)))

print(oneTailProbability(2))
