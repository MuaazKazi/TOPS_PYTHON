# Write a Python program to remove an empty tuple(s) from a list of tuples.
list=[1,2,(3,4),(),5,()]
new_list=[]
for n in list:
    if n:
        new_list.append(n)
print(f"List after removing empty tuple:{new_list}")
