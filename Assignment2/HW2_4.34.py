"""
question 4.34
"""
import string
#Get the input from user
a = input("Enter a hex character: ")

#Check the number is well
if not(a in string.hexdigits):
    print("Invalid input")

#if it is well, print the hex to the number
else:
    print("The decimal values is", int(a,16))
