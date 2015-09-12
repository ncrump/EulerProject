# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 11:09:20 2015
Euler Project, Problem 112
"""

# we shall call a positive integer that is neither
# increasing nor decreasing a "bouncy" number; for example, 155349.

# bouncy numbers become more common and by the time we reach 21780
# the proportion of bouncy numbers is equal to 90%.

# find the least number for which the proportion of bouncy numbers is exactly 99%.

from datetime import datetime
t1=datetime.now()

prop = 0
cnt  = 0
tot  = 0
num  = 0

# count up bouncy numbers until hitting 99%
while prop < 0.99:
    num += 1
    chk  = 0
    rep  = 0
    nstr = str(num)
    nlen = len(nstr)
    # condition to check for bouncy number
    for i in range(nlen-1):
        if nstr[i+1] > nstr[i]:
            chk += 1
        elif nstr[i+1] < nstr[i]:
            chk -= 1
        else:
            rep += 1

    # count if bouncy number
    if abs(chk) != nlen-1-rep:
        cnt += 1

    # get new percentage
    tot += 1
    prop = cnt/float(tot)

print num,round(prop,2)

t2=datetime.now()
print '\nElapsed time:', t2-t1