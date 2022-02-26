import random
import numpy as np


class Graph:
    class Edge:
        def __init__(self, a, b, cost=0.0) -> None:
            self.a = a
            self.b = b
            self.cost = cost

        def __eq__(self, __o: object) -> bool:
            return (__o.a == self.a and __o.b == self.b) or (__o.b == self.a and __o.a == self.b)

        def __str__(self) -> str:
            return f"{self.a} ---{self.cost}--- {self.b}"

        def __hash__(self):
            return (self.a, self.b).__hash__()

    def __init__(self, nodes=None, edges=None) -> None:
        if nodes is None:
            nodes = []
        if edges is None:
            edges = []
        self.edges = edges
        self.nodes = nodes
        self.nodeMap = {}
        self.edgeMap = {}

        for e in self.edges:
            self.edgeMap[(e.a, e.b)] = e
            if len(nodes) == 0:
                if e.a not in self.nodes:
                    self.nodes.append(e.a)
                if e.b not in self.nodes:
                    self.nodes.append(e.b)

    def __str__(self) -> str:
        a = ""
        for e in self.edges:
            a += str(e) + "\n"
        return str(a)

    def get_edge(self, a, b) -> Edge:
        edge = (a, b) if (a, b) in self.edgeMap else (b, a)
        return self.edgeMap[edge]

    def node_count(self):
        return len(self.nodes)

    def as_tuples(self) -> []:
        result = []
        for e in self.edges:
            result.append((e.a, e.b))
        return result


def generate_clique(size=10, edge_type=Graph.Edge, nodes=[]):
    edges = []
    for i in range(size):
        for j in range(i,  size):
            if i != j:
                e = edge_type(nodes[i],nodes[j], float("%.2f" % np.linalg.norm(np.asarray(nodes[i]) - np.asarray(nodes[j]))))
                edges.append(e)
    return Graph(nodes, edges)
