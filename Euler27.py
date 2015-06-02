"""
Created on Tue Nov 26 15:42:59 2012
Euler Project, Problem 27
"""

#Considering quadratics of the form: n**2 + an + b 
#where |a| < 1000 and |b| < 1000. 

#find the product of the coefficients a and b for the quadratic 
#that produces the maximum number of primes for consecutive 
#values of n, starting with n = 0.


from datetime import datetime
t1=datetime.now()

import math

#generate list of primes
primes=[2]
i=3
#number theory: greatest prime divisor of n is <= sqrt(n)
while i < int(1e4):
    for j in [p for p in primes[0 : int(math.sqrt(i))]]:
        if i % j == 0:
            i=i+2      #need only look at odds since prime
            break
    else:
        primes.append(i)
        i=i+2


#loop through a and b to check if result is prime
tot = 0
for a in range(-1000,1000):
    print a
    for b in range(-1000,1000):
        ntot = 0
        for n in range(0,1000):
            num = n**2 + a*n + b
            
            if num in primes:
                ntot = ntot + 1
            else: 
                if ntot > tot:
                    tot = ntot
                    wina = a
                    winb = b
                break        
            
                
print 'Answer is:', wina, winb, wina*winb

t2=datetime.now()
print '\nElapsed time:', t2-t1
