"""
Created on Fri Nov 30 16:50:22 2012
Euler Project, Problem 38
"""

#what is the largest 1 to 9 pandigital 9-digit number that can be 
#formed as the concatenated product of an integer with 
#(1,2, ... , n) where n > 1?


from datetime import datetime
t1=datetime.now()

tot = 0
i = 2

while i < 10000:  #guessing on upper bound here
    concat0 = ''
    concat = ''
    
    for j in range(1,100):  #also guessing on only going to 100
        prod = str(i*j)
        concat0 = concat0 + prod
        
        #check to make sure that zero is not in the product
        #and that there are no repeated numbers by using set
        if str(0) in prod or len(set(concat0)) < len(concat0):
            i = i + 1         
            break
        else: concat = concat + prod
        
    if len(concat) > 0 and int(concat) > tot:
        tot = int(concat)
        
        
print 'Answer is:', tot

t2=datetime.now()
print '\nElapsed time:', t2-t1
