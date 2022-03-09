from matplotlib import pyplot as plt
from Graphs import generate_clique
from aco import AcoTsp
import numpy as np
import SimulatedAnnealing


def test(graph, iterations=10, func="acs", max_ants=10, save_file=True, plot=False):
    plt.cla()
    print("Running test 2 please wait...")
    result = []
    for i in range(1, max_ants):
        avg = 0
        print(f"\n\nGetting data for ant count: {i}")
        for m in range(10):
            print("###", end="", flush=True)
            aco = AcoTsp(graph=graph, colony_size=i)
            if str(func).lower() == "acs":
                aco_result = aco.run(start=graph.nodes[0], func=aco.acs, iter=iterations, test=True)
            elif str(func).lower() == "elitist":
                aco_result = aco.run(start=graph.nodes[0], func=aco.elitist, iter=iterations, test=True)
            elif str(func).lower() == "minmax":
                aco_result = aco.run(start=graph.nodes[0], func=aco.minmax, iter=iterations, test=True)
            else:
                raise Exception(f"function '{func}' is not supported")
            best_trip, best_distance = aco_result[-1]
            avg += best_distance
        avg /= 10
        result.append(avg)

    x = range(1, max_ants)
    y = [y for y in result]
    plt.title(f"{func.upper()} Ant Count Test")
    plt.xlabel("Ant Count")
    plt.ylabel("Average best distance")
    plt.plot(x, y)
    if save_file:
        plt.savefig(f"{func}_Ant_count_test")
        print(f"image saved: {func}_Ant_count_test")
    if plot:
        plt.show()




ilm = ['I', ' ','L','o','v','e',' ','M','a','m','i']
def ilovemami(x):
    print(x)
    ilovemami(ilm[(x+1) % len(ilm)])