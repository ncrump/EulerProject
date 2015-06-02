"""
Created on Fri Nov 16 23:21:20 2012
Euler Project, Problem 56
"""

#considering natural numbers of the form, a^b, where a and b < 100
#what is the maximum digital sum?

tot = 0
for i in range(2,100):
    for j in range(2,100):
        sum0 = 0
        num = i**j
        for k in str(num):
            sum0 = sum0 + int(k)
        
        if sum0 > tot:
            tot = sum0

print 'Answer is:', tot