"""
Created on Fri Dec 14 09:25:59 2012
Euler Project, Problem 31
"""

#in England the currency is made up of pound P and pence. 
#there are eight coins in general circulation:
#1p, 2p, 5p, 10p, 20p, 50p, 1P (100p) and 2P (200p).

#how many different ways can 2P be made using any number of coins?


from datetime import datetime
t1=datetime.now()

count = 1 

#approach here is not clever but works fast
#i want to look at the equation p200 = a*p100 + b*p50 + c*p20 + d*p10 + e*p5 + f*p2 + g*p1
#and iterate over a,b,c,d,e,f,g until total is equal to 200 (with a few constrains)
#including constraints such as if iterating over b for p50, don't want to go more than 4*50 since that is 200

for a in range(3):  #iterate over p100 value
    p200 = a*100 
    if p200 == 200:
        count = count + 1
        break
    elif p200 > 200:
        break
    else:
        
        for b in range(5):  #iterate over p50 value
            p200 = a*100 + b*50 
            if p200 == 200:
                count = count + 1
                break
            elif p200 > 200:
                break
            else:
                
                for c in range(11):  #iterate over p20 value
                    p200 = a*100 + b*50 + c*20
                    if p200 == 200:
                        count = count + 1
                        break
                    elif p200 > 200:
                        break
                    else:
                        
                        for d in range(21):  #iterate over p10 value
                            p200 = a*100 + b*50 + c*20 + d*10 
                            if p200 == 200:
                                count = count + 1
                                break
                            elif p200 > 200:
                                break
                            else:
                    
                                for e in range(41):  #iterate over p5 value
                                    p200 = a*100 + b*50 + c*20 + d*10 + e*5 
                                    if p200 == 200:
                                        count = count + 1
                                        break
                                    elif p200 > 200:
                                        break
                                    else:

                                        for f in range(101):  #iterate over p2 value
                                            p200 = a*100 + b*50 + c*20 + d*10 + e*5 + f*2 
                                            if p200 == 200:
                                                count = count + 1
                                                break
                                            elif p200 > 200:
                                                break
                                            else:
                            
                                                for g in range(201):  #iterate over p1 value
                                                    p200 = a*100 + b*50 + c*20 + d*10 + e*5 + f*2 + g*1
                                                    if p200 == 200:
                                                        count = count + 1
                                                        break
                                                    elif p200 > 200:
                                                        break
                                

print 'Answer is:', count
    
t2=datetime.now()
print '\nElapsed time:', t2-t1
