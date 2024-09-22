# Write a Python program to find the highest 3 values in a dictionary
dict={'n1':1,'n2':20,'n3':300,'n4':400,'n5':50}
highest_value=sorted(dict.values(),reverse=True)[:3]
print("Highest 3 values from dictionary:",highest_value)
