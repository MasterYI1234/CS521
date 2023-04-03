"""
CS521
SiCheng Yi
"""

class Account:
    
    #A constructor that creates an account with the specified id (default 0), initial
    #balance (default 100), and annual interest rate (default 0).
    def __init__(self,id=0,balance=100,annualIntersetRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualIntersetRate = annualIntersetRate

    #A private int data field named id for the account.
    def getId(self):
        return self.__id

    #A private float data field named balance for the account.
    def getBalance(self):
        return self.__balance

    #A private float data field named annualInterestRate that stores the currentinterest rate.
    def getAnnualIntersetRate(self):
        return self.__annualIntersetRate

    #The accessor and mutator methods for id.
    def setId(self,id):
        self.__id = id

    #The accessor and mutator methods for balance.
    def setBalance(self,balance):
        self.__balance = balance

    #The accessor and mutator methods for annualInterestRate.
    def setAnnualIntersetRate(self,annualIntersetRate):
        self.__annualIntersetRate = annualIntersetRate

    #A method named getMonthlyInterestRate() that returns the monthlyinterest rate.
    def getMonthlyInterestRate(self):
        return self.__annualIntersetRate/ 12

    #A method named getMonthlyInterest() that returns the monthly interest.
    def getMonthlyInterest(self):
        return self.getBalance() *self.getMonthlyInterestRate()

    #A method named withdraw that withdraws a specified amount from the account.
    def deposit(self,balance):
        self.__balance += balance

    #A method named deposit that deposits a specified amount to the account.
    def withdraw(self,amount):
        self.__balance -= amount








#Test file
#Make a account, input value.
Account1 = Account(1122,20000,0.045)


#use the withdraw in class to withdraw money.
Account1.withdraw(2500)

#Get the account detail and print.
accountid = Account1.getId()
balance = Account1.getBalance()
mirmonthlyrate = Account1.getMonthlyInterestRate() 
monthlyinterest = Account1.getMonthlyInterest()
print("Account ID:", accountid, "\nBalance:", balance,"\nMonthly Interest Rate:", mirmonthlyrate, "\nMonthly Interest:", monthlyinterest,"\n")


#Use the deposit in class to depost money.
Account1.deposit(3000)

#Get the account detail and print.
accountid = Account1.getId()
balance = Account1.getBalance()
mirmonthlyrate = Account1.getMonthlyInterestRate() 
monthlyinterest = Account1.getMonthlyInterest()
print("Account ID:", accountid, "\nBalance:", balance,"\nMonthly Interest Rate:", mirmonthlyrate, "\nMonthly Interest:", monthlyinterest)




