'''
Assignment
Ensure the following requirements
from the game designers are completed:

Archer should inherit from Hero.
Archer should set up the hero's name and health.
Set a private "number of arrows" variable that 
can be set by the third parameter to the constructor.
Complete the shoot method. It takes a target hero as input.
If there are no arrows left, raise a not enough arrows exception.
Otherwise, 
remove an arrow and deal 10 damage to the target hero.
'''
class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


# don't touch above this line


class Archer:
    def __init__(self, name, health, num_arrows):
        pass

    def shoot(self, target):
        pass
