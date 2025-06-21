'''
Assignment
We changed the coordinates themselves to be private by adding two underscores to them. We now need to write getter methods to access them.

Complete the following methods:

get_left_x(): Returns the leftmost (smallest) x value
get_right_x(): Returns the rightmost (largest) x value
get_top_y(): Returns the topmost (largest) y value
get_bottom_y(): Returns the bottom-most (smallest) y value
Remember that we're working with a standard Cartesian plane.

We will explain the __repr__ method later, don't worry too much about it.

Tips
You may find Python's built-in min and max functions useful.
'''
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        pass

    def get_right_x(self):
        pass

    def get_top_y(self):
        pass

    def get_bottom_y(self):
        pass

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
