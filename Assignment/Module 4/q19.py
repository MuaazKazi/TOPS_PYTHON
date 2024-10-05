# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.
num=int(input("Enter a number:"))
try :
    print(num,"divided by zero is",num/0)
except:
    print("Any number can't divided by zero")
finally:
    print("This will execute code any how")
