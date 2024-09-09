# while loop to print first 10 even num
n= 10
while n <=10:
    if n % 2 == 0:
        for num in range(1,n+1):
            n += num
print(n)
