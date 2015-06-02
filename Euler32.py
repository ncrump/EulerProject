"""
Created on Fri Dec 7 14:56:05 2012
Euler Project, Problem 32
"""

#the product 7254 is unusual, as the identity 39 * 186 = 7254, 
#containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#find the sum of all products whose multiplicand/multiplier/product
#can be written as 1 through 9 pandigital.


from datetime import datetime
t1=datetime.now()

pandigs = []
tot = 0

#loop through values to multiply together 
#note: had to guess on upper bounds (trial and error)
for i in range(1,5000):  
    for j in range(1,100):  
        #get arrays with i and j digits
        si = [z for z in str(i)]
        sj = [z for z in str(j)]
        
        #check to make sure i and j don't have repeating digits
        if len(si) > len(set(si)):
            break
        if len(sj) == len(set(sj)):
            prod = i*j 
            nums = str(i) + str(j) + str(prod)
            numarray = [z for z in nums]
            
            #then check if i,j and product are 1-9 pandigital
            if '0' not in numarray and len(numarray) == len(set(numarray)) == 9:
                pandigs.append(prod)
        
#finally sum the set of pandigs
#note: must take set(pandigs) to toss out duplicates
pandigs = set(pandigs)
while pandigs:
    tot = tot + pandigs.pop()
    
print 'Answer is:', tot

t2=datetime.now()
print '\nElapsed time:', t2-t1