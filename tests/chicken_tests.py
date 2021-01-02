import unittest
from classes.chicken import Chicken

test_chicken = Chicken("Test Chicken")
test_chicken.max_health = 50
test_chicken.health = test_chicken.max_health


class ChickenTests(unittest.TestCase):
    def test_reduce_health_1(self):
        test_chicken.reduce_health(5)
        self.assertEqual(45, test_chicken.health)

    def test_reduce_health_2(self):
        test_chicken.reduce_health(50)
        self.assertEqual(0, test_chicken.health)

    def test_reduce_health_3(self):
        test_chicken.reduce_health(51)
        self.assertEqual(0, test_chicken.health)


if __name__ == '__main__':
    unittest.main()
