# Write a Python function to calculate the factorial of a number (a nonnegative integer)
inp=int(input("Enter number:"))
factorial=1
if inp > 0:
    for i in range(1,inp+1):
        if i < 0:
            print("Enter valid number.")
        else:
            factorial*=i
    print(f"factorial of {inp} is {factorial}")

