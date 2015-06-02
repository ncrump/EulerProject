"""
Created on Thu Oct 18 14:20:56 2012
Euler Project, Problem 3
"""

#largest prime factor of 600851475143 

primefactor=[]
for i in range(3,10000,2): #need only check odds since has to be prime
    if 600851475143 % i == 0:
        for j in range(2,i):
            if i % j == 0:
                break
        else: primefactor.append(i)

print primefactor

