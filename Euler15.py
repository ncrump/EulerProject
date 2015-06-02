# -*- coding: cp1252 -*-
"""
Created on Thu Nov 1 11:57:05 2012
Euler Project, Problem 15
"""

#starting in the top left corner of a 2×2 grid, there are 6 routes
#without backtracking) to the bottom right corner.

#how many routes are there through a 20×20 grid?

#create 20x20 grid of zeroes
grid = [[0 for x in range(41)] for x in range(41)]

#method used is to visualize the grid and label each node with the number
#of possible routes that can be taken from that node.
#It turns out that if you start at the bottom right and work your way
#up to the top left (node by node), the number of routes possible at
#each node is the sum of the routes possible from the two adjacent nodes,
#and this relationship is Pascal's Triangle.

#the code below represents the grid by a matrix where each element
#represents the number of routes possible for that node.

#Note: this draws a flipped grid (from bottom left to top right)
#in order to sequence through points.
for i in range(0,41):
    for j in range(0,41):
       
        if i == 0 or j == 0:
            grid[i][j] = 1
        if i == 0 and j == 0:
            grid[i][j] = 0
        if i != 0 and j != 0:
            grid[i][j] = grid[i-1][j] + grid[i][j-1]


for i in range(0,41):
    print grid[i]