from Graphs import Graph
import numpy as np


class AcoTsp:
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
            self.trip.append(start)     # we add the first node to complete a full circle
            return self.trip

        def get_distance(self):
            distance = 0
            prev = None
            for node in self.trip:
                if prev is not None:
                    distance += self.graph.get_edge(prev, node).cost
                prev = node
            return distance

    def __init__(self, graph: Graph, colony_size: int) -> None:
        self.graph = graph
        self.colony_size = colony_size
        self.steps = 100
        self.ants = [self.Ant(1, 3, self.graph) for _ in range(self.colony_size)]
        self.rho = 0.1
        self.pheromone_deposit_weight = 1
        self.bestDistance = float("inf")
        self.bestTrip = None
        self.elitist_weight = 1.0
        self.min_scale_factor = 0.001

    def add_pheromones(self, trip, distance_covered, weight=1.0):
        pheromones = self.pheromone_deposit_weight / distance_covered
        for i in range(self.graph.node_count()):
            self.graph.get_edge(trip[i], trip[(i + 1) % self.graph.node_count()]).pheromone += pheromones * weight

    def acs(self, start, step=None):
        for ant in self.ants:
            path = ant.find_path(start)
            ant_distance_traveled = ant.get_distance()
            if ant_distance_traveled < self.bestDistance:
                self.bestTrip = path
                self.bestDistance = ant_distance_traveled
                self.add_pheromones(path, ant_distance_traveled)

    def elitist(self, start, step):
        self.acs(start,step)
        self.add_pheromones(self.bestTrip, self.bestDistance, weight=self.elitist_weight)

    def minmax(self, start, step):
        current_best_trip = None
        current_best_distance = float("inf")
        for ant in self.ants:
            ant.find_path(start)
            if ant.get_distance() < current_best_distance:
                current_best_trip = ant.trip
                current_best_distance = ant.get_distance()
        if float(step + 1) / float(self.steps) <= 0.75:
            self.add_pheromones(current_best_trip, current_best_distance)
            max_pheromone = self.pheromone_deposit_weight / current_best_distance
        else:
            if current_best_distance < self.bestDistance:
                self.bestTrip = current_best_trip
                self.bestDistance = current_best_distance
            self.add_pheromones(self.bestTrip, self.bestDistance)
            max_pheromone = self.pheromone_deposit_weight / self.bestDistance
        min_pheromone = max_pheromone * self.min_scale_factor
        for edge in self.graph.edges:
            edge.pheromone *= (1 - self.rho)
            if edge.pheromone > max_pheromone:
                edge.pheromone = min_pheromone
            elif edge.pheromone < min_pheromone:
                edge.pheromone = min_pheromone

    # ACS
    def run(self, start, func, test=False):
        result = []
        for step in range(self.steps):
            func(start, step)
            if func.__name__ != "minmax":  # minmax has its own update evaporate rules
                for edge in self.graph.edges:   # evaporate pheromones
                    edge.pheromone *= (1 - self.rho)
            if test:
                result.append((self.bestTrip, self.bestDistance))
        if test:
            return result
        return self.bestTrip, self.bestDistance
