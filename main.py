from Graphs import generate_clique
import numpy as np
from tests.Test1 import test as test1
from tests.Test2 import test as test2
from Aco import AcoTsp
import sys

if __name__ == "__main__":
    GRAPH_SIZE = 30
    min_point_value = -200
    max_point_values = 200

    print(f"Generating Graph with size: {GRAPH_SIZE}")
    nodes = [(float("%.2f" % np.random.uniform(min_point_value,max_point_values)),
              float("%.2f" % np.random.uniform(min_point_value,max_point_values))) for i in range(GRAPH_SIZE)]
    g = generate_clique(len(nodes), AcoTsp.AcoEdge, nodes)
    # Uncomment this to use the vertices that was used for the tests showed in the project
    # nodes = [(123.04, -129.27), (124.4, -188.9), (-20.26, 54.79), (15.03, -160.71), (-45.81, 2.47), (-142.52, 84.35),
    #          (187.83, 93.37), (-146.26, 89.6), (-60.64, -44.3), (103.03, 150.06), (164.27, -82.86), (-81.15, 43.23),
    #          (68.98, 3.33), (-57.0, 136.38), (-196.74, -77.47), (83.08, -187.65), (13.35, 161.51), (-98.33, 115.91),
    #          (78.93, -129.1), (139.22, 1.84)]

    # TEST 1:
    # Colony Size: the amount of ants to use
    # iter: iterations (default = 300)
    # func: available functions (acs, elitist, minmax)
    # plot: set to true if you want to popup a plot (default is true)
    # save_file: set to true if you want to save the plot to a file (default is true)
        
    # TEST 2: (this test migh take along time to run
    # so to get fast result use a small amount of iterations and max_ant

    # max ants: check until max ant is reached
    # iter: iterations (default = 20) it
    # func: available functions (acs, elitist, minmax)
    # plot: set to true if you want to popup a plot (default is true)
    # save_file: set to true if you want to save the plot to a file (default is true)

    if len(sys.argv) == 3:
        if sys.argv[1] in ["t1","test1"]:
            if sys.argv[2] in ['acs', 'elitist','minmax']:
                test1(graph=g, colony_size=10, iterations=100, func=sys.argv[2], plot=False, save_file=True)

        elif sys.argv[1] in ["t2", "test2"]:
            if sys.argv[2] in ['acs', 'elitist','minmax']:
                test2(graph=g, iterations=10,  func=sys.argv[2], max_ants=5, plot=False, save_file=True)

    elif (len(sys.argv) == 2):
        if sys.argv[1] in ['acs', 'elitist','minmax']:
            test1(graph=g, colony_size=10, iterations=100, func=sys.argv[1], plot=False, save_file=True)
    
    else:
        print("error: please provide and test number (optional) ACO funtion (required)")
        print("example: 'python3 main.py test1 elitist'")
