# Write a Python program to get the Fibonacci series of given range.
num=10
n1,n2=0,1
print("Fibonacci series:",n1,n2,end='')
for i in range(2,num):
    res=n1 + n2
    n1=n2
    n2=res
    print(res,end=' ')
print()