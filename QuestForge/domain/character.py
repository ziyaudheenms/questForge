from abc import ABC, abstractmethod

class Character(ABC):

    """fleshed out level 1"""
    def __init__(self, name, health, attack_power):
        self.name = name
        self._health = health  # _ is used in order to say thhat its a protected variable but python doesnt stops accessing it 
        self.__max_health = health #__max_health uses two __ which is a stronger way to tell everyone that this variable is private and should not be accessed or modified directly. It is a convention in Python to use a single underscore for "protected" variables and double underscores for "private" variables.
        self.attack_power = attack_power

    # @property    -> used to access the private , protected variabes in a way like h1.health instead of h1.health() which is more like a function call.
    @property
    def health(self) -> int:
        return self._health

    @property
    def is_alive(self) -> bool:
        return self._health > 0

    def describe(self) -> str:
        return f"{self.name} has {self._health} HP and {self.attack_power} ATK with max health of {self.__max_health} HP."

    def take_damage(self, damage:int) -> None:
        if damage < 0:
            raise ValueError("Damage cannot be negative.")
        self._health = max(0, self._health - damage)  # Ensures health doesn't go below 0 , if -tve val comes, zero is greater than -tive there fore we get the 0 as the health.

    def attack(self, target: 'Character') -> None:    ## target: 'Character'  -> says that the target parameter is expected to be an instance of the Character class.
       if not self.is_alive:
           return
       
       target.take_damage(self.attack_power)
       print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def heal(self, hp: int) -> None:
        if hp < 0:
            raise ValueError("Healing amount cannot be negative.")
        self._health = min(self.__max_health, self._health + hp)  # Ensures health doesn't exceed max health, if our health is 90 and max health is 100, if we heal for 20, we should only go to 100, not 110. So we take the minimum of max health and current health + healing amount.
       

    @abstractmethod
    def special_ability(self, target: 'Character'):
        raise NotImplementedError     # The special Ability is a abstract method which that is used to tell the subclasses such that this method should be reused and implemented accordingly in the subclasses.


# We are going to generate the inherited Characters from the base Character class. We will create a Warrior and a Mage class that inherit from Character and have their own unique attributes and methods.

class Warrior(Character):
    def __init__(self, name):
        # super is used to call the parent and pass the required attributes to the parent class constructor so that we can use the base methods
        super().__init__(name, health=150, attack_power=20)  # Warrior has more health and attack power than a base character.


    def special_ability(self, target: Character) -> None:
        bonus = int(self.attack_power * 1.5)   # calling the self.attack_power will get the attack power from the base class and will use it
        target.take_damage(bonus)
        print(f"{self.name} uses Cleave! {bonus} damage to {target.name}")



class Mage(Character):
    def __init__(self, name: str):
        super().__init__(name, health=80, attack_power=10)
        # we can define the vaiables or data that is just belongs to this class onlyyyy.
        self.mana = 50


    def special_ability(self, target: Character) -> None:
        cost = 20
        if self.mana < cost:
            print(f"{self.name} doesn't have enough mana!")
            return
        self.mana -= cost
        damage = self.attack_power * 3
        target.take_damage(damage)
        print(f"{self.name} casts Fireball! {damage} damage to {target.name}")



class Rogue(Character):
    def __init__(self, name: str):
        super().__init__(name, health=90, attack_power=14)


    def special_ability(self, target: Character) -> None:
        crit = self.attack_power * 2
        target.take_damage(crit)
        print(f"{self.name} lands a Backstab! {crit} critical damage to {target.name}")

class Cleric(Character):
     def __init__(self, name: str, ):
            super().__init__(name, health=90, attack_power=14)
            self.heal_power = 100

    #clerik heals a friend instead of attcking the enemy
     def special_ability(self, target: Character) -> None:
         hp = 20
         if self.heal_power < hp:
             print(f"{self.name} doesn't have enough heal power!")

         target.heal(hp=hp)
         print(f"{self.name} spreads the heal power! {target.name}'s health boosted by {hp}HP")