'''
Assignment
Some lazy class variable code written by another dev team 
at Age of Dragons Studios is causing bugs in our team's Dragon class.
In the main() function (that our team isn't responsible for) the line:
Dragon.element = "fire"
should not affect our existing Dragon instances!
The Dragon class should be safe to use in other parts of the codebase,
even if silly developers are out there changing class-level variables.
Fix the Dragon class.
Remove the element class variable.
Use an instance variable for element, and allow it to be set in the constructor.
'''

class Dragon:
    element = "ice"

    def __init__(self, element):
        return

    def get_breath_damage(self):
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0


# don't touch below this line


def main():
    first_dragon = Dragon("fire")
    print(
        f"{first_dragon.element} dragon does {first_dragon.get_breath_damage()} damage"
    )

    second_dragon = Dragon("ice")
    Dragon.element = "fire"
    print(
        f"{second_dragon.element} dragon does {second_dragon.get_breath_damage()} damage"
    )


main()
