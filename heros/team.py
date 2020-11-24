
import random
from hero import Hero


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            if hero.deaths != 0 and hero.kills != 0:
                kd = str(hero.kills / hero.deaths)
                print("{} Kill/Deaths:{}".format(hero.name, kd))
            else:
                print("{} Kill/Deaths: N/A".format(hero.name))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)
        for hero in other_team.heroes:
            living_opponents.append(hero)
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            attacked_hero = random.choice(living_heroes)
            attacked_opponent = random.choice(living_opponents)
            attacked_hero.fight(attacked_opponent)
            if attacked_hero.is_alive():
                living_opponents.remove(attacked_opponent)
            else:
                living_heroes.remove(attacked_hero)
