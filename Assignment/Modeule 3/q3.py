# Differentiate between append () and extend () methods?
"""
append(): Adds a single element to the end of the list.
"""
# Example:
list=[1,2,3]
list.append(4)
print("Append list:",list)

list.append([5,6])
print("Append list:",list)

"""
extend():Takes an iterable as an argument and adds each of its elements to the end of the list.
"""
# Example:
my_list = [1, 2, 3]
my_list.extend([4, 5])
print("Extend list:",my_list)  


