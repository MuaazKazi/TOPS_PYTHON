# What is the purpose continue statement in python?

"""
In Python, the continue statement is used within loops to skip the remaining code inside the loop for the current iteration and 
proceed with the next iteration of the loop.
"""
# Example

for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)

