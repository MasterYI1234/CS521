rate = 0.00417

growthrate = 1 + rate

saving = eval(input("Enter your monthly saving amount:"))

amount = saving * growthrate**6 + saving * growthrate**5 + saving * growthrate**4 + saving * growthrate**3 + saving * growthrate**2 + saving * growthrate**1

print("The six month account value is :", amount)
