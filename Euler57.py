# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:32:50 2015
Euler Project, Problem 57
"""

#it is possible to show that the square root of two
#can be expressed as an infinite continued fraction:
#sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

#in the first one-thousand expansions,
#how many fractions contain a numerator with more digits than denominator?

# sqrt(2) can be approximated by generating a ratio of Pell numbers
count = 0
d0 = 0
d1 = 1
# loop to generate sequence
for i in range(1000):
    # generate Pell numbers as the sequence in denominator
    # generate sequence in numerator from denominator
    denom = 2*d1 + d0
    numer = denom + d1
    d0 = d1
    d1 = denom
    if len(str(numer)) > len(str(denom)):
        count += 1

print count