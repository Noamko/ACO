import random
class Graph:
    class Edge:
        def __init__(self, a, b, cost = 0) -> None:
            self.a = a
            self.b = b
            self.cost = cost

        def __eq__(self, __o: object) -> bool:
            return (__o.a == self.a and __o.b == self.b) or (__o.b == self.a and __o.a == self.b)

        def __str__(self) -> str:
            return f"{self.a} ---{self.cost}--- {self.b}"
    
    def __init__(self, nodes=[], edges=[]) -> None:
        self.edges = edges
        self.nodes = nodes
        self.nodeMap = {}
        self.edgeMap = {}
        self.neighborLists = {}

        for n in self.nodes:
            self.nodeMap[n] = n

        for e in self.edges:
            self.edgeMap[(e.a, e.b)] = e

            if e.a in self.neighborLists:
                self.neighborLists[e.a].append(e.b)
            else: self.neighborLists[e.a] = [e.b]

            if e.b in self.neighborLists:
                self.neighborLists[e.b].append(e.a)
            else: self.neighborLists[e.a] = [e.a]

    def __str__(self) -> str:
        a = ""
        for e in self.edges:
            a += str(e) + "\n"
        return str(a)

    def getEdge(self, a, b) -> Edge:
        edge = (a, b) if (a, b) in self.edgeMap else (b, a)
        return self.edgeMap[edge]
    
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