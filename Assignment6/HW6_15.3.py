"""
CS521
SiCheng Yi
"""

def gcd(m, n):
    #If m%n is 0, gcd(m,n) is n.
    if m % n == 0:
        return n
    #Otherwise, gcd(m,n) is gcd(n,m%n).
    return gcd(n, m % n)




#Test code
def main():
    #Ask for two number, just like:55,33
    m, n = eval(input("Enter two numbers: "))

    #Use gcd class to get greatest common divisor.
    print("The GCD of", m, "and", n, "is", gcd(m, n))

main()

