# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:54:07 2012
Euler Project, Problem 14
"""

#using the following iterative sequence for positive integers:
#n → n/2    (if n is even)
#n → 3n + 1 (if n is odd)

#which starting number, under one million, produces the longest chain?

from datetime import datetime
t1=datetime.now()

chainlen = 0

for i in range(2, int(1e6)):
    chain = []
    n = i
    print n
    while n > 1:
        chain.append(n)
        if n % 2 == 0:
            n = n/2
            if n == 1:
                if len(chain) > chainlen:
                    chainlen = len(chain)
                    winner = i
                    chain = []
        elif n % 2 != 0:
            n = 3*n + 1  
            if n == 1:
                if len(chain) > chainlen:
                    chainlen = len(chain)
                    winner = i
                    chain = []
                    
print "Answer is:",winner, "Chain length:",chainlen

t2=datetime.now()
print '\nElapsed time:', t2-t1
