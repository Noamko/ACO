from Graphs import generate_clique
from aco import AcoTsp
import random


nodes = [(float("%.2f" % random.uniform(-200,200)), float("%.2f" % random.uniform(-200,200))) for i in range(10)]
g = generate_clique(10, AcoTsp.AcoEdge, nodes)

acs = AcoTsp(g, 12)
acs.run(g.nodes[0])
