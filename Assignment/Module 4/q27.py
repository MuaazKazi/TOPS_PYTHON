# What is used to check whether an object o is an instance of class A?
"""
To check whether an object o is an instance of class A in Python, you use the isinstance() function.
"""

class A:
    pass

class B:
    pass

o = A()  
print(isinstance(o, A)) 
print(isinstance(o, B)) 
