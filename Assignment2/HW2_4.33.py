"""
question 4.33
"""
#Get the user's input integer between 0 and 15
a = eval(input("Enter a decimal value (0 to 15): "))

#make a letter dict for the number between 10 to 15
letter = {10: 'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

#Check the value is well
if a > 15 or a < 0:
    print("Invalid input")
#If the number is well, get the hex and print it
elif a < 10:
    print("The hex value is", a)
else:
    print("The hex value is", letter[a])
