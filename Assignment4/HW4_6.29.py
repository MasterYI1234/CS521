"""
CS521
SiCheng Yi
"""

# Check the number is vaild or not vaild, if is, return true.
def isValid(number):
    valid = False
    #Check which card is.
    if prefixMatched(4 , getPrefix(number, 1)): 
        valid |= True 
    if prefixMatched(5 , getPrefix(number, 1)):
        valid |= True
    if prefixMatched(6 , getPrefix(number, 1)): 
        valid |= True
    if prefixMatched(37 , getPrefix(number, 2)): 
        valid |= True
    #Check how much number of the carf number, if it larger for the card number size, reuturn flase.
    if getSize(number) < 13 or getSize(number) > 16:
        valid &= False
    #Check is it vaild?
    result = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    if result % 10 != 0:
        valid &= False

    return valid

#Step 2, add all single-digit numbers from step1.
def sumOfDoubleEvenPlace(number):
    sum = 0
    even = 0
    #Just from a single to even, if even is 1, then it is even.
    while number > 0:
        if even == 1:
            sum += getDigit(number % 10)
        even ^= 1 
        number //= 10
    return sum


def getDigit(number):
    #if the number * 2 >=10, then  % 10 + /10(how many ten), return the sum, if number * 2<10, then / 10 is 0.
    number *= 2
    return (number % 10) + (number // 10); 
    

# Sum of odd place.
def sumOfOddPlace(number):
    #Just the same as even, if the odd is 1, it is odd place.
    sum = 0
    odd = 1
    while number > 0:
        if odd == 1:
            sum += number % 10
        odd ^= 1
        number //= 10
    return sum


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    return True if str(number).startswith(d) else False


# Return the number of digits in d
def getSize(d):
    return len(str(d))


#Return the first k digits of the number
def getPrefix(number, k):
    return str(number) if getSize(number) <= k else str(number)[0:k] # actually it works like ternary operator so if condition is true then str(number) will execute else str(number)[0:k] will execute. str(number) just typecasting number to string. getSize(number) returns the no of digits in number. so if its <= k return the number otherwise return its prefix so for example number= 12345, and k = 2 it will return 12, but if k = 5 or more it will return 12345 as string. so "12345"
print("Enter the credit card number")
number = int(input())

print ("valid" if isValid(number) else "invalid")