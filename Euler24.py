"""
Created on Thu Nov 15 15:37:2:59 2012
Euler Project, Problem 24
"""

#if all the permutations of a sequence of characters is listed numerically 
#or alphabetically, it is called lexicographic order.

#what is the millionth lexicographic permutation of the digits 0 through 9? 


import itertools

list0 = range(10)
#computes all permutations of a list using itertools function 
perms = list(itertools.permutations(list0))
        
print 'Answer is:', perms[int(10**6)-1]              
