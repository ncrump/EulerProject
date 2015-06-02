"""
Created on Thu Nov 8 19:26:05 2012
Euler Project, Problem 30
"""

#surprisingly there are only three numbers that can be written as the sum 
#of fourth powers of their digits:

#1634 = 14^4 + 64^4 + 34^4 + 44^4
#8208 = 84^4 + 24^4 + 04^4 + 84^4
#9474 = 94^4 + 44^4 + 74^4 + 44^4

#find the sum of all the numbers that can be written as the sum of 
#fifth powers of their digits


count = 0
tot = 0
i = 11

while count < 6:    #had to run it through once to figure out there are only 6
    sum0 = 0
    si = str(i)
    len0 = len(si)
    for j in range(0,len0):
        sum0 = sum0 + int(si[j])**5
    
    if sum0 == i:
        count = count + 1
        tot = tot + sum0
        print i
        i = i + 1
    else:
        i = i + 1
        
print 'Answer is:', tot
    