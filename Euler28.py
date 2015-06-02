"""
Created on Wed Nov 7 15:40:07 2012
Euler Project, Problem 28
"""

#starting with the number 1 and moving to the right in a clockwise direction as below:

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#what is the sum of the numbers on the diagonals in a 1001 by 1001 spiral matrix?


import math

center = 1
diagTR = []
diagTL = []
diagBR = []
diagBL = []

#first get numbers along top-right diagonal from center
#these are the totals of their corresponding NxN dimension matrices
for i in range(3,1002,2):
    diagTR.append(i**2)

#next get numbers along top-left diagonal from relation to TR diagonal
#these are the TR diags subtracted by the number of rows in that dimension minus one
dim = 2
for i in diagTR:
    diagTL.append(i - dim)
    dim = dim + 2

#next get numbers along bottom-right diagonal from relation to TR diagonal
#since the sqrt of each diagTR value gives the dimension of that matrix
#then each of diagBR can be found by taking the dim of the matrix - 1 and
#multiplying that by 3 (for the number of sides of the matrix), which then
#gives the number of values away that the diagBR value is from the diagTR
for i in diagTR:
    diagBR.append(i - (int(math.sqrt(i)-1))*3)

#finally get numbers along bottom-left diagonal using same method to get diagTLs
#(adding rather than subtracting this time...)
dim = 2
for i in diagBR:
    diagBL.append(i + dim)
    dim = dim + 2


#sum all elements to get the answer
print 'Answer is:',center + sum(diagTR) + sum(diagTL) + sum(diagBR) + sum(diagBL)