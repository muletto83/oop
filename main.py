'''
Assignment
Let's add a new game unit: Crossbowman.
A crossbowman is always an archer, 
but not all archers are crossbowmen.
Crossbowmen have several arrows,
but they have an additional method: triple_shot().

Complete the use_arrows method on the Archer class.
It should remove num arrows, 
but if there aren't enough arrows to remove, 
it should raise a not enough arrows exception instead.
Complete the Crossbowman class.
Its constructor should call its parent's constructor.
Its triple_shot method should:
Use 3 arrows
Return the string TARGET was shot by 3 crossbow bolts where TARGET is the name of the Human that was shot (any Human can be a target).
'''
class Human: # Base class for all humans
    # Constructor to initialize the name of the human
    def __init__(self, name): # Constructor with name parameter
        self.__name = name # private attribute

    def get_name(self):
        return self.__name # public method to access private attribute


## don't touch above this line


class Archer(Human): # Inherits from Human
    def __init__(self, name, num_arrows): # Constructor with name and number of arrows
        super().__init__(name) # Call the parent constructor to set the name
        self.__num_arrows = num_arrows # Private attribute for number of arrows

    def get_num_arrows(self): # Public method to get the number of arrows
        return self.__num_arrows # public method to access private attribute

    def use_arrows(self, num): # Method to use a certain number of arrows
        if num > self.__num_arrows: # Check if there are enough arrows
            raise Exception("not enough arrows") # Raise an exception if not enough arrows
        self.__num_arrows -= num # Decrease the number of arrows by num


class Crossbowman(Archer): # Inherits from Archer
    def __init__(self, name, num_arrows): # Constructor with name and number of arrows
        super().__init__(name, num_arrows) # Call the parent constructor to set the name and arrows

    def triple_shot(self, target): # Method to perform a triple shot
        self.use_arrows(3) # Use 3 arrows
        # Return a formatted string indicating the target was shot by 3 crossbow bolts
        return f"{target.get_name()} was shot by 3 crossbow bolts" 
