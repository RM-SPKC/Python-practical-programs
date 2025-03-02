print("\n\t\t\tFunctions")
print("\t\t\t---------")
print("\n\nSTUDENT DETAILS")
print("---------------")
def studinfo():
    global sname,sid,cname,dept,cpp,dd,php;
    sname=  input("\nEnter the student name       : ")
    sid=int(input("Enter the register number    : "))
    cname=  input("Enter the class name         : ")
    cpp=int(input("Enter the C++ mark           : "))
    dd=int(input("Enter the DD mark            : "))
    php=int(input("Enter the PHP mark           : "))
def calc():
    global total,average
    total=cpp+dd+php
    average=total/3
def display():
    print("\n\n\t\t\tSTUDENT MARK DETAILS")
    print("\t\t\t--------------------")
    print("\tStudent name         :  ",sname)
    print("\tRegister No.         :  ",sid)
    print("\tClass name           :  ",cname)
    print("\tC++ Mark             :  ",cpp)
    print("\tDD  Mark             :  ",dd)
    print("\tPHP Mark             :  ",php)
    print("\tTotal                :  ",total)
    print("\tAverage              :  ",average)
studinfo( )
calc( )
display( )
