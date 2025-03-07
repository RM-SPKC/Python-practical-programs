print("\n\t\t\tLIST")
print("\t\t\t-----")
print("1. Create")
print("2. Insert")
print("3. Remove")      		
print("4. Sort")
print("5. Exit")
a=[ ]
while (1):
    b=int(input("\nEnter the choice:"))
    if(b==1):
        a=[ ]
        n=int(input("Enter the number of elements:"))
        for i in range(n):
            e =int(input("Enter the element: "))
            a.append(e)
        print("\n\tList: ",a)
    elif(b==2):
        c=int(input("Enter the element to insert :"))
        d=int(input("Enter index value :"))
        a.insert(d,c)
        print("\n\tList: ",a)
    elif(b==3):
        rem=int(input("Enter the element to remove: "))
        a.remove(rem)
        print("\n\tList: ",a)
    elif(b==4):
        a=sorted(a)
        print("\n\tSorted list: ",a)
    elif(b==5):
        print("\n\t\tExiting....")
        break
    else:
        print("Enter the option between 1-5")
