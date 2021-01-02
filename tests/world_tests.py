import unittest
from classes.graph import Vertex
from classes.graph import Graph


class WorldTests(unittest.TestCase):
    def test_graph_add_1(self):
        graph = Graph()
        test = Vertex("Test")
        graph.add(test)
        self.assertTrue(test in graph.vertices)

    def test_graph_connect_1(self):
        graph = Graph()
        first = Vertex("First")
        graph.add(first)
        second = Vertex("Second")
        graph.add(second)
        graph.connect(first, second)
        graph.display()
        self.assertTrue(second in graph.neighbors(first) and first in graph.neighbors(second))

    def test_world_1(self):
        class City(Vertex):
            def __init__(self, name: str):
                super().__init__(name)

        white_rock = City("White Rock")
        surrey = City("Surrey")
        delta = City("Delta")
        new_west = City("New West")
        coquitlam = City("Coquitlam")
        burnaby = City("Burnaby")
        richmond = City("Richmond")
        vancouver = City("Vancouver")
        north_vancouver = City("North Vancouver")

        world = Graph()

        world.add(white_rock)
        world.add(surrey)
        world.add(delta)
        world.add(new_west)
        world.add(coquitlam)
        world.add(burnaby)
        world.add(richmond)
        world.add(vancouver)
        world.add(north_vancouver)

        world.connect(white_rock, surrey)
        world.connect(surrey, delta)
        world.connect(surrey, new_west)
        world.connect(new_west, coquitlam)
        world.connect(burnaby, new_west)
        world.connect(richmond, burnaby)
        world.connect(burnaby, vancouver)
        world.connect(richmond, vancouver)
        world.connect(vancouver, north_vancouver)

        world.display()
