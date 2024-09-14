# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers 
# between 1 and 30.

mylist =[]
for n in range(1,31):
    square=n**2
    mylist.append(square)
first_five=mylist[:5]
last_five=mylist[-5:]
print(f"First five ",first_five)
print(f"last five ",last_five)
print(first_five + last_five)


