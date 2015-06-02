"""
Created on Thu Oct 24 16:14:05 2012
Euler Project, Problem 12
"""

#value of the first triangle number to have over five hundred divisors?

from datetime import datetime
t1=datetime.now()

import math

off = 0
trinum = 1
l = 0
i = 1

#for divisors of some number n, every divisor d that is < sqrt(n) will have a 
#counterpart that is also a divisor of n, which is n/d. So to find all
#divisors of n, only have to look at numbers up to sqrt(n).

while off == 0:
    divs = [j for j in range(2,int(math.sqrt(trinum))) if trinum % j == 0]
    l = len(divs)*2 + 2
    if l >= 500:
        print "Answer is:", trinum
        off = 1     
        
    else:
        print l
        i=i+1
        trinum = trinum+i   
   

t2=datetime.now()
print '\nElapsed time:', t2-t1