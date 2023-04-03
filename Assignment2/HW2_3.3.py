"""
Problem 3.3
"""
import math
r = 6371.01
#Set the location first
x1 = 33.7489954
y1 = -84.3879824
x2 = 28.5383355
y2 = -81.3792365
x3 = 32.0835407
y3 = -81.0998342
x4 = 35.2270869
y4 = -80.8431267

# We need to find the distance for vevry city first, then area.

#Find dictance
def distance(x1,y1,x2,y2):
     d = r * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1 - y2)))
     return d
 
#Find area
def area(side1,side2,side3):
    s = (side1 + side2 + side3)/2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

#Sun the two triangles for these city
def city(x1,y1,x2,y2,x3,y3,x4,y4):
    
    #Use function to find distance of each city for the triangle 1
    side1 = distance(x1,y1,x2,y2)
    side2 = distance(x2,y2,x3,y3)
    side3 = distance(x3,y3,x1,y1)
    
    #Use function to find distance of each city for the triangle 2
    
    side4 = side3
    side5 = distance(x3,y3,x4,y4)
    side6 = distance(x4,y4,x1,y1)
    
    #Find area of triangle use the area function
    area1 = area(side1,side2,side3)
    area2 = area(side4,side5,side6)
    #Sum it 
    sum = area1+area2
    
    return sum


#Print it
sum = city(x1,y1,x2,y2,x3,y3,x4,y4)
print("The area is " + str(round(sum,2)) + " square kilmoeters")


