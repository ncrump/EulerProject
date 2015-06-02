"""
Created on Fri Nov 2 11:25:05 2012
Euler Project, Problem 20
"""

#sum of the digits of the number 100!

import math

n = str(math.factorial(100))
sum0 = 0

for i in range(0,len(n)):
    sum0 = sum0 + int(n[i])

print sum0