from domain.character import Character, Rogue, Warrior,Mage, Cleric
from domain.battle import run_special_round, total_party_damage
if __name__ == "__main__":
    print("QuestForge booting (level 0 skelton)")
    # hero = Character("Aria", 100, 15)
    # hero.take_damage(150)
    # hero.health(-50)  # This will raise a ValueError because damage cannot be negative.
    # print(hero.health)   # since we have implementd checks we get health as zero preventing from it going into negative values.



    # warrior = Warrior("Bram")
    # mage = Mage("Sylla")
    # cleric = Cleric('clera')


    # warrior.attack(mage)            # Reusing parent Character method
    # mage.special_ability(warrior)   # Using specialized Mage method
    # print(f"Bram HP: {warrior.health}, Sylla HP: {mage.health}")
    # cleric.special_ability(warrior)

    # party = [Warrior("Bram"), Mage("Sylla"), Rogue("Kade"), Cleric('Clara')]   #creating a list of character instances ----> where with just a same function call we trigger different actions
    # dummy = Warrior("Training Dummy")

    # for member in party:
    #     run_special_round(member, dummy)

    # print(f"Dummy HP: {dummy.health}\n")

    person = Character("Test" , 10 , 1)  #this will give as error since we have a abstactmethod in this core class anf we havent implemented it ---> which means we cant direclty build object with classes that have abstractmethod , in replace we have to create a subclass of it....