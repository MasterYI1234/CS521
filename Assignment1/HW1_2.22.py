year = eval(input("Enter the number of years: "))

averageSec = 1/7 - 1/13 + 1/45

averageyear = averageSec * 60 * 60 * 24 * 365

grow = round(averageyear * year)

num = grow + 312032486

print("The population in ", year, "is", num)