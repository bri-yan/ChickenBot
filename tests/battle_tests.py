import unittest
import random
from classes.battle import Battle
from classes.chicken import Chicken
from classes.ability import Ability

test_ability = Ability("Test Ability", "normal", 100)

test_chicken = Chicken("Test Chicken")
test_chicken.health = test_chicken.max_health
test_chicken.level = 5
test_chicken.abilities.append(test_ability)


class BattleTests(unittest.TestCase):
    def test_calculate_damage_1(self):
        expected_damage = int((((2 * test_chicken.level / 5 + 2) * test_ability.power *
                                (test_chicken.strength / test_chicken.defense)) / 50) + 2)
        actual_damage = Battle.calculate_damage(test_chicken, test_chicken, test_ability, is_critical=False)
        print(actual_damage)
        self.assertLessEqual(actual_damage, expected_damage)
        self.assertGreaterEqual(actual_damage, int(expected_damage * 0.85))


if __name__ == '__main__':
    unittest.main()
