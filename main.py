'''
Assignment
Complete the Wizard class.

Wizard should inherit from Hero.
Wizard should set up the hero's name and health.
Set a private mana variable that
can be passed in as a third parameter to the constructor.
Create a cast method that takes a target hero as input.
If there is less than 25 mana left,
raise a not enough mana exception.
Otherwise, remove 25 mana from the wizard 
and deal 25 damage to the target hero.
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


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


# don't touch above this line


class Wizard(Hero):
    def __init__(self, name, health, mana):
        pass

    def cast(self, target):
        pass
