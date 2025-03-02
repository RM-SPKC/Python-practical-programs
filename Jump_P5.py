print("\n\t\t\tJump Statements")
print("\t\t\t---------------")
print("\nSum of Positive Numbers")
print("------------------------\n")
print("\nEnter -1 to exit \n")
s=0
while True :
    n=int(input("\nEnter any Number :"))
    if(n==-1):
        break
    elif(n<=0):
        continue
    else :
        s=s+n
print("\n\n\t\tSum  of given Positive Numbers :",s)
