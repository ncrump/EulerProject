"""
Created on Thu Nov 29 16:58:22 2012
Euler Project, Problem 37
"""

#find the sum of the only eleven primes that are both truncatable 
#from left to right and right to left.

from datetime import datetime
t1=datetime.now()

import math

primes = [2]
i = 3

#number theory: greatest prime divisor of n is <= sqrt(n)
while i < int(1e6):
    for j in [p for p in primes[0 : int(math.sqrt(i))]]:
        if i % j == 0:
            i=i+2      #need only look at odds since prime
            break
    else:
        primes.append(i)
        i=i+2
    
    
trunc = []
while len(trunc) < 11:
    for i in range(4,len(primes)):
        print len(primes) - i
        appnd = 'Y'
        p = str(primes[i])
        l = len(p)
        
        for j in range(1,l):
            if int(p[0:j]) not in primes or int(p[j:l]) not in primes:
                appnd = 'N'
                break
            
        if appnd == 'Y':
            trunc.append(int(p))

        
print 'Answer is:', sum(trunc)

t2=datetime.now()
print '\nElapsed time:', t2-t1
