"""
Created on Thu Oct 18 17:29:20 2012
Euler Project, Problem 6
"""

#difference between the square of the sum and the sum of the squares
#of the first one hundred natural numbers 

r=range(1,101)
rsqr=[]
for i in r:
    rsqr.append(i**2)
    
print 'difference is', (sum(r)**2) - sum(rsqr)
