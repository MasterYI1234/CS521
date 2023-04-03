# -*- coding: utf-8 -*-
"""
cs521
5.46
"""

import math

#Set the start count sum and squaresum
COUNT = 0
sum = 0
squareSum = 0

#Ask for input
print("Enter any numbers: ", end='')


#Make a loop which is broken by enter an 'Enter', and every time calculate the sum count and squaresum
while 1:
    n = input()
    if n == "":
       break
    else:
       sum += float(n)
       squareSum += float(n) * float(n)
       COUNT += 1
    

#Calculate the mean and dveiation

mean = sum / COUNT
dev = math.sqrt((squareSum - sum * sum / COUNT) / (COUNT - 1))

#Print the output
print("The mean is", mean)
print("The standard deviation is", dev)

