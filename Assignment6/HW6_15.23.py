"""
CS521
SiCheng Yi
"""

#Invokes displayPermuationHelper("", s). 
def displayPermuation(s):
    displayPermuationHelper("", s)


#Uses a loop to move a character from s2 to s1 and recursively invokes it with a new s1 and s2.
def displayPermuationHelper(s1, s2):
    if s2 == '':
        print(s1)
    else:
        for i in range(len(s2)):
            displayPermuationHelper(s1 + s2[i], s2[0:i] + s2[i + 1:len(s2)])


#Test code
def main():
    #Just ask a string,like:abc
    displayPermuation(input("Enter a string: "))
main()
