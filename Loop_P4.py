print("\n\n\t\t\tLoop Statements")
print("\t\t\t----------------")
print("\n\nDouble the values in List")
print("--------------------------")
l = [ ]
n = int(input("\nEnter the number of elements: "))

#for Loop to get input from user
for i in range(n):
    e = int(input("\nEnter the element: "))
    l.append(e)

i = 0
r = [ ]

# While loop to square the values
while i < n:
    r.append(l[i] * l[i])
    i += 1

print("\n\n\tThe given list:", l)
print("\n\tDoubled values in list:", r)



