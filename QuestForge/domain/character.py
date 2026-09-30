class Character:
    """fleshed out level 1"""
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power


    def describe(self) -> str:
        return f"{self.name} has {self.health} HP and {self.attack_power} ATK"

    def attack(self, target: 'Character') -> None:    ## target: 'Character'  -> says that the target parameter is expected to be an instance of the Character class.
       target.health -= self.attack_power
       print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def heal(self, hp: int) -> None:
        self.health += hp
        print(f"{self.name} boosted the health by {hp} points!")

