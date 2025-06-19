'''
Assignment
Complete all the missing methods:

Complete the private helper methods, which are intended to be used by the other four sprinting methods.
__raise_if_cannot_sprint(): Raise the exception: not enough stamina to sprint if the human is out of stamina.
__use_sprint_stamina(): Remove one stamina from the human.
For each of the sprint methods:
Raise an error if there isn't enough stamina to sprint (use __raise_if_cannot_sprint()).
Use the stamina needed to sprint (use __use_sprint_stamina())
Move twice in the direction of the sprint.
'''

class Human:
    def sprint_right(self):
        pass

    def sprint_left(self):
        pass

    def sprint_up(self):
        pass

    def sprint_down(self):
        pass

    def __raise_if_cannot_sprint(self):
        pass

    def __use_sprint_stamina(self):
        pass

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina
