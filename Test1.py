#test
#test

from datetime import datetime
t1=datetime.now()

#generate Fibonacci sequence 

#Method 1
#------------------------------------
#fib = [1,2]
#for i in range(2,100):
#    fib.append(fib[i-1] + fib[i-2])
#------------------------------------


#Method 2
#------------------------------------
f1 = 1
f2 = 2
term = 3

while term <= 13:
    fib = f1 + f2
    term = term + 1
    print fib
    
    f1 = f2
    f2 = fib
#------------------------------------


t2=datetime.now()
print '\nElapsed time:', t2-t1