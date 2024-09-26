#  Write a Python function that takes two lists and returns true if they have at least one common member.
def compare_list(list1,list2):
    for element in list1:
        if element in list2:
            print(f"List1:{list1} and list2:{list2} have common element:{element}")
            return True
        
        else:
            print("No common element found.")
            return False
            
list1=[7,2,8,9,10]
list2=[1,2,3,7]
result=compare_list(list1,list2)
print(result)
