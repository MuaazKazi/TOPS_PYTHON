# Write a Python function to reverses a string if its length is a multiple of 4.
def rev_string(String):
    if len(String) % 4 ==0:
        return String[::-1]
    else:
        return String
inp=input("Enter a string:")
result= rev_string(inp)
print("Result:",result)

        