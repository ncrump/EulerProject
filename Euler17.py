"""
Created on Thu Nov 1 14:41:05 2012
Euler Project, Problem 17
"""

#if the numbers 1 to 5 are written out in words, there are 19 letters used total.
#if all the numbers from 1 to 1000 inclusive were written out in words,
#how many letters would be used?

#NOTE: Don't count spaces or hyphens.
#and numbers like 342 are counted as three hundred and forty two

s = ['zero','one','two','three','four','five','six','seven','eight','nine']
d = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
dd = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

count = 0
sd = s + d

#gets letters in words from 1 to 19
for i in range(1,len(sd)):    #start at 1 to avoid hitting 'zero'
    word = sd[i]
    count = count + len(word)
    print word

#gets letters in words from 20 to 99
for i in range(0,len(dd)):
    for j in range(0,len(s)):
        if j == 0:
            word = dd[i]
            count = count + len(word)
        else:
            word = dd[i] + s[j]
            count = count + len(word)
        print word

i = 0
#gets letters in words from 100 to 999
#this part in the box does the hundred one to hundred nineteen part
#-------------------------
for m in range(1,len(s)):    #start at 1 to avoid hitting 'zero'
    for n in range(0,len(sd)):
        if n == 0:
            word = s[m] + 'hundred'
            count = count + len(word)
        if n != 0:
            word = s[m] + 'hundredand' + sd[n]
            count = count + len(word)
        print word
#-------------------------
        
#this part does the hundred twenty to next hundred part 
#this is inside the previous double for loop
        if n == len(sd)-1:
            
            i = i + 1
            for j in range(0,len(dd)):
                for k in range(0,len(s)):
                    if k == 0:
                        word = s[i] + 'hundredand' + dd[j]
                        count = count + len(word)
                    if k != 0:
                        word = s[i] + 'hundredand' + dd[j] + s[k]
                        count = count + len(word)
                    print word


print "Answer is:",count + len('onethousand')