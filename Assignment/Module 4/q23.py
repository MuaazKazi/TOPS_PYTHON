# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self,length,width):
            self.l= length
            self.w=width
    def area(self):
          return self.l * self.w
    
result=Rectangle(10,20)
print("The area of the rectangle is:",result.area())