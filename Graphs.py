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
        def __init__(self, a, b, cost = 0) -> None:
            self.a = a
            self.b = b
            self.cost = cost

        def __eq__(self, __o: object) -> bool:
            return (__o.a == self.a and __o.b == self.b) or (__o.b == self.a and __o.a == self.b)

        def __str__(self) -> str:
            return f"{self.a} ---{self.cost}--- {self.b}"
        
    def __init__(self, edges = [], nodes = []) -> None:
        self.edges = edges
        self.nodes = nodes
        self.type = type

    def __str__(self) -> str:
        a = ""
        for e in self.edges:
            a += str(e) + "\n"
        return str(a)

    def generate(self, size = 10, mincost = 1, maxcost = 100):
        for i in range(size):
            self.nodes.append(self.Node(i))

        for n in self.nodes:
            e = self.Edge(n, self.nodes[random.randint(0, size -1)],random.randint(mincost, maxcost))
            if e.a != e.b and e not in self.edges:
                e.a.neighbors.append(e.b)
                e.b.neighbors.append(e.a)
                self.edges.append(e)
            

class DirectedGraph(Graph):
    class DirectedEdge(Graph.Edge):
        def __init__(self, a, b, cost) -> None:
            super().__init__(a, b, cost)

        def __str__(self) -> str:
            return f"{self.a} --{self.cost}--> {self.b}"
        def __eq__(self, __o: object) -> bool:
            return (__o.a == self.a and __o.b == self.b)

    def __init__(self, edges=[], nodes=[]) -> None:
        super().__init__(edges, nodes)

    def generate(self, size = 10, mincost = 1, maxcost = 100):
        for i in range(size):
            self.nodes.append(self.Node(i))

        for n in self.nodes:
            e = self.DirectedEdge(n, self.nodes[random.randint(0, size -1)],random.randint(mincost, maxcost))
            if e.a != e.b and e not in self.edges:
                e.a.neighbors.append(e.b)
                self.edges.append(e)