"""
Created on Thu Oct 18 17:39:51 2012
Euler Project, Problem 7
"""

#10,001st prime number

from datetime import datetime
t1=datetime.now()

count=0
i=3
primes=[2]

while count < 10001:  
    for j in primes:
        if i % j == 0:
            i=i+2      #need only look at odds since prime
            break
    else:
        count=count+1
        print 'count', count
        primes.append(i)
        i=i+2

print primes[count-1]

t2=datetime.now()
print '\nElapsed time:', t2-t1
