"""
question 3.9
"""
#Get the date from the user's enter first
name = input("Please enter the name of the employee:")
hours = eval(input("Please enter the number of the hours for the employee work in a week:"))
rate = eval(input("Please enter the hourly pay rate:"))
fed = eval(input("Please enter the federal tax withholding rate:"))
sta = eval(input("Please enter the state tax withholding rate:"))

#Calculate every data we need, we need Gross pay, fed withholding, sta withholding, total of deduction and net Pay

#Gross pay
gross = float(hours) * float(rate)

#fed wtihholding
fed_percent = float(fed) * 100
fed_withholding = float(gross) * float(fed)

#sta withholding
sta_percemt = float(sta) * 100
sta_withholding = float(gross) * float(sta)

#Total deduction
deduction = float(fed_withholding) + float(sta_withholding)

#net pay
net = float(gross) - float(deduction)

#Print all of it
print("  Employee Name: " + str(name))
print("  Hours Worked: " + str(round(hours,1)))
print("  Pay Rate: $" + str(rate))
print("  Gross Pay: $" + str(round(gross,2)))
print("  Deduction:")
print("    Federal Withholding(" + str(fed_percent) + "%): $" + str(round(fed_withholding,2)))
print("    State Withholding(" + str(sta_percemt) + "%): $"+ str(round(sta_withholding,2)))
print("    Total Deduction: $" + str(round(deduction,2)))
print("  Net Pay: $" + str(round(net,2)))


