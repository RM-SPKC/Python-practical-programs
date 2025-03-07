l = [ ]
t = ( )
print("\n\t\t\tTuple")
print("\t\t\t------")
print("1. Create")
print("2. Length")
print("3. Concatenate")
print("4. Delete")
print("5. Exit")
while True:
    c = int(input("\nEnter the choice: "))
    if c == 1:
        n = int(input("Enter the number of elements: "))
        l=[ ]# Clear the list before creating new list
        t=( )  # Clear the tuple before creating new tuple
        for i in range(n):
            e = int(input("Enter the element: "))
            l.append(e)
        t=t+tuple(l)
        print("Tuple: ", t)
    elif c == 2:
        print("Number of elements in tuple: ", len(t))
    elif c == 3:
        up = int(input("Enter the element to append: "))
        t = t + (up,)  # Append the new element as a single-element tuple
        print("Tuple: ", t)
    elif c == 4:
        del t  # Reset the tuple instead of deleting
        print("Tuple deleted")
    elif c == 5:
        print("Exiting...")
        break
    else:
        print("Enter the option between 1-5")








