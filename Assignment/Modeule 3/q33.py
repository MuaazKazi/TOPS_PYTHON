# Write a Python script to concatenate following dictionaries to create a new one.
n1={'n1':1,'n2':2,'n3':3,'n4':4,'n5':5}
n2={'n6':6,'n7':7,'n8':8,'n9':9,'n10':10}
n3={'n11':11,'n12':12}
result={}
for d in (n1,n2,n3):
    result.update(d)
print("Result:",result)


