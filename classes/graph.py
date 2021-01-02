class Graph:
    def __init__(self, size):
        self.size = size
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])

    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print(f"No edge between {v1} and {v2}")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size
