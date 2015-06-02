"""
Created on Wed Dec 12 10:40:59 2012
Euler Project, Problem 49
"""

#the arithmetic sequence, 1487, 4817, 8147, in which each of the 
#terms increases by 3330, is unusual in two ways: (i) each of the 
#three terms are prime, and, (ii) each of the 4-digit numbers are 
#permutations of one another.

#there is one other 4-digit increasing sequence. what 12-digit 
#number do you form by concatenating the three terms in this sequence?


import math
import itertools

primes = [2]
i = 3

#first get list of primes
#number theory: greatest prime divisor of n is <= sqrt(n)
while i < 10000:  #trial and error to get upper bound needed for greatest pandigital prime...
    for j in [p for p in primes[0 : int(math.sqrt(i))]]:
        if i % j == 0:
            i = i + 2      #need only look at odds since prime
            break
    else:
        primes.append(i)
        i = i + 2
        

#loop through primes and generate list of permutations for primes > 4 digits
#then check if each meets conditions and is in prime list
match = []
for i in primes:
    if len(str(i)) == 4:
        concat = str(i)
        num = i
        perms = list(itertools.permutations(str(i)))  #get list of permutations
        
        #create string value out of each list in permutations list
        for j in range(len(perms)):
            perm = ''
            for k in range(4):
                perm = perm + perms[j][k]
            
            #check if permutation is prime and meets conditions
            perm = int(perm)
            if perm > i:
                diff = perm - num
                if perm in primes and diff == 3330:
                    concat = concat + str(perm)
                    num = perm
                    
        if len(concat) == 12:
            match.append(concat)
            
print 'Answer is:', match[1]
