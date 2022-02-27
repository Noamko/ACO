from matplotlib import pyplot as plt
from Graphs import generate_clique
from aco import AcoTsp
import numpy as np
import SimulatedAnnealing


def test(graph, colony_size=5, steps=300, func="acs"):
    # run acs
    aco = AcoTsp(graph=graph, colony_size=colony_size)
    if str(func).lower() == "acs":
        func = aco.acs
    elif str(func).lower() == "elitist":
        func = aco.elitist
    elif str(func).lower() == "minmax":
        func = aco.minmax
    else:
        raise Exception(f"function '{func}' is not supported")
    acs_result = aco.run(start=graph.nodes[0], func=func, steps=steps, test=True)
    best_trip, best_distance = acs_result[-1]

    # run simulated Annealing
    sa_result = SimulatedAnnealing.simulate(graph.nodes, steps=steps)

    # save plot result as image
    for point in graph.as_tuples():
        x_values = [point[0][0], point[1][0]]
        y_values = [point[0][1], point[1][1]]
        plt.plot(x_values, y_values, color='black', linestyle='-', linewidth=3, zorder=1)
        plt.plot(x_values, y_values, color='#453A66', linestyle='-', linewidth=2, zorder=1)

    x = [x[0] for x in best_trip]
    y = [y[1] for y in best_trip]
    plt.plot(x, y, linestyle='-', color='black', linewidth=5, zorder=1)
    plt.plot(x, y, linestyle='-', color='red', linewidth=4, zorder=1)
    plt.scatter(x, y, s=100, zorder=2, color='black')
    plt.scatter(x, y, s=50, zorder=2, color='#E49100')
    # for i, node in enumerate(graph.nodes):
    #     plt.annotate(i,node)
    plt.title(f"Ant Colony {func.__name__.upper()} Solution")
    plt.savefig(f"{func.__name__}_Solution.png")
    plt.close()

    plt.title(f"ACO ({func.__name__.upper()}) vs Simulated Annealing")
    plt.xlabel("Iteration")
    plt.ylabel("Best distance")
    y_values = [d[1] for d in acs_result]
    x_values = range(steps)
    plt.plot(x_values, y_values)
    x_values = range(steps)
    y_values = [d for d in sa_result]
    plt.plot(x_values, y_values)
    plt.legend(["ACS", "SA"])
    plt.savefig(f"{func.__name__.upper()}_vs_SA.png")


def test2(graph, steps=100, func="acs", max_ants=10):
    result = []
    for i in range(1, max_ants):
        avg = 0
        print(f"\n\nGetting data for ant count: {i}")
        for m in range(10):
            print("###", end="", flush=True)
            aco = AcoTsp(graph=graph, colony_size=i)
            if str(func).lower() == "acs":
                acs_result = aco.run(start=graph.nodes[0], func=aco.acs, steps=steps, test=True)
            elif str(func).lower() == "elitist":
                acs_result = aco.run(start=graph.nodes[0], func=aco.elitist, steps=steps, test=True)
            elif str(func).lower() == "minmax":
                acs_result = aco.run(start=graph.nodes[0], func=aco.minmax, steps=steps, test=True)
            else:
                raise Exception(f"function '{func}' is not supported")
            best_trip, best_distance = acs_result[-1]
            avg += best_distance
        avg /= 10
        result.append(avg)

    x = range(1, max_ants)
    y = [y for y in result]
    plt.title(f"{func.upper()} Ant Count Test")
    plt.xlabel("Ant Count")
    plt.ylabel("Average best distance")
    plt.plot(x, y)
    plt.savefig(f"{func}_Ant_count_test")

GRAPH_SIZE = 30

min_point_value = -200
max_point_values = 200
#
# nodes = [(float("%.2f" % np.random.uniform(min_point_value,max_point_values)),
#           float("%.2f" % np.random.uniform(min_point_value,max_point_values))) for i in range(GRAPH_SIZE)]

nodes = [(123.04, -129.27), (124.4, -188.9), (-20.26, 54.79), (15.03, -160.71), (-45.81, 2.47), (-142.52, 84.35),
         (187.83, 93.37), (-146.26, 89.6), (-60.64, -44.3), (103.03, 150.06), (164.27, -82.86), (-81.15, 43.23),
         (68.98, 3.33), (-57.0, 136.38), (-196.74, -77.47), (83.08, -187.65), (13.35, 161.51), (-98.33, 115.91),
         (78.93, -129.1), (139.22, 1.84)]
g = generate_clique(len(nodes), AcoTsp.AcoEdge, nodes)

# test(g, 10, steps=300, func="minmax")
test2(g, func="minmax", max_ants=20)
# plt.show()
