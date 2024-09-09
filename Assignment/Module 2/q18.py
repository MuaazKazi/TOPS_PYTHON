# Write a Python program to add 'ing' at the end of a given string (lengthshould be at least 3). If the given string already ends with 
# 'ing' then add'ly' instead if the string length of the given string is less than 3, leave it unchanged.
inp=input("Enter a string:")
if len (inp)>=3:
    if inp.endswith('ing'):
        result = inp + 'ly'
    else:
        result= inp + 'ing'
else:
    result=inp
print("Result:",result)
