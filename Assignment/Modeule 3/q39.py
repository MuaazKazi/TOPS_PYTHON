# Write a Python script to merge two Python dictionaries
dict1={'n1':1,'n2':2,'n3':3,'n4':4,'n5':5}
dict2={'n6':6,'n7':7,'n8':8,'n9':9,'n10':10}
print("Merged_dict:",dict1 | dict2)


#2nd method
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)