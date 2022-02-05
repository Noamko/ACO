
from Graphs import Graph
import random

class Ant:

    def chooseEdge():
        pass

# the  graph is fully connected so we assume we wont get stuck
def get_random_loop_Path(start, graph):
    visited = []
    current = start
    while len(visited) != graph.nodeCount():
        c = current.getNeighbors()[random.randint(0, current.neighborsCount() -1)]
        if c.id not in visited:
            current = c
            visited.append(c.id)
    return visited

# create a fully connected graph
cities = [Graph.Node("Tel Aviv"), 
Graph.Node("Kfar Saba"),
Graph.Node("Eilat"),
Graph.Node("Haifa"),
Graph.Node("Beer Sheva")]

roads = [Graph.Edge(cities[0], cities[1], 30),
 Graph.Edge(cities[0], cities[2], 400),
 Graph.Edge(cities[0], cities[3], 100),
 Graph.Edge(cities[0], cities[4], 150),
 Graph.Edge(cities[1], cities[2], 450),
 Graph.Edge(cities[1], cities[3], 80),
 Graph.Edge(cities[1], cities[4], 180),
 Graph.Edge(cities[2], cities[4], 200),
 Graph.Edge(cities[2], cities[3], 620),
 Graph.Edge(cities[3], cities[4], 580)]


israel = Graph(cities, roads)

print(get_random_loop_Path(israel.getNodeById("Tel Aviv"), israel))