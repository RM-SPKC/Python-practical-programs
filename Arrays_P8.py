print("\n\t\t\tArrays")
print("\t\t\t------")
print("\nReverse the Array")
print("-----------------")

import array as ar
a=ar.array('i',[])
l=int(input("\nEnter the number of elements:"))
for i in range(l):
    n=int(input("\nEnter the elements: "))
    a.append(n)
    
print("\n\nGiven Array : ")
for i in a:
    print(i,end=" ")

a=a[::-1]

print("\n\nReversed Array : ")
for i in a:
    print(i,end=" ")





