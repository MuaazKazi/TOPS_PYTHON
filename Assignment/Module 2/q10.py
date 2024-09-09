# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
sum=num1+num2
sub=num1-num2
if num1 == num2 or sum == 5  or sub == 5:
    print("This condition is",True)
    print(f"Additon of given number is:{sum}")
    print(f"Subtraction of given number is:{sub}")
else:
    print("This condition is",False)
