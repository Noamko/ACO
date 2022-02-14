from Graphs import Graph
import numpy as np


class AcoTsp:
    # we just use
    class AcoEdge(Graph.Edge):
        def __init__(self, a, b, cost=0) -> None:
            super().__init__(a, b, cost)
            self.pheromone = 1

    class Ant:
        def __init__(self, alpha, beta, graph: Graph) -> None:
            self.graph = graph
            self.trip = None
            self.alpha = alpha
            self.beta = beta

        def select_edge(self):
            # we are in self.trip[-1]
            unvisited = [node for node in self.graph.nodes if node not in self.trip]

            total = 0.0
            for unode in unvisited:
                total += (1 / self.graph.getEdge(self.trip[-1], unode).cost) ** self.beta * \
                         (self.graph.getEdge(self.trip[-1], unode).pheromone) ** self.alpha

            probs = []
            for unode in unvisited:
                probs.append((self.graph.getEdge(self.trip[-1], unode).pheromone ** self.alpha *
                              (1 / self.graph.getEdge(self.trip[-1], unode).cost) ** self.beta) / total)

            return np.random.choice(unvisited, 1, p=probs)[0]

        def find_path(self, start):
            self.trip = [start]
            distance = 0
            while len(self.trip) != len(self.graph.nodes):
                nxt = self.select_edge()
                d = self.graph.getEdge(self.trip[-1], nxt).cost
                distance += d
                print((self.trip[-1], nxt), distance)
                self.trip.append(self.select_edge())
            return self.trip, distance

    def __init__(self, graph: Graph, colony_size: int) -> None:
        self.graph = graph
        self.colony_size = colony_size
        self.steps = 100
        self.ants = [self.Ant(1, 3, self.graph) for _ in range(self.colony_size)]
        self.rho = 0.1
        self.pheromone_deposit_weight = 1
        self.bestDistance = float("inf")
        self.bestTrip = None

    def addPheromones(self, trip, distanceCovered):
        pheromones = self.pheromone_deposit_weight / distanceCovered
        for i in range(self.graph.nodeCount()):
            self.graph.getEdge(trip[i], trip[(i + 1) % self.graph.nodeCount()]).pheromone += pheromones

    # ACS
    def run(self, start):
        for step in range(self.steps):
            for ant in self.ants:
                path = ant.find_path(start)
                if path[1] < self.bestDistance:
                    self.bestTrip = path[0]
                    self.bestDistance = path[1]
                    self.addPheromones(path[0], path[1])

            # evapurate pheromones
            for edge in self.graph.edges:
                edge.pheromone *= (1 - self.rho)
        print((self.bestTrip, self.bestDistance))  # bugs..4
