"""
Created on Tue Nov 13 14:28:59 2012
Euler Project, Problem 50
"""

#which prime below one-million can be written as the sum of the most
#consecutive primes?


from datetime import datetime
t1=datetime.now()

import math
n = int(10**6)

primes=[2]
i=3

#first generate list of all primes up to one-million
#number theory: greatest prime divisor of n is <= sqrt(n)
while i <= n:
    for j in [p for p in primes[0:int(math.sqrt(i))]]:
        if i % j == 0:
            i=i+2      #need only look at odds since prime
            break
    else:
        primes.append(i)
        i=i+2
        
        
#then sum over consecutive primes in list while checking if prime 
#and keeping track of the length of consecutive primes
#only keeping the sum of the longest consecutive primes
sum0 = 0
sum1 = 0
len1 = 0

for i in range(0,5):  #just guessing here to look only out to five positions
    for j in range(i,len(primes)):
        sum0 = sum(primes[i:j])
        len0 = j - i - 1
        if sum0 >= n:
            break
        elif sum0 in primes and sum0 > sum1 and sum0 < n and len0 > len1:
            sum1 = sum0
            len1 = len0
                          
    
print 'Answer is:', sum1
    
t2=datetime.now()
print '\nElapsed time:', t2-t1
