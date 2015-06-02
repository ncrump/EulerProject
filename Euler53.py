"""
Created on Wed Dec 12 13:33:03 2012
Euler Project, Problem 53
"""

#in combinatorics, we use the designation "n choose k" to refer the 
#number ways k numbers can be selected from a sequence of n number.
#in general "n choose k" =  n!/(n-k)!k!

#how many values of  "n choose k" for 1 <= n <= 100 are greater than one-million?


import math

count = 0
n = 20

#this is brute force method and very straight forward
#however, there is a very elegant way of doing it by realizing that for some
#sequence of numbers n, the maximum number of combinations are formed when k 
#is exactly n/2. That would require significantly less computation than going 
#through each k from 2 to n-1. But this runs in less than a second so who cares...
while n <= 100:
    for i in range(2,n):
        combs = math.factorial(n) / (math.factorial(n-i)*math.factorial(i))
        if combs > 1e6:
            count = count + 1
    
    n = n + 1
            
print 'Answer is:', count