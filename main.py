'''
Assignment
Complete the bottom half of the main() function using two for-loops:

Iterate over all the dragons and describe() each one in order.
Iterate over all the dragons again and have each dragon breathe_fire at coordinatex=3, y=3.
Pass in all the other dragons (not the one currently breathing fire) as the units parameter,
so we can see if they get hit.
Pass in the dragons in the same order as the original list, excluding the current dragon.
For example, when Blue Dragon breathes fire, 
it should check to breathe fire on the other dragons in this order:

Green Dragon
Red Dragon
Black Dragon
Example Output
When you describe the dragons, your output should look like this:

Green Dragon is at 0/0
Red Dragon is at 2/2
Blue Dragon is at 4/3
Black Dragon is at 5/-1

The output of the first dragon breathing fire should look like this:

====================================
Green Dragon breathes fire at 3/3 with range 1
------------------------------------
Red Dragon is hit by the fire
Blue Dragon is hit by the fire
====================================
Red Dragon breathes fire at 3/3 with range 2
------------------------------------

Tips
Copying a List
To get a new copy of a list, use the copy() method. If you just do new_list = old_list, your new variable will just be a reference to the original list... which is not what we want.

nums = [4, 3, 2, 1]
nums_copy = nums.copy()
# nums_copy is [4, 3, 2, 1]

Delete from a List
fruits = ["apple", "banana", "cherry", "kiwi"]
del fruits[1]
# fruits is ["apple", "cherry", "kiwi"]
'''
def main(): 
    dragons = [ 
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    # don't touch above this line

    # ?
    # Iterate over all the dragons and describe each one
    for dragon in dragons:
        describe(dragon)
    # Iterate over all the dragons again and have each dragon breathe fire
    for dragon in dragons:
        # Create a copy of the dragons list excluding the current dragon
        other_dragons = dragons.copy()
        other_dragons.remove(dragon)
        # Have the dragon breathe fire at (3, 3) with the other dragons as units
        dragon.breathe_fire(3, 3, other_dragons)
        

    
# don't touch below this line


def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print("====================================")
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        print("------------------------------------")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


main()
