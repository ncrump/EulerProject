"""
Created on Thu Oct 18 10:30:56 2012
Euler Project, Problem 1
"""

#sum of all multiples of 3 or 5 below 1000

mults=[]
mult3=range(3,1000,3)
mult5=range(5,1000,5)
#get multiples of 5 that are not also multiples of 3
for i in mult5:
    for j in mult3:
        if i == j:
            break
    else: mults.append(i)

print "sum of all multiples of 3 or 5 below 1000 is", sum(mult3)+sum(mults)


#much faster way to generate multiples of 3 or 5
#----------------------------------------------------------------  
#mults=[n for n in range(1,1000) if n%3==0 or n%5==0]
#print "sum of all multiples of 3 or 5 below 1000 is", sum(mults)
#----------------------------------------------------------------
