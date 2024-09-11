# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers 
# between 1 and 30.
def square_num(start,end):
    for n in range(start,end):
        if start <= n:
            return n
        if end <= n:
            return n
n=5
start=1
end=30
result=square_num(start**2,end**2)
print(result)

    