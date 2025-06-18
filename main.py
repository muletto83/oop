'''
Assignment
Complete the Wizard class's constructor.

Set 2 private properties (be sure to include the private __ prefix):
stamina
intelligence
Set 3 public properties:
name: Use the value passed into the constructor
health: 100x the value of "stamina"
mana: 10x the value of "intelligence"
'''

class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = self.__stamina * 100
        self.mana = self.__intelligence * 10
