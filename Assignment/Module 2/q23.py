# Write a Python function to insert a string in the middle of a string.
def new_string(str1,new_str):
    midlle_string=len(str1) // 2
    final_str= str1[:midlle_string] + new_str + str1[midlle_string:]
    return final_str

inp=input("Enter a string:")
add_string=input("Enter a string:")

result= new_string(inp,add_string)
print("Result:",result)