class Vertex:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Vertex({self.name})"


class Graph:
    def __init__(self):
        self.vertices = {}

    def add(self, vertex: Vertex) -> bool:
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
            return True
        return False

    def connect(self, vertex: Vertex, neighbor: Vertex) -> bool:
        if vertex in self.vertices and neighbor in self.vertices:
            self.vertices[vertex].add(neighbor)
            self.vertices[neighbor].add(vertex)
            return True
        return False

    def neighbors(self, vertex: Vertex):
        return self.vertices[vertex]

    def display(self):
        for vertex in self.vertices:
            print(f"{vertex.name}: {[neighbor.name for neighbor in self.vertices[vertex]]}")

    def get(self, name: str):
        vertices = self.vertices.keys()
        for vertex in vertices:
            if vertex.name == name:
                return vertex
        return None

    def __len__(self):
        return len(self.vertices)

