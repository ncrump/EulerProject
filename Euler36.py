# -*- coding: utf-8 -*-
"""
Created on Tue Dec 4 17:07:05 2012
Euler Project, Problem 36
"""

#the decimal number 585 = 10010010012 (binary), is palindromic in both bases

#find the sum of all numbers, less than one million, which are 
#palindromic in base 10 and base 2.


from datetime import datetime
t1=datetime.now()

tot = 0

for i in range(int(1e6)):
    decnum = str(i)
    binum = bin(i)[2::]  #bin get binary of number and [2::] takes off first 2 digits
    
    #note: [::-1] reverses list or string
    if decnum == decnum[::-1] and binum == binum[::-1]:
        tot = tot + i
        
print 'Answer is:', tot
    

t2=datetime.now()
print '\nElapsed time:', t2-t1