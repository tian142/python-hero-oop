from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")

    def create_ability(self):
        name = input("Enter an ability: ")
        max_damage = int(input("Enter max ability danage: "))
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("Enter weapon name:  ")
        max_damage = int(input("Enter max weapon damage: "))
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("Enter armor name:  ")
        max_block = int(input("Enter max armor damage reduction: "))
        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Enter Hero name ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        team_size = int(
            input("How many Heros in team 1?\n"))
        for _ in range(team_size):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        team_size = int(
            input("How many Heros in team 2?\n"))
        for _ in range(team_size):
            hero = self.create_hero()
            self.team_two.add_hero(hero)  # Add the created hero to team two.

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_kd(self, team):
        team_kills = 0
        team_deaths = 0
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        kd = team_kills/team_deaths
        print(f"Kill/Death ratio for {team.name} is: {kd}.")

    def surviving_heros(self, team):
        for hero in team.heroes:
            if hero.deaths == 0:
                print(f"{hero.name} survived.")

    def show_stats(self):
        print(f"\n{self.team_one.name}'s team stat: ")
        self.team_one.stats()
        print(f"\n{self.team_two.name}'s team stat: ")
        self.team_two.stats()
        print("\n")
        self.show_kd(self.team_one)
        self.show_kd(self.team_two)
        self.surviving_heros(self.team_one)
        self.surviving_heros(self.team_two)


if __name__ == "__main__":
    battling = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    while battling:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Would you like to play again? (y/n) ")
        if play_again.lower() == "n":
            battling = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
