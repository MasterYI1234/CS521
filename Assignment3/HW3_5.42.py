"""
cs521
5.42
"""
import random

num = 1000000

#Count odd time from 0

numodd = 0

#start count

for dart in range(num):
    x,y = -1 + 2*random.random(), -1 + 2*random.random()
    if x<0:
        numodd += 1
    elif x>0 and 0<y<-x+1:
        numodd += 1
    
#caculate the probability

p = numodd / num

#Print the output
print('The probability of hitting an oddnumbered region is', format(p,'0.2%'))

