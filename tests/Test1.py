from matplotlib import pyplot as plt
from Aco import AcoTsp
import SimulatedAnnealing


def test(graph, colony_size=5, iterations=300, func="acs", save_file=True, plot=True):
    plt.cla()
    print("Running test 1 please wait...")
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
    acs_result = aco.run(start=graph.nodes[0], func=func, iter=iterations, test=True)
    best_trip, best_distance = acs_result[-1]

    # run simulated Annealing
    sa_result = SimulatedAnnealing.simulate(graph.nodes, iter=iterations)

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
    print(f"image saved: {func.__name__}_Solution.png")
    plt.close()

    plt.title(f"ACO ({func.__name__.upper()}) vs Simulated Annealing")
    plt.xlabel("Iteration")
    plt.ylabel("Best distance")
    y_values = [d[1] for d in acs_result]
    x_values = range(iterations)
    plt.plot(x_values, y_values)
    x_values = range(iterations)
    y_values = [d for d in sa_result]
    plt.plot(x_values, y_values)
    plt.legend(["ACS", "SA"])
    if save_file:
        plt.savefig(f"{func.__name__.upper()}_vs_SA.png")
        print(f"image saved: {func.__name__.upper()}_vs_SA.png")
    if plot:
        plt.show()
