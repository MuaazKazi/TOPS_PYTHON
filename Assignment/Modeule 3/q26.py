# Write a Python program to replace last value of tuples in a list.
my_tuple=(1,2,3,4,5)
new_value=0

list=list(my_tuple)

replace_value=list[-1]
list[-1]=new_value

new_list=[replace_value]


print("modified tuple:",list)
print("Replaced value in list:",new_list)