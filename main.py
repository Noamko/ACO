from matplotlib import pyplot as plt
from Graphs import generate_clique
from aco import AcoTsp
import random


min_point_value = 0
max_point_values = 100
nodes = [(float("%.2f" % random.uniform(min_point_value,max_point_values)), float("%.2f" % random.uniform(min_point_value,max_point_values))) for i in range(10)]
g = generate_clique(10, AcoTsp.AcoEdge, nodes)

acs = AcoTsp(g, 12)
p,d = acs.run(g.nodes[0],acs.acs)

print(p)

