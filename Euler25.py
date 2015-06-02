"""
Created on Fri Nov 2 11:36:19 2012
Euler Project, Problem 25
"""

#first term in the Fibonacci sequence to contain 1000 digits


#start with 2nd and 3rd terms in sequence (1 is also 1st term)
f1 = 1   
f2 = 2
term = 3
len0 = 0

while len0 < 1000:
    fib = f1 + f2
    term = term + 1
    len0 = len(str(fib))
    f1 = f2
    f2 = fib

print 'Answer is:',term