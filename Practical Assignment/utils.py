# Relative imports
from .circle import Circle
from .rectangle import Rectangle

def show_areas():
    c = Circle(3)
    r = Rectangle(2, 5)
    print("Circle Area:", c.area())
    print("Rectangle Area:", r.area())
