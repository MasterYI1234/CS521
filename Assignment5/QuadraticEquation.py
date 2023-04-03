"""
CS521
SiCheng Yi
"""

import math



class QuadraticEquation:
    #The private data fields a, b, and c that represent three coefficients.
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        
    #Get methods for a.
    def getA(self):
        return self.__a
    
    #Get methods for b.
    def getB(self):
        return self.__b
    
    #Get methods for c.
    def getC(self):
        return self.__c
    
    # A method named getDiscriminant() that returns the discriminant, which is b^2 - 4ac.
    def getDiscriminant(self):
        return self.getB() * self.getB() - 4 * self.getA() * self.getC()
    
    #Roots of the equation1
    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.getB() + math.sqrt(self.getDiscriminant())) / (2 * self.getA())
        
    #Roots of the equation2
    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.getB() - math.sqrt(self.getDiscriminant())) / (2 * self.getA())

