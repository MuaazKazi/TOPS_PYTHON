# Write a Python function to get the largest number, smallest num and sum of all from a list.
def my_list(num):
    largest=num[0]
    smallest=num[0]
    sum=num[0]
    for n in num:
        if n > largest:
            largest=n
        if n < smallest:
            smallest=n
        sum+=n
    return largest,smallest,sum
num=[1,2,3,5,9,2]
largest,smallest,sum=my_list(num)
print(f"largest number :{largest}")
print(f"smallest number:{smallest}")
print(f"Total sum:{sum}")
    