from classes.graph import Vertex
from classes.graph import Graph

white_rock = Vertex("White Rock")
surrey = Vertex("Surrey")
delta = Vertex("Delta")
new_west = Vertex("New West")
coquitlam = Vertex("Coquitlam")
burnaby = Vertex("Burnaby")
richmond = Vertex("Richmond")
vancouver = Vertex("Vancouver")
north_vancouver = Vertex("North Vancouver")

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
world.connect(delta, burnaby)
world.connect(surrey, new_west)
world.connect(new_west, coquitlam)
world.connect(burnaby, new_west)
world.connect(richmond, burnaby)
world.connect(burnaby, vancouver)
world.connect(richmond, vancouver)
world.connect(vancouver, north_vancouver)



