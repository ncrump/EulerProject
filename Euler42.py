"""
Created on Thu Nov 8 16:28:05 2012
Euler Project, Problem 42
"""

#using words.txt containing nearly 2000 common English words, convert each
#letter in a word to a number corresponding to its alphabetical position and
#adding these values we form a word value. If the word value is a triangle
#number then we call the word a triangle word.

#how many are triangle words?


val = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#read in words file
file = open('words_Euler42.txt')
line = file.readline()
file.close()

#split words by commas into array
words = line.split(',')

#remove quotes from each word
for i in range(0,len(words)):
    words[i] = words[i].strip(' " ')
   
#sort alphabetically
words = sorted(words)

#get word value of each word in list and store to array
wordval = []

for i in range(0,len(words)):       
    n = words[i]
    sum0 = 0
    for j in range(0,len(n)):        #gets each letter in word
        for k in range(0,len(val)):  #checks letter to alphabet in val
            if n[j] == val[k]:       #gets alphabet position for letter in word
                sum0 = sum0 + k+1    #gets sum of all letter numbers
                break
    wordval.append(sum0)


#generate list of triangle numbers and compare to wordval list
wordval = sorted(wordval)

#generate trinum list
i = 1
tri = 1
trinums = [1]

while tri <= max(wordval):
    i = i + 1
    tri = tri + i
    trinums.append(tri)

#get all wordvals that are in trinums
tot = len([j for j in wordval if j in trinums])

print 'Answer is:',tot