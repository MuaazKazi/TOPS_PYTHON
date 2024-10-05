# What is Instantiation in terms of OOP terminology?

# Instantiation in Object-Oriented Programming (OOP) refers to the process of creating an object from a class. 

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  
        self.model = model  
        self.year = year    

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()


"""
Here,
my_car = Car("Toyota", "Camry", 2020)  is Instantiation

"""