"""
Created on Wed Dec 12 12:57:03 2012
Euler Project, Problem 52
"""

#it can be seen that the number 125874 and its double 251748 
#contain exactly the same digits, but in a different order.

#find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, 
#and 6x, contain the same digits.


stop = 0
n = 100000

while stop == 0:
    for i in range(2,7):
        mult = n*i
        #use sorted function to turn string into list by increasing order
        #then simply compare each list
        if sorted(str(n)) == sorted(str(mult)):
            if i == 6:
                winner = n
                stop = 1
        else:
            n = n + 1
            break
        
print 'Answer is:', winner
    