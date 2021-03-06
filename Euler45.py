# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:24:05 2012
Euler Project, Problem 45
"""

#triangle, pentagonal, and hexagonal numbers are generated by:
#Triangle 	  	Tn=n(n+1)/2 	1, 3, 6, 10, 15, ...
#Pentagonal 	Pn=n(3n−1)/2 	1, 5, 12, 22, 35, ...
#Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...

#it can be verified that T285 = P165 = H143 = 40755.

#find the next triangle number that is also pentagonal and hexagonal.

from datetime import datetime
t1=datetime.now()

T = []
P = []
H = []

i = 1
while i < int(10**5):
    T.append(i*(i+1)/2)
    P.append(i*(3*i-1)/2)
    H.append(i*(2*i-1))
    i = i + 1

count = 0
while count < 3:    
    for i in T:
        for j in P:
            
            if i < j:
                break
            
            elif i == j:
                for k in H:                
                    if i < k:
                        break
                    elif i == k:
                        count = count + 1
                        print k
  

t2=datetime.now()
print '\nElapsed time:', t2-t1