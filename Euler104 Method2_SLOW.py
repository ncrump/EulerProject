"""
Created on Fri Nov 2 14:40:19 2012
Euler Project, Problem 104
"""

#find the first Fibonacci term for which the first nine digits AND the last
#nine digits are 1-9 pandigital (contain all digits from 1-9 in any order)


#!!takes WAY too long!

from datetime import datetime
t1=datetime.now()

#start with 2nd and 3rd terms in sequence (1 is also 1st term)
f1 = 1   
f2 = 2
term = 3

#create check list for first and last 9 digits
chk = ['1','2','3','4','5','6','7','8','9']

off = 0

while off == 0:

    #get Fibonacci number and term
    fib = str(f1 + f2)
    term = term + 1
       
    if len(fib) <= 18:
        f1 = f2
        f2 = int(fib)
       
    else:
        fib1 = fib[0:9]                    #get first 9 digits of Fib number
        fib2 = fib[len(fib)-9:len(fib)]    #get last 9 digits of Fib number         
        
        #sort from lowest to highest value
        #and check if each is equal to list of 1-9
        if sorted(fib1) == sorted(fib2) == chk:
            off = 1

        else:
            print term
            f1 = f2
            f2 = int(fib)
       

print 'Answer is:', term

t2=datetime.now()
print '\nElapsed time:', t2-t1