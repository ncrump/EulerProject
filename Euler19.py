"""
Created on Fri Nov 16 12:49:05 2012
Euler Project, Problem 19
"""

#1 Jan 1900 was a Monday.
#thirty days has September,April, June and November.
#all the rest have thirty-one, saving February alone, which has twenty-eight.
#and on leap years, twenty-nine.
#a leap year occurs on any year evenly divisible by 4 
#but not on a century unless it is divisible by 400.

#how many Sundays fell on the first of the month during the 
#twentieth century (1 Jan 1901 to 31 Dec 2000)?


month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

sundate = 7  #7 Jan 1900 - first sunday of month 
suncount = 0

#loop through year and check for leap year
for i in range(1900,2001):
    if i % 4 == 0 and i != 1900:
        leap = 'yes'
    else: leap = 'no'
            
    #loop through month and check for number of days in that month
    for j in range(0,12):
        if month[j] == 'feb':
            if leap == 'yes':
                dy = 29
            else: dy = 28
                
        elif month[j] == 'apr' or month[j] == 'jun' or month[j] == 'sep' or month[j] == 'nov':
            dy = 30
            
        else: dy = 31
        
        #need to add 28 days to get to sunday of next month if number of days in the month is less than 28
        #but add 35 days if number of days in the month is greater than 28
        if sundate + 28 <= dy:
            sundate = sundate + 35
        else: sundate = sundate + 28
        
        #then find the date of the sunday in the new month by taking the difference
        sundate = sundate - dy
        
        #count if sunday of new month is on the first
        if i >= 1901:
            if sundate == 1:
                suncount = suncount + 1
        
       
print 'Answer is:', suncount

    