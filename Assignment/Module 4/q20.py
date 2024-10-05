#Write python program that user to enter only odd numbers, else will raise an exception.
def only_odd():
    try:
        num=int(input("Enter a number:"))
        if num %2==0:
            raise ValueError("Error:You entered even number.")
        print("You entered an odd number.")
    except ValueError as msg:
        print(msg)
only_odd()