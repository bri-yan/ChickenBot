import unittest
from classes.graph import Graph


class ChickenTests(unittest.TestCase):
    def test_graph_add_1(self):
        graph = Graph(2)
        len(graph)