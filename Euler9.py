"""
Created on Thu Oct 18 21:48:21 2012
Euler Project, Problem 9
"""

#there exists exactly one Pythagorean triplet for which a + b + c = 1000.
#find the product abc.

from datetime import datetime
t1=datetime.now()

import math

for i in range(1,1000):
    for j in range(i+1,1000):
        n = i**2 + j**2
        m = math.sqrt(n)
        #check if sqrt(n) is a rational #, and other conditions...
        if m == math.floor(m) and m > j and i+j+m == 1000:
            print i, j, m
            print i*j*m
              
t2=datetime.now()
print '\nElapsed time:', t2-t1
