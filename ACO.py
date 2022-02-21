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
            for unvisited_node in unvisited:
                total += (1 / self.graph.get_edge(self.trip[-1], unvisited_node).cost) ** self.beta * \
                         self.graph.get_edge(self.trip[-1], unvisited_node).pheromone ** self.alpha

            probs = []
            for unvisited_node in unvisited:
                probs.append((self.graph.get_edge(self.trip[-1], unvisited_node).pheromone ** self.alpha *
                              (1 / self.graph.get_edge(self.trip[-1], unvisited_node).cost) ** self.beta) / total)

            selected_index = np.random.choice(len(unvisited), p=probs)
            return unvisited[selected_index]

        def find_path(self, start):
            self.trip = [start]
            while len(self.trip) != len(self.graph.nodes):
                self.trip.append(self.select_edge())
            return self.trip

        def get_distance(self):
            distance = 0
            prev = None
            for node in self.trip:
                if prev is not None:
                    distance += self.graph.get_edge(prev, node).cost
                prev = node
            distance += self.graph.get_edge(self.trip[-1], self.trip[0]).cost
            return distance

    def __init__(self, graph: Graph, colony_size: int) -> None:
        self.graph = graph
        self.colony_size = colony_size
        self.steps = 200
        self.ants = [self.Ant(1, 3, self.graph) for _ in range(self.colony_size)]
        self.rho = 0.1
        self.pheromone_deposit_weight = 1
        self.bestDistance = float("inf")
        self.bestTrip = None

    def add_pheromones(self, trip, distance_covered):
        pheromones = self.pheromone_deposit_weight / distance_covered
        for i in range(self.graph.node_count()):
            self.graph.get_edge(trip[i], trip[(i + 1) % self.graph.node_count()]).pheromone += pheromones

    # ACS
    def run(self, start):
        for step in range(self.steps):
            for ant in self.ants:
                path = ant.find_path(start)
                ant_distance_traveled = ant.get_distance()
                if ant_distance_traveled < self.bestDistance:
                    self.bestTrip = path
                    self.bestDistance = ant_distance_traveled
                    self.add_pheromones(path, ant_distance_traveled)
                    print(self.bestDistance)

            # evaporate pheromones
            for edge in self.graph.edges:
                edge.pheromone *= (1 - self.rho)
        return self.bestTrip, self.bestDistance
