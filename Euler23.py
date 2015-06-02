"""
Created on Tue Nov 6 15:20:05 2012
Euler Project, Problem 23
"""

#a number n is called deficient if the sum of its proper divisors is less than n 
#and it is called abundant if this sum exceeds n.
#it can be shown that all integers greater than 28123 can be written as the sum 
#of two abundant numbers.

#find the sum of all the positive integers which cannot be written as the sum 
#of two abundant numbers.


from datetime import datetime
t1=datetime.now()

import math

#find all the abundant numbers from 12 to 28123 (not sure if I need this many though...)
abnums = []
i = 12
while i <= 28123:
    divsum = 1
    for j in range(2,int(math.sqrt(i))+1):
         if i % j == 0:
            divsum = divsum + j
            if i/j != j:
                divsum = divsum + i/j 

    if divsum > i:
        abnums.append(i)
        i = i + 1
    else: i = i + 1
      
#then get the sum of every two abundant numbers <= 28123 and store to array     
absums = []
for i in abnums:
    for j in abnums:
        num = i+j
        if num <= 28123:
            absums.append(num)
        else: break

#then do set on array of abnums to get rid of duplicates
#finally compare sets to get numbers that aren't sums of two abnums
notabsum = set(range(28124)) - set(absums)

    
print 'Answer is:',sum(list(notabsum))

t2=datetime.now()
print '\nElapsed time:', t2-t1



            
            
        
        

