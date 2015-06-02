"""
Created on Wed Nov 14 15:51:05 2012
Euler Project, Problem 179
"""

#find the number of integers n between 1 and 10^7 for which 
#n and n + 1 have the same number of positive divisors.

#!!takes about 40 mins to run!
from datetime import datetime
t1=datetime.now()

print '\nRunning...\n'

import math

numdivs0 = 0
count = 0
i = 2
#for divisors of some number n, every divisor d that is < sqrt(n) will have a
#counterpart that is also a divisor of n, which is n/d. So to find all
#divisors of n, only have to look at numbers up to sqrt(n).

while i < int(10**7):
    numdivs1 = 0
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            numdivs1 = numdivs1 + 1
            if i/j != j:
                numdivs1 = numdivs1 + 1
        
    if numdivs1 == numdivs0:
        count = count + 1
        numdivs0 = numdivs1
        i = i + 1
    else: 
        numdivs0 = numdivs1
        i = i + 1
                
                
print 'Answer is:', count - 1

t2=datetime.now()
print '\nElapsed time:', t2-t1
