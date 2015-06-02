"""
Created on Thu Nov 8 19:14:05 2012
Euler Project, Problem 48
"""

#find the last ten digits of the series 1^1 + 2^2 + ... 1000^1000

ser = 0
for i in range(1,1001):
    ser = ser + i**i
    
ser = str(ser)
    
print 'Answer is:', ser[len(ser)-10:len(ser)]
    