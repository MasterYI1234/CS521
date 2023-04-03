"""
CS521
SiCheng Yi
"""

#Design a class named Location for locating a maximalvalue and its location in a two-dimensional list. 
class Location:
    #Make a row, column, maxValue
    row = None
    column = None
    maxValue = None
    
    def __init__(self,row,column,maxValue)->None:
        self.row = row
        self.column = column
        self.maxValue = maxValue
    
    #The final output for largest number of maxvalue, row, col.
    def __str__(self) -> str:
        return "The location of the largest element is {:d} at ({:d},{:d})".format(self.maxValue,self.row,self.column)


def locateLargest(a):
    
    #Make a location
    maxVal = Location(0,0,a[0][0])
    
    #Check the element one by one and find the largest.
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] > maxVal.maxValue:
                maxVal = Location(row,col,a[row][col])
    return maxVal





#Test code
def main():
    #Ask the input for number of row and col, like enter：2 4 
    ele = input("Please enter the number of rows and columns for list, enter it interval by space: ").split()
    rows,cols = (int(ele[0]),int(ele[1]))
    array = []
    
    
    #Ask for input the element of row, like: 3 6 3 1
    for i in range(rows):
        row = input("Please enter the row %d, enter it interval by space: " % i).split()
        introw = [int(val) for val in row]
        
        #If the element of enter not the same as input col, output the error.
        if len(introw) != cols:
            raise RuntimeError("Incorrect number for enters!")
        
        #Put it in the array.
        array.append(introw)
    #Use the class   
    locatelargest = locateLargest(array)
    print(locatelargest)
main()
