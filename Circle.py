 # Circle.py

from Shape2D import Shape2D

class Circle(Shape2D):
    def __init__(self, color, radius):
        Shape2D.__init__(self, color)
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self, radius2):
        self.radius = radius2
    def computeArea(self):
        area = (3.14159 * self.radius ** 2)
        return area
    def computePerimeter(self):
        perimeter = (2 * 3.14159 * self.radius)
        return perimeter
    def getShapeProperties(self):
        return ('Shape: CIRCLE, Color: {}, Radius: {}, Area: {}, Perimeter: {}'.format(self.color, self.radius, self.computeArea(), self.computePerimeter()))

if __name__ == '__main__':
    c1 = Circle('Green', 5.3)
    c1.setRadius(20)
    print(c1.getShapeProperties())
    print('\n', c1.computePerimeter())
