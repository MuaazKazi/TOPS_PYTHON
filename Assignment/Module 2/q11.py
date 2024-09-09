# Write a python program to sum of the first n positive integers.
inp = int(input("Enter number: "))
sum = 0

if inp >= 1:
    for num in range(1, inp + 1):
        sum += num  
    print(f"The sum of the first {inp} positive integers is {sum}")
else:
    print("Please enter a positive integer.")
