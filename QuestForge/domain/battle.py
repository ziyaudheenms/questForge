from domain.character import Character


"""
    This is the example for the polymorphsim in fucntions 
    reference :--- https://www.geeksforgeeks.org/python/polymorphism-in-python/


"""
def run_special_round(attacker: Character, defender: Character) -> None:

    """  This is an example of the plymorphism in functionss
         for warrior , wage , or any charachter instance we just use this run_special_round function
         and pass the Character instance so that using the same function name we can trigger different 
         actions.........
    """


    attacker.special_ability(defender)    #as a result we can use thos run_special_round and trigger speacial_ability differently


def total_party_damage(party: Character, target:Character) -> None:

    party.attack(target)