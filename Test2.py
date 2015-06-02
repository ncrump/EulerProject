#test
#test



import math

num1 = 9876543214853495809384590348349058340985823974849347123456789
num2 = 9876543214853495809384590348349058340985823974849347123456789


l = int(math.log10(num1))+1
numf, poo = divmod(num1, 10**(l-9))

lst1 = []
lst2 = []

for i in range(9,0,-1):
    numf, rem1 = divmod(numf,10)
    lst1.append(rem1)
    
    num2, rem2 = divmod(num2,10)
    lst2.append(rem2)
    
    print num1, rem1
