# Write a Python program to check multiple keys exists in a dictionary
dict={'n1':1,'n2':2,'n3':3,'n4':4,'n5':5}
def is_key_present(x):
    if x in dict:
        print(f"key {x} exist")
    else:
        print(f"key {x} dosen't exist")
is_key_present('n1')
is_key_present('n2')
is_key_present('n5')
is_key_present('n7')

