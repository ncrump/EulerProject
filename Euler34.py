"""
Created on Thu Nov 8 19:50:05 2012
Euler Project, Problem 34
"""

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#find the sum of all numbers equal to the sum of the factorial of their digits

import math

count = 0
tot = 0
i = 11

while count < 2:   #had to run it through once to figure out there are only 2  
    sum0 = 0
    si = str(i)
    len0 = len(si)
    for j in range(0,len0):
        sum0 = sum0 + math.factorial(int(si[j]))
    
    if sum0 == i:
        count = count + 1
        tot = tot + sum0
        print i
        i = i + 1
    else:
        i = i + 1
        
print 'Answer is:', tot
    