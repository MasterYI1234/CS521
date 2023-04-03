"""
CS521
SiCheng Yi
"""

#Write a recursive function that computes the sum of the digits in an integer. Use the following function header: def sumDigits(n):
def sumDigits(x):
    #if the number < 10, just return the number
    if x%10 == 0:
        return x
    #if number>10, just add every element in the number one by one.
    else:
        
        sum = x%10 + sumDigits(x//10)
        
        return sum




#Test code, just enter a number, like: 234
def main():
    n = eval(input("Enter a digit: "))
    
    print("The sum of the digits is:", sumDigits(n))

main()