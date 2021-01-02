import unittest
import random
from classes.battle import Battle
from classes.chicken import Chicken
from classes.ability import Ability

test_ability = Ability("Test Ability", "normal", 40, 100)

test_chicken = Chicken("Test Chicken")
test_chicken.health = test_chicken.max_health
test_chicken.level = 5
test_chicken.abilities.append(test_ability)
test_chicken.type = "normal"

test_dummy = Chicken("Dummy")
test_chicken.health = test_chicken.max_health
test_chicken.level = 5
test_chicken.type = "normal"


class BattleTests(unittest.TestCase):
    def test_calculate_damage_1(self):
        battle = Battle(test_chicken, test_chicken)
        expected_damage = int((((2 * test_chicken.level / 5 + 2) * test_ability.power *
                                (test_chicken.strength / test_chicken.defense)) / 50) + 2)
        actual_damage = battle.calculate_damage(test_chicken, test_chicken, test_ability, is_critical=False)
        #self.assertLessEqual(actual_damage, expected_damage)
        #self.assertGreaterEqual(actual_damage, int(expected_damage * 0.85))


if __name__ == '__main__':
    unittest.main()
