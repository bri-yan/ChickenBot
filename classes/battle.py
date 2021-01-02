from classes.chicken import Chicken
from classes.ability import Ability
import random

types = {"fire": {"normal": 1.0, "ice": 1.5, "wind": 1.0, "ground": 1.0, "electric": 1.0, "water": 0.5},
         "ice": {"normal": 1.0, "fire": 0.5, "wind": 1.5, "ground": 1.0, "electric": 1.0, "water": 1.0},
         "wind": {"normal": 1.0, "fire": 1.0, "ice": 0.5, "ground": 1.5, "electric": 1.0, "water": 1.0},
         "ground": {"normal": 1.0, "fire": 1.0, "ice": 1.0, "wind": 0.5, "electric": 1.5, "water": 1.0},
         "electric": {"normal": 1.0, "fire": 1.0, "ice": 1.0, "wind": 1.0, "ground": 0.5, "water": 1.5},
         "water": {"normal": 1.0, "fire": 1.5, "ice": 1.0, "wind": 1.0, "ground": 1.0, "electric": 0.5}}


class Battle:
    def __init__(self, challenger: Chicken, champion: Chicken):
        self.challenger = challenger
        self.champion = champion

    @staticmethod
    def is_critical(attacker: Chicken) -> bool:
        return random.random() <= max(1, attacker.luck) / 200

    @staticmethod
    def effectiveness(ability: Ability, defender: Chicken) -> float:
        return types[ability.type][defender.type]

    def calculate_damage(self, attacker: Chicken, defender: Chicken, ability: Ability, is_critical: bool) -> int:
        luck = (random.randint(85 + attacker.luck, 100 + attacker.luck) / 100)
        modifier = (is_critical + 1) * self.effectiveness(ability, defender)
        base = (((2 * attacker.level / 5 + 2) * ability.power * (attacker.strength / defender.defense)) / 50) + 2
        damage = int(base * modifier * luck)
        return damage

    def challenger_attack(self, ability: Ability, is_critical: bool) -> int:
        return self.calculate_damage(self.challenger, self.champion, ability, is_critical)

    def champion_attack(self, ability: Ability, is_critical: bool) -> int:
        return self.calculate_damage(self.champion, self.challenger, ability, is_critical)
