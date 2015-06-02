"""
Created on Thu Oct 18 13:42:19 2012
Euler Project, Problem 2
"""

#generate Fibonacci sequence up to values lower than 4 million
fib=[1,2]
for i in range(2,100):
    fib.append(fib[i-1]+fib[i-2])
    if fib[i] >= 4e6:
        print i, fib[i]
        break  

#get only even values of sequence and sum together
even=[]
for i in fib:
    if i % 2 == 0:
        even.append(i)

print sum(even)
