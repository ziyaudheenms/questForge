from domain.character import Character

if __name__ == "__main__":
    print("QuestForge booting (level 0 skelton)")
    hero = Character("Hero", 100, 20)
    goblin = Character("Goblin", 80, 15)

    print(hero.describe())
    print(goblin.describe())

    hero.attack(goblin)   #attacking the globin instance with the hero instance

    print(goblin.describe())

    goblin.attack(hero)
    print(hero.describe())

    goblin.attack(hero)
    print(hero.describe())

    hero.attack(goblin)
    print(goblin.describe())

    hero.heal(10)
    