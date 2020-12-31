import random
import copy
from typing import List


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