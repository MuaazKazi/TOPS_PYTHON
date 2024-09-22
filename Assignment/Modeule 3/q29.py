# Write a Python program to unzip a list of tuples into individual lists.
my_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

unzipped = zip(*my_list)
list1, list2 = unzipped

l1= list(list1)
l2=list(list2)

new_list=l1,l2
print(list(new_list))



