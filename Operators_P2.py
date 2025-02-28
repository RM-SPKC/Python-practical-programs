print("\n\t\t\tOPERATORS")
print("\t\t\t---------")
a=int(input("\n\nEnter the first number  : " ))
b=int(input("Enter the second number : "))
#Arithmetic operators
print("\nArithmetic Operators")
print("--------------------")
print("Addition         : ",a+b)
print("Subraction       : ",a-b)
print("Multiplication   : ",a*b)
print("Division         : ",a/b)
print("Modulus          : ",a%b)
print("Floor Division   : ",a//b)
print("Exponent         : ",a**b)
#Relational or Comparision Operators
print("\nRelational or Comparision Operators")
print("-----------------------------------")
print("Equal to                : ",a==b)
print("Not Equal to            : ",a!=b)
print("Greater than            : ",a>b)
print("Greater than or Equal to: ",a>=b)
print("Less than               : ",a<b)
print("Less than or Equal to   : ",a<=b)
#Logical Operators
print("\nLogical Operators")
print("-----------------")
print("AND [a==b and a!=b] : ",a==b and a!=b)
print("OR [a==b or a!=b]   : ",a==b or a!=b)
print("NOT [not a]         : ",not a)
#Bitwise Operators
print("\nBitwise Operators")
print("-----------------")
print("Bitwise AND         : ",a&b)
print("Bitwise OR          : ",a|b)
print("Bitwise NOT         : ",~a)
print("Bitwise XOR         : ",a^b)
#Shift Operators
print("\nShift Operators")
print("---------------")
print("Left Shift          : ",a<<2)
print("Right Shift         : ",a>>2)
#Membership Operators
print("\nMembership Operators")
print("--------------------")
l=[1,2,3,4,5]
if(a in l):
    print(a ,"is in",l)
else:
    print(a," is not in",l)
#Identity Operators
print("\nIdentity Operators")
print("------------------")
if(a is b):
    print("a is same as b")
else:
    print("a is not same as b")
#Assignment Operators
print("\nAssignment Operators")
print("--------------------")
print("a+=b      : ",a+b)
print("a-=b      : ",a-b)
print("a*=b      : ",a*b)
print("a/=b      : ",a/b)
print("a%=b      : ",a%b)
print("a**=b     : ",a**b)
print("a//=b     : ",a//b)


