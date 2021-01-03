from classes.chicken import Chicken
from classes.ability import Ability
import random

type_chart = {
    "normal": {"normal": 0.0, "fire": 0.0, "ice": 0.0, "air": 0.0, "earth": 0.0, "electric": 0.0, "water": 0.0},
    "fire": {"normal": 0.0, "fire": 0.0, "ice": 0.5, "air": 0.0, "earth": 0.0, "electric": 0.0, "water": -0.5},
    "ice": {"normal": 0.0, "fire": -0.5, "ice": 0.0, "air": 0.5, "earth": 0.0, "electric": 0.0, "water": 0.0},
    "air": {"normal": 0.0, "fire": 0.0, "ice": -0.5, "air": 0.0, "earth": 0.5, "electric": 0.0, "water": 0.0},
    "earth": {"normal": 0.0, "fire": 0.0, "ice": 0.0, "air": -0.5, "earth": 0.0, "electric": 0.5, "water": 0.0},
    "electric": {"normal": 0.0, "fire": 0.0, "ice": 0.0, "air": 0.0, "earth": -0.5, "electric": 0.0, "water": 0.5},
    "water": {"normal": 0.0, "fire": 0.5, "ice": 0.0, "air": 0.0, "earth": 0.0, "electric": -0.5, "water": 0.0}}


class Battle:
    def __init__(self, challenger: Chicken, champion: Chicken):
        self.challenger = challenger
        self.champion = champion

    @staticmethod
    def is_miss(ability: Ability) -> bool:
        if random.random() <= ability.accuracy / 100:
            return False
        return True

    @staticmethod
    def is_critical(attacker: Chicken) -> bool:
        return random.random() <= max(1, attacker.luck) / 200

    @staticmethod
    def effectiveness(ability: Ability, defender: Chicken) -> float:
        return 1 + type_chart[ability.type][defender.type]

    @staticmethod
    def inflicts_effect(ability: Ability, defender: Chicken) -> bool:
        if ability.effect is not None:
            if random.random() <= ability.effect.infliction / 100:  # 30% chance of inflicting status effect
                defender.status = ability.effect
                return True
        return False

    @staticmethod
    def is_affected(attacker: Chicken):
        if attacker.status is not None:
            return attacker.status.does_affect()

    def calculate_damage(self, attacker: Chicken, defender: Chicken, ability: Ability, is_critical: bool) -> int:
        luck = (random.randint(85 + attacker.luck, 100 + attacker.luck) / 100)
        print(f"Luck: {luck}")
        modifier = (is_critical + 1) * self.effectiveness(ability, defender)
        print(f"Modifier: {modifier}")
        base = (((2 * attacker.level / 5 + 2) * ability.power * (attacker.strength / defender.defense)) / 50) + 2
        print(f"Base: {base}")
        damage = max(1, round(base * modifier * luck))
        print(f"Damage: {base * modifier * luck} -> {damage}")
        return damage

    def evaluate(self, attacker: Chicken, ability: Ability):
        defender = self.champion if attacker == self.challenger else self.challenger

        # Check for status effect
        if attacker.status is not None:
            if attacker.status.precedes:  # Check if status effect takes precedence
                if attacker.status.negates:  # Check if status effect can negate attacks
                    if attacker.status.does_affect():  # Check if status negates this attack
                        pass  # TODO: implement response for negated attack
                else:
                    pass  # TODO: a status.evaluate() function

        # Check for effectiveness of attack
        effectiveness = self.effectiveness(ability, defender)
        if effectiveness > 1:
            pass  # TODO: implement response for effective attack
        elif effectiveness < 1:
            pass  # TODO: implement response for ineffective attack

        # Check if attack is critical
        critical = self.is_critical(attacker)
        if critical:
            pass  # TODO: implement response for critical attack

        damage = self.calculate_damage(attacker, defender, ability, critical)
