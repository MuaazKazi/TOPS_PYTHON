#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
"""
Inheritance in Python is when a class gets the properties and methods from another class.
"""
# Example:
class A:
    def a(self):
        print("This is a class A")

class B(A):
    def b(self):
        print("This is a class B")

obj = B()
print(dir(obj))
obj.a()
obj.b()
print()

# __init__:
"""
-__init__ is a special method in Python known as a constructor.It is automatically called when an object of a class is created.

-The __init__ method is used to initialize the object's properties.
"""
# Example:
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  
        self.model = model  
        self.year = year    

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()