"""
Created on Fri Nov 16 22:55:59 2012
Euler Project, Problem 47
"""

#find the first four consecutive integers to have four distinct primes factors. 
#what is the first of these numbers?


from datetime import datetime
t1=datetime.now()

import math

primes=[2]
i=3

#number theory: greatest prime divisor of n is <= sqrt(n)
while i < int(1e3):
    for j in [p for p in primes[0 : int(math.sqrt(i))]]:
        if i % j == 0:
            i=i+2      #need only look at odds since prime
            break
    else:
        primes.append(i)
        i=i+2
        print i
  

f1 = []
f2 = []      
i = 2
while i < int(1e3):      
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0 and j in primes:
            if i/j != j:
                divsum1 = divsum1 + i/j
    
t2=datetime.now()
print '\nElapsed time:', t2-t1
