'''Assignment
Take a look at the Brawler class and the fight function provided, then complete the main function by doing the following:

Create 4 new brawlers with the following stats:
Name: Aragorn. Speed: 4. Strength: 4.
Name: Gimli. Speed: 2. Strength: 7.
Name: Legolas. Speed: 7. Strength: 7.
Name: Frodo. Speed: 3. Strength: 2.
Call fight twice:
The first fight should be Aragorn vs Gimli.
The second will be Legolas vs Frodo.'''

def main():
    brawler_Aragorn = Brawler("Aragorn", 4, 4)
    brawler_Gimli = Brawler("Gimli", 2, 7)
    brawler_Legolas = Brawler("Legolas", 7, 7)
    brawler_Frodo = Brawler("Frodo", 3, 2)
    fight(brawler_Aragorn, brawler_Gimli)
    fight(brawler_Legolas, brawler_Frodo)
# don't touch below this line


class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(f1, f2):
    print(f"{f1.name}: {f1.power} power")
    print(f"{f2.name}: {f2.power} power")
    if f1.power > f2.power:
        print(f"{f1.name} wins!")
    elif f1.power < f2.power:
        print(f"{f2.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")


main()
