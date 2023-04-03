"""
question 4.28
"""
#Get the four point of each from user's enter
x1,y1,w1,h1 = eval(input("Enter r1's center x-, y-coordintaes, width, and height: "))
x2,y2,w2,h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

#Check one r is inside another r
if((x1 + w1) < (x2 + w2)) and ((x1 - w1) > (x2 - w2)) and ((y1 + h1) < (y2 + h2)) and ((y1 - h1) > (y2 - h2)):
    print("r1 is inside r2")
elif((x1 + w1) > (x2 + w2)) and ((x1 - w1) < (x2 - w2)) and ((y1 + h1) > (y2 + h2)) and ((y1 - h1) < (y2 - h2)):
    print("r2 is inside r1")    
#Check the overlaps of r1 and r2
elif(((x1 + w1) < (x2 + w2)) and ((x1 + w1) > (x2 - w2))):
    print("r2 overlaps r1")
elif(((x1 + w1) > (x2 + w2)) and ((x1 + w1) < (x2 - w2))):
    print("r2 overlaps r1")
elif(((y1 + h1) < (y2 + h2)) and ((y1 + h1) > (y2 - h2))):
    print("r2 overlaps r1")
elif(((y1 + h1) > (y2 + h2)) and ((y1 + h1) < (y2 - h2))):
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")


