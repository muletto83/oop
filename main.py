'''
Inheritance Practice
You discovered that to properly calculate army formations in the game,
you needed to be able to get the area and perimeter of squares and rectangles of various sizes.

Assignment
Finish implementing the empty methods of the Rectangle and Square classes.
All squares are rectangles, but not all rectangles are squares.

Due to inheritance of methods,
the Square class should only need to implement the __init__ method.
'''
class Rectangle:
    def __init__(self, length, width):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Square(Rectangle):
    def __init__(self, length):
        pass
