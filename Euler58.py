"""
Created on Wed Nov 7 15:45:07 2012
Euler Project, Problem 58
"""

#starting with the number 1 and moving to the right in a counter-clockwise direction as below:
#8 out of the 13 numbers lying along both diagonals are prime, or about 62%

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

#what is the side length of the square spiral for which the ratio of primes
#along both diagonals first falls BELOW 10%?

from datetime import datetime
t1=datetime.now()

print 'Running...\n'

import math

#get diagonals as before in Problem 28
#this time, check if elements are primes
#NOTE: values along diagonals are same for clockwise or counter-clockwise

incTR = 3     #first value in diagTR
dim = 2       #collects dimension of matrix - 1
ndiags = 1    #total number of diagonal values (starting with 1 at center)
frac = 1      #fraction of primes
count = 0     #counts number of primes

off = 0

while off == 0:
    #get diagonal values
    diagTR = incTR**2
    diagTL = diagTR - dim
    diagBR = diagTR - (int(math.sqrt(diagTR)-1)*3)
    diagBL = diagBR + dim

    diags = []
    diags.append(diagBR)
    diags.append(diagBL)
    diags.append(diagTL)
    diags.append(diagTR)

    #increment counters
    incTR = incTR + 2    #want to keep odd
    dim = dim + 2        #want to keep even
    ndiags = ndiags + 4

    #check if diagonals are primes
    for i in diags:
        for j in range(3,int(math.sqrt(i))+1,2):
            if i % j == 0:
                break
        else:
            count = count + 1

    frac = float(count)/ndiags
    print frac
    if frac < 0.10:
        off = 1

      
print 'Answer is:',dim-1

t2=datetime.now()
print '\nElapsed time:', t2-t1