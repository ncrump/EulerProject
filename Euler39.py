"""
Created on Fri Dec 14 11:07:59 2012
Euler Project, Problem 39
"""

#if p is the perimeter of a right triangle with integral length sides
#{a,b,c}, there are exactly three solutions for p = 120: {20,48,52}, {24,45,51}, {30,40,50}

#for which value of p <= 1000, is the number of solutions maximized?

import math

from datetime import datetime
t1=datetime.now()

maxp = 0

#for each p (perimeter) value, can assign an i side length and j side length
#then for each i and j side lengths, get the hypotenuse based on the condition that it's a right triangle
#then simply check if the sum of these sides generated in the loop are equal to perimeter value p

for p in range(4,1001):  #iterate over possible perimeter values
    count = 0
    
    for i in range(1,p-2): #generate side length i         
            for j in range(1,i):  #generate side length j
                h = math.sqrt(i**2 + j**2)  #get hypotenuse then check if equal to perimeter value p
                perim = i+j+h
                if perim == p:
                    count = count + 1
                    break
                elif perim > p:
                    break               
                
    if count > maxp:
        maxp = count
        winner = p
                                
print 'Answer is:', winner
    
t2=datetime.now()
print '\nElapsed time:', t2-t1
