min = int(input("Enter the number of minutes: "))
day = int(min / 1440)
year = int(day / 365)
day -= (365 * year)
print(str(min), "minutes is approximately", str(year), "years and", str(day),"days")

