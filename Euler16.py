"""
Created on Thu Nov 1 12:44:05 2012
Euler Project, Problem 16
"""

#sum of the digits of the number 2^(1000)

n = str(2**1000)
sum0 = 0

for i in range(0,len(n)):
    sum0 = sum0 + int(n[i])

print sum0