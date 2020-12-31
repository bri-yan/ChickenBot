from classes import ability
from classes import chicken
import random


class Battle:
    def __init__(self, challenger: chicken, champion: chicken):
        self.challenger = challenger
        self.champion = champion

    @staticmethod
    def is_critical(attacker: chicken) -> bool:
        return random.random() <= attacker.luck / 200

    @staticmethod
    def calculate_damage(attacker: chicken, defender: chicken, ability: ability, is_critical: bool) -> int:
        modifier = (random.randint(85 + attacker.luck, 100 + attacker.luck) / 100) * (is_critical + 1)
        base = (((2 * attacker.level / 5 + 2) * ability.power * (attacker.strength / defender.defense)) / 50) + 2
        damage = int(base * modifier)
        return damage

    def challenger_attack(self, ability: ability, is_critical: bool) -> int:
        return self.calculate_damage(self.challenger, self.champion, ability, is_critical)

    def champion_attack(self, ability: ability, is_critical: bool) -> int:
        return self.calculate_damage(self.champion, self.challenger, ability, is_critical)
