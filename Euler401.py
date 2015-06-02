"""
Created on Mon Nov 12 16:12:05 2012
Euler Project, Problem 401
"""

#let sigma2(n) be the sum of the squares of the divisors of n. Thus sigma2(6)=50.
#then let SIGMA2 represent the summation of sigma2, that is SIGMA2(n)=sum(sigma2(i)) for i=1 to n.
#the first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.

#find SIGMA2(10^15) modulo 109.

#!!DID THE MATH - WILL TAKE 32 MILLION YEARS TO FINISH!!
from datetime import datetime
t1=datetime.now()

import math

print '\nRunning...\n'

sig2 = 1
i = 2

#for divisors of some number n, every divisor d that is < sqrt(n) will have a
#counterpart that is also a divisor of n, which is n/d. So to find all
#divisors of n, only have to look at numbers up to sqrt(n).

while i <= int(10**15):
    sig1 = 1 + i**2
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            d1 = j
            sd1 = d1**2
            sig1 = sig1 + sd1
            if float(i)/d1 != d1:
                d2 = float(i)/d1
                sd2 = d2**2
                sig1 = sig1 + sd2
    sig2 = sig2 + sig1
    i = i + 1

    #print i

print 'Answer is:', sig2 % int(10**9)

t2=datetime.now()
print '\nElapsed time:', t2-t1
