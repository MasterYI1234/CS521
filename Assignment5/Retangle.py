"""
CS521
SiCheng Yi
"""

class Rectangle:
    #Set width and height, just set the default is 1 and 2.
    def __init__(self,width = 1,height = 2):
        self.width = width
        self.height = height
        
    #The area of a rectangle is width * height.
    def getArea(self):
        return self.width * self.height

    #The perimeter of the rectangle is width + height then * 2.
    def getPerimeter(self):
        return (self.height+self.width)*2
    




