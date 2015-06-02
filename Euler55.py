# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:37:05 2012
Euler Project, Problem 55
"""

#if we take 47, reverse and add, 47 + 74 = 121, it is palindromic.
#but not all numbers produce palindromes so quickly or at all.
#a number that never forms a palindrome through the reverse and add 
#process is called a Lychrel number.

#given that for every number below ten-thousand it will become a 
#palindrome in less than 50 iterations or you can consider it Lychrel:
#how many Lychrel numbers are there below ten-thousand?

count = 0

#iterate through numbers up to 10,000
for i in range(10,10000):
    revi = int(str(i)[::-1])  #reverse number 
    sumi = i + revi  
    
    #set up loop to continue the reverse and add process from each sum
    loop = 0
    while str(sumi) != str(sumi)[::-1]:
        revsumi = int(str(sumi)[::-1])
        sumi = sumi + revsumi
        loop = loop + 1
        if loop == 50:
            count = count + 1
            break        

       
print 'Answer is:', count