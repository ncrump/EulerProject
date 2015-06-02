"""
Created on Fri Nov 2 14:40:19 2012
Euler Project, Problem 104
"""

#find the first Fibonacci term for which the first nine digits AND the last
#nine digits are 1-9 pandigital (contain all digits from 1-9 in any order)


#NOTE: takes WAY too long to turn Fib numbers into strings to index
#so implementing this method to get first and last 9 digits without using strings


#!!takes about 2 hrs, 12 mins!
from datetime import datetime
t1=datetime.now()

import math

print '\nRunning...\n'

#start with 2nd and 3rd terms in sequence (1 is also 1st term)
f1 = 1   
f2 = 2
term = 3

#create check list for first and last 9 digits
chk = ['1','2','3','4','5','6','7','8','9']

off = 0

while off == 0:
    #create lists to store first and last 9 digits of Fib number
    begNums = []
    endNums = []
    
    #get Fibonacci number and term
    fib = f1 + f2
    term = term + 1
    
    lenFib = int(math.log10(fib))+1  #gets length of Fib number without using strings
    
    if lenFib <= 18:  
        f1 = f2
        f2 = fib
       
    else:
        #gets first 9 digits of Fib for check
        begFib, poo = divmod(fib, 10**(lenFib-9)) 
        
        #copy Fib to use for last 9 digits check
        endFib = fib
        
        #peel off each digit of first and last nine digits of Fib and store to arrays
        for i in range(9,0,-1):
            begFib, rem1 = divmod(begFib,10)  #pulls off each digit in first 9
            begNums.append(str(rem1))
    
            endFib, rem2 = divmod(endFib,10)  #pulls off each digit in last 9
            endNums.append(str(rem2))
        
        
        #sort from lowest to highest value and check if each is equal to list of 1-9
        if sorted(begNums) == chk and sorted(endNums) == chk:
            off = 1

        else:
            #print term
            f1 = f2
            f2 = fib
       

print 'Answer is:', term

t2=datetime.now()
print '\nElapsed time:', t2-t1