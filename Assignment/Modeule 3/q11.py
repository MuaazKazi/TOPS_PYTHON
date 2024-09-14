# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_element(list1):
    return list(set(list1))

list1=[1,2,3,2,3,4,5]
unique_list=unique_element(list1)
print("unique list:",unique_list)
    