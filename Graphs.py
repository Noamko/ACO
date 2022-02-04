import random 

class Graph:
    class Node:
        def __init__(self, id) -> None:
            self.id = id
            self.neighbors = []

        def __eq__(self, __o: object) -> bool:
            return __o.id == self.id

        def __str__(self) -> str:
            return str(self.id)

        def getNeighbors(self) -> list:
            return self.neighbors.copy()

    class Edge:
        def __init__(self, a, b, cost, g) -> None:
            self.a = a
            self.b = b
            self.g = g
            self.cost = cost
            self.type = type

            if g.type == "none":
                self.a.neighbors.append(b)
                self.b.neighbors.append(a)
            elif self.g.type  =="directed":
                self.a.neighbors.append(b)

        def __eq__(self, __o: object) -> bool:
            if self.type == "none":
                return (__o.a == self.a and __o.b == self.b) or (__o.b == self.a and __o.a == self.b)
            elif self.type == "directed":
                return (__o.a == self.a and __o.b == self.b)

        def __str__(self) -> str:
            if self.g.type == "none":
                return f"{self.a} ----- {self.b}"

            elif self.g.type == "directed":
                return f"{self.a} ----> {self.b}"

    def __init__(self, edges = [], nodes = [], type = "none") -> None:
        self.edges = edges
        self.nodes = nodes
        self.type = type

    def __str__(self) -> str:
        a = ""
        if self.type == "none":
            for e in self.edges:
                a += str(e) + "\n"
        elif self.type == "directed":
            for e in self.edges:
                a += str(e) + "\n"
        return str(a)

    def generate(self, size = 10, mincost = 1, maxcost = 1):
        for i in range(size):
            self.nodes.append(self.Node(i))

        for n in self.nodes:
            e = self.Edge(n, self.nodes[random.randint(0, size -1)],random.randint(mincost, maxcost), self)
            if e.a != e.b and e not in self.edges:
                self.edges.append(e)
            





