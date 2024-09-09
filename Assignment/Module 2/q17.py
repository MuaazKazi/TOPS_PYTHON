# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each 
# string.
str1=input("Enter a string 1:")
str2=input("Enter a string 2:")

if len(str1)>=2:
    str1=str1[1]+str1[0]+str1[2]
if len(str2)>=2:
    str2=str2[1]+str2[0]+str2[2]
    
res= str1 + ' ' + str2
print("Result:",res)