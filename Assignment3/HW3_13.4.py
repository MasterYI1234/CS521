"""
cs521
13.4
"""
import os
import random
import sys

#Ask to input the file name
filename = input("Enter a filename: ").strip()

#Check the file name is well
if os.path.isfile(filename):
    print("The file already exists")
    sys.exit()

#Open the file and write 100 integer in it
file = open(filename, 'w')

for i in range(100):
    file.write(str(random.randint(0, 100)) + " ")

#Close the file
file.close()

#Check the line, and read it , then out put the file
file1 = open(filename, 'r')
nums = []
for line in file1:
    nums = line.split()

nums = [eval(x) for x in nums]
nums.sort()
for n in nums:
    print(n, end=' ')
