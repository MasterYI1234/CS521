num = int(input("Enter a number between 0 and 1000: "))

totalnum = 0

while num > 0:
    totalnum += (num % 10)
    num //= 10

print("The sum of the digits is", (totalnum))
