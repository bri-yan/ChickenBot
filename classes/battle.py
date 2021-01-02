from classes.chicken import Chicken
from classes.ability import Ability
import random

types = {"normal": {"normal": 1.0, "fire": 1.0, "ice": 1.0, "air": 1.0, "earth": 1.0, "electric": 1.0, "water": 1.0},
         "fire": {"normal": 1.0, "fire": 1.0, "ice": 1.5, "air": 1.0, "earth": 1.0, "electric": 1.0, "water": 0.5},
         "ice": {"normal": 1.0, "fire": 0.5, "ice": 1.0, "air": 1.5, "earth": 1.0, "electric": 1.0, "water": 1.0},
         "air": {"normal": 1.0, "fire": 1.0, "ice": 0.5, "air": 1.0, "earth": 1.5, "electric": 1.0, "water": 1.0},
         "earth": {"normal": 1.0, "fire": 1.0, "ice": 1.0, "air": 0.5, "earth": 1.0, "electric": 1.5, "water": 1.0},
         "electric": {"normal": 1.0, "fire": 1.0, "ice": 1.0, "air": 1.0, "earth": 0.5, "electric": 1.0, "water": 1.5},
         "water": {"normal": 1.0, "fire": 1.5, "ice": 1.0, "air": 1.0, "earth": 1.0, "electric": 0.5, "water": 1.0}}


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
        print(f"Luck: {luck}")
        modifier = (is_critical + 1) * self.effectiveness(ability, defender)
        print(f"Modifier: {modifier}")
        base = (((2 * attacker.level / 5 + 2) * ability.power * (attacker.strength / defender.defense)) / 50) + 2
        print(f"Base: {base}")
        damage = int(base * modifier * luck)
        print(f"Damage: {damage}")
        return damage

    def challenger_attack(self, ability: Ability, is_critical: bool) -> int:
        return self.calculate_damage(self.challenger, self.champion, ability, is_critical)

    def champion_attack(self, ability: Ability, is_critical: bool) -> int:
        return self.calculate_damage(self.champion, self.challenger, ability, is_critical)
