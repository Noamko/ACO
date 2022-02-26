from matplotlib import pyplot as plt
from Graphs import generate_clique
from aco import AcoTsp
import numpy as np
import SimulatedAnnealing
import random
import math

GRAPH_SIZE = 10
min_point_value = -1000
max_point_values = 1000
nodes = [(float("%.2f" % np.random.uniform(min_point_value,max_point_values)),
          float("%.2f" % np.random.uniform(min_point_value,max_point_values))) for i in range(GRAPH_SIZE)]

# nodes = [(40.62, 71.88), (78.18, 67.47), (88.84, 87.73), (92.52, 43.22), (87.87, 44.35), (8.37, 39.66), (51.08, 72.72),
#          (25.6, 89.43), (47.56, 10.5), (75.95, 55.92), (94.77, 83.64), (64.75, 93.54), (33.95, 32.8), (58.27, 13.02),
#          (80.72, 51.24), (88.01, 69.66), (4.59, 77.41), (30.67, 36.86), (62.96, 52.48), (12.67, 40.22), (60.94, 56.78),
#          (25.92, 21.49), (64.11, 73.94), (14.66, 67.67), (94.46, 98.27), (55.93, 73.44), (62.0, 6.38), (4.3, 8.65),
#          (20.01, 32.52), (64.87, 72.76)]
g = generate_clique(len(nodes), AcoTsp.AcoEdge, nodes)
x = [x[0] for x in g.as_tuples()]
y = [y[1] for y in g.as_tuples()]
for point in g.as_tuples():
    x_values = [point[0][0], point[1][0]]
    y_vales = [point[0][1], point[1][1]]
    plt.plot(x_values, y_vales, 'bo', linestyle='-')
# plt.scatter(x,y)
def test_acs(graph, colony_size):
    aco = AcoTsp(graph=graph, colony_size=colony_size)
    result = aco.run(start=graph.nodes[0], func=aco.acs, test=True)
    for i, res in enumerate(result):
        print(f'{i}: {res[1]}')
    best, d = result[-1]

    x = [x[0] for x in best]
    y = [y[1] for y in best]
    plt.plot(x,y , linestyle='-', color='red', linewidth=3)



test_acs(g, 1)
plt.show()
