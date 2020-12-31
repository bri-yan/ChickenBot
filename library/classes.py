from typing import List
import random
import copy
import discord


class Ability:
    def __init__(self, name, type_, power):
        self.name = name
        self.type = type_
        self.power = power


class Chicken:
    def __init__(self, name):
        # Info
        self.name = name
        self.level = 1
        self.wins = 0

        # Modifiers
        self.strength = 0
        self.defense = 0
        self.speed = 0
        self.luck = 0

        # Combat
        self.exp = 0
        self.exp_cap = 25
        self.health = 0
        self.max_health = 50
        self.abilities = []

    def randomize(self, lower, upper):
        self.strength += random.randint(lower, upper)
        self.defense += random.randint(lower, upper)
        self.speed += random.randint(lower, upper)
        self.luck += random.randint(0, upper)
        self.max_health += random.randint(lower, upper)
        self.health = self.max_health

    def initialize(self):
        self.randomize(-5, 5)

    def clone(self):
        return copy.deepcopy(self).randomize(-5, 0)

    def lose_health(self, amount):
        self.health = max(self.health - amount, 0)

    def health_display(self):
        # Heart emoji unicodes
        red_heart = u"\u2764"
        half_heart = u"\U0001F494"
        empty_heart = u"\U0001F5A4"

        health_bar = f"[{self.health}/{self.max_health}] "

        hearts = (self.health / self.max_health) * 10
        # Get the integer value of hearts which rounds down if hearts is within 0.75 of its floor
        heart_count = int(hearts) + (hearts >= int(hearts) + 0.75)
        # Get whether a half heart is needed if hearts is 0.25 above its floor and 0.25 below its ceiling or if this is
        # the last heart.
        half_count = heart_count + .25 < hearts < heart_count + 0.75 or 0 < hearts < 1
        empty_count = 10 - heart_count - half_count

        health_bar += heart_count * red_heart + half_count * half_heart + empty_count * empty_heart
        return health_bar


class Party:
    def __init__(self):
        self.party: List[Chicken] = []

    def add_chicken(self, chicken: Chicken) -> bool:
        if len(self.party) < self.limit:
            self.party.append(chicken)
            return True
        else:
            return False

    def remove_chicken(self, chicken: Chicken) -> bool:
        if chicken in self.party:
            self.party.remove(chicken)
            return True
        else:
            return False

    def party_display(self):
        display = ""
        for chicken in self.party:
            display += chicken.name + " "
        return display


class Battle:
    def __init__(self, challenger: Chicken, champion: Chicken):
        self.challenger = challenger
        self.champion = champion

    @staticmethod
    def is_critical(self, attacker: Chicken) -> bool:
        return random.random() <= attacker.luck / 200

    @staticmethod
    def calculate_damage(self, attacker: Chicken, defender: Chicken, ability: Ability, is_critical: bool) -> int:
        modifier = (random.randint(85 + attacker.luck, 100 + attacker.luck) / 100) * (is_critical + 1)
        base = (((2 * attacker.level / 5 + 2) * ability.power * (attacker.strength / defender.defense)) / 50) + 2
        damage = int(base * modifier)
        return damage

    def challenger_attack(self, ability: Ability, is_critical: bool) -> int:
        return self.calculate_damage(self, self.challenger, self.champion, ability, is_critical)

    def champion_attack(self, ability: Ability, is_critical: bool) -> int:
        return self.calculate_damage(self, self.champion, self.challenger, ability, is_critical)


class Player:
    def __init__(self, member: discord.Member):
        self.member = member
        self.balance = 0
        self.limit = 1
        self.party = []

    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        self.balance = max(self.balance - amount, 0)




