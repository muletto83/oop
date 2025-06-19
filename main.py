'''
Assignment
We don't want our coworkers at Age of Dragons Studios™ to have to worry about how Humans move. 
We'll abstract that away from them,
by encapsulating the private __pos_x, __pos_y, and __speed variables behind some simple methods.

Complete the following methods in the Human class:

move_right(): Adds the human's speed to its x position.
move_left(): Subtracts the human's speed from its x position.
move_up(): Adds the human's speed to its y position.
move_down(): Subtracts the human's speed from its y position.
get_position(): Returns the x position and y position as a tuple.
'''

class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def get_position(self):
        pass


