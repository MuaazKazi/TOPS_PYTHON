# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
from math import pi
class Circle:
    def __init__(self):
          self.radius= float(input("Enter any number for radius:"))
    def compute_area(self):
        print("Area of circle is:",pi*self.radius * self.radius)
    def compute_perimeter(self):
        print("Perimeter of circle is:",2*pi * self.radius)

o=Circle()
o.compute_area()
o.compute_perimeter()
