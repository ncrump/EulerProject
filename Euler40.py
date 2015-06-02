"""
Created on Thu Nov 29 16:43:22 2012
Euler Project, Problem 40
"""

#an irrational decimal fraction is created by concatenating the 
#positive integers 0.123456789101112131415161718192021...

#if dn represents the nth digit of the fractional part, find 
#the value of the following expression:
#d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000


i = 0
num = ''
while i <= int(1e6):
    num = num + str(i)
    i = i + 1

j = 1  
prod = 1  
while j <= int(1e6):
    prod = prod * int(num[j])
    j = j*10
    
                              
print 'Answer is:', prod

