# How will you compare two lists?
def comparison(l1,l2):
    l1.sort()
    l2.sort()
    if l1==l2:
        return "List are equal"
    else:
        return "List are not equal"
list1=[1,2,3,4]
list2=[2,3,4,1]
print('Result:',comparison(list1,list2))


        