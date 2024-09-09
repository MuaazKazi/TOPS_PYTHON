# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',
#  replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
inp=input("Enter a string:")
not_occur=inp.find("not")
poor_occur=inp.find("poor")

if not_occur!=-1 or poor_occur != -1 or not_occur<poor_occur:
    if not_occur < poor_occur:
        res= inp[:not_occur] + 'good' + inp[poor_occur + len('poor'):]
else:
    res=inp
print(res)

 