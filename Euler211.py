"""
Created on Wed Nov 14 16:12:22 2012
Euler Project, Problem 211
"""

#find the sum of all numbers between 0 and 64,000,000 such that the 
#sum of the squares of its divisors is a perfect square.

from datetime import datetime
t1=datetime.now()

print '\nRunning...\n'

import math 

tot = 0
i = 2

#for divisors of some number n, every divisor d that is < sqrt(n) will have a
#counterpart that is also a divisor of n, which is n/d. So to find all
#divisors of n, only have to look at numbers up to sqrt(n).

while i < 64000000:
    sum0 = 1 + i**2
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            sum0 = sum0 + j**2
            if i/j != j:
                sum0 = sum0 + (i/j)**2
    
    if math.sqrt(sum0) == int(math.sqrt(sum0)):
        tot = tot + i
        i = i + 1
    else:
        i = i + 1
        

print 'Answer is:', tot

t2=datetime.now()
print '\nElapsed time:', t2-t1
