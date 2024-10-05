# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

"""
In Python, you define a class using the class keyword followed by the class name and a colon

-class class_name:
"""

"""
Self: self is a reference to the current instance of the class. It is used to access variables and methods that belong to the class.

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
