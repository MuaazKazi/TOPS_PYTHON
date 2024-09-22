# Why Do You Use the Zip () Method in Python?
"""
The zip() method in Python is a built-in function that is used to combine two or more iterables (like lists, tuples, or dictionaries) 
into a single iterable of tuples. 
"""
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))  
