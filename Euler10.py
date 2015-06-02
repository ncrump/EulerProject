"""
Created on Thu Oct 18 18:31:59 2012
Euler Project, Problem 10
"""

#find the sum of all primes below 2 million

#!! takes about 30 mins to run!
from datetime import datetime
t1=datetime.now()

import math

primes=[2]
i=3

#number theory: greatest prime divisor of n is <= sqrt(n)
while i < 2e6:
    for j in [p for p in primes[0 : int(math.sqrt(i))]]:
        if i % j == 0:
            i=i+2      #need only look at odds since prime
            break
    else:
        primes.append(i)
        i=i+2
        print i
    
print sum(primes)
    
t2=datetime.now()
print '\nElapsed time:', t2-t1
