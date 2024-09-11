"""
Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.
"""
def count_string(strings_list):
    count=0
    for s in strings_list:
        if len(s) >=2 and s[0]==s[-1]:
            count+=1
    return count
strings_list=['aa','cc','apple','ana','dad','mom','abbs']
result=count_string(strings_list)
print(result)

        