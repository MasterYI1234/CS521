"""
CS521
SiCheng Yi
"""

class LinearEquation:
    #The private data fields a, b, c, d, e, and f with get methods.
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
    #Get methods for a.
    def getA(self):
        return self.__a

    #Get methods for b.
    def getB(self):
        return self.__b

    #Get methods for c.
    def getC(self):
        return self.__c

    #Get methods for d.
    def getD(self):
        return self.__d

    #Get methods for e.
    def getE(self):
        return self.__e

    #Get methods for f.
    def getF(self):
        return self.__f

    #A method named isSolvable() that returns true if is not 0.
    def isSolvable(self):
        denominator = self.__a * self.__d - self.__b * self.__c
        return True if denominator != 0 else False

    #Return the solution x for the equation.
    def getX(self):
        denominator = self.__a * self.__d - self.__b * self.__c
        numerator = self.__e * self.__d - self.__b * self.__f
        return numerator / denominator

    #Return the solution y for the equation.
    def getY(self):
        denominator = self.__a * self.__d - self.__b * self.__c
        numerator = self.__a * self.__f - self.__e * self.__c
        return numerator / denominator





#Test file
#Ask the input from user.
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))
d = eval(input("Enter d: "))
e = eval(input("Enter e: "))
f = eval(input("Enter f: "))

#Make the class.
equation = LinearEquation(a, b, c, d, e, f)

#Print output.
if (equation.isSolvable()):
    print("X:", equation.getX(), "\tY:", equation.getY())
else:
    print("The equation has no solution")