"""
Created on Thur Nov 1 21:14:03 2012
Euler Project, Problem 18
"""

#find the maximum total starting at the top of the triangle and moving 
#to adjacent numbers on the row below

#import pprint

tri = '\
75,\
95 64,\
17 47 82,\
18 35 87 10,\
20 04 82 47 65,\
19 01 23 75 03 34,\
88 02 77 73 07 63 67,\
99 65 04 28 06 16 70 92,\
41 41 26 56 83 40 80 70 33,\
41 48 72 33 47 32 37 16 94 29,\
53 71 44 65 25 43 91 52 97 51 14,\
70 11 33 28 77 73 17 78 39 68 17 57,\
91 71 52 38 17 14 91 43 58 50 27 29 48,\
63 66 04 68 89 53 67 30 73 16 69 87 40 31,\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

#create grid in which to write rows of triangle to
map0 = [[0 for i in range(15)] for i in range(15)]

#split out commas
s = tri.split(',')
map0[0][0] = int(s[0])

#build triangle array by placing values into array
for i in range(1,len(s)):
    r0 = s[i].split()
    for j in range(0,len(r0)):
        map0[i][j] = int(r0[j])
        
#pprint.pprint(map0)

#start from bottom of triangle and work up by going through each element of triangle
#and adding the larger number to that element that appears in the adjacent position below
#by doing this and working up the triangle, the value at the peak of the triangle will be the maximum sum
for i in range(13,-1,-1): 
    for j in range(0,i+1):
        
        if map0[i+1][j] > map0[i+1][j+1]:
            map0[i][j] = map0[i][j] + map0[i+1][j]
        elif map0[i+1][j] < map0[i+1][j+1]:
            map0[i][j] = map0[i][j] + map0[i+1][j+1]
        if map0[i+1][j] == map0[i+1][j+1]:
            print 'PROBLEM...values equal'  #luckily no problem with values being equal here
                                           
print 'Answer is:', map0[0][0] 