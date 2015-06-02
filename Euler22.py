"""
Created on Sun Nov 4 08:58:19 2012
Euler Project, Problem 22
"""


#using names.txt containing over 5000 first names, sort into alphabetical order
#then work out the alphabetical value for each name
#multiply this value by its alphabetical position in the list to obtain a name score

#what is the total of all the name scores in the file?

val = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#read in names file
file = open('names_Euler22.txt')
line = file.readline()
file.close()

#split names by commas into array
names = line.split(',')

#remove quotes from each name
for i in range(0,len(names)):
    names[i] = names[i].strip(' " ')
    
#sort alphabetically 
names = sorted(names)

tot = 0

for i in range(0,len(names)):  #runs through each name in list
    n = names[i]
    pos = i+1  #gets position of name in sorted list
    sum0 = 0
    for j in range(0,len(n)):        #gets each letter in name
        for k in range(0,len(val)):  #checks letter to alphabet in val
            if n[j] == val[k]:       #gets alphabet position for letter in name
                sum0 = sum0 + k+1    #gets sum of all letter numbers
                
    tot = tot + (pos*sum0)

print 'Answer is:', tot       
        
        

    

