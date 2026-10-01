from domain.character import Warrior,Mage, Cleric

if __name__ == "__main__":
    print("QuestForge booting (level 0 skelton)")
    # hero = Character("Aria", 100, 15)
    # hero.take_damage(150)
    # hero.health(-50)  # This will raise a ValueError because damage cannot be negative.
    # print(hero.health)   # since we have implementd checks we get health as zero preventing from it going into negative values.



    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    cleric = Cleric('clera')


    warrior.attack(mage)            # Reusing parent Character method
    mage.special_ability(warrior)   # Using specialized Mage method
    print(f"Bram HP: {warrior.health}, Sylla HP: {mage.health}")
    cleric.special_ability(warrior)