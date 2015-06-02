"""
Created on Thu Oct 18 15:10:41 2012
Euler Project, Problem 4
"""

#largest palindrome from two 3-digit numbers

palindromes=[]
r=range(100,999)
for i in r:
    for j in r:
        num=str(i*j)
        if len(num) == 6:
            if num[0:3] == str(num[5])+str(num[4])+str(num[3]):
                palindromes.append(num)

print max(palindromes)
