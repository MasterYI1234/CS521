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








#Test file
#Set two rectangle, and input the width and height.
rectangle1 = Rectangle(4, 40)
rectangle2 = Rectangle(3.5, 35.7)

#Use the class to get area.
area1 = rectangle1.getArea()
area2 = rectangle2.getArea()

#Use the class to get perimeter.
perimeter1 = rectangle1.getPerimeter()
perimeter2 = rectangle2.getPerimeter()


#print the result
print("Rectangle1:\n\tWidth =", rectangle1.width, "\n\tHeight =", rectangle1.height,
      "\n\tArea =", area1, "\n\tPerimeter =", perimeter1)

print("Rectangle2:\n\tWidth =", rectangle2.width, "\n\tHeight =", rectangle2.height,
      "\n\tArea =", area2, "\n\tPerimeter =", perimeter2)