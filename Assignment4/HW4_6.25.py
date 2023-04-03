"""
CS521
SiCheng Yi
"""
#For this program, we need 2 function, the first is check the number is prime, then reverse the number, then do the check again.


#Check the number is it prime?
def prime(n):
    div = 2
    #Let the number / 2 and check is it % is 0, if not, the number is not prime.
    while div <= n/2:
        if n % div == 0:
            return False
        div+=1
    return True

#reverse the number
def reverse(m):
    s = m
    a = len(str(s))
    h = ""
    #Let the number to be a string, then reverse the letter in the string.
    for m in range(a):
        h+=str(s%10)
        s = s//10
    #Make the string back to the number.
    return int(h)

def main():
    count = 1
    num = 10
    while count<=100:
        #Check the number is prime?
        if prime(num):
            #If return true, reverse the number. Check the reverse is prime?
            if reverse(prime(num)):
                if count%10==0:
                    print(num)
                else:
                    print(num," ",end="")
            count+=1
        num+=1
main()