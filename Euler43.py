"""
Created on Mon Dec 3 15:54:59 2012
Euler Project, Problem 43
"""

#let dn be the digit of a 0-9 pandigital number. 
#in this way we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17

#find the sum of all 0-9 pandigital numbers with this property


from datetime import datetime
t1=datetime.now()

import itertools
import math

#get all 0-9 pandigital numbers by permutation
pandigs = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

check = [2,3,5,7,11,13,17]

indx1 = []
lst1 = []
p = 1

#want to look at digits 2-4 first so that leaves 10-4=6 digits that can be permuted
#the number of permutations of a sequence of n numbers is n-factorial
#so I can look through pandigs at increments of 6-factorial since
#the first 4 digits will be the same until you go 6-factorial
#mehtod here is to filter out those numbers that meet the check criteria
#each time getting a smaller list to check through instead of checking through all 3-million permutations
di = math.factorial(6)   

for i in range(0,len(pandigs),di):
    pnum = pandigs[i]
    num = str(pnum[p]) + str(pnum[p+1]) + str(pnum[p+2])
    if int(num) % check[p-1] == 0:
        indx1.append(i)
        
for i in indx1:
    for j in range(0,di):
        lst1.append(pandigs[i+j])  #new list of pandigitals that meet 1st check
        
        
#now check through the new list and keep pandigitals that meet 2nd check
#note: now only 5 numbers to permute
indx2 = []
lst2 = []
p = 2
di = math.factorial(5)

for i in range(0,len(lst1),di):
    pnum = lst1[i]
    num = str(pnum[p]) + str(pnum[p+1]) + str(pnum[p+2])
    if int(num) % check[p-1] == 0:
        indx2.append(i)
        
for i in indx2:
    for j in range(0,di):
        lst2.append(lst1[i+j])  #new list of pandigitals that meet 2nd check
        

#now check through the new list and keep pandigitals that meet 3nd check
#note: now only 4 numbers to permute
indx3 = []
lst3 = []
p = 3
di = math.factorial(4)

for i in range(0,len(lst2),di):
    pnum = lst2[i]
    num = str(pnum[p]) + str(pnum[p+1]) + str(pnum[p+2])
    if int(num) % check[p-1] == 0:
        indx3.append(i)
        
for i in indx3:
    for j in range(0,di):
        lst3.append(lst2[i+j])  #new list of pandigitals that meet 3rd check
        

#now check through the new list and keep pandigitals that meet 4nd check
#note: now only 4 numbers to permute
indx4 = []
lst4 = []
p = 4
di = math.factorial(3)

for i in range(0,len(lst3),di):
    pnum = lst3[i]
    num = str(pnum[p]) + str(pnum[p+1]) + str(pnum[p+2])
    if int(num) % check[p-1] == 0:
        indx4.append(i)
        
for i in indx4:
    for j in range(0,di):
        lst4.append(lst3[i+j])  #new list of pandigitals that meet 4th check
     
     
#now check through the new list and keep pandigitals that meet 5nd check
#note: now only 2 numbers to permute
indx5 = []
lst5 = []
p = 5
di = math.factorial(2)

for i in range(0,len(lst4),di):
    pnum = lst4[i]
    num = str(pnum[p]) + str(pnum[p+1]) + str(pnum[p+2])
    if int(num) % check[p-1] == 0:
        indx5.append(i)
        
for i in indx5:
    for j in range(0,di):
        lst5.append(lst4[i+j])  #new list of pandigitals that meet 5th check
        
       
#with the list of possible pandigitals narrowed down, finish the final 2 checks
tot = 0
p = 6

for i in lst5:
    pnum = i
    strnum = ''
    num1 = str(pnum[p]) + str(pnum[p+1]) + str(pnum[p+2])
    num2 = str(pnum[p+1]) + str(pnum[p+2]) + str(pnum[p+3])
    
    if int(num1) % check[p-1] == 0 and int(num2) % check[p] == 0:
       
        for j in pnum:
            strnum = strnum + str(j)
        
        tot = tot + int(strnum)
            
                
print 'Answer is:', tot        
    
t2=datetime.now()
print '\nElapsed time:', t2-t1
