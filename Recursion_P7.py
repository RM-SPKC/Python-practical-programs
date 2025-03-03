print("\n\t\t\t Recursion")
print("\t\t\t-----------")
print("\nFactorial")
print("---------")
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("\nEnter a number: "))
print("\n\n\t\tFactorial of ",n," is : ",fact(n))
