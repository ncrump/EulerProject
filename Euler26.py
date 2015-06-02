"""
Created on Wed Nov 21 09:25:22 2012
Euler Project, Problem 26
"""

#a unit fraction contains 1 in the numerator.
#find the denominator d < 1000 for which 1/d contains the longest 
#recurring cycle in its decimal fraction part.

from datetime import datetime
t1=datetime.now()

#import decimal module to get any decimal precision without rounding
#NOTE: using float slightly round a large decimal and gives incorrect precision
from decimal import Decimal, getcontext
getcontext().prec = 2000  #specified number of exact digit precision

len0 = []
winner = []

#generate fraction and turn into 2,000 digit precision string
for i in range(2,1000):
    print i
    n = str(Decimal(1) / Decimal(i))  #gets decimal value to high precision
    n = n.split('.')  #split off into integer
    n = n[1]
    
    #loop through consecutive digits until the starting value repeats
    for j in range(0,len(n)-1):
        val = n[j]
        for k in range(j+1, len(n)-1):
            
            if k == j+1 and n[k] == val:
                 break
            
            #build the sequence out of digits between starting value and repeated value
            if k != j+1 and n[k] == val:
                seq1 = n[j : k]
                seq2 = n[k : k+k-j]

                #check if those consecutive digits are a sequence
                #if so, store length of sequence and denom value to array
                #NOTE: checking for longest length doesn't seem to work so had to do it this way...
                if seq1 == seq2:
                    len0.append(len(seq1))
                    winner.append(i)
                    break
                

#get position of longest sequence in array                
pos = len0.index(max(len0)) 
                              
print 'Answer is:', winner[pos]

t2=datetime.now()
print '\nElapsed time:', t2-t1
