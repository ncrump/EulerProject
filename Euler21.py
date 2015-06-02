"""
Created on Fri Nov 16 11:32:22 2012
Euler Project, Problem 21
"""

#let d(n) be the sum of proper divisors of n (not including n).
#if d(a) = b and d(b) = a, where a != b, then a and b are amicable numbers.

#evaluate the sum of all the amicable numbers under 10000.


from datetime import datetime
t1=datetime.now()

import math 

amicables = []
i = 2

#for divisors of some number n, every divisor d that is < sqrt(n) will have a
#counterpart that is also a divisor of n, which is n/d. So to find all
#divisors of n, only have to look at numbers up to sqrt(n).

while i < 10000:
    divsum1 = 1
    divsum2 = 1
    #first get sum of divisors of i
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            divsum1 = divsum1 + j
            if i/j != j:
                divsum1 = divsum1 + i/j
    
    if divsum1 > 1 and divsum1 != i:  #exclude primes (divsum1=1) and if sum of divisors of i is equal to i
        #then get sum of divisors of the sum of divisors of i
        for k in range(2,int(math.sqrt(divsum1))+1):
            if divsum1 % k == 0:
                divsum2 = divsum2 + k
                if divsum1/k != k:
                    divsum2 = divsum2 + divsum1/k
                    
    #check if amicable                
    if divsum2 == i and divsum2 not in amicables:
        print i, divsum1
        amicables.append(i)
        amicables.append(divsum1)
        i = i + 1
    else: 
        i = i + 1
        

print 'Answer is:', sum(amicables)

t2=datetime.now()
print '\nElapsed time:', t2-t1
