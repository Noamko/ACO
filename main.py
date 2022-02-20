from Graphs import Graph
from aco import AcoTsp

# create a fully connected graph
roads = [AcoTsp.AcoEdge("Tel Aviv", "Kfar Saba", 30),
         AcoTsp.AcoEdge("Tel Aviv", "Eilat", 400),
         AcoTsp.AcoEdge("Tel Aviv", "Haifa", 100),
         AcoTsp.AcoEdge("Tel Aviv", "Beer Sheva", 150),
         AcoTsp.AcoEdge("Kfar Saba", "Eilat", 450),
         AcoTsp.AcoEdge("Kfar Saba", "Haifa", 80),
         AcoTsp.AcoEdge("Kfar Saba", "Beer Sheva", 180),
         AcoTsp.AcoEdge("Eilat", "Beer Sheva", 200),
         AcoTsp.AcoEdge("Eilat", "Haifa", 620),
         AcoTsp.AcoEdge("Haifa", "Beer Sheva", 580)]

israel = Graph(edges=roads)
aco = AcoTsp(israel, 100)
aco.run("Tel Aviv")
