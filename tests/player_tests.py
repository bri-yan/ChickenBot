import unittest
from classes.player import Player
import library.world as world


class PlayerTests(unittest.TestCase):
    def test_player_location(self):
        player = Player(None, world.white_rock)
        self.assertEqual(player.location, world.white_rock)

    def test_player_locate(self):
        player = Player(None, world.white_rock)
        self.assertEqual(player.locate(), "White Rock")

    def test_player_search(self):
        player = Player(None, world.white_rock)
        self.assertEqual(player.search(), ["Surrey"])

    def test_player_travel_1(self):
        player = Player(None, world.white_rock)
        self.assertFalse(player.travel("Burnaby"))

    def test_player_travel_2(self):
        player = Player(None, world.white_rock)
        self.assertTrue(player.travel("Surrey"))
        self.assertEqual(player.location, world.surrey)
