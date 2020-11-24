from ability import Ability
from armor import Armor
from weapon import Weapon


import random


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    # If you run this file from the terminal
    # this block is executed.

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense = armor.block()
        return total_defense

    def take_damage(self, damage):
        damage_after_defense = damage - self.defend()
        if damage_after_defense > 0:
            self.current_health -= damage_after_defense

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def add_kills(self, num_kills=1):
        self.kills += num_kills

    def add_deaths(self, num_deaths=1):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def fight(self, opponent):
        # Check if any of the Heroes can do damage
        if self.abilities.count == 0 and opponent.abilities.count == 0:
            return print("Battle Draw, because both out of moves")
        while self.is_alive() and opponent.is_alive():
            self_damage = self.attack()
            opponent.take_damage(self_damage)
            opponent_damage = opponent.attack()
            self.take_damage(opponent_damage)

        if self.is_alive() == False and opponent.is_alive() == False:
            self.add_deaths()
            opponent.add_deaths()
            print("Battle Draw, beacause both died")

        elif self.is_alive() == False:
            self.add_deaths()
            opponent.add_kills()
            print(f"{opponent.name} won the Battle")

        elif opponent.is_alive() == False:
            self.add_kills()
            opponent.add_deaths()
            print(f"{self.name} won the Battle")
        else:
            return('error')


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
