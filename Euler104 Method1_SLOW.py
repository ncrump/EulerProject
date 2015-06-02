"""
Created on Fri Nov 2 14:40:19 2012
Euler Project, Problem 104
"""

#find the first Fibonacci term for which the first nine digits AND the last
#nine digits are 1-9 pandigital (contain all digits from 1-9 in any order)

#!!takes WAY too long - no answer after 3 hrs!

from datetime import datetime
t1=datetime.now()

print '\nRunning...' 

#start with 2nd and 3rd terms in sequence (1 is also 1st term)
f1 = 1   
f2 = 2
term = 3

off = 0

while off == 0:
    #create check lists for first and last 9 digits
    c1 = ['1','2','3','4','5','6','7','8','9']
    c2 = ['1','2','3','4','5','6','7','8','9']

    #create empty arrays to write matches to
    #(and clear them on each new iteration)
    nums1 = []
    nums2 = []

    #get Fibonacci number and term
    fib = str(f1 + f2)
    term = term + 1
       
    if len(fib) <= 18:
        f1 = f2
        f2 = int(fib)
       
    else:
        fib1 = fib[0:9]                    #get first 9 digits of Fib number
        fib2 = fib[len(fib)-9:len(fib)]    #get last 9 digits of Fib number         
        
        #check first 9 digits of Fib number
        for i in range(0,9):
            if fib1[i] == '0':  #break out if digit is zero
                break
           
            else:
                #check against values of c1
                for j in range(0,9):
                    if fib1[i] == c1[j]:
                        c1[j] = '0'  #set match in check list to zero to avoid duplicating
                        nums1.append(fib1[i])
                       
        if len(nums1) == 9:
            #check last 9 digits of Fib number
            for i in range(0,9):  
                if fib2[i] == '0':  #break out if digit is zero
                    break
               
                else:
                    #check against values of c2
                    for j in range(0,9):
                        if fib2[i] == c2[j]: 
                            c2[j] = '0'  #set match in check list to zero to avoid duplicating
                            nums2.append(fib2[i])
                            
        #if all matches found then num arrays will have 9 values each
        if len(nums1) == 9 and len(nums2) == 9:
            off = 1

        else:
            #print term
            f1 = f2
            f2 = int(fib)
       

print 'Answer is:', term

t2=datetime.now()
print '\nElapsed time:', t2-t1