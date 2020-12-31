from classes.chicken import Chicken
from classes.ability import Ability
import random


class Battle:
    def __init__(self, challenger: Chicken, champion: Chicken):
        self.challenger = challenger
        self.champion = champion

    @staticmethod
    def is_critical(attacker: Chicken) -> bool:
        return random.random() <= attacker.luck / 200

    @staticmethod
    def calculate_damage(attacker: Chicken, defender: Chicken, ability: Ability, is_critical: bool) -> int:
        modifier = (random.randint(85 + attacker.luck, 100 + attacker.luck) / 100) * (is_critical + 1)
        base = (((2 * attacker.level / 5 + 2) * ability.power * (attacker.strength / defender.defense)) / 50) + 2
        damage = int(base * modifier)
        return damage

    def challenger_attack(self, ability: Ability, is_critical: bool) -> int:
        return self.calculate_damage(self.challenger, self.champion, ability, is_critical)

    def champion_attack(self, ability: Ability, is_critical: bool) -> int:
        return self.calculate_damage(self.champion, self.challenger, ability, is_critical)
