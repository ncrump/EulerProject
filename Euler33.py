"""
Created on Thur Dec 6 16:51:03 2012
Euler Project, Problem 33
"""

#there are exactly four non-trivial examples of a type of fraction, 
#less than one in value, and containing two digits in the numerator
#and denominator that has the suprising cancelling property:
#49/98 = 4/8 by cancelling the 9s. 

#if the product of these four fractions is given in its lowest 
#common terms, find the value of the denominator.


numers = []
denoms = []
numer = 1
denom = 1

#loop over all 2-digit numbers for numerator and denominator
for i in range(10,100):
    for j in range(10,100):
        frac = float(i)/j  #get fraction
        
        n = []
        d = []
        
        #build lists of digits in numerator and denominator
        for k in range(2):
            n.append(float(str(i)[k]))
            d.append(float(str(j)[k]))
            
        #if any of the digits is zero then ignore it
        #if not zero, then check each combination of numer with denom to see if they are equal
        if n[0] != 0 and n[1] != 0 and d[0] != 0 and d[1] != 0 and frac < 1:
            for x in range(2):
                for y in range(2):
                    #if digits are equal, then bulid new fraction with those
                    #and check if the new fraction is equal to the original 
                    if n[x] == d[y]:
                        nn = [n[z] for z in range(2) if z != x]
                        dd = [d[z] for z in range(2) if z != y]
                        newfrac = nn[0]/dd[0]
                        if frac == newfrac:
                            numers.append(nn[0])  #keep digits in numerator of new fraction
                            denoms.append(dd[0])  #keep digits in denominator of new fraction
        

#finally get the product of numers and denoms and then simplify
for i in range(len(numers)):
    numer = numer * numers[i]
    denom = denom * denoms[i]

print 'Answer is:', denom/numer


