# -*- coding: utf-8 -*-
"""
question 4.21
"""
#Get the year, month, day from the user's input first

year = eval(input("Enter year: (e.g., 2008): "))
month = eval(input("Enter month: 1-12: "))
day = eval(input("Enter the day of the month: 1-31: "))


if month == 1 or month == 2:
    month = month + 12
    year = year - 1
    
#calculate century and remainding years
century = year // 100
r = year % 100


#Use Zeller to find day

d = (day + (((26 * (month + 1)) / 10) // 1) + r + ((r / 4) // 1) + ((century / 4) // 1) + (5 * century)) % 7

#Check the day of a week and print it
if d == 0:
    print("Day of the week is Saturday")
if d == 1:
    print("Day of the week is Sunday")
if d == 2:
    print("Day of the week is Monday")
if d == 3:
    print("Day of the week is Tuesday")
if d == 4:
    print("Day of the week is Wednesday")
if d == 5:
    print("Day of the week is Thursday")
if d == 6:
    print("Day of the week is Friday")
