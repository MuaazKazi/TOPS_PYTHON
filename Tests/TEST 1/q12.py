# largest of three
n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
n3=int(input("Enter number:"))
if n1 > n2 and n1 > n3:
    print("number 1 is greater:",n1)
elif n2 > n1 and n2 > n3:
    print("number 2 is greater:",n2)
elif n3 > n1 and n3 > n2:
    print("number 3 is greater:",n3)
else:
    print("invalid input.")
