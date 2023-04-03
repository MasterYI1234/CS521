num = int(input("Enter a four difit integer: "))

output = (num % 10)*1000
num = num // 10
output += (num % 10)*100
num = num // 10
output += (num % 10)*10
num = num // 10
output += (num % 10)
num = num // 10

print(output)