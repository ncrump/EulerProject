"""
Created on Tue Dec 11 17:11:59 2012
Euler Project, Problem 41
"""

#an n-digit number is pandigital if it makes use of all the digits 
#1 to n exactly once.

#what is the largest n-digit pandigital prime that exists?

#!!Takes about 15 minutes to run!
from datetime import datetime
t1=datetime.now()

import math

primes = [2]
i = 3

#first get list of primes
#number theory: greatest prime divisor of n is <= sqrt(n)
print 'Running Primes...'
while i < 1e7:  #trial and error to get upper bound needed for greatest pandigital prime...
    for j in [p for p in primes[0 : int(math.sqrt(i))]]:
        if i % j == 0:
            i = i + 2      #need only look at odds since prime
            break
    else:
        primes.append(i)
        i = i + 2

        
#check if prime is 1-n pandigital  
panprime = 0      
print 'Running Pandigital Check...' 
for i in primes:
    numlst = sorted(set(str(i)))  #remove duplicate digits and sort from lowest digit
    check = [str(s) for s in range(1,len(numlst)+1)]  #create string of values from 1-n of length of numlst
    #check if numlst is 1-n pandigital    
    if '0' not in numlst:
        if len(str(i)) == len(numlst):
            if numlst == check:
                if i > panprime:
                    panprime = i
    
    
print 'Answer is:', panprime

t2=datetime.now()
print '\nElapsed time:', t2-t1
