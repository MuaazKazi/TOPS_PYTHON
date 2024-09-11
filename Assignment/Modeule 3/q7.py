# Write a Python program to remove duplicates from a list.
def remove_duplicate(my_List):
        return set(my_List)
list=[1,2,3,4,2,3,2,5]
new_list=remove_duplicate(list)
print(new_list)
