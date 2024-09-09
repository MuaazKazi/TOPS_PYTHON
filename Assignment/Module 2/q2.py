# Write a Python program to get the Factorial number of given number.
num=int(input("Enter any number:"))
factorial=1

if num >= 1:
    for num in range(1,num + 1):
        factorial = factorial * num
    print("Your factorial of given number is:",factorial)