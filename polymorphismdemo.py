# Polymorphism - Poly (many) + Morph (forms) [Achieve using 1) Inheritance 2) Duck Typing]
#              - polymorphism lets you call the same method on different types of objects 
#                and each object will respond in its own unique way.

class Shape:
    def area(self):
        return 0
    
class Rectanlge(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

'''  
r = Rectanlge(4,4)
c = Circle(4)
t = Triangle(4,4)

print('Rectangle:',r.area())
print('Circle:',c.area())
print('Triangle:',t.area())
'''
shapes = [Rectanlge(4,4), Circle(4),Triangle(4,4)]

for shape in shapes:
    print(shape.area())