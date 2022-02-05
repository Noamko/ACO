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
            return self.neighbors

        def neighborsCount(self):
            return len(self.neighbors)

    class Edge:
        def __init__(self, a, b, cost = 0) -> None:
            if not isinstance(a, Graph.Node) or not isinstance(b, Graph.Node):
                raise Exception("error: Can't initiate Edge witn none Graph.Node")
            self.a = a
            self.b = b
            self.cost = cost
            self.a.neighbors.append(self.b)
            self.b.neighbors.append(self.a)

        def __eq__(self, __o: object) -> bool:
            return (__o.a == self.a and __o.b == self.b) or (__o.b == self.a and __o.a == self.b)

        def __str__(self) -> str:
            return f"{self.a} ---{self.cost}--- {self.b}"
    
    def __init__(self, nodes = [], edges = []) -> None:
        self.edges = edges
        self.nodes = nodes
        self.nodeMap = {}
        for n in self.nodes:
            self.nodeMap[n.id] = n

    def __str__(self) -> str:
        a = ""
        for e in self.edges:
            a += str(e) + "\n"
        return str(a)

    def getNodeById(self, id):
        return self.nodeMap[id]
    
    def nodeCount(self):
        return len(self.nodes)

class DirectedGraph(Graph):
    class Edge(Graph.Edge):
        def __init__(self, a, b, cost) -> None:
            super().__init__(a, b, cost)
            self.b.neighbors.remove(self.a) # pretty ugly but ok

        def init_neighbors(self):
            self.a.neighbors.append(self.b)
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
            e = self.Edge(n, self.nodes[random.randint(0, size -1)],random.randint(mincost, maxcost))
            if e.a != e.b and e not in self.edges:
                e.a.neighbors.append(e.b)
                self.edges.append(e)

class Tree(Graph):
    pass # TODO

def generate(size = 10, mincost = 1, maxcost = 100, type = "none"):
    nodes = []
    edges = []
    for i in range(size):
        nodes.append(Graph.Node(i))

    for n in nodes:
        if type == "none":
            e = Graph.Edge(n, nodes[random.randint(0, size -1)],random.randint(mincost, maxcost))
            if e.a != e.b and e not in edges:
                e.a.neighbors.append(e.b)
                e.b.neighbors.append(e.a)
                edges.append(e)

        elif type == "directed":
            e = DirectedGraph.Edge(n, nodes[random.randint(0, size -1)],random.randint(mincost, maxcost))
            if e.a != e.b and e not in edges:
                e.a.neighbors.append(e.b)
                edges.append(e)

    return Graph(edges, nodes)