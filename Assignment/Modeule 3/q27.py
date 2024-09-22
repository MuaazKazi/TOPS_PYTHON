# Write a Python program to find the repeated items of a tuple.
my_tuple=(1,2,2,1,2,3,4,5,6)
count={}
repeated_num=set()
for n in my_tuple:
    if n in count:
        count[n]+=1
        repeated_num.add(n)
    else:
        count[n]=1
print("Original elements:",my_tuple)
print('Repeated elements are:',repeated_num)


