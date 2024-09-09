# fibbonaci
inp=int(input("Enter number:"))
n1,n2=0,1

for res in range(1,inp+1):
    n2=n1
    n1=res
    res=n1+n2
    print(res)
