print("\n\t\t\tDictionary")
print("\t\t\t----------")
print("1.Create")
print("2.Insert")
print("3.Update")
print("4.Delete")
print("5.Exit")
d={}
while True :
    c=int(input("\nEnter the choice :"))
    if(c==1):
        d={}
        n=int(input("Enter the number of elements :"))
        for i in range(n):
            k=input("Enter the Key: ")
            v=input("Enter the Value: ")
            d[k]=v
        print(d)
    elif(c==2):
        nk=input("Enter the new Key :")
        nv=input("Enter the new Value :")
        d[nk]=nv
        print(d)
    elif(c==3):
        ok=input("Enter the Key :")
        ov=input("Enter the  value to update:")
        d[ok]=ov
        print(d)
    elif(c==4):
        dk=input("Enter the Key to delete :")
        del d[dk]
        print(d)
    elif(c==5):
        print("Exiting....")
        break
    else:
        print("Enter a valid option between 1-5")
















