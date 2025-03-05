print("\n\t\t\tString Operations")
print("\t\t\t------------------")
print("1.Create")
print("2.Length")
print("3.Slice Operation")
print("4.Replace") 
print("5.Exit")
 
while True:
  m = int (input ("\nEnter Your Choice :"))
  if(m == 1):
      s= input ("Enter Your String :")
      print("\n\tThe Given String is : ",s)
  elif(m==2):
      print ("\n\tLength of the given string is :",len(s))            
  elif(m==3):
      sv=int(input("Enter the Start value :"))
      ev=int(input("Enter the End value :"))
      st=int (input("Enter the stride Value :"))
      print ("\n\tSliced string is ",s[sv:ev:st]) 
  elif (m ==4):                                                                           
      old=input("Enter the Old String to be replaced :")
      new=input("Enter the new String :")
      print("\n\tThe word has been replaced: ",s.replace(old, new))
  elif(m==5):
          print("\n\t\tExiting.....")
          break
else :
    print("Enter the option between 1-5")
