"""
Created on Thu Nov 15 11:42:59 2012
Euler Project, Problem 35
"""

#the number 197 is called a circular prime because all rotations of the
#digits: 197, 971, and 719, are themselves prime.

#how many circular primes are there below one million?


from datetime import datetime
t1=datetime.now()

import math
import numpy
n = int(10**6)

primes = [2]
i = 3

#generate list of all primes up to one-million
#number theory: greatest prime divisor of n is <= sqrt(n)
while i <= n:
    for j in [p for p in primes[0:int(math.sqrt(i))]]:
        if i % j == 0:
            i=i+2      #need only look at odds since prime
            break
    else:
        primes.append(i)
        i=i+2
    

#check if rotations of each prime are also primes
count = 4  #to account for 2,3,5 and 7
for i in primes[4:len(primes)]:  #start after number 7
    
    vals = []
    pri = str(i)
    vals = [pri[j] for j in range(len(pri))]  #break number into array for indexing
    
    #this loop first rotates the number then checks if it's in primes
    for k in range(0,len(vals)):
        num = ''
        roll = numpy.roll(vals,k+1)  #rotates last value(s) in array into first position and so on
        for s in roll:
            num = num + str(s)  #rebuilds rotated number from array values
            
        #check if rotated number in primes list
        if int(num) not in primes:
            break
        elif int(num) in primes and k == len(vals)-1:
            count = count + 1
        

print 'Answer is:', count               
    
t2=datetime.now()
print '\nElapsed time:', t2-t1
