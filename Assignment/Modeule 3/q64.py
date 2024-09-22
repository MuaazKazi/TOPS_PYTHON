# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
l=[]
for i in range(1,6):
    n=int(input("Enter number:"))
    l.append(n)
print(l)
print("Minimum number is:",min(l))
print("maximum number is:",max(l))