"""
Created on Tue Dec 11 14:30:03 2012
Euler Project, Problem 67
"""

#find the maximum total starting at the top of the triangle and moving 
#to adjacent numbers on the row below in the file triangle.txt.

#this problem is similar to Euler Problem 18 but now the triangle 
#text file contains 100 rows. 


#create grid in which to write rows of triangle to
map0 = [[0 for i in range(100)] for i in range(100)]

#read in triangle values from file and bulid triangle array by placing each value into array
file = open('triangle_Euler67.txt')
line = file.readlines()
for i in range(len(line)):
    vals = line[i].split(' ')
    for j in range(len(vals)):
        map0[i][j] = int(vals[j])
file.close()


#start from bottom of triangle and work up by going through each element of triangle
#and adding the larger number to that element that appears in the adjacent position below
#by doing this and working up the triangle, the value at the peak of the triangle will be the maximum sum
for i in range(98,-1,-1): 
    for j in range(0,i+1):
        
        if map0[i+1][j] > map0[i+1][j+1]:
            map0[i][j] = map0[i][j] + map0[i+1][j]
        elif map0[i+1][j] <= map0[i+1][j+1]:
            map0[i][j] = map0[i][j] + map0[i+1][j+1]
        if map0[i+1][j] == map0[i+1][j+1]:
            print 'PROBLEM...values equal'  #had many cases where values were equal, but adding >= condition to elif statement got correct answer
                                           
print 'Answer is:', map0[0][0] 