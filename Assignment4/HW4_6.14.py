"""
CS521
SiCheng Yi
"""

def m(i):
    # Check i is not 0.
    if i == 0:
        return 0

    # Write formulas to calculate
    return (4*pow(-1, i+1)/(2*i - 1)) + m(i-1)

# Test the m(i) function and displays the table format
def main():
    #Print the first and second line.
    print("{}\t{}".format("i", "m(i)"))
    print("--------------")
    #set the number to the table
    for i in range(1, 1000, 100):
        print("{}\t{:.4f}".format(i, m(i)))


main()