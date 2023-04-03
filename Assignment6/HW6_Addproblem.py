"""
CS521
SiCheng Yi
"""



#Make the raise class.
class Negative(Exception):

   def __init__(self, message="Value Can not be negative."):
       self.message = message
       super().__init__(self.message)





class Account:
    
    #A constructor that creates an account with the specified id (default 0), initial
    #balance (default 100), and annual interest rate (default 0).
    def __init__(self,id=0,balance=100,annualIntersetRate=0):
        self.__id = id
        self.__balance = balance
        #Check the value to output the raise.
        if annualIntersetRate < 0:
            raise Negative("Annual can not less than 0.")
        else:
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
        #Check the value to output the raise.
        if balance < 0:
            raise Negative("Deposit can not less than 0.")
        else:
            self.__balance -= balance

    #A method named deposit that deposits a specified amount to the account.
    def withdraw(self,amount):
        #Check the value to output the raise.
        if amount < 0:
            raise Negative("Withdraw can not less than 0.")
        else:
            self.__balance -= amount
        
        
        
        
        
        
        
def main():
    #Use the class to make the accounts.
    accounts = []
    for i in range(10):
        ac = Account(i)
        accounts.append(ac)
        
    #Ask for input an id.
    id = eval(input("Enter an account id(between 0-9): "))

    #Make a forever loop
    while (True):
        #If id is right, print the menu.
        if 0 <= id <= 9:
            print("Main menu")
            print("1: check balance\n2: withdraw\n3: deposit\n4: exit")

            #Make different user choose to do different things.
            choice = int(input(""))
            if choice == 1:
                print("The balance is", accounts[id].getBalance(),"\n")
            elif choice == 2:
                amount = eval(input("Enter an amount to withdraw: \n"))
                accounts[id].withdraw(amount)
            elif choice == 3:
                amount = eval(input("Enter an amount to deposit: \n"))
                accounts[id].deposit(amount)
            #If choose 4 to exit, it will ask a new id, to loop it forever.
            elif choice == 4:
                id = eval(input("Enter an account id(between 0-9): "))
            #if not enter a right choose, reask a new choose.
            else:
                print("Enter the correct choose(between 1-4)")
        #If id is wrong, ask to reenter an id.
        else:
            id = eval(input("Enter an account correct id(between 0-9): "))

main()
