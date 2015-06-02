"""
Created on Thu Nov 8 18:00:05 2012
Euler Project, Problem 63
"""

#the 5-digit number 16807=75^5 is also a fifth power. 
#similarly the 9-digit number 134217728=89^9 is a ninth power.

#how many n-digit positive integers exist which are also an nth power?

from datetime import datetime
t1=datetime.now()

import math
count = 0
i = 1

while i <= int(10**5):
    i = i + 1
    for j in range(2,1000): 
        n = i**j
        if int(math.log10(n))+1 == j:
            count = count + 1
            print count 
            
print 'Answer is:', count

t2=datetime.now()
print '\nElapsed time:', t2-t1
    