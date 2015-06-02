"""
Created on Thu Oct 18 16:16:44 2012
Euler Project, Problem 5
"""

#smallest number evenly divisible by all numbers from 1 to 20

from datetime import datetime
t1=datetime.now()

#takes about 6.5 minutes... 
off=0
i=2

while off == 0:
    rems = [j for j in range(1,21) if i % j == 0]
    if len(rems) == 20:
        print 'answer is:', i
        off = 1

    else:
        #print i
        i=i+2    #assuming i has to be even number
        rems=0
       
t2=datetime.now()
print '\nElapsed time:', t2-t1