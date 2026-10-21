from domain.item import Item


class healthPotion(Item):
    #this class is inherited from the Item Class which has the abstraction property
    #so we should must create the apply() method to make this class work correct
    def __init__(self, heal_amount: int = 25):
        self.heal_amount = heal_amount


    #this apply function is the abstraction method that which is defined in the Item classsss
    def apply(self, character) -> str:
        character.heal(self.heal_amount)
        return f"{character.name} drinks a potion and heals {self.heal_amount} HP!"


class Weapon(Item):
    def __init__(self, name: str, bonus_attack: int):
        self.name = name
        self.bonus_attack = bonus_attack


    def apply(self, character) -> str:
        character.attack_power += self.bonus_attack
        return f"{character.name} equips {self.name} (+{self.bonus_attack} ATK)"


class Armor(Item):
     def __init__(self, name: str, defence_power: int):
            self.name = name
            self.defence_power = defence_power

     def apply(self, character) -> str:
        character.defence += self.defence_power
        return f"{character.name} equips {self.name} Armor's defense power of (+{self.defence_power} ATK)"
    